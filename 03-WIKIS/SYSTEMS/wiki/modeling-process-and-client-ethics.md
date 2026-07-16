---
domain: systems
type: method
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/client-interview, use-case/audit, use-case/process-design, subject/system-dynamics, subject/consulting-ethics, subject/modeling-process]
---

# The Modeling Process: Managers as Designers, Identifying the Real Client, and the Modeler's Ethical Line

**Summary**: Why the highest-leverage work is organizational *design* (not piloting), how to correctly identify "the client" (not the sponsor, not the gatekeeper, but whoever must change behavior for the work to matter), the five-step modeling process and why it's iterative rather than linear, and the explicit ethical line a modeler must hold even at the cost of the engagement.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 3 ("The Modeling Process"), sections 3.1-3.4

**Last updated**: 2026-06-22

---

## Pilots vs. Designers: Where the Real Leverage Sits

Forrester's framing question: who's most important to an aircraft's safe operation — the pilots, or the designers? Most people say pilots; the real answer is designers, because a well-designed aircraft is "stable, robust under extreme conditions," and flyable safely by an *ordinary* pilot even stressed or tired. **Managers play both roles simultaneously** — they are pilots (making individual decisions: hiring, pricing, launch timing) and designers (shaping the organizational structures, strategies, and decision rules that determine how *all* decisions get made). Sterman's direct critique: **"too many managers, especially senior managers, spend far too much time acting as pilots... rather than creating an organizational structure consistent with their vision and values."**

**The audit-relevant translation**: a client fixing one bad decision is acting as a pilot; a client who redesigns the process/incentive/information structure that produced that decision is acting as a designer. An audit engagement's highest-leverage output is rarely "make this one decision better" — it's identifying which structural redesign would make many future decisions, by ordinary people under stress, come out right by default. This is the same point Sterman makes about positive feedback loops (see [[policy-resistance-and-feedback-thinking]]): dynamics emerge from structure, and structure is the actual lever.

## Identifying the Real Client (Not the Sponsor)

A precise, non-obvious distinction worth keeping verbatim: **"The client is not the person who brings you in to an organization or champions your work, nor even the person who pays for the modeling study, though it is helpful to have contacts, champions, and cash. Your clients are the people you must influence for your work to have impact. They are those people whose behavior must change to solve the problem."** The client can be a CEO or a machine operator; can be an individual, a group, or an entire community; the client group can also expand or change as the project proceeds (directly echoed by [[dupont-maintenance-game-and-twelve-principles]], where Ledet discovered his real client group was thousands of mechanics, not the management team that had commissioned the study).

**The corollary discipline this creates**: modeling work must be focused on what actually "keeps the clients up at night" — not on the elegance of the model or the modeler's own theoretical interests. If the client doesn't perceive the model as addressing their real concern, the work has no impact regardless of its technical quality.

## The Ethical Line: When to Push Back, and When to Quit

Focusing on client needs does **not** mean being a hired gun. Sterman draws a sharp, explicit line: a modeler has a responsibility to make clients justify their opinions and ground their views in data — and to **"speak truth to power,"** telling clients their most cherished beliefs are wrong if that's what the analysis shows, "even if it means you will be fired." If a client pushes for a preselected result not supported by the analysis, push back. **"If your clients' minds are closed, if you can't convince them to use modeling honestly, you must quit. Get yourself a better client."** This is stated as a professional obligation, not an optional preference — directly relevant to any audit engagement where a client wants the report to confirm a decision they've already made.

## The Five-Step Process — and Why It's a Cycle, Not a Checklist

The five canonical steps (Table 3-1 in the source): (1) **Problem Articulation** (boundary selection — what's the problem, what time horizon, what's the historical/expected behavior pattern); (2) **Formulation of a Dynamic Hypothesis** (an endogenous theory of the problem's cause, mapped via causal-loop or stock-flow diagrams); (3) **Formulation of a Simulation Model** (specifying structure, decision rules, and parameters); (4) **Testing** (against historical reference modes, under extreme conditions, and for parameter sensitivity); (5) **Policy Design and Evaluation** (scenario testing, "what-if" analysis, robustness, and policy interaction effects).

**The explicit warning against treating this as a linear sequence**: "Modeling is a feedback process, not a linear sequence of steps... Iteration can occur from any step to any other step." Insight gained at the testing stage routinely sends you back to revise the problem articulation itself. The whole process is also explicitly nested inside the single-loop/double-loop learning structure from [[policy-resistance-and-feedback-thinking]]: experiments in the model (the "virtual world") inform real-world experiments, and real-world feedback in turn revises the model and the mental models behind it — an ongoing cycle, never a one-shot deliverable. **"Modeling is not a one-shot activity that yields The Answer."**

## Connects to

- [[model-validation-and-testing-practice]] — extends the five-step modeling cycle
  into a complete, reproducible test battery and prospective outcome assessment.
- [[operations-research-study-lifecycle]] — carries problem definition and joint
  inquiry through maintained application, operating ownership, and implementation.
- [[barriers-to-learning-and-virtual-worlds]] — the iterative model/real-world cycle described here is the practical, project-level implementation of that chapter's single-loop/double-loop learning and virtual-world concepts.
- [[dupont-maintenance-game-and-twelve-principles]] — Sterman's twelve principles (especially #6, joint inquiry not advocacy; #7, avoid black-box modeling) are the direct operational consequences of this page's client-identification and ethics discussion.
- understanding-resistance-faces-and-underlying-concerns — the "speak truth to power, even if it costs the engagement" stance parallels Block's insistence (Flawless Consulting) that authentic consulting requires being willing to say things the client doesn't want to hear.
- [[owner-dependency-diagnostic|the Gap Method & Comfort Zone diagnostic]] — Forrester's pilots-vs-designers distinction is a sharper, more general version of Gerber's on/in-the-business diagnostic: both identify the same failure mode (working at the decision level instead of the structure level) from different angles.

## North Star Connection

- How this applies to the audit business: the client-identification discipline ("not who pays you, but who must change behavior") is directly applicable to every audit engagement — a contractor-owner who hires Chris is rarely the only person whose behavior needs to change, and identifying the full client group early (estimators, foremen, dispatchers) shapes what the deliverable actually needs to be. The ethics line is a useful pre-commitment to set before any engagement that might surface an uncomfortable finding for the person paying the invoice.
- Track relevance: Business — core consulting-practice methodology, directly complementary to the Flawless Consulting material already in the wiki.
- Possible future Second Brain use: the "who is the real client" question and the explicit ethics commitment are both strong candidates for inclusion in a standalone engagement-kickoff checklist or contracting document.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Core consulting methodology directly applicable to every future engagement |
| Current usefulness | 4 | The client-identification question is immediately usable in any engagement scoping conversation |
| KSU support | 3 | Methodology content, less quantitative than the modeling-technique chapters |
| Tech-stack relevance | 1 | Conceptual chapter, no tool dependency |
| Business audit value | 5 | The pilots-vs-designers framing and the explicit ethical line are both strong, reusable client-facing arguments |
| Data/workflow value | 1 | Process/ethics content, not a data method |
| Reading urgency | 3 | Foundational but less urgent than the case studies already ingested |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Engagement-scoping tool — use the "who is the real client" question at the start of any engagement to map the full set of people whose behavior must change, not just whoever is paying; use the pilots-vs-designers framing to redirect a client focused on a single decision toward the structural redesign that would make many future decisions come out right.

**Use when**:
Scoping a new engagement, or when a client's request is framed entirely around fixing one decision/incident rather than the structure that produced it.

**Do not use when**:
The client's issue genuinely is a single, isolated decision with no recurring structural cause.

**Fast retrieval query**:
`subject/consulting-ethics` + `subject/modeling-process` — or search "pilots vs designers Forrester" / "who is the real client system dynamics" / "speak truth to power modeling" / "get yourself a better client"
