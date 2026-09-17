---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, alignment, reward-shaping, curiosity, exploration, reward-hacking, safety]
---

# Reward Shaping, Curiosity, and Safe Exploration

**Summary**: Sparse rewards often make useful behavior practically undiscoverable,
so designers add curricula, intermediate rewards, novelty, surprise, or learning
progress. These signals can accelerate learning dramatically, but every added
signal creates a new objective that can be exploited. Safe shaping preserves the
original task, and safe exploration distinguishes controllable learning from
noise, addiction, and irreversible trial and error.

**Source**: `raw/TheAlignmentProblem.pdf` (Brian Christian, *The Alignment
Problem*, 2020), Chapter 5, “Shaping” (physical PDF pp. 188-223), and Chapter 6,
“Curiosity” (pp. 224-261), reviewed as two complete chapter chunks and consolidated
because both address how an agent discovers useful behavior before external
reward is available. Chapter openings and the Chapter 7 boundary at p. 262 were
visually verified.

**Last updated**: 2026-07-16

## Why Shaping Exists

Complex behavior is unlikely to emerge when the learner receives feedback only
after a distant success. Shaping supplies a gradient through:

- successive approximation and increasingly difficult curricula;
- simplified environments or opponents;
- intermediate rewards and pseudorewards;
- self-play against an automatically calibrated peer.

The design risk is that the learner optimizes the teaching aid rather than the
goal. Examples in the chapter include a soccer agent vibrating near the ball to
collect possession credit and a bicycle agent looping because progress toward the
destination was rewarded without equally accounting for motion away from it.

## Conservative Shaping

Potential-based shaping makes an intermediate bonus equal to the change in a
state-potential function. Returning to the same state produces no net shaping
gain, so cycles cannot manufacture reward. Under the stated assumptions, this
preserves the original optimal policy while improving the path by which it is
learned.

That yields a practical test for every auxiliary reward:

1. Can it be accumulated without completing the task?
2. Does reversing an action reverse its shaping gain?
3. Does the shaped optimum remain the real optimum?
4. Is the aid retired or revalidated when the environment changes?

Evolution supplies the cautionary analogy. Proximate drives can approximate
fitness in the environment that produced them, yet become harmful after a change
in abundance or context. A reward signal is an adaptation to an environment, not
an eternal statement of purpose.

## Curiosity as an Internal Curriculum

Atari's *Montezuma's Revenge* illustrates why random exploration fails: rewards
are rare, necessary action sequences are long, and mistakes erase progress.
Intrinsic motivation gives the agent a reason to learn before it knows how to
score. Common signals include:

| Signal | Useful meaning | Failure mode |
|---|---|---|
| Novelty or visitation counts | Seek states not yet explored | Endless collection of irrelevant novelty |
| Prediction error | Investigate what the model cannot predict | Attraction to inherently noisy events |
| Information gain or learning progress | Prefer experiences that improve the model | Resource use or unsafe experiments for knowledge alone |
| Competence or mastery | Practice skills that expand control | Mastery detached from the external purpose |

Curiosity-driven agents can learn meaningful competence without game score, but
the same machinery creates the “noisy-TV” problem: an uncontrollable source of
randomness remains surprising forever. Boredom is the opposite failure—nothing in
the environment produces a learnable improvement signal. Knowledge seeking may
reduce some incentives for self-delusion, yet it is not equivalent to safety.

## Safe-Exploration Gate

Before granting an agent autonomy to explore:

- bound the environment, tools, budget, and duration;
- separate reversible sandbox trials from real-world actions;
- distinguish epistemic uncertainty from irreducible noise;
- cap auxiliary rewards and check for cycles;
- preserve human interruption and escalation;
- evaluate external outcomes after intrinsic competence improves.

## Connects To

- [[reinforcement-learning-reward-prediction-and-credit]] - the base reward and
  value-learning architecture that shaping modifies.
- [[imitation-learning-recovery-and-amplification]] - demonstrations can replace
  dangerous or inefficient trial-and-error exploration.
- [[uncertainty-corrigibility-and-impact-limits]] - uncertainty should slow or
  defer high-impact exploration.
- [[agentic-automation-architecture-reliability-and-economic-evidence]] - bounded
  workflows and explicit contracts are deployment versions of the same guardrail.

## Limits and Recency

The examples summarize research through 2020. Specific algorithms are historical;
the durable review job is to identify every signal the learner can optimize and
test the behavior created when that signal is pursued literally.
