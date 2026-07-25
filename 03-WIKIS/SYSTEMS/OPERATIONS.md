---
type: contract
timeline: reference
status: live
register: ai-directive
tags: [systems, governance]
created: 2026-07-24
---

# SYSTEMS_WIKI — OPERATIONS

## Function

Maintain the engineering-of-systems knowledge base: feedback structure,
stock-and-flow modeling, factory physics, queuing theory, MRP/inventory theory,
operations research, process mining, and business-cycle dynamics as a special
case of system dynamics.

The controlling question:

> What system-dynamics or ISYE concept is worth knowing, and what audit or
> coursework does it strengthen?

This hub is a **research-retrieval engine** — a reference corpus with index and
tag retrieval. It becomes a staged learning engine only when ISYE 2600
activates.

## Two audiences, one corpus

Every page serves both or it does not belong here:

1. **ISYE coursework readiness** — the ISYE 2600 spine and the engineering
   fundamentals under it.
2. **Audit methodology** — entering an unfamiliar operation and diagnosing where
   time, money, and capacity actually leak.

A page should be able to answer *"how does this help diagnose or improve a real
operation,"* not only *"what does the textbook say."* No orphan knowledge: every
concept connects to ISYE prep or a named audit use case.

## Authority

| Owns | Authority |
|---|---|
| Permanent direction and AI limits | `01-NORTH_STAR\NORTH_STAR.md` |
| Current business vehicle and offer design | `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md` |
| System-dynamics and ISYE knowledge | this wiki |
| Raw-source disposition | `wiki\raw-source-coverage-and-intake-status.md` |
| Offer layer, audit method, client-facing pathways | `03-WIKIS\BUSINESS` |
| Tool and landscape research | `03-WIKIS\TECHNOLOGY` |
| Sequencing, gates, and proof status | CASTLE and `NOW.md` |
| Reusable audit diagnostics | `05-BUSINESS\06-Capability Library` and `00-BRAIN\CASTLE\wiki\skills\field-observation.md` |

This wiki feeds BUSINESS and TECHNOLOGY; it owns neither. A concept that becomes
a repeatable audit diagnostic is **routed** to the capability library or the
field-observation skill page — not duplicated there.

## Coverage discipline — this hub's governing lesson

`wiki\raw-source-coverage-and-intake-status.md` is the disposition ledger for
every substantive file in `raw/`. It is not optional bookkeeping; it is the
control that keeps this corpus honest, and it is the pattern other `.ROOT` hubs
are expected to follow.

From the July 15, 2026 audit, and still governing:

> Do not infer complete coverage from inherited pages, source mentions, or
> summary-level similarity. **Presence in `raw/` is not coverage.** A synthesis
> page is not evidence that every source chunk was reviewed.

A large source is complete only when **every chapter or defined section** has an
explicit disposition: ingested, covered by a named page, deferred with a reason,
or intentionally excluded with a reason.

Update the ledger in the same session a source arrives, closes, or changes
disposition. Verified 2026-07-24: all 27 raw files carry a disposition.

## Structure

```text
raw/          source PDFs and captures — immutable
wiki/
  index.md                                 complete retrieval map
  log.md                                   append-only history
  raw-source-coverage-and-intake-status.md source disposition ledger
  <concept pages, flat>
```

The corpus sits **flat** in `wiki/` — inherited from FORGE and kept that way.
Add subfolders only when page count genuinely demands them; do not pre-build
structure.

There is no `wiki\current-position.md` and there should not be one until staged
ISYE learning actually activates. This hub tracks corpus state, not learner
state.

## Inherited metadata — do not re-mix

This corpus came from FORGE (retired July 7, 2026) and was converted 2026-07-21
per `00-BRAIN\TAG_REGISTRY.md`: the legacy `priority/*`, `status/*`, `domain/*`,
`source-role/*`, and `use-case/*` tag tracks became real properties
(`timeline:`, `status:`, `source_role:`, `use_cases:`). `domain/*` was dropped —
it is inferable from the path.

All pages, new and inherited, now use the canonical property schema in
`WHERE_IT_GOES.md`. **Do not reintroduce a legacy control tag alongside a
property; dual encoding is a metadata error.** Inherited `subject/...` tags
remain valid topic tags and are still useful for retrieval.

Inherited pages may carry a `North Star Connection` heading. Read it as an
**application hypothesis**, not permanent business doctrine — load
`CURRENT_STRATEGY.md` before treating one as current strategy.

## Operations

### INGEST

1. Name the concept gap or audit question the source can close.
2. Classify the source and record it in the coverage ledger **before**
   synthesizing.
3. Read large sources in bounded chunks — chapter or defined section — and
   record exactly which chunks were covered.
4. Update an existing page before creating a new one.
5. Keep the established page shape: Summary / Sources / Last updated, Key Ideas,
   Connects to, Ranking, Use and Retrieval Notes.
6. Cite precisely; never invent a citation or a page number.
7. Update `wiki\index.md`, the coverage ledger, and `wiki\log.md`.

### QUERY

1. Read `wiki\index.md` — it is the complete retrieval map.
2. Retrieve by property or topic tag; inherited pages also answer to
   `subject/...` tags.
3. Load only the pages the active question needs.
4. Answer with the diagnostic use, not only the definition.
5. End with the concept applied to a real situation, or an explicit statement
   that it has not been.

### LINT

Check: raw sources absent from the coverage ledger; ledger entries whose named
page no longer exists; large sources closed without chapter-level disposition;
concepts with no ISYE or audit connection; `North Star Connection` sections
being read as doctrine; legacy control tags re-mixed with properties;
cross-hub link ambiguity; unresolved links; and index-versus-tree drift.

## Proof

A concept is proven when it correctly diagnoses or models a real situation — an
independent course or practice example within academic-integrity limits, a
practice audit finding, or a client-diagnosis pattern actually applied.

Reading is not proof. A synthesis page is not proof. A `North Star Connection`
paragraph is not proof.

## Raw boundary

`raw\` is immutable. AI MUST NOT create, edit, move, rename, reorganize,
archive, or delete anything under it without Chris explicitly authorizing a
named exception.

## Shared wiki rules

Raw immutability, large-source chunking, session start/close minimums,
update-over-create, contradiction flagging, recency markers, and the lint pass
are defined once in `00-BRAIN\AGENT.md § Wiki Shared Layer`.

## Loop and return

This hub runs the **RESEARCH** and **STRUCTURE** stages of the System Loop.
Proof returns through the Return Packet — both canonical in
`01-NORTH_STAR\System Contracts\ROOT_CAPABILITY_CONTRACT.md`. Do not define a
competing loop or packet here.

## Close

Log which pages were used and how. Update a page's `Ranking` or priority line
only when its timing genuinely changed. Update `wiki\index.md` only when a page
was added or renamed, and the coverage ledger whenever a source's disposition
moved. State the next action in one line.

## Final operating principle

Activate ISYE content on demand; stay audit-usable throughout.

A corpus that cannot say what it has and has not read is not a knowledge base —
it is a pile. The ledger is what makes the difference.
