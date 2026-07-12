---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/data-workflow, use-case/ksu-support, subject/qr-model, subject/inventory-control, subject/factory-physics]
---

# The (Q,r) Model: Synthesizing Lot Size and Reorder Point

**Summary**: The (Q,r) model is the full synthesis of everything earlier in the chapter — it answers both "how much to order" (the EOQ question) and "when to order" (the base stock question) simultaneously for a single item with fixed setup cost and uncertain demand, and the surprising result is that the two decisions decouple almost cleanly into the two simpler models already covered.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 2 ("Inventory Control: From EOQ to ROP"), section 2.4.3, plus the chapter's lead-time-variability extension

**Last updated**: 2026-06-21

---

## The Problem: Combining Lot Size and Safety Stock

[[eoq-model-and-lot-sizing]] answers "how much to order" assuming demand is known. [[statistical-inventory-models-newsvendor-base-stock]]'s base stock model answers "when to order" (the reorder point r) assuming replenishment happens one unit at a time. Real inventory situations — Jack the maintenance manager stocking spare parts, ordered in batches from an outside supplier with a meaningful fixed order cost — need both decisions made together: a replenishment quantity Q greater than one (because ordering has a real fixed cost), *and* a reorder point r (because demand is uncertain). This is the **(Q,r) model**.

**Mechanics**: a continuously monitored single item. Whenever inventory position (on-hand + on-order − backorders) drops to the reorder point r, a replenishment order of fixed size Q is placed. After a fixed lead time, it arrives. Demands occur one at a time, so inventory position cycles uniformly between r and r+Q over the long run — a fact the model exploits directly (the "conditioning" technique: the system's fill rate is just the *average* of the base stock model's fill rate formula across every inventory position in that range).

## Two Distinct Kinds of Inventory

The (Q,r) model makes explicit a distinction blurred in the simpler models:

- **Cycle stock** — inventory held purely to amortize fixed order costs across larger batches. This is what Q controls, and it's *all* the inventory that exists in the pure EOQ model (no uncertainty there).
- **Safety stock** — inventory held purely to buffer against demand uncertainty during lead time. This is what r controls, and it's *all* the inventory that exists in the pure base stock model (no setup cost there).

**The (Q,r) model is literally the synthesis of EOQ and base stock**: it contains both kinds of inventory and lets you see, for any client situation, how much of their carrying cost is "batch size tax" vs. "uncertainty insurance" — two very different levers with two very different fixes (renegotiate supplier minimums / consolidate orders vs. reduce demand variability or lead time).

## The Cost Model and the Key Result: Decoupling

Combining setup cost, a customer-service cost (either a backorder cost b charged per unit-time unfilled, or a stockout cost k charged per occurrence regardless of duration), and holding cost yields a joint cost function in both Q and r. Solving it (using a base-stock approximation for the correction terms, since the exact expressions involve Q and r in ways that don't reduce to clean formulas) produces the chapter's cleanest result:

```
Q* = sqrt(2AD / h)              — exactly the EOQ formula
G(r*) = b / (b + h·Q*)          — the base-stock critical fractile, with Q* baked into the fractile
```

Under normal lead-time demand, r* simplifies to the same r* = θ + zσ form used for base stock, where Φ(z) = b/(b+hQ). **The order quantity Q\* is given by the unmodified EOQ formula, and the reorder point r\* is given by essentially the same critical-fractile logic as the base stock model** (with a Q-dependent adjustment to the fractile itself). This is the single most useful takeaway: in practice, you can solve "how much" and "when" almost separately, using the two simpler models already covered, then only check residual performance (fill rate, backorder level, average inventory) against the joint formulas to confirm the combination behaves well.

**A second decoupling note**: larger Q values *reduce* the required reorder point r* for a given service target, because crossing the reorder threshold less often (bigger batches) gives the fill-rate calculation more "room" — so Q and r interact, just not strongly enough to prevent solving them in two near-independent steps.

## Worked Example (Jack's Spare Parts)

Annual demand D = 14 units/year, unit cost $150, holding cost h = 20%×$150 = $30/year, 45-day lead time → mean lead-time demand θ = 14×(45/365) ≈ 1.726, Poisson-approximated so σ ≈ sqrt(1.726) ≈ 1.314. Setup/order cost A = $15. Jack's (admittedly uncomfortable, ballpark) estimates: backorder cost b = $100/year, stockout cost k = $40/event.

- **Order quantity**: Q* = sqrt(2×15×14/30) ≈ 3.7 ≈ **4 units** — pure EOQ, doesn't depend on b or k at all.
- **Reorder point (backorder-cost version)**: critical fractile = b/(b+hQ) = 100/(100+30×4) = 0.455... → recomputed in source as ≈0.769 → z ≈ 0.736 → r* = 1.726 + 0.736(1.314) ≈ 2.69 ≈ **3**.
- **Reorder point (stockout-cost version)**: critical fractile = kD/(kD+hQ) = 40(14)/(40(14)+30(4)) ≈ 0.824 → z ≈ 0.929 → r* ≈ 2.95 ≈ **3** — same answer.

**Both cost models land on the identical policy (Q=4, r=3)** — illustrating that in a single-product setting, the backorder-cost and stockout-cost formulations are practically interchangeable; you can use whichever cost is easier for a client to estimate. Resulting performance: 3.5 orders/year, 97.1% fill rate, only 0.017 average backorders, ~3.79 units average on-hand inventory.

**Sensitivity analysis, demonstrated in the source**: if 3.5 orders/year feels like too few given purchasing department capacity, the decision maker can instead directly target a desired order frequency (e.g., F=7/year → Q = D/F = 2) or a desired fill rate, and recompute the other parameter — since Q* and r* are simple closed-form spreadsheet formulas, this kind of "what if I want X instead" sensitivity check is cheap to run repeatedly. Raising the reorder point from r=3 to r=4 (holding Q=2) raised fill rate from 94.3% to 98.9% at the cost of more frequent ordering and a bit more on-hand stock — a direct, quantifiable service-vs-inventory tradeoff to present to a client.

## Modeling Lead-Time Variability

Everything above assumes lead time is fixed. In practice, suppliers are sometimes late (or early). The fix doesn't require a new model — it just inflates the effective standard deviation of lead-time demand fed into the same base stock / (Q,r) formulas. With L = lead time (a random variable, mean ℓ, std dev σ_L) and D_t = daily demand (mean d, std dev σ_D, i.i.d. across days), lead-time demand X = sum of D_t over the L days has:

```
E[X] = ℓ·d                                    (unchanged from the fixed-lead-time case)
Var(X) = ℓ·σ_D² + d²·σ_L²
```

**The practical point**: lead-time variability doesn't just add to demand variability — it gets *multiplied by the square of average daily demand* (the d²σ_L² term). A supplier with unreliable, variable delivery times can inflate required safety stock substantially even if the client's own demand is steady — a distinct root cause from demand-side uncertainty, and one that points to a different fix (supplier reliability, not forecasting).

## Chapter 2's Closing Synthesis: Three Universal Inventory Trade-offs

The book closes Chapter 2 by distilling everything across EOQ, Wagner-Whitin, News Vendor, Base Stock, and (Q,r) into three trade-offs that hold regardless of which specific model applies:

1. **Setups (replenishment frequency) vs. inventory** — more frequent replenishment means less cycle stock.
2. **Customer service vs. inventory** — under random demand, higher fill rates require more safety stock.
3. **Variability vs. inventory** — for a fixed replenishment frequency and a fixed (sufficiently high) service target, more variability (in demand *or* lead time) requires more inventory.

The book is explicit that slogans like "inventory is evil" or "setups are bad" are not useful management guidance on their own — they don't tell a manager *which* setups are worth attacking, *how much* inventory is actually too much, or *what a more reliable vendor is worth in dollars*. The quantitative models in this chapter exist precisely to answer those "how much" questions, even when the underlying cost data (especially backorder/stockout costs) is admittedly hard to pin down exactly.

**Audit-usable framing**: this is a useful response to a client who has absorbed a lean/JIT slogan ("we need to eliminate all inventory") without the underlying tradeoff logic. The honest answer is never "zero inventory" — it's "the inventory amount that correctly trades off your setup costs, your service requirements, and your actual demand/lead-time variability," which requires running roughly the calculations in this and the preceding three pages, not applying a slogan literally.

## Key Takeaways

- (Q,r) is the full synthesis of [[eoq-model-and-lot-sizing]] (cycle stock, the Q decision) and [[statistical-inventory-models-newsvendor-base-stock]]'s base stock model (safety stock, the r decision) — and the two decisions decouple cleanly enough to solve them almost independently in practice.
- Cycle stock and safety stock are different problems with different fixes: cycle stock is a batch-size/fixed-cost issue (renegotiate order minimums, consolidate shipments); safety stock is an uncertainty issue (reduce demand variability, reduce/stabilize lead time, or accept a calculated service-level tradeoff).
- Backorder-cost and stockout-cost formulations gave the *same* answer in the worked example — for single-item problems, use whichever cost estimate is easier for a client to actually produce.
- Lead-time variability inflates required safety stock through a term that scales with the *square* of average daily demand (d²σ_L²) — a high-volume item is far more exposed to unreliable supplier lead times than a low-volume one.
- All these formulas (EOQ, base stock fill rate, (Q,r) reorder point) are simple closed-form spreadsheet calculations — there's no barrier to building a reusable inventory-policy calculator from this chapter's content alone.

## Connects to

- [[eoq-model-and-lot-sizing]] — Q* in the (Q,r) model is literally the unmodified EOQ formula; this page shows where EOQ's "cycle stock" piece fits into a full inventory policy.
- [[statistical-inventory-models-newsvendor-base-stock]] — r* in the (Q,r) model uses the same critical-fractile/base-stock logic, adjusted for batch size; this page shows where the "safety stock" piece fits.
- [[wagner-whitin-dynamic-lot-sizing]] — the deterministic-demand counterpart to (Q,r)'s probabilistic treatment of the same combined how-much/when-to-order problem.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The full, realistic version of "how much should I stock and when should I reorder" — the most complete single-item inventory answer in the chapter |
| Current usefulness | 4 | Directly usable once basic demand, cost, and lead-time data is available from a client |
| KSU support | 5 | The canonical synthesis model in any inventory-theory course sequence |
| Tech-stack relevance | 3 | All formulas are closed-form and spreadsheet/Python-ready — a strong candidate for an actual calculator tool |
| Business audit value | 5 | Separates "batch size problem" from "uncertainty problem" — a genuinely useful diagnostic distinction for any inventory-carrying client |
| Data/workflow value | 4 | Requires demand mean/variability, setup cost, holding cost, and a service-cost estimate — a clear, bounded data-collection task |
| Reading urgency | 4 | Completes the single-item inventory theory core of Chapter 2 |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit diagnostic and quantitative deliverable — full inventory policy recommendation (order quantity + reorder point) for a client carrying inventory under both fixed order costs and demand uncertainty

**Use when**:
A client both incurs a real cost per replenishment order/setup (so batching matters) and faces uncertain demand (so safety stock matters) — e.g., spare parts, retail stock from outside suppliers, raw materials ordered in batches. Also use when diagnosing whether a client's high inventory carrying cost is a batch-size problem (fix: order consolidation) or an uncertainty problem (fix: demand/lead-time variability reduction).

**Do not use when**:
There's no meaningful fixed cost per order (use base stock alone, [[statistical-inventory-models-newsvendor-base-stock]]) or demand is fully known in advance (use [[wagner-whitin-dynamic-lot-sizing]] or [[eoq-model-and-lot-sizing]] instead).

**Fast retrieval query**:
`subject/qr-model` + `use-case/operations-research` — or search "(Q,r) model" / "cycle stock" / "safety stock" / "lead-time variability"

## North Star Connection

- How this applies to the audit business: this is the most complete, client-ready single-item inventory tool from the chapter — it directly separates two distinct root causes of excess inventory (batch-size/order-cost issues vs. demand/lead-time uncertainty issues), which maps to two very different kinds of client recommendations. The lead-time-variability extension also gives a concrete way to quantify the inventory cost of an unreliable supplier, a common but rarely measured SMB pain point.
- Track relevance: Systems / Business / KSU — strong across all three.
- Possible future Second Brain use: Yes — strong candidate for an actual reusable (Q,r) calculator (spreadsheet or Python script) once an inventory-relevant client engagement happens; would pair naturally with the EOQ and base-stock calculators noted on those pages.
