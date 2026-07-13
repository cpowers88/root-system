---
type: research
tags: [ai-automation, openai, models, api, prompting]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ (OpenAI official docs, moved from CASTLE raw/ to this wiki July 12, 2026 — "OpenAI API.md" [Models], "OpenAI API 1.md" [Pricing], "Models and providers  OpenAI API.md", "Model guidance  OpenAI API.md", "Model optimization  OpenAI API.md", "Text generation  OpenAI API.md")
---

# OpenAI Model Lineup, Selection, and Optimization Workflow

**Official OpenAI documentation, read in full July 12, 2026.** CASTLE's
July 12 shallow pass (`00-BRAIN\CASTLE\wiki\source-summaries\openai-platform-docs-pack-2026-07.md`)
inventoried this pack into ten retrieval chunks and only deep-read Chunks
01–04 and 08 at the architecture level; this page is this wiki's own full
read of the model-selection and optimization slice, one layer more precise
than the CASTLE pass.

## One-paragraph summary

GPT-5.6 (aliased `gpt-5.6` → `gpt-5.6-sol`) is OpenAI's current flagship,
offered in three tiers — `sol` (flagship reasoning/coding), `terra`
(balanced), `luna` (cheap high-volume) — priced $1–5 per million input
tokens and $6–30 per million output tokens depending on tier, roughly half
that again for the long-context rate. The model-optimization loop is a
fixed five-step flywheel (evals → prompt → optional fine-tune → measure →
tweak, repeat), and prompt engineering technique now matters more than
scale tuning: OpenAI's own internal coding-agent evals found leaner system
prompts improved scores 10–15% *while cutting tokens 41–66% and cost
33–67%* — evidence that verbose instructions actively hurt performance,
not just cost, directly validating `.ROOT`'s own <200-line instruction-file
discipline from a second vendor independent of Anthropic.

## Source-naming defect — flag for whoever else routes this pack

Twelve files in this raw folder (`OpenAI API.md` through `OpenAI API 9.md`,
plus `OpenAI AP15I (1).md` / `(2).md`) all captured the literal page
`<title>` tag ("OpenAI API"), which OpenAI's doc site sets identically on
every guide page — so the real topic survives only in each file's
`source:` URL, not its filename. **Checked by hash: none are duplicates**
(unlike the already-flagged byte-identical `Agents SDK` pair) — all twelve
are genuinely distinct content that happened to collide on filename during
capture. Two are used here (`OpenAI API.md` = Models, `OpenAI API 1.md` =
Pricing); the other ten are out of this page's scope (Agent Skills, Shell
tool, Retrieval/vector stores, Responses Multi-agent, Webhooks, Compaction,
Prompting, Graders, Agents SDK quickstart, ChatKit) and need routing by
whoever covers those CASTLE chunks — this is a *collision-masking* defect,
not a duplication one, worth its own note alongside the existing
Agents-SDK duplicate flag rather than silently left for someone to
rediscover by opening all twelve.

## The GPT-5.6 model family

| Model | Role | Input | Cached input | Output (short context) |
|---|---|---|---|---|
| `gpt-5.6-sol` (= `gpt-5.6` alias) | Flagship — complex reasoning/coding | $5.00/M | $0.50/M | $30.00/M |
| `gpt-5.6-terra` | Balance intelligence/cost | $2.50/M | $0.25/M | $15.00/M |
| `gpt-5.6-luna` | Cost-sensitive, high-volume | $1.00/M | $0.10/M | $6.00/M |

Long-context rates roughly double the short-context ones for the same
tier. Prior families remain priced and available: `gpt-5.5` ($5/$30),
`gpt-5.5-pro` ($30/$180 — no cache discount), `gpt-5.4` ($2.50/$15) down to
`gpt-5.4-nano` ($0.20/$1.25). **Regional data-residency processing carries
a 10% uplift** on eligible post-March-2026 models; Bedrock-hosted OpenAI
models bill through AWS at different rates.

## What's actually new in GPT-5.6 (migration-relevant)

- **Programmatic Tool Calling (PTC)**: the model writes JavaScript that
  calls eligible tools directly in a hosted runtime, processes results,
  and returns only the final structured output — Zero-Data-Retention
  compatible, no extra container cost. Use it for *bounded* stages
  (filtering, joining, ranking, dedup, validation) where intermediate
  results are large and don't need model judgment between each call; don't
  use it when one call suffices, intermediate outputs are already small,
  each result changes the next decision, or an action needs approval.
- **Multi-agent [beta]**: a GPT-5.6 instance coordinates subagents in
  parallel and synthesizes results — explicitly compared in the docs to
  "ultra mode in Codex." Available in the Responses API only.
- **Explicit prompt caching**: mark exactly which prefixes to cache
  (vs. automatic/implicit mode). Cache *writes* cost 1.25× the uncached
  input rate; cache *reads* stay discounted — track both `cached_tokens`
  and `cache_write_tokens` to know true net cost, since writing an
  ill-chosen breakpoint can cost more than it saves.
- **Persisted reasoning** (`reasoning.context`): reuse prior turns'
  reasoning items for multi-turn quality/cache efficiency. `all_turns`
  when goals stay stable across turns (pair with `previous_response_id`);
  `current_turn` when earlier reasoning is stale. Under `store: false` /
  ZDR, must explicitly `include: ["reasoning.encrypted_content"]` and
  replay it.
- **`reasoning.effort`** now spans `none | low | medium | high | xhigh |
  max` (six levels, up from prior families' narrower range). **`max`** is
  new — reserved for the hardest quality-first work; compare against
  `xhigh` rather than assuming higher is always better.
- **Pro mode** (`reasoning.mode: "pro"`): more model work before a single
  final answer, same model/effort slug (no separate "Pro" model). Billed
  at the model's standard token rate on the aggregated work. Reserve for
  cases where a marginal quality gain materially matters — not routine or
  latency-sensitive work.
- **Real-time safety classifiers**: cyber/bio misuse classifiers can
  synchronously pause generation mid-stream or refuse outright, including
  on legitimate dual-use work (security research, patch dev, defensive
  testing) — send a stable `safety_identifier` per end-user to help the
  system distinguish abuse patterns from legitimate use.

## Prompting best practices GPT-5.6 actually measured

- **Leaner prompts win on quality, not just cost** (the finding in the
  one-paragraph summary above) — remove one instruction/example/tool
  group at a time and re-run the same evals rather than guessing.
- **State each instruction once.** Repeated "ask first" / "don't mutate"
  boundaries can *increase* unnecessary approval requests rather than
  reinforcing the rule.
- **A compact autonomy policy is usually sufficient** — the docs' own
  template: read/explain/plan requests get inspection + a report only;
  change/build/fix requests get in-scope changes + non-destructive
  validation without asking first; external writes, destructive actions,
  purchases, and scope expansion require confirmation. This is
  structurally identical to `.ROOT`'s own "Executing actions with care"
  reversibility framing.
- **`text.verbosity`** (`low`/`medium`/`high`) sets a *default* level of
  detail app-wide; task-specific length rules belong in the prompt itself,
  not as a blanket "be concise" instruction (GPT-5.6 is already more
  concise by default than 5.5 — old brevity instructions may now be
  redundant or actively harmful).
- **Message role priority is fixed**: `developer` > `user` > `assistant`
  — `developer` messages (think: function definition) outrank `user`
  messages (think: arguments). The `instructions` parameter is
  per-request only — it does *not* persist across `previous_response_id`
  turns, unlike a system-prompt mental model might suggest.
- **Reusable prompt objects are being deprecated**: de-emphasized from
  June 3, 2026, `v1/prompts` shuts down November 30, 2026. OpenAI's own
  recommendation is to version prompts as code (typed builders near the
  feature, tests/evals before changing production prompts) rather than
  server-stored prompt objects — not a `.ROOT` concern directly, but
  validates keeping prompt/instruction text in versioned files rather
  than an opaque external store, same principle `.ROOT` already follows.

## The model-optimization flywheel

```text
write evals -> prompt the model -> (optional) fine-tune -> run evals on
representative data -> tweak prompt/fine-tune dataset -> repeat
```

Fine-tuning itself is being wound down for new users (existing users can
still create jobs "for the coming months"); four methods remain documented
(SFT, vision fine-tuning, DPO, RFT — the last requiring expert graders and
reasoning-only base models) but the guide's own framing treats fine-tuning
as the last resort after evals + prompting, not a default lever.

## Why this matters for this wiki / `.ROOT`

- **Second independent vendor confirming the <200-line-instruction
  discipline** — this time with a hard number (10-15% quality gain,
  41-66% token cut) rather than Anthropic's qualitative "adherence drops."
  Worth citing alongside the Claude Code finding in
  [[claude-code-context-and-instruction-economics]] the next time this
  wiki argues for pruning an always-loaded file.
- **The compact-autonomy-policy template is close to a direct match** for
  how `.ROOT`'s own governance already frames reversible-vs-hard-to-reverse
  actions — worth noting as a second-source validation, not a change.
- **Evals-before-prompting (BDD-style)** is a concrete idea this wiki
  hasn't surfaced yet: write the eval first, then the prompt. Relevant if
  `.ROOT` ever builds a proof-project that calls the OpenAI API directly
  rather than only using Claude Code.
- Companion page: [[openai-multimodal-generation]] covers vision, image
  generation, audio, and voice agents from the same pack.

---
*Processed July 12, 2026. Source in raw/ (immutable).*
