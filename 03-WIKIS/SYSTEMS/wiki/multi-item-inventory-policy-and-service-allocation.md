---
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, supply-chain-science, inventory, multi-item, service-level, reorder-point, spare-parts, audit]
---

# Multi-Item Inventory Policy and Service Allocation

**Summary**: Inventory should be classified by why it exists, then controlled with
the policy appropriate to cycle stock, safety stock, or both. In a multi-item system,
uniform days-of-supply targets are structurally inefficient because they ignore
part cost, demand variability, and replenishment lead time. Service and inventory
must be allocated jointly across items: inexpensive or highly variable parts may
deserve higher service, while expensive slow-moving items may be pooled or stocked
at lower local levels.

**Source**: `suppyChainScience.pdf` (Wallace J. Hopp, *Supply Chain Science*),
Chapter 7, "Inventory" (printed pp. 114-142; physical PDF pp. 128-156), reviewed as
one complete main-content chunk. Questions for Thought (printed pp. 143-144;
physical pp. 157-158) were identified and excluded as practice material.

**Last updated**: 2026-07-16

## Chapter Coverage

| Section | Disposition |
|---|---|
| 7.1-7.2 | Cost/service tradeoff and working, congestion, cycle, safety, and anticipation stock captured |
| 7.3 | EOQ/cycle-stock mechanics routed to existing EOQ coverage |
| 7.4 | Base-stock/safety-stock mechanics routed to existing stochastic inventory coverage |
| 7.5-7.6 | Periodic and continuous review mechanics routed to existing inventory pages |
| 7.7 | Multi-item coupling, service allocation, days-of-supply critique, and Bell & Howell case captured here |

## Classify Before Optimizing

- **Working stock** is actively processing or moving and is intrinsic to flow.
- **Congestion stock** accumulates unintentionally because of variability,
  utilization, mismatched components, or poor release control.
- **Cycle stock** results from purchasing, production, or transportation batches.
- **Safety stock** intentionally protects against uncertain demand or supply.
- **Anticipation stock** is built ahead of a known seasonal or future requirement
  to level capacity.

One physical unit can perform more than one job. Cycle stock can provide service
protection; anticipation stock can mask poor forecast or capacity policy. Assign the
dominant cause and avoid adding an independent safety allowance without accounting
for protection already provided by other stock.

## Match the Policy to the Stock

- EOQ balances order/setup frequency against average cycle stock under stable
  demand.
- A base-stock system orders one replacement per demand and isolates the safety-
  stock problem.
- Periodic review uses an order-up-to level when inventory is observed and
  replenished at scheduled intervals.
- Continuous review uses a reorder point for timing and an order quantity for size,
  combining cycle and safety stock.

The inventory position is on-hand plus on-order minus backorders. Reorder decisions
must use this position rather than the physical shelf count alone.

## Multi-Item Systems Are Coupled

Items interact when they share money, storage, ordering capacity, service targets,
machine-availability consequences, or customer baskets. Optimizing each SKU against
the same local rule does not allocate the shared resource efficiently.

For each item, retain at least:

- unit cost and annual holding cost;
- demand rate and demand variability during replenishment lead time;
- replenishment lead time and its variability;
- ordering/setup cost;
- shortage or downtime consequence;
- criticality, substitution, repairability, and pooling options.

Use item-specific order quantities and reorder points, then evaluate total
investment and weighted service across the portfolio. A common shortage-cost
parameter can act as a service “dial”; increase it when observed portfolio service
is inadequate and decrease it when stock cost dominates.

## Why Days of Supply Fails

Days of supply sets safety stock proportional to average demand. This feels fair but
ignores the variables that determine the economic and service value of protection.
It can overstock expensive items, understock inexpensive variable items, and treat
short and long replenishment lead times as equivalent.

In the chapter's four-part spare-parts example, a cost/lead-time/variability-aware
continuous-review policy achieved the same 99.82 percent average service with about
$39,114 of inventory, versus about $51,235 under a tuned 60-days-of-supply rule—
more than 30 percent less inventory for equal portfolio service. The days rule set
sensor protection too low and most other reorder points too high.

Bell & Howell found the same structural problem in practice. Its distribution
center and regional facilities used demand-only days-of-stock settings. Adding part
cost, lead time, variability, criticality, and echelon coordination identified a
potential inventory reduction of roughly 40 percent at equal service, or a smaller
reduction with improved service.

## Audit Sequence

1. Classify stock by purpose and separate congestion from intentional protection.
2. Identify whether each item is managed by base stock, periodic review, continuous
   review, or an undocumented heuristic.
3. Compare reorder parameters with cost, replenishment lead time, and lead-time
   demand variability.
4. Flag uniform days-of-supply or service rules applied across dissimilar items.
5. Define the shared constraint: investment, space, order workload, or system
   availability.
6. Allocate service jointly and plot item-level service against inventory value.
7. Pilot new settings on one item family and monitor fill rate, backorders,
   replenishment frequency, and total investment.

## Overlap Decisions

[[eoq-model-and-lot-sizing]], [[statistical-inventory-models-newsvendor-base-stock]],
and [[qr-model-and-lead-time-variability]] retain the single-item derivations and
policy mechanics. [[supply-chain-inventory-placement-and-bullwhip-control]] retains
the broader policy by raw material, WIP, FGI, and spare-parts purpose. This page
captures Chapter 7's genuinely distinct multi-item allocation logic and the
quantified days-of-supply failure.

## Connects to

[[multiechelon-inventory-and-revenue-management]],
[[supply-chain-coordination-contracts-and-information]], and
[[quality-variability-spc-and-supplier-reliability]].

## Use / Retrieval Notes

**Use when**: Every SKU carries the same days of supply, spare-parts service is
managed only by dollar value, or inventory investment rises without an explainable
portfolio-level service gain.

**Proof**: Reorder parameters vary rationally with cost, lead time, variability, and
criticality, while total portfolio service is maintained or improved with lower
inventory investment.
