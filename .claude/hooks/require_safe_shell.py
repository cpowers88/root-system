#!/usr/bin/env python3
"""
require_safe_shell.py — PreToolUse gate: bulk/scripted work must run behind the wrapper.

WHY THIS EXISTS
  `AGENT.md` File Safety 12 requires that any operation touching many files in one
  pass run through `00-BRAIN/scripts/safe_shell.sh` — the only OS-level write deny
  in this stack with measured enforcement (flag #96; `verify_controls.py` reports
  the declarative `sandbox` block INERT in both environments).

  Until now that requirement was prose. Nothing checked it. A session that did not
  read item 12, or read it and forgot, ran bulk work unprotected — which is what
  happened on 2026-08-10, when a glob rewrote 2,713 files with neither `88-JOURNAL`
  nor `raw/` excluded, and again on 2026-08-11, when probing `fetch_fred.py` ran it
  and wrote three ECON dataset rows nobody asked for.

  This hook turns item 12 from a sentence into a mechanism.

WHAT IT DOES
  Classifies each `Bash` command. If a segment could touch many files in one pass
  and is NOT launched through `safe_shell.sh`, the call is denied with the exact
  wrapped command to run instead. It is a redirect, not a refusal: the work is
  never blocked, only routed through the wall.

  There is deliberately NO string-based override. Any escape hatch spelled in the
  command would be one an AI could type for itself, which is not a wall. The only
  ways past are the wrapper, or Chris editing this allowlist / disabling the hook
  in `settings.json` — both human acts.

FAIL-CLOSED
  Unparseable input, an unreadable command, or an internal error all DENY. A gate
  that fails open reads as protection in an audit and stops nothing — flag #95's
  failure mode, and the one thing `.claude/CONTROL_INVENTORY.md` exists to prevent.
  A visibly broken gate is recoverable; a silently absent one is not.

CONTRACT
  stdin  : PreToolUse hook JSON (`tool_name`, `tool_input.command`, `cwd`, ...)
  stdout : hookSpecificOutput JSON when a decision is made
  exit 0 : no opinion (command is not bulk work, or is already wrapped)
  exit 2 : blocked

Owner and check moment: re-measured by whoever changes anything under `.claude/`,
and at the monthly review, via `verify_controls.py` from BOTH environments.
"""

import json
import os
import re
import sys

WRAPPER_REL = "00-BRAIN/scripts/safe_shell.sh"

# Interpreters that, handed a script, can do anything the script says.
INTERPRETERS = {
    "python", "python3", "py", "python.exe", "python3.exe",
    "bash", "sh", "zsh", "dash", "ksh",
    "node", "perl", "ruby", "deno", "bun",
    "pwsh", "powershell", "pwsh.exe", "powershell.exe",
}

SCRIPT_EXTS = (".py", ".sh", ".bash", ".zsh", ".js", ".mjs", ".cjs", ".ts", ".pl", ".rb", ".ps1")

# Governed, reviewed vault scripts that do not write to protected paths.
#
# This list is a TRUST ASSERTION, not a measurement. Anything not named here is
# gated by default — new and unreviewed is exactly the fetch_fred.py case. Adding
# a name here is a governance act: it asserts the script has been read and does
# not touch 88-JOURNAL or any raw/ folder.
ALLOWED_SCRIPTS = {
    "root_health.py",           # read-only health gate
    "validate_boot_chain.py",   # read-only: are rules present?
    "verify_controls.py",       # read-only: do rules bite?
    "frontmatter_audit.py",     # read-only audit
    "wiki_lint.py",             # read-only lint
    "build_graph_colors.py",    # writes only the Obsidian graph config
    "sync_shared_skills.py",    # writes only the .agents/.claude skill mirrors
    "safe_shell.sh",            # the wrapper itself
    "test_require_safe_shell.py",  # this gate's own evaluation suite
}

# Command shapes that touch many files in one pass. Each entry is (regex, why).
BULK_PATTERNS = [
    (re.compile(r"\bfind\b(?=[^|;&]*\s-(?:exec|execdir|delete|fprint)\b)"),
     "find with -exec/-delete acts on every match at once"),
    (re.compile(r"\bxargs\b"),
     "xargs fans one command out over every input line"),
    (re.compile(r"\bsed\b[^|;&]*\s-[A-Za-z]*i"),
     "sed -i edits files in place"),
    (re.compile(r"\bperl\b[^|;&]*\s-[A-Za-z]*i"),
     "perl -i edits files in place"),
    (re.compile(r"\bgit\s+(?:clean|checkout\s+\.|restore\s+\.)"),
     "git clean/checkout . discards many files at once"),
    (re.compile(r"\b(?:rsync|robocopy)\b"),
     "rsync/robocopy copies whole trees"),
    (re.compile(r"\bdd\b[^|;&]*\bof="),
     "dd writes raw blocks to a target"),
    (re.compile(r"\bshutil\.(?:rmtree|copytree|move)\b"),
     "an inline shutil tree operation"),
    (re.compile(r"\bos\.(?:walk|removedirs)\b"),
     "an inline os.walk traversal"),
    (re.compile(r"\bpathlib\b[^|;&]*\brglob\b|\bPath\([^)]*\)\.rglob\b"),
     "an inline recursive glob"),
]

# Loop constructs must be matched against the WHOLE command, never a segment.
# `for f in *.md; do rm $f; done` contains two semicolons that belong to the
# construct, not to command separation — split first and the loop disappears,
# leaving three fragments that each look harmless. That is how a bulk operation
# would have walked straight through this gate.
LOOP_PATTERNS = [
    (re.compile(r"\bfor\b\s+\w+\s+in\b[\s\S]*?\bdo\b"),
     "a for loop repeats an operation over a list"),
    (re.compile(r"\bwhile\b[\s\S]*?\bdo\b"),
     "a while loop repeats an operation"),
    (re.compile(r"\buntil\b[\s\S]*?\bdo\b"),
     "an until loop repeats an operation"),
]

# Mutating commands that become bulk the moment a wildcard is involved.
MUTATORS = re.compile(
    r"\b(?:rm|rmdir|mv|cp|chmod|chown|chgrp|truncate|shred|unlink|install|tee|touch)\b"
)
GLOB = re.compile(r"[*?]|\{[^}]*,[^}]*\}")

# Redirections that write, e.g. `> file` or `>> file` (not `2>&1`, not `>&`).
REDIRECT_WRITE = re.compile(r"(?<![0-9&])>>?(?!&)")


def split_segments(command):
    """Split a shell command into segments on && || ; | and newlines, honouring quotes.

    Quote tracking matters: a `;` inside a quoted string is data, not a separator,
    and treating it as one would let a gated construct hide inside a quoted argument.
    """
    segments = []
    buf = []
    quote = None
    i = 0
    while i < len(command):
        ch = command[i]
        if quote:
            buf.append(ch)
            if ch == "\\" and quote == '"' and i + 1 < len(command):
                buf.append(command[i + 1])
                i += 2
                continue
            if ch == quote:
                quote = None
            i += 1
            continue
        if ch in ("'", '"'):
            quote = ch
            buf.append(ch)
            i += 1
            continue
        if ch == "\\" and i + 1 < len(command):
            buf.append(ch)
            buf.append(command[i + 1])
            i += 2
            continue
        two = command[i:i + 2]
        if two in ("&&", "||"):
            segments.append("".join(buf))
            buf = []
            i += 2
            continue
        if ch in (";", "|", "\n", "&"):
            segments.append("".join(buf))
            buf = []
            i += 1
            continue
        buf.append(ch)
        i += 1
    segments.append("".join(buf))
    return [s.strip() for s in segments if s.strip()]


def strip_quoted(text):
    """Blank out quoted spans, preserving length.

    Quoted text is DATA, not code: `git commit -m "while testing, do not skip"`
    is a commit message, and gating it would train whoever hits it to disable the
    hook. The exception is inline code — `bash -c '...'`, `python -c '...'` —
    where the quoted span IS the program; classify() scans those unstripped.
    """
    out = []
    quote = None
    i = 0
    while i < len(text):
        ch = text[i]
        if quote:
            if ch == "\\" and quote == '"' and i + 1 < len(text):
                out.append("  ")
                i += 2
                continue
            if ch == quote:
                quote = None
                out.append(" ")
            else:
                out.append(" ")
            i += 1
            continue
        if ch in ("'", '"'):
            quote = ch
            out.append(" ")
            i += 1
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def tokenize(segment):
    """Cheap whitespace tokenizer that keeps quoted spans together."""
    tokens = []
    buf = []
    quote = None
    for ch in segment:
        if quote:
            if ch == quote:
                quote = None
            else:
                buf.append(ch)
            continue
        if ch in ("'", '"'):
            quote = ch
            continue
        if ch.isspace():
            if buf:
                tokens.append("".join(buf))
                buf = []
            continue
        buf.append(ch)
    if buf:
        tokens.append("".join(buf))
    return tokens


def basename(token):
    return os.path.basename(token.replace("\\", "/")).lower()


def strip_prefix_tokens(tokens):
    """Drop leading env assignments and exec/command/time/nohup wrappers."""
    out = list(tokens)
    while out:
        head = out[0]
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", head):
            out.pop(0)
            continue
        if basename(head) in ("exec", "command", "time", "nohup", "env", "sudo"):
            out.pop(0)
            continue
        break
    return out


def is_wrapped(segment):
    """True when this segment is itself launched through safe_shell.sh."""
    tokens = strip_prefix_tokens(tokenize(segment))
    if not tokens:
        return False
    if basename(tokens[0]) == "safe_shell.sh":
        return True
    # `bash 00-BRAIN/scripts/safe_shell.sh ...`
    if basename(tokens[0]) in ("bash", "sh", "zsh") and len(tokens) > 1:
        if basename(tokens[1]) == "safe_shell.sh":
            return True
    return False


def script_invocation(tokens):
    """Return the script basename when this segment runs an interpreter on a script."""
    if not tokens:
        return None
    if basename(tokens[0]) not in INTERPRETERS:
        return None
    for tok in tokens[1:]:
        if tok.startswith("-"):
            continue
        if tok.lower().endswith(SCRIPT_EXTS):
            return basename(tok)
        # `python -c '...'` / `bash -c '...'` carry the program inline; the flag
        # itself is caught by the inline-code check below.
        return None
    return None


def classify(segment):
    """Return a reason string when this segment needs the wrapper, else None."""
    tokens = strip_prefix_tokens(tokenize(segment))
    if not tokens:
        return None

    head = basename(tokens[0])

    # 1. An interpreter pointed at a script file.
    script = script_invocation(tokens)
    if script is not None:
        if script in ALLOWED_SCRIPTS:
            return None
        return ("runs the script `%s`, and a script can touch any number of files "
                "in one pass" % script)

    # 2. Inline code handed to an interpreter (`python -c`, `bash -c`, `node -e`)
    #    or to `eval`. Here the quoted span IS the program, so it is scanned in
    #    full rather than stripped.
    inline = head in INTERPRETERS and bool(
        {t for t in tokens[1:] if t.startswith("-")}
        & {"-c", "-e", "--eval", "-Command", "-command"}
    )
    if head == "eval":
        inline = True
    if inline:
        for pattern, why in LOOP_PATTERNS + BULK_PATTERNS:
            if pattern.search(segment):
                return "inline %s code where %s" % (head, why)
        if MUTATORS.search(segment) and GLOB.search(segment):
            return "inline %s code combining a mutating command with a wildcard" % head

    # Everything below reads code only — quoted spans are blanked out, so a
    # commit message describing a bulk operation is not mistaken for one.
    bare = strip_quoted(segment)

    # 3. Known bulk shapes anywhere in the segment.
    for pattern, why in BULK_PATTERNS:
        if pattern.search(bare):
            return why

    # 4. A mutating command plus a wildcard — the 2026-08-10 shape exactly.
    if MUTATORS.search(bare) and GLOB.search(bare):
        return ("combines a mutating command with a wildcard, so the targets are "
                "resolved at runtime and never appear in the command string")

    # 5. A write redirection whose target is a wildcard expansion.
    if REDIRECT_WRITE.search(bare) and GLOB.search(bare):
        return "redirects a write to a wildcard-resolved target"

    return None


# Command substitution bodies run as commands in their own right, so
# `echo $(bash migrate.sh)` executes the script while looking like an echo.
SUBSTITUTION = re.compile(r"\$\(([^()]*)\)|`([^`]*)`")


def evaluate(command, _depth=0):
    """The single decision path: return (segment, why) when the wrapper is required.

    main() and the test suite both call this. They must never reimplement it
    separately — a test that walks its own copy of the logic passes while the
    real path is broken, which is how the loop-splitting defect survived its
    first evaluation run.
    """
    # Command substitutions first: their contents execute regardless of what the
    # surrounding command looks like, and they survive quoting.
    if _depth < 3:
        for outer, inner in SUBSTITUTION.findall(command):
            body = outer or inner
            if not body.strip():
                continue
            sub_segment, sub_why = evaluate(body, _depth + 1)
            if sub_why:
                return sub_segment, "%s (inside a command substitution)" % sub_why

    segments = split_segments(command)

    # Whole-command pass first, for constructs that span segment separators.
    # Skipped only when the wrapper is genuinely in play somewhere in the chain.
    if not any(is_wrapped(seg) for seg in segments):
        bare_command = strip_quoted(command)
        for pattern, why in LOOP_PATTERNS:
            if pattern.search(bare_command):
                return command.strip(), why

    # Per-segment pass for everything else.
    for segment in segments:
        if is_wrapped(segment):
            continue
        why = classify(segment)
        if why:
            return segment, why

    return None, None


def deny(reason, detail):
    payload = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    sys.stdout.write(json.dumps(payload))
    sys.stdout.flush()
    sys.stderr.write(detail + "\n")
    sys.exit(2)


def build_message(segment, why, cwd):
    on_windows = os.name == "nt"
    wrapped = "%s %s" % (WRAPPER_REL, segment)
    lines = [
        "BLOCKED by require_safe_shell — AGENT.md File Safety 12.",
        "",
        "This segment %s:" % why,
        "    %s" % segment,
        "",
        "Bulk or scripted work runs behind the OS-level write deny, which is the "
        "only control in this stack measured as enforcing. The declarative "
        "`sandbox` block in settings.json is INERT in both environments (flag #96), "
        "so nothing else stops a spawned process from writing 88-JOURNAL or raw/.",
        "",
    ]
    if on_windows:
        lines += [
            "You are on Windows, where the wrapper cannot run — bwrap is Linux-only.",
            "Re-launch it from WSL:",
            "",
            '    wsl -e bash -lc "cd /mnt/c/Users/chris/.ROOT && %s"' % wrapped,
        ]
    else:
        lines += [
            "Run it through the wrapper instead:",
            "",
            "    %s" % wrapped,
            "",
            "Run `%s --selftest` first for a consequential pass." % WRAPPER_REL,
        ]
    lines += [
        "",
        "Also required by item 12: run it against a disposable copy first. The "
        "wrapper is the mechanism; copy-first is the discipline. Neither replaces "
        "the other.",
        "",
        "There is no command-string override — that would be a wall an AI could "
        "walk through by typing. If this is a false positive, the allowlist lives "
        "in .claude/hooks/require_safe_shell.py (ALLOWED_SCRIPTS) and is Chris's "
        "to change.",
    ]
    return "\n".join(lines)


def main():
    try:
        raw = sys.stdin.read()
    except Exception as exc:  # noqa: BLE001 - fail closed on any read failure
        deny(
            "require_safe_shell could not read hook input (%s). Failing closed." % exc,
            "require_safe_shell: stdin unreadable, denying.",
        )

    if not raw.strip():
        deny(
            "require_safe_shell received empty hook input. Failing closed.",
            "require_safe_shell: empty stdin, denying.",
        )

    try:
        payload = json.loads(raw)
    except Exception as exc:  # noqa: BLE001
        deny(
            "require_safe_shell could not parse hook input (%s). Failing closed." % exc,
            "require_safe_shell: unparseable stdin, denying.",
        )

    if payload.get("tool_name") != "Bash":
        sys.exit(0)

    tool_input = payload.get("tool_input") or {}
    command = tool_input.get("command")
    if command is None:
        sys.exit(0)
    if not isinstance(command, str):
        deny(
            "require_safe_shell saw a non-string Bash command. Failing closed.",
            "require_safe_shell: non-string command, denying.",
        )

    cwd = payload.get("cwd") or ""

    segment, why = evaluate(command)
    if why:
        message = build_message(segment, why, cwd)
        deny(message, message)

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 - the whole point is not failing open
        deny(
            "require_safe_shell crashed (%s). Failing closed — a gate that fails "
            "open reads as protection and stops nothing." % exc,
            "require_safe_shell: internal error, denying.",
        )
