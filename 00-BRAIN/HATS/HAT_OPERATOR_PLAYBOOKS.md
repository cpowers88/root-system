---
type: reference
tags: [reference, governance]
---

# HAT_OPERATOR_PLAYBOOKS.md — Operator Skill Scripts (on demand)
### Moved out of HAT_OPERATOR.md July 11, 2026 (slim pass). Load the one you need when its trigger fires — not at session start.
### Native Claude Code skills already exist for some of these: `session-close`, `profit-gate` (the castle gate), `atlas-brief`. Prefer the skill when running in Claude Code.

---

## SKILL: Strategy Session
Trigger: priorities, North Star alignment, business direction, weekly
planning, project sequencing, school/tech/business balance.
1. Load NORTH_STAR.md context + current school reality
2. Identify the active track (School → Tech → Solo Business — this order)
3. Give the critical path
4. Produce ONE decision or ONE next action
5. Park non-critical ideas; state what to log
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
Output: process map → friction inventory → quick wins → tool
recommendations → automation opportunities → retainer proposal.
Method file: 05-BUSINESS\01-Audit Templates\OBSERVATION_METHODOLOGY.md.
Rule: the audit is the first product. Software comes after the
workflow proves the need.

## SKILL: Technology Recommendation
Trigger: any "should I/they use X" — tool selection, software
purchase, build-vs-buy, AI adoption, stack decisions, client recs.
1. Load 02-LIBRARY\08-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md
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
2. Prune dead signals (⏸ 60+ days → 🗑), verify tiers on new entries
3. Promote at most ONE hot signal → run it through the castle gate
   (`00-BRAIN\CASTLE\wiki\decision-rules\adding-a-profit-skill.md`)
4. Log the verdict on the radar (✅ GATED with reason)
Rule: eyes, not hands — the tower never changes the roadmap directly.
Dark during danger weeks.

## SKILL: Ratchet Review
Trigger: quarterly review ONLY (or Chris explicitly calls it).
1. Load NORTH_STAR.md → The Ratchet + Revenue Milestones
2. For each floor: hit early? capability jump (AI included)? gated
   watchtower signal that survived?
3. Propose raised targets with reasons — Chris approves every turn
4. Record the turn (or the deliberate hold) in the quarterly review
Rules: floors ratchet UP only. Never mid-cycle. "The goal evolved"
outside a quarterly is scope creep wearing a costume — flag it.

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
   - Template / playbook → BUSINESS wiki (blank master) or 05-BUSINESS
   - Tool / code pattern → note in project docs + castle proof-project page
   - Case study / proof → 05-BUSINESS\03-Case Studies (when client-based)
   - Lesson worth keeping → handoff → weekly review promotion path
3. Update proof-project or Capability Library maturity when the evidence
   warrants it — draft to tested-internally needs a named test, not a vibe.
4. Archive inactive project material — archive, don't delete.
5. Record the next horizon and the single next action.
Rule: no engagement ends without the harvest question being asked. That's
step 9 of the service model — the portfolio step.
