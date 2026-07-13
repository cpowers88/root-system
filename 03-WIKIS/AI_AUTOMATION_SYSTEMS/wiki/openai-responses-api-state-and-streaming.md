---
type: research
tags: [ai-automation, openai, responses-api, context-management, prompt-caching]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ (OpenAI official docs, relocated from CASTLE July 12, 2026) — OpenAI API Platform Documentation, Developer quickstart, Conversation state, Results and state, Streaming API responses, WebSocket Mode, Background mode, Migrate to the Responses API, From prompts to products (One year of Responses), Structured model outputs, Prompt caching, Counting tokens, File inputs
---

# OpenAI Responses API — State, Streaming, and Context Mechanics

**Official OpenAI documentation, read in full July 12, 2026.** CASTLE already
did a shallow pass on this 95-file pack (`00-BRAIN\CASTLE\wiki\source-summaries\openai-platform-docs-pack-2026-07.md`)
and promoted high-level claims (Responses-first design, schema-constrained
tools, least privilege, human approval, traces/evals) into the July 12
launch audit. This page goes to full technical depth on the mechanics
behind those claims — state management, streaming transports, caching, and
structured output constraints — the layer a governance audit summary
doesn't carry. Notable: this is also Codex's own underlying API surface
(`OpenAI CLI.md`, read in the companion tooling page, explicitly frames CLI
usage "for Codex") — `.ROOT` already has a live Codex lane
(`00-BRAIN\CODEX.md`), so this isn't purely landscape research the way the
Claude Code CI/CD chunk was.

## One-paragraph summary

The Responses API is OpenAI's recommended primitive over the older Chat
Completions API — same request shape family, but built around typed
**Items** (`message`, `reasoning`, `function_call`, `function_call_output`)
instead of a flat `messages` array, with three distinct ways to carry state
across turns (manual replay, `previous_response_id` chaining, or a durable
Conversations API object), two transports beyond plain HTTP (SSE streaming,
and a WebSocket mode built specifically for tool-call-heavy agentic loops),
and a fully asynchronous background mode for multi-minute reasoning tasks.
OpenAI claims concrete numbers for the migration: 3% SWE-bench improvement
and 40–80% better cache utilization vs. Chat Completions on the same
prompt/setup — vendor-reported, not independently verified, but backed by
five real production case studies in the "One year of Responses" retrospective.

## Three ways to carry state (and what each actually costs)

| Approach | Mechanism | Billing/cost note |
|---|---|---|
| Manual replay | Append `response.output` items back into the next `input` array | All replayed tokens billed as input tokens every turn — no discount |
| `previous_response_id` | Chain responses server-side; only send new items | **Still bills all prior input tokens in the chain** — the guide states this explicitly twice. The benefit is *latency* (cache reuse), not token cost. Does not carry over top-level `instructions` — must resend those every turn. |
| Conversations API | `openai.conversations.create()` → durable object with its own ID, persists across sessions/devices/jobs | Pass `conversation=<id>` instead of chaining individual response IDs — the object *is* the state, not a pointer to the last turn |

**Reasoning-model specific**: for stateless (ZDR-compatible) multi-turn use
with reasoning models, add `reasoning.encrypted_content` to `include` and
replay every item in `output` — this preserves encrypted reasoning tokens
and the assistant `phase` field without persisting anything server-side.
Models supporting persisted reasoning can instead set
`reasoning.context: "all_turns"` to reuse earlier-turn reasoning without
manual replay.

**Agents SDK result surfaces** (from `Results and state`, distinct from raw
Responses state): `finalOutput`/`final_output` (the answer), `history`/
`to_input_list()` (local replay), `lastAgent`/`last_agent` (which specialist
should own the next turn after a handoff), `lastResponseId`/
`last_response_id` (server-chained continuation), and — the case that
matters most for anything resembling `.ROOT`'s human-approval-gated
patterns — `interruptions` + `state`/`to_state()`: when a run pauses for
approval, `finalOutput` stays empty and `state` is the serializable snapshot
you persist and later resume after a human approves or rejects the pending
tool calls. This is the same approval-gate shape `.ROOT`'s own permission
hardening and Claude Code's `bypassPermissions`-only protected paths already
converged on independently (see [[claude-code-permissions-security-and-review]]).

## Streaming, WebSocket, and background mode — three transports for three problems

- **SSE streaming** (`stream=true`, plain HTTP): typed semantic events
  (`response.created`, `response.output_text.delta`, `response.completed`,
  `error`, plus per-tool events like `response.function_call_arguments.delta`)
  rather than raw text chunks — you branch on `event.type`, not on parsing a
  delta string. Explicit moderation-risk note: streaming makes content
  harder to moderate since partial completions may not reflect the final
  output's safety classification.
- **WebSocket mode** (`/v1/responses` over a persistent socket): built
  specifically for **tool-call-heavy agentic loops** — up to ~40% faster
  end-to-end on rollouts with 20+ tool calls, because the connection keeps
  one **connection-local, in-memory-only** cache of the most recent response,
  so continuation reuses that state instead of re-fetching. This is why it's
  compatible with `store=false`/Zero Data Retention — nothing hits disk. A
  socket runs turns **sequentially, one in-flight response at a time** (no
  multiplexing — use multiple connections for parallel runs), and hard-caps
  at 60 minutes before you must reconnect. A failed turn (`4xx`/`5xx`)
  evicts that `previous_response_id` from the connection cache to prevent
  reuse of stale state. `generate: false` lets a client "warm up" request
  state (tools/instructions loaded, no model call yet) before the real turn.
- **Background mode** (`background=true`): async execution for
  multi-minute reasoning tasks (the guide names Codex and Deep Research as
  the motivating examples), polled via `GET` on the response object.
  **Breaks Zero Data Retention** — background responses are stored ~10
  minutes to enable polling, so ZDR projects that use it lose that
  guarantee even though the request is still accepted "for legacy reasons."
  Requires `store=true` (stateless/background is a rejected combination).
  Can combine with `stream=true` to get both async execution *and* live
  events, tracked via a `sequence_number` cursor for reconnection. Canceling
  is idempotent — a second cancel call just returns the already-final object.

## Migrating from Chat Completions — the concrete differences

Chat Completions remains supported; Responses is recommended for all new
work. The real differences, precisely:

- **Items, not Messages.** A Chat Completions `message` bundles role +
  content + everything else into one object; Responses splits distinct
  concerns into typed Items (`message`, `function_call`,
  `function_call_output`, `reasoning`) correlated by `call_id`. The `n`
  parameter (multiple parallel generations) is gone — one generation per
  request, make separate requests if you need candidates.
- **Storage default flips implicitly.** Responses are stored by default;
  Chat Completions are stored by default only for *new* accounts. `store:
  false` disables storage in either.
- **Structured outputs move from `response_format` to `text.format`.**
  Same JSON Schema constraint system underneath (see below), different
  request field.
- **Function definitions are internally tagged** in Responses vs.
  externally tagged in Chat Completions, and **strict mode is the
  attempted default** in Responses (omitting `strict` tries strict, falls
  back to best-effort non-strict if the schema can't comply) vs.
  non-strict-by-default in Chat Completions.
- **Nine named migration failure modes**, worth keeping as a checklist for
  any future OpenAI-API build: reading `choices[0].message.content` instead
  of `output_text`/`output`; treating every output entry as a message
  (reasoning/tool/function-call items aren't); dropping reasoning or
  function-call items when manually replaying context; missing `call_id`
  on a function result; still using `response_format`; reusing old
  streaming-chunk handlers against typed events; and assuming
  `previous_response_id` removes prior-context billing (it doesn't).
- **Assistants API is sunsetting** August 26, 2026 (deprecated since
  August 26, 2025) — Responses now has Assistant-like and Thread-like
  objects, explicitly positioned as its replacement.

## Structured outputs — the JSON Schema constraint system

`text.format: { type: "json_schema", strict: true, schema: {...} }`
guarantees schema-conformant output (vs. JSON mode, which only guarantees
*valid* JSON, not schema match). Concrete limits worth remembering before
designing a schema for either this or a Claude tool definition:

- **Every field must be `required`** — there is no true "optional" field;
  emulate one with a `["string", "null"]` union type.
- **`additionalProperties: false` is mandatory** on every object.
- **Root object must be a plain object, not `anyOf`** — a Zod
  `discriminatedUnion` at the top level will fail; nest the union instead.
- **Hard caps**: 5,000 object properties total / 10 levels of nesting max;
  120,000 characters total across all property/enum/const strings; 1,000
  enum values total, and enum string length capped further (15,000 chars)
  once a single enum property exceeds 250 values.
- **Not yet supported**: `allOf`, `not`, `dependentRequired`,
  `dependentSchemas`, `if`/`then`/`else` — and for fine-tuned models
  specifically, several string/number/array constraint keywords are also
  unsupported.
- **`$ref`/`$defs` and recursive schemas (including self-`$ref` via `#`)
  are supported** — directly useful for any tree/graph-shaped tool
  parameter (e.g., a nested UI-component schema, shown verbatim in the
  source as a worked example).
- **Refusals surface structurally**: a safety refusal returns a `refusal`
  field instead of (or alongside) parsed content — check for it explicitly
  rather than assuming a schema-shaped response always succeeded.

## Prompt caching — direct comparison to Claude's mechanics

[[claude-code-context-and-instruction-economics]] documented Claude Code's
caching mechanics in this same wiki. The two engines solve the same
problem — reuse of a stable prefix — with meaningfully different levers:

| | OpenAI (Responses/Chat Completions) | Claude Code |
|---|---|---|
| **Trigger** | Automatic above 1,024 tokens; no opt-in needed | Automatic above the API's own threshold; no opt-in needed |
| **Routing** | Hash of the first ~256 tokens of the prefix, optionally combined with a developer-set `prompt_cache_key` for reliable routing to the same machine | Exact-prefix match on the full assembled context (system prompt → project context → conversation); no developer-facing routing key |
| **Manual control** | **Explicit cache breakpoints** (GPT-5.6+): mark exactly where a reusable prefix ends via `prompt_cache_breakpoint: {mode: "explicit"}` on a content block; up to 4 new writes per request, up to the latest 50 breakpoints considered for reads | No exposed breakpoint API — cache validity is entirely a function of session actions (model switch, MCP connect/disconnect, `/compact`, upgrade) rather than developer-marked prefixes |
| **Write cost** | **Billed on GPT-5.6+**: 1.25× the uncached input rate, reported in `cache_write_tokens`. Free on pre-GPT-5.6 models. | Not described as separately billed in the source material read for the companion page — worth verifying directly if cross-engine cost comparison ever matters |
| **Lifetime** | Pre-GPT-5.6: in-memory, 5–10 min inactivity, max ~1 hr. GPT-5.6+: minimum 30 min (only supported TTL value), "may be retained longer." Extended retention (specific older models only): up to 24 hr via GPU-local KV-tensor offload. | 5 min default (API billing) / 1 hr (Claude subscription, drops to 5 min under overage usage) |
| **Scope key** | Content-hash based — same prefix routes to the same cache regardless of client/session identity | Machine **and** directory scoped — two sessions in different directories, or the same directory with different git branch/status, don't share a cache even on one machine |
| **What's cacheable** | Messages, images (with matching `detail`), tool definitions, and the structured-output schema itself (schema acts as a prefix to the system message) | CLAUDE.md, auto memory, unscoped rules, and the growing conversation prefix |

**The one mechanic that doesn't have a Claude-side equivalent documented so
far**: OpenAI's `prompt_cache_key` throughput guidance — keep traffic per
key to ~15 requests/minute, partition across more keys for higher volume,
with a *stable* key-to-traffic mapping. This is a rate-shaping lever with
no analog surfaced in the Claude Code caching docs.

## Token counting — a capability Claude's docs don't describe

A dedicated endpoint, `POST /v1/responses/input_tokens`, accepts the exact
same payload shape as `responses.create` (text, images, files, tools,
conversations) and returns the **exact** token count the model will
actually receive — including structural/formatting tokens that local
tokenizers like `tiktoken` can't account for, and images/files that
character-based estimation (`chars / 4`) gets wrong entirely. Useful for
pre-flight cost estimation or size-based request routing (small prompts to
a cheaper model). No equivalent server-side counting endpoint was
documented in the Claude Code pack — Claude-side token accounting appeared
only as `/context` (introspective, current-session-only) rather than a
pre-flight count-before-you-send API.

## File inputs — type-dependent processing, not one code path

`input_file` items branch by file type, not a single "read the file"
behavior:

- **PDFs** (vision-capable models only): both extracted text *and* rendered
  page images go to the model — `detail: auto|low|high` controls image
  fidelity (`auto` resolves to `high` on GPT-5.6+, `low` on earlier
  models). Non-PDF files never get this — convert to PDF first if chart/
  diagram fidelity matters.
- **Non-PDF documents/text/code** (`.docx`, `.pptx`, `.txt`, code files):
  text extraction only, no embedded images.
- **Spreadsheets** (`.xlsx`, `.csv`, `.tsv`, etc.): a distinct
  "augmentation" path — only the first 1,000 rows per sheet, plus
  model-generated summary/header metadata, so the model works from a
  structured digest rather than a raw dump. For deep spreadsheet analysis
  (joins, aggregations, charting), the guide explicitly redirects to
  Hosted Shell instead.
- **Limits**: 50 MB per file, 50 MB combined per request, three input
  paths (base64 `file_data`, uploaded `file_id`, or external `file_url`).

## Five production case studies (Tier 3 — vendor blog, customer stories)

From "One year of Responses" — useful for grounding the abstract API
mechanics in what people actually build, not as independent evidence:
Raindrop AI (agent-failure monitoring via background analysis), Repo
Prompt (context-builder agent feeding a separate non-tool-calling
"Oracle" reasoning model — a clean **separation of context-gathering from
reasoning** pattern worth remembering generally), Collxn (Responses
replacing a full RAG build for a chat-over-personal-collection app —
concrete evidence Responses can substitute for RAG in some cases), Arcade
(computer-use tool turning screen recordings into product demos, cutting
publish-step count 50%), and Hexagon (a four-agent content pipeline plus
daily simulation runs to measure brand visibility in AI answers). The
recurring theme across all five: teams choosing Responses specifically for
its **built-in state/tool orchestration** over hand-rolling the equivalent.

## Why this matters for this wiki / `.ROOT`

- **This is Codex's underlying API, not just landscape research.** Unlike
  the Claude Code CI/CD/IDE integration chunk (genuinely "no current use
  case yet"), `.ROOT` already runs a live Codex lane
  (`00-BRAIN\CODEX.md`) — Codex sessions are built on exactly this API
  surface. Understanding the state/caching mechanics here has more direct
  bearing on Codex session behavior than most of this pack's other chunks.
- **The cross-engine caching comparison is the most reusable table in this
  page.** `.ROOT` runs sessions on both Claude and OpenAI-backed engines;
  knowing that OpenAI exposes manual cache-breakpoint control (with a
  billed write cost on newest models) while Claude's caching is entirely
  session-action-driven (with no manual breakpoint API but also no
  documented write cost) is directly useful if cost or latency tuning ever
  becomes a real concern rather than an assumption.
- **The `interruptions`/`state` approval-pause pattern validates `.ROOT`'s
  own human-gating instinct** independently of Claude Code's permission
  system — two unrelated vendors converged on "pause the run, serialize
  state, resume after a human decides" as the shape for consequential
  actions.
- **The structured-outputs constraint table is immediately reusable**
  any time a `.ROOT` skill or tool defines a JSON schema for either engine
  — the `additionalProperties: false` / all-fields-required / no-top-level-
  `anyOf` rules are easy to violate by habit if writing schema-first from a
  language-native type system (Zod, Pydantic) without checking this list.
- **No current build target**, honestly: `.ROOT` has no live application
  code calling this API directly (Codex is used as an agent CLI, not
  invoked as raw API calls from `.ROOT`'s own scripts) — this page is
  reference depth for the day that changes, not an active gap.
- Companion page for SDK/CLI/Agent-Builder surface:
  [[openai-sdks-cli-and-agent-builder]].

---
*Processed July 12, 2026. Source in `raw/OPEN_AI-CHATGPT_CODEX_FILES/` (immutable).*
