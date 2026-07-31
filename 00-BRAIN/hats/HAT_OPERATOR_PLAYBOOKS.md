---
type: reference
timeline: reference
tags: [governance]
---

# HAT_OPERATOR_PLAYBOOKS.md — Operator Skill Scripts (on demand)
### Moved out of HAT_OPERATOR.md July 11, 2026 (slim pass). Load the one you need when its trigger fires — not at session start.
### Shared native skills exist for some procedures: `session-close`, `profit-gate`, and `atlas-brief`. Use the shared skill on any surface where it is available.

---

## SKILL: Strategy Session
Trigger: priorities, North Star alignment, business direction, weekly
planning, project sequencing, school/tech/business balance.
1. Load NORTH_STAR.md + current school reality; add CURRENT_STRATEGY.md only for a
   business/market/offer/revenue decision
2. Reconcile fixed commitments, the semester technology/business floor, urgent revenue evidence, and the highest-value remaining action
3. Give the critical path
4. Produce ONE decision or ONE next action
5. Preserve non-critical ideas without letting AI-generated tangents replace the requested decision
Rule: strategy exists to produce action, not more strategy.

## SKILL: Business Workflow Audit
Trigger: contractor workflow, field productivity, business audit,
operations review, process mapping, client offer, retainer proposal.
Three systems questions on every process:
```
Where does state live?
Where does feedback live?
What breaks if I delete this?
```
Friction patterns: waiting, rework, double entry, tribal knowledge,
manual handoffs, spreadsheet-as-database, text/email as system of
record, missing feedback loop.
Output: process evidence → friction and consequence → smallest justified
recommendation → next decision.
Method file: 05-BUSINESS\01-Audit Templates\OBSERVATION_METHODOLOGY.md.
Rule: under the current strategy, a concise observation audit is the first-offer
hypothesis. Implementation or retained support must be earned by evidence; "change
nothing" or "simplify what exists" may be the correct outcome.

## SKILL: Technology Recommendation
Trigger: any "should I/they use X" — tool selection, software
purchase, build-vs-buy, AI adoption, stack decisions, client recs.
1. Load 02-LIBRARY\REF-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md
2. Name the category (1–12) the problem belongs to
3. Walk the Recommendation Ladder top-down: eliminate → simplify →
   use what they own → configure → integrate → build light → build
   real. Never skip a rung.
4. Check need signals vs. waste signals for that category
5. State the rec with numbers: cost, hours saved, payback
6. "Don't buy anything" is a valid, complete deliverable
Rule: the cheapest software is the software you don't buy.
Vendor neutrality is the moat — sell the ladder, not a product.

## SKILL: Field Notes Capture
Trigger: Chris observes a real workflow, business problem, field
issue, or operational failure.
Capture: what was observed / where / who by role only / what was
slow, broken, manual, repeated, or missing / signal type
(Build / Sell / Both / Neither) / connected track / next action.
Output: FIELDNOTES_DATE_TOPIC.md → 05-BUSINESS\02-Field Notes\

## SKILL: File / Drive Session
Trigger: file creation or rewrite, Drive cleanup, folder review,
maps, templates, handoffs, 00-BRAIN work, system prompts.
1. Apply all File Safety rules (AGENT.md) — read before write,
   search before create, archive not delete, parent chain by name
2. Produce the requested artifact
3. Report what changed; note unresolved risks
Rule: file safety can block work. Scope commentary cannot.

## SKILL: Watchtower Sweep
Trigger: weekly review, or Chris says "sweep the tower."
1. Open `...projectSuccess\radar.md`
2. Reject rows missing a new external change, material consequence, evidence home,
   or review trigger; prune dead signals and verify tiers
3. Promote at most ONE hot signal → run it through the castle gate
   (`00-BRAIN\CASTLE\wiki\decision-rules\adding-a-profit-skill.md`)
4. Log the verdict and bounded test; after execution, return the measured outcome
   and affected CURRENT_STRATEGY assumption/milestone
Rule: eyes, not hands — the tower never changes the roadmap directly. During
the high-load school window, warn once before optional expansion, then follow
Chris's direction.

## SKILL: Ratchet Review
Trigger: quarterly review or Chris explicitly requests a target review.
1. Load NORTH_STAR.md → The Ratchet, plus CURRENT_STRATEGY.md assumptions/milestones
   and only material Watchtower rows with completed tests
2. Separate the fixed destination from the vehicle; compare measured outcomes to
   the active assumptions and floors
3. Propose keep/refine/replace decisions and any earned higher floor — Chris approves
4. Record the decision, evidence, displacement, and next check date
Rule: autonomous AI does not quietly change targets. Chris may directly
authorize a mid-cycle change after an impact review.

## SKILL: Project Kickoff
Trigger: any build, project, or engagement starting — including personal
builds (tracker, POL) and CASTLE proof projects.
1. Define the outcome and success criteria in one sentence.
2. Name the owner realm and deadline.
3. Search archives, wikis, and templates for a reusable packet before writing
   anything new — update-over-create applies to project setup too.
4. Capture current thinking, open questions, and likely failure modes.
5. Name the smallest provable slice — not the whole project.
Rule: a kickoff that skips the reuse search is how the vault ends up with two
half-built versions of the same thing.

## SKILL: Project Completion & Asset Harvest
Trigger: any build, project, or engagement reaching done — including
personal builds (tracker, POL).
1. Confirm the outcome against the kickoff's success criteria, with evidence.
2. Ask the harvest question: what reusable asset did this produce?
   - Template / playbook → BUSINESS wiki (blank master) or reusable/sanitized 05-BUSINESS asset
   - Tool / code pattern → note in project docs + castle proof-project page
   - Case study / proof → separate client workspace while client-specific; approved sanitized version → 05-BUSINESS\03-Case Studies
   - Lesson worth keeping → handoff → weekly review promotion path
3. Update proof-project or Capability Library maturity when the evidence
   warrants it — draft to tested-internally needs a named test, not a vibe.
4. Archive inactive project material — archive, don't delete.
5. Record the next horizon and the single next action.
Rule: no engagement ends without the harvest question being asked. That's
step 9 of the service model — the portfolio step.
