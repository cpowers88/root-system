---
domain: systems
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, system-dynamics, bounded-rationality, decision-making, policy-resistance]
---

# Bounded Rationality, Intended Rationality, and Local Policy

**Summary**: People use routines, goals, heuristics, and organizational decomposition
because attention and cognition are limited. Their decisions can be sensible within
their local mental models and incentives while interacting to create price wars,
capacity crises, policy resistance, and poor system-wide performance.

**Source**: BusinessDynamics.pdf (Sterman, Business Dynamics, 2000), Chapter 15,
"Modeling Human Behavior: Bounded Rationality or Rational Expectations?"
(printed pp. 597-629; physical PDF pp. 622-654), reviewed as one complete
chapter chunk.

**Last updated**: 2026-07-15

## Chapter Coverage

| Source section | Disposition |
|---|---|
| 15.1-15.2 Bounded versus rational expectations | Empirical framing, selective attention, cognitive limits, and heuristics captured |
| 15.3 Responses to bounded rationality | Routines, attention management, satisficing, goal adaptation, decomposition, and decentralization captured |
| 15.4 Intended rationality | Local mental-model test and partial-model-testing method captured |
| 15.5 High-tech growth firm | Sales, order fulfillment, capacity acquisition, and interaction-driven growth failure captured |
| 15.6 Summary | Descriptive-model and policy-design implications incorporated |

## Descriptive Models Must Represent Actual Practice

A simulation of organizational behavior should describe how people decide, not how
an optimizer says they should decide. The modeler can then test structural changes
that improve performance.

Perfect rationality assumes information, foresight, computation, and consistency
that real decision makers do not possess. At the other extreme, portraying people as
unresponsive automata ignores learning and purpose. The useful middle is bounded
rationality: purposeful actors adapting with limited information, limited time, and
simplified mental models.

## Cognitive and Attention Limits

People perceive only a small fraction of available information and use few cues in
each decision. Attention shifts with salience, perceived importance, interruption,
stress, and mental models. Under overload, critical information may not be noticed
at all.

Common consequences:

- concrete, recent, and certain cues dominate remote or uncertain evidence;
- people underweight feedback delays and side effects;
- mental models direct attention toward familiar measures and away from diagnostic
  but unexpected information;
- training reduces some errors but does not remove structural cognitive limits.

## How People and Organizations Cope

### Habits, routines, and rules of thumb

Routines reduce deliberation and let repeated work proceed quickly. They can be
informal or codified, rigid or adaptable. Rules of thumb aim for a good-enough
decision using readily available information.

### Managing attention

Reporting structures, dashboards, agendas, physical layout, accounting systems,
and informal networks decide which signals reach whom. Information architecture
is therefore part of the decision policy and a source of organizational power.

### Goals and satisficing

People set targets and act on the gap between target and performance. Search often
stops once the result is satisfactory so scarce attention can move elsewhere.
Goals themselves adapt to experience, peers, realized performance, and pressure.

### Decomposition and decentralization

Organizations split a complex objective into subgoals assigned to departments,
teams, and individuals. This makes decisions manageable but assumes that achieving
local subgoals will produce the system-wide goal. That assumption often fails.

Examples include sales maximizing volume without considering fulfillment capacity,
production meeting quota by deferring maintenance, or a developer building from
current rents while ignoring the industry construction pipeline.

## Intended Rationality

A rule is intendedly or locally rational when it would be sensible if the environment
were as simple as the actor believes.

An apparently irrational action may therefore reveal:

- a boundary that excludes competitor response;
- a delayed or distorted perception;
- a local incentive;
- an assumed constant that is actually endogenous;
- a missing side effect or supply line.

The audit task is to reconstruct the premises that make the action sensible, then
show where the real feedback structure violates those premises.

## Partial Model Tests

To test intended rationality:

1. Isolate one decision rule or organizational function.
2. Make its environment behave as the actor believes it does.
3. Challenge it with steps, shocks, trends, and extreme inputs.
4. Confirm the rule performs sensibly within that local mental model.
5. Restore the omitted feedbacks and interactions.
6. Observe whether several locally sensible rules create dysfunction together.

This separates a badly formulated rule from an interaction failure. It also avoids
blaming people for system behavior produced by boundaries and incentives.

## Price-War Example

A firm with low utilization may cut price to fill capacity. The rule is locally
rational if competitor prices remain fixed. If competitors use the same rule, each
price cut reduces rivals' utilization and triggers another cut. The interacting local
balancing loops create an industry-wide reinforcing price war.

The remedy is not simply teaching one manager to optimize better. It requires
changing the information, incentives, coordination, capacity structure, or rules that
couple the firms.

## High-Tech Growth-Firm Case

The source model divides a growing firm into sales, order fulfillment, and capacity
acquisition. Each function uses different information and pursues a sensible local
goal. Delays in capacity, service, and market response allow the policies to interact
in ways that can create:

- order backlogs and worsening delivery performance;
- sales-force responses to perceived opportunity;
- late capacity expansion;
- overexpansion after growth slows;
- stagnation or repeated management crises despite a viable product and market.

Growth failure can therefore originate in decision-policy interaction rather than
product quality or individual incompetence.

## Audit Translation

For each recurring operational failure:

| Question | Evidence |
|---|---|
| What local goal is each actor pursuing? | Targets, incentives, queue rules, escalation criteria |
| What cues receive attention? | Dashboards, reports, meetings, alerts, informal channels |
| What is treated as exogenous? | Competitor, supplier, customer, or upstream/downstream response |
| What delay or side effect is omitted? | Lead time, rework, maintenance, hiring, churn, trust |
| Is the rule locally sensible? | Partial model test |
| What happens when all actors use it? | Integrated feedback test |

## Connects to

[[barriers-to-learning-and-virtual-worlds]],
[[modeling-decision-rules-and-rate-formulations]],
[[forecasting-expectations-and-fudge-factors]],
[[policy-resistance-and-feedback-thinking]],
[[designing-for-human-error-and-recovery]], and
[[human-centered-design-conceptual-models-and-action-cycle]].

## Use / Retrieval Notes

**Use when**: An incident is blamed on irrational people, departments meet their
targets while the whole system fails, or a policy works in isolation but fails after
others respond.

**Proof**: The analysis identifies each actor's information, goal, heuristic, local
rationale, omitted feedbacks, and the integrated mechanism that converts reasonable
local action into poor system behavior.

