---
type: os
timeline: reference
tags: [governance, technology]
---

# CLAUDE.md — Technology Wiki OS

## Purpose

Research and maintain Chris's tech-skill and tech-adoption roadmap: what to
learn next, what tools exist, where the landscape is moving. This wiki feeds
`01-NORTH_STAR\SKILL_GAP_ANALYSIS.md` and the Watchtower
(`...projectSuccess\WATCHTOWER.md`).

The controlling question:

> What tool or skill category should Chris know exists, and when does it
> become worth learning or recommending?

## Spine Reference

`02-LIBRARY\REF-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md` is this wiki's
operational spine — the 12-category possibility map (need/waste signals per
category, the Recommendation Ladder, the selling model). It stays in place at
`02-LIBRARY` (July 7, 2026 decision: it's load-bearing in ~10 live files
including `NORTH_STAR.md`, `AGENT.md`, and the surface profiles' session boot
order — moving it risked breaking the boot chain for no real gain). This wiki
links to it and builds landscape research around it; it does not duplicate or
fork its content.

## System Boundary

- This vault has two layers as of July 7, 2026. The original layer is
  landscape-research and skill-roadmap — tool categories, adoption timing,
  what's worth learning next ("what exists and when does it matter"). The
  second, newer layer is **applied technical reference** ("how do I actually
  use it") — 68 pages inherited from FORGE's retirement covering web
  frameworks (Flask/Django), distributed systems, DevOps, AI/LLM concepts, and
  applied data science/ML. FORGE retired July 7; this wiki absorbed its
  non-Python applied-technique content rather than that knowledge having
  nowhere to live. (The Python/data-analysis half of FORGE's technology
  content went to `03-WIKIS\PYTHON` instead — see that wiki's `source-map.md`.)
- Landscape research still feeds `01-NORTH_STAR\SKILL_GAP_ANALYSIS.md` and the
  Watchtower per the Purpose section above; applied-reference pages exist to
  be pulled from directly during audits and builds, the role FORGE used to
  serve. Don't conflate the two — a landscape page answers "should Chris learn
  this," an applied-reference page answers "how does this actually work."
- `03-WIKIS\AI_AUTOMATION_SYSTEMS` is the sibling wiki for AI tooling, agent
  patterns, and self-evolution research on `.ROOT` itself — a narrower slice
  of the same landscape-watching function, specific to AI/automation.
  **Lane closure (July 9, 2026):** this wiki's `ai-and-llm/` subfolder is
  inherited applied reference, closed to new intake — new AI/LLM/agent
  research routes to `03-WIKIS\AI_AUTOMATION_SYSTEMS`. And
  `02-LIBRARY\REF-AI-AUTOMATION` is an artifact/reference home (the spine,
  prompt libraries, promoted syntheses, capture folders Chris places there),
  not an intake lane.

## Folder Structure

```text
raw/          # tool docs, landscape articles, vendor comparisons — immutable
wiki/
  index.md
  log.md
  current-position.md   # once landscape tracking is active
  web-frameworks/        # applied reference: Flask, Django, lightweight frameworks, task queues, hosting
  distributed-systems/   # applied reference: scalability, caching, consistency, messaging, storage engines, transactions
  devops/                 # applied reference: Phoenix Project, DevOps Handbook, IT ops, deployment, security
  ai-and-llm/             # applied reference: LLM fundamentals, alignment, co-intelligence (closed lane, see System Boundary)
  data-science-ml/        # applied reference: CRISP-DM, data mining, trees/linear models, inferential statistics
  database-sql/           # applied reference: SQL fundamentals through window functions (added 2026-07-13)
  software-craft/         # applied reference: Clean Code, The Clean Coder, The Pragmatic Programmer (added 2026-07-13)
  security/               # applied reference: API security, OWASP API Top 10 (added 2026-07-13)
  software-engineering/   # applied reference: Agile/Scrum, requirements, testing (added 2026-07-13)
  (landscape-research pages live at wiki/ root, not in a subfolder — first
  batch added 2026-07-13; see index.md)
```

The five original applied-reference subfolders were built July 7, 2026 for the
FORGE-inherited content; four more (`database-sql/`, `software-craft/`,
`security/`, `software-engineering/`) were built July 13, 2026 for that day's
raw/ audit-and-ingest batch, same justification (content arrived in clear
clusters, not built speculatively). Build further category subfolders under
`wiki/` only as new landscape research or applied-reference material actually
accumulates per category — do not pre-build empty categories.

## Shared Wiki Rules

The shared layer for all `03-WIKIS` hubs — raw/ immutability, large-source
chunking, session start/close minimums, update-over-create, contradiction
flagging, recency markers, and the lint pass — lives in
`00-BRAIN\AGENT.md § Wiki Shared Layer`. One copy, zero drift. This file
carries only this wiki's own rules.

New or edited pages use metadata v2 properties rather than legacy control
tags. Applied-reference pages normally use `timeline: reference` and
`status: wiki-only`; keep `tags` categorical (for example,
`domain/technology`, `source-role/primary`, and subject tags). Never put
`priority/*` or `status/*` control values in `tags` once `timeline:` exists.

Session note: when the session concerns a specific category, also read
`TECHNOLOGY_LIBRARY_STRATEGY.md` at start.

## Maintenance Cadence

Same cadence `TECHNOLOGY_LIBRARY_STRATEGY.md` already defines: weekly
30-minute landscape rep (one category, one tool, or one real use case),
monthly review alongside `SKILL_GAP_ANALYSIS.md`. Landscape study is
preparation, not production — if it displaces audit or build work two weeks
running, rebalance.

## Watchtower Handoff

Keep full technology evidence here. Promote only a verified new external change
with a material consequence to `...projectSuccess\radar.md`, and include the
evidence page, affected active strategy assumption/system choice, consequence or
bounded test, and review trigger. The radar never replaces this wiki's research.

## Final Operating Principle

This wiki watches the landscape so Chris doesn't have to relearn it cold on
every audit. It stays vendor-neutral and ties every category studied back to
a client service, skill gap, or audit scenario — same no-orphan-knowledge rule
`TECHNOLOGY_LIBRARY_STRATEGY.md` already uses.
