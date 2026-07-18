---
type: os
timeline: reference
tags: [systems]
---

# CLAUDE.md — Systems Wiki OS

## Purpose

Systems engineering and system-dynamics knowledge: feedback structures, stock-and-flow
models, oscillation, delay, and the ISYE curriculum spine (queuing theory, operations
research, simulation) as it activates.

The controlling question:

> What system-dynamics or ISYE concept is worth knowing, and what audit or coursework
> does it strengthen?

## System Boundary

- This vault owns the engineering-of-systems lane specifically: stock-and-flow
  modeling, causal loop diagrams, feedback structure, factory physics, queuing theory,
  MRP/inventory theory, and business-cycle/economic dynamics as a special case of
  system dynamics.
- Distinct from `03-WIKIS\FORGE` (retired July 7, 2026 — this content is FORGE's
  former `wiki/systems/` folder, moved here wholesale as part of that retirement).
- Distinct from `03-WIKIS\BUSINESS` (offer layer, audit method, client-facing
  pathways) and `03-WIKIS\TECHNOLOGY` (tool/landscape research). SYSTEMS feeds both:
  ISYE coursework readiness and audit methodology — several pages already carry
  direct audit use-case tags (`use-case/audit`, `use-case/systems-analysis`) from
  their FORGE origin and those tags remain accurate here.
- Existing pages carry FORGE's original frontmatter (`domain: systems`, `type`,
  and the full `priority/status/domain/source-role/use-case/subject` tag tracks) —
  this is a clean lift, not a re-tag, and that legacy metadata remains readable.
  **New pages use the canonical property schema in `WHERE_IT_GOES.md`** (`type`,
  one `timeline`, optional `status`/`reference_priority`, and topic tags). Do not
  copy legacy `priority/*` or `status/*` control tags onto a page that has
  `timeline:`; dual encoding is a metadata error.

## Folder Structure

```text
raw/          # source PDFs (Sterman Business Dynamics, Factory Physics, etc.) — immutable
wiki/
  index.md
  log.md
  current-position.md   # future file; create only once ISYE 2600 prep is active
```

The inherited FORGE corpus plus any later direct ingests sit flat in `wiki/`
(no subfolders) — this matches how they lived in FORGE. Only add subfolders
if the page count grows enough to need them; don't pre-build structure.

## Shared Wiki Rules

The shared layer for all `03-WIKIS` hubs — raw/ immutability, large-source
chunking, session start/close minimums, update-over-create, contradiction
flagging, recency markers, and the lint pass — lives in
`00-BRAIN\AGENT.md § Wiki Shared Layer`. One copy, zero drift. This file
carries only this wiki's own rules.

**Raw/source status (verified 2026-07-18):** every substantive file currently in
`raw/` now has an explicit disposition in
`wiki/raw-source-coverage-and-intake-status.md`. The corrected gap queues for
*Business Dynamics*, *Factory Physics*, and *Supply Chain Science* are closed.
The July 17 *Process Mining Handbook* intake is selectively closed through a
complete 17-chapter disposition map and eight full applied chapter chunks.
Three sources are intentionally parked behind activation triggers rather than
treated as active reading backlog: *Algorithms to Live By*, the image-heavy
*Learning to See* workbook, and the short TOC/lean/Six Sigma comparison article.

The July 15 audit remains the governing lesson: do not infer complete coverage
from inherited pages, source mentions, or summary-level similarity. A large source
is complete only when every chapter or defined section has an explicit disposition:
ingested, covered by a named page, deferred with a reason, or intentionally excluded
with a reason. Presence in `raw/` is not coverage, and a synthesis page is not
evidence that every source chunk was reviewed.

## Final Operating Principle

This wiki activates ISYE-track content on demand and stays audit-usable throughout —
every page should be able to answer "how does this help diagnose or improve a client's
operation," not just "what does the textbook say."
