---
type: proposal
tags: [ai-automation, proposal, governance]
timeline: reference
---

# Proposal: Mid-Session Governance-Edit Discipline

**Status: APPROVED & APPLIED July 12, 2026** — added to `AGENT.md` § File
Safety, immediately after the "System files include..." line, as agreed
wording (kept general to all system files, not just governance files).

## Friction / Drift Observed

Confirmed mechanic, sourced exactly to `PROMPT_CACHING.md`'s "Editing
CLAUDE.md mid-session" section (see [[claude-code-context-and-instruction-economics]]):
project-root and user-level CLAUDE.md files are read once at session start
and held in memory. **Editing one mid-session neither invalidates the cache
nor changes the session's behavior** — the session keeps operating on the
version loaded at launch. The edit only takes effect on the next `/clear`,
`/compact`, or restart.

`.ROOT` sessions routinely edit their own boot-chain governance files —
`AGENT.md`, lane `CLAUDE.md`s, `CHRIS_CORE.md` — and then keep working in
the same sitting, including verifying the new behavior. Per the mechanic
above, the editing session itself never actually runs under its own edit;
only a later session (or an explicit `/clear`/`/compact` within the same
one) picks it up. This is a real, current gap: nothing in `AGENT.md` states
this, so a session has no reason to know its own "verification" of a
governance edit it just made is running against stale, pre-edit behavior.

## Files Touched

`00-BRAIN\AGENT.md` — a short addition to whatever section already covers
self-editing of governance files (or a new short rule if none exists),
along these lines:

> Editing a boot-chain governance file (AGENT.md, a lane file, CHRIS_CORE.md)
> mid-session does not take effect for that session — the file was already
> loaded at launch and stays cached until `/clear`, `/compact`, or a
> restart. A session that both edits governance and needs to verify the new
> behavior in the same sitting should `/clear` or start fresh rather than
> trusting its own live state.

## Why Better Than Status Quo

Without this, a session can edit a rule, believe it verified the new
behavior, and be wrong — silently. The fix is one paragraph and prevents a
specific, mechanically-confirmed failure mode from recurring unnoticed.

## Risk / Blast Radius

Trivial. One short addition to `AGENT.md`, no behavior change to anything
except making an already-true mechanic visible in governance text. No other
files affected.

## Source Basis

[[claude-code-context-and-instruction-economics]] — "Prompt caching — the
mechanics the prior pass missed" section, sourced exactly to
`PROMPT_CACHING.md`.

## Post-Change Check (added 2026-07-15, check_at discipline)

- **Expected behavior:** system/governance files are edited only with explicit approval, never silently mid-task; mid-session improvement ideas get recorded separately instead of applied on the spot.
- **Evidence for improvement or regression:** the July 15 remediation-and-design sprint is the richest test window — every governance edit (Codex phases, Claude chunks) should carry an explicit Chris approval in the DAILY. Regression = any governance diff with no matching approval record.
- **check_at:** 2026-07-29 (immediately after the sprint's governance-heavy window closes)
- **Outcome:** (blank until the check date — record what actually happened, with an evidence link)
- **Verdict:** (keep / modify / revert — blank until the check date)
