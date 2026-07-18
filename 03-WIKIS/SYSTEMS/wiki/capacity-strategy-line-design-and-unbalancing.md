---
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, factory-physics, capacity-strategy, line-design, cycle-time, bottleneck, facility-design, audit]
---

# Capacity Strategy, Line Design, and Deliberate Unbalancing

**Summary**: Capacity is a strategic buffer, not merely a cost to minimize or a
utilization percentage to maximize. A capacity-feasible line can still fail its
cycle-time promise because congestion rises nonlinearly near full utilization.
Design and improvement must therefore minimize cost subject to throughput and
cycle-time constraints, compare added machines with variability reduction, and
build from customer requirements toward processes, equipment, and facilities.
Ordinary flow lines should usually be intentionally unbalanced; classic line
balancing belongs mainly to paced assembly.

**Source**: `factoryPhysics.pdf` (Hopp and Spearman, *Factory Physics*, 3rd ed.),
Chapter 18, "Capacity Management" (printed pp. 649-665; physical PDF pp.
2063-2106), reviewed as one complete main-content chunk. Appendix 18A, study
questions, and problems (printed pp. 666-670; physical pp. 2107-2122) were
identified and excluded.

**Last updated**: 2026-07-16

## Chapter Coverage

| Section | Disposition |
|---|---|
| 18.1 | Short/long-term options, strategic questions, scale, and modern capacity view captured |
| 18.2 | Queueing-network model and capacity-versus-cycle-time feasibility captured |
| 18.3 | Existing-line improvement heuristic and variability alternatives captured |
| 18.4 | Customer-backward new-line/facility design captured |
| 18.5 | Paced assembly versus flow-line balancing and deliberate unbalancing captured |
| 18.6 | Strategic, modeling, economic, and human conclusions incorporated |

## Capacity Decisions Cascade Through the System

Capacity strategy specifies how much, when, where, and what type of capability to
provide. It also decides whether to lead or lag demand, expand in large or small
increments, centralize or distribute, automate or retain flexibility, and make or
outsource.

Short-term options include overtime, shifts, temporary labor, subcontracting, and
workforce changes. Long-term choices include equipment, process technology,
facilities, skill development, and supplier capability. Outsourcing can provide
flexibility but may surrender process knowledge, supply control, or a future route
to competition.

The traditional view treats unused capacity as waste and aims to minimize the cost
of meeting average volume. The modern view recognizes that capacity buffers
variability and protects cycle time, delivery reliability, quality response, and
the rest of the planning hierarchy. Utilization is an input to congestion, not a
standalone objective.

## Capacity Feasibility Is Not Performance Feasibility

A **minimum-cost, capacity-feasible** configuration gives every station nominal
capacity above target throughput. It does not guarantee an acceptable cycle time.
At a station near full utilization, queue time can dominate processing time even
when average demand is technically below capacity.

Use two gates:

1. **Throughput gate**: every station has practical capacity above the target rate.
2. **cycle-time gate**: a variability-aware queueing model predicts total cycle time
   within the customer requirement at that rate.

If the second gate fails, compare options by cycle-time reduction per dollar:

- add a machine or labor increment;
- reduce failures or repair time;
- externalize or reduce setups;
- reduce arrival variability;
- change routing or product assignment;
- improve yield and eliminate rework load.

The cheapest capacity purchase is not necessarily the cheapest compliant system.
A reliability or variability change can outperform another machine, while a cheap
parallel resource can provide more value than protecting an expensive bottleneck
with excessive WIP.

## Existing-Line Improvement Heuristic

1. Establish target throughput and cycle time.
2. Find the minimum-cost capacity-feasible configuration.
3. predict station and total cycle time using demonstrated mean and variability.
4. If the target fails, enumerate discrete equipment and variability-reduction
   options.
5. Select the best cycle-time improvement per incremental dollar.
6. Recalculate the entire network because moving one constraint changes arrival
   and downstream behavior.
7. Repeat until both throughput and cycle-time constraints are met.
8. Stress-test demand mix, failures, setups, and capacity increments.

This is a heuristic, not a claim of global optimum. Its value is making the
tradeoffs explicit and repeatedly checking whole-line performance.

## Design New Lines From the Customer Backward

Traditional facility design often starts with a building shape or equipment list
and then fits flow around it. Reverse the sequence:

1. customer requirements determine product mix, volume, service, and cycle time;
2. products determine process recipes;
3. processes determine candidate machines and labor systems;
4. machines determine utilities, handling, storage, support, and space;
5. these requirements determine facility structure and size.

Then iterate cost and feasibility. Product lives may be shorter than equipment
lives, so value flexibility, reconfigurability, expansion paths, learning curves,
maintenance access, material handling, safety, environmental constraints, and
operator capability—not just purchase price and rated speed.

Generate a cost-versus-performance frontier rather than one “optimal” design. A
strategic decision maker can then see what additional cycle-time or flexibility
performance costs and choose a target consistent with market objectives.

## Why Flow Lines Should Usually Be Unbalanced

For an ordinary flow line, equal capacity at every station is rarely economical or
operationally desirable:

- balanced high-utilization stations compound congestion and create ambiguous,
  floating constraints;
- equipment prices and capacity increments differ;
- variability and reliability differ by station;
- cheap, finely divisible capacity should not be allowed to constrain an expensive
  line;
- one visible, stable bottleneck is easier to protect and manage.

Place the planned bottleneck where capacity arrives in large, expensive increments,
then keep inexpensive flexible operations safely above its capability. This is
deliberate unbalancing, not neglect.

Classic line-of-balance methods are appropriate for **paced assembly lines**, where
the belt or pacing mechanism sets the rate and work elements can be divided among
stations. They do not transfer directly to independent-machine flow lines.

## Audit Sequence

1. State the throughput, cycle-time, service, mix, and flexibility requirements.
2. Replace rated capacity with demonstrated effective capacity and variability.
3. Test both capacity feasibility and cycle-time feasibility.
4. Price variability reduction beside equipment additions.
5. Identify whether the current bottleneck is stable, floating, or accidental.
6. Check whether cheap capacity is being run as a constraint to preserve a local
   utilization metric.
7. For new facilities, trace requirements customer → product → process → machine →
   facility.
8. Present a cost/performance frontier and scenario results, not a single precise
   forecast.

## Overlap Decisions

[[capacity-planning-and-shop-floor-control]] retains RCCP/CRP mechanics.
[[factory-dynamics-definitions-bottleneck-rate-and-critical-wip]] and
[[vut-equation-and-parallel-machines]] retain the underlying factory-dynamics and
queueing derivations. [[production-scheduling-and-aggregate-workforce-planning]]
owns shorter-horizon capacity and labor choices. This page adds Chapter 18's
strategic line-design procedure, dual feasibility gate, improvement heuristic, and
deliberate-unbalancing rule.

## Connects to

[[practical-worst-case-and-bottleneck-investment-tradeoffs]],
[[variability-buffering-batching-and-diagnostic-laws]],
[[strategic-objectives-hierarchy-and-efficient-frontiers]], and
[[factory-physics-implementation-synthesis-and-team-focus]].

## Use / Retrieval Notes

**Use when**: A line meets nominal rate on paper but misses cycle time, a capital
request assumes balanced utilization is ideal, or a new facility begins with a
building/equipment layout instead of customer performance requirements.

**Proof**: The proposed configuration passes both throughput and variability-aware
cycle-time gates, the chosen bottleneck is intentional, and alternatives are shown
on a cost/performance frontier under plausible scenarios.
