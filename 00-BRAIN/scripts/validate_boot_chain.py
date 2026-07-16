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
  7. Claude safety policy exists at user + project scope, local settings cannot
     override it, and no nested settings shadow exists

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
    ROOT / "AGENTS.md", ROOT / "CLAUDE.md", ROOT / "START_HERE.md",
    ROOT / "NOW.md", ROOT / "CODEX.md",
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
    require("AGENTS.md", r"00-BRAIN\\AGENT\.md",
            "Codex root pointer routes to the universal OS")
    require("AGENTS.md", r"00-BRAIN\\CODEX\.md",
            "Codex root pointer routes to the Codex profile")
    require("CLAUDE.md", r"00-BRAIN\\AGENT\.md",
            "Claude root pointer routes to the universal OS")
    require("CLAUDE.md", r"00-BRAIN\\CLAUDE\.md",
            "Claude root pointer routes to the Claude profile")
    require("CODEX.md", r"AGENTS\.md.{0,120}canonical",
            "legacy Codex pointer defers to canonical AGENTS.md")
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

    # Claude safety is split deliberately:
    #   user scope   = launch-independent, non-negotiable deny/mode baseline
    #   project scope = reviewable .ROOT policy, asks, and sandbox defense in depth
    #   local scope  = machine-specific allow candidates only; no safety overrides
    project_settings_path = ROOT / ".claude" / "settings.json"
    local_settings_path = ROOT / ".claude" / "settings.local.json"
    user_template_path = ROOT / ".claude" / "user-settings-policy.template.json"
    user_settings_path = Path.home() / ".claude" / "settings.json"

    def load_json(path: Path, label: str):
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            failures.append(f"MISSING {label}: {path}")
        except json.JSONDecodeError as exc:
            failures.append(f"INVALID {label}: {exc}")
        return None

    project_settings = load_json(project_settings_path, "Claude project settings")
    local_settings = load_json(local_settings_path, "Claude local settings")
    user_template = load_json(user_template_path, "Claude user-policy template")
    user_settings = load_json(user_settings_path, "deployed Claude user settings")

    destructive_deny = {
        "Bash(rm *)", "Bash(rmdir *)", "Bash(git reset --hard*)",
        "Bash(git clean *)", "PowerShell(Remove-Item *)",
        "PowerShell(Clear-Content *)",
    }
    project_required_deny = destructive_deny | {
        "Read(/88-JOURNAL/**)", "Edit(/88-JOURNAL/**)",
        "Write(/88-JOURNAL/**)", "Edit(/**/raw/**)",
        "Write(/**/raw/**)",
    }
    user_required_deny = destructive_deny | {
        "Read(~/.ROOT/88-JOURNAL/**)",
        "Edit(~/.ROOT/88-JOURNAL/**)",
        "Write(~/.ROOT/88-JOURNAL/**)",
        "Edit(~/.ROOT/**/raw/**)",
        "Write(~/.ROOT/**/raw/**)",
    }
    required_modes = {
        "defaultMode": "default",
        "disableBypassPermissionsMode": "disable",
        "disableAutoMode": "disable",
    }

    def validate_permissions(settings, label: str, required_deny: set[str]) -> None:
        if settings is None:
            return
        permissions = settings.get("permissions", {})
        actual_deny = set(permissions.get("deny", []))
        missing = sorted(required_deny - actual_deny)
        if missing:
            failures.append(f"{label} missing deny rules: {missing}")
        unexpected = sorted(actual_deny - required_deny)
        if unexpected:
            failures.append(
                f"{label} has unreviewed capability-restricting deny rules: "
                f"{unexpected}")
        for key, expected in required_modes.items():
            if permissions.get(key) != expected:
                failures.append(
                    f"{label} permissions.{key} must be {expected!r}")

    validate_permissions(project_settings, "Claude project settings",
                         project_required_deny)
    validate_permissions(user_template, "Claude user-policy template",
                         user_required_deny)
    validate_permissions(user_settings, "deployed Claude user settings",
                         user_required_deny)

    if project_settings is not None:
        permissions = project_settings.get("permissions", {})
        required_ask = {"Edit", "Write", "Bash(*)", "PowerShell(*)", "mcp__*"}
        actual_ask = set(permissions.get("ask", []))
        missing_ask = sorted(required_ask - actual_ask)
        if missing_ask:
            failures.append(f"Claude project settings missing ask rules: {missing_ask}")
        unexpected_ask = sorted(actual_ask - required_ask)
        if unexpected_ask:
            failures.append(
                f"Claude project settings has unreviewed prompt-friction rules: "
                f"{unexpected_ask}")
        filesystem = project_settings.get("sandbox", {}).get("filesystem", {})
        if "./88-JOURNAL" not in filesystem.get("denyRead", []):
            failures.append("Claude project sandbox does not deny 88-JOURNAL reads")
        required_raw = {
            "./00-BRAIN/CASTLE/raw",
            *{f"./03-WIKIS/{hub}/raw" for hub in (
                "PYTHON", "PHYSICS", "BUSINESS", "EDUCATION",
                "TECHNOLOGY", "AI_AUTOMATION_SYSTEMS", "SYSTEMS",
                "REVENUE_LAB")},
        }
        missing_raw = sorted(required_raw - set(filesystem.get("denyWrite", [])))
        if missing_raw:
            failures.append(
                f"Claude project sandbox missing raw write-deny paths: {missing_raw}")

    if local_settings is not None:
        unexpected_top = sorted(set(local_settings) - {"$schema", "permissions"})
        if unexpected_top:
            failures.append(
                f"Claude local settings has policy keys outside its role: {unexpected_top}")
        local_permissions = local_settings.get("permissions", {})
        unexpected_permissions = sorted(set(local_permissions) - {"allow"})
        if unexpected_permissions:
            failures.append(
                "Claude local settings may contain only machine-specific allow "
                f"rules; found: {unexpected_permissions}")

    # Root-only configuration: any settings file in a nested .claude directory is
    # a blocker. This guard checks ignored files too, so repository status cannot
    # hide a reintroduced shadow.
    allowed_settings = {project_settings_path, local_settings_path}
    settings_skip = {"99-ARCHIVE", ".git", "Report Archive"}
    for sp in sorted(ROOT.rglob(".claude/settings*.json")):
        if sp in allowed_settings:
            continue
        if settings_skip.intersection(sp.relative_to(ROOT).parts):
            continue
        failures.append(
            f"nested Claude settings shadow is prohibited: {sp.relative_to(ROOT)}")
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
