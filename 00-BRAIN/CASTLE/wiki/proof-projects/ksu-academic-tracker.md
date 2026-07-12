---
type: proof-project
status: active
tags: [proof-project, track-1, track-2, now]
---

# KSU Academic Tracker

**One-line description**: Python + SQLite CLI that answers "what needs attention today/this week" across all five Fall 2026 courses, linking structured data to Obsidian notes.
**Phase served**: [[phase-0-current-position-and-baseline]]
**Deadline / window**: July 5–24, 2026 — before D2L access opens (~July 25)
**Location of work**: `02-LIBRARY\.PROJECTS\KSU_Academic_Tracker\` — brief + tracker.py + academic.db, one folder (Chris consolidated July 8, 2026; flag 53 closed)

## What It Proves
- SQL/SQLite — the **#1 skill gap**: 4-table schema (courses, assignments, tests, readings), foreign keys, real queries
- Python CLI craft: sqlite3, argparse, datetime date-math, clean terminal output
- Scope discipline: two functions only, no dashboard, no web UI — per the brief
- The compounding pattern: tracker is practice, POL is the product, same concepts

## Definition of Done (from the brief)
- [x] Four tables created; courses entered
- [x] `--week`, `--today`, `--tests`, `--course X`, `--overdue` all working (V1 also shipped `--courses`, `--add-test`, `--add-assignment`, `--add-reading`)
- [ ] notes_file paths displayed, linking DB rows to Obsidian markdown — verify during real-data entry
- [ ] Real syllabus data entered once D2L opens (~July 25); works with partial data
- [ ] In daily morning use by August 24

## North Star Connection
Track 2 project serving Track 1 directly. Walking into CSE 1321 having built this
means every classroom concept lands on prior context. Daily use through the semester
is the ongoing proof — an abandoned tracker proves the opposite.

## Status Log
| Date | What happened | Next action |
|---|---|---|
| 2026-06-15 | Brief completed | — |
| 2026-07-05 | Build slot confirmed over POL; Session 1 target | Sessions 2–3 per brief |
| 2026-07-06 | Registered as Phase 0 proof project in the castle | Finish remaining queries; log sessions here |
| 2026-07-08 | **V1 SHIPPED and tested** — all briefed queries plus `--courses` and three `--add-*` commands work. Brief reconciled by Chris (stale future-tense language removed); duplicate brief copy archived. V2 (edit/delete/update, dashboard, web UI) explicitly PARKED — no expansion unless real use exposes the need. | Enter real D2L/syllabus data ~July 25; then daily morning use through the semester — that's the remaining proof |
