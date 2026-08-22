---
type: phase
timeline: next
stage: phase-3
status: planned
tags: [phase]
---

# Phase 3 — Data & Workflow Systems Foundation

**Window**: November 2026 – March 2027 (overlaps Phases 1–2; semester pace rules)
**One-line purpose**: Prove the full operational-data pipeline — messy data → validated structure → defensible analysis → decision-ready communication.

## Purpose
The current audit hypothesis uses waste-math such as `(minutes per instance ×
instances per year × loaded hourly rate) + error/rework cost + revenue leakage`
(source: smb-ai-audit-method.md, Step 3). This phase builds the broader ability to
turn messy operational data into a traceable conclusion another person can use.

## Why It Matters to the North Star
Decision-facing evidence must make its assumptions, calculation, and consequence
clear. A visual is useful when it materially improves that decision; it is not the
only valid format. This phase turns the Phase 1 data foundation into a reusable
analytical capability before the current first-offer test.

## Skills Needed
- Tabular-data handling, cleaning, and validation — Technical
- Relational data modeling and querying — Technical
- Decision-facing communication and appropriate visualization — Technical / Delivery
- Repeatable report generation in a justified format — Delivery
- Waste quantification math applied to real data — Diagnostic

## Skills NOT Needed Yet
- Deep API integration — wait for a real interface need
- Production automation builds — recommendation fluency suffices until a verified workflow requires one

## Best Sources
| Source | Tier | Location | What it proves |
|---|---|---|---|
| Pandas/SQL source-summary pages | 1 digested | `03-WIKIS\PYTHON\wiki\source-summaries\` (reading-writing-csv-with-pandas, pandas-missing-data-and-duplicates, groupby-aggregation-with-agg, sql-joining-tables-and-relationships, sql-grouping-and-aggregate-functions...; migrated from FORGE July 7, 2026 — inventoried as a Stage 9-10 gap, not yet built into the active curriculum, see `PYTHON\wiki\source-map.md`) | The exact techniques |
| `03-WIKIS\PYTHON` Stages 9–10 | internal | `03-WIKIS\PYTHON\wiki\stages\` (automation bridge: CSV/JSON, report scripts, SQLite, CLI) | School-aligned practice path that also builds permanent technical capability |
| smb-ai-audit-method.md, Step 3 | internal | `03-WIKIS\BUSINESS\` | The waste-math formula this phase exists to serve |
| Practical SQL / Python for Data Analysis | 1 | `03-WIKIS\PYTHON\raw\books\` (source PDFs; already digested into the source-summary pages above) | Depth on demand |

## Tools, Methods, or Platforms Under Test
Current candidates include SQLite, pandas, a justified reporting or visualization
platform, and a repeatable document pipeline. The approved proof vehicle and its
constraints select the smallest useful combination through the Recommendation Ladder.

## Capability and Value Enabled
Turn an unfamiliar operational dataset into a validated structure, defensible
finding, and decision-ready explanation. Under the current strategy, that capability
supports data-backed audit findings.

## Proof Projects
- **Approved reporting vehicle** — a small real dataset flowing through storage,
  analysis, visualization, and a generated report. POL remains one parked option,
  not the designated project; a future weak-link review must reactivate it.
- One end-to-end rep on a foreign dataset: take a messy real-world export Chris
  didn't create, clean it, quantify one "waste" finding, present it on one page.

## Exit Criteria
- [ ] One approved real-data vehicle producing repeatable structured analysis and a decision-ready output
- [ ] One decision-facing output on real data using a justified format
- [ ] One foreign messy dataset → validated → quantified finding → decision-ready communication, end-to-end without help
- [ ] Waste-math formula applied with conservative, defensible numbers at least twice

## Risks and Distractions
- Tool-collecting (what-not-to-do.md names it a core failure mode) — one BI tool, not three
- Over-engineering the proof vehicle — it stays small and completable
- This phase runs at semester pace; spring courses outrank it

## Next Action
When this phase activates, select the smallest real reporting vehicle from current
evidence. Do not automatically resume POL or expand the shipped tracker.
