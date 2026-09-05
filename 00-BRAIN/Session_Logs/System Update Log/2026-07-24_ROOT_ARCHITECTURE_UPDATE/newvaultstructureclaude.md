---
type: proposal
timeline: reference
status: implemented-partial
tags: [governance, system-evolution]
created: 2026-07-24
---

# `.ROOT` Structure Synopsis — v3 evidence-aligned proposal

**Status:** Evidence-aligned synopsis reconciled to the implemented 2026-07-24 meta-layer. **Updated 2026-07-25 — CASTLE elevation is retired, not gated.** CASTLE stays at `00-BRAIN\CASTLE\`; no impact audit is owed. Sections below that describe elevation as a live candidate are historical.
**Primary design authority:** `vault-skeleton-design.md`; this file is only the folder/file synopsis.
**Implementation packet:** `00-BRAIN\Session_Logs\System Update Log\2026-07-24_ROOT_ARCHITECTURE_UPDATE\SESSION_INDEX.md`
**Supersedes for discussion:** `99-ARCHIVE/ARCHIVED_2026-07-24_newvaultstructure.md`
**Date:** July 24, 2026

---

## The one thing this restructure gets right

*Historical — 2026-07-25: the hypothesis below was tested and declined. The
evidence never appeared, so CASTLE stays at `00-BRAIN\CASTLE\`. What survives
and still governs is the authority model in the next section, which was never
contingent on the move.*

CASTLE may come out of `00-BRAIN/CASTLE/` and up to the top level, but that is now a hypothesis requiring a deterministic read-only impact report and no-write dry run. The morning architecture review did not prove that nesting currently causes enough navigation, loading, ownership, or maintenance failure to justify the move.

But "on top" means **operational** apex, not **constitutional** apex. Two things must not be collapsed:

- **Folder position** (`00-` prefix) = what sorts first / opens first. CASTLE first = correct.
- **Authority** (who governs whom) = must not invert.

## Authority model (locked)

Three layers. CASTLE runs the system; it does not rewrite the law above it.

| Layer | Folder(s) | Changes | Role |
|---|---|---|---|
| **Constitution — Direction** | Current `01-NORTH_STAR` | Rarely | Durable direction and contracts; overrides all operating proposals. |
| **Constitution — Behavior** | Current `00-BRAIN` | Rarely | AI behavior, safety, approval boundaries, and coordination. |
| **Engine / Overseer** | Current `00-BRAIN/CASTLE` (candidate future top-level `CASTLE`) | Daily | Sequencing and proof cockpit; relocation is gated, not assumed. |
| **External sensing** | Current `...projectSuccess` (candidate future `Watchtower`) | As signals arrive | Read-only external sensing with a narrow typed handoff to CASTLE. |
| **Material** | `02-LIBRARY`, `03-WIKIS`, `05-BUSINESS`, `77-INBOX`, `88-JOURNAL`, `99-ARCHIVE` | Constantly | Knowledge, work, intake, privacy, and history that CASTLE steers. |

**Authority order when things conflict:**

1. Chris's current explicit request
2. `01-NORTH_STAR` (the truth file)
3. `00-BRAIN` governance (`AGENT.md`, behavior/safety)
4. `00-BRAIN/CASTLE/OPERATIONS.md` (how sessions run the cockpit)
5. Nearest domain `claude.md` / `readme.md` / `how_to_use.md`
6. General assumptions

CASTLE may sort first operationally, but North Star and BRAIN remain above it as law. CASTLE flags a conflict with either—it never silently overrides them.

---

## Recommended folder structure

```
.ROOT/
├── CASTLE/                 → candidate top-level overseer; current live home is `00-BRAIN/CASTLE/`; impact gate required.
│   ├── raw/                → CASTLE intake. Recommendations Chris drops in from the wikis,
│   │                          awaiting extraction into the CASTLE wiki.
│   ├── templates/          → Design + test bench for .ROOT structures/templates not yet rolled
│   │                          out system-wide.
│   ├── wiki/               → CASTLE's steering memory: current position, roadmap, phase map,
│   │                          skill map, decision rules, proof projects, logs.
│   ├── claude.md           → Claude's instruction set for turning raw/ into wiki knowledge that
│   │                          improves the system.
│   ├── agent.md            → Behavior pointer into 00-BRAIN (CASTLE inherits, never overrides).
│   ├── how_to_use.md       → Human quick-start for a CASTLE run.
│   └── operations.md       → Authoritative operating contract for how sessions run CASTLE.
│
├── 00-BRAIN/              → Behavior layer. Who the AI is, how it behaves, safety + approval
│   │                          boundaries, and every AI instruction doc for the rest of .ROOT.
│   ├── agent.md            → Universal AI behavior + boot chain.
│   ├── ai_os_core.md
│   ├── chris.md / chris_core.md   → The person the system serves.
│   ├── claude.md           → Claude surface/capability profile.
│   ├── color_map.yaml      → (was coleor_map.yaml)
│   ├── evening_reading_instructions.md
│   ├── folder_icon_system.md
│   ├── local_machine_map.md
│   ├── morning_launch_instructions.md
│   ├── system_flags.md
│   ├── system_learnings.md
│   ├── vault_map.md
│   ├── where_it_goes.md    → Placement + metadata rules for every artifact.
│   ├── Hats/               → Mode profiles (econ, educator, engineering, operator, physics,
│   │                          python, software, tcom…) the AI wears for a kind of work.
│   ├── Scripts/            → Automation + validation utilities that keep the vault healthy.
│   ├── Session_logs/       → Running reports, review templates (daily/weekly/monthly/quarterly),
│   │                          closed flags, system update log.
│   └── Skills/             → Packaged repeatable procedures (briefs, gates, health checks,
│                              session close).
│
├── 01-NORTH_STAR/         → THE TRUTH FILE. Durable direction — the why and where. Overrides all.
│   ├── Goals_and_Milestones/
│   │   ├── current_strategy.md
│   │   ├── current_school_plan.md
│   │   ├── weekly_plan.md
│   │   └── weekly_plan_template.md
│   └── System_Contracts/
│       ├── root_capability_contract.md      → Canonical System Loop + Return Packet.
│       └── root_information_flow_contract.md → Information-state translation + seven-line trace.
│
├── 03-WIKIS/             → Living knowledge domains. Each wiki is a bounded raw→wiki learning
│   │                         engine (intake → extract → classify → update → index) for one field.
│   │                         Where learning becomes durable capability CASTLE harvests.
│   ├── AI_automation_systems/   (raw/ · wiki/ · claude.md · how_to_use.md · readme.md)
│   ├── Business/                (raw/ · wiki/ · claude.md · how_to_use.md · readme.md)
│   ├── Education/               (raw/ · wiki/ · claude.md · how_to_use.md · readme.md)
│   ├── Physics/                 (raw/ · wiki/ · claude.md · how_to_use.md · readme.md)
│   ├── Python/                  (raw/ · wiki/ · claude.md · how_to_use.md · readme.md)
│   ├── Revenue_Lab/             (raw/ · wiki/ · claude.md · how_to_use.md · readme.md)
│   ├── Systems/                 (raw/ · wiki/ · claude.md · how_to_use.md · readme.md)
│   └── Technology/              (raw/ · wiki/ · claude.md · how_to_use.md · readme.md)
│
├── 02-LIBRARY/          → Reference shelf + project holding. Static, look-it-up material.
│   │                        Read-mostly; NOT an active learning engine like a wiki.
│   ├── .projects/
│   ├── 00-SCHOOL/
│   ├── REF-Business/     → (was REF-Buisness)
│   ├── REF-Field-Operations/
│   ├── REF-Health/
│   ├── REF-Math/
│   ├── REF-Meta-how-to-work/
│   ├── REF-Misc/
│   └── REF-Programming/
│       └── syntax-cheat-sheets/
│
├── 05-BUSINESS/         → Revenue workspace. Client-facing, revenue-producing assets. Where the
│   │                        AI-operations business is actually built and sold.
│   ├── audit_templates/
│   ├── field_notes/
│   ├── case_studies/
│   ├── pricing_models/
│   ├── proposals_and_SOWs/
│   └── capability_library/
│
├── 77-INBOX/            → Single universal intake door; web clips now land here and are routed
│                           to a wiki raw/, the Library, or CASTLE raw/. Resolved 2026-07-24.
│
├── 88-JOURNAL/          → Personal record. Journal, notes, stray thoughts, therapy notes,
│                           reflection. The human layer, kept out of operating governance.
│
├── 99-ARCHIVE/          → Cold storage. Dated, obsolete-but-preserved material. Nothing deleted;
│                           retained for provenance and reversal.
│
└── `...projectSuccess/` → current Watchtower home; keep sensing separate from CASTLE and test
                            any future rename/move independently.
```

---

## Rules for CASTLE (the new part — this is what makes elevation safe)

1. **CASTLE serves, it does not rule.** It reads `01-NORTH_STAR` and `00-BRAIN` and steers toward them. It cannot rewrite either. On conflict with the North Star or a safety/behavior boundary, CASTLE **stops and flags** — it never resolves silently.

2. **CASTLE decides sequence; it does not own truth.** It points to the authoritative source (North Star, a wiki, a contract) and records only the decision or proof state needed to steer. No copying owner truth into CASTLE.

2a. **CASTLE is not read-only.** It may write CASTLE-owned maps, decisions,
logs, proof-status updates, indexes, `NOW.md` updates, and approved return
packets. It may also apply ordinary reconciliations that `OPERATIONS.md`
already authorizes. It may not silently rewrite North Star, governance,
owner-truth pages, immutable `raw/`, private journal material, or another
realm's content. Watchtower remains the read-only sensing surface; its typed
handoff is what CASTLE evaluates and records.

3. **Watchtower → radar → gate.** Watchtower surfaces candidate upgrades; radar ranks them against the North Star; only gated items become work. Unranked ideas don't jump straight to implementation.

4. **A CASTLE decision names five things:** why now, owner (realm + human approval boundary), the one next action sized to real capacity, the proof that closes it, and the return file that receives the result.

5. **Work happens in the owning realm.** Verified results return to CASTLE only when they change sequence, proof status, or the live operating picture.

6. **Chris owns direction, timing, capacity, and consequential decisions.** CASTLE proposes; Chris disposes.

---

## Evidence gate before execution — CLOSED 2026-07-25

*Item 1 is retired: no move-impact inventory is owed, because there is no
candidate move. Items 2–5 remain the standing requirements for any **future**
structural change, and item 5 is already settled.*

1. ~~Produce a read-only move-impact inventory and no-write dry run for the candidate CASTLE elevation.~~ **Retired — relocation declined.**
2. Validate four explicit scanner checks: path moves, resolvable references/anchors, canonical-copy violations, and instruction-register conformance.
3. Define dependency discovery, performance budget, abort/rollback triggers, fresh-session acceptance, and a post-change `check_at` before any move.
4. Keep Watchtower separate and test its typed handoff; do not merge it into CASTLE by default.
5. Treat `77-INBOX` as resolved. Naming cleanups are separate, bounded decisions—not automatic side effects of this proposal.

## Execution risk — resolved by declining the move (2026-07-25)

The risk below is why the move needed proof, and no proof arrived. Preserved
because it is the standing cost estimate for anyone who proposes relocating
CASTLE again:

> Moving CASTLE from `00-BRAIN/CASTLE` will affect hardcoded paths in
> `AGENT.md`, `START_HERE.md`, `NOW.md`, `ROOT_OPERATING_MANUAL.md`, and the
> CASTLE docs. Any approved move must inventory and update those pointers in
> the same change, or the boot chain breaks.

**Next action:** none. CASTLE stays where it is. This file is a folder/file
synopsis only — `vault-skeleton-design.md` is the design authority and
`00-BRAIN\Session_Logs\System Update Log\2026-07-24_ROOT_ARCHITECTURE_UPDATE\SESSION_INDEX.md`
is the closed evidence packet. Reopening relocation requires new evidence of a
live failure caused by the nesting, not another proposal.
