---
domain: systems
type: framework
tags: [subject/eoq, subject/inventory-control, subject/factory-physics]
timeline: next
status: wiki-only
source_role: primary
use_cases: [systems-analysis, operations-research, ksu-support]
---

# The EOQ Model: Lot Sizing, Cost Tradeoffs, and Why Errors Don't Matter Much

**Summary**: The Economic Order Quantity model — the oldest formal inventory-control result (Harris 1913, popularized by Wilson 1934) — balances fixed setup/ordering costs against inventory holding costs to find an optimal lot size, and turns out to be remarkably insensitive to errors in its own inputs.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 2 ("Inventory Control: From EOQ to ROP"), sections 2.1-2.3

**Last updated**: 2026-06-21

---

## The Setup: Why Lot Sizing Is a Real Tradeoff

Every replenishment order (whether a purchase order to a supplier or a production run on a machine) carries a **fixed cost per order/setup (A)** — independent of how many units are ordered — plus a **per-unit holding cost (h)** for carrying inventory. Order in small, frequent lots and setup costs dominate; order in large, infrequent lots and holding costs dominate. The EOQ model finds the lot size that minimizes the sum of both.

## The Model and Its Result

Given demand rate λ (units/year), setup cost A, and annual holding cost per unit h, the total annual cost as a function of lot size Q is:

```
Y(Q) = (λ/Q)A + (Q/2)h
```

The first term is annual setup cost (more orders as Q shrinks); the second is annual average holding cost (holding Q/2 units on average, the "sawtooth" inventory pattern). Setting dY/dQ = 0 yields the classic result:

```
Q* = sqrt(2Aλ / h)
```

This is the single most-cited formula in inventory theory — the "square root law" of lot sizing.

## The Sensitivity Result: Why Getting Q Wrong Doesn't Hurt Much

The book's most practically important finding about EOQ isn't the formula — it's how forgiving it is. **A 100% error in the lot-size decision (ordering twice or half the optimal Q) produces only a 25% increase in total cost.** This comes directly from the shape of Y(Q): it's a shallow, flat-bottomed curve near the optimum, not a sharp V. Practically: if you're uncertain about your true setup cost or holding cost inputs, don't agonize over precision — the EOQ formula is robust to being "roughly right."

**Audit-usable framing**: this is a permission slip, not a warning. A client's inventory or batch-size policy doesn't need to hit a perfectly computed EOQ to capture most of the available savings — getting within a factor of 2 of the right order is usually good enough. This matters because it means a quick, rough EOQ estimate from imperfect client data is still worth doing and acting on.

## Practical Extension: Powers-of-2 Ordering Policies

Because the EOQ cost curve is so flat, firms don't need bespoke order intervals for every SKU. A common practical simplification is the **powers-of-2 policy**: restrict order intervals to powers of 2 of some base period (e.g., order every 1, 2, 4, 8, or 16 weeks). This loses very little compared to the true continuous-optimal interval (the flatness of Y(Q) guarantees the loss is small) while making coordination across many SKUs, multiple suppliers, or shared transportation dramatically simpler — orders naturally synchronize on common dates instead of falling on arbitrary, uncoordinated schedules.

## Key Takeaways

- EOQ formalizes the core inventory tradeoff: fixed cost per order vs. holding cost per unit, and resolves it to Q* = sqrt(2Aλ/h).
- The cost curve is flat near the optimum — a 100% lot-size error costs only 25% more, so precision in estimating A and h matters less than getting them roughly right.
- Powers-of-2 ordering intervals exploit that same flatness to simplify multi-SKU scheduling with minimal cost penalty.
- EOQ assumes deterministic demand — it says nothing about uncertainty, which is exactly the gap the [[wagner-whitin-dynamic-lot-sizing]] and statistical models address.

## Connects to

- [[wagner-whitin-dynamic-lot-sizing]] — EOQ assumes constant demand; Wagner-Whitin solves the same setup-vs-holding tradeoff when demand varies period to period.
- [[statistical-inventory-models-newsvendor-base-stock]] — EOQ and its extensions handle the "how much to order" question under known demand; the statistical models handle the same question under uncertain demand.
- [[factory-physics-framing-and-scope]] — EOQ is the canonical example of a simple, robust quantitative law the book argues every operations manager should know cold.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Lot-sizing/batch-size questions come up directly in any client with purchasing, setups, or batch production |
| Current usefulness | 3 | Useful once a client engagement involves inventory or batching decisions |
| KSU support | 5 | Canonical first model in any OR/inventory-theory sequence |
| Tech-stack relevance | 2 | Easy to implement as a single-formula spreadsheet or Python calculation for client deliverables |
| Business audit value | 4 | The sensitivity result is a direct, reassuring talking point when recommending a lot-size change from imperfect data |
| Data/workflow value | 3 | Requires only demand rate, setup cost, and holding cost — all obtainable from basic client records |
| Reading urgency | 3 | Mid-ingest of Chapter 2, actively in progress |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Audit diagnostic / quick quantitative deliverable — recommending an order quantity or batch size from basic cost data

**Use when**:
A client orders supplies, raw materials, or runs production batches and can supply (even roughly) a per-order/setup cost and a holding-cost rate.

**Do not use when**:
Demand is highly uncertain or seasonal — use the statistical models ([[statistical-inventory-models-newsvendor-base-stock]]) instead; or when demand varies sharply period-to-period in a known pattern — use [[wagner-whitin-dynamic-lot-sizing]] instead.

**Fast retrieval query**:
`subject/eoq` + `use-case/operations-research` — or search "economic order quantity" / "powers of 2" / "square root law"

## North Star Connection

- How this applies to the audit business: any client that orders materials, supplies, or runs batch production has an implicit lot-sizing decision, usually made by habit rather than calculation. A rough EOQ estimate is a fast, low-effort audit deliverable, and the sensitivity result means Chris doesn't need precise client cost data to make a credible recommendation.
- Track relevance: Systems / KSU — foundational OR model, directly testable in coursework and directly applicable to audit work.
- Possible future Second Brain use: Not yet — a strong candidate for a quick-calculation tool/template once the first inventory-relevant client engagement happens.
