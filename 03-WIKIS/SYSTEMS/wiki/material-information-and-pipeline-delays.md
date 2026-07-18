---
domain: systems
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, system-dynamics, delays, information-flow, material-flow, audit]
---

# Material, Information, and Pipeline Delays

**Summary**: Every delay contains accumulation. The same average delay can produce
very different behavior depending on whether it conserves material, smooths
information, preserves sequence, or mixes items across stages. Modeling only the
average hides the distribution, instability, and operational state inside the delay.

**Source**: BusinessDynamics.pdf (Sterman, Business Dynamics, 2000), Chapter 11,
"Delays" (printed pp. 409-467; physical PDF pp. 434-492), reviewed as one
complete chapter chunk.

**Last updated**: 2026-07-15

## Chapter Coverage

| Source section | Disposition |
|---|---|
| 11.1 Introduction | Definition, stock requirement, and dynamic role captured |
| 11.2 Material delays | Pipeline, first-order, higher-order, Little's Law, and input-response behavior captured |
| 11.3 Information delays | Adaptive expectations, exponential smoothing, and higher-order perception captured |
| 11.4 Variable delay times | Material/information differences and ratchet effects captured |
| 11.5 Estimating delays | Numerical estimation, judgmental decomposition, and "walk the line" fieldwork captured |
| 11.6 Semiconductor forecasting | Design-win pipeline and operational forecasting lesson captured |
| 11.7 Mathematics | Koyck/geometric and Erlang/Pascal interpretations retained conceptually |
| 11.8 Summary | Delay-selection and evidence guidance incorporated |

## Every Delay Contains a Stock

A delay's output differs from its input over time. The difference must accumulate
somewhere: letters in transit, work in process, candidates in hiring, buildings under
construction, unreported incidents, or a perceived value that has not yet caught up
with reality.

If a process is described as "taking time" but the model contains no stock or state
representing what is waiting, moving, learning, or being perceived, the delay is
probably implicit or missing.

## Two Characteristics Must Be Specified

Every delay requires:

1. **Mean delay time** - the average residence or adjustment time.
2. **Output distribution** - how completions are spread around that average.

Two processes with the same mean can behave differently. One may produce some
output immediately with a long tail; another may produce nothing until a narrow
completion window; a pipeline may reproduce the input exactly after a fixed lag.

## Material and Information Delays

| Property | Material delay | Information delay |
|---|---|---|
| What moves | Conserved items, work, people, money, or physical units | A perception, estimate, average, or belief |
| Internal state | Quantity in transit or in process | Smoothed/perceived value |
| Output | Exit flow from the stock | The current perceived state |
| Conservation | Inflow minus outflow changes the stock | Old information need not physically exit |
| Variable delay time | Changes can release or trap accumulated material | Changes alter the speed of adjustment without conserving a material population |

With a fixed delay time, first-order material and information delays can generate
the same output pattern. They are not interchangeable: their response diverges when
the delay time changes or conservation matters.

## Pipeline, First-Order, and Higher-Order Delays

### Pipeline delay

Items preserve entry order and spend a fixed duration in the process. The output is
the input shifted in time. Use for transportation or processing with little mixing
and tightly controlled lead time.

### First-order delay

The contents are treated as perfectly mixed. Every item has the same probability of
leaving, so a pulse produces its largest outflow immediately and then an exponential
tail. Use only when this mixing/residence-time assumption is plausible.

### Higher-order delay

Several first-order stages are cascaded. The response begins near zero, rises to a
peak, and declines. More stages reduce the variance around the mean and better
represent sequential work.

The continuous higher-order family corresponds to Erlang distributions; discrete
versions correspond to Pascal lags. The first-order discrete information lag is also
known as a Koyck or geometric lag.

## Little's Law Inside a Delay

For a stable material delay:

Amount in process = throughput x average delay

This is the operational check connecting lead time, flow, and work in process.
Changing throughput or delay without accounting for the amount accumulated in
transit creates an inconsistent model and often an impossible operating plan.

## Why Variable Delay Times Matter

Changing an average completion time can create nonlinear release or accumulation.
A faster process may flush work already in transit; a slower process can rapidly
increase WIP. Information delays instead change how fast beliefs catch up.

Adjustment times can also be asymmetric. Organizations may respond quickly to
bad news but slowly reverse the response, or rapidly raise a target while lowering
it reluctantly. These ratchet effects must be modeled explicitly rather than hidden
inside one constant lag.

## Estimating a Delay

When transaction-level data exist:

- reconstruct entry and exit times;
- inspect the full residence-time distribution, not only the average;
- estimate mean and variance and compare plausible delay orders;
- test for changing lead times, censoring, rework, losses, and multiple routes.

When numerical data are weak:

1. Decompose the process into observable stages.
2. Estimate each stage separately using several people and evidence sources.
3. Walk the line and observe where work actually waits.
4. Compare official procedure with actual routing, batching, rework, and prioritization.
5. Reconcile the sum of stage delays with end-to-end experience.

Judgment improves when the question changes from "How long does this take?" to
"Where is the work between entry and exit, and what controls each transition?"

## Semiconductor Forecasting Lesson

The source case forecasts semiconductor demand by tracking design wins through
design, prototyping, production, and revenue. The leading indicator is not merely a
smoothed sales history; it is the population of opportunities already moving through
a staged pipeline, with cancellation probabilities and anticipated volumes.

This is directly reusable for sales pipelines, hiring, projects, permits, claims, and
capital programs: forecast from the state and aging of work already committed, not
only from recent output.

## Audit Translation: Build a Delay Register

For each important lag, record:

| Field | Question |
|---|---|
| State | What accumulates while the output waits? |
| Type | Is it material, information, or a hybrid? |
| Mean and distribution | What are the full residence-time characteristics? |
| Order and route | Are items mixed, sequential, batched, prioritized, or reworked? |
| Evidence | Which timestamps, observations, and interviews support the estimate? |
| Variability | Does the delay change with load, staffing, age, priority, or policy? |
| Consequence | Does it create instability, stale decisions, hidden WIP, or poor forecasts? |

## Connects to

[[littles-law-and-best-case-performance]],
[[flow-variability-and-queueing-fundamentals]],
[[stock-flow-fundamentals-and-notation]],
[[forecasting-expectations-and-fudge-factors]],
[[coflows-aging-chains-and-attribute-dynamics]], and
[[model-validation-and-testing-practice]].

## Use / Retrieval Notes

**Use when**: A process has lead time, approvals, work in progress, stale
information, forecast lag, hiring/training time, or unexplained oscillation.

**Proof**: The delay is represented by an explicit state, its type and distribution
match the real process, and transaction data or firsthand observation supports the
chosen mean, stages, and variability.

