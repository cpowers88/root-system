---
type: os
tags: [reference, systems]
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
  this is a clean lift, not a re-tag. Keep using that tagging system for new pages
  in this wiki so the inherited FORGE corpus stays consistent with anything added later.

## Folder Structure

```text
raw/          # source PDFs (Sterman Business Dynamics, Factory Physics, etc.) — immutable
wiki/
  index.md
  log.md
  current-position.md   # once ISYE 2600 prep is active
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

Raw note: the PDFs that originally sourced the inherited FORGE corpus (Sterman's
*Business Dynamics*, *Strategic Modeling and Business Dynamics*, *Factory Physics*,
*Supply Chain Science*) lived in FORGE's `raw/` and were archived to `99-ARCHIVE`
at FORGE's retirement, not copied here — the pages in `wiki/` are already a
full-fidelity extraction per FORGE's ingest protocol, confirmed by direct
cross-check against each book's actual table of contents/principles (2026-07-13).

**Correction (2026-07-13):** *Introduction to Operations Research* (Hillier &
Lieberman) was previously listed in this note alongside the other four titles,
but was never actually extracted — its LP/Simplex/Duality/Sensitivity/
Transportation content (Ch. 3–9) had zero overlap with the inherited pages
until the deterministic-OR core was ingested this session (see `wiki/log.md`
2026-07-13 and the "Linear Programming" index section). Lesson: this note's
claims are a starting assumption to verify against the actual wiki content,
not a substitute for checking — a stale/unverified "already covered" claim
here would otherwise cause the same gap to persist silently.

## Final Operating Principle

This wiki activates ISYE-track content on demand and stays audit-usable throughout —
every page should be able to answer "how does this help diagnose or improve a client's
operation," not just "what does the textbook say."

