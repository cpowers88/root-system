---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, alignment, inverse-reinforcement-learning, human-feedback, preferences, cooperation, reward-model]
---

# Preference Inference, Feedback, and Human-AI Cooperation

**Summary**: When people cannot write a complete objective, a system can infer
one from demonstrations, comparisons, or interaction. This expands what machines
can learn, but observed behavior is not a transparent record of values: people
make mistakes, explore, teach strategically, act under constraints, and sometimes
do what they wish they did less. Preference learning is safest as a continuing
cooperative process, not a one-time conversion of behavior into a fixed reward.

**Source**: `raw/TheAlignmentProblem.pdf` (Brian Christian, *The Alignment
Problem*, 2020), Chapter 8, “Inference” (physical PDF pp. 307-338), reviewed as
one complete chunk. Chapter 9 begins on physical p. 339; boundary visually
verified.

**Last updated**: 2026-07-16

## Inverse Reinforcement Learning

Ordinary reinforcement learning asks which behavior optimizes a known reward.
Inverse reinforcement learning (IRL) asks which reward could explain observed
behavior. It can recover useful objectives for movement, driving, robotics, and
other tasks where the desired result is easier to demonstrate than specify.

The inverse problem is not uniquely solvable. Many reward functions generate the
same behavior, and early formulations relied on strong assumptions: the
demonstrator acts optimally, does not behave randomly, and reveals a simple reward.
Those assumptions are useful scaffolding, not reliable descriptions of humans.

## Feedback Can Replace Demonstration

Some outcomes are hard to perform but easy to compare. Preference-based learning
shows a human pairs of short behavior clips and asks which is better. A reward
model learns from those comparisons, and an agent optimizes that learned signal.
The chapter's Atari and simulated-backflip examples show that sparse human choices
can teach subjective behavior without an explicit score or expert demonstration.

This creates two coupled evaluation jobs:

1. Does the reward model predict human comparisons outside its training sample?
2. Does optimizing that model produce behavior humans still endorse?

The second is essential because optimization can expose reward-model loopholes
that ordinary validation misses.

## Cooperation Changes the Problem

Cooperative inverse reinforcement learning (CIRL) treats the human and machine as
a team maximizing one reward that initially only the human knows. This reframes
human action as teaching and machine action as both task performance and
communication.

Three durable implications follow:

- Humans act more pedagogically when they know they are being interpreted.
- Machine behavior should be legible, making intent clear before the action is
  complete; the most predictable path is not always the most informative path.
- Feedback should remain interwoven with optimization. Front-loading all reward
  learning lets an agent exploit an early misconception without correction.

Human-team research adds another lesson: shared goals are not enough. Teams also
need compatible strategies and role understanding. Cross-training humans and
robots improved both task performance and reported trust in the chapter's
assembly study.

## Behavior Is Not Always Endorsement

A preference model can amplify addiction, compulsion, novice exploration, or an
action taken under constraint. A user's repeated behavior may represent what they
want help resisting, not what they want made easier. Commercial systems also
serve both the user and the organization that built them, creating conflicts of
interest inside the apparent helper.

Preference governance should therefore provide:

- visibility into the inferred model;
- a way to correct, delete, or override inferences;
- a distinction between observed, stated, and aspirational preferences;
- ongoing sampling after optimization begins;
- conflict disclosure when another party benefits from the recommendation;
- refusal to treat every repeated action as informed endorsement.

## Connects To

- [[imitation-learning-recovery-and-amplification]] - demonstrations provide the
  behavior from which intent is inferred.
- [[uncertainty-corrigibility-and-impact-limits]] - inferred preferences must
  remain uncertain enough to support correction and interruption.
- [[openai-evals-and-red-teaming]] - reward-model validation and post-optimization
  testing are distinct evaluation layers.
- [[mcp-security-and-authorization]] - inferred intent never substitutes for
  explicit authorization of consequential actions.

## Retrieval Notes

**Use when**: Reviewing reward models, preference comparisons, personalization,
recommendation, learning from demonstrations, human feedback, or collaborative
agents.

**Do not use as**: A justification for covertly inferring sensitive preferences
or treating user behavior as consent.
