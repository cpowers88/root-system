---
domain: systems
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, human-factors, human-centered-design, automation, audit]
---

# User-Centered System Design: Seven Principles and Real Tradeoffs

**Summary**: Good design is not maximum simplicity, maximum features, or maximum
automation. It balances capability, usability, safety, cost, reliability, and
aesthetics while making valid action discoverable and failure recoverable.

**Sources**: `The-Design-of-Everyday-Things-Norman-2002.pdf`, Ch. 6,
"The Design Challenge" (pp. 141-186), and Ch. 7, "User-Centered Design"
(pp. 187-218), reviewed as two complete chapter chunks.

**Last updated**: 2026-07-15

## Why Useful Systems Still Become Difficult

- **Designer-user distance**: experts operate from knowledge in their heads and
  underestimate what an infrequent user can infer from the system image.
- **Feature accumulation**: each feature adds interactions, modes, documentation,
  and failure combinations; complexity can grow faster than the feature count.
- **Local optimization**: cost, appearance, technical novelty, or one safety fix
  can be improved while the whole user experience becomes worse.
- **Evolution and installed base**: standards, habits, equipment, and training make
  a theoretically superior redesign expensive or disruptive.
- **Capability variation**: vision, hearing, dexterity, attention, experience, and
  stress differ across users and across the same person's life.

The answer is not automatically fewer controls. Too few controls can force one
control to serve many hidden modes. The better target is appropriate complexity:
show the controls relevant to the present task and keep their function stable.

## Norman's Seven Design Principles

1. Use knowledge in both the world and the head.
2. Simplify the structure of the task.
3. Make possible actions and resulting state visible, closing the execution and
   evaluation gulfs.
4. Make mappings between intent, control, action, state, and outcome natural.
5. Exploit natural and artificial constraints.
6. Design for error, detection, reversal, and recovery.
7. When arbitrary relationships remain, standardize them so they are learned once.

Standardization is a last-resort solution to unavoidable arbitrariness, and timing
matters: too early can freeze an immature design; too late can leave incompatible
conventions too costly to reconcile.

## Four Ways to Simplify a Task

- Keep the task but provide mental aids and visible structure.
- Use technology to make previously invisible or difficult steps easier.
- Automate parts of the task while keeping the human's model and intervention path.
- Change the nature of the task so the old difficult sequence is no longer required.

Automation can remove burden, but overautomation creates out-of-the-loop operators
who are asked to intervene only when the system is unfamiliar and failing. Keep
state, limits, and manual recovery visible.

## Applied Review for `.ROOT` and Client Systems

Use this sequence on a workflow, dashboard, form, agent, or operating procedure:

1. Name the user's actual goal, frequency of use, stress, and prior knowledge.
2. Draw the current action/state/recovery path.
3. Mark every invisible state, arbitrary mapping, hidden mode, and memory demand.
4. Identify where the system blames the user for a predictable design outcome.
5. Prefer safe defaults, visible state, constraints, and reversibility over prose.
6. Test with a realistic user and task; the designer's successful walkthrough is
   not usability evidence.
7. Record the tradeoff: what became safer/easier and what cost or capability changed.

For `.ROOT`, this supports progressive loading, owner pointers instead of copied
state, explicit write gates, readable handoffs, and one visible next action. It
argues against adding more instructions when the actual defect is placement,
mapping, hidden state, or missing feedback.

## Limits

The source predates modern mobile conventions, accessibility standards, and current
AI systems. Translate the principles, but validate implementation against current
standards and observed users. Deliberate difficulty can be valid for security,
training, or games; it must be intentional and matched to the real goal.

## Connects to

[[human-centered-design-conceptual-models-and-action-cycle]],
[[designing-for-human-error-and-recovery]],
[[modeling-process-and-client-ethics]], and
[[bpmn-2-0-specification]].

## Use / Retrieval Notes

**Use when**: Scoping a new internal tool, reviewing an AI workflow, simplifying
an operating procedure, or deciding whether another feature should be added.

**Proof**: Observe a realistic user complete the target task, including one error
and recovery path, without designer coaching.
