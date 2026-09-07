---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, alignment, fairness, evaluation, ground-truth, feedback, governance, audit]
---

# Algorithmic Fairness: Metrics, Ground Truth, and Intervention

**Summary**: Fairness cannot be guaranteed by deleting protected attributes or
choosing a single universal metric. Proxy variables reconstruct group membership,
common fairness criteria can be mathematically incompatible, observed labels may
measure institutional activity rather than the claimed outcome, and even an
accurate prediction may support the wrong intervention. A defensible system makes
those choices explicit and tests the full decision loop.

**Source**: `raw/TheAlignmentProblem.pdf` (Brian Christian, *The Alignment
Problem*, 2020), Chapter 2, “Fairness” (physical PDF pp. 67-104), reviewed as one
complete chunk. Chapter 3 begins on physical p. 105; boundary visually verified.

**Last updated**: 2026-07-16

## Fairness Through Blindness Fails

Removing race, gender, disability status, or another sensitive field does not make
a model neutral. Location, employment history, language, arrest history, school,
and many other variables can redundantly encode the same information. A model
designed to infer hidden correlations will hear the equivalent of the orchestra
auditioner's shoes even after the visible identifier is removed.

Blindness can also prevent measurement and mitigation. If reviewers cannot access
the sensitive attribute under controlled conditions, they cannot calculate group
performance or determine whether a supposedly neutral variable functions as a
proxy. Operationally, protected attributes may need stricter access and purpose
limits—not automatic deletion from every evaluation dataset.

## Fairness Metrics Can Conflict

The COMPAS controversy illustrates three different questions:

- **calibration**: does a risk score mean the same observed probability for each
  group?
- **false-positive parity**: are people who do not produce the outcome equally
  likely to be incorrectly classified as high risk?
- **false-negative parity**: are people who do produce the outcome equally likely
  to be incorrectly classified as low risk?

When outcome base rates differ between groups, calibration and equal error rates
generally cannot all hold simultaneously. This is not a defect unique to a given
algorithm; it is a constraint on any scoring system, including human judgment.

Therefore a fairness audit cannot end with “the model is biased” or “the model is
calibrated.” It must state:

1. which fairness property is being prioritized;
2. which incompatible property is being relaxed;
3. who bears each kind of error;
4. why that tradeoff fits the decision domain;
5. who had authority to make the policy choice.

The mathematics clarifies the choice; it does not make the moral or legal choice.

## The Label May Not Be Ground Truth

A model can accurately predict its recorded label and still miss the intended
phenomenon. Arrest data reflects crime plus police attention, reporting, charging,
and record quality. A model trained on arrests may predict future policing more
directly than future crime. Similarly, an image dataset labeled by crowd workers
contains worker judgments, not unmediated truth.

Use a label-lineage check:

| Question | Audit purpose |
|---|---|
| What outcome do stakeholders believe is predicted? | Names the intended construct. |
| What event actually created the label? | Exposes institutional and measurement processes. |
| Which outcomes remain unobserved? | Identifies selective labels and missing negatives/positives. |
| Does the decision influence later observation? | Detects self-confirming feedback. |
| Is a more reliable outcome available? | Supports redesign or narrower use. |

## Prediction Is Not Intervention

Even a well-calibrated prediction does not determine what to do. A forecast that
someone may miss court could lead to detention, or it could lead to a reminder,
transportation, or child-care assistance. Those actions have radically different
costs and effects. A risk score developed for treatment or release planning may be
misused if it is imported into sentencing or punishment.

The decision gate is:

```text
prediction
  -> available interventions
  -> expected benefit and harm of each
  -> resource and service availability
  -> monitored outcome
  -> feedback into policy and model review
```

If there is no safe or effective action attached to a prediction, improving its
accuracy may add surveillance without improving the underlying outcome.

## Applied Review Sequence

1. Define the decision, affected people, and actual harm being reduced.
2. Trace the label back to the process that generated it.
3. Measure calibration and error types by relevant groups and intersections.
4. Identify proxies and redundant encodings.
5. Document incompatible fairness goals and the chosen tradeoff.
6. Verify the model is used only for its validated purpose.
7. Compare the proposed intervention with less harmful alternatives.
8. Monitor whether deployment changes the observed data or underlying behavior.

## Connects To

- [[training-data-representation-and-feedback-risk]] - dataset composition and
  representation precede the fairness analysis.
- [[interpretable-models-and-human-oversight]] - reviewers need evidence about
  what the model uses and why.
- [[nist-ai-rmf]] - fairness is a governed tradeoff requiring context, measurement,
  and continuing management.
- [[oecd-ai-incidents-monitor]] - incident evidence can reveal which error costs
  matter in a specific domain.

## Limits and Recency

The chapter is a historical and conceptual source published in 2020. Its cases and
legal references are not current legal advice. Verify live law, current system
versions, and present population data before applying any specific threshold or
policy.
