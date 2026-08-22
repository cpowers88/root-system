---
type: skill
timeline: now
category: technical
status: building
tags: [skill]
---

# SQL / SQLite

**One-line definition**: Querying and modeling relational data — schema design, joins,
filtering, aggregation — well enough to turn messy real data into a traceable answer.
**Phase**: [[phase-0-current-position-and-baseline]] (active build) → carries into
[[phase-1-school-core-technical-foundation]] (real school-workflow use) →
[[phase-3-data-and-workflow-systems-foundation]] (data/workflow systems)
**Minimum useful level**: Can design a normalized multi-table schema from scratch, write
joins/filters/aggregates without looking up syntax, and go from a raw export to an
answered question end-to-end without help.

## What This Skill Is
Relational thinking (tables, keys, relationships) plus the SQL to query it: SELECT/WHERE/
JOIN/GROUP BY/aggregate functions, schema design with foreign keys, and — eventually —
reading messy real-world data into that shape before querying it.

## Why It Matters
Confirmed the #1 skill gap at the July monthly review ([[current-position]],
capability_development_goal.md). The current tracker provides school and real-data proof;
decision-facing visuals require traceable calculations; later data pipelines,
integrations, and database-backed applications require reliable schema/query work.
Commercial waste quantification is one current-strategy application, not the only
reason to build the capability.

## What Problem It Solves
Real workflows produce scattered rows, repeated fields, and questions that cannot be
answered safely by scanning a spreadsheet. SQL turns structured data into reproducible
answers while preserving relationships and calculation provenance.

## Outcome or Value It Enables
- **Academic:** reliable use of verified tracker/course data and stronger database
  foundations for computing and engineering work.
- **Technical:** schema design, data validation, integrations, dashboards, and
  database-backed applications.
- **Operational:** repeatable answers, provenance, anomaly detection, and decision
  support from workflow data.
- **Employability:** demonstrable relational modeling and query capability.
- **Commercial hypothesis:** evidence-based waste quantification and data/dashboard
  work when a real observation or client question justifies it.
- **Reusable asset:** tested schemas, queries, imports, and validation patterns.

## Source Support
| Source | Tier | Location |
|---|---|---|
| KSU_Academic_Tracker_Brief.md | internal, spine | `02-LIBRARY\.PROJECTS\KSU_Academic_Tracker\` |
| Practical SQL (Anthony DeBarros) | 1, inventoried not yet curriculum-built | `03-WIKIS\PYTHON\wiki\source-summaries\` (migrated from FORGE July 7, 2026; raw PDF in `03-WIKIS\PYTHON\raw\books\`) |
| Luke Barousse SQL course | 3, support | web — 20-min off-day reps |
| CSE 1321 + Lab | 1, spine | `04-SCHOOL\01-CSE-Python\` — Fall 2026 course itself |

## Proof Project
[[ksu-academic-tracker]] — 4-table schema (courses, assignments, tests, readings),
foreign keys, real queries (`--week`, `--today`, `--tests`, `--course`, `--overdue`).
The next proof is correct use against verified course data when the real workflow
requires it, with observed friction recorded and corrected.

## Current Applied Evidence

On July 21, the MCP Bootcamp Day 3 rep converted six real observation rows into a
two-table SQLite fixture (`friction_categories` + `businesses`) with a foreign-key
relationship. Chris chose the separated-table shape, repaired a misplaced SQL
fragment and a repeat-run table collision with support, and correctly explained the
foreign-key link. AI completed the remaining insert code at Chris's explicit request
after several correction cycles, so this is guided-build and debugging evidence—not
an independent-build or mastery claim. Reusable implementation reference:
`03-WIKIS\TECHNOLOGY\wiki\database-sql\sql-python-sqlite3-integration.md`.

## Prerequisites
Relational concepts, tables/rows/keys, and careful question definition are the active
prerequisites. Python Stage 3 is the live curriculum frontier; later data-shape and
file-handling stages support ingestion but are not prerequisites for every SQL rep.

## What Comes Next
First independently query or make one bounded extension to the Bootcamp fixture so
the assistance level can be measured. When D2L populates, use verified tracker data
and produce correct schema/query answers in the real school workflow. After that,
design a schema from a justified CSV/Excel or workflow dataset rather than inventing
a client export in advance.

## What to Park
Query optimization, indexing strategy, and multi-database administration — not needed
until client data volume actually demands it (Phase 7+). Don't chase performance tuning
on a personal tracker with a few hundred rows.
