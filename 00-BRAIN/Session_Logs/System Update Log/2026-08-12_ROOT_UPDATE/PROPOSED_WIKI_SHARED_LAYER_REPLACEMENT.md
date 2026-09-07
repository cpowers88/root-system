---
type: proposal
timeline: reference
status: proposed
tags: [governance, wikis, replacement-draft]
created: 2026-08-12
replaces_if_approved: 00-BRAIN/WIKI_SHARED_LAYER.md
---

# Proposed replacement — Wiki Shared Layer

## Trigger

Load this contract before reading or changing any `03-WIKIS` hub or CASTLE's
wiki. Then load that hub's `OPERATIONS.md`. The shared layer supplies the common
minimum; the local contract adds domain rules and names the state owner. A local
contract may strengthen this minimum but may not silently remove it.

## Start

1. Read the hub's `wiki/index.md` and its three newest `wiki/log.md` entries.
2. Read the hub's named **state owner**. If `current-position.md` is intentionally
   absent, `OPERATIONS.md` must name the alternate owner and explain the boundary.
3. State one sentence: **goal, owner, and completion evidence**.

**Complete when:** the active question has one owner, current state is recovered
without oral history, and the session has a falsifiable finish condition.

## Evidence intake

1. Treat every `raw/` folder as immutable evidence. Extract into `wiki/`; do not
   write, move, rename, archive, delete, reorganize, or hash-dedupe `raw/`.
2. For a long source, define complete chunks before extraction: normally 10–15
   pages or one coherent chapter/section. Record each completed range in
   `wiki/log.md`; synthesize only after all required ranges are accounted for.
3. Search the live wiki before creating a page. Update the existing owner when
   the new evidence strengthens, corrects, or extends the same claim.

**Complete when:** every used source range is accounted for, raw evidence is
unchanged, and each resulting claim has one live owner.

## Claim maintenance

1. Before changing a claim, classify the change:
   - **temporal update** — the world changed;
   - **context variant** — both claims can be true under different conditions;
   - **contradiction** — the evidence conflicts.
2. Preserve the classification on the owner page with source and date. A
   contradiction remains visible until resolved.
3. Mark volatile prices, versions, capabilities, regulations, and adoption
   figures `(as of YYYY-MM, source)`.

**Complete when:** a later session can distinguish what changed in the world
from what changed in the evidence or interpretation.

## Close

1. Append the operation and evidence range to `wiki/log.md`.
2. Update `wiki/index.md` only when navigation changed.
3. Update the state owner only when its owned truth changed.
4. State one next action, or explicitly state that none was created.
5. After frontmatter edits, run:
   `python 00-BRAIN/scripts/frontmatter_audit.py --baseline 00-BRAIN/scripts/frontmatter_baseline.json`
   and resolve every new finding before close.

**Complete when:** navigation resolves, the state owner agrees with current
evidence, the log records the delta, and a fresh session can recover the next
truth without conversation history.

## Periodic lint

At monthly review or on request, check orphan pages, dead wikilinks,
contradictions, stale volatile claims, superseded claims, index/tree mismatch,
and state-owner freshness. Record findings under normal flag priority.

## Hub conformance declaration

Every hub `OPERATIONS.md` carries one compact declaration:

> **Shared layer:** load `00-BRAIN/WIKI_SHARED_LAYER.md` for every hub session.
> This file adds local rules. State owner: `<exact path and ownership boundary>`.

This declaration is the local discoverability mechanism. It points to the
shared source instead of duplicating the eight rules.

## Academic boundary

Academic integrity remains governed by `AGENT.md`. Course-support hubs add the
exact course policy and stop when graded status is unclear.
