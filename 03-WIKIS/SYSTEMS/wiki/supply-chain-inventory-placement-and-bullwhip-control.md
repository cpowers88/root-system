---
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, factory-physics, supply-chain, inventory, bullwhip, spare-parts, multiechelon, audit]
---

# Supply-Chain Inventory Placement and Bullwhip Control

**Summary**: Supply-chain management is not indiscriminate inventory reduction. It
is making raw material, WIP, finished goods, and spare-parts stocks perform their
specific buffering jobs with minimum total investment. Each category requires a
different policy. Improve visibility and lead time before adding raw-material
stock; attack queue, batch, and matching delays to reduce WIP; locate finished
goods at the right inventory/order interface; separate scheduled from emergency
spares; and coordinate multiechelon policies so local optimization does not amplify
demand into bullwhip.

**Source**: `factoryPhysics.pdf` (Hopp and Spearman, *Factory Physics*, 3rd ed.),
Chapter 17, "Supply Chain Management" (printed pp. 603-645; physical PDF pp.
1942-2053), reviewed as one complete main-content chunk. Discussion, study
questions, and problems (printed pp. 646-648; physical pp. 2054-2062) were
identified and excluded.

**Last updated**: 2026-07-16

## Chapter Coverage

| Section | Disposition |
|---|---|
| 17.1-17.2 | Four inventory categories and reasons for holding each captured |
| 17.3 | Visibility, ABC, JIT, safety lead time/stock, and order-frequency policies captured |
| 17.4 | Queue, wait-for-batch, and wait-to-match WIP reduction captured |
| 17.5 | FGI purpose and inventory/order-interface choices captured |
| 17.6 | Scheduled versus emergency spare-parts logic captured |
| 17.7 | Multiechelon structure, measures, bullwhip, and two-level approximation role captured |
| 17.8 | Structural-change and continual-improvement conclusions incorporated |

## Start With the Job of the Inventory

| Inventory | Legitimate jobs | Primary improvement levers |
|---|---|---|
| Raw material | purchase/delivery batching; protection from supply, schedule, and yield variability | demand visibility, shorter production and supplier lead times, supplier reliability, differentiated purchasing policies |
| WIP | buffers process variability and utilization; waits for batches or matching components | variability reduction, capacity slack, smaller move batches, synchronization, pull |
| Finished goods | shields customers from manufacturing time, demand variability, and seasonal capacity mismatch | shorter/predictable cycle time, dynamic quoting, postponement, pooling, interface placement |
| Spare parts | enables planned maintenance and rapid emergency repair | separate predictable demand from stochastic failures, criticality-based service, pooling |

Obsolete stock is not a buffer. Once demand or design has invalidated its purpose,
dispose of it and correct the policy that created it rather than continuing to count
it as usable protection.

## Raw Materials: Divide and Conquer

Use ABC classification by annual purchase value to focus attention, but supplement
it with bulk, outage criticality, lead time, and handling risk.

- **A parts** merit schedule visibility, frequent review, short supplier lead time,
  lot-for-lot ordering, or genuine JIT synchronization. A higher unit price can be
  cheaper overall when it buys shorter lead time, reliability, and flexibility.
- **B parts** use an intermediate policy based on value and risk.
- **C parts** usually do not justify tight schedule synchronization. Use economical
  replenishment, simple two-bin/base-stock signals, or supplier-managed stock so
  transaction cost and outage risk do not overwhelm tiny carrying-cost savings.

JIT purchasing is a relationship and information design, not merely smaller trucks.
Share schedule changes early, define allowable quantity changes, and account for
transportation and ordering cost. Daily delivery that cuts stock but multiplies
freight or supplier fragility can reduce local inventory while worsening the total
system.

Safety stock and safety lead time protect against the same uncertainty in different
forms. Estimate the combined variability of requirement timing, supplier delivery,
and yield. Do not add both independently without recognizing the double buffer.

## WIP: Remove the Cause of Waiting

For fixed throughput, Little's Law makes WIP reduction and cycle-time reduction the
same problem. Most WIP in disconnected flows is in one of three states:

1. **Queueing**: reduce utilization where economically justified, lower arrival and
   effective-process-time variability, add targeted capacity, and keep releases
   from overwhelming the line.
2. **Waiting for a batch**: separate process batches from move batches; split lots,
   use flow-oriented layouts, reduce handling/setup effort, and move completed units
   before the entire process batch finishes.
3. **Waiting to match**: synchronize component releases with assembly, use pull from
   assembly completions, set different WIP levels for fabrication paths of different
   length, and improve reliability on the path that frequently delays kits.

Cutting visible WIP without changing any of these mechanisms simply relocates the
buffer into lost throughput or late orders.

## Finished Goods and the Inventory/Order Interface

FGI is the point where production time is hidden from the customer. Reduce it by
shortening and stabilizing cycle time, dynamically quoting lead time from current
load, postponing differentiation, and pooling common stock before customization.

The correct question is not “make to stock or make to order?” for the whole company.
It is where each product family's inventory/order interface should sit. Move it
downstream for rapid response when demand is predictable and proliferation is low;
move it upstream to preserve flexibility and pooling when variants are numerous or
obsolescence is costly.

## Spare Parts

- **Scheduled preventive-maintenance parts** have derived, predictable demand. MRP,
  netting, and ordinary lot sizing are appropriate.
- **Emergency-repair parts** have stochastic, often intermittent demand. Use a
  service-based inventory model, machine criticality, replenishment time, commonality,
  repairability, and downtime exposure.

A missing low-cost fuse can stop the same machine as a missing expensive controller,
so purchase value alone is a poor criticality measure. Pool rare expensive spares
centrally when transport response is acceptable; distribute critical fast-response
items near equipment when downtime dominates carrying cost.

## Multiechelon Coordination and Bullwhip

Central stock pools variability and reduces safety inventory; distributed stock
responds faster. Choose the network using customer-level fill rate, backorder delay,
availability, and total inventory—not the warehouse's local service alone.

Bullwhip arises when each echelon independently forecasts, batches, ration-games,
and reacts to the orders of the next echelon rather than to final demand. Reduce it
through:

- shared end-demand and inventory-position data;
- smaller, steadier replenishment batches;
- stable pricing that avoids forward buying;
- allocation rules that do not reward inflated shortage orders;
- coordinated base-stock/reorder policies across levels;
- lead-time and variability reduction.

Local optima are especially dangerous here: each node can improve its own metric
while increasing total stock and upstream variance.

## Audit Sequence

1. Classify every material stock as raw material, WIP, FGI, spare, or obsolete.
2. Record the explicit batching, variability, timing, or service purpose of each.
3. Segment purchased items by value, criticality, bulk, and replenishment risk.
4. Decompose WIP into queue, batch, and match waiting.
5. Locate each product family's inventory/order interface.
6. Separate preventive-maintenance spares from emergency spares.
7. Map information and replenishment signals across echelons and compare their
   variance with final demand.
8. Evaluate changes on total landed cost, customer service, and total inventory.

## Overlap Decisions

Existing EOQ, base-stock, and `(Q,r)` pages retain model mechanics.
[[variability-buffering-batching-and-diagnostic-laws]] owns the general buffer and
batch laws. [[push-pull-conwip-and-postponement]] owns the inventory/order-interface
definition. [[multiechelon-inventory-and-revenue-management]] retains the separate
OR textbook's deterministic echelon-stock optimization. This page adds Chapter
17's integrated policy by inventory type, spare-parts stratification, and bullwhip
control.

## Connects to

[[stock-management-structure-and-amplification]],
[[manufacturing-supply-chain-model]],
[[supply-chain-interactions-and-trust]], and
[[quality-variability-spc-and-supplier-reliability]].

## Use / Retrieval Notes

**Use when**: Inventory reduction is being pursued as one undifferentiated target,
sites optimize replenishment independently, raw-material shortages coexist with
excess stock, or spare-parts value does not match downtime risk.

**Proof**: Each major stock has a named purpose, owner, service target, and policy;
WIP is decomposed by waiting cause; and a network-level measure prevents local
inventory savings from increasing total cost or bullwhip.
