---
domain: systems
type: method
timeline: reference
status: active
reference_priority: core
tags: [systems, system-dynamics, nonlinear-modeling, table-functions, elicitation, testing]
---

# Nonlinear Relationships and Table Functions

**Summary**: Real operations contain thresholds, saturation, capacity limits,
diminishing returns, and asymmetric responses. Table functions provide a transparent
way to represent these nonlinear relationships using physical laws, reference
policies, extreme conditions, numerical data, and expert knowledge.

**Source**: BusinessDynamics.pdf (Sterman, Business Dynamics, 2000), Chapter 14,
"Formulating Nonlinear Relationships" (printed pp. 551-595; physical PDF
pp. 576-620), reviewed as one complete chapter chunk.

**Last updated**: 2026-07-15

## Chapter Coverage

| Source section | Disposition |
|---|---|
| 14.1 Table functions | Full nine-step specification method and capacitated-delay example captured |
| 14.2 Overtime/corner cutting | Schedule-pressure effects, interacting loops, and feasible bounds captured |
| 14.3 Qualitative and numerical evidence | Triangulation and uncertainty refinement captured |
| 14.4 Pitfalls | Wrong input, improper normalization, and hump-shaped-function warning captured |
| 14.5 Interactive elicitation | Individual elicitation, anchors, group reconciliation, and implementation value captured |
| 14.6 Summary | Sensitivity-driven evidence allocation incorporated |

## Why Nonlinearity Matters

Linear approximations fail when:

- output cannot exceed capacity;
- a flow must fall to zero when a stock is empty;
- additional pressure initially helps but later creates fatigue, errors, or rework;
- quality, demand, or productivity approaches a ceiling;
- several constraints bind simultaneously;
- response near normal conditions differs from response near extremes.

A table or lookup function makes the assumed shape visible and editable instead of
hiding it inside a complicated analytic expression.

## Nine-Step Table-Function Method

1. **Normalize when appropriate.** Express the input relative to a reference input
   and the output as a dimensionless effect on a reference output.
2. **Identify reference points.** Include values fixed by definition, such as an
   effect of one at the normal operating point.
3. **Identify reference policies.** Plot no-effect, proportional-response, capacity,
   or other bounding policies that rule out infeasible regions.
4. **Test extreme conditions.** Determine required values and slopes at zero,
   very large, very small, or joint extreme inputs.
5. **Specify the complete domain.** Cover the full plausible range, not only the
   historical operating neighborhood.
6. **Identify plausible shapes.** Use physical constraints, actor policies,
   qualitative evidence, and justified inflection points.
7. **Enter the best estimate.** Use enough points for needed smoothness and inspect
   unexplained kinks; judgmental estimates are acceptable when uncertainty is explicit.
8. **Run and test the model.** Confirm the function is actually exercised across
   its intended range and does not operate continually off an endpoint.
9. **Run sensitivity analysis.** Gather better data only if plausible variation
   changes behavior or policy conclusions.

## Capacitated Delay

A common nonlinear structure is a backlog whose desired completion rate rises with
the backlog but whose actual completion rate saturates at capacity.

Desired completion = backlog / target delivery delay

Actual completion = capacity x utilization effect(schedule pressure)

The utilization effect must:

- go to zero when there is no work;
- pass through a defined normal point;
- approach, but not exceed, physical capacity;
- cover extreme backlogs and schedule pressure;
- remain consistent with the target-delivery policy.

This structure appears in production, service queues, paperwork, project tasks,
claims, and any process where work waits and throughput is capacity constrained.

## Schedule Pressure, Overtime, and Cutting Corners

Schedule pressure can increase throughput through two different channels:

- people work longer hours;
- people spend less time per task.

Both are bounded. Workweek cannot increase without limit, and reducing time per
task eventually increases errors, fatigue, rework, or failure. These effects interact:
an individual relationship that looks plausible can create impossible behavior when
combined with the others.

Estimate each relationship, then test the total response at the normal point and all
joint extremes. The overall model must respect physical capacity and the feedback
from quality loss or rework.

## Evidence Hierarchy for Shape

Use all available evidence:

- physical conservation laws and hard constraints;
- definitions and known anchor points;
- official or observed reference policies;
- transaction and experimental data;
- direct observation;
- interviews and written process descriptions;
- comparison across analogous situations;
- extreme-condition reasoning.

Numerical data often cover only the normal operating range. Qualitative evidence and
extreme conditions can rule out large portions of the possible function even when
the exact values remain uncertain.

## Common Pitfalls

### Wrong input

Choose the signal the real actor or physical process responds to. A decision may
depend on perceived schedule pressure, not actual backlog; a physical constraint may
depend on inventory, not an accounting proxy.

### Improper normalization

Normalized inputs and effects need meaningful reference values and balanced units.
Changing the reference value should not accidentally change the underlying physical
relationship.

### Hump-shaped functions

A causal link should have unambiguous polarity. If a relationship rises and then
falls, it usually contains two distinct causal effects. Split them into separately
named monotonic functions so each mechanism, evidence source, and loop polarity
can be inspected.

## Interactive Expert Elicitation

Elicit tacit knowledge before forcing group consensus:

1. Ask experts individually to visualize and describe the process.
2. Record written walkthroughs.
3. Identify high-confidence anchor points and physical constraints.
4. Sketch the relationship and explain its causal meaning.
5. Compare individual curves and surface disagreements.
6. Use the group discussion to reconcile definitions, evidence, and boundary
   assumptions rather than averaging incompatible views.

The process creates model evidence and organizational learning. Participation also
builds credibility and improves transfer of the resulting policy.

## Audit Translation

Use a table-function worksheet for any threshold or saturation claim:

| Field | Required evidence |
|---|---|
| Input and output | Clear real-world meaning and units |
| Reference point | Normal condition fixed by definition or observation |
| Bounds | Physical, policy, or contractual limits |
| Extreme behavior | Values and slopes at zero and plausible maxima |
| Shape | Causal explanation for curvature and inflection |
| Uncertainty | Alternative plausible curves |
| Sensitivity | Whether uncertainty changes the recommendation |

## Connects to

[[modeling-decision-rules-and-rate-formulations]],
[[material-information-and-pipeline-delays]],
[[causes-of-variability-breakdowns-setups-rework]],
[[model-validation-and-testing-practice]],
[[sensitivity-analysis-and-postoptimality]], and
[[designing-for-human-error-and-recovery]].

## Use / Retrieval Notes

**Use when**: Modeling capacity saturation, workload pressure, quality loss,
thresholds, diminishing returns, or a relationship known mainly through expert
judgment.

**Proof**: The function has traceable anchors, bounds, domain, causal shape,
extreme-condition behavior, alternative plausible forms, and a sensitivity result
showing whether better measurement would change the decision.

