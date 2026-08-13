---
type: contract
timeline: reference
status: live
register: ai-directive
tags: [technology, governance]
created: 2026-07-24
---

# TECHNOLOGY_WIKI — OPERATIONS

## Function

Two layers, one hub. Keep them distinct.

| Layer | Answers | Feeds |
|---|---|---|
| **Landscape research** | "What exists, and when does it become worth learning or recommending?" | the capability weak-link ranking and the Watchtower |
| **Applied reference** | "How does this actually work?" | audits and builds, pulled from directly |

The controlling question for the landscape layer:

> What tool or skill category should Chris know exists, and when does it become
> worth learning or recommending?

A landscape page answers *should Chris learn this*. An applied-reference page
answers *how does this work*. Do not conflate them, and do not let one silently
become the other.

The applied layer is 68 pages inherited from FORGE (retired July 7, 2026) plus
everything compiled since. FORGE's Python and data-analysis half went to
`03-WIKIS\PYTHON` instead.

## Spine reference

`02-LIBRARY\REF-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md` is this wiki's
operational spine — the 12-category possibility map with need/waste signals per
category, the Recommendation Ladder, and the selling model.

It stays at `02-LIBRARY` by the July 7, 2026 decision: it is load-bearing in
roughly ten live files including `NORTH_STAR.md`, `AGENT.md`, and the surface
profiles' boot order. This wiki **links to it and builds around it; it never
duplicates or forks its content.** When a session concerns a specific category,
read the spine at session start.

## Authority

| Owns | Authority |
|---|---|
| Permanent direction and AI limits | `01-NORTH_STAR\NORTH_STAR.md` |
| Capability stack and weak-link order | `01-NORTH_STAR\Goals & Milestones\capability_development_goal.md` |
| Current business vehicle | `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md` |
| The 12-category map and Recommendation Ladder | `02-LIBRARY\REF-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md` |
| Tool landscape and applied technical reference | this wiki |
| Raw-source disposition | `wiki\raw-source-coverage-and-intake-status.md` |
| AI tooling, agent patterns, `.ROOT` self-evolution | `03-WIKIS\AI_AUTOMATION_SYSTEMS` |
| System dynamics and ISYE | `03-WIKIS\SYSTEMS` |
| Offer, audit method, client pathways | `03-WIKIS\BUSINESS` |
| Sequencing and proof status | CASTLE and `NOW.md` |
| External signal promotion | Watchtower (`01-NORTH_STAR\radar.md`) |

## Closed lanes — do not reopen without Chris

- **`wiki\ai-and-llm\` is closed to new intake** (July 9, 2026). It is inherited
  applied reference. New AI, LLM, or agent research routes to
  `03-WIKIS\AI_AUTOMATION_SYSTEMS`.
- `02-LIBRARY\REF-AI-AUTOMATION` is an artifact and reference home — the spine,
  prompt libraries, promoted syntheses, captures Chris places there. It is
  **not** an intake lane.

## Structure

```text
raw/          tool docs, landscape articles, vendor comparisons — immutable
wiki/
  index.md
  log.md
  raw-source-coverage-and-intake-status.md   disposition ledger
  <landscape-research pages at wiki/ root>
  ai-and-llm/            applied reference — CLOSED intake lane
  data-science-ml/       CRISP-DM, data mining, models, inferential statistics
  database-sql/          SQL fundamentals through window functions
  devops/                DevOps Handbook, IT ops, deployment, security
  distributed-systems/   scalability, caching, consistency, messaging, storage
  instrumentation-iot/   measurement trust, sensors, edge/IoT architecture
  security/              API security, OWASP API Top 10
  software-craft/        Clean Code, The Clean Coder, Pragmatic Programmer
  software-engineering/  agile, requirements, reliability, testing
  user-experience/       five-plane model, strategy through surface, validation
  web-frameworks/        Flask, Django, task queues, hosting
```

Landscape pages live at `wiki/` root, not in a subfolder. Build a new category
subfolder only when material has actually accumulated in a clear cluster — never
speculatively. Every existing category was created that way, from a real batch.

**There is no `wiki\current-position.md` here and there should not be one.** The
landscape frontier of record is `TECHNOLOGY_LIBRARY_STRATEGY.md § Current State`;
`wiki\index.md` owns the applied-reference inventory. Do not create a second
frontier in this hub.

**The applied collection is a retrieval library, not a study queue.** Most of
`distributed-systems/` and `data-science-ml/` sits ahead of Chris's live
frontier. Target the spine's real gap list first — never whatever category
happens to have the most pages.

## Coverage discipline

`wiki\raw-source-coverage-and-intake-status.md` is the disposition ledger for
every physical file in `raw/`. Its own standard: *"Accounted" means the file has
a truthful disposition; it does not mean every source was converted into a
dedicated Technology page.*

Statuses: **Compiled**, **Selective**, **Derived**, **Cross-hub**,
**Reference-only**, **Excluded**. Every file carries one, with a reason.

Register a source in the ledger **in the session it arrives** — not when it is
compiled. A file read for another hub's purpose still needs a row here, because
this is where it lives. Presence in `raw/` is not coverage.

Accounted is not the same as usable. An unsourced model export can be correctly
dispositioned and still be unfit to cite; the ledger says so explicitly where it
applies.

## Operations

### INGEST

1. State the category and whether this serves the landscape or applied layer.
2. Register the file in the ledger with a disposition and reason.
3. Read large sources in bounded chunks; record which chunks were covered.
4. Update an existing page before creating one; do not duplicate the spine.
5. Mark volatile claims — prices, versions, vendor capabilities, adoption stats —
   with "(as of YYYY-MM, source)". This hub ages faster than any other.
6. Update `wiki\index.md`, the ledger, and `wiki\log.md`.

### QUERY

1. Read `wiki\index.md`; read the spine when the question is category-level.
2. Answer from the correct layer — landscape for "should we," applied for "how."
3. Give the recommendation with its trigger, not just the tool name.
4. State when a claim is dated and needs re-verification before use.

### LINT

Check: raw files missing from the ledger and ledger totals that disagree with
the folder; stale volatile claims without an as-of date; landscape and applied
pages blurring; new AI/LLM material landing in the closed `ai-and-llm/` lane;
spine content duplicated instead of linked; legacy control tags re-mixed with
properties; unresolved or folder-targeted wikilinks; index-versus-tree drift.

## Metadata

New and edited pages use v2 properties, not legacy control tags. Applied
reference normally carries `timeline: reference` and `status: wiki-only`.

Converted 2026-07-21 per `00-BRAIN\TAG_REGISTRY.md`: `domain/*` dropped
(inferable from the path), `source-role/*` → `source_role:`, `use-case/*` →
`use_cases:`, `stack/*` → `stack:`. Keep `tags` for genuine cross-cutting
topics. **Do not reintroduce `domain/*`, `source-role/*`, `use-case/*`, or
`stack/*` as tags, and never put `priority/*` or `status/*` control values in
`tags` once `timeline:` exists.** Dual encoding is a metadata error.

## Maintenance cadence

The cadence the spine already defines: a weekly 30-minute landscape rep — one
category, one tool, or one real use case — and a monthly review alongside
`capability_development_goal.md`.

Landscape study is preparation, not production. If it displaces audit or build
work two weeks running, rebalance.

## Watchtower handoff

Full technology evidence stays here. Promote to `01-NORTH_STAR\radar.md`
only a **verified new external change with a material consequence**, naming its
evidence page, the affected strategy assumption or system choice, the
consequence or bounded test, and the review trigger. The radar never replaces
this wiki's research.

## Proof, loop, and return

Proof is a landscape rep that became a recommendation pattern actually used in a
real or practice audit, or an applied lookup that unblocked a real build step —
never the existence of the page.

This hub runs the **RESEARCH** and **STRUCTURE** stages of the System Loop and
serves as a SENSE evidence home for the Watchtower. Proof returns through the
Return Packet — both canonical in
`01-NORTH_STAR\System Contracts\ROOT_CAPABILITY_CONTRACT.md`. Do not define a
competing loop or packet here.

When a recommendation pattern is genuinely used in real work, update
`TECHNOLOGY_LIBRARY_STRATEGY.md § Current State`. Do not duplicate it here.

## Raw boundary

`raw\` is immutable. AI MUST NOT create, edit, move, rename, reorganize,
archive, or delete anything under it without Chris explicitly authorizing a
named exception.

## Shared wiki rules

Raw immutability, large-source chunking, session start/close minimums,
update-over-create, contradiction flagging, recency markers, and the lint pass
are defined once in `00-BRAIN\WIKI_SHARED_LAYER.md`.

## Final operating principle

This wiki watches the landscape so Chris does not relearn it cold on every
audit. Stay vendor-neutral. Tie every category studied back to a client service,
a capability gap, or a real audit scenario — no orphan knowledge.
