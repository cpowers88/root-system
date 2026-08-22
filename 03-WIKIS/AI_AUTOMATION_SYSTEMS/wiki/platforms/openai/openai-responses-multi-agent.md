---
type: research
timeline: reference
tags: [ai-automation, openai, multi-agent, responses-api, orchestration]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/OpenAI API 5.md (title-collided capture of "Enable Responses API Multi-agent" — https://developers.openai.com/api/docs/guides/responses-multi-agent — one of 12 files that inherited the generic title "OpenAI API" during capture; identified and routed July 12, 2026)
---

# OpenAI Responses API Multi-agent — A Third Orchestration Primitive

**Official OpenAI documentation, read in full July 12, 2026.** This is
architecturally distinct from the Agents SDK's handoffs/agents-as-tools
already covered in [[openai-agents-sdk-and-orchestration]] — Multi-agent is
a **built-in Responses API feature** (beta, all GPT-5.6 models), not an SDK
you install. `.ROOT` itself is a heavy user of parallel-fork research
patterns (this very OpenAI-docs ingest used six parallel forks), which makes
a vendor's built-in multi-agent primitive directly relevant landscape
research, not just an inventory item.

## One-paragraph summary

Multi-agent lets the model itself spawn and coordinate a tree of subagents
mid-response — `spawn_agent`, `send_message`, `followup_task`,
`wait_agent`, `interrupt_agent`, `list_agents` are six hosted collaboration
actions the model calls directly, with the root agent (`/root`) responsible
for synthesizing subagent output into a final answer. This is the same
"root delegates to bounded workers" shape `.ROOT`'s fork pattern already
uses, but pushed down into the API itself rather than orchestrated by
application code — the model decides when to spawn, not your harness.

## When OpenAI recommends it (and when not to)

Explicit guidance, not just a feature flag: use Multi-agent when work
splits into **independent, bounded tasks** where separate context improves
focus and parallel exploration reduces wall-clock time (codebase
exploration, comparing proposals/documents/hypotheses, researching multiple
sources, implementing independent components, investigating parallel
failure causes). Prefer one agent when each step depends on the previous
one, the task is small, agents would contend over shared mutable state, or
you need a fixed deterministic execution graph. This table is close to a
direct restatement of `.ROOT`'s own actual fork-dispatch judgment calls in
this conversation (parallel chunks for independent doc-pack sections;
sequential when one step's output determines the next), now with vendor
vocabulary for it.

## Mechanics

- **Agent tree, hierarchical paths.** Subagents get paths like
  `/root/researcher`, `/root/reviewer/tester` — a spawned agent can itself
  spawn children, unbounded depth, unbounded total subagent count. Only
  `max_concurrent_subagents` (default `3`, no fixed upper bound) limits how
  many are *simultaneously active* across the whole tree — direct analog to
  `.ROOT`'s own de facto practice of running 3-6 forks in parallel per
  ingest wave, though `.ROOT` sizes that by task count, not a request
  parameter.
- **The root agent owns synthesis.** Only `/root` messages tagged
  `phase: "final_answer"` are the actual reply; everything else is
  intermediate agent chatter your application should not surface directly.
- **HTTP vs. WebSocket is a real latency decision, not a style choice.**
  Over HTTP, the *entire* multi-agent response completes before your
  application can execute any function call each agent requested — one
  slow subagent blocks the whole batch's tool-output round trip. Over
  WebSocket, function outputs can be injected (`response.inject`) into the
  *running* response as soon as they're ready, so one agent's tool call
  doesn't stall the others. OpenAI's own guidance: HTTP is fine for
  few-call workflows (parallel web searches), WebSocket is recommended for
  tool-heavy or long-running Multi-agent workflows specifically because of
  this blocking behavior.
- **Compaction is implicitly forced on.** When `multi_agent.enabled` is
  `true`, server-side compaction activates automatically even if the
  request never configured `context_management` — applied independently
  per agent, preserving each agent's own context separately. The
  `/responses/compact` standalone endpoint is explicitly **not** supported
  while Multi-agent is enabled (see [[openai-webhooks-and-compaction]] for
  compaction mechanics generally). Two other features are disabled
  outright while Multi-agent runs: `reasoning.summary` and
  `max_tool_calls`.
- **Injected, non-editable system instructions.** OpenAI automatically
  appends a developer message to root and subagents describing the
  collaboration actions and concurrency-slot count; you cannot remove it,
  only add to it additively. Worth knowing precisely: unlike a Claude Code
  fork (which receives exactly the prompt the coordinator wrote, no vendor
  boilerplate injected), an OpenAI Multi-agent subagent always carries this
  vendor-authored framing whether you want it or not.

## Comparison to `.ROOT`'s fork pattern and to the Agents SDK

| | `.ROOT` forks (this wiki, today) | OpenAI Multi-agent | OpenAI Agents SDK (Agents-as-tools) |
|---|---|---|---|
| Who decides to spawn | The coordinating Claude session, per explicit instruction | The model itself, mid-response, per its own judgment | Application code, calling `agent.asTool()` |
| Coordination | Forks report once, coordinator reads all reports | `send_message`/`wait_agent` allow live mid-task messaging between agents | None — a tool call is a tool call |
| Depth | Coordinator spawns forks directly; forks don't spawn sub-forks in current practice | Unbounded tree depth, subagents can spawn their own subagents | Flat — the manager calls specialists, specialists don't call their own specialists via this primitive |
| Transport | N/A (same harness) | HTTP (blocking) or WebSocket (non-blocking injection) | N/A (regular request/response) |

The live mid-task messaging (`send_message` to a *running* agent, without
starting a new turn) is the one capability with no `.ROOT` or Claude Code
equivalent documented anywhere in this wiki so far — closest adjacent idea
is Claude Code's experimental, disabled-by-default "agent teams"
(peer-messaging, noted in [[claude-code-workflows-and-sessions]]), but that
is still a different product surface, not a Responses-API-level primitive.

## Why this matters for this wiki / `.ROOT`

- **This is not a gap `.ROOT` needs to close.** `.ROOT`'s forks are
  correctly modeled as bounded, independent workers reporting to one
  coordinator — the same "prefer one agent unless work is genuinely
  independent" judgment OpenAI states explicitly as guidance. Live
  mid-task agent-to-agent messaging has no current `.ROOT` need (every
  ingest wave in this session used independent, non-communicating forks by
  design, precisely because the chunks were genuinely separable).
- **The HTTP-vs-WebSocket blocking distinction is a transferable design
  principle** even without ever calling this API: a coordinator that waits
  for *all* parallel workers before processing *any* result (HTTP-style)
  is strictly worse than one that can act on each worker's result as it
  lands (WebSocket-style) — worth remembering if `.ROOT` or a future proof
  project ever builds its own multi-agent coordination layer instead of
  relying on this session's own fork-and-report pattern.
- **A fourth vendor-side confirmation that "start single-agent, prove the
  need, then go multi-agent" is the converged industry position** —
  matches [[openai-evals-and-red-teaming]]'s nondeterminism-ladder finding
  and CASTLE's own already-applied "traces/evals before multi-agent scale"
  launch-audit criterion. Not a new claim, but a third independent
  articulation of the same discipline, this time embedded directly in a
  product's own documentation rather than a best-practices essay.
- Companion pages: [[openai-agents-sdk-and-orchestration]] covers the
  SDK-level handoffs/agents-as-tools primitives this feature sits
  alongside; [[openai-webhooks-and-compaction]] covers the compaction
  mechanics this feature forces on.

---
*Processed July 12, 2026. Source in `raw/OPEN_AI-CHATGPT_CODEX_FILES/` (immutable).*
