---
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, factory-physics, push-pull, conwip, wip-control, postponement, audit]
---

# Push, Pull, CONWIP, and Postponement

**Summary**: Pull is not defined by cards, make-to-order production, or workers
physically retrieving material. A pull system sets an advance limit on WIP; a push
system does not. The WIP cap explains pull's lower average WIP and cycle time,
greater cycle-time predictability, pressure for quality improvement, and retained
flexibility. CONWIP provides the simplest general cap by releasing one job when one
leaves. The inventory/order interface then locates where flow changes from
make-to-stock to make-to-order, trading response speed against customization and
inventory pooling.

**Source**: `factoryPhysics.pdf` (Hopp and Spearman, *Factory Physics*, 3rd ed.),
Chapter 10, "Push and Pull Production Systems" (printed pp. 356-381; physical PDF
pp. 1104-1170), reviewed as one complete chapter-content chunk. Study questions
and problems (printed pp. 381-383; physical pp. 1171-1175) were identified and
excluded from synthesis.

**Corroborating source disposition**: `suppyChainScience.pdf` (Wallace J. Hopp,
*Supply Chain Science*), Chapter 6, "Push/Pull" (printed pp. 95-110; physical PDF
pp. 109-124), reviewed in full on 2026-07-16. Its definition, examples, WIP-cap
benefits, push/CONWIP comparisons, and implementation continuum corroborate the
framework below without adding a distinct retrieval layer. Questions for Thought
(printed pp. 111-113; physical pp. 125-127) were identified and excluded.

**Last updated**: 2026-07-16

## Chapter Coverage

| Section | Disposition |
|---|---|
| 10.1-10.2 | Push/pull definition, trigger distinction, and hybrid reality captured |
| 10.3 | Cost, variability, quality, flexibility, and work-ahead effects captured |
| 10.4 | CONWIP mechanics and mean-value-analysis role captured |
| 10.5 | Observability, efficiency, variability, and robustness comparisons captured |
| 10.6 | Card count, product mix, people, and inventory/order-interface comparisons captured |
| 10.7 | Six-point conclusion incorporated |

## The Controlling Definition

- A **push system** schedules releases from information outside the production
  system, such as actual or forecast demand, without an advance WIP ceiling.
- A **pull system** authorizes releases from internal system status and establishes
  an advance limit on WIP.

The release trigger alone is insufficient. A worker can physically "pull" material
without changing system behavior. Pull works when its signal represents an open WIP
position. Most real systems are hybrids: MRP users modify releases for shop status,
while pull systems may delay an authorized release because forecast demand does not
justify it.

## Why the WIP Cap Matters

A WIP cap:

- prevents congestion from becoming a WIP explosion after disruption;
- holds work as flexible information longer instead of prematurely giving it
  physical form and priority;
- uses less average WIP for a given throughput than an equivalent pure push line;
- prevents cycle-time explosions and narrows the range of customer lead-time
  outcomes;
- exposes failures, setups, rework, and weak quality that excess inventory masks;
- shortens the delay between producing and detecting a defect.

These benefits come from controlled WIP, not from cards themselves. Low WIP does
not remove variability; it makes the system vulnerable enough that variability must
be reduced to retain throughput.

## CONWIP

CONWIP means **constant work in process**. One line-level card returns to the front
when a completed job leaves, authorizing the next item on a release list. Within the
line, material flows forward without workstation-specific card limits.

### Compared with pure push

- WIP is directly observable; true capacity and a safe release rate are not.
- For equal throughput, CONWIP requires less average WIP and therefore less average
  cycle time.
- The control target is more robust: errors in the card count degrade performance
  more gradually than comparable errors in a push release rate.
- Work can advance when conditions are favorable without allowing unlimited WIP.

### Compared with kanban

- One line card count is simpler than a card count at every workstation.
- A release list handles low-volume items and changing product mix without keeping
  every part permanently represented in stock.
- WIP naturally accumulates before the active bottleneck, including a bottleneck
  that moves as product mix changes.
- Midline operators can work whenever material is present, reducing the pacing
  stress created by station-by-station authorization.

Kanban can provide tighter local control and encourage adjacent-worker interaction,
but quality acceptance and cooperation can be designed independently through
buy-sell handoffs, cross-training, and line-level measures.

## Inventory/Order Interface and Postponement

The inventory/order interface is the point where material flow changes from
make-to-stock replenishment to make-to-order response.

- Moving it **toward the customer** stocks more specialized output and provides
  faster response, but reduces flexibility and can multiply finished-goods stock.
- Moving it **upstream** preserves generic inventory and customization flexibility,
  but exposes the customer to more production time.

Choose the interface using customer-perceived speed, product proliferation, process
feasibility, and pooling economics. Postponement redesigns the product/process to
delay differentiation: generic printers receive country-specific power supplies in
regional distribution, or undyed sweaters are colored after demand is known. This
can reduce both customer lead time and safety stock by pooling demand before
customization.

## Audit Sequence

1. Find the actual release authorization, not the label used for the system.
2. Determine whether an enforceable WIP ceiling exists and where it applies.
3. Measure WIP, throughput, mean cycle time, and cycle-time spread together.
4. Check whether local card counts fight a changing mix or moving bottleneck.
5. Ask whether one line-level cap plus a release list would be simpler.
6. Locate the inventory/order interface and quantify the speed/flexibility trade.
7. Look for a generic intermediate form that permits late customization.

## Overlap Decisions

[[kanban-mechanics-and-pull-system-variants]] retains the Chapter 4 card mechanics
and base-stock equivalence. [[mrp-history-and-push-pull-paradigm]] retains the
historical MRP contrast. This page adds Chapter 10's formal WIP-cap definition,
CONWIP comparison laws, moving-bottleneck logic, and inventory/order-interface
placement.

## Connects to

[[variability-buffering-batching-and-diagnostic-laws]],
[[variability-pooling-and-chapter-8-conclusions]],
[[capacity-planning-and-shop-floor-control]], and
[[jit-implementation-tactics-and-quality-revolution]].

## Use / Retrieval Notes

**Use when**: Releases outrun completion, WIP and lead time swing widely, a kanban
system is too rigid for product mix, or customization creates excessive finished
goods inventory.

**Proof**: A bounded pilot enforces the chosen cap and demonstrates the throughput,
WIP, cycle-time, quality, and service effects without relying on the pull label.
