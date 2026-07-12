---
domain: systems
type: case-study
tags: [priority/now, status/wiki-only, domain/systems, source-role/example, use-case/systems-analysis, use-case/process-design, use-case/client-interview, subject/system-dynamics, subject/project-management, subject/rework-cycle]
---

# Ingalls Shipbuilding: Quantifying Project "Ripple Effects" with the Rework Cycle

**Summary**: A $500M+ cost-overrun dispute between Ingalls Shipbuilding and the US Navy (1970s) was resolved using a system dynamics model that — for the first time in the industry — quantified how a customer's design changes could cause cost and schedule damage many times larger than their direct (re-drawing, re-engineering) cost, via a feedback structure centered on the "rework cycle." The case is Sterman's primary illustration of using a formal model to separate two parties' contributions to a shared problem, replacing pure finger-pointing with a structural accounting both sides could inspect and challenge.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 2 ("System Dynamics in Action"), section 2.3

**Last updated**: 2026-06-22

---

## The Dispute: Direct Costs vs. "Ripple Effects"

Ingalls Shipbuilding won contracts to build 30 Navy destroyers and 9 amphibious-assault ships (1969-70) under fixed-price contracts, then faced cost overruns eventually exceeding $500M (over $1.5B in 1999 dollars). Ingalls blamed the Navy's continuous stream of design changes (driven by rapidly advancing navigation, communications, and weapons technology); the Navy conceded it generated the changes but argued their cost impact was limited to the direct expense of redrawing specifications — dismissing claimed "ripple effects" as either nonexistent or the result of contractor mismanagement.

**Industry baseline context** (Cooper and Mullen 1993, a sample averaging 130,000-170,000+ person-hours per project): commercial projects ran 140% of budget and 190% of schedule; **defense projects ran 310% of budget and 460% of schedule** — overruns and delays of this magnitude are the norm for large projects, not an Ingalls-specific failure.

## The Core Mechanism: the Rework Cycle

The model's foundational structure (reused across nearly every subsequent project-dynamics model the field has built since): work flows from "to be done," through "being done," and splits into **work really done** (correct) or **undiscovered rework** (contains errors not yet caught). Average fraction of work done correctly the first time, from the underlying dataset: **68% for commercial projects, just 34% for defense projects** — meaning in defense work, roughly two-thirds of all initial work eventually needs rework. Errors are typically discovered only later, by a downstream phase or QA — Cooper and Mullen found an average **9-month rework-discovery delay**, a large fraction of total project duration.

**Customer specification changes act exactly like a quality failure**: a change makes previously-completed correct work obsolete, moving it from "work really done" back into "known rework" — but the affected phase must also *recall* work already passed downstream, which itself triggers cascading rework in phases that built on top of the now-obsolete work.

## Why Direct Costs Understate the True Damage: The Vicious Cycles

The model's key structural insight is that the *intended* corrective responses to falling behind schedule — overtime and hiring — each trigger an unintended, self-reinforcing side loop that undercuts the fix:

- **Overtime** (intended: more effective people-hours) → extended overtime causes fatigue/burnout → productivity and quality fall, undiscovered rework grows, *and* burnout drives attrition/transfer requests, shrinking the workforce — undercutting the very capacity overtime was meant to add.
- **Hiring** (intended: more people) → if the regional labor pool is thin relative to need, rapid hiring dilutes average experience and erodes recruiting standards just to fill seats — lowering average productivity and quality even as headcount rises.
- **Schedule compression** (working out of sequence to hit dates) → activities start before upstream deliverables (designs, specs, materials) are mature/stable → worksite congestion, coordination overhead, and rework from building on immature inputs.
- All three loops feed the same rework cycle, which is itself a positive feedback: lower quality → more undiscovered errors → more eventual rework discovered later → more schedule pressure → more of the same corrective measures → more side effects.

**The conclusion this structure supports**: a customer-driven design change's *direct* cost (redrawing one set of specs) can be a small fraction of its *total* cost once these cascading, cross-phase, cross-project effects (when projects share workforce, worksites, or management) are included — exactly the claim Ingalls needed to substantiate and the Navy disputed.

## The Modeling Process: Building Credibility Under Adversarial Scrutiny

Because the model had to survive cross-examination by the Navy's own hired experts, the team (Pugh-Roberts Associates, led by Ken Cooper) built in explicit discipline beyond typical project modeling: **pre-committed limits of reasonableness for every parameter** (never relaxed to improve the fit), **cross-section consistency checks** between different parts of the model, **"shock tests"** for robustness under extreme conditions, and **comparison of historical replication not just to confirm fit but specifically to find where the model needed improvement**.

**The counterintuitive result that won the case**: when the Navy's outside experts forced revisions incorporating their own preferred parameter estimates, **the claim value attributable to Navy design changes actually increased**, not decreased. This directly disproved the "garbage in, garbage out, the model was cooked" criticism — a model genuinely built to a preselected conclusion would not have survived its critics' own changes intact, let alone moved further in the claimant's favor. Goldbach (Ingalls): "For the first time the Navy saw that Ingalls had a credible case." The dispute settled for **$447 million** in June 1978, with the model estimated to have contributed $170-350M of that.

## A Reframe Worth Keeping Verbatim

Pre-model dispute resolution, per Goldbach: "just a bunch of finger-pointing... there was no way to separate the impact of government and contractor problems or examine the synergy between them." Post-model: "here are the things the contractor didn't do well and here are the things the government didn't do well, and here's how much each contributed." **This is the general value proposition of a structural model in any two-party dispute or diagnosis**: it converts an unresolvable blame argument into an inspectable, falsifiable accounting that both sides can challenge on its own terms — directly the same move Sterman flags in [[barriers-to-learning-and-virtual-worlds]] (the fundamental attribution error: blaming a person/party instead of examining the system structure both parties are embedded in).

## Long-Run Payoff: From Litigation Tool to Management Tool

The real value, per Sterman, isn't winning the lawsuit — by the time of litigation the damage is already done; litigation only allocates who pays. **The larger value is using such models proactively, before the damage happens.** Ingalls itself used descendants of the model on every subsequent program. Rich Goldbach (who later ran Metro Machine shipyard) commissioned a similar model for ongoing bidding and used it interactively with the Defense Contract Audit Agency itself — "she can ask us to run any set of assumptions, and we usually get the answer back in an hour." His own description of the lasting change: "I never had the ability I think I got from working with system dynamics to ask 'how will this decision ripple out?' ... Now I ask how customers, employees, suppliers and so on will react to what we might do... It permeates every aspect of my thinking."

## Connects to

- [[barriers-to-learning-and-virtual-worlds]] — the pre-model "finger-pointing" dynamic is a direct illustration of the fundamental attribution error (blaming the other party rather than examining the shared system structure); the model itself functions as exactly the "virtual world" the chapter argues is necessary when intuition can't track multi-loop dynamics.
- [[policy-resistance-and-feedback-thinking]] — overtime and hiring's unintended side effects are textbook policy resistance: the intended (negative/balancing) loop is real, but it triggers an unintended (positive/reinforcing) loop that undercuts it.
- [[causes-of-variability-breakdowns-setups-rework]] — Factory Physics's rework-as-nonpreemptive-outage formula is the queueing-theory cousin of this case's rework cycle; both treat rework as structurally identical to a capacity-reducing disruption, not just an added cost line.
- [[gm-auto-leasing-case-study]] — both cases use a formal model specifically to overturn a "blame the external party / blame the market" mental model with a structural account of internally-generated dynamics.

## North Star Connection

- How this applies to the audit business: the rework-cycle structure (overtime → burnout → attrition; hiring → diluted experience; schedule compression → out-of-sequence work) is a directly reusable diagnostic checklist for any client project (construction, software, fabrication) running behind schedule — specifically useful for distinguishing genuine capacity shortfalls from self-inflicted vicious cycles created by the client's own corrective responses to being behind.
- Track relevance: Business / Systems — directly applicable to construction/field-service project audits (the entry-hypothesis market) and a strong KSU/ISYE case study in project dynamics.
- Possible future Second Brain use: a "rework cycle diagnostic" (where is undiscovered rework hiding, what's the discovery delay, is overtime/hiring/compression currently being used as a fix) is a strong candidate audit-checklist artifact for any client project-management engagement.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The rework-cycle and vicious-cycle structures are directly applicable to construction project audits — Chris's entry-market hypothesis |
| Current usefulness | 5 | The overtime/hiring/compression side-effect checklist is immediately usable in a project-management audit |
| KSU support | 5 | Canonical project-dynamics case study, directly supports systems engineering / project management coursework |
| Tech-stack relevance | 1 | Conceptual case study, no direct tool dependency |
| Business audit value | 5 | The "convert finger-pointing into structural accounting" reframe is a sharp, generally applicable consulting technique beyond this specific case |
| Data/workflow value | 3 | The rework/undiscovered-rework tracking concept could inform a real client data-collection approach (tracking rework discovery delay) |
| Reading urgency | 4 | High-value case, directly tied to the construction/field-productivity entry market |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Project-management audit diagnostic — when a client project is behind schedule or over budget, use the rework-cycle structure and the overtime/hiring/compression vicious-cycle checklist to distinguish genuine capacity shortfalls from self-inflicted dynamics created by the client's own corrective responses.

**Use when**:
A construction, fabrication, or project-based client describes a "death spiral" of falling further behind despite (or because of) overtime, rapid hiring, or schedule compression — or when a client is in a two-party dispute (with a subcontractor, customer, or vendor) over whose fault delays/overruns are.

**Do not use when**:
The client's schedule problem is a single, isolated, well-understood cause (e.g., one late material delivery) with no compounding rework or resource-dilution dynamic — the full rework-cycle framing would overcomplicate a simple fix.

**Fast retrieval query**:
`subject/rework-cycle` + `subject/project-management` — or search "Ingalls Navy shipbuilding claim" / "rework cycle undiscovered rework" / "ripple effects design changes" / "finger-pointing structural accounting"
