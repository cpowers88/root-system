---
type: research
tags: [ai-automation, openai, gpt-actions, api-integration, function-calling]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ (OpenAI official docs, read in full July 12, 2026 — GPT Actions, GPT Actions library, GPT Action authentication, Data retrieval with GPT Actions, Sending and returning files with GPT Actions, Production notes on GPT Actions, AI app development: Concept to production)
---

# OpenAI GPT Actions — Custom GPT API Integration Surface

**Official OpenAI documentation, read in full July 12, 2026.** GPT Actions
predate and sit alongside the MCP-based ChatGPT Apps/Connectors covered in
[[openai-mcp-and-chatgpt-apps]] — a second, older, schema-driven way OpenAI
lets ChatGPT call external REST APIs, scoped to **Custom GPTs** specifically
rather than the Responses API generally. No current `.ROOT` use case (no
Custom GPT, no REST API to expose), recorded as landscape/inventory, with one
piece of directly reusable API-design guidance pulled out below.

## One-paragraph summary

A GPT Action is an OpenAPI schema attached to a Custom GPT; function calling
decides which endpoint is relevant to the user's question, generates the
JSON input, and executes the call — the developer's job is just describing
the API surface and its authentication (none / API key / OAuth), not writing
translation logic. Three retrieval patterns are documented (direct REST API,
relational database via required middleware, vector database via required
middleware plus query-embedding conversion), each with a real constraint:
relational and vector databases aren't natively REST-exposed or
internet-reachable, so a middleware layer is mandatory, and vector-chunk
retrieval loses the source document's original access permissions unless the
middleware re-implements them. Production guidance converges on the same
principle already seen twice elsewhere in this pack: **gate write/destructive
actions behind explicit confirmation, let reads flow freely** — here
implemented as the `x-openai-isConsequential` OpenAPI extension.

## How GPT Actions work, and the library pattern

- **Mechanism**: standard function calling — decide relevant endpoint → build
  JSON input → execute the API call — with authentication (API key or OAuth)
  handled by the platform so the end user never sees the API layer, only
  natural-language in and out.
- **GPT Actions library** is a curated cookbook (OpenAI Cookbook) of
  pre-built integrations for common 3rd-party apps, split into **direct**
  (SaaS APIs called straight, e.g. Google Drive, Snowflake) and **middleware**
  (Azure/GCP/AWS functions sitting between the GPT and an endpoint not
  natively HTTP-exposed, e.g. a database) patterns — community-contributed
  via a documented PR template (app info, exact Custom GPT instructions,
  exact OpenAPI schema, exact auth setup, FAQ/troubleshooting). Explicitly
  **not guaranteed to keep working** — 3rd-party APIs change outside OpenAI's
  control.

## Authentication — three schemes, one deliberate UX tradeoff

- **None**: recommended for *first* interactions specifically to avoid
  sign-in drop-off — start unauthenticated, then move the user into a
  separate authenticated action once they're engaged.
- **API key**: encrypted at rest; useful when actions are more consequential
  than "none" but don't need per-user identity.
  - **OAuth**: full per-user flow — client ID/secret, authorization/token
  URLs, scope, mandatory `state` parameter for CSRF protection, refresh-token
  support, fixed callback URL pattern
  (`https://chatgpt.com/aip/{g-YOUR-GPT-ID}/oauth/callback`). Every
  subsequent action call carries the user's token in the `Authorization`
  header — same "resend every call, nothing cached server-side" posture as
  the MCP `authorization` field in [[openai-mcp-and-chatgpt-apps]].

## Data retrieval — three patterns, and a real permission-loss risk

1. **API retrieval** (Salesforce, Zendesk, Confluence, Google Drive, etc.):
   confirm the provider's search + get methods and auth scheme; import an
   existing OpenAPI spec where the provider supplies one, trimming
   unused-endpoint clutter to constrain what the GPT can actually call.
2. **Relational database retrieval**: databases aren't REST-native or
   internet-reachable by default, so a middleware layer is required to
   accept a query string, run it, and return records. Explicit
   recommendation: **read-only service-account credentials**, since end
   users won't have (and shouldn't be given) direct database access.
3. **Vector database retrieval**: same middleware requirement, plus the
   middleware must also convert plaintext queries into embeddings before
   querying. **The permission-loss risk is worth remembering past this
   specific doc**: vector databases store de-contextualized text chunks, so
   whatever document-level access controls existed on the original source
   material typically don't carry over — "any user who can access your GPT
   will have access to all of the text chunks in the database" unless the
   middleware explicitly re-implements per-user filtering. Directly relevant
   audit vocabulary alongside the MCP security material already in
   [[mcp-security-and-authorization]] for any future client RAG conversation.

## Sending and returning files — concrete limits worth having on hand

- **Sending**: up to 10 files per request via `openaiFileIdRefs` (name, id,
  mime_type, a download link valid for **5 minutes only**) — covers
  user-uploaded files, DALL-E images, and Code Interpreter outputs.
- **Returning**: up to 10 files, **10 MB each, no images or video**, via
  `openaiFileResponse` — either inline base64 content or a URL (with
  required `Content-Disposition`/`Content-Type` headers, 10-second fetch
  timeout). Returned files re-enter the conversation exactly like a
  user upload — available to Code Interpreter, file search, and later
  action calls.

## Production constraints and the consequential-action pattern

- **Hard limits**: 45-second round-trip timeout, TLS 1.2+ on port 443 with a
  valid public cert, 100,000-character payload cap each direction,
  text-only payloads (no images/video in the request/response body itself —
  only via the file mechanisms above), **custom headers not supported**,
  300/700-character caps on OpenAPI endpoint/parameter descriptions.
  ChatGPT respects `429`/`500` and backs off automatically — implement your
  own rate limiting, it will be honored.
- **`x-openai-isConsequential`** — a third independent occurrence, in this
  pack alone, of the same underlying pattern: gate write/destructive actions
  behind explicit confirmation, let reads flow freely. Same shape as
  Claude Code's permission modes ([[claude-code-permissions-security-and-review]])
  and the MCP `require_approval` flow in [[openai-mcp-and-chatgpt-apps]]. If
  unset, GET defaults to `false` (auto-allow available) and everything else
  defaults to `true` (must always confirm, no "always allow" button) — a
  sane, security-conscious default that mirrors the read/write split this
  wiki's own agent-tool vetting screen already treats as load-bearing.
- **API-response design guidance directly reusable regardless of platform**:
  return raw structured data (`{"todos": ["get groceries", "walk the dog"]}`),
  not a pre-written natural-language sentence — let the model compose the
  reply from data. This is the same principle as MCP's `structuredContent` +
  JSON-string `content` pattern in [[openai-mcp-and-chatgpt-apps]]'s "Building
  MCP servers" section: **structured data in, let the model narrate out** is
  now confirmed across two different OpenAI integration surfaces, not just one.
  Also: don't write action descriptions that prescribe a conversational
  script ("say yes to continue") — describe *what the action does*, not
  *when to trigger it*; the model handles triggering.

## Brief note: "AI app development: Concept to production"

A learning-track landing page (four phases: foundations → hands-on → evals/
guardrails → cost/latency optimization), not a technical reference — mostly
links out to deeper tracks (Building Agents, evals, RAG, fine-tuning) already
covered elsewhere in this docs pack or out of scope for this ingest. Recorded
for completeness; nothing durable to extract beyond its four-phase framing,
which is a reasonable one-line mental model for "what production-readiness
means" if this wiki ever needs to explain that arc to a client.

## Why this matters for this wiki / `.ROOT`

- **No current `.ROOT` use case** — no Custom GPT, no REST API to expose —
  recorded honestly as inventory, matching how this pack's other
  no-current-use-case material was handled.
- **The consequential-action pattern is now confirmed three times** across
  this ingest alone (Claude Code permission modes, MCP approval flow, GPT
  Actions' `x-openai-isConsequential`) — strong, vendor-independent evidence
  that "reads free, writes/destructive actions gated" is the converged
  industry default, useful as citable vetting-screen vocabulary for
  `TECHNOLOGY_LIBRARY_STRATEGY.md` Category 10.
- **The structured-data-in / narration-out principle** is immediately
  reusable the next time this wiki or a Capability Library asset designs any
  tool/action interface, regardless of platform.
- **The vector-DB permission-loss risk** is a concrete, non-obvious audit
  point worth remembering if a `05-BUSINESS` client engagement ever proposes
  a RAG/vector-search integration — access control has to be re-implemented
  explicitly, it does not carry over from the source system by default.

---
*Processed July 12, 2026. Source in raw/ (immutable).*
