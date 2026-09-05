#!/usr/bin/env python3
"""verify_controls.py — does each declared control actually enforce anything here?

`validate_boot_chain.py` checks that the rules are PRESENT and well-formed.
This script checks whether they BITE in the environment currently reading them.
The two answer different questions, and flag #95 exists because the first was
mistaken for the second: a config set is read from both Windows and WSL with no
per-environment resolution, so a rule can be syntactically valid, pass its gate,
and protect nothing.

Read-only and non-destructive. It creates no files, deletes nothing, and makes no
network request unless `--network` is passed explicitly.

Usage:
    python  00-BRAIN/scripts/verify_controls.py            # Windows
    python3 00-BRAIN/scripts/verify_controls.py            # WSL
    python3 00-BRAIN/scripts/verify_controls.py --network  # also probe egress
    python3 00-BRAIN/scripts/verify_controls.py --strict   # exit 1 if any INERT
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

ENFORCED = "ENFORCED"
INERT = "INERT"
UNMEASURABLE = "NOT MEASURABLE"
SKIPPED = "NOT TESTED"

rows: list[tuple[str, str, str, str]] = []


def record(control: str, declared: str, measured: str, verdict: str) -> None:
    rows.append((control, declared, measured, verdict))


def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def child_can_write(path: Path) -> bool | None:
    """Ask a SPAWNED PROCESS whether it may write `path`.

    The distinction matters: tool-level Edit/Write denies govern tool calls, not
    the children a shell starts, and it was a child process that rewrote 2,713
    files on 2026-08-10. Returns None where the answer is not measurable.
    """
    if os.name == "nt":
        # Windows os.access() reports directories writable regardless of ACLs,
        # so a result here would be noise presented as evidence.
        return None
    probe = (
        "import os,sys;"
        "sys.exit(0 if os.access(sys.argv[1], os.W_OK) else 1)"
    )
    try:
        done = subprocess.run(
            [sys.executable, "-c", probe, str(path)],
            capture_output=True, timeout=20, check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return done.returncode == 0


def child_can_list(path: Path) -> bool | None:
    probe = "import os,sys;os.listdir(sys.argv[1]);sys.exit(0)"
    try:
        done = subprocess.run(
            [sys.executable, "-c", probe, str(path)],
            capture_output=True, timeout=20, check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return done.returncode == 0


def check_interpreters(*settings_files: tuple[str, dict | None]) -> None:
    """Is each allowed script reachable here by at least ONE spelling?

    The question is not whether every rule resolves — carrying both a `python`
    and a `python3` variant is the portability fix, and one of the pair is
    always dead in a given environment. The question is whether any script ends
    up with no working spelling at all, which is what made every scripted run
    prompt in WSL (flag #95 instance 3).
    """
    for label, settings in settings_files:
        if not settings:
            continue
        allows = settings.get("permissions", {}).get("allow", [])
        # script path -> True if some rule names an interpreter that exists here
        reachable: dict[str, bool] = {}
        for rule in allows:
            if not rule.startswith("Bash("):
                continue
            inner = rule[len("Bash("):].rstrip(")")
            parts = inner.split()
            if len(parts) < 2:
                continue
            interpreter, script = parts[0], parts[1].replace("\\", "/")
            resolves = shutil.which(interpreter) is not None
            reachable[script] = reachable.get(script, False) or resolves
        if not reachable:
            continue
        stranded = sorted(s for s, ok in reachable.items() if not ok)
        if stranded:
            record(
                f"allow-rule reachability — {label}",
                f"{len(reachable)} distinct scripts across {len(allows)} rules",
                f"{len(stranded)} have NO working interpreter here: "
                + ", ".join(Path(s).name for s in stranded),
                INERT,
            )
        else:
            record(
                f"allow-rule reachability — {label}",
                f"{len(reachable)} distinct scripts across {len(allows)} rules",
                "every script reachable by at least one spelling",
                ENFORCED,
            )


def check_sandbox(project: dict | None) -> None:
    sandbox = (project or {}).get("sandbox", {})
    if not sandbox:
        record("sandbox block", "absent", "nothing declared", SKIPPED)
        return

    fs = sandbox.get("filesystem", {})
    deny_write = [p for p in fs.get("denyWrite", []) if "*" not in p]
    writable, protected, unknown = [], [], 0
    for rel in deny_write:
        target = (ROOT / rel.lstrip("./")).resolve()
        if not target.is_dir():
            continue
        answer = child_can_write(target)
        if answer is None:
            unknown += 1
        elif answer:
            writable.append(rel)
        else:
            protected.append(rel)

    declared = f"enabled={sandbox.get('enabled')}, {len(deny_write)} literal denyWrite paths"
    if unknown and not writable and not protected:
        record("sandbox filesystem.denyWrite", declared,
               "Windows cannot measure child-process write access reliably",
               UNMEASURABLE)
    elif writable:
        record("sandbox filesystem.denyWrite", declared,
               f"{len(writable)} of {len(writable) + len(protected)} "
               f"writable by a spawned child", INERT)
    elif protected:
        record("sandbox filesystem.denyWrite", declared,
               f"all {len(protected)} refused to a spawned child", ENFORCED)

    for rel in fs.get("denyRead", []):
        target = (ROOT / rel.lstrip("./")).resolve()
        if not target.is_dir():
            continue
        answer = child_can_list(target)
        if answer is None:
            record(f"sandbox denyRead {rel}", "declared", "not measurable here",
                   UNMEASURABLE)
        else:
            record(f"sandbox denyRead {rel}", "declared",
                   "listed by a spawned child" if answer
                   else "refused to a spawned child",
                   INERT if answer else ENFORCED)


def check_network(sandbox: dict, do_probe: bool) -> None:
    allowed = sandbox.get("network", {}).get("allowedDomains", [])
    if not allowed:
        return
    if not do_probe:
        record("sandbox network.allowedDomains", f"{len(allowed)} hosts",
               "not probed (pass --network to make one outbound request)",
               SKIPPED)
        return
    probe = (
        "import sys,urllib.request;"
        "urllib.request.urlopen('https://example.com', timeout=10);"
        "sys.exit(0)"
    )
    try:
        done = subprocess.run([sys.executable, "-c", probe],
                              capture_output=True, timeout=30, check=False)
        reached = done.returncode == 0
    except (OSError, subprocess.SubprocessError):
        reached = False
    record("sandbox network.allowedDomains", f"{len(allowed)} hosts",
           "non-allowlisted example.com reachable" if reached
           else "non-allowlisted example.com blocked",
           INERT if reached else ENFORCED)


def check_deployed_policy() -> None:
    deployed = load(Path.home() / ".claude" / "settings.json")
    if deployed is None:
        record("deployed user policy", "expected at ~/.claude/settings.json",
               "not found", INERT)
        return
    denies = deployed.get("permissions", {}).get("deny", [])
    vault_rules = [d for d in denies if ".ROOT" in d]
    dangling = []
    for rule in vault_rules:
        inside = rule[rule.index("(") + 1:rule.rindex(")")]
        base = inside.split("/**")[0]
        expanded = Path(os.path.expanduser(base))
        # Walk up to the vault root portion of the pattern.
        probe = expanded
        while "*" in probe.name or probe.name in {"88-JOURNAL", "raw"}:
            probe = probe.parent
        if not probe.exists():
            dangling.append(rule)
    if not vault_rules:
        record("deployed user policy vault denies", "expected 5",
               "none present — the vault is not guarded at user scope", INERT)
    elif dangling:
        record("deployed user policy vault denies", f"{len(vault_rules)} rules",
               f"{len(dangling)} point at a path that does not exist here",
               INERT)
    else:
        record("deployed user policy vault denies", f"{len(vault_rules)} rules",
               "every guarded path resolves in this environment", ENFORCED)


def check_wrapper() -> None:
    wrapper = ROOT / "00-BRAIN" / "scripts" / "safe_shell.sh"
    if not wrapper.is_file():
        record("safe_shell.sh wrapper", "required by AGENT.md File Safety 12",
               "MISSING", INERT)
        return
    if os.name == "nt":
        record("safe_shell.sh wrapper", "present",
               "run `--selftest` from WSL to measure enforcement", SKIPPED)
        return
    if shutil.which("bwrap") is None:
        record("safe_shell.sh wrapper", "present", "bwrap not installed", INERT)
        return
    done = subprocess.run(["bash", str(wrapper), "--selftest"],
                          capture_output=True, text=True, check=False)
    record("safe_shell.sh wrapper", "present",
           "selftest 3/3 pass" if done.returncode == 0 else "SELFTEST FAILED",
           ENFORCED if done.returncode == 0 else INERT)


def check_bulk_gate(project: dict | None) -> None:
    """Does the PreToolUse bulk-work gate actually block, in THIS environment?

    Measured the way Claude Code invokes it: the configured command string is
    read from settings.json, run through the shell, and fed real hook payloads.
    Asking whether the files exist would answer the wrong question — the failure
    mode this guards against is a hook whose command is dead in one environment
    (WSL has `python3` and no `python`; Windows the reverse), because a hook that
    cannot launch is a NON-BLOCKING error and the tool call proceeds unprotected.

    Two probes, because a gate that blocks everything is as broken as one that
    blocks nothing:
      1. a bulk command MUST be denied (rc=2)
      2. an ordinary command MUST pass (rc=0)
    """
    hooks = (project or {}).get("hooks", {}).get("PreToolUse", [])
    entry = None
    for group in hooks:
        if group.get("matcher") != "Bash":
            continue
        for hook in group.get("hooks", []):
            if "require_safe_shell" in str(hook.get("command", "")):
                entry = hook
                break
    if entry is None:
        record("PreToolUse bulk-work gate",
               "required by AGENT.md File Safety 12",
               "no hook configured — item 12 is prose again", INERT)
        return

    command = str(entry.get("command", "")).replace(
        "${CLAUDE_PROJECT_DIR}", str(ROOT)
    ).replace("$CLAUDE_PROJECT_DIR", str(ROOT))

    # Reproduce the harness's invocation, not cmd.exe's.
    #
    # Measured 2026-08-11: on Windows `bash` on PATH is the WSL launcher at
    # ...\WindowsApps\bash.exe, which cannot resolve a Windows-style path and
    # exits 127. Claude Code runs shell-form hooks through Git Bash instead, so
    # the gate fires correctly while this probe — going through cmd.exe with
    # shell=True — saw 127 and reported the live gate as INERT.
    #
    # That false negative is the mirror of flag #95: there, config read as
    # protection and enforced nothing; here, a working control read as dead.
    # Both come from measuring something other than what actually runs.
    if os.name == "nt" and command.lstrip().startswith("bash "):
        git_bash = Path(r"C:\Program Files\Git\bin\bash.exe")
        resolved = shutil.which("bash") or ""
        if git_bash.is_file() and "WindowsApps" in resolved:
            command = f'"{git_bash}" ' + command.lstrip()[len("bash "):]

    def probe(bash_command: str) -> int | None:
        payload = json.dumps({
            "hook_event_name": "PreToolUse",
            "tool_name": "Bash",
            "cwd": str(ROOT),
            "tool_input": {"command": bash_command},
        })
        try:
            done = subprocess.run(
                command, shell=True, input=payload,
                capture_output=True, text=True, timeout=30, check=False,
                cwd=str(ROOT),
            )
        except (OSError, subprocess.SubprocessError):
            return None
        return done.returncode

    bulk_rc = probe("find . -name '*.md' -exec sed -i 's/a/b/' {} \\;")
    safe_rc = probe("git status")

    declared = "hook configured for Bash"
    # rc=127 is "command not found" — the PROBE failed to launch, which says
    # nothing about whether the hook launches under Claude Code's own runner.
    # A measurement that could not run must never report its subject as dead;
    # that is how a working control gets "fixed" or a protected environment gets
    # declared open. Report the gap honestly instead.
    launch_failed = bulk_rc is None or safe_rc is None or 127 in (bulk_rc, safe_rc)
    if launch_failed:
        record("PreToolUse bulk-work gate", declared,
               "probe could not launch the hook command here — NOT evidence the "
               "gate is dead; verify with a real bulk Bash call", UNMEASURABLE)
    elif bulk_rc != 2:
        record("PreToolUse bulk-work gate", declared,
               f"bulk command NOT blocked (rc={bulk_rc}, expected 2)", INERT)
    elif safe_rc != 0:
        record("PreToolUse bulk-work gate", declared,
               f"ordinary command wrongly blocked (rc={safe_rc}, expected 0)",
               INERT)
    else:
        record("PreToolUse bulk-work gate", declared,
               "bulk denied (rc=2), ordinary allowed (rc=0)", ENFORCED)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--network", action="store_true",
                        help="make one outbound request to probe the allowlist")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 if any control measures INERT")
    args = parser.parse_args()

    project = load(ROOT / ".claude" / "settings.json")
    local = load(ROOT / ".claude" / "settings.local.json")

    print("# CONTROL ENFORCEMENT VERIFICATION\n")
    print(f"Vault:       {ROOT}")
    print(f"Platform:    {platform.system()} {platform.release()}")
    print(f"Interpreter: {sys.executable}")
    print(f"Home:        {Path.home()}\n")

    check_interpreters(("project settings", project), ("local settings", local))
    check_sandbox(project)
    check_network((project or {}).get("sandbox", {}), args.network)
    check_deployed_policy()
    check_wrapper()
    check_bulk_gate(project)

    width = max(len(r[0]) for r in rows)
    for control, declared, measured, verdict in rows:
        print(f"{verdict:<15} {control:<{width}}  {measured}")
        print(f"{'':<15} {'':<{width}}  declared: {declared}")

    inert = [r for r in rows if r[3] == INERT]
    print(f"\n{len(rows)} controls checked; {len(inert)} measured INERT.")
    if inert:
        print("An INERT control reads as protection in an audit and stops nothing.")
        print("Record it beside the config, or remove it — do not leave it silent.")
    return 1 if (args.strict and inert) else 0


if __name__ == "__main__":
    raise SystemExit(main())
