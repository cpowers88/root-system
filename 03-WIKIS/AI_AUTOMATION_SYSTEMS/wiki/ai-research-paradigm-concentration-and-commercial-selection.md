---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, research, deep-learning, concentration, commercialization, academia, governance, historical]
---

# AI Research Paradigms, Concentration, and Commercial Selection

**Summary**: The dominant AI paradigm was selected by scientific performance and
by its compatibility with commercial power. Deep learning scales with data,
compute, and general-purpose infrastructure that large platforms already control;
it also converts statistical prediction into products on corporate planning
timelines. As industry funding, talent, and compute came to dominate the field,
alternative research paths lost the institutional capacity to compete. The result
is path dependence: today's model architecture reflects who could fund and
commercialize research, not proof that all other approaches were exhausted.

**Source**: `raw/empireofAIDreamsandNightmares.pdf` (Karen Hao, *Empire of AI*,
2025), Chapter 4, “Dreams of Modernity” (physical PDF pp. 92-118), reviewed as
one complete dense chapter chunk. Chapter 5 begins p. 119; boundaries visually
verified.

**Last updated**: 2026-07-16

## “Artificial Intelligence” Is a Direction-Setting Label

The chapter treats the field's name as more than description. “Intelligence”
invites anthropomorphism, implies universal desirability, and encourages progress
to be measured against human capabilities. Yet there is no settled scientific
definition of intelligence, and benchmarks repeatedly stop counting as the goal
once machines pass them.

This ambiguity has operating consequences:

- claims can slide between narrow pattern matching and humanlike understanding;
- capability demonstrations become evidence for an ever-receding AGI objective;
- present costs can be justified by benefits attached to an undefined future
  system;
- developers can compare models to humans when useful and call them mere tools
  when responsibility is at issue.

Any AI proposal should therefore define the actual task, measurable outcome, and
known limitations without relying on “intelligence” as explanatory shorthand.

## Scientific Merit and Commercial Fit

The historical contest between symbolic and connectionist AI is often told as
deep learning winning solely because it was better. Hao's account adds a selection
mechanism:

| Paradigm | Strength | Commercial constraint/advantage |
|---|---|---|
| Symbolic or expert systems | Explicit knowledge and inspectable reasoning | Slow, domain-specific knowledge engineering; uncertain path to revenue |
| Neural networks | Flexible statistical pattern matching across data types | Data- and compute-hungry, but reusable and rapidly productizable by large platforms |
| Neurosymbolic and other hybrids | Potential combination of learning and reasoning | Far less funding and institutional momentum to test at comparable scale |

Neural networks produced real breakthroughs. They also fit the assets and
business model of Google, Meta, Microsoft, and other platforms: user data, cloud
infrastructure, advertising, general-purpose products, and capital-intensive scale.
Commercial success then generated more funding, talent, data, and compute for the
same approach.

## Research Capture Through Resource Dependency

The chapter documents a reinforcing loop:

```text
commercially useful deep learning
  -> greater corporate revenue and investment
  -> better compute, data, and compensation
  -> talent moves from universities to industry
  -> industry authors more influential research
  -> students train for the funded paradigm
  -> fewer viable alternatives
```

The cited historical measures include a sharp rise in AI PhDs entering industry,
industry affiliation among top-performing models, and corporate coauthorship of
influential papers. These are 2025-book figures requiring primary-source checking
before reuse, but the mechanism is durable: dependence can shape a research agenda
without any explicit censorship.

## Why Concentration Matters Technically

Deep learning's limitations include distribution shift, opaque internal rules,
adversarial sensitivity, hallucination, and amplification of representational
imbalance. Increasing scale has improved many capabilities without eliminating
those failure classes. A concentrated field is less able to test whether the
limitations require better data and architecture, hybrid methods, or an entirely
different paradigm.

The governance question is therefore not “Does deep learning work?” It plainly
does. It is “Which problems and alternatives are we failing to investigate because
one path controls the money, compute, publication prestige, and jobs?”

## Portfolio Review for AI Adoption

Before choosing a frontier general-purpose model:

1. Define whether the task needs generation, retrieval, classification, rules, or
   causal/domain reasoning.
2. Compare a smaller or specialized model and a deterministic/rule-based baseline.
3. Price verification, privacy, and failure handling as part of the architecture.
4. Identify which vendor-controlled resources create lock-in.
5. Ask whether the benchmark reflects the deployed population and workflow.
6. Preserve funding for competing approaches when uncertainty is material.

## Connects To

- [[training-data-representation-and-feedback-risk]] - data selection determines
  what a statistical model can represent.
- [[interpretable-models-and-human-oversight]] - complex models should earn their
  deployment advantage over inspectable baselines.
- [[ai-index-2026]] - supplies current ecosystem-scale evidence on frontier
  convergence and declining disclosure.
- [[root-maturity-self-assessment]] - capability growth without verification
  growth creates the same concentration risk at system scale.

## Limits and Source Framing

Hao explicitly argues that the current paradigm reflects commercial and political
choices and uses an empire/colonialism frame. This page preserves the mechanism
without treating the metaphor as a neutral empirical category. Verify the book's
quantitative claims against its cited primary studies before external publication.
