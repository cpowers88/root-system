---
type: decision-rule
timeline: reference
reference_priority: supporting
status: active
tags: [decision-rule, scope-control]
---

# Decision Rule: Adding a Profit Skill

**Trigger**: Any new "this could be highly profitable" idea — a skill, tool, market,
side hustle, or digital-asset concept — from Chris, an AI session, or any source.
**Owner**: Chris decides; AI applies the gate and flags, never silently adopts.

## The Rule

Before applying the gate or creating anything, search both [[skill-map]] and
[[opportunity-queue]] for the idea or an equivalent signal. Update an existing row
instead of creating a duplicate.

A new profit skill enters the [[skill-map]] only if ALL five pass:

1. **No-orphan test** (NORTH_STAR.md): the idea must serve at least one of: a fixed
   commitment, an active capability gap named in a live phase, a real workflow or
   project already underway, employability tied to the current degree, or a current
   strategy assumption (S-01–S-05) it would generate evidence for. A general appeal
   to North Star alignment alone does not pass — name the specific phase, project,
   or assumption. If profit is claimed, name the economic mechanism and the evidence
   needed. "Might be useful someday" fails.
2. **Source test**: at least one Tier 1–2 source preserved in the owning evidence
   home (and linked from [[source-map]] only when it is roadmap-relevant)
   supports the claim that this skill produces income for someone in Chris's
   position. Tier 4 hype (Reddit threads, YouTube income claims, X posts) can
   trigger the question but can never pass this test by itself.
3. **Phase test**: it names the live phase it serves. If that phase is more than
   two quarters away, it does not enter the skill map. A checkable activation
   condition may trigger an earlier bounded test only when new evidence satisfies
   tests 1, 2, 4, and 5 and Chris approves the exception. Otherwise, if the idea
   has permanent evidence and is worth retaining, keep or add one
   [[opportunity-queue]] row with status `parked`; otherwise create no page.
4. **Displacement test**: name what it displaces. Time is fixed (full-time school,
   family of nine). If nothing can be displaced, it waits.
5. **Proof test**: a concrete proof project can be stated in one sentence. If the
   proof can't be named, the skill isn't ready to be learned.

**Timing advisory**: during the high-load school window or a heavy semester,
name the school commitment and displacement cost, recommend park/scope-down when
appropriate, then follow Chris's decision.

## Why This Rule Exists

NORTH_STAR.md names the operating risks: ideas are not commitments, planning can
imitate progress, and time is the constraint. This rule makes that defense
mechanical while leaving the active vehicle open to replacement by stronger proof.

## Worked Example

*Idea (July 2026): "Day trading — there's a whole shelf of books in 02-LIBRARY."*
1. No-orphan: serves no fixed commitment, active gap, live workflow/project,
   degree-linked employability need, or current strategy assumption — **fail**.
2. Source: books exist (Tier 2) but support a different career, not this roadmap — fail.
Verdict: **parked** (which is exactly where those books already are). Two failures,
no page, no time spent. The rule took 60 seconds.

*Counter-example that PASSES: "Report-generation pipeline (Markdown → PDF)."*
Serves an active reporting capability gap in Phases 3–5, the BUSINESS/PYTHON
evidence homes cover it, the phase is near, it displaces a lower-value formatting
task, and proof is one real report rendered and used. → skill map.

## When to Break It

Chris may authorize a bounded exception after an explicit impact/displacement review.
Record the override, proof sentence, stop condition, and next review. AI never grants
it silently.
