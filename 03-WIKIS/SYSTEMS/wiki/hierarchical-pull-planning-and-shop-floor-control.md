---
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, factory-physics, production-planning, shop-floor-control, conwip, feedback, audit]
---

# Hierarchical Pull Planning and Shop-Floor Control

**Summary**: Production planning should be disaggregated because no single model
can resolve strategic capacity, tactical product mix, and real-time releases at
once. The hierarchy works only when its modules use consistent assumptions and
receive feedback from actual output. In a pull environment, aggregate plans become
WIP caps and quotas; schedules guide sequence; shop-floor control decides actual
release and response. CONWIP is the simplest incumbent control, extended only when
routings, shared resources, assemblies, setups, or span of control justify the
added complexity.

**Source**: `factoryPhysics.pdf` (Hopp and Spearman, *Factory Physics*, 3rd ed.),
Chapters 13-14. Chapter 13 main content, "A Pull Planning Framework" (printed pp.
435-473; physical PDF pp. 1291-1411), and Chapter 14 main content, "Shop Floor
Control" (printed pp. 483-511; physical PDF pp. 1452-1526), were reviewed as one
coordinated planning-and-execution chunk. Chapter 13 Appendix 13A and practice
material (printed pp. 474-482; physical pp. 1412-1451), plus Chapter 14 Appendix
14A and practice material (printed pp. 512-515; physical pp. 1527-1538), were
identified and excluded.

**Last updated**: 2026-07-16

## Chapter Coverage

| Section | Disposition |
|---|---|
| 13.1-13.2 | Synthesis purpose; disaggregation by time, process, product, and people; coordination captured |
| 13.3 | Forecasting's planning role and qualitative override captured; method details routed to existing forecasting pages |
| 13.4 | Pull-planning advantages and conveyor-model role captured |
| 13.5-13.6 | Complete hierarchy, module links, feedback, and environment-specific design captured |
| 14.1-14.2 | SFC role, gross capacity, bottleneck limits, and span of control captured |
| 14.3-14.4 | Basic and extended CONWIP configurations plus alternative pull mechanisms captured |
| 14.5-14.6 | Statistical throughput control, capacity tracking, feedback, and conclusions captured |

## Why Planning Must Be Hierarchical

Real production systems are too complex for one model. Disaggregate the decision
space along four dimensions:

- **time**: long-range strategy, intermediate tactics, and short-range control;
- **process**: distinct technologies or operating areas;
- **product**: families at longer horizons and specific part numbers near execution;
- **people**: bounded managerial attention and workable spans of control.

Detail should increase as the horizon shortens. A detailed schedule built on a
speculative long-range forecast creates false precision, while a coarse aggregate
plan cannot guide today's release decision. The hierarchy is valuable only if the
subproblems are coordinated. Capacity, staffing, demand, yield, and timing
assumptions must reconcile across modules.

## Planning Is a Closed Loop

The planning hierarchy is not a one-way cascade from forecast to floor. It is a
closed loop:

1. Forecasts and business choices establish long-range demand expectations.
2. Capacity/facility and workforce plans establish plausible resource envelopes.
3. Aggregate planning selects product volumes and timing within those envelopes.
4. WIP and quota setting translate the aggregate plan into pull controls.
5. Demand management shapes orders into a manageable master plan.
6. Sequencing and scheduling propose order and release timing.
7. Shop-floor control authorizes real releases and adapts to disruptions.
8. Production tracking updates capacity, variability, yield, and progress data.

Without the return path, optimistic capacity estimates and inconsistent data can
survive indefinitely. Feedback must support problem solving rather than blame;
otherwise people learn to hide the very deviations the hierarchy needs to see.

## Planning for Pull

Pull does not eliminate planning. It changes the parameters that planning sets.

- **WIP/card count** is a tactical control, not a throttle to adjust every time
  demand changes. Throughput responds slowly and weakly to frequent WIP changes.
- **Production quota** links a WIP-capped line to due-date commitments. A capacity
  cushion makes quota attainment reliable despite ordinary variability.
- **Release sequence** communicates demand priority, while the pull mechanism
  decides when physical work can enter.
- **Demand management** levels and groups orders where possible so the factory does
  not inherit every fluctuation in the order stream.

The result is a conveyor-like planning model: estimate a practical production rate
and transit time, then use quotas and WIP limits to keep real behavior close enough
to that model for commitments to be credible.

## Shop-Floor Control Is More Than Routing

Shop-floor control (SFC) is where the plan meets the evolving process. It must:

- control releases and material movement;
- adapt sequence when failures, missing components, rework, or hot jobs occur;
- show whether the plant is on pace for the current quota or schedule;
- collect actual capacity and variability data for higher planning modules;
- keep the control burden proportional to the plant's real complexity.

No schedule can anticipate every random disruption. Treat it as guidance, then
constrain real-time choices to a small, robust action set rather than continually
rebuilding a theoretically optimal plant-wide schedule.

## CONWIP as the Incumbent Design

Start with the simplest workable CONWIP configuration and require evidence before
adding complexity.

### Basic loop

A fixed set of cards or authorizations caps WIP in a product flow. Completion
returns an authorization to the release point. Cards identify capacity positions,
not product types, so a release list can change mix without redesigning the loop.

### Configuration rules

- Group similar routings into a small number of product flows. Routing differences
  add variability and therefore require more WIP or accept less throughput.
- Split a long line into tandem loops when span of control or operational
  independence justifies the buffer cost. More loops move the design toward kanban:
  tighter local control, but more WIP parameters and coordination points.
- At an interior shared resource, FISFO preserves system-level demand order. Split
  loops around the resource only when stronger downstream priority signaling is
  worth the additional buffers and controls.
- When products have very different processing requirements, cap workload rather
  than raw unit count, using bottleneck or total standard hours where defensible.
- In assembly, coordinate component loops from assembly completions. Different
  fabrication lead times can justify different loop WIP levels.

Kanban is appropriate when station-level signaling and communication are valuable
and the environment is repetitive enough to support many local caps. Pull from the
bottleneck can help when downstream failures would starve a constraint or when
ordinary CONWIP would release work far before its due-date window. These are
extensions, not automatic upgrades.

## Statistical Throughput Control

Statistical throughput control (STC) applies control-chart logic to cumulative
production rather than defect measurements. During a shift, week, or other quota
period, compare actual cumulative output with the expected path and its variability
band. An early low-side signal creates time to arrange overtime, move labor, or
correct a disruption before the commitment is missed.

The same output history should update the mean and standard deviation of regular-
time capacity used by aggregate planning, workforce planning, and quota setting.
Rated speed minus guessed detractors is not demonstrated capacity. When quota
achievement stops production early, track time-to-quota instead so the estimate is
not artificially capped.

## Audit Sequence

1. Map every planning module, its horizon, owner, inputs, outputs, and regeneration
   frequency.
2. Compare capacity, staffing, yield, and demand assumptions across modules.
3. Trace one order from forecast through aggregate plan, quota, schedule, release,
   completion, and feedback.
4. Identify the actual WIP cap and test whether it is changed too frequently.
5. Start with one CONWIP loop per coherent flow; document why every added loop or
   exception exists.
6. Measure cumulative output against a statistically credible quota path.
7. Feed demonstrated capacity and variability back upstream without using the data
   to punish truthful reporting.

## Overlap Decisions

[[forecasting-time-series-and-exponential-smoothing]] retains forecasting method
mechanics, while this page keeps forecasting's role in the PPC hierarchy.
[[push-pull-conwip-and-postponement]] owns the formal push/pull definition and base
CONWIP comparison. [[capacity-planning-and-shop-floor-control]] retains Chapter 3's
MRP-era RCCP, CRP, dispatching, and I/O-control critique. This page adds Chapters
13-14's closed-loop pull hierarchy, configurable SFC architecture, STC, and
feedback discipline.

## Connects to

[[production-scheduling-and-aggregate-workforce-planning]],
[[variability-buffering-batching-and-diagnostic-laws]],
[[human-laws-incentives-authority-and-change]], and
[[quality-variability-spc-and-supplier-reliability]].

## Use / Retrieval Notes

**Use when**: Plans disagree across horizons, schedules are routinely overridden,
the plant cannot state its demonstrated capacity, or a pull implementation has
accumulated too many cards, loops, and exceptions to explain.

**Proof**: One product flow has reconciled assumptions from aggregate plan through
release; an explicit WIP cap; a quota with a variability band; and a feedback cycle
that changes upstream parameters when actual performance changes.
