---
type: research
timeline: reference
tags: [ai-automation, openai, tool-calling, agents, context-management]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ (OpenAI official API docs, relocated from CASTLE raw/ to this wiki July 12, 2026 — Using tools, Function calling, Tool search, Programmatic Tool Calling, Code Interpreter, Code generation, Apply Patch, Local shell, Computer use, File search, Web search, Citation Formatting, Sandbox Agents; plus three title-collided captures added July 12, 2026 — Agent Skills, Shell tool, Retrieval/vector stores)
---

# OpenAI Tools and Function Calling — Mechanics and Claude Code Contrasts

**Official OpenAI API documentation, read in full July 12, 2026.** CASTLE's
earlier pass (`00-BRAIN\CASTLE\wiki\source-summaries\openai-platform-docs-pack-2026-07.md`)
covered this material at inventory depth only ("tool schemas, structured
outputs, retrieval, safe execution" as a claim family, not the mechanics).
This page goes to mechanic depth and, where genuinely useful, contrasts
OpenAI's tool architecture against Claude Code's (already documented in
[[claude-code-workflows-and-sessions]] and [[mcp-landscape-architecture-and-patterns]]).

## One-paragraph summary

OpenAI's tool surface splits into hosted tools (web search, file search, code
interpreter, image generation — OpenAI runs them), function/custom tools
(your code, model just requests the call), and orchestration primitives that
sit on top of both (tool search for deferred loading, Programmatic Tool
Calling for code-composed multi-tool sequences, apply_patch for structured
file diffs). Two of these primitives are **independent re-inventions of
patterns already documented in this wiki from the Claude Code/MCP side**:
`tool_search` is the same deferred-loading idea as MCP's progressive tool
discovery, and Programmatic Tool Calling is functionally identical to the
MCP ecosystem's "code mode" — different vendors, same architectural answer to
the same context-cost problem, which is a stronger validation of that pattern
than either source alone.

## Function calling — the core loop

Five-step loop: request with tools → model returns a `function_call` item
(`call_id`, `name`, JSON `arguments`) → your code executes it → you return a
`function_call_output` keyed to `call_id` → model gives a final answer or
calls again. Best practices worth carrying into any tool-definition work:

- **Keep initial functions under ~20** for accuracy; use `tool_search` to
  defer the rest — a stated numeric threshold, more concrete than MCP's
  "1–5% of context window" guidance for the same problem.
- **Namespaces** group related tools (`crm`, `billing`) so the model can
  reason about a domain before drilling into individual functions —
  structurally the same idea as an MCP server boundary, but expressed as an
  in-request grouping object rather than a separate connection.
- **Offload what code already knows** — don't make the model re-supply an
  `order_id` it already gave you in a prior step; fold sequential calls that
  always run together into one function.
- **Strict mode** (`strict: true`) enforces the JSON schema exactly via
  structured outputs — recommended as the default, not an edge case.
- Token accounting is explicit: function definitions are billed as input
  tokens every request, which is *why* tool_search and namespace deferral
  exist — the same cost pressure MCP's client-scaling patterns describe.

## Tool search — deferred loading as a first-class API type

Where MCP/Claude Code describe progressive tool discovery as a *recommended
implementation pattern* (build your own `search_tools` meta-tool), OpenAI
ships it as a **typed API primitive**: add `{"type": "tool_search"}` to
`tools`, mark deferred functions/namespaces/MCP servers with
`defer_loading: true`, and the model emits `tool_search_call` /
`tool_search_output` items to load what it needs mid-conversation.

- **Hosted mode**: OpenAI searches your declared tool inventory and returns
  the loaded subset in the same response (`execution: "server"`).
- **Client-executed mode**: the model asks your application to search
  (`execution: "client"`), useful when tool availability depends on
  tenant/project state the request can't declare up front.
- **Cache-preserving by design**: newly loaded tools are always injected at
  the *end* of the context window, specifically so the prefix cache survives
  — the same prompt-caching-vs-tool-loading tension [[claude-code-context-and-instruction-economics]]
  documents for Claude Code (adding/removing tools mid-conversation
  invalidates the cache there too).
- Only `gpt-5.4`+ models support it — a recency/version constraint to
  recheck before relying on it, per this pack's own recheck rules.

## Programmatic Tool Calling — "code mode," confirmed independently

The model writes JavaScript that orchestrates tool calls — runs in a fresh,
isolated V8 runtime with **no** Node.js, filesystem, network, or persistent
state between executions; it can only call tools explicitly marked
`allowed_callers: ["programmatic"]` and emit output via `text()`/`image()`.
This is the *same* pattern [[mcp-landscape-architecture-and-patterns]]
described as "code mode" (~100K+ tokens of intermediate results collapsed to
a short script and answer) — now confirmed as a named, documented, built-in
OpenAI primitive rather than an MCP-ecosystem-only idea.

- **Decision table, not a default**: OpenAI's own guidance is explicit that
  Programmatic Tool Calling is for *predictable control flow* stages (filter/
  join/rank/aggregate over several results, or dependent calls with known
  data flow) — direct tool calling stays the right choice for adaptive
  search, approval-sensitive writes, and citation/artifact validation. This
  routing table is a reusable heuristic independent of vendor.
- Supported callers: `function`/`custom`, `mcp`, `apply_patch`, `shell`,
  `code_interpreter` — i.e., nearly every other tool type in this page can be
  called *from inside* a program.

## Apply Patch — structured diffs as a first-class tool type

`apply_patch` makes file edits an explicit API contract instead of prose the
harness has to parse: the model emits `apply_patch_call` items
(`create_file`/`update_file`/`delete_file`, V4A diff format), your harness
applies them and returns `apply_patch_call_output` with a `status`. Contrast
with Claude Code, where Edit/Write are local tool calls with no equivalent
wire-level diff contract — OpenAI's version is meant to be portable across
harnesses (a reference Python/TypeScript diff-apply implementation ships in
the Agents SDK repos). Safety practices named: path validation against
directory traversal, backups/scratch-copy before applying, explicit
all-or-nothing vs. per-file failure semantics.

## Code Interpreter and Sandbox Agents — two different container models

- **Code Interpreter**: a single hosted Python sandbox per conversation,
  memory-tiered (1g/4g/16g/64g), **auto-expires after 20 minutes idle** with
  no recovery — explicitly "treat as ephemeral, download what you need."
  Files the model creates are cited via `container_file_citation`
  annotations on the next message.
- **Sandbox Agents** (beta, Agents SDK only): a much heavier construct — a
  full Unix-like workspace (`Manifest` for starting files/repos/mounts),
  swappable providers (Docker, E2B, Modal, Cloudflare, Vercel, Runloop,
  Daytona, Blaxel, or local Unix), resumable sessions, and **its own memory
  system** distinct from conversation history: `memory_summary.md` injected
  at run start, `MEMORY.md` searched on demand, per-run raw memories and
  rollout summaries opened only when needed. This is the **third**
  independent implementation of the same index-plus-detail-files memory
  shape this wiki has now seen — Claude Code's native auto memory
  ([[claude-code-context-and-instruction-economics]]) and `.ROOT`'s own
  hand-built `memory/` system being the other two. Three vendors converging
  on the same shape is a stronger signal than either prior instance alone.
- The harness-vs-compute boundary Sandbox Agents draws explicitly (control
  plane owns auth/approvals/tracing; sandbox owns only execution) is a clean
  articulation of a design principle `.ROOT`'s own permission hardening
  already follows implicitly (deny rules and session logic outside any one
  "workspace," raw/ immutability enforced at the settings layer, not in
  conversation).

## Computer use — a sharper consent taxonomy than Claude Code's permission modes

Three harness shapes (built-in click/type/scroll loop, wrap an existing
Playwright/Selenium/VNC harness as a tool, or a code-execution harness that
mixes visual and DOM interaction) sit under one genuinely reusable framework:
a **three-tier action-risk taxonomy**, more granular than anything in
[[claude-code-permissions-security-and-review]]'s six permission modes:

| Tier | Examples | Rule |
|---|---|---|
| **Hand-off required** | final password-change step, bypassing an HTTPS/paywall warning | Human must physically take over |
| **Always confirm at action time** | deleting data, changing permissions, financial transactions, installing software | Ask immediately before, even mid-task |
| **Pre-approval can be enough** | logging into a site the user named, accepting a browser permission prompt, uploading a file | One earlier "yes" covers it, if the user's own prompt was specific |

Paired with an explicit **user-vs-third-party-content boundary**: only
direct user-authored instructions count as permission; on-screen text,
pasted documents, emails, and tool outputs are untrusted by default *even if
they claim urgency or claim to override policy* — stop and ask if content
looks like injected instructions. This is the same prompt-injection posture
Claude Code's own docs take, but OpenAI's version names the three
confirmation tiers explicitly where Claude Code's permission-mode table
stays coarser (six modes, not tied to action-risk category).

## Agent Skills — OpenAI's skill system, compared to Claude Code Skills

*(Added July 12, 2026 from a title-collided capture — `tools-skills`, not
in the original reading chunk.)* Versioned bundles of files plus a
`SKILL.md` manifest (frontmatter + instructions), explicitly built to the
**open Agent Skills standard** (agentskills.io) — the same spec Claude Code
Skills also implement, making this a genuine cross-vendor-compatible
format, not just a parallel invention. Mechanics: upload a directory or zip
(50MB cap, 500 files/version, 25MB uncompressed file max), attach via
`tools[].environment.skills` to the shell tool (hosted or local), and the
model sees each skill's `name`/`description`/`path` injected into **user
prompt context** (not system-level) so it can decide when to invoke one —
explicit-instruction override ("use the `<skill name>` skill") still works
for deterministic control. Versioning is real: `default_version`,
`latest_version`, per-reference version pins, additive-only updates.

**Contrast with Claude Code Skills**: OpenAI skills are always attached to
a shell execution environment (hosted container or local runtime) — a
skill *is* a bundle of code plus instructions meant to run. Claude Code
skills (documented in [[claude-code-workflows-and-sessions]]) are more
general — reference material or a workflow, not necessarily bound to code
execution. Both share the same core security posture stated almost
identically: **treat any skill as privileged, potentially-untrusted input**
until reviewed, never expose an open skill catalog to end-users directly,
gate write/high-impact actions behind explicit approval. The shared open
standard means a skill bundle following the spec could plausibly be
portable between the two ecosystems — worth testing if `.ROOT` ever needs
a skill to run identically under both Claude Code and an OpenAI-API-backed
tool.

## Shell tool — hosted and local execution (fills a gap this page previously flagged)

*(Added July 12, 2026 — the original reading chunk covered "Local shell"
as deprecated and explicitly flagged the replacement `shell` tool as
unread; this section closes that gap.)* The `shell` tool gives models a
full terminal, in two modes:

- **Hosted shell**: OpenAI-managed containers (`container_auto` to
  provision per-request, or create-once-and-reuse via `container_reference`
  for iterative multi-turn work). Debian 12 runtime, preinstalled Python
  3.11/Node 22.16/Java 17/PHP 8.2/Ruby 3.1/Go 1.23, default working
  directory `/mnt/data`, no `sudo`, no interactive TTY, **20-minute idle
  auto-expiry with no recovery** (same ephemeral posture as Code
  Interpreter, already noted above). Skills attach the same way as the
  shell tool generally (see above).
- **Local shell**: you execute `shell_call` actions yourself and return
  `shell_call_output` — full control over environment/filesystem, the mode
  Codex-style CLI agents use. Explicitly documented Agents SDK integration
  point (`needsApproval: true` + an `onApproval` callback) for gating local
  command execution behind human review.
- **Network access is opt-in and double-gated**: hosted containers have no
  outbound network by default; enabling it requires both an org-level admin
  allowlist *and* a request-level `network_policy` naming a subset of that
  allowlist — a request fails outright if it asks for domains outside the
  org list. **`domain_secrets`** let a container call an authenticated
  third-party API without the model or runtime ever seeing the raw
  credential — only a placeholder name (`$API_KEY`) is visible in
  model-context; a server-side "auth-translation sidecar" substitutes the
  real value only for the approved destination. This is a sharper
  credential-isolation pattern than anything else read in this pack —
  worth remembering as a reference design if `.ROOT` or a proof project
  ever needs an agent to call an authenticated API without the credential
  ever entering model-visible context.
- **Risks named explicitly, matching this page's existing prompt-injection
  posture**: any externally-fetched content is untrusted by default and
  may carry hidden instructions; only allowlist domains you actively trust
  and maintain; log and periodically review actual outbound destinations
  against expected ones to catch drift.

## File search, web search, citation formatting — retrieval and grounding

- **File search / Retrieval API — the actual mechanics** *(expanded July
  12, 2026 from a title-collided "Retrieval" capture; the original chunk
  only had the tool-level summary below this line)*: File search is built
  on the **Retrieval API**'s semantic search over **vector stores**. A
  vector store auto-chunks, embeds, and indexes uploaded files (default
  `800` tokens/chunk, `400`-token overlap, tunable within `100–4096` and
  `≤ half of chunk size` respectively; 512MB/5M-token-per-file limits;
  first 1GB storage free, then $0.10/GB/day). `client.vector_stores.search()`
  returns up to 50 results (10 default) with per-chunk similarity scores,
  file provenance, and up to 16 filterable `attributes` per file (256-char
  values). **Query rewriting** (`rewrite_query=true`) automatically
  reformulates a conversational question into a denser search query before
  embedding — OpenAI's own example: "I'd like to know the height of the
  main office building" → "primary office building height." **Hybrid
  search** blends semantic (embedding) and keyword (sparse) matching via
  reciprocal rank fusion, with independently tunable weights — useful when
  a corpus has exact-match-critical terms (product SKUs, legal citations)
  that pure semantic similarity would under-rank. Batch ingestion (up to
  500 files/request) is the recommended path for bulk uploads over
  many single-file calls. This is the retrieval layer any future
  `.ROOT`-adjacent RAG build (a client audit knowledge base, for instance)
  would actually be built on — the tool-level "File search" summary below
  was the interface; this is what's underneath it.
- **File search (tool interface)**: hosted semantic+keyword search over
  uploaded vector stores, with `max_num_results` and metadata `filters` for
  cost/precision tradeoffs — conceptually the retrieval half of what MCP
  resources do, minus the protocol-level host/client separation.
- **Web search**: three modes by cost/depth — non-reasoning (fast lookup),
  agentic-with-reasoning (searches as part of chain-of-thought), and deep
  research (`high`/`xhigh` reasoning, background mode, can run minutes,
  hundreds of sources). `sources` returns the full URL list consulted, wider
  than the inline citations shown — a useful distinction for any audit trail
  a client engagement might need to produce.
- **Citation Formatting**: a genuinely reusable framework independent of any
  specific tool — choose a **citable unit** (document / block / line-range,
  block-level as the recommended default), represent it with a stable
  source ID, and use one consistent marker syntax. Directly applicable if
  `.ROOT` or a Capability Library asset ever needs an AI-generated report
  with verifiable, per-claim citations (a client audit deliverable, for
  instance) — the citable-unit taxonomy alone (document vs. block vs. line)
  is a useful vocabulary even without adopting OpenAI's exact marker syntax.

## Minor/legacy notes

- **Local shell is deprecated** in favor of the `shell` tool covered above
  (gap closed July 12, 2026) — was Codex-CLI-specific, is now explicitly
  labeled outdated in its own doc.
- **Code generation** page is mostly a Codex/gpt-5.6 marketing gallery (one-
  shot frontend demos) — no durable mechanics beyond "use Codex for agentic
  coding, use gpt-5.6 directly for API-embedded code generation."

## Why this matters for this wiki / `.ROOT`

- **Deferred tool loading and code-mode orchestration are now
  cross-vendor-confirmed patterns**, not single-source claims — strengthens
  the existing validation in [[mcp-landscape-architecture-and-patterns]]
  that `.ROOT`'s own pointer-only routing (root CLAUDE.md → hub CLAUDE.md →
  skill body) is the general-purpose answer to context-cost problems, not an
  Anthropic-specific idiom.
- **The memory-shape convergence is now a three-source pattern** (OpenAI
  Sandbox Agents, Claude Code auto memory, `.ROOT`'s hand-built `memory/`) —
  raises the priority of the open question already flagged in
  [[claude-code-context-and-instruction-economics]]: is this shape worth
  naming as a documented `.ROOT` architecture principle rather than three
  parallel implementations that happened to converge.
- **The Computer Use consent taxonomy (hand-off / always-confirm /
  pre-approval-sufficient) is a sharper vocabulary than `.ROOT` currently
  has for judging its own risky actions** — this session's own operating
  instructions already draw a "reversible vs. hard-to-reverse vs.
  irreversible" line for file/git operations; OpenAI's three-tier framework
  with named example categories could sharpen that into a reusable
  decision table rather than a prose judgment call each time. Flagged as a
  candidate self-evolution note, not drafted.
- **Citation Formatting's citable-unit taxonomy** is usable now if a
  Capability Library asset or client audit report ever needs per-claim
  citations — no gap to close, just a vocabulary worth remembering.
- Companion page: [[openai-agents-sdk-and-orchestration]] covers the
  agent-definition, handoff, and guardrail layer these tools plug into.

---
*Processed July 12, 2026. Source in `raw/OPEN_AI-CHATGPT_CODEX_FILES/` (immutable).*
