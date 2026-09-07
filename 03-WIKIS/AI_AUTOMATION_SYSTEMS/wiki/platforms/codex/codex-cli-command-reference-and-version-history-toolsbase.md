---
type: research
timeline: reference
tags: [ai-automation, codex, commands, changelog, self-evolution]
source: "raw/OpenAI Codex CLI Cheat Sheet 2026.md (toolsbase.dev/en/reference/codex-commands, third-party reference site, verified against codex-cli v0.145.0, captured 2026-07-22)"
---

# Codex CLI — Command Surface and Version-History Reference (Toolsbase, 2026)

**Third-party (not vendor) command reference cataloging all 64 Codex CLI
commands, flags, and a version-by-version changelog back to v0.107.0.**
Complements [[codex-app-configuration-and-security]] (the official-docs page
covering config layers, sandbox/approval model, and deterministic guards in
depth) — that page explains *how Codex decides what it may do*; this source
is the *command surface* — what you actually type — plus roughly four months
of release history the config page doesn't carry.

**Volatility warning:** captured once, 2026-07-22, at codex-cli v0.145.0.
Command names, flags, and defaults are correct as of that capture only —
Codex CLI ships near-weekly; re-verify with `codex --help` or `codex doctor`
before depending on a specific flag.

## Command surface, grouped

- **Session lifecycle:** `codex` (start), `codex exec` (non-interactive
  one-shot), `codex resume` (`--last`/`<SESSION_ID>`), `codex fork`, `codex
  archive` / `unarchive` / `delete` (session housekeeping, added
  v0.136.0-v0.140.0 — delete is irreversible and confirmation-gated).
- **Review:** `codex review --uncommitted | --base <branch> | --commit
  <sha>`.
- **Cloud:** `codex apply <TASK_ID>`, `codex cloud list | diff | apply |
  exec` — remote non-interactive execution with local apply.
- **Auth:** `codex login` (`--device-auth`, `--with-api-key`,
  `--with-access-token` for non-interactive login), `codex login status`,
  `codex logout`.
- **Servers/daemons:** `codex app-server`, `codex exec-server` (WebSocket
  endpoint, v0.119.0+), `codex remote-control` (headless daemon with pairing
  via `codex remote-control pair`, v0.130.0+), `codex mcp-server` (run Codex
  itself as an MCP server over stdio).
- **MCP client-side:** `codex mcp add | list | get | remove`, `codex mcp
  login/logout <name>` (interactive OAuth for MCP servers, no experimental
  opt-in needed since v0.144.0).
- **Plugins:** `codex plugin`, `codex plugin marketplace add <SOURCE>` (repo
  slug, Git URL, or local dir; `--ref`, `--sparse`) — moved under `codex
  plugin` in v0.122.0, replacing the removed top-level `codex marketplace`.
- **Diagnostics/maintenance:** `codex doctor` (`--summary`/`--json`/`--all`,
  added v0.131.0 — now a "comprehensive setup checkup" per the Claude Code
  changelog's parallel `/checkup` naming), `codex update`, `codex features
  list | enable | disable`, `codex completion zsh|bash|fish`.
- **Sandbox/debug:** `codex sandbox`, `codex debug`.
- **Local models:** `codex --oss --local-provider lmstudio|ollama` — connect
  to a local LM Studio or Ollama provider instead of a hosted model.

## Key flags worth remembering

- `-m/--model`, `-p/--profile` (`fast`/`default`/`deep`/`max` reasoning
  depth), `-s/--sandbox` (`read-only`/`workspace-write`/
  `danger-full-access`), `-a/--ask-for-approval`
  (`untrusted`/`on-request`/`never`).
- `-C/--cd <dir>`, `--add-dir <dir>` (extra writable roots).
- `--search` (live web search via the Responses `web_search` tool),
  `--remote <ws://…>` + `--remote-auth-token-env` (connect TUI to a remote
  app-server), `-i/--image <file>` (attach images to the initial prompt).
- CI/automation-oriented: `--json` (JSONL event stream), `-o/
  --output-last-message <file>`, `--output-schema <file>` (JSON Schema
  validation of the final response), `--ephemeral` (no session persistence),
  `--skip-git-repo-check`, `--color always|never|auto`.
- Isolation/determinism for CI: `--ignore-user-config` (skip
  `$CODEX_HOME/config.toml`, auth still resolved), `--ignore-rules` (skip
  execpolicy `.rules`), `--strict-config` (fail on unrecognized config
  keys) — combine the first two for a fully isolated automated run.
- `--dangerously-bypass-approvals-and-sandbox` and
  `--dangerously-bypass-hook-trust` — both explicitly documented as for
  externally-sandboxed/vetted automation only, mirroring Claude Code's
  `--dangerously-skip-permissions` framing.
- `-c/--config key=value` — one-off TOML override, same mechanic as Claude
  Code's `/config key=value` (v2.1.181).

## Version-history highlights (0.107.0 → 0.145.0, ~4 months)

Themes that recur across the changelog, most-recent first:

- **Multi-agent orchestration matured fastest.** MultiAgentV2 config
  (thread caps, wait-time controls, v0.128.0) → sub-agent readable
  path-addresses like `/root/agent_a` with structured inter-agent messaging
  (v0.117.0) → **stabilized in v0.145.0** with configurable sub-agent
  models, reasoning levels, concurrency, and restored roles — the same
  expand-then-stabilize arc documented on the Claude Code side in
  [[claude-code-features-catalog-and-version-history-toolsbase]].
- **Session housekeeping arrived late and deliberately.** Archive/unarchive
  (v0.136.0) → permanent delete with confirmation + subagent cleanup
  (v0.140.0) → thread search across local history (v0.134.0) → experimental
  paginated thread history with persisted names and memories (v0.145.0).
- **Cross-tool migration is now bidirectional.** `/import` pulled Claude
  Code setup/config/chats into Codex (v0.140.0) → expanded to also migrate
  Cursor settings, MCP servers, plugins, sessions, and project-scoped
  memories (v0.145.0). Directly relevant to any `.ROOT` skills-mirror parity
  work between the two CLIs, per the recommendation already logged in
  [[codex-app-configuration-and-security]].
- **Guardian subagent** — routes sensitive review requests for additional
  approval; denies critical-risk, requires authorization for high-risk,
  fails closed on errors (documented in depth on the config-security page;
  this source adds the `codex review` command surface it attaches to).
- **Danger-command detection kept tightening.** v0.144.5 "improved
  dangerous-command detection, including more forced `rm` forms, with
  clearer rejection reasons" — same defense-in-depth pattern as Claude
  Code's `Bash(rm:*)` hardening.
- **Remote/Bedrock expansion:** experimental Amazon Bedrock login with
  custom endpoints (v0.145.0), GPT-5.6 Sol/Terra/Luna as Bedrock models with
  `max` reasoning effort (v0.143.0), Bedrock console-login credential
  support (v0.130.0).
- **New in v0.145.0 beyond multi-agent:** audio inputs/tool outputs and
  streaming realtime V3 conversations — the first audio-native capability
  logged for Codex CLI in this hub.

## Why this matters for `.ROOT`

- Fills the command-surface gap that
  [[codex-app-configuration-and-security]] intentionally left for a
  dedicated page (that page's "Command surface worth remembering" section
  cites `/import`, `codex exec`, and session lifecycle only in brief) — this
  source is the fuller reference for actually invoking Codex from a script
  or CI pipeline.
- `--ignore-user-config` + `--ignore-rules` + `--strict-config` together are
  the concrete recipe for a deterministic, profile-free CI run, worth
  citing directly if `.ROOT` ever wires Codex into GitHub Actions the way
  the existing Claude Code integration-surface page documents for Claude
  Code.
- Reinforces (third instance, after Claude Code's changelog and the
  config-security page's guardian/execpolicy findings) that both major CLI
  agent vendors are converging on the same shape: expand agent autonomy,
  then add a named deterministic guard a few releases later. Worth
  treating as a standing expectation, not a one-off observation, in any
  future agent-vetting or tool-adoption write-up from this hub.

---
*Processed July 22, 2026. Source in raw/ (immutable); third-party site, not vendor documentation — re-verify volatile claims before relying on them.*
