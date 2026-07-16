---
domain: systems
type: method
timeline: reference
status: active
reference_priority: core
tags: [systems, system-dynamics, decision-rules, model-formulation, audit]
---

# Modeling Decision Rules and Rate Formulations

**Summary**: Dynamic models require explicit rules that convert available
information into decisions and actions. Those rules must match actual practice,
separate desired from realized outcomes, remain physically possible under extreme
conditions, and allow equilibrium or instability to emerge rather than assuming it.

**Source**: BusinessDynamics.pdf (Sterman, Business Dynamics, 2000), Chapter 13,
"Modeling Decision Making" (printed pp. 513-550; physical PDF pp. 538-575),
reviewed as one complete chapter chunk.

**Last updated**: 2026-07-15

## Chapter Coverage

| Source section | Disposition |
|---|---|
| 13.1 Principles | Decisions/rules distinction and all five formulation fundamentals captured |
| 13.2 Rate equations | Fractional rates, goal adjustment, stock management, resource-productivity, effects, fuzzy limits, floating goals, weighted averages, search, and allocation captured |
| 13.3 Pitfalls | Outflow control, IF/THEN/ELSE avoidance, and net-flow disaggregation captured |
| 13.4 Summary | Robustness, dimensional consistency, available-information, and template guidance incorporated |

## Decisions and Decision Rules

A decision is an event or action; a decision rule is the policy that generates it
from information. A useful model does not simply replay historical decisions. It
represents how actors would decide under conditions they have not yet experienced.

The rule must be appropriate for the model's purpose and grounded in fieldwork,
records, experiments, or other evidence about actual behavior.

## Five Formulation Fundamentals

| Principle | Operational meaning |
|---|---|
| 1. Baker Criterion | A decision rule may use only information actually available to the real decision maker when the decision is made |
| 2. Conform to managerial practice | Variables and relationships need real-world counterparts; do not force behavior to match a preferred theory |
| 3. Separate desired and actual conditions | Goals and authorizations are not realized outcomes; physical constraints and delays determine what actually happens |
| 4. Remain robust under extreme conditions | Inputs outside historical experience must not generate negative stocks, impossible flows, or meaningless actions |
| 5. Do not assume equilibrium | Stability, instability, and equilibrium must emerge from interacting rules and structure |

### Corollaries of the Baker Criterion

- The future is unknown; forecasts and beliefs are formed from history and can be wrong.
- Perceived conditions differ from actual conditions because information is delayed,
  sampled, averaged, biased, noisy, or incomplete.
- Outcomes of untried contingencies are conjectures, not information the actor
  already possesses.

Model the process that creates the report, perception, or expectation used in the
decision. Do not give the simulated actor access to the modeler's omniscient state.

## Reusable Rate-Equation Patterns

### Fractional increase and decrease

A flow often scales with the stock or resource exposed to the process:

- increase flow = stock x fractional increase rate;
- decrease flow = stock x fractional decrease rate;
- average residence time is the inverse of a constant fractional outflow rate.

### Adjustment to a goal

Indicated adjustment = (desired state - perceived state) / adjustment time

This represents goal-seeking behavior, but the actual flow may be constrained and
must not become physically impossible.

### Stock management

Required inflow = normal outflow or replacement rate + correction for the stock gap

Replacing only the discrepancy creates steady-state error when a continuing outflow
exists. The normal replacement rate and the adjustment must both be represented.

### Resource times productivity

Flow = available resource x productivity of that resource

This separates capacity from its utilization or effectiveness and supports explicit
effects of skill, quality, fatigue, equipment state, or process design.

### Multiple effects

Use multiplicative effects when each factor proportionally modifies a reference
rate. Use additive effects when each factor contributes an independent increment.
Normalize when helpful so the reference condition has an effect of one.

### Fuzzy minimum and maximum

Hard MIN and MAX functions capture real constraints but create abrupt corners.
Fuzzy versions represent gradual approach to capacity, resource scarcity, or a
nonnegative bound when the real response is smooth.

### Floating goals and nonlinear weighted averages

Goals adapt to experience, peers, benchmarks, or external expectations. A floating
goal is a stock or weighted perception, not an unexplained moving target. Nonlinear
weights allow actors to shift attention among signals as conditions change.

### Search and hill climbing

Decision makers often do not know the global optimum. They vary price, capacity,
labor mix, or another control in the direction that recently improved performance.
This local search can be intendedly rational yet overshoot, stall, or interact badly
with delay and noise.

### Resource allocation

When total demand exceeds a limited resource, allocate explicitly among uses.
Priority rules, minimum commitments, and changing attractiveness should be visible
rather than hidden in unconstrained parallel flows.

## Common Pitfalls

### Uncontrolled outflows

Every outflow needs first-order control so the stock cannot become negative.
Shipments must fall when inventory is exhausted; layoffs cannot exceed the
available workforce.

### Nested IF/THEN/ELSE logic

Nested logical statements combine several ideas, obscure units, create
discontinuities, and are difficult for clients to inspect. Prefer separate equations
for distinct concepts, then constrain them with transparent MIN, MAX, or smooth
functions.

### Net flows

Model hiring, quits, layoffs, and promotions separately rather than one net workforce
change. Separate flows can use different information, constraints, delays, and
evidence. A net rate destroys that causal detail.

## Decision-Rule Interview

For each operational decision, ask:

1. Who makes or authorizes it?
2. What information do they actually see, in what form, and with what delay?
3. What target, threshold, comparison, or rule triggers action?
4. What do they want to happen, and what constrains what actually happens?
5. How do they respond when several constraints bind at once?
6. What happens at zero, maximum load, severe shortage, or unprecedented growth?
7. How do goals and beliefs change after success, failure, or new information?
8. Which inflows and outflows have been improperly collapsed into a net number?

## Connects to

[[operations-research-study-lifecycle]],
[[modeling-process-and-client-ethics]],
[[stock-management-structure-and-amplification]],
[[nonlinear-relationships-and-table-functions]],
[[bounded-rationality-intended-rationality-and-local-policy]],
[[forecasting-expectations-and-fudge-factors]], and
[[model-validation-and-testing-practice]].

## Use / Retrieval Notes

**Use when**: Translating interviews, SOPs, heuristics, forecasts, approvals, or
management policies into a simulation or an auditable operating rule.

**Proof**: A real decision owner recognizes the information and rule, units balance,
desired and actual outcomes are distinct, flows remain possible at extremes, and
system behavior emerges without hidden foresight or assumed equilibrium.

