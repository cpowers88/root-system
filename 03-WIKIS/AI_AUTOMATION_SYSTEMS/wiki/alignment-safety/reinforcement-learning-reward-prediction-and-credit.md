---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, alignment, reinforcement-learning, reward, temporal-difference, evaluation]
---

# Reinforcement Learning: Reward, Prediction, and Credit

**Summary**: Reinforcement learning can turn a scalar reward into increasingly
effective behavior, but that strength does not answer the prior design question:
which reward will actually produce the behavior humans intend? Temporal-difference
learning and reward-prediction errors explain how an agent assigns credit and
updates expectations. They also show why capability can improve while alignment
does not: the learner may become excellent at optimizing the wrong signal.

**Source**: `raw/TheAlignmentProblem.pdf` (Brian Christian, *The Alignment
Problem*, 2020), Chapter 4, “Reinforcement” (physical PDF pp. 150-187), reviewed
as one complete chunk. Chapter 5 begins on physical p. 188; boundary visually
verified.

**Last updated**: 2026-07-16

## The Architecture

A reinforcement-learning agent repeatedly observes a state, takes an action,
receives a reward, and enters a new state. Its policy chooses actions; its value
function estimates the future return available from states or actions. An
actor-critic system separates those jobs: the actor behaves, while the critic
uses outcomes to improve the actor.

The reward hypothesis proposes that purposes can be represented as maximizing a
single cumulative scalar. That compression makes general algorithms possible,
but it is an assumption, not a discovery about human values. Some objectives are
incommensurable, contextual, contested, or only partially observable.

## Credit Assignment Is Prediction Updating

Delayed outcomes make it difficult to know which earlier action deserves credit.
Temporal-difference learning addresses this by updating an estimate whenever the
new estimate of the future differs from the old one. The learner need not wait
until the entire episode ends: a newly promising or disappointing state supplies
an immediate teaching signal.

The chapter connects this mechanism to dopamine research. Dopamine activity is
better understood as a reward-prediction error than as reward itself:

- an unexpectedly good result produces a positive update;
- an expected result produces little update;
- an omitted expected result produces a negative update.

The distinction matters operationally. Learning responds to changes in expected
future value, not simply to the amount of reward received. A stable score can stop
teaching, and a volatile proxy can dominate learning even when it is not the true
goal.

## The Alignment Question Comes First

Classical reinforcement learning asks which policy maximizes a specified reward.
Alignment reverses the problem: which specification causes the learned policy to
serve the intended purpose across the situations it will encounter?

Before using a reward-driven agent, document:

1. the real outcome humans care about;
2. the observable signal used as reward;
3. the time horizon and discounting assumptions;
4. who or what receives the consequences;
5. behaviors that can increase reward without improving the outcome;
6. the conditions under which the reward stops being a valid proxy.

A rising training return is evidence that optimization works. It is not evidence
that the objective was right.

## Connects To

- [[reward-shaping-curiosity-and-safe-exploration]] - sparse rewards and proxy
  failures motivate shaping and intrinsic objectives.
- [[preference-inference-feedback-and-human-ai-cooperation]] - infers a reward
  from behavior or feedback instead of assuming it is already known.
- [[uncertainty-corrigibility-and-impact-limits]] - preserves doubt about the
  objective and limits action when confidence or impact is unsafe.
- [[openai-evals-and-red-teaming]] - evaluation must distinguish optimization
  success from task and safety success.

## Retrieval Notes

**Use when**: Reviewing an agent score, reinforcement-learning design, reward
model, long-horizon task, or unexplained gap between training return and desired
behavior.

**Do not use as**: A claim that one scalar can faithfully encode every human
purpose or that biological reward systems directly specify an engineering design.
