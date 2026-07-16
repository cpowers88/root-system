---
domain: systems
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, human-factors, human-centered-design, reliability, audit]
---

# Designing for Human Error, Forcing Functions, and Recovery

**Summary**: Human error is expected system behavior, not an exceptional event.
The design task is to reduce predictable slips, prevent high-consequence invalid
actions, expose modes and state, detect errors quickly, and make recovery safe.

**Source**: `The-Design-of-Everyday-Things-Norman-2002.pdf`, Ch. 5,
"To Err Is Human" (pp. 105-140), reviewed as one complete chapter chunk.

**Last updated**: 2026-07-15

## Slips and Mistakes Are Different Failure Classes

- A **mistake** begins with the wrong goal, diagnosis, rule, or plan. The action
  may be executed exactly as intended and still be wrong.
- A **slip** begins with a valid goal but the performed action is not the intended
  action. Familiar routines, distraction, similarity, hidden modes, or interrupted
  sequences often produce it.

The repair must match the class. More execution training does not fix a bad
mental model; more policy prose does not fix controls that invite a slip.

## Recurring Slip Patterns

| Pattern | System condition | Design response |
|---|---|---|
| Capture error | A familiar sequence takes over from a less familiar intended sequence | Separate the paths early; add a salient checkpoint before they diverge |
| Description error | The intended target resembles another available target | Make targets physically/visually distinct and show selection state |
| Data-driven error | Incoming sensory data triggers an unintended action | Reduce competing signals; confirm the selected object/context |
| Associative activation | A related thought or cue activates the wrong action | Remove ambiguous cues and use explicit context |
| Loss of activation | The goal or next step is forgotten during interruption | Preserve resumable state and display the next unfinished action |
| Mode error | The same control behaves differently in an unclear mode | Make mode visible, reduce modes, or make the action mode-independent |

## Error-Proofing Hierarchy

1. **Remove the hazardous choice** when it serves no valid purpose.
2. **Constrain the choice** so the invalid action cannot be completed.
3. **Differentiate targets and modes** so the intended action is perceptible.
4. **Provide immediate feedback** before consequence compounds.
5. **Make the action reversible** and preserve the prior state.
6. **Warn or confirm** only when prevention and safe defaults cannot do the job.
7. **Train** for necessary complexity and truly exceptional conditions.

A confirmation prompt is not automatically a guardrail. If it appears constantly,
people habituate and click through. Confirmation earns its place at an infrequent,
consequential, and clearly described boundary.

## Forcing Functions

A forcing function structures the sequence so one condition must be satisfied
before another action can occur.

- **Interlock**: one operation prevents another from occurring in an unsafe order.
- **Lockin**: an operation cannot be stopped prematurely; the system preserves the
  action until a required condition is met.
- **Lockout**: a hazardous operation is blocked until prerequisite conditions are met.

These patterns increase reliability when narrowly tied to consequence. Overused,
they create workarounds and new failure modes.

## Audit Questions

1. Was this a mistake, slip, violation, or design-induced mode error?
2. Did the operator have an accurate, visible system state at the decision point?
3. Was the invalid action easier, faster, or more obvious than the valid one?
4. What interruption, similarity, social pressure, or workload shaped the action?
5. How quickly was the error detectable, reversible, and containable?
6. Would the same design predictably produce the same failure with another person?

## AI and Automation Translation

For AI workflows, keep reads easy and gate consequential writes; show tool target,
scope, current state, and expected effect before execution; preserve checkpoints
and rollback; and make human escalation a designed path. A model warning in prose
is weaker than a runtime constraint at the action boundary.

## Connects to

[[reliability-theory-series-parallel-and-k-out-of-n-systems]],
[[modeling-process-and-client-ethics]], and
[Just Culture and Blameless Postmortems](../../TECHNOLOGY/wiki/devops/just-culture-and-blameless-postmortems.md).

## Use / Retrieval Notes

**Use when**: An incident report ends with "operator error," a workflow has a
dangerous irreversible step, or an automation hides modes/state.

**Proof**: Replace one warning/training-only control with a constraint, visible
state, safe default, or tested recovery path.
