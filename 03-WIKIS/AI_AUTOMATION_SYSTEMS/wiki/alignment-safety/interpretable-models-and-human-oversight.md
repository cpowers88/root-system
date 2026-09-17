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

**Last updated**: 2026-07-27

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

## Keep Explanation Evidence Separate from Verbalization

An LLM can make a technical explanation easier to read, but fluency is not
fidelity. Preserve a layered evidence chain:

```text
source cases/events
  -> analytical model or cluster
  -> machine-checkable explanation
  -> bounded natural-language rendering
  -> human review and challenge
```

For each layer, retain:

| Layer | Evidence needed |
|---|---|
| Source | case/event identifiers, fields, timestamps, extraction limits |
| Model | version, inputs, output/cluster, uncertainty, validated scope |
| Explanation | rule, differentiating features, accuracy/fidelity, coverage |
| Verbalization | model/prompt version, supplied facts, task boundary, output |
| Review | reviewer, comparison result, correction/override, downstream action |

The verbal explanation must never become the only retained rationale. A reviewer
needs access to the underlying rule and source cases because a natural-language
summary can omit a condition, invent a relationship, or describe the wrong
entity while remaining persuasive.

### Bound the explanation interface by task

Define a small explanation contract rather than allowing open-ended analysis.
Useful operations include:

1. describe what distinguishes one group from all others;
2. compare two named groups using supplied rules and metrics;
3. summarize the process/model without adding causes;
4. define a supplied metric and report its value.

Reject requests outside the supplied evidence and task contract. In particular,
do not let the presentation model infer causation, policy compliance, business
value, or corrective action merely from cluster membership.

### Evaluate explanation usefulness directly

Technical rule quality and verbalization quality are different tests:

- **Rule fidelity/accuracy:** does the rule represent the model output?
- **Rule coverage:** how much of the relevant model behavior does it explain?
- **Soundness:** does the narrative contain only entities and relationships
  supported by the rule?
- **Completeness:** did it preserve the important rule conditions?
- **Context awareness:** did it place supplied entities and metrics in the
  correct domain relationship?
- **Fluency and length:** can the target user understand it without important
  evidence being buried?
- **Decision utility:** does it improve error detection, comparison, override,
  or escalation on the actual task?

Do not choose a model because users prefer its prose. Preference and fluency can
coexist with missing or wrong evidence. Compare outputs against the underlying
explanation artifact and test them with the people who perform the review.

## Stress-Test Local Explanations

A local surrogate such as LIME approximates a complex model near one instance.
Its result depends on how the neighborhood is sampled, how locality is weighted,
which features are available, the surrogate form, and representation choices.
Therefore, one feature chart from one run is not a stable rationale.

For a consequential case, retain an explanation reproducibility packet:

```text
case and model version
explainer implementation/version
random seed and sample count
sampling or perturbation method
locality/kernel settings
feature selection and representation
surrogate fit/fidelity
repeated-run agreement
small-input-perturbation agreement
comparison explainer, if available
known out-of-distribution samples
```

Run the explainer repeatedly and perturb the case within a domain-valid
neighborhood. Then ask:

- Do the same features retain similar direction and importance?
- Does the surrogate remain faithful to the black-box predictions locally?
- Are generated samples realistic and in distribution?
- Does a small, irrelevant input change produce a radically different story?
- Does a second explanation method support or contradict the main hypothesis?
- Is the explanation compact enough for the user without hiding interactions?

If plausible explainers disagree, report explanation uncertainty. Do not select
the most convenient chart or average contradictory rationales into false
consensus. Instability can come from the model, the locality definition,
sampling, feature representation, or the explainer itself; isolate those causes
before using the explanation in a decision.

## Monitor What the Model Relies On

Production monitoring should distinguish four changes:

| Signal | Question |
|---|---|
| Input drift | Did the distribution or quality of incoming features change? |
| Output drift | Did predictions, scores, or action rates change? |
| Performance drift | Did error, calibration, cost, or workflow outcomes worsen once truth arrived? |
| Explanation drift | Did the model begin relying on different features, directions, or interactions? |

Explanation drift can reveal a changed relationship before aggregate error
crosses a threshold, and it gives the reviewer a hypothesis about which feature
changed. It is not proof of concept drift or model failure: explainer
instability, seasonal variation, correlated inputs, changed missingness, or a
moving reference window can produce the signal.

Maintain a versioned baseline distribution of explanation values on a trusted
reference period. Compare rolling windows against it and record:

```text
reference dates and model/explainer version
feature contribution mean, spread, sign, and ranking
current-window dates and data-quality state
drift score and per-feature contributors
threshold, sensitivity settings, and alert history
prediction/error/outcome measures over the same window
review verdict and authorized response
```

### Retraining is a governed change

A drift alert opens an investigation. It does not authorize automatic
retraining. Before changing the model:

1. confirm the input pipeline and labels are sound;
2. identify whether the change is expected, temporary, harmful, or unresolved;
3. compare against input, output, and performance drift;
4. test the candidate model on stable, recent, edge, and regression cases;
5. compare feature reliance and workflow outcomes before and after;
6. obtain the named approval and preserve rollback.

Choose window size, threshold, cooldown, and minimum evidence using the joint
cost of missed drift, false alarms, review labor, retraining, and regression
risk. A detector that maintains accuracy by retraining continuously may be
operationally worse than a slightly less sensitive detector with meaningful
human review.

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

Additional source for the explanation/verbalization evidence chain: Amling et
al., “Bridging the Interpretability Gap in Process Mining,” in *Explainable
Artificial Intelligence: xAI 2025 Proceedings, Part II* (CCIS 2577), physical
PDF pp. 97-122 (printed pp. 78-103), reviewed in full 2026-07-27 from
`raw/Explainable Artificial Intelligence - xAI 2025 Proceedings Part 2 (CCIS
2577).pdf`. Its seven-participant, single-event-log user study supports a design
pattern and evaluation vocabulary, not a general ranking of current models.

Additional source for local-explanation validation: Knab et al., “Which LIME
Should I Trust? Concepts, Challenges, and Solutions,” in the same proceedings,
physical PDF pp. 47-71 (printed pp. 28-52), reviewed in full 2026-07-27. The
paper is a structured literature review and taxonomy of LIME variants; retained
the locality, fidelity, interpretability, stability, and efficiency failure
classes plus reproducibility/evaluation requirements, not a preferred variant.

Additional source for explanation-drift monitoring: Teixeira, Pinto, and Vale,
“Detecting Concept Drift with SHapley Additive ExPlanations for Intelligent
Model Retraining in Energy Generation,” in the same proceedings, physical PDF
pp. 173-185 (printed pp. 156-168), reviewed in full 2026-07-27. Retained the
feature-contribution baseline, rolling comparison, dynamic-threshold tradeoff,
and joint accuracy/retraining-cost evaluation. Its one energy-forecasting case
and highly frequent retraining result do not justify automatic retraining or
general performance claims.
