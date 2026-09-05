---
domain: systems
type: framework
tags: [subject/news-vendor-model, subject/base-stock-model, subject/inventory-control, subject/factory-physics]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, operations-research, data-workflow, ksu-support]
---

# Statistical Inventory Models: The News Vendor and Base Stock Models

**Summary**: Two related models for inventory decisions under genuinely uncertain demand — the single-period News Vendor model and its multi-period extension, the Base Stock model — both built on the same "critical fractile" logic: balance the cost of ordering too much against the cost of ordering too little, weighted by their relative likelihood.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 2 ("Inventory Control: From EOQ to ROP"), sections 2.4-2.4.2

**Last updated**: 2026-06-21

---

## The Shift From Deterministic to Probabilistic Models

[[eoq-model-and-lot-sizing]] and [[wagner-whitin-dynamic-lot-sizing]] both assume demand is known. Real demand usually isn't. There are two broad ways to handle that: model demand as deterministic and pad it with fudge factors (the dominant approach inside MRP systems), or model uncertainty explicitly using probability distributions (the dominant approach in statistical reorder-point methods). The News Vendor and Base Stock models are the foundational examples of the second approach, both originating from Wilson's 1934 framing of inventory control as having two separable parts: how much to order, and when (the reorder point).

## The News Vendor Model

**Setup**: a single-period decision under random demand — named for the classic problem of a street vendor deciding how many newspapers to stock for one day, knowing unsold copies are worthless and stockouts mean lost sales. The motivating book example is buying Christmas lights once before the season: order too few and you lose sales; order too many and you're stuck with worthless leftover stock.

**Assumptions**: (1) products can be analyzed individually, (2) it's a single period — no opportunity to reorder, (3) demand X is random with known distribution g(x)/G(x), (4) the full order quantity arrives before demand occurs, (5) overage and underage costs are linear per unit.

**The cost tradeoff**: let co = cost per unit of *overage* (ordered too much) and cs = cost per unit of *shortage* (ordered too little, i.e. lost-sale or backorder cost). The optimal order quantity Q* satisfies the **critical fractile** result:

```
G(Q*) = cs / (co + cs)
```

This says: order enough that the probability of *not* stocking out equals the ratio of shortage cost to total (over + under) cost. If demand is normal with mean μ and standard deviation σ, this simplifies to:

```
Q* = μ + zσ
```

where z is the standard-normal value satisfying Φ(z) = cs/(co+cs). **Intuition check on the formula**: the higher the shortage cost relative to overage cost, the larger the critical fractile, the larger z, and the more you order above the mean — and vice versa. Demand variability (σ) amplifies whatever direction that critical fractile points: more variable demand means a higher Q* when shortage costs dominate, and a lower Q* when overage costs dominate.

**Worked example (ice cream sweet shop)**: a shop sells $15 pints (cost $10) weekly, mean weekly demand 25 units, modeled as Poisson so σ = sqrt(25) = 5. Shortage cost cs = $5 (lost profit per unit). Overage cost co = interest on the $10 wholesale cost at a 25%/year rate prorated weekly ≈ $0.048/unit. Critical fractile = 5/(5+0.048) ≈ 0.99 → z ≈ 2.326 → Q* = 25 + 2.326(5) ≈ 36.63 ≈ **37 pints**. Because lost-sale cost vastly exceeds the tiny weekly holding cost, the model says stock far above the mean — a useful, immediately legible result for a client with similar economics (high margin, cheap-to-hold, costly-to-stock-out goods).

**Extension to multi-period order-up-to systems**: the same critical-fractile math reappears (per Nahmias 1993) as the optimal *order-up-to level* in a periodic-review system with backordered demand and no setup cost — co becomes the per-period holding cost and cs the per-period backorder cost, or with lost sales, co is holding cost and cs is unit profit margin.

## The Base Stock Model

**Setup**: a continuous-review system for a single item, replenished one unit at a time with a fixed lead time, where a replenishment order is triggered every time the inventory position drops by one unit (the standard model for an item that's reordered automatically on every sale, e.g. an appliance store's refrigerator stock).

**Key definitions**: inventory position = on-hand inventory − backorders + outstanding orders, and is held constant at the **base stock level** (r + 1) at all times by the system's own logic — this is also exactly what a kanban system does mechanically (see Chapter 4 in the source). The decision variable is the reorder point r (equivalently, the base stock level r+1, or the safety stock s = r − θ, where θ is mean lead-time demand).

**Performance measures, all derived from the lead-time demand distribution**:
- **Fill rate** S(r) = G(r+1) — the probability a unit of demand is filled directly from stock.
- **Expected backorder level** B(r) — a "loss function" with the same structural role here as it will later have in the more complex (Q,r) model.
- **Expected on-hand inventory** I(r) = r + 1 − θ + B(r).

**The same critical-fractile structure reappears**: formulating a cost function Y(r) = h·I(r) + b·B(r) (holding cost plus backorder cost) and minimizing it over r yields:

```
G(r* + 1) = b / (b + h)
```

— structurally identical to the News Vendor's G(Q*) = cs/(co+cs). Under normal lead-time demand this again simplifies to r* + 1 = θ + zσ, where Φ(z) = b/(b+h).

**Worked example (Superior Appliance)**: mean lead-time demand θ = 10 units/month, σ = sqrt(10) ≈ 3.16 (Poisson-derived), h = $15/unit/month (2%/month interest on a $750 wholesale refrigerator), b = $25/unit/month (estimated lost-margin/discount cost of a stockout). Critical fractile = 25/(25+15) = 0.625 → z ≈ 0.32 → r*+1 ≈ 10 + 0.32(3.16) ≈ 11.01 ≈ 11, giving a fill rate of only ≈62% — flagged in the book itself as low, likely meaning the backorder cost b was underestimated. Raising b to $200/unit/month pushes the critical fractile to 0.93 and the fill rate correspondingly higher — a clean illustration of how sensitive the "right" inventory level is to getting the backorder/shortage cost roughly right, in sharp contrast to EOQ's famous insensitivity to lot-size error (see [[eoq-model-and-lot-sizing]]).

## Key Takeaways

- Both models reduce to the same **critical fractile** logic: optimal order/stock level is set so the probability of avoiding a stockout equals shortage-cost ÷ (shortage-cost + overage-cost) — a single mental model covering single-period (News Vendor) and continuous-review (Base Stock) inventory decisions.
- Getting the backorder/shortage cost estimate right matters far more here than in EOQ — small changes to b or cs can swing the recommended stock level and resulting fill rate substantially, the opposite of EOQ's famous robustness to lot-size error.
- The base stock level (r+1) is exactly what a kanban system maintains mechanically — this is the direct mathematical link between formal inventory theory and lean's pull-system practice (see [[lean-methodology#The Seven Wastes (plus an eighth)|the seven wastes (muda)]], takt-time-and-pull-systems).
- A normal or Poisson approximation to demand, plus three or four client-supplied numbers (mean demand, demand variability or count data to estimate it, holding cost, shortage/backorder cost), is enough to produce a defensible recommended stock level — a genuinely fast audit deliverable.

## Connects to

- [[eoq-model-and-lot-sizing]] — same overall inventory-control problem (how much/when to order), but EOQ assumes known demand while these models assume uncertain demand; the deliberate contrast in cost-estimate sensitivity is worth remembering.
- [[wagner-whitin-dynamic-lot-sizing]] — the other deterministic-demand extension; together the three models span the deterministic side (EOQ, Wagner-Whitin) and the probabilistic side (News Vendor, Base Stock) of single-item inventory control.
- takt-time-and-pull-systems and [[lean-methodology#The Seven Wastes (plus an eighth)|the seven wastes (muda)]] — the base stock level is the formal mathematical equivalent of a kanban system's fixed card count; lean's pull-system intuition and this chapter's inventory theory describe the same mechanism from different angles.
- [[factory-physics-framing-and-scope]] — both models are clean examples of the book's "basics" layer: simple, well-understood quantitative laws meant to be internalized before attempting synthesis-level problem solving.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Directly answers "how much stock should this client carry" — one of the most common, concrete audit questions for any inventory-holding business |
| Current usefulness | 4 | Needs only a handful of client-supplied numbers (demand mean/variability, holding cost, shortage cost) to produce a real recommendation |
| KSU support | 5 | Core OR/inventory-theory content, near-certain to recur in ISYE coursework |
| Tech-stack relevance | 3 | Straightforward to implement as a Python/spreadsheet calculator (normal/Poisson z-lookup) for client deliverables |
| Business audit value | 5 | The critical-fractile question (what's your real lost-sale cost vs. holding cost?) is itself a powerful client-interview prompt, independent of the math |
| Data/workflow value | 4 | Requires basic demand-history data collection and a cost estimate — a natural first data-workflow task in an inventory-heavy audit |
| Reading urgency | 4 | The most directly client-usable section of Chapter 2 so far |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit diagnostic and quantitative deliverable — recommending a stock level or safety-stock target for a client carrying inventory under uncertain demand

**Use when**:
A client holds inventory of any kind (retail stock, spare parts, raw materials, finished goods) and demand fluctuates rather than following a known schedule; especially useful when the client currently sets stock levels by gut feel rather than any calculation.

**Do not use when**:
Demand is known in advance on a fixed schedule (use [[wagner-whitin-dynamic-lot-sizing]]) or roughly constant (use [[eoq-model-and-lot-sizing]]); or when the client's real constraint is setup/changeover cost rather than demand uncertainty.

**Fast retrieval query**:
`subject/news-vendor-model` or `subject/base-stock-model` + `use-case/operations-research` — or search "critical fractile" / "order-up-to level" / "fill rate"

## North Star Connection

- How this applies to the audit business: this is the most directly usable quantitative model in Chapter 2 so far — a fast way to turn "how much should I stock?" (a question almost every inventory-holding client asks, usually answered by habit) into a defensible, numbers-backed recommendation using a handful of inputs Chris can gather in a single client conversation. The explicit link to kanban/pull systems also means this content bridges directly into the lean-methodology material already in the wiki.
- Track relevance: Systems / Business / KSU — strong across all three: solid OR theory, directly client-deliverable, and core coursework material.
- Possible future Second Brain use: Yes — a strong candidate for a reusable stock-level calculator template (spreadsheet or small Python script) once the first inventory-relevant client engagement happens.
