---
type: phase
status: planned
tags: [phase, next]
---

# Phase 3 — Data & Workflow Systems Foundation

**Window**: November 2026 – March 2027 (overlaps Phases 1–2; semester pace rules)
**One-line purpose**: Prove the full client-data pipeline — messy export → SQL → analysis → visual, numbers-backed report.

## Purpose
An audit's credibility is the waste-math: `(minutes per instance × instances per
year × loaded hourly rate) + error/rework cost + revenue leakage` (source:
smb-ai-audit-method.md, Step 3). This phase builds the ability to compute and SHOW
those numbers from a client's real, messy data.

## Why It Matters to the North Star
Findings without visuals don't sell (gap #3, SKILL_GAP_ANALYSIS). The audit report's
headline is a dollar number with evidence behind it. This phase turns the Phase 1
Python/SQL foundation into the audit's analytical engine before the first client.

## Skills Needed
- pandas/CSV handling + cleaning — Technical
- SQL beyond basics (joins, grouping, aggregates) — Technical
- Looker Studio dashboarding — Technical / Delivery
- Report generation (Python → Markdown → PDF) — Delivery
- Waste quantification math applied to real data — Diagnostic

## Skills NOT Needed Yet
- REST APIs at depth — first pull can wait for a real integration need (Phase 7)
- Make.com/n8n builds — recommendation fluency suffices until clients exist

## Best Sources
| Source | Tier | Location | What it proves |
|---|---|---|---|
| Pandas/SQL source-summary pages | 1 digested | `03-WIKIS\PYTHON\wiki\source-summaries\` (reading-writing-csv-with-pandas, pandas-missing-data-and-duplicates, groupby-aggregation-with-agg, sql-joining-tables-and-relationships, sql-grouping-and-aggregate-functions...; migrated from FORGE July 7, 2026 — inventoried as a Stage 9-10 gap, not yet built into the active curriculum, see `PYTHON\wiki\source-map.md`) | The exact techniques |
| `03-WIKIS\PYTHON` Stages 9–10 | internal | `03-WIKIS\PYTHON\wiki\stages\` (automation bridge: CSV/JSON, report scripts, SQLite, CLI) | Track 1-aligned practice path |
| smb-ai-audit-method.md, Step 3 | internal | `03-WIKIS\BUSINESS\` | The waste-math formula this phase exists to serve |
| Practical SQL / Python for Data Analysis | 1 | `03-WIKIS\PYTHON\raw\books\` (source PDFs; already digested into the source-summary pages above) | Depth on demand |

## Tools to Learn
sqlite3 → pandas → Looker Studio (one real dashboard) → a Markdown/PDF report script

## Business Capability Unlocked
Data-backed audit findings: turn any client export (QuickBooks, jobs list, timesheet)
into quantified waste and a visual an owner understands in ten seconds.

## Proof Projects
- **POL (Powers Operating Ledger)** — the designated vehicle: sessions → CSV →
  SQLite → weekly summary report (SKILL_GAP_ANALYSIS names it as training all four
  gaps). Upgrade its output to a visual dashboard + generated PDF here.
- One end-to-end rep on a foreign dataset: take a messy real-world export Chris
  didn't create, clean it, quantify one "waste" finding, present it on one page.

## Exit Criteria
- [ ] POL producing weekly reports automatically (Python + SQLite)
- [ ] One Looker Studio dashboard live on real data
- [ ] One foreign messy dataset → cleaned → quantified finding → one-page visual report, end-to-end without help
- [ ] Waste-math formula applied with conservative, defensible numbers at least twice

## Risks and Distractions
- Tool-collecting (what-not-to-do.md names it a core failure mode) — one BI tool, not three
- Over-engineering POL — it stays small and completable
- This phase runs at semester pace; spring courses outrank it

## Next Action
When the tracker ships (~July 25): resume POL with this phase's exit criteria as its scope.
