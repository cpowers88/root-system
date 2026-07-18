---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, alignment, interpretability, explainability, oversight, evaluation, audit]
---

# Interpretable Models and Human Oversight

**Summary**: Predictive accuracy is not sufficient evidence that a model is safe
to deploy. A model can learn a real correlation produced by the existing care or
decision process and then recommend removing the very intervention that caused
the good outcome. Prefer an intrinsically interpretable model when it can perform
the job; when complexity is unavoidable, use multiple diagnostic methods and test
the explanation with the people who must act on it.

**Source**: `raw/TheAlignmentProblem.pdf` (Brian Christian, *The Alignment
Problem*, 2020), Chapter 3, “Transparency” (physical PDF pp. 105-149), reviewed as
one complete chunk. Part II begins on physical p. 150; boundary visually verified.

**Last updated**: 2026-07-16

## Accuracy Can Encode a Dangerous Process

The chapter's pneumonia case is the central warning. Asthma appeared correlated
with lower mortality because clinicians treated asthmatic pneumonia patients as
high risk and gave them intensive care. A model could accurately learn that
correlation and then recommend outpatient treatment, removing the care that made
the group look safe.

This is intervention or treatment confounding: historical outcomes reflect both
the underlying condition and the decisions already made in response to it. Before
using a predictive relationship as a decision rule, ask whether an existing
intervention created the relationship.

## Prefer Interpretability When the Task Allows It

For consequential decisions using a manageable set of structured variables,
simple or constrained models can often match complex systems. The chapter's
research history supports several durable findings:

- consistent statistical rules frequently outperform unaided expert integration;
- human expertise is especially valuable in choosing what evidence matters;
- equal or simple weights can generalize better than weights overfit to one site;
- generalized additive models, rule lists, and sparse scorecards can remain
  inspectable while retaining strong predictive performance;
- computational power can search for the best simple model instead of being used
  only to increase complexity.

The practical division of labor is: experts define the decision, candidate
variables, constraints, and unacceptable behavior; a reproducible model combines
the evidence consistently; experts review exceptions and observed consequences.

## Explanation Is Not One Technique

When raw images, audio, or language require a complex model, use complementary
diagnostics:

| Method | What it can reveal | Typical failure it catches |
|---|---|---|
| Saliency or attention map | Where the model looked | Background or ruler used instead of the intended object or lesion |
| Feature visualization | What internal units respond to | Category learned with an unintended companion feature |
| Multitask outputs | Related predictions around the main outcome | A supposedly low-risk case with high treatment intensity or cost |
| Concept activation tests | Whether a human-defined concept influences output | Gender, ethnicity, color, or context driving an unexpected category |
| Intrinsically interpretable model | The decision rule itself | Hidden interactions and unreviewable rationale |

No diagnostic is a proof of correctness. A plausible heat map can create false
confidence; a transparent interface can make users less likely to notice an error.
Use explanations to generate and test hypotheses, not as decorative reassurance.

## The Explanation Must Fit the User

Interpretability exists for human use, so its quality is empirical. An engineer,
clinician, operator, auditor, affected person, and executive may need different
information. A valid review asks:

- What action must this person take?
- What evidence would let them challenge the recommendation?
- Can they identify when the model is outside its validated conditions?
- Does the explanation improve error detection, not merely reported trust?
- Is responsibility paired with enough information and authority to refuse?

If the analyst must sign their name to a recommendation but cannot understand its
rationale, the workflow has assigned accountability without control.

## Deployment Gate

Before a high-impact model moves into production:

1. Establish a simple, interpretable baseline.
2. Measure whether a complex model adds material decision value, not merely a small
   benchmark gain.
3. Inspect variables and training labels for treatment or policy confounding.
4. Use more than one explanation technique on critical cases.
5. Test explanations with actual decision-makers and affected workflows.
6. Define refusal, escalation, override, and incident-review paths.
7. Monitor whether the model changes care, behavior, or data collection in ways
   that invalidate its original evidence.

## Connects To

- [[training-data-representation-and-feedback-risk]] - interpretability checks
  whether the learned representation relies on intended evidence.
- [[algorithmic-fairness-metrics-ground-truth-and-intervention]] - an explanation
  must sit inside a defensible fairness and intervention policy.
- [[nist-ai-rmf]] - turns transparency and explainability into governed lifecycle
  practices rather than a one-time visualization.
- [[agentic-automation-architecture-reliability-and-economic-evidence]] - supports
  bounded, observable automation with explicit contracts and human oversight.
- [[root-maturity-self-assessment]] - `.ROOT`'s verification capacity is the same
  constraint: responsibility must be matched with inspectable evidence.

## Limits and Recency

The chapter describes interpretability research through roughly 2020. Specific
methods and legal examples are historical. The durable lesson is the evaluation
architecture: test why a model works, whether the explanation helps the real user,
and whether a simpler model can safely do the job.
