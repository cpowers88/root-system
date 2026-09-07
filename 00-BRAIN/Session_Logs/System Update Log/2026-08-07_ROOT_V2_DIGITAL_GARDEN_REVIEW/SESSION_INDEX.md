---
type: index
timeline: log
status: complete
tags: [governance, architecture, digital-garden, root-v2, system-update]
created: 2026-08-07
---

# `.ROOT V2` Digital-Garden Review — Evidence Packet

## Purpose and authority

This packet records the first external architecture comparison for a possible
successor runtime to `.ROOT`. It answers Chris's request to study the gardens
closest to the mission, preserve linked reports, and extract only the patterns
that improve learning, implementation, and economic value creation.

Authority remains Chris's current request, the North Star, `00-BRAIN/AGENT.md`,
and the owning contracts. This is a research and decision packet. It does not
authorize restructuring, migration, deletion, or a second live vault.

## Research boundary

- **Catalog used for discovery:** [best-of-digital-gardens](https://github.com/lyz-code/best-of-digital-gardens)
- **Gardens reviewed:** six, plus one supplemental agent-runtime comparison
- **Selection:** three close matches, two architectural contrasts, and one
  deliberately minimal negative control
- **Evidence standard:** repository-owned README, configuration, source, or
  build files; observations dated August 7, 2026
- **Excluded:** `nikitavoloboev/knowledge`, because that catalog entry now
  resolves to an unrelated Go-tools repository. This is evidence that the
  catalog is a discovery aid, not an authoritative ranking or currentness map.

## Direct conclusion

Do not make a clean-room replacement vault. Preserve `.ROOT` as the canonical
Markdown knowledge store and test a **shadow successor runtime** that compiles
small, task-specific views from it. The external gardens support four useful
patterns: canonical-source/derived-view separation, search-first retrieval,
explicit knowledge maturity, and atomic notes produced by real implementation.
None of the reviewed systems supplies `.ROOT`'s missing business proof loop by
itself.

## Packet inventory

- `01-davidgasquez-handbook.md` — strongest teaching and learning model.
- `02-lyz-blue-book.md` — broad lifecycle model and strongest overgrowth warning.
- `03-maxdeviant-knowledge.md` — minimal publishing negative control.
- `04-karlicoss-exobrain.md` — search-first retrieval and source/compiler split.
- `05-jethrokuan-braindump.md` — incremental source-to-view compilation.
- `06-simonw-til.md` — implementation-born atomic knowledge and generated index.
- `07-primeintellect-prime-agent.md` — agent-operated runtime, controlled
  self-refinement, durable execution, and security-boundary review.
- `ROOT_V2_MASTER_DESIGN_REPORT.md` — complete capability ceiling, architecture,
  data model, folder evolution, staged implementation, migration gates, risks,
  and exact decisions required from Chris.
- `comparison-and-root-v2-deltas.md` — cross-case findings, decision, and proposed
  V2 deltas.
- `claude-challenge-packet.md` — bounded independent-review brief for Claude.
- `claude-challenge-response.md` — Claude's independent verdict, objections,
  corrections, and smallest falsifiable pilot.

## Safe next action

Reconcile Claude's four corrections and the Prime Agent runtime-boundary
findings into a final proposed ADR. Interview Chris about the unresolved
product decisions before any prototype or structural change. If a Prime Agent
trial is later approved, run it only in a disposable non-sensitive environment,
never against the live vault.

## Validation result

The canonical read-only health gate was run after filing this packet on
2026-08-07.

- New packet frontmatter and timeline debt: **0**.
- Live Markdown text-integrity findings: **0**.
- Overall vault result: **BLOCKER**, from the pre-existing Claude sandbox gap
  that omits write-deny rules for the eight governed wiki `raw/` paths.
- Existing wiki review debt: **4** — two weekly-plan index omissions and the
  same two files reported as orphans.
- Not evaluated by the gate: semantic freshness, review-cadence completion,
  source routing/duplicate disposition, and ordinary direct-path prose outside
  its checked contracts.

The blocker prevents a system checkpoint or migration claim. It does not
invalidate this read-only comparison, and no repair is authorized by this
packet.

## Scope warning

“100% more efficient and effective” is a direction, not yet a measurable
acceptance test. The comparison report converts it into candidate metrics. No
claim of a 100% improvement is made in this packet.
