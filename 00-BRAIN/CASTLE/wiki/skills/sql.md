---
type: skill
timeline: now
category: technical
status: building
tags: [skill]
---

# SQL / SQLite

**One-line definition**: Querying and modeling relational data — schema design, joins,
filtering, aggregation — well enough to turn a messy business export into an answer.
**Phase**: [[phase-0-current-position-and-baseline]] (active build) → carries into
[[phase-1-school-core-technical-foundation]] (daily use through the semester) →
[[phase-3-data-and-workflow-systems-foundation]] (client-data pipelines)
**Minimum useful level**: Can design a normalized multi-table schema from scratch, write
joins/filters/aggregates without looking up syntax, and go from a raw export to an
answered question end-to-end without help.

## What This Skill Is
Relational thinking (tables, keys, relationships) plus the SQL to query it: SELECT/WHERE/
JOIN/GROUP BY/aggregate functions, schema design with foreign keys, and — eventually —
reading messy real-world data into that shape before querying it.

## Why It Matters
Confirmed the #1 skill gap at the July monthly review ([[current-position]],
SKILL_GAP_ANALYSIS.md). Every later phase assumes it: audit findings need real numbers
pulled from client data (Phase 2–3), dashboards need a query behind them (gap #3), and
Flask/API builds (Phase 3/7) all sit on top of a database. No orphan skill — this is
the one every downstream skill leans on.

## What Business Problem It Solves
Clients hand over messy exports (spreadsheets, CRM dumps, accounting data) and want an
answer, not a spreadsheet. SQL is the difference between "I can look through this" and
"I can tell you exactly where the money is leaking, with numbers."

## What Service It Unlocks
The waste-quantification step of the audit (Phase 2's "findings with numbers in mock
report") and every data-and-dashboard client pathway
(`03-WIKIS\BUSINESS\wiki\ai-integration-company\data-and-dashboard-pathway.md`).

## Source Support
| Source | Tier | Location |
|---|---|---|
| KSU_Academic_Tracker_Brief.md | internal, spine | `02-LIBRARY\.PROJECTS\KSU_Academic_Tracker\` |
| Practical SQL (Anthony DeBarros) | 1, inventoried not yet curriculum-built | `03-WIKIS\PYTHON\wiki\source-summaries\` (migrated from FORGE July 7, 2026; raw PDF in `03-WIKIS\PYTHON\raw\books\`) |
| Luke Barousse SQL course | 3, support | web — 20-min off-day reps |
| CSE 1321 + Lab | 1, spine | `02-LIBRARY\00-SCHOOL\01-CSE-Python\` — Fall 2026 course itself |

## Proof Project
[[ksu-academic-tracker]] — 4-table schema (courses, assignments, tests, readings),
foreign keys, real queries (`--week`, `--today`, `--tests`, `--course`, `--overdue`).
In daily use through the semester is the ongoing proof; an abandoned tracker proves
the opposite.

## Prerequisites
Python fundamentals through Stage 5 (data shapes) — already building per
`03-WIKIS\PYTHON`'s Stage 1-10 curriculum.

## What Comes Next
Reading messy real exports (CSV/Excel from a real or mock business) into a schema
Chris designs himself, not one already given — that's the Phase 3 stretch
(`data-and-dashboard-pathway.md`).

## What to Park
Query optimization, indexing strategy, and multi-database administration — not needed
until client data volume actually demands it (Phase 7+). Don't chase performance tuning
on a personal tracker with a few hundred rows.
