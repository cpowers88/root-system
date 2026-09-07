---
type: research
timeline: reference
tags: [ai-automation, mcp, security, authorization, agent-vetting]
source: raw/Security Best Practices.md + raw/Understanding Authorization in MCP.md (modelcontextprotocol.io clips, 2026-07-08)
---

# MCP Security and Authorization — Threat Catalog

**Official MCP security best practices and authorization docs
(modelcontextprotocol.io), clipped July 8, 2026.** Companion to
[[mcp-landscape-architecture-and-patterns]]; this is the depth layer under
the approved agent-tool vetting screen (Category 10,
`TECHNOLOGY_LIBRARY_STRATEGY.md`).

## One-paragraph summary

MCP's authorization model is OAuth 2.1 over the HTTP transport (optional
but strongly recommended whenever a server touches user-specific data,
needs audit trails, or serves enterprises); local stdio servers use
environment credentials instead. The security doc is effectively a threat
catalog of eight named attack classes — most exploit the *trust seams*
MCP creates: between client and server (malicious servers attacking
clients), between server and downstream APIs (proxy/token problems), and
between the protocol and the local machine (installed servers as code
execution). The recurring lesson: **a malicious or compromised MCP server
is an active adversary of the client**, not just a bad data source — every
URL, tool list, and session event it supplies is untrusted input.

## The eight attack classes

1. **Confused deputy** — an MCP proxy server that fronts a third-party API
   with one static client ID + dynamic client registration + the
   third-party's consent cookie lets an attacker's crafted link skip the
   consent screen and steal an authorization code via a malicious
   redirect URI. Mitigation: per-client consent registry checked *before*
   the third-party flow, exact-match redirect-URI validation, hardened
   single-use `state` parameters.
2. **Token passthrough** — server forwards client-supplied tokens to
   downstream APIs without validating they were issued *to the server*.
   Explicitly forbidden by the spec: it breaks rate limiting, audit
   trails, and trust boundaries. Servers MUST NOT accept tokens not
   issued for them (audience validation).
3. **SSRF via OAuth discovery** — a malicious server hands the client
   metadata URLs pointing at internal IPs, cloud metadata endpoints
   (`169.254.169.254` → IAM credential theft), or localhost services; the
   client becomes a proxy through the firewall. Mitigations: HTTPS-only,
   block private IP ranges (don't hand-roll the parser — encoding tricks),
   validate redirect hops, egress proxies, DNS pinning against rebinding.
4. **Session hijacking** — two variants: an attacker with a session ID
   injects events into a shared queue that get *resumed* into the victim's
   stream (including `tools/list_changed` — silently changing the victim's
   tool set), or simply impersonates the client. Mitigations: never use
   sessions for authentication, non-deterministic session IDs, bind
   session IDs to user identity (`<user_id>:<session_id>`).
5. **Local MCP server compromise** — installed servers are binaries with
   the client's privileges; attack vectors are malicious startup commands
   in one-click configs, payloads in the server itself, and DNS rebinding
   against insecure localhost servers. Mitigations: show the exact
   untruncated command before execution, flag dangerous patterns
   (`sudo`, `rm -rf`, SSH-key paths), sandbox spawned servers, prefer
   stdio over localhost HTTP.
6. **OAuth authorization URL injection** — malicious servers supply
   `javascript:` URLs (XSS in the client) or shell-metacharacter URLs
   (RCE if the client opens URLs via a shell). Mitigations: allowlist
   `http(s)://` schemes only, never open URLs through a shell, CSP for
   web clients.
7. **stdio proxy escalation** — in proxy architectures (a local service
   spawning stdio servers on request), client-side XSS can steal the
   proxy auth token and spawn arbitrary commands → full RCE. Mitigations:
   fix the XSS classes above, sandbox spawned processes, least-privilege
   proxy.
8. **Scope inflation** — broad up-front scopes (`files:*`, `admin:*`)
   expand blast radius, muddy audits, and train users to click through
   consent. Mitigation: minimal initial scopes with incremental elevation
   via `WWW-Authenticate` challenges when a privileged operation is first
   attempted.

## Authorization essentials

- **When to add it**: user-specific data, per-user audit needs, consented
  API access, enterprise controls, per-user rate limiting. Optional in the
  spec, strongly recommended in practice for anything remote.
- **Local vs. remote split**: stdio servers can use environment
  credentials; OAuth flows exist for HTTP transports where the server is
  remote.
- **Pitfall list worth keeping** (from the authorization doc): never
  hand-roll token validation; short-lived tokens; always validate audience
  ("a token arriving is not a token that's valid *for you*");
  least-privilege scopes per tool; never log credentials; treat
  `Mcp-Session-Id` as untrusted input and never tie authorization to it;
  unauthenticated dynamic client registration means anyone can register
  any client.

## Why this matters for this wiki / `.ROOT`

- **Direct sharpening of the vetting screen.** The approved Category 10
  screen asks whether an agent tool can be stopped, sandboxed, and
  audited. This catalog supplies the MCP-specific questions behind those
  checks: *Does this local server config show me the exact command? Is the
  remote server's OAuth its own or is it proxying a third party? What
  scopes does it demand up front?* Worth folding into any future audit
  checklist — via proposal, not unilaterally.
- **Chris's own setup is in scope.** Every MCP server added to Claude
  Desktop/Code on this machine is an instance of attack class 5. The
  practical house rule the docs imply: trusted sources only, read the
  full startup command, prefer stdio, and treat one-click installs with
  the same suspicion as `curl | sh`.
- **The Comet incident pattern generalizes.** [[2025-ai-agent-index]]
  logged Comet's hidden-MCP-API incident; this catalog shows the same
  seams (untrusted server input, session events changing tool sets) are
  protocol-generic, not one vendor's bug — supporting the Index's finding
  that MCP dominance concentrates risk as well as capability.
- **For client work**: "the MCP server you install is code execution with
  your privileges" is the one-sentence version for a small-business
  audience; the eight classes give the professional backing.

---
*Processed July 8, 2026. Source clips in `raw/` (immutable). SVG-heavy
source; text extracted to scratchpad during processing, nothing in `raw/`
modified.*
