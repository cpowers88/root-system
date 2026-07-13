---
type: research
tags: [ai-automation, openai, fine-tuning, assistants-api, legacy, platform-landscape]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ (OpenAI official docs, relocated from CASTLE July 12, 2026) — Fine-tuning best practices, Supervised fine-tuning, Reinforcement fine-tuning, Reinforcement fine-tuning use cases, Direct preference optimization, Vision fine-tuning, Assistants API deep dive, Assistants API tools, Assistants migration guide
---

# OpenAI Fine-Tuning Methods and Legacy Assistants API

**Official OpenAI documentation, read in full July 12, 2026.** CASTLE's prior
pass (`00-BRAIN\CASTLE\wiki\source-summaries\openai-platform-docs-pack-2026-07.md`)
already recommended parking fine-tuning "until evals show simpler approaches
are insufficient" and treating Assistants as migration context, not default
architecture. This page doesn't relitigate that verdict — it turns out the
docs themselves now make the call closer to moot than CASTLE's pass could see
from an inventory-level read, because both surfaces carry hard shutdown dates
that weren't previously on record precisely.

## One-paragraph summary

**OpenAI is actively shutting down both surfaces in this chunk, not just
deprioritizing them.** The fine-tuning platform ("winding down," per every
fine-tuning doc's own banner) is already closed to new users — existing users
can still create training jobs "for the coming months," and trained models
stay servable until their base model is deprecated, but this is not a live
option to build on. The Assistants API has a hard, specific shutdown date:
**August 26, 2026** — after "achieving feature parity" with the Responses
API, which is now positioned as the sole forward-compatible mental model
(prompts replace Assistants, conversations replace threads, responses
replace runs, items replace run steps). Neither surface is something `.ROOT`
would newly adopt even in a hypothetical technology-landscape sense; this
page exists so a future session doesn't have to re-derive "is this still
relevant" from scratch.

## Fine-tuning: four methods, one shared precondition

| Method | How it works | Best for | Models |
|---|---|---|---|
| Supervised (SFT) | Train on example prompt→correct-response pairs | Classification, nuanced translation, format-specific generation, correcting instruction-following failures | `gpt-4.1` family |
| Reinforcement (RFT) | A programmable grader scores every candidate response; policy-gradient updates favor high scorers | Complex domain reasoning with verifiable answers (medical diagnosis, legal passage relevance) | `o4-mini` only (reasoning models) |
| Direct Preference Optimization (DPO) | Train on (prompt, preferred response, non-preferred response) triples | Subjective preference tasks — tone, style, "focus on the right things" summarization | `gpt-4.1` family |
| Vision | SFT restricted to image-containing examples | Image classification, correcting complex-prompt instruction failures on visual input | `gpt-4o` |

**The precondition every method shares, stated explicitly in the Supervised
Fine-Tuning guide: "Good evals first! Only invest in fine-tuning after
setting up evals."** This is the same verdict CASTLE already reached
independently — the docs themselves gate fine-tuning behind eval
infrastructure that has to exist first, for an unrelated reason (RFT's
own guide: if the model already scores at the ceiling or floor on your eval,
there's no training signal to learn from, so fine-tuning literally cannot
help until an eval reveals a real gap).

**Practical minimums, in case ever revisited:** SFT needs a 10-example floor,
50–100 to see real improvement. RFT is reasoning-model-only and use-case
gated (deterministic-checkable code/config generation, structured fact
extraction, complex rule/policy application — not general chat quality).
DPO recommends running SFT first, then DPO on top, rather than DPO alone.
Vision fine-tuning excludes any image containing people, faces, children, or
CAPTCHAs — a hard content-moderation filter, not a configurable one.

**RFT use cases, condensed** (from real customer examples in the docs — useful
vocabulary if a client audit ever surfaces a "should we fine-tune" question):
turning instructions into working code that must compile/pass tests
(ChipStack chip-verification binding, Runloop Stripe-API code generation),
pulling facts into verifiable structured output (Ambience medical coding,
Harvey legal-citation extraction), and applying nuanced multi-step rules
(Accordance tax analysis, SafetyKit content-policy enforcement, Thomson
Reuters legal document review/compare/summarize). All three categories share
one property: a grader that can score correctness *without a human in the
loop* — if that can't be written, RFT is explicitly "not the right tool."

## Assistants API: deprecated, shutting down August 26, 2026

Every Assistants doc in this chunk opens with the same banner: *"After
achieving feature parity in the Responses API, we've deprecated the
Assistants API. It will shut down on August 26, 2026."* This is a harder
verdict than "migration context" — it's an end-of-life date, not an ongoing
alternative architecture.

**What Assistants were:** a persistent, server-managed bundle of model +
instructions + tools (`code_interpreter`, `file_search`, custom
`function` calling, up to 128 tools), operating over **Threads** (message
history, server-truncated to fit context) via **Runs** (async executions
with a status lifecycle: queued → in_progress → completed/failed/expired,
with thread-locking while a run is active) producing **Run Steps**
(message-creation or tool-call records).

**What replaces each concept, per the migration guide:**

| Assistants concept | Responses-API replacement | Why |
|---|---|---|
| Assistant | Prompt | Versioned behavioral profile — snapshot, diff, roll back, point code at a version ID |
| Thread | Conversation | Stores generalized items (messages, tool calls, outputs), not just messages |
| Run | Response | Send input items, get output items back; tool-call loop explicitly managed by your app, not the server |
| Run Step | Item | Generalized — message, tool call, or output |

Migration is explicitly **not automated** — OpenAI provides no thread→
conversation migration tool; the guide's own recommendation is to route new
chats onto Conversations going forward and backfill old threads only "as
necessary," with a worked Python example for that backfill. Note also:
**prompt objects (the Assistants replacement) are themselves being
deprecated** per a separate timeline referenced in the migration guide — a
detail CASTLE's pass didn't have, worth knowing precisely if this is ever
revisited, since it means "migrate to prompts" isn't itself a fully stable
end state either.

## Why this matters for this wiki / `.ROOT`

- **This strengthens, not contradicts, CASTLE's "park fine-tuning" verdict.**
  It's not just deprioritized — new fine-tuning access is already closed, and
  Assistants has a dated shutdown. Nothing here changes the recommendation;
  if anything it removes ambiguity about whether it's worth a second look
  soon (it isn't — there's no live surface to newly adopt).
- **The eval-before-fine-tuning gate is a reusable due-diligence rule**,
  independent of vendor — if `.ROOT` or a client project ever considers any
  model customization (OpenAI or otherwise), "do you have an eval that shows
  the base model scoring between floor and ceiling on this task" is the
  first question, sourced directly to OpenAI's own guidance rather than
  general caution. See [[openai-evals-and-red-teaming]] for the eval
  mechanics that gate is built on.
- Companion page: [[openai-responses-api-state-and-streaming]] covers what
  Assistants migrates *to* — Conversations/Items replace Threads/Run Steps.
- **The RFT use-case pattern (verifiable grader, no human in the loop) is a
  useful audit-conversation vocabulary item** for `05-BUSINESS` client work —
  it names precisely which tasks are fine-tuning-shaped versus which aren't,
  which is a faster filter than explaining fine-tuning mechanics from
  scratch to a skeptical client.
- **No action item.** Both surfaces are confirmed dead ends for `.ROOT`'s own
  use, recorded here so the question doesn't get re-asked from zero.

---
*Processed July 12, 2026. Source in `raw/OPEN_AI-CHATGPT_CODEX_FILES/` (immutable).*
