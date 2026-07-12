---
type: research
tags: [ai-automation, claude-code, context-management, instruction-files, self-evolution]
source: raw/CLAUDE_FILES/ (Anthropic official docs, moved from CASTLE raw/ to this wiki July 12, 2026 — Best_Practices_for_Claude_Code, STORE__INSTRUCTIONS_AND_MEMORIES, EXPLORE_CLAUDE_CONTEXT_WINDOW, HOW_CLAUDE_CODE_WORKS, PROMPT_CACHING)
---

# Claude Code — Context, Memory, and Instruction-File Economics

**Official Anthropic documentation, read in full July 12, 2026.** A prior
CASTLE ingest (`00-BRAIN\CASTLE\wiki\source-summaries\claude-code-docs-pack-2026-07.md`)
already mined the high-level architecture claim (three-tier instruction
system, <200-line budget) that drove the July 11 system self-review. This
page goes one layer deeper into the mechanics that summary only partially
covered — especially prompt caching, which was previously "read in part" —
because `.ROOT` is itself a large, self-editing instruction-file system and
the exact rules for when an edit takes effect are directly load-bearing.

## One-paragraph summary

Claude Code carries two memory channels across sessions — CLAUDE.md files
(human-written, loaded in full every session) and auto memory (Claude-written
notes, capped at 200 lines / 25KB for the index file) — both delivered as
context, never as enforced configuration, so anything that must hold 100% of
the time belongs in a hook, not a memory file. The most consequential
mechanic missed by the first pass: **editing a CLAUDE.md file mid-session
does not take effect until `/clear`, `/compact`, or a session restart** —
the file is read once at launch and held in memory, so a session that edits
its own governance files keeps operating on the pre-edit version for the
rest of that session, even though the edit is safely on disk.

## The two memory channels

| | CLAUDE.md | Auto memory |
|---|---|---|
| Who writes it | You | Claude |
| Loaded into | Every session, in full | Every session, first 200 lines / 25KB of `MEMORY.md` only |
| Storage | Wherever you place the file | `~/.claude/projects/<project>/memory/` — one directory per git repo, shared across worktrees, machine-local |
| Scope | Managed policy > user (`~/.claude/CLAUDE.md`) > project (`./CLAUDE.md`) > local (`./CLAUDE.local.md`) | Per repository |
| Best for | Coding standards, workflows, architecture | Build commands, debugging insights, preferences Claude discovers on its own |

Auto memory's own structure — a concise `MEMORY.md` index plus separate
topic files loaded on demand — is the same index/detail-file split `.ROOT`'s
own memory system (`memory/MEMORY.md` + topic files, described in this
session's system prompt) already implements by hand. **This is worth a
self-evolution note**, not a change: `.ROOT`'s memory system was built
before or independent of native auto memory and follows nearly the same
shape voluntarily. Whether the two should be reconciled, kept parallel, or
one deprecated in favor of the other is a live open question, not yet
proposal-ready.

## CLAUDE.md mechanics not in the prior summary

- **HTML comments are stripped before injection.** Block-level `<!-- maintainer notes -->` comments in a CLAUDE.md file never enter Claude's context — they cost zero tokens — but remain visible to a human opening the file directly, or to Claude via the Read tool. `.ROOT`'s governance files could carry human-only annotations (e.g., "why this rule exists," review-due dates) this way without taxing every session.
- **Load order is root-to-leaf, not override.** All discovered CLAUDE.md files concatenate into context rather than replacing each other; files closer to the working directory are read *last*, so they take precedence when instructions conflict. Nested/subdirectory CLAUDE.md files load on demand, only when Claude reads a file in that subdirectory — this is the exact mechanic `.ROOT`'s hub-routing pattern (root `CLAUDE.md` → lane file → hub `CLAUDE.md`) already depends on, now confirmed at the API level rather than inferred from behavior.
- **`@path` imports recurse up to 4 hops** and are skipped inside code fences (wrap a path in backticks to mention it without importing it). Imported files still load in full at launch — imports organize, they don't reduce token cost.
- **`AGENTS.md` is not read by Claude Code** — only `CLAUDE.md`. Teams that want one shared instruction file for multiple agent tools import `AGENTS.md` from `CLAUDE.md` (`@AGENTS.md`) or symlink it. `.ROOT` already handles this correctly by convention rather than by this exact mechanism: Codex reads its own `AGENTS.md`/`CODEX.md` lane, Claude Code reads `CLAUDE.md`, and `AGENT.md` (singular, `.ROOT`'s own universal OS filename) is a different file from Anthropic's `AGENTS.md` multi-agent standard — worth noting only so the naming similarity is never mistaken for the same mechanism.
- **`.claude/rules/` supports path-scoped instructions** (`paths:` frontmatter, glob-matched) that load only when Claude reads a matching file, and can be shared across projects via symlink. `.ROOT` has no direct equivalent, but its per-hub `CLAUDE.md` files (loaded only when working in that hub) already achieve the same context economy at folder granularity — true path-scoped rules would only add value if a single `.ROOT` folder needed different rules for different file types within it, which hasn't come up.

## Prompt caching — the mechanics the prior pass missed

Prompt caching matters here because it explains *when a governance edit
actually takes hold*, not just how Claude Code manages cost.

**How it works:** every message is a fresh API call that resends the full
prior context plus what's new. The API caches by exact-prefix match — system
prompt, then project context (CLAUDE.md, auto memory, unscoped rules), then
the growing conversation. A change anywhere in the prefix invalidates
everything after it; there is no per-file caching.

**Actions that invalidate the cache** (next turn is slower/costlier while it
rebuilds): switching models, changing effort level, toggling fast mode,
connecting/disconnecting an MCP server *when its tools are loaded into the
prefix rather than deferred*, enabling/disabling a plugin that provides an
MCP server, denying an entire tool by bare name, compacting the conversation,
upgrading Claude Code. Resuming a session after an upgrade is the worst case
— it reprocesses the entire history with zero cache hits, cost scaling with
how long the resumed conversation is.

**Actions that keep the cache** (and, critically, why some edits don't take
effect immediately): editing files in the repo, changing output style,
changing permission mode, invoking skills/commands, `/recap`, `/rewind`
(truncates back to an already-cached prefix), spawning a subagent (builds
its own separate cache). And the one that matters most here:

> **Editing CLAUDE.md mid-session keeps the cache — and also doesn't apply.**
> Project-root and user-level CLAUDE.md are read once at session start and
> held in memory. An edit during the session neither invalidates the cache
> nor changes Claude's behavior; Claude keeps working from the version
> loaded at launch. The new content only takes effect on the next `/clear`,
> `/compact`, or restart. (Source: `PROMPT_CACHING.md`, "Editing CLAUDE.md
> mid-session" — confirms and sources the mechanic exactly; not stated this
> precisely in `HOW_CLAUDE_CODE_WORKS.md` or `Best_Practices_for_Claude_Code.md`,
> which is why the prior "read in part" pass missed it.)
>
> Nested CLAUDE.md files and `paths:`-scoped rules behave differently: if
> edited *before* they've loaded (i.e., before Claude reads a matching file
> that session), the edit takes effect normally. Once loaded, they're part
> of conversation history like anything else — a later edit doesn't
> retroactively change what's already in context.

**Cache lifetime:** five minutes by default on API-key billing; Claude Code
requests the one-hour TTL automatically on a Claude subscription (free,
since usage is plan-included) but drops back to five minutes once a session
draws on overage usage credits. **Cache scope is per machine *and*
directory** — the system prompt embeds working directory, platform, and git
branch/status, so two sessions in different directories, or two sequential
sessions where the git state changed, don't share a cache even on the same
machine.

## Context window shape (from the interactive walkthrough)

Before any prompt is typed, five things load in this order: system prompt
(~4.2K tokens, invisible), auto memory MEMORY.md (~680 tokens), environment
info, MCP tool *names* only (schemas deferred), skill *descriptions* only
(full content on invocation), then CLAUDE.md files. A subagent — including
every fork this wiki uses for parallel research — gets its **own fresh
copy** of the parent's CLAUDE.md loaded into its own context (except the
built-in Explore/Plan agents, which skip it for a smaller footprint); none
of that counts against the parent's context, but it does mean a heavy root
CLAUDE.md is a tax paid again by every subagent spawned. This is a point in
favor of keeping `.ROOT`'s root `CLAUDE.md` pointer-only, as it already is
— every fork spawned across every wiki pays that cost, so its size
multiplies with fork count.

**What survives `/compact`:** system prompt and output style (unchanged,
not part of history), project-root CLAUDE.md and auto memory (re-injected
from disk), invoked skill bodies (re-injected, capped at 5,000 tokens/skill
and 25,000 total, oldest dropped first). **What's lost until re-triggered:**
path-scoped rules and nested CLAUDE.md files (reload only when a matching
file is read again), and the skill *description* listing itself (only
skills actually invoked survive — the catalog of what's available doesn't).

**Capacity note:** Sonnet 5 — the model this session runs on — has a native
1M-token context window with no special flag required. The <200-line
instruction-file discipline is therefore a *quality* lever (adherence drops
as always-loaded files grow, independent of whether they'd technically fit)
rather than a hard capacity workaround. Worth remembering next time a
"just make the file bigger, there's room" argument comes up — there being
room isn't the constraint being managed.

## Why this matters for this wiki / `.ROOT`

- **The mid-session-edit gotcha is the single highest-value finding in this
  batch.** `.ROOT` sessions routinely edit their own boot-chain files
  (`AGENT.md`, lane `CLAUDE.md`s, `CHRIS_CORE.md`) and then keep working —
  today's own correction pass did exactly this. Per the mechanic above, the
  editing session itself never runs under its own edits; only the *next*
  session (or a `/clear`/`/compact` within the same one) actually picks them
  up. This is worth a governance note, not urgent enough alone to justify a
  formal proposal on its own, but real: a session that both edits governance
  and needs to *verify* the new behavior in the same sitting should `/clear`
  or start fresh rather than trusting its own live state.
- **Auto memory vs. `.ROOT`'s hand-built memory system** is a genuine
  architecture question worth a future self-evolution rep: is `.ROOT`'s
  memory/ directory duplicating a now-native capability, complementary to
  it (broader scope, cross-session narrative vs. auto memory's
  per-repo tactical notes), or should one inform the other's design going
  forward? Flagged here as an open question, not resolved.
- **HTML-comment stripping** is immediately usable: any `.ROOT` governance
  file can carry human-only rationale in `<!-- -->` blocks at zero context
  cost — useful for "why" notes that would otherwise bloat the always-loaded
  budget just to explain a rule that's already stated concisely.
- **Root `CLAUDE.md` staying pointer-only is validated harder than before**:
  every subagent/fork this wiki (and the rest of `.ROOT`) spawns re-pays the
  full CLAUDE.md cost in its own separate context, so a bloated root file
  wouldn't just tax the main session — it would tax every fork on top of it.
- Companion page for workflow/session mechanics: [[claude-code-workflows-and-sessions]].
  Existing CASTLE summary for the architecture-level claim this page goes
  deeper on: `00-BRAIN\CASTLE\wiki\source-summaries\claude-code-docs-pack-2026-07.md`.

---
*Processed July 12, 2026. Source in raw/ (immutable).*
