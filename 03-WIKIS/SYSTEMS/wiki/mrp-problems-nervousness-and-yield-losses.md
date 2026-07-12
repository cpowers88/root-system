---
domain: systems
type: framework
tags: [priority/next, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/process-design, use-case/ksu-support, subject/mrp, subject/inventory-control, subject/factory-physics]
---

# MRP's Core Problems: Yield Losses, Capacity Infeasibility, Long Lead Times, and System Nervousness

**Summary**: The chapter's frank accounting of where MRP's deterministic, infinite-capacity model breaks against reality — yield loss (fewer good parts finish than started), capacity infeasibility (MRP assumes infinite capacity), the self-reinforcing spiral toward ever-longer planned lead times, and "system nervousness" (a counterintuitive failure mode where a *decrease* in demand can make a previously feasible plan infeasible) — plus the practical remedies the industry developed in response (rough-cut capacity planning, capacity requirements planning, frozen zones/time fences, firm planned orders).

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 3 ("The MRP Crusade"), sections 3.1.8-3.1.9

**Last updated**: 2026-06-21

---

## Yield Loss: Why "Average Yield" Isn't Enough

When a process scraps some fraction of what it starts, MRP must inflate planned order quantities to compensate: starting N_t/(1−y) units (where y is the average yield-loss fraction) should average out to the N_t units actually needed. But "average" hides the real problem — actual output around that average is genuinely random, so the job will, roughly half the time, finish with *more* than needed (extra inventory, a real cost if the product is customized) and roughly half the time with *less* (a new job needed, an order that probably ships late). **Safety stock, or simply inflating the start quantity by more than the average yield-loss factor, can buy back better service — but only at the cost of carrying more inventory; the two approaches are essentially equivalent.**

**The deeper, more practically important insight**: an "average yield rate" alone tells you nothing about how *effective* a yield-protection strategy will be — the actual variability and failure *mechanism* matter enormously. The book's own contrast: if 100 units start with each having an *independent* 0.9 probability of completing, the mean/std dev of completions is 90/3, so starting 120 units (mean + ~10 std devs of slack, more precisely 3 std devs above mean using a smaller margin in the source's example) gives >99% confidence of finishing at least 100 — requiring only 8 extra units of average inventory. But if the failure mode is **all-or-nothing** (as in a batch process — either the whole batch finishes or none of it does), achieving the same 99% confidence requires releasing two entire separate 100-unit jobs, since a single job either succeeds completely or fails completely — inflating average inventory by 80 units, ten times worse. **Independent, item-by-item yield risk is vastly cheaper to hedge against than correlated, batch-level yield risk** — a distinction that matters far beyond MRP (any process where failures cluster rather than scatter independently needs disproportionately more buffer).

## Problem 1: Capacity Infeasibility

MRP's basic working model assumes a fixed planned lead time *independent of how loaded the line actually is* — in other words, **MRP implicitly assumes infinite capacity**. When a line is near or at capacity, this assumption breaks down and MRP can generate schedules that are arithmetically consistent but physically impossible to execute. The industry's response was two capacity-checking modules, both eventually folded into **manufacturing resources planning (MRP II)** and later **enterprise resources planning (ERP)**: **rough-cut capacity planning (RCCP)**, an approximate feasibility check applied to the master production schedule itself, and the more detailed **capacity requirements planning (CRP)**, applied to the resulting MRP-generated plans.

## Problem 2: The Self-Reinforcing Spiral Toward Long Planned Lead Times

Setting a part's planned lead time equal to its *average* actual manufacturing time yields only a 50% service level for that component (half the time the job genuinely takes longer than average) — and the effective service level for a finished assembly built from several such components is far worse than 50%, by the same independent-reliability multiplication logic covered in [[mrp-special-topics-lot-sizing-safety-stock-troubleshooting]]. Because **excess inventory is silent while dissatisfied customers are loud**, planners facing this tradeoff consistently err toward longer, more pessimistic planned lead times. But MRP treats lead time as *constant* regardless of how loaded the line is — and the longer the planned lead time, the longer parts sit waiting between operations, which **inflates the actual amount of work-in-process inventory in the system**, which (per the queuing/congestion relationships covered later in the book's Part II) tends to make real cycle times even longer, reinforcing the same pessimistic-lead-time behavior in the next planning cycle. **This is a structurally self-reinforcing problem, not a one-time miscalibration** — the book flags it as one of MRP's most persistent real-world failure modes.

## Problem 3: System Nervousness — Why a Demand Decrease Can Break a Feasible Plan

**System nervousness** occurs when a small change in the master production schedule produces a disproportionately large change in downstream planned order releases. The book's worked example (after Vollmann et al. 1992) demonstrates something genuinely counterintuitive: **reducing demand for item A in one period (from 24 units to 23) can make a previously-feasible plan for a lower-level component infeasible** — because the fixed-order-period lot-sizing rule's period-grouping logic shifts entirely (aggregating a different set of periods together) in response to even a tiny input change, cascading into a wildly different, sometimes physically infeasible, set of planned order releases for component B several levels down. **The fragility isn't a bug in this specific example — it's a structural property of how lot-sizing rules group demand across periods**, and it means a planner can't safely assume "a smaller demand change implies a smaller, safer schedule change."

**Remedies**, in increasing order of structural intervention:
- **Choice of lot-sizing rule** — lot-for-lot guarantees the change in planned order releases is never larger than the change in the MPS itself (since there's no period-grouping to destabilize), at the cost of more frequent setups. Vollmann et al. (1992) recommend *varying* the lot-sizing rule by BOM level — fixed order quantity for end items, FOQ or lot-for-lot for intermediate levels, fixed order period for the lowest levels — since fixed lot sizes at higher levels don't change in response to demand-quantity changes, directly damping the nervousness those levels would otherwise propagate downward.
- **Frozen zones** — forbid any changes to the earliest portion of the MPS (e.g., the first 4 weeks), since changes there are the most disruptive to already-committed near-term plans.
- **Time fences** — a graduated version of frozen zones: an absolutely frozen near-term fence, a more flexible mid-term fence (changes accepted only under certain conditions, possibly with a customer penalty), and a fully open far-term zone (anything goes). This formalizes the realistic middle ground between "rigid" and "fully responsive" planning.
- **Firm planned orders** (already covered in [[mrp-special-topics-lot-sizing-safety-stock-troubleshooting]]) — pin specific planned orders in place regardless of MPS changes, the most surgical of the remedies since it targets individual orders rather than whole time windows or whole lot-sizing rules.

## Key Takeaways

- An average yield rate is not sufficient information to design an effective yield-loss hedging strategy — the *variability and failure mechanism* matters far more: independent, item-level failure is vastly cheaper to buffer against than correlated, batch-level failure (10x more inventory needed in the book's own worked comparison).
- MRP's infinite-capacity assumption is real and consequential — RCCP and CRP exist specifically to catch capacity-infeasible plans before they hit the shop floor.
- Long planned lead times aren't a one-time calibration mistake; they're a self-reinforcing spiral (longer lead time → more WIP → longer real cycle times → even longer planned lead time next cycle) driven by the asymmetric visibility of inventory cost (silent) vs. poor service (loud).
- "System nervousness" is a structural property of lot-sizing rules that group demand across periods, not a rare edge case — a small MPS change can produce a disproportionately large, sometimes infeasible, downstream schedule change, and this can happen even when demand *decreases*.
- The standard remedies (lot-sizing-rule choice by BOM level, frozen zones, time fences, firm planned orders) all work by deliberately sacrificing some scheduling optimality for stability — there's no remedy that gets both full responsiveness and full stability simultaneously.

## Connects to

- [[mrp-special-topics-lot-sizing-safety-stock-troubleshooting]] — firm planned orders and lot-sizing-rule choice are covered there as direct nervousness remedies; the independent-component-reliability math underlying the long-lead-time spiral is the same logic as the safety-lead-time assembly example there.
- [[mrp-mechanics-netting-lot-sizing-bom-explosion]] — the four-step algorithm whose lot-sizing step is the literal mechanism behind nervousness.
- [[mrp-history-and-push-pull-paradigm]] — MRP's deterministic, infinite-capacity core assumption (critiqued throughout this page) is the same simplification the independent/dependent-demand framing rests on.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | The long-lead-time spiral and the independent-vs-correlated-yield-risk distinction are both transferable diagnostic lenses well beyond formal MRP systems |
| Current usefulness | 3 | Background/diagnostic value pending an active ERP/MRP or production-scheduling client engagement |
| KSU support | 5 | Canonical, detailed production-control-systems critique content |
| Tech-stack relevance | 2 | Conceptual, not a direct coding task |
| Business audit value | 4 | "Why does our planning lead time keep getting longer and our inventory keep growing" is a genuinely common client complaint this page directly explains |
| Data/workflow value | 2 | Mostly conceptual/diagnostic rather than a data-handling technique |
| Reading urgency | 3 | Mid-ingest of Chapter 3, actively in progress |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Audit diagnostic / KSU support — explaining a client's chronically-lengthening planning lead times and growing inventory, or diagnosing yield/scrap-loss hedging strategies that aren't accounting for whether failures are independent or correlated

**Use when**:
A client's production planning lead times keep getting longer year over year alongside growing inventory (the self-reinforcing spiral), or a client hedges against scrap/yield loss using only an average rate without considering whether failures cluster (batch-level) or scatter independently (item-level).

**Do not use when**:
The client has no formal capacity-constrained production scheduling system — the yield-loss independent-vs-correlated distinction still applies generally, but the MRP-specific remedies (RCCP, CRP, time fences) won't.

**Fast retrieval query**:
`subject/mrp` + `use-case/process-design` — or search "system nervousness" / "capacity infeasibility" / "yield loss" / "time fences" / "frozen zone"

## North Star Connection

- How this applies to the audit business: the self-reinforcing long-lead-time spiral is a sharp, plain-language explanation for a complaint Chris will hear often — "our lead times keep growing and so does our inventory, but nothing specific seems to have changed." The independent-vs-correlated yield-loss distinction is also broadly portable: any client process where failures can cluster (one bad batch ruins everything) needs a fundamentally different buffering strategy than one where failures scatter independently (one bad unit doesn't affect the others).
- Track relevance: Systems / Business / KSU — strong across all three.
- Possible future Second Brain use: Not yet — strong diagnostic background for whenever a client's planning/scheduling system becomes an active audit focus.
