---
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, supply-chain-science, coordination, contracts, bullwhip, information, inventory-order-interface, audit]
---

# Supply-Chain Coordination, Contracts, and Information

**Summary**: Multilevel supply chains fail when stocking, ordering, pricing, and
information policies are optimized locally. Coordination requires joint inventory
placement, deliberate inventory/order-interface design, bullwhip controls,
risk-sharing contracts, accurate shared data, and structural simplification.
Technology only helps when records are trustworthy and decision rules actually use
lead-time, variability, reliability, and customer-criticality information.

**Source**: `suppyChainScience.pdf` (Wallace J. Hopp, *Supply Chain Science*),
Chapter 9, "Coordination" (printed pp. 179-215; physical PDF pp. 193-229), reviewed
as one complete main-content chunk. Questions for Thought begin on the shared
printed p. 215 / physical p. 229 and continue through printed p. 217 / physical
pp. 230-231; they were identified and excluded as practice material.

**Last updated**: 2026-07-16

## Chapter Coverage

| Section | Disposition |
|---|---|
| 9.1-9.2 | Multilevel structures, local decomposition limits, and inventory placement captured |
| 9.3 | Pooling/proximity and inventory/order-interface position captured |
| 9.4 | Bullwhip causes and countermeasures captured |
| 9.5 | Double marginalization and risk-sharing contract families captured |
| 9.6 | Data collection, accuracy, sharing, use, and ERP/change limits captured |
| 9.7 | Level elimination, virtual pooling, product platforms, VMI/CPFR, and restructuring captured |

## Coordinate the Hierarchy, Not Just Each Node

A stock point's demand pattern is created by policies below it; replenishment lead
time, batching, and reliability are created by policies above it. Treating a
warehouse or store as an isolated inventory problem hides these dependencies.

For each item and echelon, decide jointly:

- where stock belongs;
- which level owns the service target;
- how downstream orders translate into upstream demand;
- how replenishment delays and batches propagate;
- who controls inventory and bears surplus/shortage risk.

Central locations offer pooling; local locations offer proximity. Low-volume,
high-cost, or highly variable parts tend toward central stocking. Low-cost,
predictable, response-critical parts can justify local stock. Criticality and
cross-shipping feasibility can override simple volume rules.

## Position the Inventory/Order Interface

The inventory/order interface is where flow switches from make-to-stock to
make-to-order.

- Long production lead times push the interface toward the customer if fast response
  must be protected with differentiated stock.
- High product proliferation pulls it upstream so generic inventory can be pooled
  and customization delayed.
- Postponement, modular product design, and short cycle time can improve both sides
  of the tradeoff.

Design the interface by product family rather than imposing one make-to-stock or
make-to-order identity on the entire company.

## Bullwhip Is Policy-Generated Variability

Demand variance grows upstream through:

1. order and transportation batching;
2. repeated local forecasting and forecast-error correction;
3. promotions and forward buying;
4. shortage gaming and inflated orders.

Reduce bullwhip through smaller batches, stable pricing, allocation based on actual
sales rather than inflated orders, shared point-of-sale demand, shorter lead times,
and coordinated replenishment. Information sharing is necessary but insufficient:
decision rules must stop converting small demand changes into large order changes.

## Risk-Sharing Contracts

Separate firms often produce **double marginalization**: each adds a margin, while
inventory risk falls disproportionately on the downstream buyer. The retailer then
stocks less than the quantity that maximizes total supply-chain profit.

Coordination contracts change the risk/reward structure:

- **buyback**: supplier repurchases unsold stock, lowering the retailer's overage
  risk;
- **quantity flexibility**: retailer may return a limited quantity at the wholesale
  price;
- **revenue sharing**: supplier lowers upfront price in exchange for part of sales
  revenue;
- **sales rebate**: supplier raises the retailer's marginal reward above a sales
  threshold.

The contract should make the locally rational order equal or approximate the
system-optimal order. A fixed transfer payment can redistribute profit without
distorting that marginal decision. Contract performance still depends on compatible
demand forecasts, trustworthy measurement, enforceability, and the parties' power.

## Information: Collect, Share, Use

### Collect accurately

Inventory records, location accuracy, original promise dates, failure/repair data,
and supplier delivery distributions must reflect physical reality. Changing a late
order's due date in the database destroys the evidence needed to improve supplier
performance.

### Share with the decision owner

One logical data source is preferable to unsynchronized departmental copies, but
ERP installation is a change-management program, not a turnkey coordination fix.
Across firms, sharing requires commercial trust, access rules, and aligned
incentives.

### Use the distribution, not only the average

Managers routinely collect MTTF, MTTR, supplier delivery, demand, and service data
but collapse them into availability percentages, averages, or one-number forecasts.
Preserve variability and tail behavior so models can distinguish long rare outages
from short frequent ones and severe lateness from harmless earliness.

## Restructure When Tuning Is Not Enough

Large gains may require changing the network:

- remove an echelon and use direct fulfillment;
- create a virtual distribution center through visibility and cross-shipping;
- standardize components and postpone differentiation;
- reduce unnecessary parts and suppliers while checking concentration risk;
- transfer inventory authority through VMI, consignment, or CPFR;
- redesign products and processes around pooled generic resources.

The closing rule is: practices progress, but principles persist. Direct marketing,
VMI, cross-docking, product platforms, and supplier partnerships are different ways
to exploit pooling, shorter lead time, aligned incentives, and shared information.

## Audit Sequence

1. Map material, order, forecast, and ownership flows by echelon.
2. Compare final demand variability with order variability at every upstream level.
3. Locate the inventory/order interface for each major family.
4. Identify who bears overage and shortage risk and test whether the contract aligns
   local orders with total profit.
5. Reconcile physical inventory with records and preserve original promise dates.
6. Check whether shared data change an actual decision rule.
7. Evaluate echelon removal, cross-shipping, component commonality, or authority
   transfer before merely tuning reorder points.

## Overlap Decisions

[[supply-chain-inventory-placement-and-bullwhip-control]] retains the integrated
inventory-type and Chapter 17 bullwhip policy. [[push-pull-conwip-and-postponement]]
retains the base inventory/order-interface and postponement mechanics.
[[multiechelon-inventory-and-revenue-management]] retains formal echelon-stock
optimization. This page adds Chapter 9's interfirm incentive layer, risk-sharing
contract families, information quality/use discipline, and structural redesign
options.

## Connects to

[[supply-chain-risk-pooling-and-crisis-readiness]],
[[supply-chain-interactions-and-trust]],
[[manufacturing-supply-chain-model]], and
[[multi-item-inventory-policy-and-service-allocation]].

## Use / Retrieval Notes

**Use when**: Retail and supplier forecasts disagree, promotions create order
spikes, ERP data are plentiful but unreliable, or contracts shift risk without
aligning systemwide profit.

**Proof**: Order variance falls toward final-demand variance, physical and recorded
inventory reconcile, risk-sharing changes the marginal stocking decision, and
shared information is tied to named replenishment or allocation rules.
