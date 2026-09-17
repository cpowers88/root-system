---
type: research
timeline: reference
tags: [ai-automation, codex, configuration, sandboxing, approvals, security, self-evolution]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ — Config basics.md, Configuration Reference.md, Advanced Configuration.md, Agent approvals & security.md, Developer commands.md (official Codex app docs from learn.chatgpt.com, captured by Chris July 17, 2026 specifically to close this hub's Codex-config evidence gap)
---

# Codex App — Configuration Layers, Sandboxing, Approvals, and Command Surface

**Official Codex (CLI/desktop/IDE) configuration documentation, all five pages
read in full July 17, 2026 — the first vendor-grounded coverage of the Codex
app's own config surface in this hub.** The existing OpenAI pack covered the
*platform* (Responses API, Agents SDK, MCP); this batch covers the *local
agent product* `.ROOT` actually runs. Captured same-day to convert the July 17
AI-surface config audit (`00-BRAIN\Session_Logs\AI_SURFACE_CONFIG_AUDIT_2026-07-17.md`)
from model-knowledge to evidence — and the reading immediately resolved one
audit unknown and surfaced two mechanisms the audit didn't know existed.

## One-paragraph summary

Codex resolves configuration through a six-level precedence stack (CLI flags →
project `.codex/config.toml` files root-to-cwd, closest wins → `--profile`
files → user `~/.codex/config.toml` → system → defaults), and **project-scoped
layers load only when the project is trusted** — trust is therefore not a
convenience flag but the switch that turns a repo's checked-in Codex policy on
or off. Security comes from two cooperating layers — an OS-enforced sandbox
(what Codex *can* do) and an approval policy (when it must *ask*) — with
network off by default in `workspace-write`, and `.git/`, `.codex/`, and
`.agents/` kept read-only *inside* the writable workspace. Beyond the basics
the docs reveal three deterministic-guard mechanisms this hub had no evidence
for: **named permission profiles** (beta; per-path/glob `read`/`write`/`deny`
filesystem rules), **execpolicy `.rules` files** (prefix rules that allow,
prompt, or forbid specific commands), and **lifecycle hooks** (PreToolUse etc.,
Claude-hook-equivalents, trusted-project-gated).

## The configuration layer model

Highest precedence first:

1. CLI flags and `-c`/`--config` one-off overrides (values parsed as TOML)
2. Project `.codex/config.toml` files, project root down to cwd, **closest wins — trusted projects only**
3. Profile file selected with `--profile name` (`~/.codex/name.config.toml`; since 0.134 profiles are separate files, not `[profiles.*]` tables)
4. User `~/.codex/config.toml`
5. System `/etc/codex/config.toml` (Unix)
6. Built-in defaults

Load-bearing details:

- **Untrusted projects skip every project `.codex/` layer** — config, hooks,
  and rules. `projects.<path>.trust_level = "trusted"` in the user config is
  what arms a repo's checked-in policy. (This resolved audit Finding C2 the
  day the docs were captured: `.ROOT`'s project config is live because
  `c:\users\chris\.root` is trusted.)
- Project config **cannot** override machine-owned keys — provider/auth
  (`model_provider`, `model_providers`, `openai_base_url`), `notify`,
  `profile(s)`, telemetry (`otel`) are ignored with a startup warning. A
  malicious repo cannot redirect credentials or traffic via checked-in config.
- Project root = first ancestor containing `.git` (customizable via
  `project_root_markers`).
- Verification commands: **`/status`** (active model, approval policy,
  writable roots, token use) and **`/debug-config`** (layer order, on/off
  state, policy sources) — the exact tools for "is this file actually
  loading?" questions. `codex doctor` for full installation diagnostics.

## AGENTS.md discovery

- Codex reads `AGENTS.md` at the project level and includes it in the first
  turn; `~/.codex/AGENTS.md` is the global (every-session) instruction file.
- `project_doc_max_bytes` caps how much is read per file;
  `project_doc_fallback_filenames` lets other filenames stand in when
  `AGENTS.md` is absent at a directory level.
- `/init` generates an `AGENTS.md` scaffold; `model_instructions_file`
  replaces built-in instructions entirely (a bigger hammer than AGENTS.md).
- Relative paths inside a project config resolve from the `.codex/` folder
  that declares them.

## Sandbox and approvals — the two-layer model

**Sandbox mode** (what's technically possible): `read-only` |
`workspace-write` | `danger-full-access`. **Approval policy** (when to ask):
`untrusted` | `on-request` | `never` | granular table. The "Auto" preset =
`workspace-write` + `on-request`.

`workspace-write` mechanics worth knowing precisely:

- Network **off by default**; opt in via `[sandbox_workspace_write] network_access = true`.
- Writable roots include the workspace plus `/tmp`-style dirs; extend with
  `writable_roots` or `--add-dir` (prefer these over escalating to full access).
- **Protected read-only paths inside writable roots: `.git/`, `.codex/`, and
  `.agents/`** — recursive, vendor-enforced. Codex cannot edit its own project
  config or a repo's `.agents/` content from inside the sandbox. (Direct
  parallel to Claude Code's protected-`.claude/` backstop documented in
  [[claude-code-permissions-security-and-review]].)
- OS enforcement: macOS Seatbelt; Linux bwrap+seccomp; **native Windows uses
  its own sandbox implementation** — `[windows] sandbox = "elevated"` is the
  documented recommendation, `"unelevated"` is the fallback when admin setup
  isn't available; `/setup-default-sandbox` performs the elevated upgrade
  in-session, `/sandbox-add-read-dir` grants extra read roots (both
  Windows-only). WSL2 gives Linux sandbox semantics instead. Test any command
  under the sandbox with `codex sandbox windows [--permissions-profile <name>] -- <cmd>`.
- Approval prompts also cover side-effecting app/MCP tool calls; tools that
  advertise a destructive annotation *always* require approval.

**Granular approval policy** (`approval_policy = { granular = { ... } }`)
keeps chosen prompt categories interactive while auto-rejecting others
(sandbox escalations, execpolicy prompts, MCP elicitations,
`request_permissions`, skill approvals) — fail-closed automation without
going to `never`.

**`approvals_reviewer`**: `user` (default) routes approval prompts to the
human; **`auto_review` routes them to a reviewer agent** (guardian policy:
denies critical-risk, requires authorization for high-risk, fails closed on
errors; `/approve` retries a denial once). This changes *who reviews*, not
the sandbox boundary — but it substitutes an AI reviewer for the human on
exactly the actions that were consequential enough to prompt. Uses extra
model calls.

## Network policy and web search

- `[features.network_proxy]` (experimental) constrains enabled network access
  to a domain policy: allowlist-first; exact hosts; `*.example.com`
  (subdomains only) vs `**.example.com` (apex + subdomains); `deny` always
  wins; global `*` allow = broad access, discouraged. Local/private
  destinations blocked by default (`allow_local_binding = false`); DNS
  rebinding best-effort checks (failed lookups blocked).
- The proxy feature *shapes* traffic; `sandbox_workspace_write.network_access`
  decides whether commands have network at all. Off + proxy on = still off.
- `web_search` is a separate channel: `"cached"` (default — OpenAI-maintained
  index, no live fetch, reduced prompt-injection exposure), `"indexed"`,
  `"live"` (`--search`), `"disabled"`. Under `--yolo`/full access it defaults
  to live. Web results are untrusted in every mode.

## Deterministic guards beyond the sandbox

Three mechanisms give Codex rule-level control this hub previously believed
it lacked:

1. **Named permission profiles (beta).** Built-ins `:read-only`, `:workspace`,
   `:danger-full-access`; custom `[permissions.<name>]` tables with
   `extends`, per-path/glob filesystem rules valued `"read"` / `"write"` /
   `"deny"` (deny blocks *reads*), `:workspace_roots`-relative subpath rules
   (e.g. deny `**/*.env`), and a full network sub-policy. Selected via
   `default_permissions` — **do not combine with `sandbox_mode` /
   `[sandbox_workspace_write]`**; it replaces them. This is the Codex
   equivalent of Claude's path deny rules: a profile can make `raw/`
   read-only and a private folder read-denied, mechanically.
2. **Execpolicy rules.** `.rules` files (user `~/.codex/rules/`, project
   layer) hold prefix rules with decisions `allow`/`prompt`/`forbidden` —
   command-level guards (e.g. forbid `Remove-Item`, prompt on `git push`).
   Validate with `codex execpolicy check --rules <file> -- <cmd>`;
   `--ignore-rules` exists for exec runs, so rules are a guard, not an
   absolute wall. Admin `requirements.toml` can enforce restrictive-only
   rules (`prompt`/`forbidden`) plus `permissions.filesystem.deny_read`
   that users cannot weaken — enterprise-grade but documented, and the
   conceptual ceiling for what "managed" hardening looks like.
3. **Lifecycle hooks.** `hooks.json` or inline `[hooks]` next to any active
   config layer (`~/.codex/` or `<repo>/.codex/`); events include
   `PreToolUse`, `PermissionRequest`, `PostToolUse`, `SessionStart`, `Stop`,
   subagent events; command hooks supported, `commandWindows` for
   Windows-specific overrides; project hooks gated on trust; `/hooks`
   browser with explicit trust step. Same "guardrails belong in hooks"
   principle already confirmed on the Claude side.

## Command surface worth remembering

- `codex exec` — non-interactive runs (`--json`, `--output-last-message`,
  `--output-schema`, `--ephemeral`, `exec resume --last`); `codex review
  --uncommitted|--base|--commit` — non-interactive code review;
  `review_model` config key overrides the review model.
- Session lifecycle: `codex resume`/`fork`/`archive`/`unarchive`/`delete`;
  in-TUI `/new`, `/fork`, `/side` (ephemeral side chat), `/compact`,
  `/rename`.
- **`/import` migrates Claude Code configuration, project files, and recent
  chats into Codex** — directly relevant to any skills-mirror or dual-surface
  parity work.
- `/skills` (skill picker; `skills.config` per-skill enablement),
  `/memories` + `[features] memories` (experimental, off by default —
  Codex's own auto-memory channel), `/goal` (persistent task goal),
  `/plan` (plan mode; `plan_mode_reasoning_effort`).
- Ops/privacy toggles: `[analytics] enabled=false`, `[feedback]
  enabled=false`, `[history] persistence="none"` / `max_bytes`, `[otel]`
  opt-in telemetry (off by default; prompts redacted unless opted in),
  `shell_environment_policy` (env-var hygiene for spawned commands —
  KEY/SECRET/TOKEN filtered by default), `allow_login_shell = false`
  hardening, `notify` external-command notifications vs `tui.notifications`.
- `--yolo` / `--dangerously-bypass-approvals-and-sandbox` exists; docs are
  blunt that it belongs only inside externally hardened isolation.

## Why this matters for this wiki / `.ROOT`

- **Audit Finding C2 resolved by evidence**: project `.codex/config.toml`
  loads for trusted projects; `.ROOT` is trusted, so its
  `workspace-write` + `on-request` + network-off policy is live. Corollary:
  the protection *depends on* the trust grant — and on the flip side, every
  `trust_level = "trusted"` entry arms that directory's checked-in `.codex/`
  layers, which strengthens the audit's prune-the-stale-trust-grants item.
- **`.ROOT`'s global config sets `approvals_reviewer = "auto_review"`** — an
  AI guardian, not Chris, currently reviews Codex approval prompts. That is
  in tension with `AGENT.md`'s consequential-actions-remain-human-approved
  rule and was invisible before this batch. Needs a Chris decision:
  `user` for alignment, or a documented exception.
- **A mechanical raw/journal guard for Codex now has a documented path**:
  a custom permission profile (raw read-only, journal read-denied) or, more
  simply now, execpolicy rules forbidding destructive commands — candidates
  for the audit's action plan, replacing the filesystem-attributes workaround
  as the idiomatic option. Beta status means: pilot, verify with
  `codex sandbox windows -P <profile>`, then adopt.
- **Windows sandbox mode should probably move `unelevated` → `elevated`**
  (docs' explicit recommendation; `/setup-default-sandbox` does it) — audit
  item, needs admin rights once.
- **`.codex/` and `.agents/` are vendor-protected read-only in-sandbox** —
  the skills mirror and project config can't be silently self-edited by a
  sandboxed Codex, mirroring Claude's protected-path backstop. Two vendors,
  same conclusion: agent config is not agent-writable.
- **`/import` (Claude Code → Codex migration)** is the cheap first move for
  audit item 9 (skills-mirror parity) before extending `sync_shared_skills.py`.
- Companion pages: [[claude-code-permissions-security-and-review]] (the
  Claude-side mirror of this page), [[openai-sdks-cli-and-agent-builder]]
  (the `openai` CLI and SDK landscape — a different tool than this local
  agent surface), [[shift-to-agentic-ai-codex]] (usage evidence),
  [[mcp-security-and-authorization]] (the MCP server allowlisting/identity
  requirements echo its threat catalog).
- Not yet captured: the dedicated Permissions, Hooks, Rules, AGENTS.md, and
  Sandboxing concept pages this batch links to — grab those before
  implementing the permission-profile or hooks recommendations.

---
*Processed July 17, 2026. Sources in raw/ (immutable).*
