---
type: map
timeline: reference
status: complete
tags: [castle, architecture, source-intake, ai-automation, machine-learning]
created: 2026-07-24
---

# Architecture Update Source Intake — 2026-07-24

## Purpose

This is the evidence-building layer for the `.ROOT` architecture update. Each
named PDF is read in complete physical-page or named-section chunks. Relevant
claims are preserved here before any final decision changes
`vault-skeleton-design.md`.

The lens is intentionally broad: information acquisition, Markdown and
instruction design, retrieval, learning, evaluation, agent architecture,
production systems, data/ML lifecycle, observability, value, human governance,
migration, maintenance, and evidence that challenges the current model.

## Source Register

| Source | Physical pages | Intake status | Report |
|---|---:|---|---|
| Chip Huyen, *AI Engineering* (2025) | 1,108 | Complete — all 1,108 physical pages | [[ai-engineering-chunk-intake]] |
| LevelUp Labs, *The AI Builder's Handbook* (2026) | 152 | Complete — 11 chunks | [[ai-builders-handbook-chunk-intake]] |
| Berryman and Ziegler, *Prompt Engineering for LLMs* (2025) | 282 | Complete — 11 chapters, all 282 pages | [[prompt-engineering-for-llms-chunk-intake]] |
| Phoenix and Taylor, *Prompt Engineering for Generative AI* (2024) | 791 | Complete — all 791 physical pages | [[prompt-engineering-for-generative-ai-chunk-intake]] |
| McKinsey, *The Economic Potential of Generative AI* (2023) | 68 | Complete — 6 chunks | [[generative-ai-economic-potential-chunk-intake]] |
| Nagasubramanian, *Agentic AI for Engineers* | 460 | Complete — all 460 physical pages | [[agentic-ai-for-engineers-chunk-intake]] |
| Lakshmanan, Robinson, and Munn, *Machine Learning Design Patterns* (2020) | 408 | Complete — all 408 physical pages; former pp. 108–300 render fault resolved and visually verified | [[machine-learning-design-patterns-chunk-intake]] |
| Wickham and Grolemund, *R for Data Science* (2017) | 520 | Complete — all 520 physical pages | [[r-for-data-science-chunk-intake]] |

Total physical coverage target: **3,789 pages**. Closed as of 2026-07-24:
**3,789 pages (100%)**. All eight source reports are complete; the
cross-source architecture synthesis is now unblocked.

## Intake Rule

Each report records:

1. exact physical-page or named-section chunks;
2. source claims and source limitations;
3. transferable principles;
4. Markdown, instruction, retrieval, learning, engineering, value, and
   governance implications where present;
5. contradictions and negative findings;
6. proposed owner returns without changing the final architecture early.

“Extracted” means searchable text exists in temporary working files. It does not
mean read, ingested, understood, or accepted.

## Decision Gate

All eight reports are closed. The evidence-only cross-source synthesis is now
recorded in `vault-skeleton-design.md` §8 and distinguishes:

- repeated independent evidence;
- source-specific advice;
- dated or volatile claims;
- unresolved contradictions;
- current `.ROOT` behavior already supported;
- genuine deltas that justify change.

This closes source intake, not architecture approval. CASTLE/Chris review is the
next gate; no move, validator implementation, or metadata/governance change is
authorized by these reports.
