---
tags:
  - phase-3
  - strategy
  - human-agent
  - delivery
---

# Human Role Redesign

> The change-management half of every engagement: moving client staff from manual production into supervision, exception handling, and system improvement — without losing the knowledge in their heads.

## Purpose
Define how client employees transition when AI takes over first-pass work: what their jobs become, how to design the transition so staff cooperate instead of resist, and how to sell role redesign as part of every implementation.

## Key Idea
Every automation project is secretly a **job redesign project**. The hours AI removes from a person's week don't disappear — they get reallocated, and *how* they're reallocated decides whether the system survives. The redesign pattern:

> **Producer → Reviewer → Improver.** The person who used to type the quotes now reviews AI-drafted quotes and handles the weird ones; six months later they're the one updating the quote rules and training new hires on the system.

Staff who see this path become the system's champions. Staff who see replacement become its saboteurs — and sabotage is trivially easy (just stop using it). Adoption failure — one of the deadliest entries in [[risks-and-failure-modes|Risks & Failure Modes]] — is usually role-redesign failure.

## Why It Matters
- **Knowledge preservation.** The 15-year admin knows every exception, every difficult customer, every unwritten rule. Cut her without capturing that knowledge and the shiny new system fails on cases she handled invisibly. Role redesign converts tribal knowledge into the rules, prompts, and SOPs the system runs on — she becomes the [[agent-manager-job-design|knowledge-base maintainer]], and she's finally *documented*.
- **Owner economics.** The honest pitch is capacity, not headcount: "your team handles 40% more volume without hiring," not "fire two people." SMB owners mostly don't want to fire loyal staff anyway — giving them the growth framing removes their private objection.
- **Your accountability.** You designed the system; the redesigned roles are its operating manual. A build handed to unre-designed roles is a build set up to decay.

## The Redesign Method (Per Workflow)
For each workflow the [[smb-ai-audit-method|audit]] targets:
1. **Name the current owner** of the manual work and their hours/week on it.
2. **Classify the tasks** with the [[human-agent-operating-model|Human-Agent Operating Model]] — what goes AI-first, what stays human-only, what becomes review work.
3. **Write the new role card:** what they review, what they escalate, what they update, what they're now free to do (usually: more customer contact, more selling, more field work — revenue work).
4. **Capture their knowledge first:** interview them for the exception rules *before* go-live; their expertise seeds the prompts and SOPs.
5. **Give them the improvement lever:** they log what the AI gets wrong and either fix the rule or flag it for you. People support systems they can correct.
6. **Report the shift to the owner:** hours moved from production to revenue/judgment work is a headline metric in the [[case-study-template|case study]].

## Practical Actions
- Add a "who owns this workflow today, and what do they become?" row to your audit findings table — every recommendation names the human transition.
- Build the one-page **role card template** (reviews / escalates / updates / newly freed for) and include one per affected employee in implementation proposals.
- In staff interviews, say the design out loud early: "the goal is that you stop doing the typing and start managing the system that does it." Watch cooperation change.

## Beginner Version
On small quick-win projects, the "redesign" is one conversation and one role card: the affected staffer knows what to check, what to escalate, and who to tell when the AI is wrong. Even that minimal version doubles adoption odds.

## Intermediate Version
Role redesign is a named line item in every implementation SOW: role cards, a knowledge-capture interview per affected role, one training session, and a 30-day adoption check with usage metrics reported to the owner ([[fulfillment-system|Fulfillment System]] handoff step).

## Advanced Version
Role redesign becomes a sellable workshop/consulting layer: org-level redesign for clients automating multiple departments, career-path design for their staff ("operator → agent manager → process designer"), and train-the-trainer programs so client teams onboard their own hires onto the systems. This is high-margin work no tool vendor can offer.

## Revenue Connection
Role redesign is priced into implementations (it's real work), it protects the retainer (adopted systems renew; sabotaged systems churn), and it creates the training and staff-support deliverables inside [[retainer-model|retainer tiers]]. Indirectly it's the biggest LTV protector in the model: the #1 cause of quiet churn is staff abandoning the system.

## Human-Agent Management Connection
This page is the *transition path* into the new job layer: the specific mechanics of moving a client's people into the [[agent-manager-job-design|agent-manager roles]], with the [[human-agent-operating-model|operating model]] deciding what their new work is and [[quality-control-and-risk-gates|gates]] defining what they review.

## Risks / Failure Modes
- **Redesign skipped under budget pressure:** the build ships, nobody's role changed, the system decays unused. Warning sign: no named system owner on the client side. Prevention: role cards are non-optional in the SOW.
- **Client insists on replacement, not redesign:** knowledge walks out before it's captured. Prevention: at minimum, sell the knowledge-capture interviews before any staffing change. If the client refuses entirely, weigh it as a [[what-not-to-do|bad-fit signal]].
- **Overpromising job security:** you design roles; the owner makes employment decisions. Never promise staff outcomes you don't control — frame as "this is the role the system needs," not "your job is safe."

## Related Pages
- [[agent-manager-job-design|Agent Manager Job Design]] — the destination roles in detail
- [[human-agent-operating-model|Human-Agent Operating Model]] — the classification behind the redesign
- [[fulfillment-system|Fulfillment System]] — where role cards and training land in delivery
- [[risks-and-failure-modes|Risks & Failure Modes]] — adoption failure and knowledge loss
