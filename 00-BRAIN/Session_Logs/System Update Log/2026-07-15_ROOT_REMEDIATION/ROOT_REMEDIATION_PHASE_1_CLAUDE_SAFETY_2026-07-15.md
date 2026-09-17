---
type: plan
tags: [governance, audit]
status: complete
created: 2026-07-15
timeline: now
---

# Phase 1 — Canonical Claude Safety

## Outcome

Claude has one reviewable `.ROOT` project policy, launch-independent user-level
Claude-tool denies for `.ROOT`'s journal/raw boundaries and destructive commands,
no nested settings shadows, and a validator that fails if any part of that design
drifts. The native-Windows subprocess limitation remains explicit rather than being
misreported as OS-level enforcement.

## Evidence

- Baseline commit: `af8e3ba` (`Phase 0: stabilize remediation baseline and loop protocol`).
- Claude Code version: `2.1.210`.
- User settings at `C:\Users\chris\.claude\settings.json` contain interface
  preferences only; they contain no safety rules.
- `.ROOT\.claude\settings.json` does not exist.
- `.ROOT\.claude\settings.local.json` mixes portable safety policy with
  machine-specific allow rules.
- Eight ignored `03-WIKIS\**\.claude\settings.local.json` files exist and share
  SHA-256 `5317ba14d577674c...`; originals are preserved in
  `99-ARCHIVE\ARCHIVED_2026-07-15_nested-claude-settings\`.
- The baseline boot validator reports PASS even while those eight settings files
  exist because it accepts partial nested copies instead of rejecting shadows.
- Current Claude documentation confirms user settings apply across projects,
  permission rules resolve deny → ask → allow, `/path` rules are relative to the
  settings source, `~/path` rules are home-relative, and file-tool denies do not
  constrain arbitrary subprocesses. Claude's OS-level sandbox is unavailable in
  native Windows, so project sandbox settings are defense in depth for supported
  environments, not the native-Windows hard boundary.

## Owned paths

- `.claude\settings.json`
- `.claude\settings.local.json`
- `.claude\user-settings-policy.template.json`
- `C:\Users\chris\.claude\settings.json` (deployment target)
- non-archived nested `03-WIKIS\**\.claude\settings*.json`
- `00-BRAIN\scripts\validate_boot_chain.py`
- `ROOT_OPERATING_MANUAL.md`
- `00-BRAIN\Session_Logs\ROOT_SYSTEM_INTEGRITY_AUDIT_2026-07-15_CODEX.md`
- this brief and `00-BRAIN\Session_Logs\DAILY_2026-07-15.md`

## Exclusions

- `88-JOURNAL\` and every `raw\` folder remain unread and unwritten.
- Claude's concurrent school lane (`03-WIKIS\EDUCATION`, `PHYSICS`, `PYTHON`
  content/current-position/log files) is excluded; only the ignored nested
  settings files inside those hubs may be removed under this safety phase.
- `NOW.md`, CASTLE content, skills, hooks, wiki/frontmatter validators, metadata,
  and root-health orchestration are deferred.
- Windows registry/managed settings are not changed. The user-scope policy is
  reviewable but not administrator-enforced.

## Acceptance tests

1. Project, user-template, deployed-user, and local settings parse as JSON.
2. Required journal/raw/destructive denies exist at user and project scope.
3. Manual/default mode is active; bypass and auto modes are disabled.
4. The machine-local file contains allow rules only and cannot override safety.
5. No non-archived nested `.claude\settings*.json` exists.
6. A temporary nested settings probe makes the boot validator return nonzero;
   removing the probe restores PASS.
7. Existing boot, wiki, frontmatter, shared-skill, and diff checks do not regress.
8. In fresh Claude sessions, Chris verifies `/status` and `/permissions` once at
   `.ROOT` and once from a former nested launch location. This human behavior test
   cannot be proven by editing the live session.

## Rollback boundary

The Phase 1 diff begins at `af8e3ba`. The eight removed nested files can be
restored from their dated archive; the user settings file is backed up before
deployment. No Phase 2 work enters this boundary.

## Human decision

After Pass 1 plus adversarial Loop 1 and optional Loop 2, Chris chooses:
**approve**, **revise once more**, **hold**, or **reject**. Phase 2 cannot start
before that stop.

## Pass record

### Pass 0 — baseline

- Working tree clean; no Codex-owned file has a concurrent edit.
- Nested settings shadows: 8.
- User-scope required safety rules: 0.
- Tracked project policy: absent.
- Boot validator: false PASS with all eight shadows present.

### Pass 1 — smallest coherent implementation

- Added tracked `.claude\settings.json` as the reviewable project policy.
- Added `.claude\user-settings-policy.template.json`, preserved the existing
  interface preferences, backed up the live user settings to
  `C:\Users\chris\.claude\settings.pre-phase1-2026-07-15.json`, and deployed the
  template to `C:\Users\chris\.claude\settings.json`.
- Reduced ignored `.claude\settings.local.json` to machine-specific allow
  candidates only. Project `ask` rules still outrank these candidates, so they
  cannot bypass manual confirmation.
- Removed all eight nested settings files after verifying their archived originals.
- Replaced partial-copy validation with complete user/project/local role checks and
  a zero-tolerance nested-shadow guard.
- Added a concise human launch/verification procedure to `ROOT_OPERATING_MANUAL.md`.

### Loop 1 — adversarial refinement

- Rechecked the design against the live Claude 2.1.210 documentation. Corrected the
  audit's unproven “no parent fallback” explanation and documented that Claude's
  OS-level sandbox is unavailable on native Windows.
- Injected `77-INBOX\.claude\settings.local.json`; the validator returned 1 with
  the exact shadow path. Removed the probe; PASS returned.
- Removed one required user-template raw deny; the validator returned 1 naming the
  exact missing rule. Restored it; PASS returned.
- Measurable gain: nested settings accepted by the validator **8 → 0**; user-level
  required safety controls **0 → 14** (11 denies plus 3 mode controls); tracked
  project safety policy **absent → present**.

### Loop 2 — capability-parity refinement

Chris requested one final pass specifically to prove that safety does not shrink
Claude's `.ROOT` job. The pass mapped the universal capability contract and Claude
profile to the effective permission policy:

| Required work | Effective access | Result |
|---|---|---|
| Orient, search, route, and audit | Read/Grep/Glob available everywhere except `88-JOURNAL` | PASS |
| Research and maintain evidence | raw may be read; non-raw wiki/index/log files may be written with approval | PASS |
| Teach and update learning systems | all school/wiki working files remain available; academic rules still govern | PASS |
| Build, script, test, and validate | Edit/Write/Bash/PowerShell available through prompts; exact validators remain local allow candidates | PASS |
| Operate CASTLE, North Star, projects, and business assets | no path deny applies outside journal/raw | PASS |
| Build skills, tools, agents, and extensions | no Skill, Agent, MCP, plugin, or project-path deny exists | PASS |
| Use web and connected services | Web tools remain available; MCP calls are approval-gated, not denied | PASS |
| Version, preserve, and checkpoint | normal Git and archive/move operations remain available; destructive reset/clean/delete commands stay blocked | PASS |

The existing validator checked for missing safety rules but would have accepted an
additional broad deny that silently removed a capability. Loop 2 now requires the
deny sets to match the reviewed boundary exactly and rejects extra project `ask`
rules that add unreviewed prompt friction. This protects both sides of the design:
required safety cannot disappear, and Claude's working role cannot quietly shrink.
Adversarial proof: a temporary bare `Read` deny failed with the exact capability-
restriction finding; a temporary bare `Read` ask failed with the exact prompt-
friction finding; restoring both returned the validator to PASS.

No permission was loosened. The effective model remains: **all `.ROOT` work is
available except journal access, raw modification, destructive shell cleanup, and
actions stopped by the universal human-governance rules.**

### Validation and human-review stop

- Boot chain: PASS (30 boot files / 1094 live pages).
- Strict wiki lint: 0 blockers / 0 review debt / 716 expected.
- Frontmatter baseline: 620 known findings; no regression.
- Shared skills: PASS (4 canonical / 2 mirrors).
- `claude doctor`: native 2.1.210, no installation issues.
- `git diff --check`: clean except expected line-ending notices.
- Nested non-archived settings files: 0.
- Human-only check still required: start fresh Claude sessions from `.ROOT` and one
  former nested location; run `/status` and `/permissions`; confirm user + project
  sources and the deny rules. Settings changes cannot alter the already-open session.

**Human decision:** approved by Chris on July 15, 2026 after the capability-parity
Loop 2 review. Chris accepted the root/subfolder `claude doctor`, deterministic
policy checks, and adversarial probes as the bounded evidence for checkpointing;
fresh-session `/status` and `/permissions` remain a non-blocking operational spot-
check because Codex cannot enter those interactive menus. Phase 1 is complete and
ready for its isolated checkpoint.
