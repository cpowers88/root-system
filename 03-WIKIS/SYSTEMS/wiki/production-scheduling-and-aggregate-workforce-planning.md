---
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, factory-physics, production-scheduling, aggregate-planning, workforce-planning, linear-programming, conwip, audit]
---

# Production Scheduling and Aggregate Workforce Planning

**Summary**: Scheduling balances due dates, utilization, WIP, cycle time, and
service goals that cannot all be maximized. Realistic scheduling is computationally
hard and data-sensitive, so the practical objective is a feasible, robust plan—not
a brittle mathematical optimum. Simplify the environment, quote achievable due
dates, sequence the bottleneck, diagnose WIP versus capacity infeasibility, and let
pull govern actual release. At the longer horizon, simple linear programs expose
product-mix, inventory, overtime, hiring, layoff, and subcontracting tradeoffs;
scenario robustness matters more than numerical precision.

**Source**: `factoryPhysics.pdf` (Hopp and Spearman, *Factory Physics*, 3rd ed.),
Chapters 15-16. Chapter 15 main content, "Production Scheduling" (printed pp.
516-550; physical PDF pp. 1539-1650), and Chapter 16 main content, "Aggregate and
Workforce Planning" (printed pp. 553-590; physical PDF pp. 1668-1893), were
reviewed as one coordinated planning block. Chapter 15 practice material (printed
pp. 550-552; physical pp. 1651-1667), and Chapter 16 Appendix 16A plus practice
material (printed pp. 591-602; physical pp. 1894-1941), were identified and
excluded.

**Last updated**: 2026-07-16

## Chapter Coverage

| Section | Disposition |
|---|---|
| 15.1 | Due-date, utilization, WIP, cycle-time, and service tradeoffs captured |
| 15.2 | MRP/finite-scheduling limits, classic results, dispatching, complexity, and practical implications captured |
| 15.3 | Planning/scheduling link, batch-size role, and due-date quoting captured |
| 15.4-15.5 | Bottleneck scheduling, setups, heuristics, and infeasibility diagnosis captured |
| 15.6-15.7 | Schedule-planning/pull-execution architecture and conclusions captured |
| 16.1-16.2 | Aggregate-planning purpose, horizon, inventory balance, and capacity logic captured |
| 16.3 | Multiproduct mix, floating bottlenecks, resource constraints, and extensions captured |
| 16.4-16.5 | Workforce decisions, iterative LP modeling, simplicity, and robustness captured |

## Scheduling Is a Tradeoff, Not a Single Objective

Common goals conflict:

- due dates are easier to meet with capacity slack;
- near-zero customer lead time can be purchased with large finished-goods stock;
- high utilization near capacity creates congestion unless variability is low;
- low WIP supports short cycle time, flexibility, quality feedback, and less
  forecast dependence, but cannot protect throughput without adequate capacity;
- batching similar jobs saves setup capacity but can delay other families.

Use multiple measures. Average lateness can hide late jobs behind early jobs;
tardiness counts only positive lateness. Service level alone hides the magnitude of
misses. Makespan and utilization matter only when the output is actually needed.

## Why Detailed Scheduling Fails So Often

Classic scheduling results usually assume few machines, deterministic processing,
all jobs available at time zero, no failures, no preemption, and no sequence-
dependent setups. Real plants violate most of these assumptions. Many realistic
problems are NP-hard, so commercial finite-capacity schedulers necessarily use
heuristics even when marketed as optimization.

A detailed schedule can still fail before execution begins:

- MRP creates planned releases with fixed lead times and infinite capacity.
- A bolt-on scheduler cannot make an infeasible material plan feasible.
- Deterministic job-by-machine simulation ignores the variability that controls
  congestion and becomes stale as soon as real events depart from the assumed path.
- Local dispatching is fast but myopic; it cannot see future arrivals or downstream
  consequences.

The practical standard is therefore explainable feasibility and resilience, not a
claim of plant-wide optimality.

## Solve a Better Problem

When scheduling is intractable, change the operating problem:

- reduce variability and cycle time before adding algorithmic detail;
- choose process batches for capacity and transfer batches for flow;
- quote due dates from demonstrated rate, current backlog, and transit time instead
  of accepting arbitrary promises;
- structure work into predictable CONWIP flows;
- schedule the bottleneck or a small number of shared constraints rather than every
  operation;
- use a robust sequence when exact timestamps will decay immediately.

For a CONWIP line without important setups, earliest due date (EDD) is a useful
sequence, while pull controls release timing. Shared resources can preserve that
order with FISFO. With sequence-dependent setups, group compatible work enough to
protect constraint capacity, then use a heuristic such as tabu search to improve
the feasible sequence. "Optimal" is unnecessary if the sequence is stable,
understandable, and meets the commitments that matter.

## Diagnose Infeasibility Before Rescheduling

The conveyor model separates two failure modes:

- **WIP infeasibility**: required near-term output cannot be reached because work is
  not far enough through the system. More nominal capacity does not reposition WIP;
  the near-term demand must move.
- **Capacity infeasibility**: cumulative demand exceeds demonstrated production
  capability. Move demand, add capacity, change mix, or subcontract.

This distinction prevents endless resequencing of a promise that no sequence can
save. A schedule should flag the type, location, and date of infeasibility before
offering detailed dispatch advice.

## Schedule Planning, Pull Execution

Use a schedule to rank and time prospective work, but use pull to authorize actual
release.

1. Generate a future release list from the conveyor model, MRP, or another planning
   method.
2. Organize the list by CONWIP loop and scheduled release priority.
3. Release only when the loop has an open WIP position and the job is within its
   allowed time window.
4. If the line falls behind, the cap blocks congestion-producing releases. If it
   runs ahead, the next eligible job is pulled in.
5. Use statistical throughput control and a capacity cushion to trigger corrective
   action before commitments fail.

This preserves the material-planning reach of MRP without allowing its planned
dates to override the real-time state of the factory.

## Aggregate Planning

Aggregate planning supports decisions whose consequences extend roughly one to
three years: staffing, supplier contracts, long-lead procurement, subcontracting,
capacity changes, and marketing emphasis. The model should be coarse because the
data are forecasts and the plan will be revised.

A basic time-phased model links:

`ending inventory = beginning inventory + production - sales`

subject to demand and capacity bounds. It chooses when to build inventory, accept
backlog or lost sales where allowed, use overtime, or add outside capacity. A
multiproduct model adds product-specific resource use and reveals a **floating
bottleneck**: the binding workstation can change with product mix. Include labor,
materials, transport, supplier limits, or other resources only when they can alter
the decision.

Formal optimization matters because contribution per unit is not contribution per
minute of the binding resource. Product rankings based on absorbed unit cost can
produce an inferior mix when a different resource actually constrains output.

## Workforce Planning

Workforce planning should be linked to the aggregate production plan when labor
availability, hiring delays, training, overtime, layoffs, attrition, or work rules
materially affect capacity. A useful model can compare:

- level production with inventory buffering;
- chase production with hiring and workforce reductions;
- overtime and undertime;
- subcontracting;
- delayed or forgone sales;
- cross-training and alternative labor categories.

Not every human consequence belongs in a dollar coefficient. Layoff penalties,
overtime ceilings, minimum staffing, labor agreements, and skill-preservation needs
may be better represented as explicit constraints. A mathematically cheap plan
that causes burnout, destroys trust, or loses scarce capability is not operationally
cheap.

## Modeling Discipline

- Start with the simplest formulation that can change the decision.
- Treat the first solution as a diagnostic. It often reveals a missing constraint,
  unrealistic cost, or unacceptable behavior.
- Add detail iteratively and retain traceability from each change to its effect.
- Generate several candidate plans and explain their tradeoffs; the model supports
  judgment rather than publishing "The Plan" automatically.
- Prefer linear programming for this horizon when linear approximations are
  decision-adequate. Speculative long-range data rarely justify intricate nonlinear
  or integer detail.
- Stress-test demand, capacity, cost, and policy assumptions. Robust performance
  across plausible scenarios matters more than a precise optimum for one forecast.

## Audit Sequence

1. Name the scheduling objectives and expose their conflicts.
2. Test material and capacity feasibility before optimizing sequence.
3. Separate WIP-position failures from capacity failures.
4. Identify the smallest set of true constraints that deserves scheduling.
5. Verify that actual release is gated by current WIP, not merely by planned dates.
6. Build an aggregate model with explicit inventory balance and demonstrated
   resource capacities.
7. Challenge unit-profit rankings against contribution per binding-resource unit.
8. Model labor policies as constraints where monetization would conceal the real
   decision.
9. Compare candidate plans across scenarios and document the assumptions that make
   each one fail.

## Overlap Decisions

[[capacity-planning-and-shop-floor-control]] retains Chapter 3's RCCP/CRP and
dispatch-rule mechanics. [[push-pull-conwip-and-postponement]] owns the base pull
and CONWIP laws. [[simplex-method-mechanics]] and
[[sensitivity-analysis-and-postoptimality]] retain LP solution mechanics, while
[[cost-accounting-pitfalls-abc-and-production-planning]] owns the detailed
absorbed-cost product-mix example. This page adds the Chapters 15-16 architecture
that connects feasible scheduling, pull execution, aggregate product mix, and
workforce policy.

## Connects to

[[hierarchical-pull-planning-and-shop-floor-control]],
[[variability-buffering-batching-and-diagnostic-laws]],
[[forecasting-time-series-and-exponential-smoothing]], and
[[human-laws-incentives-authority-and-change]].

## Use / Retrieval Notes

**Use when**: A finite schedule is constantly regenerated, MRP releases inflate
WIP, due dates are promised without capacity evidence, product mix ignores the
binding resource, or the workforce plan oscillates between overtime and layoffs.

**Proof**: The planning team can classify infeasibility, show a feasible constraint
sequence, demonstrate that real release obeys a WIP gate, and compare aggregate and
workforce plans across plausible demand and capacity scenarios.
