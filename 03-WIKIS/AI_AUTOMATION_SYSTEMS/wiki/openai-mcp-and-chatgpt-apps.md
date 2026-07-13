---
type: research
tags: [ai-automation, mcp, openai, chatgpt-apps, agent-builder]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ (OpenAI official docs, read in full July 12, 2026 — MCP and Connectors, Building MCP servers for ChatGPT Apps and API integrations, Secure MCP Tunnel, What makes a great ChatGPT app, ChatGPT Developer mode, ChatKit widgets, Actions in ChatKit, Advanced integrations with ChatKit, Theming and customization in ChatKit, Agent Builder, Migrate from Agent Builder, Migrate from prompt objects)
---

# OpenAI MCP Integration, ChatGPT Apps, and Agent Builder

**Official OpenAI documentation, read in full July 12, 2026.** This is OpenAI's
specific *product and implementation surface* around MCP — not the protocol
itself, which this wiki already covers in depth from the neutral spec in
[[mcp-landscape-architecture-and-patterns]], [[mcp-security-and-authorization]],
and [[mcp-client-primitives-and-build-notes]]. Where OpenAI's material assumes
protocol concepts (tools, resources, transports, approval flows), those pages
carry the depth; this page only adds what's OpenAI-specific.

## One-paragraph summary

OpenAI exposes MCP through the Responses API's `mcp` tool type in two flavors —
**connectors** (OpenAI-maintained wrappers for Dropbox, Gmail, Google
Calendar/Drive, MS Teams, Outlook Calendar/Email, SharePoint) and **remote MCP
servers** (any public server implementing the spec) — both gated by the same
`mcp_list_tools` → `mcp_call` → optional `mcp_approval_request`/`response` item
flow, with **Secure MCP Tunnel** as the answer for private/on-prem servers
(an outbound-only client that polls OpenAI for queued work — no equivalent
documented in Anthropic's MCP material read so far). Above the protocol layer,
**ChatGPT Apps** (formerly "connectors," renamed December 17, 2025) is a
product philosophy — apps are model-callable capabilities, not ported
products — built on **ChatKit**, OpenAI's full embeddable-chat-UI SDK with a
declarative widget tree. **Agent Builder**, the no-code visual workflow
canvas, is being deprecated (shuts down November 30, 2026), pushing users to
either the Agents SDK or ChatGPT Workspace Agents — the same date OpenAI is
also shutting down server-managed reusable **Prompt objects**, in both cases
pushing logic out of a managed UI/object and back into version-controlled code.

## MCP integration surface: connectors, remote servers, Secure MCP Tunnel

- **Two access paths, one tool shape.** Both connectors (`connector_id`, OAuth
  token in `authorization`) and remote MCP servers (`server_url`, optional
  OAuth) use the same `type: "mcp"` tool block in the Responses API. The
  `authorization` value is **never stored** by OpenAI — it must be resent on
  every Responses API call, not just the first.
- **Approval flow, explicit item types.** `mcp_list_tools` (imported tool
  definitions — kept in context across turns so the list isn't re-fetched
  every turn), `mcp_call` (arguments sent + output returned), and
  `mcp_approval_request`/`mcp_approval_response` (skippable per-tool or
  globally via `require_approval: "never"`). Structurally identical in shape
  to the protocol's own approval primitives — OpenAI's contribution here is
  making per-tool approval skip-lists a first-class API parameter rather than
  purely a client-UI decision.
- **`defer_loading: true`** on an MCP server tool definition is OpenAI's name
  for exactly the **progressive tool discovery** pattern already documented in
  [[mcp-landscape-architecture-and-patterns]] — the model sees the server's
  label/description and can search it, but individual tool schemas load only
  when needed. Two ecosystems (Anthropic's MCP client-best-practices docs and
  OpenAI's Responses API) independently converged on the same solution to the
  same context-cost problem — useful as a second confirmation when explaining
  this pattern's importance to a client.
- **Secure MCP Tunnel — the OpenAI-specific capability with no documented
  Anthropic equivalent.** `tunnel-client` runs inside a private network,
  long-polls an OpenAI-hosted tunnel endpoint over outbound-only HTTPS, and
  forwards MCP requests to a local server (stdio or HTTP) — no inbound
  firewall ports, no public exposure. Ships an embedded HTTP-callout proxy
  ("Harpoon") for narrowly-scoped REST access to a fixed target list. Worth
  noting for the agent-tool vetting screen (`TECHNOLOGY_LIBRARY_STRATEGY.md`
  Category 10) as an ecosystem-maturity data point: OpenAI ships an official
  private-network bridge product; the equivalent pattern on the Claude side
  (per the docs read so far) is left to third-party self-hosting.
- **Risk framing is nearly identical to the neutral MCP spec's threat catalog**
  already covered in [[mcp-security-and-authorization]] — prompt injection via
  untrusted MCP content, over-broad parameter requests, data exfiltration via
  read *and* write actions, connecting only to official/trusted servers. No
  new attack class; OpenAI's write-up is product-specific guidance layered on
  the same underlying risks.

## What makes a great ChatGPT app (design philosophy, not protocol)

The most reusable material in this batch, independent of any OpenAI-specific
mechanism — a **know / do / show** filter for whether an integration adds
real value:

- **Know**: makes new context available (live data, internal metrics,
  permissioned/user-specific data) that the base model can't see.
- **Do**: takes real actions on the user's behalf (create records, send
  messages, trigger workflows) — "less a source of truth, more a pair of
  hands."
- **Show**: presents information in a clearer, more actionable UI than plain
  text (comparisons, tables, structured summaries) — valuable specifically
  when users are making trade-off decisions.

Design process: **list jobs-to-be-done → ask "what can't the user do here
without this?" → name a handful of concrete operations** (`search_properties`,
`create_support_ticket`) rather than porting an entire product surface. Three
audiences to design for simultaneously: the human in the chat, the model
runtime deciding when to call the tool (clear names, unambiguous parameters,
predictable structured outputs, stable IDs), and data minimization (only
request fields actually needed; never "send the whole conversation").
Six-point pre-ship checklist: new powers, focused surface, graceful first
interaction (vague vs. specific intent), model-friendliness, an evaluation
set with a win-rate baseline, and ecosystem fit (small focused actions that
compose with *other* apps in the same conversation, not a walled garden).

## ChatGPT Developer mode — MCP client inside the ChatGPT UI itself

Full read/write MCP client support built into the ChatGPT product (Pro,
Plus, Business, Enterprise, Education), distinct from the API-level `mcp`
tool — this is an end-user-facing feature, enabled per-account via
**Settings → Security and login**. Two mechanics worth remembering if this
becomes relevant to a client engagement:

- **`readOnlyHint` tool annotation is respected** — any tool lacking it is
  treated as a write action requiring manual confirmation by default.
- **Disambiguation is a prompting problem, not just a config problem**: with
  multiple overlapping apps active, OpenAI's own guidance is to be explicit
  in the prompt itself ("use `Acme CRM`'s `update_record` tool... do not use
  built-in browsing or other tools") and to use the MCP `instructions` field
  (capped at a self-contained first 512 characters) for cross-tool,
  server-wide guidance — a smaller-scale version of the same
  disambiguation problem `.ROOT`'s own multi-skill, multi-MCP-server routing
  already has to solve.

## ChatKit — the embeddable chat UI framework

OpenAI's much heavier analogue to a single "Artifacts"-style output surface:
a full declarative widget component tree (`Card`, `Box`, `Row`, `Col`,
`Button`, `Form`, `Markdown`, `Select`, `DatePicker`, etc. — dozens of typed
props each) rendered server-side and streamed into a chat surface, plus an
`ActionConfig` system so widget interactions (button clicks, form submits)
trigger server- or client-side handlers without a full message round-trip.
Advanced/self-hosted mode runs a custom `ChatKitServer` (Python SDK) wired to
the Agents SDK, with your own thread/file storage. *(Security note added
July 12, 2026 from a title-collided intro capture)*: every ChatKit session
creation call requires a `user` parameter unique per end user — explicitly
the integrating backend's responsibility to authenticate and supply, not
something ChatKit derives on its own; skipping this is named as a real
misconfiguration risk, not just a data-quality nicety. Theming is a single
options object (color scheme, accent color, density, radius, starter
prompts, custom header buttons, @-mention entity tags, file-attachment
limits). This is genuinely more extensive than anything documented on the
Claude Code integration side — a full custom-UI product framework, not just
a chat wrapper — but it's infrastructure for building a *product*, and
`.ROOT` isn't building a customer-facing chat product, so it stays inventory.

## Agent Builder — deprecated visual workflow canvas

A drag-and-drop node-based canvas for multi-step agent workflows (design →
publish, versioned → deploy via ChatKit embed or downloaded Agents SDK code).
**OpenAI is shutting it down November 30, 2026** — the same deprecation date
as reusable Prompt objects (see below). Migration paths: export as Agents SDK
code (TypeScript/Python) to run yourself, or convert into a ChatGPT Workspace
Agent (Business/Enterprise/Edu only). Explicitly **not** a lossless
conversion — "does not convert your workflow graph or guarantee that every
behavior transfers unchanged," and workflows with strong internal determinism
are flagged as the hardest case to migrate faithfully. No `.ROOT` use case
(no visual-canvas workflow exists here), but the deprecation itself is a
useful landscape data point: a major vendor's no-code agent-builder product
had roughly a one-year lifecycle before being superseded by code-first
tooling — a data point for any future client conversation about whether to
invest in a no-code agent platform versus code.

## A second, independent confirmation: prompts belong in versioned code

OpenAI is also deprecating server-managed reusable **Prompt objects**
(`v1/prompts`, same November 30, 2026 shutdown) in favor of inlining prompt
text directly into application code. The stated reasoning: prompt changes
should "go through the same review and release process as product logic" —
git commits, PR review, evals in CI, static content first for prompt-caching
prefix stability. This is the same claim [[claude-code-integration-surface-and-platform]]
already surfaced from the CI/CD side (CLAUDE.md-as-steering-lever is
vendor-universal) — a second major vendor, from the opposite direction
(deprecating a *managed* alternative rather than recommending a convention),
arriving at the same conclusion: instructions/prompts as version-controlled
files beat instructions as an opaque managed object. Direct validation of
`.ROOT`'s own practice of keeping every instruction file (CLAUDE.md, AGENT.md,
skills, HATs) as a plain versioned file rather than any kind of managed
config object.

## Why this matters for this wiki / `.ROOT`

- **Secure MCP Tunnel is the one concrete ecosystem-maturity data point** worth
  carrying into the Category 10 vetting screen — an official private-network
  bridge is a real capability gap between "OpenAI's MCP story" and "Anthropic's
  MCP story" as documented so far, not just a branding difference.
- **`defer_loading` and progressive tool discovery converging independently**
  strengthens (doesn't just repeat) the case already made in
  [[mcp-landscape-architecture-and-patterns]] for treating deferred/on-demand
  tool loading as a load-bearing pattern, not a vendor quirk.
- **The know/do/show filter and the six-point ChatGPT-app checklist are
  reusable now**, independent of any OpenAI mechanism — directly usable
  vocabulary for a `05-BUSINESS` client conversation about whether a proposed
  AI integration ("should we build a ChatGPT app / Claude MCP server for
  this?") actually adds value, or is just porting an existing product badly.
  Same underlying question as the agentic-AI-industry adoption barriers this
  wiki already tracks in [[agentic-ai-industry-adoption-barriers]].
- **The Prompt-objects deprecation is a second independent vendor validation**
  that `.ROOT`'s prompts-as-versioned-files practice is the industry-converged
  answer, not an idiosyncratic choice — worth remembering the next time a
  "should this become a managed/hosted config instead of a file" question
  comes up for any `.ROOT` skill or HAT.
- **ChatKit and Agent Builder stay inventory** — no current `.ROOT` use case
  (not building a customer product chat surface, no visual-canvas workflow),
  recorded honestly rather than forced into relevance, matching how
  [[claude-code-integration-surface-and-platform]] handled its own
  no-current-use-case material.

---
*Processed July 12, 2026. Source in raw/ (immutable).*
