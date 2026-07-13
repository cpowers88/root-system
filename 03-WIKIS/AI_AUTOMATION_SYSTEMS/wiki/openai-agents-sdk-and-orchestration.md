---
type: research
tags: [ai-automation, openai, agents-sdk, orchestration, guardrails, multi-agent]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ (OpenAI official API docs, relocated from CASTLE raw/ to this wiki July 12, 2026 — Agents SDK, Agent definitions, Running agents, Orchestration and handoffs, Guardrails and human review, Safety in building agents, Integrations and observability. Confirmed duplicate: "Agents SDK  OpenAI API 1.md" is byte-identical to "Agents SDK  OpenAI API.md", SHA-256 0ddb73d5...92db1 — read once, not double-summarized)
---

# OpenAI Agents SDK — Orchestration, Guardrails, and the Claude Code Contrast

**Official OpenAI API documentation, read in full July 12, 2026.** Covers the
agent-definition and multi-agent orchestration layer that sits above the
tool mechanics in [[openai-tools-and-function-calling]]. Where that page
found two independent re-inventions of MCP/Claude Code patterns, this page's
comparison runs the other way: OpenAI's orchestration model (handoffs,
agents-as-tools, resumable approval state) is architecturally **richer**
than anything in Claude Code's subagent model documented in
[[claude-code-workflows-and-sessions]] — genuinely different, not just
differently named.

## One-paragraph summary

The Agents SDK is a runner that owns the agent loop (call model → execute
tool calls → follow handoffs → stop) so applications don't hand-roll it
themselves — the explicit alternative is the Responses API, where you own
that loop yourself. Its two orchestration primitives, **handoffs**
(full ownership transfer to a specialist) and **agents-as-tools** (a manager
stays in control and calls specialists as bounded capabilities), map onto
exactly the two collaboration shapes Claude Code's docs describe as absent
from its own subagent model — Claude Code subagents only report back to a
single caller, one-way, with no equivalent to "hand off full ownership of
the reply." Layered on top: a **first-class resumable-approval state
machine** for human review that treats a paused run as the same run, not a
new turn — more developed than Claude Code's per-action permission-mode
prompts.

## Agents SDK vs. Responses API — the explicit fork

OpenAI states this choice plainly rather than leaving it implicit:

| | Responses API | Agents SDK |
|---|---|---|
| You own | The loop, tool routing, branching | Nothing — the SDK runs the loop |
| Multi-agent | Build routing/delegation yourself | Built-in handoffs + agents-as-tools |
| Safety | Tool-specific approvals only | Input/output/tool guardrails + resumable approval flows |
| Debugging | Response objects, API logs | Built-in tracing across model calls, tools, agents, guardrails, handoffs |

This is a cleaner articulation of a choice `.ROOT` implicitly already made:
Claude Code's subagent/hook/fork model is closer to "own your own loop with
SDK-provided primitives" than to a fully managed agent runner — worth
knowing the vocabulary if a future proof project ever needs to explain why
it chose one architecture over the other.

## Agent definition — what belongs where

An agent packages `name`, `instructions`, `model`, `tools`, `outputType`
(structured output instead of free text), `handoffs`, and guardrails. The
one design rule worth carrying elsewhere: **local context vs. model
context is an explicit, named boundary** — `RunContext` passes application
state (auth info, DB clients, loggers) into tool execution *without* it
ever entering the model's conversation history. "If the model needs a fact,
put it in instructions/input/retrieval/a tool. If only your runtime needs
it, keep it in local context." Claude Code has no named equivalent to this
split; it's a useful naming convention even without adopting the SDK.

**When to split one agent into several** — stated as a discipline, not a
default: only when a specialist needs a different tool/MCP surface,
different approval policy, different model/output style, or explicit
routing visibility in traces. "Splitting too early creates more prompts,
more traces, and more approval surfaces without necessarily making the
workflow better" — the same anti-sprawl instinct this wiki's own charter
already states for skill/HAT creation, independently confirmed.

## Orchestration — handoffs vs. agents-as-tools

| Pattern | Who owns the final reply | Use when |
|---|---|---|
| **Handoff** | The specialist, after control transfers | A branch of work should be owned end-to-end by one specialist |
| **Agents as tools** (`agent.asTool()`) | The manager, always | The specialist does one bounded task (summarize, classify) and the manager synthesizes |

Neither has a clean Claude Code equivalent. A Claude Code subagent is
closest to "agents as tools" (reports back, caller stays in control) — but
Claude Code has **no handoff primitive**: nothing transfers full
conversation ownership to a subagent the way an OpenAI handoff does.
[[claude-code-workflows-and-sessions]] separately notes Claude Code's
experimental "agent teams" (peer-messaging, shared task list, disabled by
default) as the nearest adjacent idea, but that's peer coordination, not
ownership transfer — a third shape, not the same as either OpenAI pattern.

## Running agents — conversation-state strategies

Four explicit strategies, chosen once per conversation rather than mixed:
`result.history` (your app replays it — max control, small chats),
`session` (SDK + your storage — the default recommendation for durable/
resumable state), `conversationId` (OpenAI-hosted, shared across workers),
`previousResponseId` (lightest-weight, single-response continuation). The
guidance to **pick one and not mix local replay with server-managed
state** "unless deliberately reconciling both layers" is a clean warning
against exactly the kind of dual-source-of-truth bug that's easy to
introduce accidentally — relevant vocabulary if `.ROOT` or a proof project
ever builds a stateful agent loop of its own.

**Approvals are paused runs, not new turns** — a deliberate design choice
stated explicitly: resuming from `state` after a human approval keeps turn
counts, history, and continuation IDs consistent. Serialize `state`, store
it, resume whenever the decision arrives, even much later. This is a more
formal treatment of "wait for user confirmation" than anything in Claude
Code's permission-mode docs, which handle approval as an inline prompt, not
a resumable, storable, potentially-delayed-by-days state object.

## Guardrails and human review — three checkpoints, one lifecycle

| Guardrail type | Runs | Scope |
|---|---|---|
| Input | Before the main agent starts | Only the first agent in the chain |
| Output | Before the final reply leaves | Only the agent producing final output |
| Tool | Around a specific function call | Only the tool it's attached to |

**Explicit boundary warning**: agent-level input/output guardrails do *not*
automatically cover every tool call in a manager-style (agents-as-tools)
workflow — validation has to sit next to the tool that creates the side
effect, not just at the edges. A concrete failure mode worth remembering
for any multi-tool `.ROOT` automation: guardrails at the conversation
boundary don't substitute for checks at each side-effecting action.

**Approval lifecycle** (four steps, always the same): run pauses and
records an "interruption" instead of executing → result returns
`interruptions` + resumable `state` → application approves/rejects → resume
from `state`, not a new turn. `needsApproval: true` on a tool definition is
the trigger — declarative, attached to the tool itself rather than decided
ad hoc by the calling code.

## Safety in building agents — prompt injection specifically

Agent Builder itself is being deprecated (shutdown November 30, 2026,
ChatKit stays) but its safety guidance is general-purpose, not tool-specific:

- **Never put untrusted variables in developer/system-level messages** —
  they take precedence over user/assistant messages, so injecting untrusted
  text there gives an attacker the *most* control available. Route
  untrusted input through user messages instead, which the model treats
  with appropriately lower trust.
- **Structured outputs as an injection defense**, not just a data-quality
  tool — enums and fixed schemas between workflow nodes eliminate the
  freeform text channel an injection needs to smuggle instructions through.
- **Keep tool approvals on for MCP** specifically — "always enable tool
  approvals so end users can review and confirm every operation, including
  reads" — reads, not just writes, which is a stricter default than
  intuition suggests and stricter than `.ROOT`'s own posture (read-only
  tools are unrestricted in Manual mode per
  [[claude-code-permissions-security-and-review]]). Worth noting as a
  contrast, not necessarily a gap — `.ROOT`'s MCP connections (Gmail,
  Drive, Notion, etc.) are Chris's own authenticated services, not
  arbitrary third-party servers, which changes the threat model this
  guidance assumes.
- **Private data leakage is named as distinct from injection** — a model
  can over-share with a connected MCP server with no attacker involved at
  all, just imprecise judgment about what context to include in a call.

## Integrations and observability — MCP wiring and tracing

Two MCP paths mirror the hosted-vs-local split already familiar from
[[mcp-landscape-architecture-and-patterns]]: hosted MCP tools (model calls
a public remote server directly) vs. SDK-managed local/private MCP servers
(your runtime owns the connection, approvals, network boundary) — same
architecture, OpenAI's naming. **Tracing is on by default** in the
server-side SDK path, capturing every model call, tool call, handoff, and
guardrail into a dashboard — a stronger default than anything `.ROOT`
currently has for its own fork/subagent runs, which rely on the coordinator
reading each fork's final report rather than a structured, replayable trace
of the fork's internal tool calls.

## Why this matters for this wiki / `.ROOT`

- **Handoffs are a genuine capability gap worth naming, not closing.**
  `.ROOT`'s fork-heavy research pattern (used constantly in this wiki) is
  correctly modeled as "agents as tools," never needs "handoffs" — every
  fork reports back to one coordinator, nothing needs full ownership
  transfer mid-task. This is confirmation the current pattern is the right
  one for `.ROOT`'s actual workload, not evidence of a missing feature.
- **The resumable-approval-as-paused-run model is worth borrowing as
  vocabulary**, even without the SDK: `.ROOT`'s own risky-action
  confirmation flow (this session's own operating instructions) is
  currently a same-turn prompt, with no notion of "pause, store, resume
  later" for a decision Chris wants to sit with. Not a gap that needs
  fixing — `.ROOT` sessions are short-lived by design — but a concept worth
  having language for if a long-running automation ever needs it.
- **The local-context-vs-model-context naming** (`RunContext`) is a useful
  distinction to borrow in prose even without the SDK: when a CASTLE or
  wiki session is deciding whether a fact belongs in a fork's prompt
  (model context) vs. just something the coordinator tracks itself
  (local/run context), this is the exact question, now named.
- **"Splitting too early" as a stated discipline** independently confirms
  this wiki's own anti-sprawl instinct for skills/HATs/proposals — external
  validation, no change needed.
- Companion page: [[openai-tools-and-function-calling]] covers the tool
  mechanics (function calling, tool search, sandboxes) these agents call.
  [[openai-responses-multi-agent]] (added July 12, 2026 from a
  title-collided capture) covers a third, distinct orchestration
  primitive — model-initiated multi-agent trees built into the Responses
  API itself, separate from this SDK's handoffs/agents-as-tools.

---
*Processed July 12, 2026. Source in `raw/OPEN_AI-CHATGPT_CODEX_FILES/` (immutable).*
