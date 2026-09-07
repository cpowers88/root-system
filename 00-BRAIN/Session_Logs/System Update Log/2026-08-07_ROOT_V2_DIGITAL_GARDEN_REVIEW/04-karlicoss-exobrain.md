---
type: report
timeline: log
status: complete
tags: [architecture, digital-garden, search, provenance, root-v2]
created: 2026-08-07
---

# Review 04 — Karlicoss Exobrain

## Source

- Knowledge repository: [karlicoss/exobrain](https://github.com/karlicoss/exobrain)
- Repository explanation: [README.org](https://github.com/karlicoss/exobrain/blob/master/README.org)
- Separate compiler: [karlicoss/exobrain-compiler](https://github.com/karlicoss/exobrain-compiler)
- Accessed: 2026-08-07

## Why it was selected

Exobrain is the strongest retrieval contrast. It explicitly treats search as a
primary interface and separates knowledge source from the code that compiles
its public representation.

## What the system does well

- Search-first retrieval reduces dependence on remembering a manual hierarchy.
- A curated, high-information section can coexist with a lower-confidence pile
  when the distinction is visible.
- Timestamps expose age and relevance.
- Processing states such as TODO, started, and done make unfinished knowledge
  visible.
- Source material and compiler are separate, supporting disposable derived
  views.

## What `.ROOT V2` should take

1. Make retrieval search- and task-first, with folders remaining ownership
   boundaries rather than the main user interface.
2. Separate canonical Markdown from the compiler/runtime that builds context,
   dashboards, and public or client-facing views.
3. Show confidence, source, processing state, and age at retrieval time.
4. Put refined claims above supporting clips or links rather than mixing them
   invisibly.

## What not to copy

- Clips, beliefs, and verified claims should not share the same apparent
  authority.
- Public-first notes create privacy and client-confidentiality risk.
- The separate compiler repository is archived as of this review, showing that
  source/runtime separation helps architecture but does not remove maintenance.

## Root-specific inference

`.ROOT V2` needs a provenance-aware search result, not merely full-text search:
each result should say why it was retrieved, what kind of evidence it contains,
how current it is, and whether it is safe for school, internal, public, or
client use.
