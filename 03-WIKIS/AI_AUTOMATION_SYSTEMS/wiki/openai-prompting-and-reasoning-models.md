---
type: research
tags: [ai-automation, openai, prompting, reasoning-models, agent-patterns]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ — Prompt engineering, Prompt optimizer, Reasoning models, Reasoning best practices (official OpenAI API docs, relocated from CASTLE July 12, 2026; read in full for the first time in this pass — CASTLE's own ingest marked this chunk "review only for concrete projects," never actually read)
---

# OpenAI Prompting Craft and Reasoning-Model Mechanics

**Official OpenAI API documentation, read in full July 12, 2026.** CASTLE's
shallow first pass (`00-BRAIN\CASTLE\wiki\source-summaries\openai-platform-docs-pack-2026-07.md`)
never opened this chunk — its own semantic-review order explicitly deferred
prompting/reasoning (Chunk 07) to "use only for concrete projects." This page
is that deferred read, plus a direct comparison to the Claude-side reasoning
vocabulary this wiki already knows from the Claude Code docs pack.

## One-paragraph summary

OpenAI splits its model family into two prompting regimes — GPT models
("junior coworker": fast, cheap, needs explicit step-by-step instructions)
and reasoning models ("senior coworker": slower, pricier, works from a goal
and fills gaps itself) — with a `reasoning.effort` parameter (`none` →
`minimal` → `low` → `medium` → `high` → `xhigh`) that trades latency/cost for
depth, model-dependent defaults, and adaptive internal use (simple tasks
burn fewer reasoning tokens automatically even at a fixed effort setting).
The most consequential craft advice: **reasoning models actively perform
worse with "think step by step" prompting** — chain-of-thought instruction
is redundant with (and can conflict with) the model's own internal reasoning
process, the opposite of the advice that applies to non-reasoning models.

## Prompt structure and message-role mechanics

- **Chain of command**: `developer` messages (app-level rules, highest
  priority) > `user` messages (end-user input) > `assistant` (model output).
  Analogous to a function definition (`developer`) applied to arguments
  (`user`). The `instructions` API parameter is shorthand for a `developer`
  message but does **not** persist across turns when using
  `previous_response_id` — it must be resent every call if it should keep
  applying.
- **Four-section prompt convention**: Identity → Instructions → Examples →
  Context, marked with Markdown headers and XML tags for the model to parse
  boundaries reliably. Context (RAG-style injected data) goes last because
  it changes per-request while the rest is stable — this ordering also
  maximizes prompt-cache hits (stable content first, volatile content last,
  same principle as the mid-session-caching mechanics in
  [[claude-code-context-and-instruction-economics]]).
- **Prompt versioning is moving out of the platform and into code.** OpenAI
  is deprecating reusable Prompt objects (`v1/prompts`): de-emphasized
  starting June 3, 2026, shut down November 30, 2026. Replacement pattern:
  keep prompt-builder functions in a small code module near the feature,
  with typed inputs, tests, and normal code review/deployment — i.e., treat
  a prompt exactly like source code, not a CMS entry. This is the same
  "write it like code, prune it when behavior drifts" instinct
  `Best_Practices_for_Claude_Code.md` already established for CLAUDE.md.
- **Few-shot vs. zero-shot**: for GPT models, few-shot examples steer
  behavior without fine-tuning; for reasoning models, try zero-shot first —
  reasoning models often don't need examples, and mismatched examples can
  actively hurt (discrepancies between the example and the instructions
  confuse the internal reasoning process).

## Reasoning-model mechanics not previously in this wiki

- **Reasoning tokens are invisible but billed and context-consuming.**
  They occupy space in the context window and count as output tokens, but
  the raw text is never returned — only an optional `summary` (`auto`,
  `concise`, or `detailed`, model-dependent) is. OpenAI recommends reserving
  **at least 25,000 tokens** of headroom for reasoning + output when first
  experimenting with a reasoning model, since hitting the cap mid-reasoning
  returns `status: incomplete` and can bill for input+reasoning tokens with
  *zero* visible output.
- **Reasoning state persistence — three modes**: `reasoning.context` set to
  `current_turn` (default-ish; only this turn's reasoning renders forward),
  `all_turns` (renders compatible reasoning from every prior turn — needs
  `previous_response_id` or full manual replay), or `auto` (model picks).
  For stateless/zero-data-retention use, `reasoning.encrypted_content` lets
  the caller carry encrypted reasoning tokens forward manually. This is a
  materially different persistence model from Claude's prompt-caching
  approach (which caches by exact-prefix match across the whole
  conversation, not per-reasoning-block) — different vendors solved
  "carry expensive internal state forward cheaply" with different
  primitives, worth knowing precisely rather than assuming parity.
- **`reasoning.mode`: `standard` vs. `pro`.** Independent of `effort` — mode
  selects execution depth, effort controls how much reasoning within that
  mode. `pro` costs more (aggregates more underlying model work) and is
  reserved for genuinely hard tasks that can tolerate latency.
- **`phase` field (`commentary` vs. `final_answer`)** — for long-running,
  tool-heavy GPT-5.5/5.4 flows, tags intermediate updates vs. the completed
  answer so preambles before tool calls aren't mistaken for final output.
  Optional but recommended; dropping it on manual history replay can cause
  early-stopping bugs.
- **Markdown is off by default in reasoning-model output** (since
  `o1-2024-12-17`) — must include the literal string `Formatting
  re-enabled` on the first line of the developer message to get Markdown
  back. An easy silent failure mode if migrating a GPT-model prompt to a
  reasoning model without adjusting for this.

## Direct comparison: OpenAI `reasoning.effort` vs. Claude Code's effort scale

| | OpenAI `reasoning.effort` | Claude Code (e.g. `/code-review` levels) |
|---|---|---|
| Scale | `none, minimal, low, medium, high, xhigh` | `low, medium, high, xhigh, max` |
| Selection | Per-API-call parameter, model-dependent defaults | Per-invocation flag/skill argument |
| Adaptive? | Yes — model uses fewer tokens on easy sub-tasks even at a fixed effort | Not documented as adaptive in the docs read so far |

Six-ish-point effort scales with near-identical naming (`low/medium/high/xhigh`
shared verbatim) emerged independently at both labs — convergent vocabulary
for the same underlying trade-off (quality vs. latency/cost), useful to know
precisely when translating between the two ecosystems rather than assuming
either vendor invented the concept.

## Why this matters for this wiki / `.ROOT`

- **The four-section prompt convention (Identity/Instructions/Examples/
  Context) is the same shape `.ROOT` section-operating files already use**
  informally (purpose → rules → worked example → live context) — another
  independent-vendor validation of a pattern `.ROOT` converged on before
  reading either company's docs, same story as
  [[claude-code-prompt-library-patterns]]'s six-pattern checklist.
- **"Don't chain-of-thought a reasoning model" is a real, checkable craft
  rule** for any future OpenAI-model integration `.ROOT` might build — worth
  remembering precisely rather than defaulting to Claude-side prompting
  habits if a project ever calls the OpenAI API directly.
- **The prompt-versioning deprecation (Prompt objects → code) is a strong,
  dated recency flag** for anyone reading the raw OpenAI docs later:
  anything referencing saved/reusable Prompt objects in this pack is on a
  fixed sunset timeline (de-emphasized June 3, 2026; shut down November 30,
  2026) — a concrete instance of the source-map's general "verify live
  models, prices, limits before implementation" recheck rule, not abstract.
- Companion page: [[openai-evals-and-red-teaming]] covers the
  measurement/verification side this page's prompting craft feeds into.

---
*Processed July 12, 2026. Source in raw/ (immutable).*
