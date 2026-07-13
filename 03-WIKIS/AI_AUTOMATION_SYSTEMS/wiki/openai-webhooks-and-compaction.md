---
type: research
tags: [ai-automation, openai, webhooks, compaction, context-management]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/OpenAI API 6.md, OpenAI API 7.md (title-collided captures of "Webhooks" and "Compaction" — https://developers.openai.com/api/docs/guides/webhooks and .../guides/compaction — two of 12 files that inherited the generic title "OpenAI API" during capture; identified and routed July 12, 2026)
---

# OpenAI Webhooks and Context Compaction

**Official OpenAI documentation, read in full July 12, 2026.** Two
unrelated but both previously-unrouted topics from the same title-collision
cleanup pass. Grouped here because both are standalone infrastructure
mechanics rather than agent-orchestration or tool topics covered elsewhere
in this wiki's OpenAI pages.

## One-paragraph summary

Webhooks are OpenAI's async-notification mechanism (batch/background-run/
fine-tuning-job completion events, Standard-Webhooks-spec compliant,
signature-verified, 72-hour retry with exponential backoff) — infrastructure
`.ROOT` has no current use for (no server endpoint exists in this system to
receive them). Compaction is materially more relevant: it is OpenAI's
answer to the same problem Claude Code's `/compact` solves (long
conversations exceeding usable context), but the *mechanism* is genuinely
different — OpenAI returns an opaque, non-human-readable encrypted
compaction item that must be passed through unmodified, where Claude's
`/compact` produces a human-readable summary re-injected as normal context.

## Webhooks

- **Delivery**: HTTP POST to a developer-controlled public URL, one
  endpoint per project, configured per event type in the OpenAI dashboard.
  Payload includes `webhook-id`, `webhook-timestamp`, `webhook-signature`
  headers plus a JSON body naming the event `type` and a `data.id`
  reference back to the resource (e.g. a `response.completed` event
  references the response ID — you then call the API to retrieve the full
  object, the webhook itself carries no payload beyond the pointer).
- **Reliability contract**: your endpoint must return `2xx` within a few
  seconds or OpenAI retries for up to 72 hours with exponential backoff;
  `3xx` redirects are treated as failures, not followed. Duplicate
  deliveries can happen ("rare... internal system issues") — use the
  `webhook-id` header as an idempotency key.
- **Verification**: `client.webhooks.unwrap(request.data, request.headers,
  secret=...)` is the official SDK helper; manual verification follows the
  open Standard Webhooks spec (portable across languages/libraries, not an
  OpenAI-proprietary signature scheme).
- **No current `.ROOT` use case** — `.ROOT` has no publicly-reachable
  server to receive webhook POSTs (it's a local C: vault, cloud-backed by
  Google Drive, not a hosted service). Recorded for completeness; revisit only if a future
  proof project stands up its own backend that calls the OpenAI API in
  background mode and needs completion notifications instead of polling.

## Context compaction — two modes, both opaque by design

**Server-side compaction** (automatic): set `context_management` with a
`compact_threshold` on a `/responses` call; when the rendered token count
crosses it mid-stream, the server runs compaction and emits an encrypted
compaction item in the same response stream before continuing inference.
No separate call needed. ZDR-friendly when paired with `store=false`.

**Standalone `/responses/compact` endpoint** (explicit/manual): send a full
context window (messages, tools, everything), get back a new, smaller
context window containing an encrypted compaction item plus some retained
prior items, to use as-is in the next `/responses` call. Fully stateless,
ZDR-friendly, but the window sent to it must still fit within the model's
context window first — compaction shrinks what you carry *forward*, it
doesn't rescue an already-overflowing request.

**The load-bearing rule, stated three times in the source with the same
emphasis**: the compaction item is **opaque and not intended to be
human-interpretable** — carries forward prior state and reasoning in
compressed form, but you cannot read or edit it, only pass it through.
Client-side pruning is explicitly restricted: with stateless input-array
chaining, you may drop items *before* the most recent compaction item
(the compaction item itself already carries what's needed); with
`previous_response_id` chaining, manual pruning is explicitly disallowed
("do not manually prune") since the server already tracks state via the ID.

## Direct comparison: OpenAI compaction vs. Claude Code `/compact`

| | OpenAI compaction | Claude Code `/compact` ([[claude-code-context-and-instruction-economics]]) |
|---|---|---|
| Trigger | Automatic (`compact_threshold`) or explicit endpoint call | User-invoked slash command, or automatic at context limits |
| Output form | Opaque encrypted blob, non-human-readable | Human-readable summary, visible in the transcript |
| What's preserved automatically | Compaction item only; everything else must be explicitly re-included | Project-root CLAUDE.md, auto memory, invoked skill bodies (capped, oldest dropped first) — all re-injected from disk automatically |
| What's lost | Everything not carried forward in the compacted window you construct | Path-scoped rules and nested CLAUDE.md files (reload only when a matching file is read again) |
| Editability | None — pass through unmodified | The summary is plain text; a user could in principle read and reason about what survived |
| Multi-agent interaction | Forced on implicitly when Multi-agent is enabled, applied per-agent independently (see [[openai-responses-multi-agent]]) | N/A — no built-in multi-agent primitive to interact with |

The opacity difference is the real finding: Claude's compaction is a
*visible* summary a user or the model itself can inspect and reason about
after the fact; OpenAI's is a black box you're contractually forbidden from
interpreting, closer to a database cursor than a conversation summary. Two
vendors solved "shrink a long conversation losslessly enough to continue"
with philosophically different transparency trade-offs, not just different
APIs for the same thing.

## Why this matters for this wiki / `.ROOT`

- **Webhooks: no action, correctly out of scope.** `.ROOT` has no server to
  receive them; recorded so a future session doesn't have to re-derive
  "does `.ROOT` need this" from scratch.
- **Compaction's opacity contrast is the one transferable insight.** If
  `.ROOT` or a future proof project ever integrates the OpenAI API for a
  long-running task, the inability to inspect what a compaction pass
  actually dropped is a real operational risk worth designing around
  (e.g., logging the pre-compaction window separately for debugging, since
  the compacted version can't be introspected after the fact) — a risk
  Claude Code's human-readable `/compact` summaries don't carry to the same
  degree.
- **This reinforces, not duplicates, the mid-session-edit finding** already
  documented in [[claude-code-context-and-instruction-economics]]: both
  vendors treat "what survives a context-reduction event" as a precise,
  documented mechanic worth knowing exactly rather than assuming — the
  specific mechanics differ, but the discipline of checking rather than
  guessing is the same lesson twice.

---
*Processed July 12, 2026. Source in `raw/OPEN_AI-CHATGPT_CODEX_FILES/` (immutable).*
