---
domain: systems
type: case-study
tags: [priority/now, status/wiki-only, domain/systems, source-role/example, use-case/systems-analysis, use-case/process-design, use-case/audit, subject/system-dynamics, subject/stocks-and-flows, subject/model-boundary, subject/recycling]
---

# Aggregation, Challenging the Clouds, and Two Real Stock-Flow Case Studies

**Summary**: How to decide the right level of detail (aggregation) and model boundary (what to truncate with a "cloud") in a stock-flow map, illustrated by a real pulp-mill construction model (Homer et al. 1993) that cut project delivery time 30%+, and a real automobile-recycling model showing how "design for disassembly" and lightweighting policies can backfire through delayed, badly-coordinated stock-flow dynamics. Closes Chapter 6 of Business Dynamics.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 6 ("Stocks and Flows"), sections 6.3-6.4 (chapter complete)

**Last updated**: 2026-06-22

---

## When Should a Causal Diagram Show Explicit Stock-Flow Structure?

**Rule of thumb**: show stock-flow structure explicitly when physical processes, delays, or a stock's own behavior matter to the dynamics you're explaining — but recognize that a causal-diagram-only rendering of a stock-flow chain (e.g., Production Start Rate → WIP → Completion Rate → Finished Inventory → Shipment Rate, all drawn as plain causal links) is "technically correct" yet actively **obscures** the physical flow of material and its conservation, and routinely produces confusing polarity readings exactly because of the stock/flow distinction problem covered in [[identifying-stocks-flows-and-state-determined-systems]]. **The general guidance, restated from this specific case**: a rising production completion rate doesn't tell you whether finished inventory is rising — that depends on the *shipment* rate too — so a causal link alone can't convey the real behavior of the stock it feeds.

## Aggregation: Two Distinct Decisions (Serial Detail, Parallel Detail)

**Serial aggregation** — how finely to break a single production chain into stages (e.g., WIP as one stock, vs. disaggregated into parts/assembly/test stages) — should be driven by **average residence time relative to the dynamics you care about**. The chapter's clean rule: stocks with short residence times relative to your time horizon can usually be omitted or merged into adjacent stocks without losing anything that matters. The energy-system example sharpens this: in a multi-decade national energy model, undiscovered petroleum reserves (years-to-decades residence time) need explicit treatment, but crude-oil/refined-product pipeline inventories (a few months' worth) don't — yet **for a short-term spot-price model, exactly the opposite holds**: the months-long supply-chain stocks become critical, and the decades-long reserve stocks can be dropped entirely. **The same physical system requires opposite aggregation choices depending purely on the model's time horizon and purpose** — there is no universally "correct" level of detail independent of purpose.

**Parallel aggregation** — whether to lump multiple simultaneous activities (chassis fabrication and engine fabrication for a car) into one stock-flow chain or represent them separately — is appropriate **only if the parallel activities share similar decision rules and similar residence times**. Auto parts can usually be aggregated (similar ordering procedures, similar lead times); plant and equipment usually cannot (wildly different lifetimes, and the decision rules for greenfield builds vs. existing-facility upgrades differ in lead time, financing, and regulatory exposure). **A practical warning against over-disaggregating regardless of theoretical justification**: in the limit, representing every individual part and operation separately produces "a model... just as complex as the real system, at least as hard to understand, and quite useless" — detail complexity for its own sake destroys, not improves, a model's usefulness.

### The Client-Detail Tension, Quantified

A specific, durable finding worth keeping verbatim: **clients generally want roughly twice as much detail as the modeler thinks is actually needed to capture the relevant dynamics** (Roberts 1977/1978) — and Sterman notes his own experience suggests this is "often an underestimate." The reason isn't that clients are wrong about what's *needed* for the model to work — it's that **the detail needed to capture the dynamics and the detail needed to give the client confidence to act on the results are two genuinely different requirements.** Roberts, quoted directly: "You must provide the level of detail that causes [the client] to be persuaded that you have properly taken into account his issues, his questions, his level of concerns. Otherwise he will not believe the model you have built, he will not accept it, and he will not use it." **The resolution isn't simply acquiescing to every detail request** (that produces an expensive, unmaintainable black box) — it's working with the client over the course of the engagement so that, as confidence and understanding build, excess structure can later be stripped back out to leave a simpler, more durable model.

## Case Study: The Pulp Mill Construction Model (Homer et al. 1993)

A forest-products company's pulp-and-paper-mill design/construction division needed to cut total engineering-procurement-construction (EPC) cycle time without raising cost, in an intensifying competitive market — and recognized that **their existing, highly disaggregated project-management tools captured detail complexity (thousands of individual activities) but contained zero feedback loops, i.e., no dynamic complexity at all.** They needed a complementary tool, not a replacement.

**The boundary/aggregation negotiation itself is the most transferable part of this case**: one client-team member argued the model needed to represent every engineering drawing and purchase order individually (which would have made it unbuildable); others argued for the simplest workable structure. **The settled compromise**: two parallel stock-flow chains (Process & Equipment, and Construction), with P&E further split into three categories — reactor vessels, major equipment, and minor equipment — specifically because **reactor vessels were large enough, slow enough, and routinely on the critical path/bottleneck often enough to justify their own dedicated detail**, while construction materials (steel, concrete, rebar) could be safely lumped into one category. **This is aggregation-by-purpose in direct action**: detail wasn't added or withheld uniformly — it tracked specifically where the actual project bottleneck risk lived.

**The model explicitly included a rework-discovery-delay structure** (tasks completed incorrectly, or rendered obsolete by changes elsewhere, move from "apparently completed" into "undiscovered rework," only later being detected and pulled back into active completion) — the identical structural pattern as [[ingalls-shipbuilding-project-dynamics-case]]'s rework cycle, applied here to mill construction rather than shipbuilding. **Outcome**: the model successfully replicated historical labor hours, overtime, rework rates, purchase order volumes, and construction progress to the client's satisfaction (calibration evidence shown directly against real project data), surfaced several previously-favored policies that turned out to generate harmful side effects, and **identified policies that reduced project delivery time by at least 30% within a few years** — several of which had been "hotly debated" before the modeling work gave the team a shared structural basis for resolving the disagreement (the same blame-to-structure conversion seen repeatedly elsewhere in this ingest).

## Challenging the Clouds: Setting (and Re-Examining) the Model Boundary

Every "cloud" (source or sink) in a stock-flow diagram is an explicit decision to assume infinite capacity at that point — a real boundary choice, not a neutral default. **Barry Richmond's phrase, adopted directly by Sterman as the standing discipline**: you must "challenge the clouds" — explicitly ask whether each boundary assumption is actually appropriate for your purpose, and what real-world feedbacks you're excluding by drawing it there.

**The chapter's worked progression, using automobile production, shows what happens as the boundary is challenged repeatedly**:

1. **Initial map**: Production Starts ← source (unlimited parts supply); Shipments → sink (no effect from dealer or customer stocks). Both assumptions are immediately suspect for autos — suppliers genuinely can run short (strikes, capacity limits), and dealers genuinely do regulate orders based on their own 40-60-day inventory target.
2. **First expansion**: add explicit Supplier and Dealer sectors, with WIP and finished-inventory stocks at each — now supplier shortages and dealer-order-driven feedback are both representable, and the model spans three organizational entities (suppliers, manufacturer, dealers) rather than one.
3. **Second expansion**: replace the Sales sink with an explicit stock of Cars on the Road — because new-car sales genuinely depend on how many cars people already own and how old/needed-for-replacement those cars are (directly the same insight that drove [[gm-auto-leasing-case-study]]'s entire dynamic hypothesis).
4. **A further, explicitly flagged remaining gap**: scrapped cars still simply "disappear" in this expanded map, when in reality ~94% are shredded (steel/nonferrous recovery, one of the highest recycling rates of any industry), some are illegally abandoned, and a large residual (plastics, glass, ASR/"fluff") ends up in landfills — over two billion discarded tires already accumulated in the US at time of writing. **This specific remaining gap is exactly what the next case study addresses.**

**The general process this demonstrates**: you can, in principle, keep expanding the boundary indefinitely (suppliers' suppliers' suppliers...) — the actual stopping point is always a judgment call tied to the model's purpose, not a fact about where the "real" boundary sits.

## Case Study: Automobile Recycling (Zamudio-Ramirez 1996)

Built in response to rising landfill pressure and proposed European take-back mandates, this model picks up exactly where the prior boundary-expansion example left off, tracking what actually happens to cars after they leave the road: legal scrapping (sold to dismantlers) vs. illegal abandonment (a small flow that can nonetheless build a large, persistent stock of abandoned/burned-out cars, since both outflows from that stock — dismantler processing and government collection — are themselves small); dismantlers strip economically-valuable parts into a used-parts stock before selling the stripped "hulk" to one of roughly 200 US shredders (processing ~94% of deregistered cars at the time); shredders separate recoverable metals (steel, nonferrous) for recycling, leaving "automotive shredder residue" (ASR/"fluff" — plastics, glass, elastomers, unrecovered metal) as a major remaining environmental burden.

**Estimating the model's two hardest parameters — the supply curves for recovered parts and recovered materials — required real field methodology worth keeping as a template**: the Vehicle Recycling Partnership (a consortium spanning the Big Three automakers, dismantlers, and the recycling industry) completely disassembled a range of late-model cars to build a comprehensive part-removal-time database, since the true cost driver (labor time to remove a part) depends heavily on *precedence relationships* — which other parts must be removed first, and in what order, to reach a given valuable component. An optimization model was then built on top of that database to derive the actual supply curve (how many parts get recovered, and in what order) as a function of prices, labor costs, and vehicle design — **and that optimization model's output was embedded directly into the system dynamics simulation**, an explicit example of combining two different modeling techniques rather than forcing one tool to do both jobs.

### Why Both "Obviously Good" Recycling Policies Backfire

**Policy 1 — Design for Disassembly (DFD)**, intended to permanently increase part recovery and reduce landfill-bound fluff: **the first effect is nothing** — there's a multi-year lag between launching a DFD program and the first DFD-compliant cars even being built, then roughly a decade before those cars are old enough to be scrapped in meaningful numbers (US cars average ~10 years on the road; new cars have very low scrap rates outside insurance write-offs). **Once DFD cars finally do start reaching dismantlers in volume, the actual effect is a temporary glut of used parts** — recovery rate rises above the (much more price-inelastic, since automakers/parts-makers actively defend their lucrative new-parts market and can restrict used-part use in authorized service/warranty repairs) usage rate, used-part prices fall, and the falling price reduces how many parts remain *economically* worth recovering — pulling the recovery rate back down toward roughly its pre-DFD level. **"The principal effect of DFD might simply be to depress the price of used parts, offsetting most of the benefit of improved design."**

**Policy 2 — lightweighting (more plastic, less steel)**, intended to improve fuel economy and reduce both fluff volume and vehicle weight: **the unintended mechanism runs through shredder economics, not dismantler economics.** Shredders' revenue depends heavily on recovered steel/nonferrous metal value; as lightweighted cars begin entering the scrap stream, per-hulk metal revenue falls while shredders' largely *fixed* processing costs do not — squeezing shredder profitability. **The predicted result, confirmed by the model**: shredders may respond by shredding fewer hulks (diverting more directly to landfill) — meaning **a policy explicitly designed to reduce fluff and landfill burden can instead increase the number of abandoned cars and the volume of landfilled fluff**, precisely the opposite of its stated goal, because the policy's designers modeled the *materials* benefit but not the *economic* feedback running through the shredders who actually process the stock.

**The general lesson, stated by the source and directly continuous with [[traffic-congestion-and-compensating-feedback]]'s closing theory**: "the collection of recyclable materials and the actual recycling of those materials aren't the same thing" — a supply-side intervention (better designs, recyclable materials) doesn't automatically translate into more material actually recycled unless matched by demand-side policy (ensuring recovered parts/materials are actually used), because the intervening economic actors (dismantlers, shredders) respond to *price*, and price is exactly the variable a purely design-focused policy doesn't touch.

## 6.4 Chapter Summary

Stocks are the states of the system providing the basis for decisions, the source of inertia/memory and of all delays, and the mechanism generating disequilibrium by decoupling flow rates governed by different decision processes. The diagramming notation is mathematically exact (Stock = ∫(Inflow − Outflow), equivalently d(Stock)/dt = Inflow − Outflow) while remaining far easier to build, explain, and revise with a client than the equivalent equations. **The chapter's closing aggregation rule, restated as the final, most generalizable takeaway**: serial stocks can be aggregated if short-lived relative to your time horizon; parallel activities can be aggregated if governed by similar decision rules with similar residence times; and **every source/sink in your model represents a real boundary assumption (infinite capacity) that should be actively challenged, not passively accepted**, against the specific purpose of the model.

## Connects to

- [[identifying-stocks-flows-and-state-determined-systems]] — this page's aggregation and boundary discussion directly extends that page's stock-identification toolkit to the question of how many stocks, and how far upstream/downstream, a real model should actually include.
- [[ingalls-shipbuilding-project-dynamics-case]] — the pulp mill model's rework-discovery-delay structure is the identical pattern, applied to a different industry; both are direct descendants of the same generic project-phase module logic.
- [[time-horizon-and-endogenous-explanation]] — the petroleum-reserves-vs-pipeline-inventory aggregation example is a direct, concrete instance of that page's "set your boundary and detail relative to your purpose and time horizon" discipline.
- [[traffic-congestion-and-compensating-feedback]] — the recycling case's "supply-side policy doesn't guarantee demand-side outcomes unless price feedback is addressed" closing lesson is structurally the same compensating-feedback warning as that chapter's road-building case, here running through dismantler/shredder economics instead of induced traffic demand.

## North Star Connection

- How this applies to the audit business: the client-detail-tension finding (clients want ~2x the detail modelers think necessary, and the *reason* is persuasion/confidence, not modeling accuracy) is a directly actionable scoping lesson for designing any audit deliverable — building in enough visible detail to earn client trust, even where the underlying analysis doesn't strictly require it, then simplifying later as trust builds. The DFD/lightweighting case is a sharp, generally applicable warning: **a policy that looks obviously beneficial on the supply side can still fail or backfire if it doesn't account for the economic behavior of the intermediate actors who have to act on it** — directly relevant to any client recommendation involving a supply chain, vendor, or subcontractor relationship.
- Track relevance: Business / Systems — the "challenge the clouds" discipline and the client-detail-tension finding are both broadly applicable scoping tools for every future engagement.
- Possible future Second Brain use: a "challenge the clouds" model-boundary checklist (what's assumed infinite, and is that actually safe for this client's situation) is a strong candidate audit-scoping tool, alongside a "supply-side fix, demand-side check" diagnostic drawn from the recycling case.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The "challenge the clouds" discipline and the supply-side/demand-side recycling lesson are both broadly transferable audit scoping tools |
| Current usefulness | 4 | The client-detail-tension finding is immediately useful for designing the next audit deliverable |
| KSU support | 5 | Two fully worked, real, well-documented case studies — strong systems engineering coursework material |
| Tech-stack relevance | 2 | The aggregation-by-residence-time rule directly informs spreadsheet/simulation model structure decisions |
| Business audit value | 5 | "A policy that looks obviously beneficial can still backfire if it doesn't account for the intermediate actors' economic behavior" is a sharp, broadly reusable consulting caution |
| Data/workflow value | 3 | The Vehicle Recycling Partnership's disassembly-database methodology is a concrete, transferable data-collection template for any parameter requiring real field measurement |
| Reading urgency | 4 | Closes Chapter 6 with the chapter's most directly practical scoping guidance |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Model-boundary and deliverable-scoping tool — use the "challenge the clouds" discipline when defining any audit model's boundary, and use the client-detail-tension finding when deciding how much supporting detail to build into a client deliverable beyond what the core analysis strictly requires.

**Use when**:
Scoping a new model or deliverable's boundary, or when a client requests more detail than seems analytically necessary (recognize this as a confidence-building need, not necessarily scope creep to resist).

**Do not use when**:
The model's boundary is genuinely simple and uncontroversial (e.g., a single, self-contained process with no real upstream/downstream ambiguity) — the full "challenge the clouds" exercise isn't needed.

**Fast retrieval query**:
`subject/model-boundary` + `subject/recycling` — or search "challenge the clouds Richmond" / "clients want twice as much detail" / "pulp mill construction Homer 30 percent" / "design for disassembly used parts glut" / "shredder economics lightweighting fluff"
