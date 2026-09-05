#!/usr/bin/env python3
"""
test_require_safe_shell.py — evidence for AGENT.md's Agent Evaluation Gate.

The gate requires typical, edge, and failure/recovery cases tested before
consequential or recurring unsupervised use, plus the tool/permission cases the
workflow itself introduces. This file is that evidence, and it is re-runnable so
a regression returns the hook to supervised use rather than passing silently.

Run:  python3 .claude/hooks/test_require_safe_shell.py
Exit: 0 all pass, 1 any failure.

Two layers:
  1. classify()/is_wrapped() unit cases — is the decision right?
  2. end-to-end subprocess cases — does the real launcher exit 0/2 correctly,
     including when the input is garbage?
"""

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import require_safe_shell as gate  # noqa: E402

LAUNCHER = os.path.join(HERE, "require_safe_shell.sh")

# (command, should_be_gated, label)
CASES = [
    # ---- TYPICAL: ordinary work that must NOT be gated -----------------------
    ("ls -la", False, "plain ls"),
    ("cat README.md", False, "single file read"),
    ("grep -rn 'flag 96' 00-BRAIN/", False, "recursive grep is read-only"),
    ("git status", False, "git status"),
    ("git add 00-BRAIN/SYSTEM_FLAGS.md && git commit -m 'x'", False, "ordinary commit"),
    ("git diff --stat", False, "git diff"),
    ("wc -l NOW.md", False, "line count"),
    ("mkdir -p 99-ARCHIVE/newdir", False, "single mkdir"),
    ("cp NOW.md NOW.md.bak", False, "single-file copy, no wildcard"),
    ("echo hello > /tmp/one.txt", False, "single redirect, no wildcard"),

    # ---- TYPICAL: allowlisted governance scripts must NOT be gated -----------
    ("python3 00-BRAIN/scripts/root_health.py", False, "allowlisted health gate"),
    ("python 00-BRAIN/scripts/verify_controls.py", False, "allowlisted, Windows spelling"),
    ("python3 00-BRAIN/scripts/validate_boot_chain.py", False, "allowlisted boot chain"),
    ("python3 00-BRAIN/scripts/sync_shared_skills.py --check", False, "allowlisted sync"),
    ("bash 00-BRAIN/scripts/safe_shell.sh --selftest", False, "the wrapper itself"),

    # ---- THE REAL CASES: bulk work that MUST be gated ------------------------
    ("python3 00-BRAIN/scripts/fetch_fred.py", True, "unreviewed script (the Aug 11 case)"),
    ("python3 migrate.py", True, "arbitrary migration script"),
    ("bash cleanup.sh", True, "arbitrary shell script"),
    ("node rewrite.js", True, "arbitrary node script"),
    ("find . -name '*.md' -exec sed -i 's/a/b/' {} \\;", True, "find -exec (the Aug 10 shape)"),
    ("find . -name '*.tmp' -delete", True, "find -delete"),
    ("ls *.md | xargs rm", True, "xargs fan-out"),
    ("sed -i 's/old/new/' *.md", True, "sed -i with glob"),
    ("for f in *.md; do echo $f; done", True, "for loop over a glob"),
    ("while read l; do rm $l; done < list.txt", True, "while loop"),
    ("rm -rf 03-WIKIS/*/raw", True, "mutator plus wildcard"),
    ("mv 02-LIBRARY/*.md 99-ARCHIVE/", True, "bulk move"),
    ("cp -r 03-WIKIS/* /tmp/backup/", True, "recursive copy with wildcard"),
    ("chmod 777 03-WIKIS/*/raw/*", True, "bulk chmod"),
    ("git clean -fd", True, "git clean"),
    ("rsync -a 03-WIKIS/ /tmp/x/", True, "rsync tree copy"),
    ("python3 -c \"import shutil; shutil.rmtree('x')\"", True, "inline shutil.rmtree"),
    ("python3 -c \"import os; [os.remove(f) for f in os.walk('.')]\"", True, "inline os.walk"),

    # ---- EDGE: wrapped commands must NOT be gated ----------------------------
    ("00-BRAIN/scripts/safe_shell.sh python3 migrate.py", False, "wrapped script"),
    ("bash 00-BRAIN/scripts/safe_shell.sh find . -name '*.md' -delete", False, "wrapped find"),
    ("./00-BRAIN/scripts/safe_shell.sh sed -i 's/a/b/' *.md", False, "wrapped sed -i"),
    ("cd /mnt/c/Users/chris/.ROOT && 00-BRAIN/scripts/safe_shell.sh python3 migrate.py",
     False, "cd then wrapped"),

    # ---- EDGE: compound commands are evaluated per segment -------------------
    ("git status && python3 migrate.py", True, "safe segment then gated segment"),
    ("python3 migrate.py && git status", True, "gated segment first"),
    ("ls && cat NOW.md && git diff", False, "all segments safe"),
    ("cd 03-WIKIS && rm *.tmp", True, "gated after a cd"),

    # ---- EDGE: quoted text is DATA; quoted text fed to -c is CODE ------------
    # This distinction is the difference between a gate people keep and a gate
    # people switch off. Both halves must hold.
    ("echo 'for f in *; do rm $f; done'", False, "loop inside quotes is just text"),
    ("echo \"rm *\"", False, "quoted mutator+glob is just text"),
    ("grep 'safe_shell.sh' AGENT.md", False, "wrapper named as data, not invoked"),
    ('git commit -m "Record the gate; while testing, do not skip"', False,
     "commit message containing a loop-shaped phrase"),
    ('git commit -m "for each hub, do the lint"', False,
     "commit message containing for/do"),
    ('git commit -m "find . -delete is what broke it"', False,
     "commit message describing a bulk command"),
    ("bash -c 'for f in *; do rm $f; done'", True,
     "the SAME text handed to bash -c is code, and is gated"),
    ("sh -c \"rm -rf 03-WIKIS/*/raw\"", True, "inline sh code with mutator+glob"),
    ("eval \"rm *\"", True, "eval treats its argument as code"),
    ("python3 -c 'for p in Path(\".\").rglob(\"*\"): p.unlink()'", True,
     "inline python loop"),

    # ---- EDGE: command substitution runs code regardless of its wrapper ------
    ("echo $(bash migrate.sh)", True, "script inside $( )"),
    ("echo `bash migrate.sh`", True, "script inside backticks"),
    ('git commit -m "$(cat msg.txt)"', False, "benign substitution stays allowed"),
    ('echo "today is $(date)"', False, "date substitution stays allowed"),

    # ---- EDGE: prefixes must not bypass the gate -----------------------------
    ("exec python3 migrate.py", True, "exec prefix"),
    ("FOO=1 python3 migrate.py", True, "env-assignment prefix"),
    ("sudo rm -rf 03-WIKIS/*/raw", True, "sudo prefix"),
    ("env python3 migrate.py", True, "env prefix"),
]


def run_unit_cases():
    failures = []
    for command, expect_gated, label in CASES:
        # Call the real decision path — never a local reimplementation of it.
        _segment, why = gate.evaluate(command)
        gated = why is not None
        if gated != expect_gated:
            failures.append(
                "  %-9s %s\n            command: %s\n            expected %s, got %s"
                % ("FAIL", label, command,
                   "GATED" if expect_gated else "allowed",
                   "GATED" if gated else "allowed")
            )
    return failures


def invoke(payload_text):
    """Run the real launcher end to end; return (returncode, stdout, stderr)."""
    proc = subprocess.run(
        ["bash", LAUNCHER],
        input=payload_text,
        capture_output=True,
        text=True,
    )
    return proc.returncode, proc.stdout, proc.stderr


def run_e2e_cases():
    failures = []

    def check(label, payload_text, expect_rc, expect_deny_json):
        rc, out, err = invoke(payload_text)
        if rc != expect_rc:
            failures.append("  FAIL      %s\n            expected rc=%s, got rc=%s\n"
                            "            stderr: %s" % (label, expect_rc, rc, err.strip()[:200]))
            return
        if expect_deny_json:
            try:
                decision = json.loads(out)["hookSpecificOutput"]["permissionDecision"]
            except Exception as exc:  # noqa: BLE001
                failures.append("  FAIL      %s\n            stdout is not a deny decision (%s)\n"
                                "            stdout: %s" % (label, exc, out[:200]))
                return
            if decision != "deny":
                failures.append("  FAIL      %s\n            expected deny, got %s"
                                % (label, decision))

    def bash_payload(command):
        return json.dumps({
            "hook_event_name": "PreToolUse",
            "tool_name": "Bash",
            "cwd": "/mnt/c/Users/chris/.ROOT",
            "tool_input": {"command": command},
        })

    # Normal operation, end to end through the launcher.
    check("e2e allow: git status", bash_payload("git status"), 0, False)
    check("e2e allow: allowlisted script",
          bash_payload("python3 00-BRAIN/scripts/root_health.py"), 0, False)
    check("e2e deny: unreviewed script",
          bash_payload("python3 fetch_fred.py"), 2, True)
    check("e2e deny: the Aug 10 glob shape",
          bash_payload("find . -name '*.md' -exec sed -i 's/a/b/' {} \\;"), 2, True)
    check("e2e allow: wrapped bulk work",
          bash_payload("00-BRAIN/scripts/safe_shell.sh python3 migrate.py"), 0, False)

    # Other tools are none of this hook's business.
    check("e2e allow: non-Bash tool",
          json.dumps({"hook_event_name": "PreToolUse", "tool_name": "Read",
                      "tool_input": {"file_path": "/x"}}), 0, False)

    # FAILURE / RECOVERY: every malformed input must fail CLOSED (rc=2), never
    # rc=0 (silently allowed) and never rc=1 (non-blocking error = allowed).
    check("e2e fail-closed: empty stdin", "", 2, True)
    check("e2e fail-closed: unparseable stdin", "{not json", 2, True)
    check("e2e fail-closed: non-string command",
          json.dumps({"hook_event_name": "PreToolUse", "tool_name": "Bash",
                      "tool_input": {"command": {"nested": "object"}}}), 2, True)

    # A truncated payload must not be read as "no command, proceed".
    check("e2e fail-closed: truncated JSON",
          '{"tool_name": "Bash", "tool_input": {"comm', 2, True)

    return failures


def main():
    print("require_safe_shell — evaluation gate evidence")
    print("  gate:     %s" % os.path.join(HERE, "require_safe_shell.py"))
    print("  launcher: %s" % LAUNCHER)
    print()

    unit_failures = run_unit_cases()
    print("  classification cases: %d run, %d failed" % (len(CASES), len(unit_failures)))
    e2e_failures = run_e2e_cases()
    print("  end-to-end cases:     11 run, %d failed" % len(e2e_failures))
    print()

    failures = unit_failures + e2e_failures
    if failures:
        print("FAILURES")
        for line in failures:
            print(line)
        print()
        print("EVALUATION FAIL — %d case(s) failed. The hook is not fit for "
              "unsupervised use until these pass." % len(failures))
        return 1

    print("EVALUATION PASS — typical, edge, and failure/recovery cases all hold.")
    print("Malformed input fails CLOSED (rc=2) in every probed shape.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
