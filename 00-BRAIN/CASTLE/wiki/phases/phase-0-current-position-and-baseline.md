---
type: phase
timeline: log
stage: phase-0
status: complete
tags: [phase]
closed: 2026-08-19
---

# Phase 0 — Current Position & Baseline — CLOSED 2026-08-19

**Window**: July 2026
**One-line purpose**: Know exactly where the start line is, and ship the first proof project.

> **Closure record (Chris-approved 2026-08-19, flag #103 repair).** Closed 19 days
> after its window on work that genuinely happened, not on a waiver:
>
> - Baseline, CASTLE maps, and the shipped tracker closed in July (criteria 1–3 below).
> - The "August 1 monthly review" criterion pointed at an event that never existed:
>   July's monthly was an explicit **early close on Jul 25** whose "next packet" was
>   never written. The weak-link work it asked for was done anyway —
>   `capability_development_goal.md` (Jul 24, 6-rank table) and the four-seat Council
>   review (Aug 11). Recorded as **superseded by those two artifacts**.
> - The "verified Fall 2026 course data" criterion is **moved to Phase 1**, which
>   already owns the same outcome in two of its own exit criteria — it was misfiled
>   here one phase early; D2L cannot populate before Aug 24, inside Phase 1's window.
>
> Why it sat open: no review read this page between Jul 25 and Aug 19 — the cadence
> failure recorded in flag #103, not missing work.

## Purpose
Establish a written, honest baseline of skills, assets, and gaps — and move the
shipped KSU Academic Tracker from synthetic tests to verified D2L/syllabus data when
the Fall 2026 course shells populate (expected August 24 or later). A roadmap from
an unknown starting point is fiction.

## Why It Matters to the North Star
Every later phase measures progress against this baseline. The tracker is also the
live fix for the #1 skill gap (SQL) and the walking-into-CSE-1321-loaded advantage.

## Skills Needed
- Python fundamentals (CS50P pace) — active
- SQL/SQLite basics — trained by the tracker build
- Honest self-assessment — the monthly weak-link question

## Skills NOT Needed Yet
- Web applications, APIs, and automation platforms — wait for a verified need
- Sales/outreach skills — Phase 4
- Any parked skill or idea that has not passed the active CASTLE gate

## Best Sources
| Source | Tier | Location | What it proves |
|---|---|---|---|
| capability_development_goal.md | internal-spine | `01-NORTH_STAR\Goals & Milestones\` | The capability stack and weak-link priority order |
| KSU_Academic_Tracker_Brief.md | internal-spine | `02-LIBRARY\.PROJECTS\KSU_Academic_Tracker\` | Scope + data model of the proof project |
| CS50P (Harvard) | 1 | online | Python path |

## Tools or Methods in the Current Proof
sqlite3, argparse, datetime (all inside the tracker build)

## Capability and Value Enabled
The shipped tracker demonstrates bounded Python/SQLite CLI delivery: a four-table
schema, working queries, argument handling, date logic, tested terminal output, and
scope discipline. That is real technical and delivery evidence. Still unproven are
reliability on verified course data, continued usefulness in the live school
workflow, independent transfer of every underlying skill, and any client or market
outcome. Honesty requires preserving both sides of that boundary.

## Proof Projects
- [[ksu-academic-tracker]] — V1 shipped July 8; real-data use remains the proof

## Exit Criteria
- [x] [[current-position]] written and reviewed by Chris (July 6)
- [x] Castle live with maps, phases 0–2, source map (July 6)
- [x] Tracker: all four tables + `--week`, `--today`, `--tests`, `--course`, `--overdue` working (V1 shipped July 8)
- [ ] Verified Fall 2026 course data entered when D2L populates (expected August 24 or later)
- [ ] August 1 monthly review updates the weak links

## Risks and Distractions
- Building the castle instead of the tracker (planning-as-avoidance — named risk)
- Expanding tracker scope beyond the brief (two functions only; no dashboard)

## Next Action
When D2L populates with verified Fall 2026 data, enter it and run the shipped command
set against the real workflow. Until then, use the Bootcamp fixture and other bounded
real-data reps for SQL practice—not tracker expansion or invented course data.
