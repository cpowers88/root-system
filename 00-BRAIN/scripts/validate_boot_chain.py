#!/usr/bin/env python3
"""validate_boot_chain.py — post-edit governance validation.

Run after any edit to governance files (00-BRAIN, router, START_HERE,
hats, hub operating files). Encodes the POST_SPLIT_REVIEW_2026-07-10
validation checks:

  1. Boot files exist: router, AGENT.md, lane files, CHRIS_CORE, hats,
     CASTLE pointers/OPERATIONS, all seven hub CLAUDE.mds
  2. No active file loads the retired OS (AI_Agent.md / AI_OS_CORE.md
     as an instruction — the marked pointer + retired-name lines are exempt)
  3. No dead governance references (AGENT.md "Shared Skills";
     "shifts the color groups")
  4. Track count consistent (no "four tracks" in live governance)

Read-only. Exit 0 = PASS, 1 = FAIL.
Usage (from .ROOT):  python 00-BRAIN/scripts/validate_boot_chain.py
"""

import re
import sys
import json
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]

BOOT_FILES = [
    ROOT / "CLAUDE.md", ROOT / "START_HERE.md", ROOT / "NOW.md", ROOT / "CODEX.md",
    ROOT / "00-BRAIN" / "AGENT.md", ROOT / "00-BRAIN" / "CLAUDE.md",
    ROOT / "00-BRAIN" / "CODEX.md", ROOT / "00-BRAIN" / "ATLAS.md",
    ROOT / "00-BRAIN" / "CHRIS_CORE.md", ROOT / "00-BRAIN" / "WHERE_IT_GOES.md",
    ROOT / "00-BRAIN" / "vault_map.md", ROOT / "00-BRAIN" / "SYSTEM_FLAGS.md",
    ROOT / "00-BRAIN" / "CASTLE" / "CLAUDE.md",
    ROOT / "00-BRAIN" / "CASTLE" / "CODEX.md",
    ROOT / "00-BRAIN" / "CASTLE" / "OPERATIONS.md",
] + [ROOT / "00-BRAIN" / "HATS" / f"HAT_{h}.md" for h in
     ("OPERATOR", "EDUCATOR", "PYTHON", "PHYSICS", "TCOM", "ECON", "ENGR1000")
] + [ROOT / "03-WIKIS" / h / "CLAUDE.md" for h in
     ("AI_AUTOMATION_SYSTEMS", "BUSINESS", "EDUCATION", "PHYSICS",
      "PYTHON", "SYSTEMS", "TECHNOLOGY")]

EXCLUDED = {"99-ARCHIVE", "raw", ".git", ".obsidian", "Report Archive",
            "Session_Logs", "88-JOURNAL", ".claude", ".agents"}
# Lines that legitimately mention retired names (marked pointers/records)
EXEMPT_MARKERS = re.compile(
    r"retired|superseded|archived|ARCHIVED|scan pattern|AI_Agent\|", re.I)

CHECKS = [
    (re.compile(r"(load|boot|read).{0,40}AI_Agent\.md", re.I),
     "instructs loading retired AI_Agent.md"),
    (re.compile(r"AGENT\.md\s*\(Shared Skills\)"),
     "dead 'AGENT.md (Shared Skills)' reference"),
    (re.compile(r"shifts? the color groups", re.I),
     "retired graph color-shift instruction"),
    (re.compile(r"[Ff]our[- ][Tt]racks?\b"),
     "four-track language (doctrine is three tracks, July 10, 2026)"),
]


def main() -> int:
    failures = []

    for f in BOOT_FILES:
        if not f.exists():
            failures.append(f"MISSING boot file: {f}")

    # Deterministic safety baseline: Claude project settings must parse and
    # preserve the private/raw boundaries defined by AGENT.md.
    settings_path = ROOT / ".claude" / "settings.local.json"
    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
        permissions = settings.get("permissions", {})
        deny = set(permissions.get("deny", []))
        required_deny = {
            "Read(/88-JOURNAL/**)", "Edit(/88-JOURNAL/**)",
            "Write(/88-JOURNAL/**)", "Edit(/**/raw/**)",
            "Write(/**/raw/**)",
        }
        missing_deny = sorted(required_deny - deny)
        if missing_deny:
            failures.append(f"Claude settings missing deny rules: {missing_deny}")
        if permissions.get("defaultMode") != "default":
            failures.append("Claude default permission mode must be 'default'")
        if permissions.get("disableBypassPermissionsMode") != "disable":
            failures.append("Claude bypassPermissions mode is not disabled")
        if permissions.get("disableAutoMode") != "disable":
            failures.append("Claude auto mode is not disabled during supervised launch")
        filesystem = settings.get("sandbox", {}).get("filesystem", {})
        if "./88-JOURNAL" not in filesystem.get("denyRead", []):
            failures.append("Sandbox does not deny reads from 88-JOURNAL")
        required_raw = {
            "./00-BRAIN/CASTLE/raw",
            *{f"./03-WIKIS/{hub}/raw" for hub in (
                "PYTHON", "PHYSICS", "BUSINESS", "EDUCATION",
                "TECHNOLOGY", "AI_AUTOMATION_SYSTEMS", "SYSTEMS")},
        }
        missing_raw = sorted(required_raw - set(filesystem.get("denyWrite", [])))
        if missing_raw:
            failures.append(f"Sandbox missing raw write-deny paths: {missing_raw}")
    except FileNotFoundError:
        failures.append("MISSING .claude/settings.local.json safety configuration")
    except json.JSONDecodeError as exc:
        failures.append(f"INVALID .claude/settings.local.json: {exc}")

    agent_text = (ROOT / "00-BRAIN" / "AGENT.md").read_text(
        encoding="utf-8", errors="replace")
    for marker in ("## Agent Evaluation Gate", "typical, edge, and failure/recovery",
                   "Review the full action trace"):
        if marker not in agent_text:
            failures.append(f"AGENT.md missing evaluation control: {marker}")

    # log.md files and dated proposals/reports are history — logs record
    # experience (AGENT.md); they keep pre-split wording by design.
    historical = re.compile(r"^(log\.md|\d{4}-\d{2}-\d{2}_.*|.*_\d{4}-\d{2}-\d{2}\.md)$")
    live_md = [p for p in ROOT.rglob("*.md")
               if not EXCLUDED.intersection(p.relative_to(ROOT).parts)
               and not historical.match(p.name)]
    for p in live_md:
        rel = p.relative_to(ROOT)
        for i, line in enumerate(
                p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if EXEMPT_MARKERS.search(line):
                continue
            for pat, why in CHECKS:
                if pat.search(line):
                    failures.append(f"{rel}:{i} — {why}: {line.strip()[:90]}")

    print("# BOOT CHAIN VALIDATION")
    print(f"\nBoot files checked: {len(BOOT_FILES)} | live pages scanned: {len(live_md)}\n")
    if failures:
        print(f"## FAIL — {len(failures)} finding(s)")
        for f in failures:
            print(f"- {f}")
        return 1
    print("## PASS — boot chain clean, no stale governance references")
    return 0


if __name__ == "__main__":
    sys.exit(main())
