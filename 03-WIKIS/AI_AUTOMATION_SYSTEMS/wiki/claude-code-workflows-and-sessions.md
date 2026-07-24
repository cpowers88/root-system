---
type: research
tags: [ai-automation, claude-code, workflow-patterns, session-management, extensibility]
source: raw/CLAUDE_FILES/ (Anthropic official docs, moved from CASTLE raw/ to this wiki July 12, 2026 — COMMON_WORKFLOWS, MANAGE_SESSIONS, Extend_Claude_Code)
---

# Claude Code — Workflow Recipes, Session Mechanics, and the Extension Ladder

**Official Anthropic documentation, read in full July 12, 2026.** Companion
to [[claude-code-context-and-instruction-economics]], which covers memory
and caching. This page covers the operational layer: how sessions are
named, resumed, and branched; what triggers adding each extension type
(CLAUDE.md, skills, subagents, hooks, MCP, plugins); and where `.ROOT`'s
existing HANDOFF/DAILY discipline overlaps or diverges from Claude Code's
native session mechanics.

## One-paragraph summary

Claude Code sessions are named, resumable, and branchable objects backed by
local JSONL transcripts (`~/.claude/projects/<project>/<session-id>.jsonl`,
30-day retention by default) — a persistence layer `.ROOT` currently
duplicates by hand through markdown HANDOFF files, for a reason that still
holds: session resume is Claude-only and machine-local, while HANDOFF/DAILY
is the cross-engine (Claude/Codex) continuity layer, so the two serve
different audiences rather than one replacing the other. The extension
guide's real contribution is a **trigger table**: each of CLAUDE.md, skills,
subagents, hooks, MCP, and plugins has a recognizable moment that says
"add this now," which is a cleaner self-evolution heuristic than `.ROOT`
has previously had for deciding when a repeated pattern earns a new skill
or HAT file.

## Session mechanics

**Naming and resuming:**

| Command | Effect |
|---|---|
| `claude -n <name>` | Name a session at startup |
| `/rename <name>` | Name or rename during a session |
| `claude --continue` | Resume the most recent session in the current directory |
| `claude --resume` | Open the interactive session picker |
| `claude --resume <name>` | Resume a named session directly (exact match) or open the picker pre-filled with it (ambiguous) |
| `claude --from-pr <number>` | Resume the session linked to that PR |
| `/resume` / `/resume <name>` | Same, from inside an active session |

Unnamed sessions still get a default display name (`<dirname>-<2-char
suffix>`) as of v2.1.196+, but that default isn't a resume handle — only a
name you set explicitly works with `--resume <name>`.

**Session picker shortcuts:** `Ctrl+W` widens to all worktrees of the
repo, `Ctrl+A` widens to every project on the machine, `Ctrl+B` filters to
the current git branch, `Space`/`Ctrl+V` previews content without resuming.
Pasting a PR/MR URL into search finds the session that created it.

**Branching:** `/branch <name>` (or `--fork-session` from the CLI) copies
the conversation so far into a new session ID and switches into it, leaving
the original untouched and still resumable. Permissions approved with
"allow for this session" do **not** carry over to the branch — each fork
starts with its own clean approval state.

**Context control within a session:** `/clear` (empty context, old
conversation still resumable), `/compact [instructions]` (replace history
with a focused summary), `/context` (see what's consuming space right now).

**Scheduling — four options, matched to where the task needs to run:**

| Option | Runs where | Best for |
|---|---|---|
| Routines | Anthropic-managed cloud | Tasks that must run even when your machine is off; can trigger on API calls or GitHub events, not just a clock |
| Desktop scheduled tasks | Local machine, via desktop app | Tasks needing direct access to local files/uncommitted changes |
| GitHub Actions | CI pipeline | Repo-event-triggered or cron tasks that belong with workflow config |
| `/loop` | Current CLI session | Quick polling; stops on a new conversation, `--resume`/`--continue` restores unexpired loops |

`.ROOT` already has both ends of this covered — the `schedule` skill maps
to Routines, the `loop` skill maps to `/loop` — so this table confirms
existing usage rather than surfacing a gap.

## The extension trigger table

The single most reusable artifact in this chunk: a table of recognizable
moments that justify adding each feature, in the order most teams add them.

| Trigger | Add |
|---|---|
| Claude gets a convention or command wrong twice | CLAUDE.md entry |
| You keep typing the same prompt to start a task | User-invocable skill |
| You paste the same multi-step playbook a third time | Skill |
| You keep copying data from somewhere Claude can't see | MCP server |
| Claude reads many files hunting a symbol definition | Code intelligence plugin |
| A side task floods your conversation with output you won't need again | Subagent |
| You want something to happen every time, no exceptions | Hook |
| A second repo needs the same setup | Plugin |

This is a cleaner decision rule than "notice a pattern, build something" —
it names the *symptom* that should trigger each specific tool, which maps
directly onto this wiki's own charter to scan `.ROOT` for extractable
skills/tools/HATs.

## Feature comparison, condensed

- **CLAUDE.md vs. Skill**: CLAUDE.md is always-on, whole-project, best for
  "always do X" rules. Skills load on demand (description at session start,
  full content on invocation), best for reference material or a workflow
  triggered by `/<name>`.
- **Subagent vs. Agent team**: a subagent reports results back to the
  caller only, one-way; an **agent team** (experimental, disabled by
  default) is multiple independent Claude Code sessions that message each
  other directly and share a task list — for work needing discussion or
  competing hypotheses, not just isolated research. `.ROOT`'s heavy use of
  parallel forks for wiki/CASTLE ingestion matches the subagent model
  correctly (independent chunks reporting to one coordinator, no
  cross-fork communication) — agent teams would only become relevant if
  forks needed to negotiate with each other mid-task, which hasn't come up.
- **Hook vs. Skill**: a hook is deterministic — it always fires on its
  event and doesn't ask Claude to reason. A skill is interpreted — Claude
  decides how to apply it, and outcome can vary. Rule stated plainly:
  *"Put guardrails in hooks. An instruction like 'never edit `.env`' in
  CLAUDE.md or a skill is a request, not a guarantee."* This is the same
  advisory-vs-deterministic split the prior CASTLE ingest already promoted
  into `.ROOT` governance language (raw/ immutability, private-folder
  boundaries as deny rules, not prose).
- **Feature layering when defined at multiple levels**: CLAUDE.md is
  *additive* (all levels concatenate); skills/subagents/MCP servers
  *override by name* at defined priority (managed > user > project, with
  MCP using local > project > user); hooks *merge* (everything registered
  fires). Worth knowing precisely if `.ROOT` ever nests conflicting
  skill/HAT names across hubs.
- **Artifacts** ("publish session output as a private, interactive web
  page") are already in active use in this system (the `dataviz` and
  `artifact-design` skills) — no gap, just confirms the pattern is used as
  designed.

## Prompt-recipe patterns worth naming (not previously catalogued here)

- **`gh pr create` auto-links the session** to that PR; `claude --from-pr
  123` or pasting the PR URL into `/resume` search returns to exactly that
  work later. Not applicable today (no `.ROOT` GitHub-backed proof project
  yet) but a concrete pattern for when `02-LIBRARY\.PROJECTS` work goes to
  GitHub.
- **`@`-referencing a directory** shows a file listing, not contents —
  useful distinction from `@file`, which pulls full content plus that
  directory's CLAUDE.md.
- **Piping into scripts**: `git log --oneline -20 | claude -p "summarize
  these"` and `claude -p "..." --output-format json | your_command` are
  the CI/batch integration points — still no current `.ROOT` use case
  (confirmed, matches the existing "no CI/CD" disposition), but concrete
  if a proof project ever needs a pre-commit or scheduled batch pass.

## Why this matters for this wiki / `.ROOT`

- **HANDOFF/DAILY and native session resume solve different problems and
  should both stay.** Native resume (`--resume <name>`, `/branch`) is
  fast, precise, and free, but it's Claude-only and machine-local — Codex
  can't read a `.claude` session transcript. `.ROOT`'s
  HANDOFF/DAILY markdown files remain the only continuity layer that
  crosses engines and machines. The two are complementary: a Claude Code
  operator could *additionally* name sessions per work lane
  (`claude -n castle-weekly-sweep`) for faster same-machine resume, without
  touching the cross-engine handoff discipline at all. Not proposal-worthy
  on its own — worth trying informally first, before writing it into
  governance.
- **The extension trigger table is directly reusable** as the screening
  heuristic this wiki already claims to use ("scan for content that can be
  extracted into reusable skills, agent tools, or software components") —
  it gives concrete symptom-to-tool mappings instead of a vague mandate.
- **Agent teams are a genuine "watch" item, not an action item.** If
  parallel research forks ever need to challenge or coordinate with each
  other mid-task (e.g., two forks auditing the same governance change from
  different angles and reconciling live), that's the trigger to revisit
  this — currently out of scope since it's experimental and disabled by
  default.
- Companion page: [[claude-code-context-and-instruction-economics]] covers
  memory, caching, and the context-budget rationale these workflow patterns
  assume.

---
*Processed July 12, 2026. Source in raw/ (immutable).*
