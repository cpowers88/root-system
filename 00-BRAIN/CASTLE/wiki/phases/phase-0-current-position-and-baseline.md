---
type: phase
timeline: now
stage: phase-0
status: active
tags: [phase]
---

# Phase 0 — Current Position & Baseline

**Window**: July 2026
**One-line purpose**: Know exactly where the start line is, and ship the first proof project.

## Purpose
Establish a written, honest baseline of skills, assets, and gaps — and move the
shipped KSU Academic Tracker from synthetic tests to real D2L/syllabus data when it
opens (~July 25). A roadmap from an unknown starting point is fiction.

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
| SKILL_GAP_ANALYSIS.md | internal-spine | `01-NORTH_STAR\` | The gap priority order |
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
- [ ] Real syllabus data entered when D2L opens (~July 25)
- [ ] August 1 monthly review updates the weak links

## Risks and Distractions
- Building the castle instead of the tracker (planning-as-avoidance — named risk)
- Expanding tracker scope beyond the brief (two functions only; no dashboard)

## Next Action
Around July 25, enter real D2L/syllabus data and run the shipped command set against
it. Until then, SQL work is maintenance and focused practice—not tracker expansion.
