---
domain: systems
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, model-validation, system-dynamics, audit, testing]
---

# Model Validation and Testing Practice

**Summary**: A model cannot be proven true. It earns confidence by being fit for
a stated purpose, open to challenge, reproducible from its documentation, and
tested across structure, behavior, uncertainty, and implementation effects.

**Source**: BusinessDynamics.pdf (Sterman, Business Dynamics, 2000), Chapter 21,
"Truth and Beauty: Validation and Model Testing" (printed pp. 845-891; physical
PDF pp. 870-916), reviewed as one complete chapter chunk.

**Last updated**: 2026-07-15

## Replace "Is It Valid?" with "Is It Fit for This Decision?"

Every model is a selective and simplified representation. It omits variables,
aggregates detail, uses imperfect data, and embeds judgments about boundaries,
causality, and behavior. Validation in the sense of establishing truth is therefore
impossible.

That does not make testing optional. It changes the purpose of testing:

- Name the decision, users, stakes, time horizon, and required accuracy.
- Try to uncover errors and limitations instead of accumulating confirming evidence.
- Compare the proposed model with the available alternatives, including the current
  mental model or status quo.
- State what the model is safe to support and what it cannot support.
- Reassess fitness when the purpose, operating conditions, or evidence changes.

Historical fit is only one signal. A model can reproduce the past for the wrong
reasons, hide implausible assumptions behind adjusted outputs, and fail when used
for a different policy or boundary.

## Evidence, Documentation, and Replication

Use numerical records, written records, direct observation, interviews, and the
experience held in people's mental models. None is automatically authoritative.
Triangulate across independent sources and document conflicts rather than selecting
only evidence that supports the favored story.

A reviewable model package should let an informed third party:

1. Identify the model's purpose, boundary, assumptions, and intended audience.
2. Trace parameter values and structural claims to their sources.
3. Check units and reproduce equations, calculations, runs, and reported outputs.
4. See the tests performed, failures found, changes made, and limitations retained.
5. Run, maintain, and modify the model without depending on its original author.

Documentation is part of the evidence, not an appendix produced after the answer.
If the result cannot be independently reproduced from the written record, it has
not passed the proof gate.

## Reflective Modeling, Not Protective Modeling

Protective modeling defends a preferred conclusion: critics are excluded, contrary
data are discounted, assumptions stay hidden, and unexplained adjustments are used
to force a plausible output. Reflective modeling treats criticism and surprise as
information. It invites affected people, domain experts, users, and skeptics to
challenge the boundary, causal structure, decision rules, and interpretation.

The practical test is simple: before analysis begins, name the evidence or model
behavior that would cause the team to revise its recommendation.

## The Complete Test Battery

No single test is adequate. Tests overlap and should run throughout development.

| Test | Question it is meant to expose |
|---|---|
| Boundary adequacy | Are important feedbacks, actors, constraints, or time horizons outside the model? |
| Structure assessment | Do the causal relationships and decision rules match how the real system works? |
| Dimensional consistency | Do units balance, and do equations preserve physical meaning? |
| Parameter assessment | Are values estimated from appropriate evidence and plausible over the intended range? |
| Extreme conditions | Does the model remain physically and behaviorally sensible at zero, very large, or limiting values? |
| Integration error | Do results change materially when the simulation time step or numerical method changes? |
| Behavior reproduction | Can the model reproduce relevant patterns, modes, and symptoms—not merely isolated points? |
| Behavior anomaly | Which assumptions or structures create a known implausible behavior? |
| Family-member | Does the structure explain related cases without case-specific patching? |
| Surprise behavior | What unexpected behavior appears, and what does it reveal about the model or system? |
| Sensitivity analysis | Do conclusions survive plausible changes in parameters, boundary, structure, and decision rules? |
| System improvement | Does using the model improve understanding, policy design, decisions, or measured outcomes? |

Parameter sensitivity alone is too narrow. Conclusions are often more sensitive to
the chosen boundary, aggregation, feedback structure, and representation of human
decision making than to small changes in individual parameter values.

## A BUILD / PROVE / DEPLOY Gate

### BUILD

- Define the purpose and success measures before selecting the technique.
- Record source lineage, assumptions, exclusions, units, and ownership.
- Involve the people who understand the work and the people who must use the result.
- Test components as they are built so errors do not compound.

### PROVE

- Require an independent reviewer to reproduce the result.
- Run the structural, dimensional, extreme-condition, behavioral, and sensitivity
  tests that match the model's purpose.
- Record failed tests and unresolved limitations, not only passed tests.
- Compare recommendations against the status quo and plausible alternative models.
- Distinguish a robust direction from a falsely precise forecast.

### DEPLOY

- Translate the model into an operating decision, owner, trigger, and review cadence.
- Preserve the documentation, executable artifact, input snapshot, and test record.
- Design outcome assessment prospectively; do not wait until after implementation
  to ask what data would have shown whether the intervention worked.
- Track changes in beliefs, behavior, policy, and system performance, while accounting
  for rival explanations and confounding changes.
- Reopen the model when assumptions or operating conditions leave the tested range.

## Audit Questions

1. What exact decision is this model meant to support, and for whom?
2. Which important variables, feedbacks, stakeholders, or time horizons were excluded?
3. Can another person reproduce the result without help from the author?
4. Which test was most capable of disproving the favored recommendation?
5. Does the result survive alternative boundaries, structures, and decision rules?
6. Are historical fit and expert agreement being mistaken for proof?
7. What evidence will be collected after deployment, and what result would trigger
   revision or withdrawal?

## Connects to

[[modeling-process-and-client-ethics]],
[[descriptive-vs-prescriptive-models-and-conjecture-refutation]],
[[operations-research-study-lifecycle]],
[[sensitivity-analysis-and-postoptimality]],
[[discrete-event-simulation-and-random-variate-generation]],
[[the-art-of-spreadsheet-modeling]], and
[[designing-for-human-error-and-recovery]].

## Use / Retrieval Notes

**Use when**: Reviewing a forecast, simulation, optimization model, spreadsheet,
AI recommendation, or analytical claim before it becomes a client decision.

**Proof**: A reviewer can reproduce the result, identify the tested purpose and
limits, inspect failed as well as passed tests, and state the evidence that would
change the recommendation.

