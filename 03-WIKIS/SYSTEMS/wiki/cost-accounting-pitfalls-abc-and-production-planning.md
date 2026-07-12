---
domain: systems
type: case-study
tags: [priority/next, status/wiki-only, domain/systems, source-role/primary, use-case/audit, use-case/data-workflow, use-case/business-model, use-case/ksu-support, subject/cost-accounting, subject/linear-programming, subject/factory-physics]
---

# Cost Accounting Pitfalls: Why Activity-Based Costing Isn't Enough, and How Fully Absorbed Costs Can Bankrupt a Production Plan

**Summary**: Cost accounting is itself a model, subject to the same assumption pitfalls as any other — the historical reason traditional labor-hour overhead allocation became obsolete, why activity-based costing (ABC) is a real improvement but still no panacea (with a full worked numeric comparison), the full-absorption-vs-variable-costing distinction and the sunk-cost trap it's meant to avoid, a complete worked example showing how a sensible-looking, cost-based production plan actually loses money while a counterintuitive linear-programming solution turns the same plant profitable, the tactical-vs-strategic modeling distinction (the same numbers, different decision horizons, via LP sensitivity analysis), and a real cautionary tale of risk analysis done wrong (an American automaker that evaluated quality investment only for its upside, not its necessity to avoid catastrophic loss).

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 6 ("A Science of Manufacturing"), sections 6.4.1-6.4.3 and Appendix 6A

**Last updated**: 2026-06-21

---

## Cost Accounting Is a Model, Not Just Bookkeeping

The mathematical models typically covered in operations-management courses (EOQ, MRP, forecasting, linear programming) are not the only models used to measure performance and evaluate policy in manufacturing — **accounting methods are themselves models**, and are therefore subject to exactly the same kind of assumption-related pitfalls as any other modeling exercise, even though accounting is often perceived as mere bookkeeping or cost tracking.

**Direct costs (raw materials, and usually direct labor) are straightforward to assign.** The real modeling challenge is **overhead** (also called fixed costs or burden) — costs not directly tied to any specific product (factory mortgage payments, the CEO's salary, an R&D lab, the company mail room) that are nonetheless part of the real cost of doing business, and so must be apportioned to products *somehow*.

## Traditional Labor-Hour Allocation Became Obsolete as Labor's Cost Share Shrank

The traditional overhead-allocation model assigns overhead in proportion to labor hours: a product using 2% of total labor hours is assigned 2% of overhead cost. **The historical rationale**: when "modern" accounting techniques were developed around the turn of the 20th century, direct labor and material represented up to 90% of a typical product's total cost (Johnson and Kaplan 1987 — whose book on the subject is pointedly titled *Relevance Lost*). **Today, direct labor constitutes less than 15% of the cost of most products** — making labor-hour-proportional overhead allocation an increasingly poor proxy for where overhead actually accrues, and increasingly challenged as inappropriate.

## Activity-Based Costing (ABC): A Real Improvement, Still No Panacea

**Activity-based costing (ABC)** links overhead costs to the *activities* that drive them, rather than directly to products. For example, if purchasing activity drives certain overhead, ABC measures that activity in purchase-order units and allocates the associated overhead to each product in proportion to the purchase orders it actually generates — and similarly for other identifiable overhead-driving activities. **Because ABC divides overhead into meaningful categories, it promotes better understanding (and eventually reduction) of overhead costs, and is a genuine positive step in cost modeling.**

**But ABC is not a panacea, for two specific reasons the book names directly**:

1. **Cost allocation can be the wrong systems-level question entirely.** A real example from one author's experience at a chemical plant: extensive debate was devoted to setting the "correct" transfer price for a commodity that was simultaneously a by-product of one process and a raw material for another. Users argued the price should be zero (the commodity would otherwise be wasted); producers argued users should pay what it would cost to produce the commodity themselves. **In reality, neither process was profitable as a stand-alone operation — but the two together were quite profitable.** No allocation scheme could have resolved the debate productively, because the entire framing (assigning a transfer price between two interdependent processes) was the wrong systems-level question. **The right focus would have been on how and where to improve the combined process's yields** — a systems question, not an allocation question.
2. **No cost-based model, however detailed, can accurately represent the real value of a limited (capacity-constrained) resource.** This limitation applies equally to ABC (full/absorption costing) and to **variable costing** (which simply ignores overhead and only counts costs that vary with output).

## Full Absorption Costing vs. Variable Costing — and the Sunk-Cost Trap

**Full absorption costing** (including all costs, overhead included) is the right framework when *building* a new plant — every cost genuinely is a live decision variable at that stage (e.g., a plan requiring more setups, which require more labor, genuinely does cost more). **Variable costing** (overhead excluded) is the right framework when *operating an existing plant*, because only costs controllable within a short time frame should factor into operating decisions — machine costs already purchased are **sunk costs** and should be entirely ignored. **The trap**: managers are frequently tempted to route more production onto an expensive existing machine specifically to "recover its cost" — but this can be actively wrong from an overall-profitability perspective, especially when that expensive machine is actually less suited to the product than a cheaper alternative machine would be.

**Most product costing, ABC included, is based on fully absorbed costs, not variable costs — and this can directly cause bad decisions.** If a customer requests a part requiring extensive time at the plant's current bottleneck process center, fully-absorbed costing will (correctly) show this as expensive. **But if demand instead arrives for an item that flows only through process centers currently sitting idle, the item's true marginal cost is close to nothing but raw materials** — the otherwise-idle machines and labor are, in the relevant decision sense, essentially free, since they have nothing else to do regardless.

## Worked Example: A Cost-Based Production Plan That Loses Money

**Setup**: a plant with three machines makes two products. Product A costs $50 in raw material, requires 2 hours on machine 1 and 2 hours on machine 3 (sells for $600, demand 75-140 units/month). Product B costs $100 in raw material, requires 2 hours on machine 1, 1.5 hours on machine 2, and 1.5 hours on machine 3 (sells for $600, demand 0-140 units/month). Labor costs $20/hour; the plant runs 21 days/month, two 8-hour shifts (336 hours/month). Nonmaterial plant overhead is $100,000/month. Both products consume identical amounts of overhead activity.

**The cost-based (intuitive) plan**: profit per unit, ignoring overhead/labor, is $600 − $50 = $550 for A and $600 − $100 = $500 for B — A looks more profitable, so a cost-driven plan favors maximizing A. With 336 hours/month available and each unit of A requiring 2 hours on machine 3, maximum monthly throughput on that constraint is 168 units — but demand caps A at 140 units/month anyway (which also satisfies the 75-unit minimum). Producing 140 units of A consumes 280 of machine 3's 336 hours, leaving 56 hours for B; since each B unit needs 1.5 hours on machine 3, this yields 56/1.5 ≈ 37 units of B (rounded down from 37.33).

**The result**: monthly profit = 140($550) + 37($500) − $100,000 = **−$4,500. This plan loses money**, despite favoring the product that looks more profitable per unit on a simple cost basis.

**The linear-programming alternative**: formulating the same problem as a profit-maximization linear program subject to the actual demand and capacity constraints (see [[wagner-whitin-dynamic-lot-sizing]] for a related optimization mindset, and Chapter 16 in the source for LP itself) yields a plan calling for **75 units of A and 124 units of B per month — the *minimum* allowed quantity of the "more profitable" product A, and far more of the "less profitable" product B.** This plan is completely counterintuitive from a per-unit-cost perspective, **but it is the actual profit-maximizing solution**, because the true binding constraint is machine-3 capacity, and B uses that scarce resource (1.5 hours) more efficiently relative to its profit contribution than A does (2 hours) — a fact invisible to any analysis based on simple per-unit "profit" figures that ignore which specific resource is actually capacity-constrained. **The resulting profit is 75($550) + 124($500) − $100,000 = $3,250/month — solidly profitable**, versus the −$4,500/month loss from the intuitive cost-based plan. **The book's stated moral: the value of a limited resource depends entirely on how it is used.** A static cost-based model, however detailed (ABC included), cannot accurately assign costs to resources subject to capacity constraints, and so can produce systematically misleading results — only a constrained-optimization model that *dynamically* determines a resource's value as part of computing the optimal plan can be guaranteed to avoid this trap.

## Tactical vs. Strategic Modeling: The Same Numbers, Different Time Horizons

**A parameter that is reasonably treated as a fixed constraint for tactical (near-term) decisions is often a genuine strategic lever over a longer horizon** — and the right model depends on which decision it's meant to inform. In the worked example above, both capacity (336 hours/month) and demand (75-140 units of A) were correctly treated as fixed for next-month production planning. But over a longer strategic horizon, **capacity could be increased (a third shift) or decreased (cutting the second shift), and demand itself could be shifted (price discounts, a competitor's next-generation product)**.

**Linear programming's sensitivity-analysis output is a genuine strategic-planning tool, not just a tactical one**: re-solving the same model *without* the 75-unit minimum-production constraint on A yields a revised plan of 68 units of A and 133 of B, raising monthly profit to $3,900 — a **$650/month improvement purely from questioning whether a constraint that looked fixed is actually negotiable.** This directly motivates a strategic question the tactical model itself cannot answer: is the 75-unit floor a genuine, binding customer commitment (in which case it should stay), or merely an approximate proxy for that commitment (in which case 68 might be just as defensible, and considerably more profitable)? **Sensitivity analysis similarly reveals that each additional hour of overtime capacity at machine 3 (up to 7 hours/day) raises profit by $275/hour** — since overtime typically costs nowhere near that much, this is a concrete, quantified case for adding overtime now, while simultaneously prompting the longer-term strategic question of whether to expand the workforce, add equipment, or subcontract instead.

**The general principle**: effective planning requires different models for different decision horizons, with deliberate coordination between them — a tactical model (like the constrained-optimization plan above) supplies intuition (which variables matter), sensitivity information (where the real leverage is), and hard data (e.g., which resource is the current bottleneck) for strategic planning; a strategic model (e.g., long-term capacity planning) supplies data (future capacity constraints) and alternatives (e.g., dynamic subcontracting options) back down to the tactical level.

## Considering Risk: Why Evaluating Only the Upside Can Be Disastrous

Manufacturing decisions face many sources of genuine uncertainty (demand fluctuation, supply disruption, yield variability, machine breakdown, labor unrest, competitor action) — sometimes uncertainty must be explicitly modeled, sometimes it can be safely ignored, but it should never be ignored *by default* without first considering what happens if an assumption fails to hold.

**A real, cautionary high-level strategic example**: a major American automobile manufacturer recognized in the late 1970s/early 1980s that it needed to invest in improved product and process quality, but repeatedly denied funding for the relevant projects because they weren't "financially justified" under the implicit (and never stated) assumption that the company's competitive position relative to its rivals would stay constant. **When the competition instead upgraded quality faster than anticipated, the company suffered a disastrous, decade-long loss of market share and widespread plant closings**, only returning to (much-diminished) profitability in the 1990s. **The book's diagnosis of the fundamental analytical flaw**: the projects were evaluated purely on their *potential to improve* profit, when they should have been evaluated on their *necessity to avoid losing* profit — product and process improvement should have been treated as a constraint on staying in business, not an optional investment for additional upside.

**Risk analysis** — explicitly evaluating potential negative consequences under uncertainty, long used in riskier industries like petroleum exploration — typically conjectures multiple scenarios with assigned probabilities and computes an expected value of a performance measure (e.g., expected profit). **An alternative, sometimes more realistic approach when downside scenarios are hard to assign reliable probabilities to is minimax** (minimize the maximum possible damage) — a strategy more associated with military planning, which explicitly prioritizes avoiding catastrophic outcomes over maximizing expected value. **Had the auto manufacturer used a minimax framing**, it likely would have approved far more of the quality-improvement projects, explicitly as a hedge against a competitor-driven quality leapfrog — a clear, retrospective illustration of how evaluating decisions purely on expected upside can miss exactly the risk that ends up mattering most.

## Activity-Based Costing: A Concrete Worked Comparison

**A concrete numeric illustration of ABC vs. the traditional labor-hour approach**: a plant makes two products ("hot" and "mild"), selling 6,000 units/month of hot and 3,000/month of mild, with $250,000/month total overhead and labor hours split evenly (2,500 hours each) between the two products.

**Traditional labor-hour allocation**: since labor hours are split evenly, overhead is split evenly too — $125,000 to each product, giving a unit overhead charge of $125,000/6,000 = $20.83 for hot and $125,000/3,000 = $41.67 for mild. **Because mild has lower volume, this method inflates its unit cost disproportionately** relative to hot.

**ABC allocation**: the $250,000 overhead is broken into four activities — requisition ($50,000, allocated by 900 total purchase orders), engineering ($65,000, by 5,000 machine hours), shipping ($35,000, by 9,000 units shipped), and sales ($100,000, by 600 sales calls). Tracking each product's actual share of each activity's base unit and recomputing: **hot's unit overhead charge comes out to $25.97, and mild's to $31.38** — mild still carries a higher unit overhead charge than hot (it remains the lower-volume product), **but the gap is far smaller than under the traditional method**, because ABC correctly recognizes that hot's higher volume drives proportionally more requisition, engineering, and sales activity (and therefore more of the real cost) than a simple even labor-hour split would suggest. **The net effect: ABC makes mild look relatively more profitable than traditional accounting would suggest** — a concrete demonstration of the real distortion traditional overhead allocation can introduce, and the genuine (if partial) correction ABC provides.

## Key Takeaways

- Accounting models are genuine *models*, with the same assumption-dependent fragility as any mathematical model — they should never be treated as objective, assumption-free bookkeeping.
- Traditional labor-hour overhead allocation made sense when labor was ~90% of product cost (turn of the 20th century); with labor now under 15% of most products' cost, this allocation method is structurally outdated.
- Activity-based costing genuinely improves overhead transparency by linking costs to driving activities, but it cannot fix problems that are actually systems-level framing errors (the by-product transfer-price example), and — like any cost-based model — it still cannot correctly represent the value of a capacity-constrained resource.
- Full absorption costing is correct for new-plant investment decisions; variable costing (ignoring sunk machine costs) is correct for operating an existing plant — conflating the two, especially via the "recover the machine's cost" fallacy, leads to systematically wrong decisions.
- The book's own worked example is a sharp, concrete demonstration that maximizing production of the "more profitable" product by simple per-unit cost can produce a *money-losing* plan, while a linear-programming solution that deliberately minimizes the "more profitable" product and maximizes the "less profitable" one is the actual profit-maximizing answer — because true profitability depends on which specific resource is the binding capacity constraint, not on a product's standalone per-unit margin.
- A constraint that's correctly treated as fixed for a tactical (near-term) decision may be a genuine strategic lever over a longer horizon — LP sensitivity analysis can directly quantify the value of questioning a constraint (the $650/month gain from challenging the 75-unit minimum) or of adding flexibility (the $275/hour value of overtime capacity).
- Evaluating a risk-mitigating investment (like a quality-improvement project) purely on its potential *upside* rather than its necessity to avoid a catastrophic *downside* is a real, documented strategic failure mode — minimax (minimizing maximum possible damage) is sometimes a more realistic framework than expected-value risk analysis when downside probabilities are hard to estimate reliably.
- The worked ABC-vs-traditional numeric comparison (hot/mild example) shows the real distortion traditional labor-hour overhead allocation introduces for lower-volume products, and the genuine, quantifiable (if partial) correction ABC provides.

## Connects to

- [[strategic-objectives-hierarchy-and-efficient-frontiers]] — cost accounting's overhead-allocation choices directly feed the "low costs" branch of the ROI objectives hierarchy developed there; this page shows how that input can itself be systematically misleading.
- [[what-went-wrong-three-trends-critique-and-case-for-science]] — cost-accounting's tautological "allocate and trust the allocation" logic is structurally similar to the Six Sigma DMAIC/VSM critiques there: a detailed-looking model that nonetheless fails to capture the real systems-level constraint.
- [[wagner-whitin-dynamic-lot-sizing]] — the linear-programming counterintuitive-solution pattern here echoes the broader theme of optimization-based answers diverging sharply from naive intuition.
- [[capacity-planning-and-shop-floor-control]] — the worked example's real lesson (identify the actual binding capacity constraint, not the apparent per-unit cost) is the same diagnostic discipline underlying RCCP/CRP bottleneck analysis.
- [[factory-physics-four-step-improvement-methodology]] — the broader improvement framework this page's tactical/strategic modeling distinction and risk-analysis caution both feed into directly.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | The sunk-cost trap and the binding-constraint worked example are both directly usable for evaluating a client's product-mix or pricing decisions |
| Current usefulness | 4 | Concrete, numbers-based example that's easy to walk a client through when challenging a "make more of our most profitable product" instinct |
| KSU support | 5 | Canonical cost-accounting/operations-research crossover material, directly tied to linear programming fundamentals |
| Tech-stack relevance | 2 | Conceptual, though the LP example is a plausible future stack/python or stack/ai-frameworks-apis optimization build |
| Business audit value | 5 | The "which resource is actually capacity-constrained" diagnostic is one of the single highest-value audit questions for any client doing product-mix or pricing decisions based on simple per-unit cost |
| Data/workflow value | 3 | The worked example is a template for a genuinely buildable product-mix optimization analysis |
| Reading urgency | 3 | Completes Chapter 6's "Models and Performance Measures" section |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Audit diagnostic / pricing and product-mix analysis — challenging a client's product-mix or pricing decisions when they're based on simple per-unit cost/profit figures rather than an analysis of the actual binding capacity constraint

**Use when**:
A client makes product-mix, pricing, or "should we make this in-house" decisions based on per-unit cost figures from their accounting system, especially if they're favoring a product because it "looks more profitable" without checking which specific machine/resource is actually capacity-constrained.

**Do not use when**:
The client's plant has no binding capacity constraint (excess capacity everywhere) — in that case, simple per-unit profit figures are a reasonable approximation and the LP-style counterintuitive result won't apply.

**Fast retrieval query**:
`subject/cost-accounting` + `subject/linear-programming` — or search "activity-based costing panacea" / "sunk cost machine" / "production planning linear programming example"

## North Star Connection

- How this applies to the audit business: the worked example is one of the most concrete, numbers-driven audit tools in the entire ingest — it gives Chris a ready template for challenging a client's "obvious" product-mix decision by asking "which specific machine or resource is actually your binding constraint, and have you checked whether your accounting-based profit ranking holds up against that constraint?" This is exactly the kind of analysis that differentiates a genuine operations audit from a surface-level review of a client's existing reports.
- Track relevance: Business / Systems / KSU — strong; bridges accounting, operations, and optimization in a single concrete example.
- Possible future Second Brain use: Yes — the production-planning worked example (full-absorption-cost plan vs. LP-optimal plan) is a strong candidate for a reusable audit analysis template, especially once Chris builds Python/LP tooling for client engagements.
