---
type: proposal
tags: [ai-automation, proposal, governance, reference]
---

# Proposal: Adopt the Extension Trigger Table in AGENT.md / CLAUDE.md

**Status: APPROVED & APPLIED July 12, 2026** — added to `AGENT.md` as its
own section (single source of truth, per CASTLE review); `CLAUDE.md` §
Skill and Tool Discovery updated to point at it rather than duplicate it.
Applying this also surfaced a related trim: `AGENT.md`'s Graph Color
Maintenance section was demoted to a new `graph-colors` skill (mirrored in
`.claude/skills/` and `.agents/skills/`) as an example of the table's own
"rarely-needed procedure → skill" logic applied to `AGENT.md` itself.

## Friction / Drift Observed

`AGENT.md`'s Wikis/CASTLE Boundary and `00-BRAIN\CLAUDE.md`'s "Skill and Tool
Discovery" section both describe *who* builds skills/HATs/tools in `.ROOT`
(Claude Code, on approval) but neither states a concrete *symptom* that
should trigger building one. The system currently relies on a session
noticing a "high-value reusable pattern" by judgment call alone.

Today's Claude Code docs ingest surfaced a cleaner, directly reusable
decision rule (see [[claude-code-workflows-and-sessions]] — "The extension
trigger table"): a table of recognizable moments, one per extension type,
each naming the exact symptom that justifies adding it —

| Trigger | Add |
|---|---|
| Claude gets a convention or command wrong twice | CLAUDE.md entry |
| You keep typing the same prompt to start a task | User-invocable skill |
| You paste the same multi-step playbook a third time | Skill |
| You keep copying data from somewhere Claude can't see | MCP server |
| A side task floods your conversation with output you won't need again | Subagent |
| You want something to happen every time, no exceptions | Hook |
| A second repo needs the same setup | Plugin |

This maps directly onto this wiki's own stated charter ("actively scan for
content that can be extracted into reusable skills, agent tools, or software
components") but gives it a concrete trigger instead of a vague mandate.

## Files Touched

`00-BRAIN\AGENT.md` and/or `00-BRAIN\CLAUDE.md` Section 2 — add the table
(or a `.ROOT`-adapted version of it) as the named heuristic for "when does a
repeated pattern earn a skill/HAT/hook," replacing or supplementing the
current judgment-only language.

## Why Better Than Status Quo

Turns "notice a pattern, maybe build something" into a checkable symptom →
tool mapping. Doesn't change who has authority to build (still Claude Code,
still needs approval per existing rules) — only sharpens when a session
should flag the opportunity in the first place.

## Risk / Blast Radius

Low. Additive table, no existing rule removed. Touches one or two
already-loaded governance files, so keep it short — the table above is
seven rows.

## Source Basis

[[claude-code-workflows-and-sessions]] — "The extension trigger table"
section.

## Post-Change Check (added 2026-07-15, check_at discipline)

- **Expected behavior:** repeated symptoms route to the smallest matching extension per the AGENT.md trigger table, instead of ad-hoc skill/hook creation or the same friction recurring with no extension at all.
- **Evidence for improvement or regression:** any extension created after 2026-07-12 names its trigger-table row; recurring symptoms in DAILY/flags map to a considered row. Regression = an extension with no table match, or a symptom repeating three-plus times with no extension decision.
- **check_at:** 2026-08-24 (enough post-change extension decisions and semester-start friction will have accumulated)
- **Outcome:** (blank until the check date — record what actually happened, with an evidence link)
- **Verdict:** (keep / modify / revert — blank until the check date)
