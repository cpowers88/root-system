---
type: proposal
tags: [ai-automation, proposal, governance, workflow]
timeline: parked
---

# Proposal: Make the HIGH-Flag-Before-Close Rule a Hook, Not Just Prose

**Status: PENDING CHRIS / CASTLE REVIEW**

## Friction / Drift Observed

`.claude\skills\session-close\SKILL.md` (lines 38–39) states: "If a HIGH
flag was raised this session, it must be fixed or explicitly handed to
Chris before closing (SYSTEM_FLAGS.md rule)." This is prose inside a skill
file — advisory, not enforced. Nothing currently stops a session from
running the close sequence and skipping this check entirely.

Today's Claude Code ingest confirmed the relevant distinction precisely
(see [[claude-code-workflows-and-sessions]] — "Hook vs Skill"): *"Put
guardrails in hooks. An instruction like 'never edit `.env`' in CLAUDE.md or
a skill is a request, not a guarantee."* A skill is interpreted — Claude
decides how to apply it, and outcome can vary. A hook is deterministic — it
always fires on its event. The HIGH-flag rule is exactly the kind of "must
hold 100% of the time, no exceptions" guarantee the docs say belongs in a
hook, not skill prose — and it currently isn't one.

## Files Touched

A new or existing Claude Code hook (`.claude\hooks\` or equivalent, if
`.ROOT` doesn't have a hooks directory yet, this proposal would need to
establish one) that fires at session-close time (or on stop/before-compact,
whichever event Claude Code's hook system actually exposes for this) and
checks `00-BRAIN\SYSTEM_FLAGS.md`'s OPEN FLAGS table for any row still
tagged HIGH with no "handed to Chris" note, blocking or warning if found.

## Why Better Than Status Quo

Removes reliance on a session remembering to check its own flag-raising
against a rule stated only in prose. Matches `.ROOT`'s own already-adopted
principle (raw/ immutability and 88-JOURNAL protection are already deny
rules, not prose, for exactly this reason) to a rule that currently isn't
implemented the same way.

## Risk / Blast Radius

Needs Codex or Chris to design the actual hook mechanics (Claude Code's
hook system and its available trigger events weren't covered in today's
ingest depth — this proposal identifies the gap and the target file, not
the implementation). Moderate risk if implemented carelessly (a
false-positive block on session close would be worse than the current
gap), so this should go through the normal Codex-audits/Claude-Code-executes
lane sequence rather than a quick patch.

## Source Basis

[[claude-code-workflows-and-sessions]] — "Hook vs Skill" section.
`.claude\skills\session-close\SKILL.md` lines 38–39 (the rule currently
unenforced).
