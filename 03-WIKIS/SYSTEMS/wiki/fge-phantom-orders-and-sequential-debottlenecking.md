---
domain: systems
type: case-study
tags: [priority/now, status/wiki-only, domain/systems, source-role/example, use-case/systems-analysis, use-case/supply-chain, use-case/audit, subject/system-dynamics, subject/phantom-orders, subject/bottleneck-management, subject/sequential-debottlenecking]
---

# Fast Growth Electronics: Why Your Hottest-Selling Product Ends Up as Your Biggest Inventory Write-Down

**Summary**: A real, $3-billion-impact McKinsey/system-dynamics engagement at a high-velocity computer/electronics manufacturer ("FGE") solves a genuinely counterintuitive puzzle — why a product selling far better than expected ends up generating massive excess inventory, exactly like a slow-moving dud. The mechanism, "phantom orders," is a precise, two-loop positive feedback that any high-growth, allocation-prone supply chain is vulnerable to — and the case closes with "sequential debottlenecking," a reusable methodology for sequencing improvement effort in a fast-growing system where today's fix simply relocates tomorrow's constraint.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 18 ("The Manufacturing Supply Chain"), section 18.3-18.4 (chapter complete)

**Last updated**: 2026-06-22

---

## The Setup: A Company Succeeding on the Surface, Straining Underneath

"Fast Growth Electronics" (FGE) was genuinely thriving — units shipped grew ~50%/year, revenue ~40%/year, net income ~60%/year, market share climbing steadily — while internally, growth had outrun the company's order-processing, forecasting, production-planning, and procurement systems (SKU count grew **35x in five years**). Delivery dates were routinely revised; commitments were met through "expediting and other last-minute heroics"; quarterly sales targets produced a severe "hockey stick" pattern (sales concentrated in the last days of each quarter). One of FGE's largest customers delivered the case's most quotable verdict: **"You're the best supplier we deal with, but you're first in a race of pigs."**

**Why traditional analysis stalled**: months of conventional consulting work generated a long list of plausible-sounding fixes (Table 18-2 in the source: cut restaging delays, cut planning cycle time, improve launch predictability, get real-time sales data, build to order, resolve credit holds earlier...) but **no clear root cause and no obvious priority order** — each policy had genuine logic and real-world precedent behind it, several conflicted with each other (shrinking procurement lead times conflicted with supplier-qualification procedures; cutting expediting reduced marketing flexibility), and the organization had a ready supply of explanations to dismiss any specific past failure ("we were just growing too fast," "that was the worst case," "we solved that one already") — **paralysis, not action, was the actual risk.**

## The Genuinely Counterintuitive Puzzle: Why Do Hot Products Generate Excess Inventory?

**Slow-moving products generating excess inventory is straightforward** — sales fall short of the forecast used to set build volumes, and a natural reluctance to cut the forecast (plus long planning-system lags) lets the resulting surplus accumulate. **But the model surfaced something that contradicted the organization's own intuition**: a product selling so well it "flies off the shelves" — a product **you literally cannot make fast enough** — also ends up generating excess inventory at the end of its life. The model's dynamic hypothesis (Figure 18-19/18-20 in the source) explains the mechanism precisely:

1. A hot product's strong initial sales rapidly depletes channel inventory, forcing channel partners to order more from FGE.
2. The surge depletes FGE's own inventory; shipments fall below requirements; the product goes on **allocation**; delivery delay rises (the **Availability** balancing loop, B2 — a negative loop that *should* self-correct, but operates on a lag).
3. **Two reinforcing loops then take over, both individually rational from the channel partner's perspective**: **Order Ahead (R1)** — as lead time stretches (say 2 to 4 weeks), the channel partner needs proportionally more product "in the pipeline" just to sustain its desired order backlog, by Little's Law — so it orders *more*, stretching lead time further, in a closing positive loop. **Order Defensively (R2)** — as delivery reliability falls, the channel partner raises its own desired safety stock as a hedge, adding still more to the backlog, further degrading reliability, closing a second positive loop.
4. **The combined effect is a surge of "phantom orders"** — orders placed not because of real underlying customer demand, but purely in reaction to growing scarcity itself. FGE (like most suppliers) could not distinguish phantom orders from genuine demand, since point-of-sale data on actual end-customer purchases wasn't shared — and channel partners, if asked, would insist every unit ordered was genuinely needed.
5. Eventually FGE's restaged production catches up; shipments rise; delivery delay falls; the product comes off allocation. **The same two loops now reverse direction**: with short, reliable lead times, channel partners cancel the remaining phantom orders and liquidate the defensive safety stock they no longer need — a self-reinforcing **collapse** of the order backlog.
6. **The final, decisive mismatch**: production, materials commitments, and supplier contracts were all ramped up to meet the (phantom-inflated) order surge, and — because of long planning lags — **continue running for some time after real demand for the surge has already evaporated**, leaving FGE "holding a mountain of excess inventory at the end of the product's life," for a product that, by every demand signal available in real time, looked like an unambiguous success story.

## Building and Testing the Model — A Methodological Template Worth Keeping

The team (led by experienced practitioner Nathaniel Mass, working with McKinsey and FGE) spent roughly **2 weeks interviewing** purchasing managers, materials planners, and other supply-chain decision-makers, plus running multiple 1.5-day workshops with cross-functional decision-makers to elicit the structure — directly the same group-model-building discipline emphasized in [[modeling-process-and-client-ethics]]. **A deliberate scope decision worth keeping as a standing modeling principle**: the model focused on *dynamic* complexity (interdependencies and feedback among channel, FGE, and suppliers) rather than *detail* complexity — no attempt to model every SKU; thousands of components were grouped into just seven categories by cost/lead-time/attribute profile. The full model still ran to roughly **500 stocks** — large, but purpose-built rather than encyclopedic.

**The validation test was unusually rigorous, and worth keeping as a model for how to actually stress-test a client deliverable**: the model had to replicate **both** a real slow-moving product's history *and* a real hot product's history **without changing any structural parameters between the two cases** — only the assumed pattern of underlying final demand was allowed to vary. **This is a much harder bar than ordinary historical curve-fitting**, and it paid off directly: the model was run on the still-live hot product *before* its outcome was known, and it correctly predicted that the existing backlog would soon flip into a large excess-inventory position — which then actually happened. **The single most important organizational consequence of this validation**: because the same unmodified structure explained both product types, FGE's management could see "the sources of the surplus inventory problem were deeply embedded in the structure of the supply chain and were not the result of bad decisions made by particular managers" — redirecting the engagement from blaming individuals toward redesigning the system, the same blame-to-structure conversion seen repeatedly across this entire ingest.

## Policy Analysis: Why the "Obvious" Fixes Underperformed, and Why Combining Them Created Real Synergy

**Counter to many participants' prior expectations, simulating individual policies in isolation found that improving forecast accuracy or launch predictability had only average impact, and reducing the quarterly "hockey stick" pattern had a weak effect.** The standalone analysis instead identified **reducing supply-chain response delays themselves** as the highest-leverage lever. **But the more important finding was about combinations, not single policies**: jointly implementing materials lead-time reduction, planning-cycle-time reduction, and a build-to-order policy together produced **synergy exceeding the sum of their individual benefits** — because shorter lead times reduce the *frequency* of initial shortages, which directly weakens both phantom-order loops (R1 and R2) simultaneously, which stabilizes channel orders, which improves FGE's own forecast accuracy, which reduces late restaging and raw-material shortages, which improves delivery reliability further still — **the same vicious cycle, running in reverse as a virtuous one**, with each improvement compounding the next.

**A second, separate vicious cycle was identified and is worth keeping as a standalone diagnostic in its own right**: financial pressure from accumulated "sludge" inventory pushed managers to **cut initial materials staging** for new products — individually rational, since (treating demand as exogenous) a smaller initial commitment seemed to simply reduce the downside risk if the product turned out to be a slow mover. **But smaller initial staging directly increased the odds of an early shortage** — which triggers the phantom-order mechanism, which forces expensive late restaging, which produces *even more* surplus inventory and *even more* financial pressure to cut future staging further. **The model's counterintuitive, high-leverage recommendation directly inverted the organization's instinct**: *larger* initial staging of critical materials could actually *reduce* total life-cycle inventory costs, by preventing the shortage that triggers the whole downstream cascade.

## Sequential Debottlenecking: Why "Fix the Current Bottleneck" Isn't Enough in a Fast-Growing System

**The implementation challenge the team faced**: the full set of recommended changes amounted to a complete redesign of order processing, production planning, logistics, supplier management, and production — too large to implement all at once, requiring a sequencing strategy. **Conventional bottleneck theory** (Goldratt's Theory of Constraints — see [[owner-dependency-diagnostic|the Gap Method & Comfort Zone diagnostic]] and the broader TOC material already in this wiki) says focus improvement effort on the *current* binding constraint, since effort spent elsewhere is wasted. **The team's key refinement, specific to a high-growth context**: in a rapidly expanding company, relaxing today's bottleneck doesn't just improve throughput — it **enables further growth that creates a brand-new bottleneck somewhere else**, in a recurring sequence (materials acquisition → MRP cycle time → build-time → forecast accuracy → ...). **Waiting for each new bottleneck to become visible before attacking it (reactive debottlenecking) measurably slows growth and erodes competitiveness relative to using the model to anticipate which constraint comes next and redesigning it proactively** — the source's own labeled comparison (Figure 18-24) shows model-anticipated debottlenecking sustaining materially faster, less volatile growth than reactive attack-as-they-emerge debottlenecking. **This sequential-debottlenecking method is a directly reusable planning technique whenever an audit recommends a multi-phase improvement program for a still-growing client**, not just for FGE's specific industry.

## Results: The Real, Audited Payoff

Over the roughly 3-year implementation (peaking at 150+ FGE professionals plus a large consulting/systems-integration team): order-to-shipment cycle time fell 60% (vs. 1993 Q1); backorders fell 60%; inventory carrying costs fell more than $600 million (1995-1997); inventory turns rose from ~4/year to 16/year by 1999; major product transitions improved margin by $200 million; **total project benefit exceeded $3 billion by 1997.** **A side note on the engagement's own internal credibility arc, worth remembering for any new methodology introduced into a skeptical client organization**: many of the consultants running the reengineering effort started out "highly skeptical" of system dynamics specifically, and ended the project as "enthusiastic advocates" — FGE itself went on to commission further system dynamics work on product development and overall growth strategy, well beyond the original supply-chain engagement's scope.

## 18.4 Chapter Summary

Supply chains are built from linked instances of the generic stock-management structure (per [[stock-management-structure-and-amplification]] and [[manufacturing-supply-chain-model]]), and oscillation, amplification, and phase lag arise **even when every individual actor manages their own piece rationally and stably** — these are emergent properties of the interconnected structure, not failures of any individual link. The chapter's explicit methodological closing note, worth restating as a standing practice: **build models in stages, relaxing simplifying assumptions one at a time, testing thoroughly before adding the next layer of structure** — exactly the discipline this chapter itself followed from section 18.1 onward.

## Connects to

- [[manufacturing-supply-chain-model]] and [[supply-chain-interactions-and-trust]] — this case is the full real-world, multi-billion-dollar-stakes instance of the generic phenomena (amplification, lead-time gaming, allocation-driven order inflation) developed abstractly in those two pages.
- [[beer-game-and-origin-of-oscillations]] — phantom ordering is precisely the same supply-line-mismanagement mechanism as the Beer Game's WSL failure, here driven by allocation rationing rather than a simple inventory gap.
- [[ingalls-shipbuilding-project-dynamics-case]] and [[dupont-maintenance-game-and-twelve-principles]] — the model-replicating-both-product-types validation, used specifically to redirect blame from individuals to structure, is the same technique used in both of those earlier cases.
- [[owner-dependency-diagnostic|the Gap Method & Comfort Zone diagnostic]] — sequential debottlenecking is a direct, dynamic-systems refinement of the static Theory-of-Constraints bottleneck-focus principle already in the wiki.

## North Star Connection

- How this applies to the audit business: the phantom-orders mechanism is a directly transferable diagnostic for any client (not just electronics) experiencing allocation, rationing, or scarcity-driven demand spikes — construction material shortages and subcontractor capacity allocation during a regional building boom are a near-exact structural match. The "larger initial staging reduces total cost" counterintuitive finding and the sequential-debottlenecking methodology are both strong, ready-to-use frameworks for any multi-phase audit recommendation in a still-growing client organization.
- Track relevance: Business / Systems — among the highest-value, most rigorously documented case studies in the entire ingest for direct application to a growing client's supply chain or capacity-planning problem.
- Possible future Second Brain use: a "phantom orders screener" (is this client's demand surge real, or scarcity-driven self-reinforcement) and a "sequential debottlenecking roadmap" template are both strong, near-ready candidate audit deliverables.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | A real, multi-billion-dollar-validated case directly transferable to any growing client's supply chain or capacity problem |
| Current usefulness | 5 | The phantom-orders mechanism and sequential debottlenecking are both immediately applicable diagnostic/planning tools |
| KSU support | 5 | An exceptionally well-documented, rigorously validated real engagement combining group model-building, formal testing, and measured business outcomes |
| Tech-stack relevance | 2 | Conceptual case study, no direct tool dependency |
| Business audit value | 5 | The counterintuitive "larger initial staging reduces cost" finding and sequential debottlenecking are both sharp, ready-to-use consulting frameworks |
| Data/workflow value | 4 | The dual-validation testing method (same structure must explain both a slow mover and a hot product) is a concrete, transferable rigor standard for any audit deliverable |
| Reading urgency | 5 | One of the highest-value, most audited, most directly applicable cases in the entire Business Dynamics ingest |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Growth-stage client diagnostic and multi-phase planning tool — use the phantom-orders mechanism to diagnose whether a client's demand surge is real or scarcity-driven self-reinforcement, and use sequential debottlenecking to sequence a multi-phase improvement program for a still-growing client.

**Use when**:
A client's best-selling product/service is simultaneously generating allocation/rationing complaints and ending up with excess inventory or capacity once the surge passes, or when planning a multi-phase improvement program for a client still actively growing.

**Do not use when**:
The client's demand surge is genuinely one-time and non-recurring with no allocation/rationing dynamic, or the client's growth has already stabilized (sequential debottlenecking specifically addresses a *moving* constraint).

**Fast retrieval query**:
`subject/phantom-orders` + `subject/sequential-debottlenecking` — or search "first in a race of pigs" / "phantom orders hot product excess inventory" / "larger initial staging reduces sludge" / "sequential debottlenecking FGE $3 billion"
