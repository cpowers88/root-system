---
type: research
tags: [ai-automation, mcp, agent-patterns, architecture, context-management]
source: raw/ MCP docs batch of 2026-07-08 (modelcontextprotocol.io clips — Architecture_Overview, WHAT_is_the_MODEL_CONTEXT_PROTOCOL, Understanding MCP servers/clients, Client Best Practices, SDKs, Build with Agent Skills, MCP Inspector, Connect to local/remote MCP servers; Build an MCP server/client kept as implementation reference)
---

# MCP Landscape — Architecture, Primitives, and Scaling Patterns

**Official Model Context Protocol documentation (modelcontextprotocol.io),
clipped July 8, 2026.** This is the MCP-landscape page that has been the
open research rep since session 3 — MCP surfaced as the dominant interop
standard in the 2025 AI Agent Index, and it is a named rung in Chris's
integration-layer build territory.

## One-paragraph summary

MCP is an open, JSON-RPC-2.0-based standard for connecting AI applications
to external systems — "a USB-C port for AI applications." A **host** (the
AI app: Claude Code, Claude Desktop, VS Code) creates one **client** per
**server** connection; servers expose context and actions through three
primitives, clients expose three back, and two transports (local stdio,
remote Streamable HTTP) carry the same message format. The most
consequential material in this batch is not the protocol itself but the
**client scaling patterns**: progressive tool discovery and programmatic
tool calling ("code mode"), which are the ecosystem's answers to the
context-window costs of connecting many tools.

## Architecture in five facts

1. **Participants**: Host (AI application) → instantiates one MCP client
   per server → each client holds a dedicated connection to one MCP server.
   "Server" means the program serving context, regardless of where it runs.
2. **Two layers**: a data layer (JSON-RPC 2.0 — lifecycle, primitives,
   notifications) inside a transport layer (stdio for local processes,
   Streamable HTTP + optional SSE for remote; OAuth recommended for auth).
3. **Lifecycle**: stateful protocol; `initialize` negotiates protocol
   version and capabilities before anything else. Capability negotiation is
   what lets clients avoid calling unsupported operations.
4. **Discovery is dynamic**: every primitive has `*/list` methods, and
   servers can push `notifications/*/list_changed` so clients refresh
   without polling. (Security note: this is also an attack surface — see
   [[mcp-security-and-authorization]] on session-hijack tool injection.)
5. **Scope**: MCP defines only the context-exchange protocol — spec, SDKs
   (Tier 1: TypeScript, Python, C#, Go), Inspector, reference servers. It
   does not dictate how hosts use LLMs or manage the provided context.

## The six primitives (plus one experimental)

Server-side — the core mental model is **who controls each one**:

| Primitive | What it is | Who controls it |
|---|---|---|
| **Tools** | Executable functions the LLM invokes (write DBs, call APIs, modify files) | Model |
| **Resources** | Passive, read-only context data with URIs and MIME types; direct or templated (`travel://activities/{city}`) | Application |
| **Prompts** | Reusable parameterized templates (slash-command style) | User |

Client-side (what servers can ask of clients):

- **Sampling** — server requests an LLM completion *through the client*,
  staying model-independent; client keeps full control of permissions.
- **Elicitation** — server pauses mid-operation to request structured user
  input (confirmations, preferences) instead of failing on missing data.
- **Roots** — client tells the server which directories are in scope.
  Advisory only — see [[mcp-client-primitives-and-build-notes]] for the
  trust semantics of all three (roots don't enforce, elicitation never
  asks for credentials, sampling is human-in-the-loop by design).

Cross-cutting and experimental: **Tasks** — durable execution wrappers for
long-running MCP requests with deferred results and status tracking.

## Client scaling patterns (the high-value section)

From "Client Best Practices" — how hosts survive hundreds of tools:

- **Progressive tool discovery**: don't inject every tool definition into
  context upfront (naive loading can burn ~150K tokens on definitions
  alone vs. ~2K on demand). Fetch via `tools/list` but defer injection;
  give the model a `search_tools` meta-tool; load full schemas only when
  needed. Recommended trigger: a threshold at ~1–5% of the context window.
  Search strategies: keyword (BM25), embeddings, a small-model subagent,
  or hybrid — and prefer the provider's native tool search when one exists.
- **Dynamic server management**: extend the same idea to whole servers —
  keep a registry, connect only when the model needs that server,
  disconnect to free context. Notably: an **agent skill can declare which
  MCP servers it needs**, and the host connects them only when the skill
  is invoked.
- **Prompt-caching interaction**: adding/removing tool definitions
  mid-conversation invalidates the prompt cache, which can cost more than
  the definitions saved. Append after the cache breakpoint, or route
  everything through one stable `call_tool({name, args})` meta-tool.
- **Programmatic tool calling / code mode**: instead of one round trip per
  tool call (with every intermediate result flowing through the model),
  the model writes a script against typed APIs auto-generated from tool
  schemas; the script runs in a sandbox and only the final result returns
  (~100K+ tokens of intermediates collapsed to a ~200-token script and a
  ~15-token answer). Requires the client to implement a sandbox.

## Building and shipping servers

- **Four deployment paths** (from the `mcp-server-dev` agent-skills
  plugin): remote Streamable HTTP is the default for anything wrapping a
  cloud API; MCP Apps add interactive widgets in chat; MCPB bundles a
  local server with its runtime into a one-file install; bare local stdio
  remains the prototyping path.
- **Agent skills as build scaffolding**: Anthropic ships composing skills
  (`build-mcp-server`, `build-mcp-app`, `build-mcpb`) that interrogate the
  use case (what it connects to, who uses it, action-surface size,
  interaction needs, upstream auth) before scaffolding — the same
  systematization pattern validated in [[shift-to-agentic-ai-codex]].
- **MCP Inspector** (`npx @modelcontextprotocol/inspector <command>`) is
  the standard test/debug harness — tabs for tools, resources, prompts,
  and server notifications.
- Client-side setup: local servers via `claude_desktop_config.json`-style
  command configs (every action user-approved); remote servers via Custom
  Connectors in Claude — verify authenticity before connecting.

## Why this matters for this wiki / `.ROOT`

- **Progressive discovery is the `.ROOT` router pattern, formalized.**
  `.ROOT` already works this way: a pointer-only `CLAUDE.md` routes to
  section operating files loaded only when needed, exactly analogous to
  catalog → inspect → execute. The official docs now recommend what
  `.ROOT` converged on independently — useful validation, and useful
  vocabulary ("1–5% of context threshold") for judging when a flat file
  structure should become a routed one.
- **Skill-declared server dependencies** ("a skill file can declare which
  MCP servers it needs") is a concrete pattern worth watching for `.ROOT`:
  section operating files could similarly declare which tools/wikis a
  session type needs, rather than every session booting everything.
- **For the audit/client lens** (castle proof projects): the deployment
  decision tree (remote HTTP vs. MCPB vs. stdio) and the "who controls
  it" primitive table are directly reusable when explaining to a small
  business what connecting an AI to their systems actually entails.
- Companion page: [[mcp-security-and-authorization]] carries the threat
  model; the approved agent-tool vetting screen in
  `TECHNOLOGY_LIBRARY_STRATEGY.md` Category 10 gets its MCP-specific depth
  from these two pages together.

---
*Processed July 8, 2026. Source clips in `raw/` (immutable). The two
"Build an MCP server/client" clips are per-language tutorials — kept as
implementation reference, not separately summarized.*
