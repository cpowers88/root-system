---
type: source-summary
tier: 1
source-role: support
tags: [source, reference, ai-tooling]
---

# OpenAI Platform, ChatGPT, and Codex Docs Pack (July 2026)

**Organization**: OpenAI
**Type**: official docs and developer articles
**Location**: `00-BRAIN\CASTLE\raw\books\OPEN_AI-CHATGPT_CODEX_FILES\` (immutable)
**Accessed**: July 12, 2026
**Tier**: 1 for mechanics; volatile details require upstream verification

## Ingestion Status

- 95 Markdown files; 1,009,215 bytes.
- Each page stays atomic so headings, code, and provenance are not split.
- Inventory, source URLs, hashes, dedupe, and thematic routing complete.
- Core semantic synthesis (Chunks 01–04 and 08) completed July 12; remaining chunks stay targeted reference. No roadmap/doctrine changes were justified.
- Raw files were untouched.

## Ten Retrieval Chunks

| # | Theme | Files |
|---|---|---:|
| 01 | Platform orientation, models, SDKs, modalities | 13 |
| 02 | Responses lifecycle, state, transport, migration | 11 |
| 03 | Tool calling and hosted/local tools | 15 |
| 04 | Agents SDK, orchestration, state, observability | 14 unique |
| 05 | MCP, connectors, ChatGPT Apps, ChatKit | 12 |
| 06 | GPT Actions | 6 |
| 07 | Prompting and reasoning | 7 |
| 08 | Evals, datasets, graders, red teaming | 7 |
| 09 | Fine-tuning and preference optimization | 6 |
| 10 | Legacy Assistants transition | 3 |

Routing follows each capture's preserved `source` URL and guide family. `Agents SDK  OpenAI API 1.md` is byte-identical to `Agents SDK  OpenAI API.md` (SHA-256 `0DDB73D5...92DB1`); both remain in raw pending Chris's decision.

## Claims Available After Review

| Claim family | Phase / skill |
|---|---|
| Responses architecture, state, streaming, background, migration | Phase 1; Phase 3 |
| Tool schemas, structured outputs, retrieval, safe execution | Phase 1; Phase 3 |
| Agent orchestration, guardrails, observability, eval iteration | Phase 3; Phase 7 |
| MCP, Apps, ChatKit, Actions integration choices | technology landscape; future delivery |
| Fine-tuning decision paths | parked advanced pending measured need |

## Recheck Rules

- Verify live models, prices, limits, SDK syntax, endpoints, and feature status before implementation.
- Treat Assistants material as migration context, not default architecture.
- Vendor articles do not independently prove ROI or demand.
- Park fine-tuning until evals show simpler approaches are insufficient.

## Semantic Review Order

Chunks 01, 02, 03, 04, then 08 form the core path. Review 05 next for integration decisions; use 06, 07, 09, and 10 only for concrete projects.

## Applied

Core findings were applied as audit criteria in `00-BRAIN\Session_Logs\FINAL_ROOT_LAUNCH_OPTIMIZATION_REPORT_2026-07-12.md`: Responses-first design, schemas at boundaries, least tool exposure, human approval for consequential actions, and traces/evals before multi-agent scale.

## Skill and Tool Candidates

- `execution-owner: Claude Code` — source-pack coverage and duplicate-hash validator; destination requires Chris approval.

## Entered in [[source-map]]: yes
