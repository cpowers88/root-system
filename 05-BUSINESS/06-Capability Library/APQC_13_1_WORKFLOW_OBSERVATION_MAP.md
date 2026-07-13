---
type: asset
tags: [reference, business, apqc, client]
---

# APQC_13_1_WORKFLOW_OBSERVATION_MAP.md

## Metadata

**Asset Name:** Workflow Observation Map
**File Name:** `APQC_13_1_WORKFLOW_OBSERVATION_MAP.md`
**Primary APQC Process:** 13.1 Manage Business Processes (13.1.2 Design and model processes)
**Secondary APQC Process:** N/A — cross-functional; the workflow observed can sit in any operating process area (4.0 Deliver Physical Products, 5.0 Deliver Services, 6.0 Manage Customer Service, etc.) depending on the client
**Asset Type:** SOP (produces a workflow map + findings one-pager as output)
**Technical Tags:** Markdown / Google Drive / spreadsheet / other (notebook + phone, zero software required)
**Business Use Case:** First on-site diagnostic conversation with a prospective client — find where their operation loses time or money in under a day, with specifics, before recommending any tool or spending any build time
**Maturity:** draft
**Source or Origin:** `05-BUSINESS\01-Audit Templates\OBSERVATION_METHODOLOGY.md` (SKELETON v1, July 5, 2026)
**Owner:** Chris Powers
**Last Reviewed:** July 12, 2026
**Index Row Added:** yes

---

## 1. Owner-Facing Problem

Most owners can feel that their operation loses time and money somewhere — a job takes too long, someone redoes work, a customer complaint slips through — but they can't point to exactly where or put a number on it. This asset is the repeatable way to walk their floor, follow one real job start to finish, and come back with specific, counted friction points instead of vague impressions.

## 2. APQC / Process Context

Sits inside 13.1 Manage Business Processes (process design, modeling, and improvement) as the diagnostic front end — but the workflow being traced on any given visit can belong to any process area the client operates in. In practice: this is the first pass Chris runs on a prospect's operation, before any technology or automation recommendation is made.

## 3. Asset Description

A structured field method in three phases:

- **Before the visit** (30 min prep): name what the business sells and who pays them, guess the three core workflows (intake → work → get paid), review the tool-category list so friction can be named on sight, and decide the one governing question the visit must answer.
- **During the visit**: pick one real job/order/customer and trace it start to finish. At every handoff, ask the Three Systems Questions (where does state live, where does feedback live, what breaks if I delete this) and tally sightings against a 9-item waste checklist (waiting, double entry, rework, tribal knowledge, manual handoff, spreadsheet-as-database, text/email-as-system-of-record, missing feedback, shadow systems). Watch first, ask second; never propose fixes on-site.
- **After the visit** (same day, within 4 hours): brain-dump into fieldnotes, draw a one-page process map, fill a friction inventory with time-cost-per-week estimates, sort findings on the Recommendation Ladder (eliminate → simplify → use what they own → configure → integrate → build), and draft the owner-facing one-pager.

## 4. Inputs

| Input | Source | Required? | Notes |
|---|---|---|---|
| Notebook + phone | Chris, physical | Required | No laptop on the first walk |
| Guessed core workflows (intake → work → get paid) | Pre-visit prep / public info | Required | Corrected on-site, not before |
| Tool-category fluency | `02-LIBRARY\08-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md` (12 categories) | Required | So Chris can name what he's looking at in real time |
| One real job/order/customer to trace | Chosen on-site, day-of | Required | Must be a live, in-progress instance, not a description of one |

## 5. Outputs

| Output | Destination | User | Notes |
|---|---|---|---|
| `FIELDNOTES_DATE_TOPIC.md` | `05-BUSINESS\02-Field Notes\` | Chris (internal) | Raw brain dump, written same day |
| One-page process map | Internal, feeds client one-pager | Chris → owner | Boxes and arrows, the job's real path |
| Friction inventory | Internal | Chris | Waste sighting → estimated time cost/week |
| Findings one-pager | Client-facing | Business owner | `ONE_PAGE_FINDINGS_FORMAT.md` — owner language, numbers first |
| Full audit report (optional) | Client-facing | Business owner | `TECHNOLOGY_AUDIT_REPORT_TEMPLATE.md` — only when engagement scope calls for it |

## 6. Implementation Notes

Zero software required to run the visit itself — notebook, phone camera (with permission), and the checklist. The write-up path is Markdown files in the local `.ROOT` workspace (cloud-backed by Google Drive): fieldnotes template → hand-sketched or Google-Drawings process map → `ONE_PAGE_FINDINGS_FORMAT.md`. No API, no paid tool, no build lead time — this asset is usable on the very first free practice rep and on the first paid engagement without waiting on anything else in the capability library.

## 7. Validation

Test is Practice Rep 1, per the method's own cadence (`OBSERVATION_METHODOLOGY.md` § Practice Cadence): one observation on a free-access business — a known jobsite, Heather's brokerage front office (observation only, not client or JV work), or an accessible retail counter. Success = a completed fieldnotes file, one process map, and a real one-pager, all produced within 4 hours of the visit, using the method exactly as written. Not yet run as of July 12, 2026.

## 8. Packaging Notes

Before this is shown to or used with an actual prospect:
1. Run at least Rep 1 so the method is tested, not just designed.
2. Confirm `ONE_PAGE_FINDINGS_FORMAT.md` and `TECHNOLOGY_AUDIT_REPORT_TEMPLATE.md` still match this method's output shape.
3. Keep enforcing the built-in privacy rule: roles only, never names, in anything that leaves the notebook.

## 9. Next Action

Schedule and run Practice Rep 1 before the Aug 24 semester start / danger-weeks ceiling. Block the 30-min prep + visit + same-day write-up as one calendar unit, then log the result and bump maturity to "tested internally" in `CAPABILITY_LIBRARY_INDEX.md`.
