---
type: research
timeline: reference
tags: [technology, landscape, category-3, business-intelligence]
source: raw/Data Studio documentation.md (Google Cloud docs, captured 2026-06-13)
---

# Looker Studio (Data Studio) — Free BI Dashboards

**Summary**: Google's no-cost drag-and-drop dashboard/report tool. Renamed
from "Data Studio" to "Looker Studio" — the source itself opens with that
rename notice, so any client-facing material should use the current name.
This closes `TECHNOLOGY_LIBRARY_STRATEGY.md` Category 3's explicit first-
listed tool ("Looker Studio (free) → Power BI → custom Flask/Plotly
reporting") — a landscape rep this wiki's log has carried as an open gap
since July 9.

## What It Actually Is

A free BI layer that turns connected data sources (Sheets, databases,
marketing platforms) into shareable, interactive dashboards — charts,
viewer-side filters, drag-and-drop editing, no code required for the base
case. Google is pushing it as part of a broader Cloud/GenAI upsell funnel
(the docs page is stapled to a "$300 free credit" GCP trial banner) — read
the core product as free/standalone; the upsell surface is separate.

## Why This Matters for Category 3

Category 3's own diagnostic: "decisions made on gut because the numbers
are scattered or stale," waste signal "Power BI licenses when Looker
Studio on a Sheet does it free." This tool is the Recommendation Ladder's
literal rung 1 for BI — the free-tier answer before any paid dashboard
platform gets proposed to a client. A client already on Google Workspace
(Sheets-based operations) is the cleanest fit: connect Sheets directly, no
new data warehouse needed.

## Use / Retrieval Notes

**Use when**: A client's numbers already live in Google Sheets and the
job-level or monthly profit picture is scattered/late — the Category 3
need-signal. Recommend before Power BI, not after.

**Do not use when**: The client needs governed, multi-source enterprise
reporting with row-level security — that's the Power BI/custom-Flask rungs
further up the ladder.

## Connects to

`TECHNOLOGY_LIBRARY_STRATEGY.md` Category 3 (Business Intelligence &
Dashboards) — this page is the landscape rep that category's own tool list
named but never had a dedicated page for.

## North Star Connection

Direct audit lever: "turn on what's already free" is the cheapest possible
first recommendation in any BI-gap audit finding, same Recommendation
Ladder logic already applied to workflow-automation tooling
([[workflow-automation-tools-landscape|via AI_AUTOMATION_SYSTEMS]]) and
Category 4 in the Make.com rep.

## Local Rep Bridge - 2026-07-16

The YT Outlier Scanner now has an offline `market-export` command that writes a
typed CSV and field dictionary from its existing deduplicated market evidence:

- `02-LIBRARY/.PROJECTS/YT_Outlier_Scanner/LOOKER_STUDIO_MARKET_DATA.csv`
- `02-LIBRARY/.PROJECTS/YT_Outlier_Scanner/LOOKER_STUDIO_FIELD_DICTIONARY.md`

This is a prepared input, not a completed Looker Studio rep. The first bounded
live proof is to load the CSV into a private Sheet, connect it to a private report,
confirm field types, and build one scorecard, one category chart, one evidence
table, and basic format/date controls. No account creation, publication, revenue
inference, or channel decision is authorized by the export.

## Real-World Dataset Decision Pattern - 2026-07-16

The next dashboard rep should be driven by a real decision rather than by the
availability of data. A ranked source review selected an Atlanta-area construction
opportunity baseline: Census Building Permits Survey data supplies residential
project-flow signals, and BLS QCEW supplies county-level construction-business
capacity. Atlanta's permit tracker is the earned project-detail layer, not the
starting point.

The working artifact is
`outputs/real_world_dataset_opportunity_map_2026-07-16/advisor_builder_dataset_opportunity_map.xlsx`.
It records the scoring model, eight official sources, a five-phase pilot, and the
stop rule: if the result produces no sharper target or question than “construction
is active,” park it. Public data can improve targeting; it does not prove customer
pain or willingness to pay.
