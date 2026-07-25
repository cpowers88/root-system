---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, alignment, training-data, representation, bias, evaluation, audit]
---

# Training-Data Representation and Feedback Risk

**Summary**: A model does not encounter the world directly. It encounters a
representation selected through sensors, labels, datasets, categories, and an
objective. Those choices determine whose cases the model learns well, which
correlations it treats as meaningful, and which historical patterns it can
amplify after deployment. The first alignment question is therefore not “Is the
algorithm biased?” but “What population, purpose, and world does its training
representation encode?”

**Source**: `raw/TheAlignmentProblem.pdf` (Brian Christian, *The Alignment
Problem: Machine Learning and Human Values*, 2020), Introduction (physical PDF
pp. 13-25) and Chapter 1, “Representation” (pp. 26-66), reviewed as one complete
chunk. Chapter 2 begins on physical p. 67; boundary visually verified.

**Last updated**: 2026-07-16

## The Representation Chain

Every learned system contains a chain of design decisions:

```text
real population and behavior
  -> captured examples
  -> selected labels/categories
  -> numerical representation
  -> training objective
  -> learned correlations
  -> deployment decisions
  -> changed future data
```

The training algorithm can behave exactly as designed while the system fails at
any other link. The Google Photos case described in the chapter was not evidence
that stochastic gradient descent itself contained a racial rule. It exposed a
failure of training-set coverage and evaluation. Likewise, a language embedding
trained to predict nearby words can accurately encode cultural stereotypes even
though no engineer explicitly programmed them.

## Coverage Is a Performance Variable

Aggregate accuracy hides unequal performance. A dataset may be large while still
being thin for particular populations, conditions, poses, ages, environments, or
intersections of attributes. The chapter's strongest example is the Gender
Shades evaluation: commercial classifiers that looked roughly accurate overall
performed dramatically worse for dark-skinned women than for light-skinned men.

The audit implication is direct:

- identify the deployment population before accepting benchmark results;
- examine dataset composition, not just dataset size;
- disaggregate performance across relevant groups and intersections;
- test rare but consequential operating conditions;
- treat a pretrained model's undisclosed training data as a material unknown;
- ask “accurate on what, and for whom?” whenever a vendor gives one number.

## Sampling Bias and World Bias Are Different

Two problems require different responses:

1. **Sampling bias**: the dataset fails to represent the intended population.
   Improve collection, rebalance evaluation, and test missing conditions.
2. **World bias**: the data accurately records an unequal or stereotyped world.
   More representative data alone will faithfully reproduce the same pattern.
   The desired target must be chosen rather than discovered.

This distinction prevents a common category error: assuming that a model trained
on more historical data will automatically become more just. Historical accuracy
and desired future behavior are not the same objective.

## Debiasing Is an Explicit Value Choice

Removing a visible sensitive dimension does not necessarily remove the structure
around it. The chapter's word-embedding work shows that explicit gender links can
be neutralized while clusters of stereotypically gendered occupations remain.
A cosmetic metric improvement can therefore conceal residual structure or even
make the system harder to audit.

Any debiasing method should name:

- which associations should remain useful;
- which associations should be suppressed;
- the application and affected population;
- the accuracy or utility tradeoff accepted;
- the tests used to detect indirect residual effects.

There is no value-free optimization target waiting to be found. The target is a
design and policy decision requiring domain and stakeholder input.

## Deployment Turns Description into Intervention

A representation may be useful descriptively and dangerous prescriptively.
Language embeddings can reveal changes in public stereotypes over time; using the
same associations to rank job applicants can reinforce those stereotypes. Once a
model affects hiring, policing, lending, or allocation, its outputs help generate
the next round of training data. A small historical skew can become a reinforcing
feedback loop.

Before deployment, ask:

1. Was this representation built for the present use?
2. Which groups or conditions are sparse or absent?
3. Which correlations are descriptive but should not drive a decision?
4. Can the decision change the data that later retrains the model?
5. What independent outcome measure could reveal amplification?

## Connects To

- [[algorithmic-fairness-metrics-ground-truth-and-intervention]] - what happens
  after a representation becomes a consequential prediction.
- [[interpretable-models-and-human-oversight]] - ways to inspect whether a model
  is relying on the intended evidence.
- [[nist-ai-rmf]] - supplies the MAP/MEASURE/MANAGE governance structure around
  these representation and feedback risks.
- [[openai-evals-and-red-teaming]] - evaluation sets must cover the people,
  conditions, and failure modes that the deployment actually faces.

## Retrieval Notes

**Use when**: Reviewing training data, vendor benchmarks, embeddings, a pretrained
model, automated ranking, or any system whose output will influence future data.

**Do not use as**: A current legal standard or a claim that representation alone
solves fairness. It identifies the first layer of the problem.
