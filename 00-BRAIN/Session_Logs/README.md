---
type: guide
timeline: reference
status: active
tags: [governance, system-review]
---

# Session Logs — Operating Guide

This folder preserves session evidence without turning the root into a pile of
reports. Git records every committed change; this structure makes the human
meaning, decision, and evidence packet easy to retrieve.

## What Stays at the Root

- `DAILY_YYYY-MM-DD.md` — append-only task record for the day.
- `DAILY_TEMPLATE.md` and `HANDOFF_TEMPLATE.md` — report templates.
- A report may remain here only while its review or decision is still active.

## The Four Evidence Homes

| Home | What belongs there |
|---|---|
| `System Update Log\` | Monthly commit ledger plus dated evidence packets for consequential multi-commit `.ROOT` changes |
| `Closed Flags\` | Monthly permanent ledger of flags moved out of `SYSTEM_FLAGS.md` when verified closed |
| `Report Archive\` | Completed standalone reports and handoffs that are not part of a system-change packet |
| `weekly_and_monthly_reports\` | `weekly_reports\` and `monthly_reports\` subfolders hold every WEEKLY/MONTHLY review and its template once written — DAILY stays at root (below), reviews move here on creation |

## System-Change Packet Rule

Create `System Update Log\YYYY-MM-DD_TOPIC\` only when a consequential system
program spans multiple linked commits/phases or produces multiple acceptance
artifacts. Ordinary one-commit maintenance uses the monthly update ledger and
DAILY only; it does not earn a folder.

Every packet contains `SESSION_INDEX.md` with:

1. purpose and authority;
2. date/commit boundary;
3. final verdict and accepted debt;
4. exact artifact inventory;
5. next recheck dates or triggers.

Keep one copy of each artifact. Git is the change history; the packet is the
retrieval layer. Do not duplicate reports into both the packet and Report
Archive.

## Close and Review

- At final acceptance, move a system program's completed reports into its
  packet and update the packet index.
- Move other completed reports/handoffs to `Report Archive\`.
- On flag closure, write the monthly `Closed Flags\` row in the same session.
- The weekly CASTLE sweep verifies update-ledger rows, closed-flag rows, and
  packet indexes for any newly completed multi-commit program.

Historical DAILYs and reports may name the file's location at the time they
were written. Do not rewrite that history; the current packet index is the
canonical retrieval route after a move.
