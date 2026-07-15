---
type: proposal
tags: [ai-automation, proposal, workflow]
---

# Proposal: Explicit "What Should Be Captured" Step in Session-Close

**Status: APPROVED & APPLIED July 12, 2026** — added to both
`.claude\skills\session-close\SKILL.md` and `.agents\skills\session-close\SKILL.md`
(kept byte-identical, confirmed the right call since this skill has no
per-engine parameterization, unlike `atlas-brief`).

## Friction / Drift Observed

Claude Code's official prompt library includes a card named
`capture-what-to-remember`: an explicit end-of-session prompt asking what
Claude had to figure out this session that the next session shouldn't have
to re-derive, with a proposal for what to write down before it's lost (see
[[claude-code-prompt-library-patterns]]).

`.ROOT`'s session-close ritual (`.claude\skills\session-close\SKILL.md`)
already does the mechanical parts of this — append a DAILY block, update
wiki logs, refresh `NOW.md` — but Step 1 ("DAILY block") asks for "what was
done, files touched, next action," which is a *record of activity*, not an
explicit prompt for *what's worth remembering that isn't obvious from the
diff*. The two aren't the same question: a session can correctly log every
file it touched and still fail to flag the one non-obvious thing it learned
along the way (a gotcha, a dead end, a judgment call that needs to be
visible to the next session).

## Files Touched

`.claude\skills\session-close\SKILL.md` — a small addition to Step 1, or a
new short step between the existing Step 1 and Step 2:

> Before writing the DAILY block, ask explicitly: *is there anything this
> session had to figure out, get wrong once, or decide by judgment call that
> the next session (or Chris) would otherwise have to re-derive from
> scratch?* If yes, name it in the DAILY block even if it doesn't fit neatly
> into "what was done."

## Why Better Than Status Quo

The current close ritual captures *what happened*; this closes the gap for
*what would otherwise be silently lost*. Low cost — one explicit question
added to a step that already runs at the end of every meaningful session —
and it's the exact mechanism a vendor's own prompt library names as
effective for this purpose.

## Risk / Blast Radius

Trivial. One short addition to an existing skill file; no change to any
other file, no change to when session-close triggers.

## Source Basis

[[claude-code-prompt-library-patterns]] — "Candidate `.ROOT` mappings"
section, `capture-what-to-remember` card.
