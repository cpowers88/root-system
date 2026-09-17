---
type: research
timeline: reference
tags: [ai-automation, mcp, agent-patterns, human-in-the-loop, practical-reference]
source: raw/Understanding MCP clients.md + raw/Build an MCP server.md + raw/Build an MCP client.md (modelcontextprotocol.io clips, 2026-07-08)
---

# MCP Client Primitives in Depth + Build Notes

**Second-pass extraction from the July 8 MCP docs batch.** The first pass
([[mcp-landscape-architecture-and-patterns]]) covered these three client
primitives in one line each and shelved the two build tutorials as
"implementation reference." This page pulls out what those files actually
add: the trust semantics of the client primitives, and the
language-agnostic build/debug knowledge buried in ~180KB of per-language
tutorial.

## The three client primitives — what the summaries miss

**Elicitation** (server → structured user input, mid-operation):
- The point is *pausing instead of failing*: servers request missing data
  or confirmation on demand rather than demanding everything up front.
- Requests carry a message plus a JSON `requestedSchema`; clients validate
  responses against the schema, and users can always fill in, decline
  (with optional explanation), or cancel outright.
- Hard privacy line in the docs: **elicitation never requests passwords
  or API keys**; clients should warn on suspicious requests. A server
  eliciting credentials is a red flag, full stop.

**Roots** (client → server filesystem scope) — the big caveat:
- Roots are `file://` URIs telling a server where to operate, updated
  live via `roots/list_changed` as the user changes workspaces.
- **Roots are coordination, not security.** The spec says servers
  "SHOULD respect" boundaries, not "MUST enforce" — because servers run
  code the client cannot control. Real enforcement must come from OS
  file permissions or sandboxing. Roots prevent *accidents* by
  well-behaved servers; they do nothing against malicious ones.

**Sampling** (server borrows the client's LLM):
- Lets a server do AI-dependent work without shipping or paying for its
  own model; the request rides through the client, which holds all the
  permission and security control.
- Requests can carry `modelPreferences` — a suggested model hint plus
  weighted cost/speed/intelligence priorities — and each sampling call is
  a *separate* model call with its own context boundary, which is also a
  context-economy device.
- Human-in-the-loop by design: users can review/modify both the prompt
  going out and the completion coming back before the server sees it;
  clients can require approval per request or auto-approve trusted
  operations, and should rate-limit and validate all content.

## Build notes — the language-agnostic 10% of the tutorials

The two "Build an MCP…" clips repeat one weather-server/client tutorial
across 8 languages. What survives extraction:

- **The stdio logging rule** (top gotcha): a STDIO server must never
  write to stdout — it corrupts the JSON-RPC stream and breaks the
  server. Log to stderr or files; plain `print()` is the classic bug.
  HTTP servers can log to stdout freely.
- **The host loop, demystified**: query → client sends question + tool
  descriptions to the model → model picks tools → client executes them
  through the server → results return to the model → natural-language
  answer. (Same loop `.ROOT` sessions live inside.)
- **Client-side best practices**: wrap tool calls in try/catch with
  meaningful errors; clean up connections deterministically; keep API
  keys in `.env`, never in code; *validate server responses* — trust
  flows both ways.
- **Debug quick-reference** (directly useful on this machine):
  - Claude Desktop MCP logs: `%APPDATA%\Claude\logs\mcp*.log` (Windows) /
    `~/Library/Logs/Claude` (macOS); `mcp-server-NAME.log` carries each
    server's stderr.
  - Config changes need a **full quit** of Claude Desktop (system-tray
    Quit on Windows — closing the window isn't enough).
  - Server paths in configs must be absolute; missing-server and
    silent-tool-failure triage starts with the logs, then running the
    server command manually.
  - First response after connecting can take ~30 seconds (server init);
    don't interrupt it.

## Why this matters for this wiki / `.ROOT`

- **"Roots are advisory" belongs in the vetting mindset.** The Category
  10 screen asks whether a tool is sandboxed; this page supplies the
  spec-level reason that question can't be waved away: MCP's own scoping
  primitive explicitly does not enforce anything. Directory scoping
  claims from a server are a courtesy, not a control — enforcement is
  the OS's or the client's job.
- **Sampling is the protocol-level verification-gap pattern.**
  Human-in-the-loop checkpoints on both sides of a server-initiated model
  call are exactly the "verification capacity gates autonomy" finding
  from [[agentic-ai-industry-adoption-barriers]], designed into a wire
  protocol.
- **The debug quick-reference is operational**, not research: it's the
  page to open when an MCP server on Chris's machine misbehaves.

---
*Processed July 8, 2026 (session 6). Completes extraction of the July 8
MCP batch; the per-language tutorial bodies in `raw/` remain as code
reference only.*
