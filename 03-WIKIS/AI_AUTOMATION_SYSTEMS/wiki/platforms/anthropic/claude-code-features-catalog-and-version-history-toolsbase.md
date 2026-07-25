---
type: research
timeline: reference
tags: [ai-automation, claude-code, features, changelog, self-evolution]
source: "raw/Claude Code Features Guide 2026 — 67 Capabilities Explained.md (toolsbase.dev/en/reference/claude-code-features, third-party reference site, verified against Claude Code v2.1.217, captured 2026-07-22)"
---

# Claude Code — Feature Catalog and Version-History Reference (Toolsbase, 2026)

**Third-party (not vendor) reference site cataloging all 67 Claude Code
features by capability category, plus a full version-history changelog back
to v1.0.x.** Complements the five existing vendor-sourced Claude Code pages
in this hub — [[claude-code-context-and-instruction-economics]],
[[claude-code-workflows-and-sessions]],
[[claude-code-permissions-security-and-review]],
[[claude-code-prompt-library-patterns]], and
[[claude-code-integration-surface-and-platform]] — which are organized by
theme (memory, sessions, security, prompts, platform surfaces). This source's
distinct value is (1) a single flat capability index across all categories,
useful as a "what can Claude Code do" lookup, and (2) a dense version-by-
version changelog spanning roughly a year of releases, which none of the
other pages carry at this granularity.

**Volatility warning:** this is a fast-moving CLI product; the source claims
"continuously updated" but was captured once, 2026-07-22, at v2.1.217. Treat
version numbers, flag names, and default values as correct as of that capture
— re-verify against `/release-notes` or official docs before depending on a
specific mechanic.

## Category structure (67 features, 8 groups)

- **Code Editing** — file read/write, multi-file editing, code generation,
  refactoring, bug fixing, code review, auto lint fix.
- **Git Operations** — commit creation, PR creation/review, branch
  management, diff analysis, conflict resolution, history investigation.
- **Terminal** — command execution, environment setup, package management,
  build & run, process management, prompt suggestions, `/btw` side
  questions, session recap.
- **Project Understanding** — codebase search, dependency analysis, code
  explanation, architecture analysis, impact analysis, image input
  (multimodal).
- **Testing** — test generation, execution/debugging, TDD cycle, test
  maintenance, run-and-verify (the `/run`, `/verify`, `/run-skill-generator`
  bundled skills, v2.1.145+).
- **MCP Integration** — server connections, browser automation (Playwright
  MCP), external API access, database access.
- **Customization** — CLAUDE.md, Skills, Hooks (20+ lifecycle events),
  permission modes, model selection, Memory (CLAUDE.md + Auto Memory),
  plugin system, keybinding customization.
- **Advanced** — sub-agents, parallel agents, agent teams, context
  management, checkpointing/rewind, IDE integration, headless mode, SDK/API
  integration, GitHub Actions, Claude Code on the Web, remote control,
  channels (Telegram/Discord/iMessage), git worktree isolation, scheduled
  tasks, voice dictation, fast mode, fullscreen rendering, push
  notifications, goal-driven work, dynamic workflows, Claude in Chrome,
  screen reader mode.

Full usage examples for every feature are in `raw/` — this page synthesizes
the version history and cross-hub-relevant mechanics rather than reproducing
the catalog entry-by-entry.

## Version-history throughline worth carrying forward

Reading roughly a year of releases in sequence (v1.0.x → v2.1.217) surfaces a
consistent pattern already independently observed elsewhere in this hub: each
capability expansion (nested subagents, dynamic workflows, auto mode) arrives
paired with a safety-hardening follow-up a few releases later. Concrete
instances:

- **Concurrency/orchestration expands, then gets a ceiling.** Sub-agents
  gained self-nesting up to 5 levels (v2.1.172) → nested spawning turned
  **off by default** with a depth env-var override, plus a default cap of 20
  concurrently-running subagents (v2.1.217). Dynamic workflows (orchestrating
  tens to hundreds of background agents, v2.1.154) later gained an advisory
  "Dynamic workflow size" setting (v2.1.202) — advisory, not a hard cap.
- **Auto mode expands, then gets destructive-action guards.** Auto mode
  reached Max subscribers on Opus 4.7 (v2.1.108-112) → destructive git
  commands (`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git
  stash drop`) blocked unless explicitly requested, `git commit --amend`
  blocked on commits not made this session (v2.1.183) → asks before `rm -rf`
  on unresolved variables (v2.1.205) → subagent spawns evaluated by the
  classifier *before* launch, closing a gap where a subagent could bypass
  review (v2.1.178).
- **Permission-rule matching got two correctness fixes worth knowing if
  `.ROOT`'s own deny rules rely on them:** hook matchers with hyphenated
  names (e.g. `mcp__brave-search`) were substring-matching instead of exact-
  matching until v2.1.195; `Tool(param:value)` syntax (e.g.
  `Agent(model:opus)`) for parameter-scoped permission rules landed in
  v2.1.178.
- **`EndConversation` tool added (v2.1.214)** — lets Claude end sessions with
  highly abusive users or jailbreak attempts. Directly matches the
  `EndConversation` deferred tool available in this Claude Code environment;
  confirms it is a documented, intentional safety feature, not a `.ROOT`-side
  customization.
- **`/ultrareview` (v2.1.120, `claude ultrareview` CI subcommand added same
  release)** — the multi-agent cloud code review skill this environment's
  own system prompt references as user-triggered and billed. The changelog
  confirms its CI-scriptable form (`--json`, exit-code semantics) exists
  alongside the interactive skill.
- **Model lineage relevant to this session:** Sonnet 5 became the Claude Code
  default (v2.1.197, 1M-token context, promotional $2/$10 per Mtok pricing
  through Aug 31 2026); Fable 5 introduced as a "Mythos-class" model
  exceeding prior general-release capability (v2.1.170); Opus 4.8 added at
  default high effort (v2.1.154). Matches the model roster this environment
  is already running under (Sonnet 5 confirmed as this session's model).

## Mechanics newly surfaced here (not yet in the other 5 Claude Code pages)

- **`/goal`** (v2.1.139) — set a completion condition; Claude keeps working
  across turns until met, with a live elapsed-time/turns/tokens overlay.
  Works in interactive, `-p`, and Remote Control.
- **Dynamic workflows / `ultracode`** (v2.1.154, keyword renamed from
  `workflow` in v2.1.160) — orchestrates tens to hundreds of background
  agents from one instruction; `/workflows` to monitor/pause/resume/save.
- **Agent Teams** (v2.1.x, 2026-03 era) — multiple Claude Code instances
  coordinating with a lead assigning tasks and direct inter-teammate
  messaging, distinct from the simpler parallel-subagent pattern.
- **Claude in Chrome** (GA v2.1.198) — browser control sharing the user's
  logged-in state; chains browser verification with coding tasks in one
  workflow (read console errors, verify UI against design, test form
  validation).
- **Channels** — Telegram/Discord/iMessage/custom webhooks pushed into a
  running session for two-way chat-bridge workflows.
- **Screen reader mode** (v2.1.208) — opt-in flat plain-text rendering,
  `claude --ax-screen-reader` / `axScreenReader` setting.

## Why this matters for `.ROOT`

- Confirms two names already live in this session's own tool surface
  (`EndConversation`, `/ultrareview`) are documented vendor features with a
  known introduction version and rationale — useful if a future audit needs
  to distinguish vendor behavior from `.ROOT` customization.
- The capability-expands-then-gets-hardened pattern is a reusable heuristic
  for this hub's own self-evolution research: when evaluating a new agentic
  capability (for `.ROOT` or a client), expect (and design for) a follow-on
  hardening pass rather than treating the initial release as the final
  safety posture.
- Companion source: [[codex-cli-command-reference-and-version-history-toolsbase]]
  is the same publisher's equivalent catalog for Codex CLI, captured the same
  day — useful for direct cross-vendor feature comparison.

---
*Processed July 22, 2026. Source in raw/ (immutable); third-party site, not vendor documentation — re-verify volatile claims before relying on them.*
