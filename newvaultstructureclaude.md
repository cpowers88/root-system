# NEW VAULT STRUCTURE — v2 (Claude recommendation, for Chris review)

**Status:** Draft for review. Nothing has been moved. This is the spec — approve it, then execution follows.
**Supersedes for discussion:** `newvaultstructure.md`
**Date:** July 23, 2026

---

## The one thing this restructure gets right

CASTLE comes out of `00-BRAIN/CASTLE/` and up to the top level, where it can see the files it needs to operate. Every `.ROOT` load already starts with a CASTLE run — so CASTLE is made the standing overseer that drives the system toward the North Star, instead of being nested where it can't reach.

But "on top" means **operational** apex, not **constitutional** apex. Two things must not be collapsed:

- **Folder position** (`00-` prefix) = what sorts first / opens first. CASTLE first = correct.
- **Authority** (who governs whom) = must not invert.

## Authority model (locked)

Three layers. CASTLE runs the system; it does not rewrite the law above it.

| Layer | Folder(s) | Changes | Role |
|---|---|---|---|
| **Constitution — Direction** | `02-NORTH_STAR` | Rarely | The truth file. The durable *why* and *where*. Overrides everything. |
| **Constitution — Behavior** | `01-BRAIN` | Rarely | Who the AI is, how it behaves, safety and approval boundaries, all AI instruction docs for the rest of the structure. |
| **Engine / Overseer** | `00-CASTLE` | Daily | Reads the constitution, scans the wikis, scouts upgrades, picks the next best action, drives execution toward the North Star. |
| **Material** | `03`–`05`, `88`, `99`, `Clippings` | Constantly | The knowledge and work CASTLE steers. |

**Authority order when things conflict:**

1. Chris's current explicit request
2. `02-NORTH_STAR` (the truth file)
3. `01-BRAIN` governance (`AGENT.md`, behavior/safety)
4. `00-CASTLE/OPERATIONS.md` (how sessions run the overseer)
5. Nearest domain `claude.md` / `readme.md` / `how_to_use.md`
6. General assumptions

CASTLE sorts first and drives the day. North Star and BRAIN sit above it as law. CASTLE flags a conflict with either — it never silently overrides them.

---

## Recommended folder structure

```
.ROOT/
├── 00-CASTLE/              → .ROOT overseer + engine. Runs the system toward the North Star.
│   ├── watchtower.md       → Forward scout. Continuously looks for upgrades, new tools, and
│   │                          capability gains and puts candidates on the radar.
│   ├── radar.md            → Triage + staging. Pulls candidates from watchtower and the wikis,
│   │                          ranks them against the North Star, promotes the best to implement.
│   ├── raw/                → CASTLE intake. Recommendations Chris drops in from the wikis,
│   │                          awaiting extraction into the CASTLE wiki.
│   ├── templates/          → Design + test bench for .ROOT structures/templates not yet rolled
│   │                          out system-wide.
│   ├── wiki/               → CASTLE's steering memory: current position, roadmap, phase map,
│   │                          skill map, decision rules, proof projects, logs.
│   ├── claude.md           → Claude's instruction set for turning raw/ into wiki knowledge that
│   │                          improves the system.
│   ├── agent.md            → Behavior pointer into 01-BRAIN (CASTLE inherits, never overrides).
│   ├── how_to_use.md       → Human quick-start for a CASTLE run.
│   └── operations.md       → Authoritative operating contract for how sessions run CASTLE.
│
├── 01-BRAIN/              → Behavior layer. Who the AI is, how it behaves, safety + approval
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
├── 02-NORTH_STAR/         → THE TRUTH FILE. Durable direction — the why and where. Overrides all.
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
├── 04-LIBRARY/          → Reference shelf + project holding. Static, look-it-up material.
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
├── 77-INBOX/            → Fast, unsorted capture from anywhere. Routed OUT to a wiki raw/, the
│                           Library, or CASTLE raw/. (Decide: keep, or fold into Clippings +
│                           CASTLE/raw — see open question below.)
│
├── 88-JOURNAL/          → Personal record. Journal, notes, stray thoughts, therapy notes,
│                           reflection. The human layer, kept out of operating governance.
│
├── 99-ARCHIVE/          → Cold storage. Dated, obsolete-but-preserved material. Nothing deleted;
│                           retained for provenance and reversal.
│
└── Clippings/           → Raw inbound web/reading capture awaiting routing into a wiki raw/ or
                            the Library.
```

---

## Rules for CASTLE (the new part — this is what makes elevation safe)

1. **CASTLE serves, it does not rule.** It reads `02-NORTH_STAR` and `01-BRAIN` and steers toward them. It cannot rewrite either. On conflict with the North Star or a safety/behavior boundary, CASTLE **stops and flags** — it never resolves silently.

2. **CASTLE decides sequence; it does not own truth.** It points to the authoritative source (North Star, a wiki, a contract) and records only the decision or proof state needed to steer. No copying owner truth into CASTLE.

3. **Watchtower → radar → gate.** Watchtower surfaces candidate upgrades; radar ranks them against the North Star; only gated items become work. Unranked ideas don't jump straight to implementation.

4. **A CASTLE decision names five things:** why now, owner (realm + human approval boundary), the one next action sized to real capacity, the proof that closes it, and the return file that receives the result.

5. **Work happens in the owning realm.** Verified results return to CASTLE only when they change sequence, proof status, or the live operating picture.

6. **Chris owns direction, timing, capacity, and consequential decisions.** CASTLE proposes; Chris disposes.

---

## Open questions before execution

1. **77-INBOX** — Keep it as the single fast-capture inbox (recommended: keep — one capture door is simpler), or fold it into `Clippings` + `CASTLE/raw/`? Your `newvaultstructure.md` dropped it; decide on purpose so intake isn't orphaned.
2. **Naming cleanups while we're in here:** `coleor_map.yaml → color_map.yaml`, `REF-Buisness → REF-Business`, and Education's `wikis/ → wiki/` to match every other wiki. Approve or skip.

## Execution risk (read before approving)

This is a top-level-folder restructure plus a role expansion for CASTLE. Per change-control it needs your explicit approval before any file moves. Moving CASTLE from `00-BRAIN/CASTLE` and shifting `01-NORTH_STAR → 02-NORTH_STAR` will break every hardcoded path in `AGENT.md`, `START_HERE.md`, `NOW.md`, `ROOT_OPERATING_MANUAL.md`, and the CASTLE docs. Those pointer updates must ship in the same change as the move, or the boot chain breaks.

**Next action:** answer the two open questions. Then I'll produce the exact move-and-update plan (every path, every pointer edit) for your approval before anything is touched.
