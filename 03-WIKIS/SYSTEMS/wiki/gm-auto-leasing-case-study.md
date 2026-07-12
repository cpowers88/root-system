---
domain: systems
type: case-study
tags: [priority/now, status/wiki-only, domain/systems, source-role/example, use-case/systems-analysis, use-case/business-model, use-case/client-interview, subject/system-dynamics, subject/feedback-loops, subject/automotive-industry]
---

# GM Auto Leasing Case Study: How a Carmaker's Own Policy Created Its Competitor

**Summary**: General Motors used a rapid system dynamics modeling process (1995-1996) to discover that the booming used-car-superstore industry wasn't an external threat — it was an endogenous consequence of the industry's own short-term leasing policies. The case is Sterman's primary illustration of how a narrow "new cars only" mental model produces a multi-billion-dollar blind spot, and how a fast, iterative, client-embedded modeling process can change it before the damage fully lands.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 2 ("System Dynamics in Action"), section 2.2

**Last updated**: 2026-06-22

---

## The Setup: A Threat That Looked External

In the mid-1990s, used-car superstores (CarMax, AutoNation) grew from nothing to $13 billion in sales by 1998, stocked with clean, late-model used cars. The prevailing industry mental model — at GM, Ford, and elsewhere — was that new and used cars were **two separate markets**: "There are really two markets — new and used" (Ford executive, *Wall Street Journal*, 1994). Under that model, superstores were simply an external competitive threat to be defended against.

GM's Decision Support Center (DSC), led by Nick Pudar working with consultant Mark Paich, built a system dynamics model in a single afternoon-and-evening sprint — deliberately kept simple to be completed in time and explainable clearly — to test that mental model before committing to any response.

## The Dynamic Hypothesis: Leasing Manufactures Its Own Disruption

The model's key move was refusing to let trade-in cars "disappear" from the model boundary the way the industry's mental model did. Instead, trade-ins flow into a stock of **late-model used cars** that doesn't vanish — it ages, gets resold, and competes directly with new cars for the same buyers.

**The mechanism, traced through the feedback loops** (see [[policy-resistance-and-feedback-thinking]] for the loop-type vocabulary):

- Two *intended*, well-understood balancing loops made leasing attractive in the short run: shorter lease terms shorten the trade-in cycle and directly boost new-car sales (**Lease Term loop, B4**), and lease subvention (cutting payments by inflating assumed residual values) makes new leases more attractive (**Lease Incentive loop, B3**).
- But these loops ignored a third, **long-delayed structure (roughly the length of the lease term itself)**: as the volume of leases grew, a wave of high-quality, low-mileage off-lease cars flooded the used market on a delay of 2-4 years. This depressed used-car prices, which pulled some new-car buyers into the used market instead (**Used Car Market loop, B5**), lengthened the average trade-in cycle for the whole population (**Used Car Quality loop, B6**), and — worst of all — fed back into lease-end behavior itself: when market value fell below the contracted residual, customers had no reason to exercise their buy option, so cars flowed back to the lessor in even greater numbers, depressing prices further still (a **self-reinforcing positive loop, R1, the Purchase Option loop**).
- **The punchline**: "Used car superstores were only the symptom of a deeper problem — the leasing policies of the carmakers." The superstores were the market's *response* to an oversupply the manufacturers themselves had created by shortening trade-in cycles industry-wide. There was no external shock; the system manufactured its own disruptor.

## Why the Industry Missed It: A Long Delay Plus a Narrow Model Boundary

The carmakers weren't being careless — they were reading real, contemporaneous evidence that *confirmed* the wrong model: used car sales and prices were rising 6%+/year through 1995, "ample evidence" cited by Ford's own sales executives and outside analysts that the used market could "easily absorb" the volume coming off lease. **The data were real; the causal story behind them was wrong** — the price rise was partly a temporary blip from superstores stocking up their own new lots, masking the structural glut about to arrive. This is a textbook instance of [[barriers-to-learning-and-virtual-worlds]]'s warning about confounding variables: the same data supported two completely different causal stories, and only a model that explicitly included the delayed feedback loop could discriminate between them.

**The communication tool that made the insight land**: rather than presenting the full causal-loop diagram to brand managers, Pudar built a simple "bathtub" metaphor — production fills the tub of new-car-substitutes, sales drain it, but the inflow from expiring leases **cannot be turned off** once sold, regardless of price. During a recession, that fixed inflow collides with falling demand, forcing deeper production cuts and price cuts than a model without the delayed lease-return structure would predict. **This is a directly reusable communication technique**: translate a multi-loop causal diagram into a single physical metaphor (a tub with an uncontrollable inflow) for an audience that won't sit through the full diagram.

## Policy Outcome and the Verification

GM shifted incentive structures toward longer lease terms (36-48 months), eliminated 2-year leases, declined to raise residual values despite pressure from brand managers citing the (temporarily) strong used market, and moved to full accrual of residual risk in reserves.

**The outcome validated the model against real competitors who didn't change course**: when the predicted glut hit in 1997, Ford Credit's profits fell 28% ($410M) on off-lease losses; GMAC's fell less than 4%, and overall GMAC profit *rose* 6%. Ford and Nissan tried to prop up wholesale prices by paying dealers to *not* return off-lease cars for auction — which only shifted where the oversupply sat, since dealer auction-purchases fell by the same amount the retained cars would have added. **By 1998 Ford and other makers belatedly followed GM's lead away from short-term leasing.**

## Connects to

- [[policy-resistance-and-feedback-thinking]] — this case is a worked, dollar-quantified instance of the "there are no side effects, only effects we failed to model" principle; the used-car glut wasn't a side effect of leasing, it was leasing's actual, designed-in delayed output.
- [[barriers-to-learning-and-virtual-worlds]] — the industry's misreading of rising used-car prices as confirming evidence (rather than a temporary confound) is a direct real-world instance of the confounding-variables barrier (1.3.3).
- [[owner-dependency-diagnostic|the Gap Method & Comfort Zone diagnostic]] — GM's willingness to act counter to industry consensus and short-term pressure from its own brand managers parallels Gerber's point that real strategic change requires confronting the organization's own comfort zone, not just market conditions.

## North Star Connection

- How this applies to the audit business: this is the cleanest available illustration of "the symptom your client is fighting may be a delayed output of their own past policy, not an external threat" — directly reusable framing for any client blaming a competitor, market shift, or "industry headwinds" for a problem that traces back to their own prior decisions on a multi-year delay. The bathtub-metaphor communication technique is a directly reusable client-presentation tool.
- Track relevance: Business / Systems — core systems-thinking case study, demonstrates the modeling process itself (small fast model → iterate → policy analysis → management flight simulator) as a template for audit engagements.
- Possible future Second Brain use: the "bathtub diagram" technique (stock with an uncontrollable, delayed inflow) is a strong candidate for a reusable client-communication template whenever a delayed feedback structure needs to be explained to a non-technical audience.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | A complete, dollar-quantified worked example of the exact diagnostic error (narrow model boundary + delayed feedback) an audit engagement exists to catch |
| Current usefulness | 4 | Directly reusable framing and communication technique (the bathtub metaphor) for client conversations |
| KSU support | 4 | Strong applied system dynamics case study; less formula-heavy than later chapters but excellent for dynamic-hypothesis methodology |
| Tech-stack relevance | 1 | No direct tool dependency — conceptual/case-study chapter |
| Business audit value | 5 | "Your problem may be your own delayed policy, not the market" is a sharp, well-evidenced client argument |
| Data/workflow value | 2 | Describes a data-gathering and iterative-modeling process but doesn't itself specify a reusable data method |
| Reading urgency | 3 | Valuable but secondary to the chapter's other two cases for immediate audit applicability |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Client-communication tool — when a client attributes a recurring problem to an external market force, use this case (and the bathtub metaphor) to probe whether the "external" pressure is actually a delayed output of the client's own prior policy.

**Use when**:
A client blames competitors, "the market," or industry trends for a problem that has a plausible multi-year lag from an internal decision (pricing, staffing, inventory, contract terms).

**Do not use when**:
The client's problem genuinely has no internal-decision lag structure — a truly exogenous shock (e.g., a new regulation, a one-time supply disruption) doesn't fit this pattern and forcing it will read as overcomplicating.

**Fast retrieval query**:
`subject/automotive-industry` + `subject/feedback-loops` — or search "used car superstores GM leasing" / "bathtub diagram leasing" / "gone today here tomorrow"
