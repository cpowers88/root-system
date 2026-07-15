#!/usr/bin/env python3
"""validate_boot_chain.py — post-edit governance validation.

Run after any edit to governance files (00-BRAIN, router, START_HERE,
hats, hub operating files). Encodes the unified-team governance checks:

  1. Boot files exist: router, AGENT.md, capability profiles, CHRIS_CORE, hats,
     CASTLE pointers/OPERATIONS, all seven hub CLAUDE.mds
  2. No active file loads the retired OS (AI_Agent.md / AI_OS_CORE.md
     as an instruction — the marked pointer + retired-name lines are exempt)
  3. No dead governance references (AGENT.md "Shared Skills";
     "shifts the color groups")
  4. No active exclusive-model or absolute danger-week doctrine remains
  5. Canonical shared skills match both product discovery mirrors
  6. High-impact semantic contracts remain reconciled across human maps,
     placement rules, the universal OS, and the opportunity queue

Read-only. Exit 0 = PASS, 1 = FAIL.
Usage (from .ROOT):  python 00-BRAIN/scripts/validate_boot_chain.py
"""

import re
import subprocess
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
      "PYTHON", "REVENUE_LAB", "SYSTEMS", "TECHNOLOGY")]

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
    (re.compile(r"Claude Code (is|as) the (exclusive|primary) builder", re.I),
     "exclusive/primary Claude Code builder doctrine"),
    (re.compile(r"Codex identifies and briefs.{0,40}Claude Code builds", re.I),
     "mandatory Codex-to-Claude build chain"),
    (re.compile(r"danger weeks.{0,60}school only", re.I),
     "absolute danger-week prohibition"),
    (re.compile(r"wrong lane", re.I),
     "wrong-lane refusal language"),
]


def main() -> int:
    failures = []

    def read(rel: str) -> str:
        return (ROOT / rel).read_text(encoding="utf-8", errors="replace")

    def require(rel: str, pattern: str, why: str) -> None:
        if not re.search(pattern, read(rel), re.I | re.M | re.S):
            failures.append(f"{rel} missing semantic contract: {why}")

    def forbid(rel: str, pattern: str, why: str) -> None:
        if re.search(pattern, read(rel), re.I | re.M | re.S):
            failures.append(f"{rel} contains stale semantic claim: {why}")

    for f in BOOT_FILES:
        if not f.exists():
            failures.append(f"MISSING boot file: {f}")

    # Cross-file semantic contracts that simple stale-word scans cannot catch.
    for rel in ("START_HERE.md", "00-BRAIN/vault_map.md",
                "ROOT_OPERATING_MANUAL.md"):
        require(rel, r"77-INBOX.{0,100}manual|manual.{0,100}77-INBOX",
                "77-INBOX is the manual external-file intake")
        require(rel, r"Clippings.{0,120}automatic|automatic.{0,120}Clippings",
                "root Clippings is automatic Obsidian intake")
    forbid("00-BRAIN/vault_map.md", r"77-INBOX[^\n]*Clippings\\ inside",
           "Clippings nested inside 77-INBOX")
    forbid("START_HERE.md", r"Real client artifacts land here",
           "active client artifacts stored in 05-BUSINESS")
    forbid("ROOT_OPERATING_MANUAL.md", r"filled business/client artifact",
           "active client artifacts stored in 05-BUSINESS")
    for rel in ("00-BRAIN/AGENT.md", "00-BRAIN/WHERE_IT_GOES.md",
                "ROOT_OPERATING_MANUAL.md", "03-WIKIS/BUSINESS/CLAUDE.md",
                "03-WIKIS/BUSINESS/HOW_TO_USE.md",
                "05-BUSINESS/06-Capability Library/README.md"):
        require(rel, r"client-specific.{0,140}(separate client workspace|outside `?\.ROOT`?)",
                "active client-specific work stays outside .ROOT")
    for rel in ("00-BRAIN/AGENT.md", "00-BRAIN/CODEX.md",
                "00-BRAIN/CLAUDE.md", "ROOT_OPERATING_MANUAL.md"):
        require(rel, r"independent challenger/validator",
                "consequential work has an independent challenge default")
    forbid("START_HERE.md", r"lane files?.{0,100}HATS.{0,30}roles",
           "retired surface-lane and HATS-role terminology")
    forbid("03-WIKIS/BUSINESS/CLAUDE.md",
           r"filled/used client artifacts.{0,80}05-BUSINESS",
           "active client instances routed into .ROOT/05-BUSINESS")
    forbid("03-WIKIS/BUSINESS/HOW_TO_USE.md",
           r"filled output goes to `?\.ROOT\\05-BUSINESS",
           "active client instances routed into .ROOT/05-BUSINESS")
    forbid("03-WIKIS/BUSINESS/wiki/index.md",
           r"Filled client artifacts live in `?\.ROOT\\05-BUSINESS",
           "active client instances routed into .ROOT/05-BUSINESS")
    forbid("05-BUSINESS/06-Capability Library/README.md",
           r"client instance.{0,180}matching `?05-BUSINESS",
           "active client instances routed into .ROOT/05-BUSINESS")
    require("00-BRAIN/AGENT.md",
            r"temporal update.{0,100}context-dependent variant.{0,100}true contradiction",
            "wiki claim changes are classified before replacement")
    require("00-BRAIN/CASTLE/wiki/opportunity-queue.md", r"\| OPP-\d{8}-\d{2} \|",
            "the live opportunity queue contains at least one evidence-backed item")

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
                "TECHNOLOGY", "AI_AUTOMATION_SYSTEMS", "SYSTEMS",
                "REVENUE_LAB")},
        }
        missing_raw = sorted(required_raw - set(filesystem.get("denyWrite", [])))
        if missing_raw:
            failures.append(f"Sandbox missing raw write-deny paths: {missing_raw}")
    except FileNotFoundError:
        failures.append("MISSING .claude/settings.local.json safety configuration")
    except json.JSONDecodeError as exc:
        failures.append(f"INVALID .claude/settings.local.json: {exc}")

    # Nested-settings shadow guard: Claude Code loads settings from the launch
    # directory's .claude with no parent fallback, so any nested settings file
    # below the root can silently change permission behavior. These files are
    # gitignored and therefore invisible to repository review. Make them visible
    # here: only the root settings file may carry `allow` rules; every nested
    # settings file must keep allow empty and preserve the launch-independent
    # privacy/destructive denies.
    NESTED_REQUIRED_DENY = {
        "Read(**/88-JOURNAL/**)", "Edit(**/88-JOURNAL/**)",
        "Write(**/88-JOURNAL/**)", "Edit(**/raw/**)", "Write(**/raw/**)",
        "Bash(rm *)",
    }
    settings_skip = {"99-ARCHIVE", ".git", "Report Archive"}
    for sp in sorted(ROOT.rglob(".claude/settings*.json")):
        if sp == settings_path:
            continue
        if settings_skip.intersection(sp.relative_to(ROOT).parts):
            continue
        rel = sp.relative_to(ROOT)
        try:
            nested = json.loads(sp.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"INVALID nested settings {rel}: {exc}")
            continue
        nperms = nested.get("permissions", {})
        if nperms.get("allow"):
            failures.append(
                f"nested settings {rel} carries {len(nperms['allow'])} allow "
                f"rule(s); only root .claude may grant permissions")
        nmissing = sorted(NESTED_REQUIRED_DENY - set(nperms.get("deny", [])))
        if nmissing:
            failures.append(
                f"nested settings {rel} missing launch-independent denies: {nmissing}")
    agent_text = (ROOT / "00-BRAIN" / "AGENT.md").read_text(
        encoding="utf-8", errors="replace")
    for marker in ("## Agent Evaluation Gate", "typical, edge, and failure/recovery",
                   "Review the full action trace"):
        if marker not in agent_text:
            failures.append(f"AGENT.md missing evaluation control: {marker}")

    skill_check = ROOT / "00-BRAIN" / "scripts" / "sync_shared_skills.py"
    try:
        result = subprocess.run(
            [sys.executable, str(skill_check), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
        if result.returncode:
            failures.append(
                "shared skill validation failed: "
                + (result.stdout + result.stderr).strip().replace("\n", " | ")
            )
    except (OSError, subprocess.TimeoutExpired) as exc:
        failures.append(f"shared skill validation could not run: {exc}")

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
