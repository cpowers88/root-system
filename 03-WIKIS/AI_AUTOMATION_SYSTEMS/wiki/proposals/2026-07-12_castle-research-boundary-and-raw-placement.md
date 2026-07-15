---
type: proposal
tags: [ai-automation, proposal, governance, castle]
---

# Proposal: Enforce CASTLE's Research Boundary + Add a `raw/` Placement Rule

**Status: APPROVED & APPLIED July 12, 2026** — resolved with the
`WHERE_IT_GOES.md` raw-intake rule alone (relocate to the correct wiki's
`raw/` before processing, no in-place ingest — kept at its original,
stricter wording; a proposed loosening was considered and explicitly
declined by Chris). No `OPERATIONS.md` change was made — the
`WHERE_IT_GOES.md` rule fully closes the gap on its own.

**Standing practice established alongside this**: raw-file retirement
(removing a source once its derived `.md` content has fully absorbed it) is
a judgment call to flag when noticed, not an automated rule — except the
Claude Code and OpenAI/Codex documentation packs, which are a standing
exception and should never be retired regardless of how complete the
derived wiki pages are (they get re-consulted directly, not just
summarized once). Checked `00-BRAIN\CASTLE\raw\` as of this session: empty
of content (both docs packs already relocated to `AI_AUTOMATION_SYSTEMS\raw\`
earlier today) — nothing currently retirement-eligible.

## Friction / Drift Observed

Two linked findings from today's full-system instruction audit.

**1. CASTLE did its own stated out-of-scope work this morning.**
`00-BRAIN\CASTLE\OPERATIONS.md` states plainly that CASTLE "is not the
landscape-research or self-evolution layer" and that `AI_AUTOMATION_SYSTEMS`
"researches AI tooling, agent patterns" — explicitly not CASTLE's job. But
this morning CASTLE did exactly that: ingested both the Claude Code and
OpenAI docs packs *in place* inside `00-BRAIN\CASTLE\raw\books\`, wrote full
source-summaries (`claude-code-docs-pack-2026-07.md`,
`openai-platform-docs-pack-2026-07.md`), and applied engineering claims into
`FINAL_ROOT_LAUNCH_OPTIMIZATION_REPORT_2026-07-12.md` — AI_AUTOMATION_SYSTEMS's
exact charter, executed by CASTLE instead. This isn't theoretical; it's this
session's own timeline, and it's also *why* both packs needed a same-day
correction — they were ingested in the wrong lane before being relocated.

**2. No placement rule exists for source material dropped into `CASTLE\raw\`.**
`WHERE_IT_GOES.md`'s routing rule is otherwise correct ("new AI/LLM/agent
research routes to AI_AUTOMATION_SYSTEMS," already stated) — the rule isn't
missing at the *research* level. What's missing is a rule at the *raw
intake* level: nothing says "if AI-tooling/agent-pattern source material
lands in `CASTLE\raw\`, relocate it to the correct wiki's `raw/` before
processing — don't ingest in place." `vault_map.md`'s CASTLE entry doesn't
even list a `raw\` subfolder as part of CASTLE's documented structure, yet
it's now been used twice as a de facto AI-tooling intake point.

## Files Touched

- `00-BRAIN\WHERE_IT_GOES.md` — add a raw-intake rule: source material
  appearing in `00-BRAIN\CASTLE\raw\` that matches a `03-WIKIS` hub's
  charter (e.g., AI/LLM/agent docs → AI_AUTOMATION_SYSTEMS) gets relocated
  to that hub's `raw/` *before* any processing, not ingested in place.
- `00-BRAIN\CASTLE\OPERATIONS.md` — either reinforce the existing boundary
  language with a concrete "if raw material shows up here that belongs to a
  wiki's charter, route it there first" step, or explicitly scope an
  exception for time-sensitive triage reads (Chris's call on which).
- `00-BRAIN\vault_map.md` — note CASTLE's `raw\` subfolder exists and what
  it's actually for (triage/staging, not a permanent intake lane).

## Why Better Than Status Quo

Closes the exact gap that caused today's double mis-placement (both docs
packs, same failure, same day) and makes CASTLE's own stated research
boundary self-enforcing at the point material first arrives, rather than
relying on a later audit to catch the lane violation after real work has
already happened in the wrong place. Companion to
[[2026-07-12_governance-drift-detection]] — that proposal catches stale
*claims*; this one catches misplaced *raw intake* before it produces any.

## Risk / Blast Radius

Low-moderate. Touches two-to-three governance files. No existing content
removed — this is a gap-fill, not a rewrite. `OPERATIONS.md`'s scope
carve-out (if any) needs Chris's judgment on how much triage latitude CASTLE
should keep for genuinely time-sensitive material.

## Source Basis

`00-BRAIN\CASTLE\OPERATIONS.md` (existing boundary language), `00-BRAIN\WHERE_IT_GOES.md`
(existing routing rule, missing raw-intake layer), `00-BRAIN\vault_map.md`
(CASTLE structure, missing `raw\`), and this session's own two-pack
mis-placement incident as the live evidence.
