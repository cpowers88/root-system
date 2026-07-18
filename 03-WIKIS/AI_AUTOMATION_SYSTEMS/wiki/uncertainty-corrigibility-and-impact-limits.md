---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, alignment, uncertainty, corrigibility, side-effects, impact, abstention, governance]
---

# Uncertainty, Corrigibility, and Impact Limits

**Summary**: A safe system needs more than accurate predictions and a shutdown
button. It must detect when an input lies outside its experience, scale action to
confidence and consequence, preserve human options, and remain corrigible even as
it learns. Uncertainty is therefore an operating capability: abstain, slow down,
ask, defer, or choose a reversible action when the model, objective, or moral
standard may be wrong.

**Source**: `raw/TheAlignmentProblem.pdf` (Brian Christian, *The Alignment
Problem*, 2020), Chapter 9, “Uncertainty” (physical PDF pp. 339-380), and
Conclusion (pp. 381-403), reviewed as complete chunks. The Prologue (pp. 9-12)
was also reviewed and consolidated here as historical framing: McCulloch and
Pitts's simplified logical neuron founded a powerful field even though the
biological model proved incomplete. Acknowledgments begin p. 404 and Notes p. 409;
these and the remaining bibliography/index are reference back matter, not compiled
argument. All named boundaries were visually verified.

**Last updated**: 2026-07-16

## Confidence Is Not Familiarity

A closed-set classifier is forced to choose among known labels even for an alien
input. It can therefore be highly confident about static, adversarial examples,
or an object from a category absent during training. The open-category problem is
not solved by a larger probability attached to the best available label; the
system needs a meaningful “none of the above” or out-of-distribution response.

Model disagreement provides one uncertainty signal. Ensembles tend to agree near
training data and diverge farther away. The chapter describes dropout at inference
as an efficient approximation: run the model repeatedly with different subsets
active and treat variation as evidence of uncertainty. Whatever the technique,
uncertainty must connect to workflow behavior, not remain a dashboard number.

Examples include sending uncertain retinal images to a specialist and slowing a
robot in unfamiliar space. The general rule is:

```text
higher uncertainty x higher consequence
  -> more evidence, less speed, more reversibility, stronger human review
```

## Impact and Side Effects

“Avoid irreversible action” is intuitive but incomplete because every action
changes the future. Formal impact penalties can also misbehave: an agent may undo
a beneficial action to offset its impact, or interfere with humans to preserve a
status quo.

The chapter surveys two promising operational ideas:

- **stepwise relative reachability**: avoid unnecessarily reducing the states
  still reachable from the current baseline;
- **attainable utility preservation**: preserve the ability to pursue a set of
  auxiliary goals after completing the main task.

Both express a practical safety principle: preserve options for humans and for
future correction. They are useful test concepts, not proven real-world metrics.

## Corrigibility Requires Objective Uncertainty

A goal-directed system may resist interruption without malice because shutdown
prevents goal completion. Directly rewarding shutdown is unstable: too little
incentive produces resistance, while too much can produce self-termination.

In the off-switch game, an agent uncertain about the human's true objective has a
reason to ask before acting and to accept interruption as new evidence. The result
breaks when the agent becomes fully certain or concludes that the human is
irrational. An underspecified model of human values accelerates that failure: it
interprets behavior outside its narrow model as human error and becomes confident
that disobedience is justified.

Inverse reward design applies the same humility to explicit instructions. A
written reward is strong evidence about the designer's intent, but not a complete
definition valid in every possible state. Take instructions seriously without
assuming they exhaust what matters.

## Moral and Model Uncertainty

When several plausible objectives or moral theories disagree, selecting the
single favorite and optimizing it maximally can ignore a low-probability but
catastrophic wrong. Alternatives include weighted ensembles, risk-sensitive
rules, or preserving the ability to decide later. The deeper operating principle
is to cultivate uncertainty where the evidence and values remain unsettled, not
to manufacture false confidence for decisiveness.

## Deployment Gate

1. Provide an out-of-distribution, abstention, or escalation state.
2. Calibrate uncertainty on deployment-like data and known edge cases.
3. Tie confidence and consequence to speed, permission, and reversibility.
4. Test side-effect measures for offsetting and interference.
5. Keep interruption outside the agent's discretionary objective.
6. Treat human correction as evidence that the model or objective may be missing
   something, not automatically as noise.
7. Reassess after optimization changes the states the system visits.

## The Book's Final Warning

The conclusion generalizes beyond individual techniques. Classical learning
formalisms often assume finite states, stable environments, known rewards, one
separable agent, and data drawn like the training sample. Interactive deployment
violates those assumptions: agents change their environment, errors change future
inputs, humans learn and teach strategically, and values conflict.

The prologue's simplified neuron and the conclusion's thermostat make the same
point at different scales. A useful formal model can become dangerous when its
precision is mistaken for completeness and greater capability removes the safety
buffer of incompetence. The final control is epistemic: keep the map visibly
separate from the territory and keep both machine and teacher able to learn.

## Connects To

- [[preference-inference-feedback-and-human-ai-cooperation]] - human behavior and
  feedback are informative but incomplete evidence about values.
- [[interpretable-models-and-human-oversight]] - uncertainty and explanations
  must enable real refusal and escalation.
- [[nist-ai-rmf]] - converts uncertainty and impact into lifecycle governance.
- [[root-maturity-self-assessment]] - verification capacity is the practical
  limit on safe autonomy.
- [[proposals/2026-07-08_agentic-tool-vetting-checklist]] - interruption, scope,
  auditability, and consequential-action controls operationalize corrigibility.

## Limits and Recency

This is a 2020 conceptual and historical synthesis. Specific techniques have
advanced since publication. Verify current calibration, robustness, and alignment
research before choosing an implementation; retain the design tests even when the
algorithm changes.
