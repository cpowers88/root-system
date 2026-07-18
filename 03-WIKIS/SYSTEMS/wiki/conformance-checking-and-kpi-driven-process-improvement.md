---
domain: systems
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, process-mining, conformance, process-improvement, audit, model-validation]
---

# Conformance Checking and KPI-Driven Process Improvement

**Summary**: Conformance checking relates observed behavior to modeled behavior,
but a deviation does not identify which representation is wrong or whether the
deviation is harmful. Use rules, replay, or alignments to produce evidence; assign
trust to both log and model; interpret deviations with domain owners; then repair or
extend only the behavior that is valid and improves a named KPI.

**Source**: `Process Mining Handbook.pdf`, Chapter 5, "Conformance Checking:
Foundations, Milestones and Challenges" (printed pp. 155-190; physical
pp. 162-197), and Chapter 8, "Foundations of Process Enhancement" (printed
pp. 243-273; physical pp. 248-278), both read in full.

**Last updated**: 2026-07-18

## What Conformance Evidence Actually Says

The two inputs are representations, not reality itself:

- the event log records selected observable events through an extraction and
  transformation process;
- the process model expresses intended, remembered, discovered, or documented
  behavior at a chosen level of abstraction.

A mismatch may mean the process deviated, the model is stale or intentionally coarse,
the log is incomplete or mislabeled, or the two artifacts use different boundaries.
Conformance creates a diagnostic artifact; it does not automatically assign blame.

## Three Conformance Artifacts

| Method | Evidence produced | Strength | Main limit |
|---|---|---|---|
| Rule checking | Violated cardinality, precedence, ordering, or exclusivity rules | Direct and explainable for named controls | Depends on the chosen rule set; weak for model precision |
| Token replay | Missing and remaining tokens while traces replay through a model | Fast, operational fitness signal | Heuristic handling can obscure the best explanation |
| Alignments | Synchronous moves, log-only moves, and model-only moves along the closest valid model path | Detailed trace-level diagnosis and a basis for fitness/precision | Computationally expensive; multiple optimal explanations may exist |

Fitness asks how much observed behavior the model can explain. Precision asks how
much behavior allowed by the model is supported by the log. Generalization and
simplicity remain separate tradeoffs. No single score is the audit finding; the useful
output is the trace, rule, object, cost, control, or delay that a person can investigate.

## Trust-Aware Interpretation

Make trust in each artifact explicit:

| Log trust | Model trust | Appropriate question |
|---|---|---|
| High | High | Where did execution depart from a reliable rule/model? |
| High | Partial | What should be repaired in the model to reflect reliable evidence? |
| Partial | High | What logging, correlation, or extraction defect should be repaired? |
| Partial | Partial | Which smallest changes to both artifacts produce a credible explanation? |
| Low | Low | Stop; a polished comparison between two untrusted artifacts is not evidence. |

This prevents the common failure of treating the documented process as unquestionable
or treating the system log as ground truth merely because it is digital.

## From Conformance to Enhancement

Process enhancement has two jobs.

### Process extension

Add perspectives that make the model useful for the decision:

- **data/decision**: discover which case and event attributes explain branch choices;
- **organization/resource**: identify roles, handoffs, collaboration structure, and
  dependency on hard-to-replace resources;
- **time**: separate service time from waiting time, identify bottlenecks, and test
  deadline/service-level constraints.

Control-flow alone cannot explain why a branch was chosen, who was overloaded, or
where time accumulated. Missing timestamps and missing values must remain visible as
uncertainty; silently imputing them can turn an assumption into an apparent fact.

### Process improvement

Do not make every observed path legitimate. Model repair that maximizes fitness may
encode errors, outliers, workarounds, fraud, unsafe behavior, or still-running cases.
Filter and classify those conditions before changing the normative model.

The KPI-driven improvement loop is:

1. Compute conformance artifacts for the trusted scope.
2. Correlate specific log/model moves with a named KPI or control outcome.
3. Separate satisfactory, unsatisfactory, prohibited, mandatory, and unexplained
   behavior.
4. Repair the log where evidence collection is faulty.
5. Repair the model only to include valid behavior associated with satisfactory
   outcomes, or to exclude behavior associated with harm/noncompliance.
6. Recheck fitness, precision, simplicity, and unintended behavior after repair.
7. Validate the recommended process change in operation; correlation alone does not
   prove the deviation caused the outcome.

## Deviation Triage

For each important deviation, record:

| Field | Question |
|---|---|
| Evidence | Which cases, events, rule, and alignment moves demonstrate it? |
| Artifact trust | How reliable are the log, model, timestamps, labels, and case mapping? |
| Classification | Error, legitimate exception, harmful anomaly, beneficial workaround, or unresolved? |
| Materiality | Frequency, delay, cost, quality, control, customer, or safety consequence? |
| Explanation | Which system condition, policy, resource, or upstream event plausibly caused it? |
| Action | Repair data, repair model, redesign process, add/remove control, automate, or monitor? |
| Proof | What post-change measure would confirm improvement or expose regression? |

Rank deviations by business consequence, not only frequency. A rare safety or control
failure may outrank a common harmless variant. Conversely, thousands of deviations
can reflect one stale model rule rather than thousands of operational failures.

## Limits

- Alignment results may be computationally expensive and non-deterministic when
  several equally low-cost explanations exist.
- Coverage error and biased sampling can make conformance estimates look precise
  while missing important behavior.
- Online conformance reduces detection latency but cannot retain or revisit an
  unbounded event stream without explicit aggregation choices.
- KPI correlation is hypothesis evidence, not causal proof. Domain validation and a
  measured intervention remain required.

## Connects to

[[pm4py-process-mining-in-python]],
[[bpmn-2-0-specification]],
[[model-validation-and-testing-practice]],
[[process-mining-audit-and-automation-opportunity]],
[[factory-physics-four-step-improvement-methodology]], and
[[responsible-process-mining-fact-gate]].

## Use / Retrieval Notes

**Use when**: Comparing a logged process with BPMN, policy, control, SLA, or a
previously discovered model; triaging variants; or deciding whether a model should be
repaired after observing real execution.

**Proof**: A domain owner can trace the finding to cases and system evidence, explain
the deviation classification, and show a post-change outcome without hiding data/model
uncertainty.
