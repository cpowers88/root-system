---
domain: systems
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, human-factors, human-centered-design, audit]
---

# Human-Centered Design: Conceptual Models, Action Cycles, and Knowledge in the World

**Summary**: A system becomes understandable when its visible structure helps
people discover possible actions, map controls to results, see the resulting
state, and use external cues instead of carrying arbitrary detail in memory.
This page combines the durable models from Chapters 1-4.

**Sources**: `The-Design-of-Everyday-Things-Norman-2002.pdf`, 2002 preface;
Ch. 1 (pp. 1-33), Ch. 2 (pp. 34-53), Ch. 3 (pp. 54-80), and Ch. 4
(pp. 81-104), reviewed as four named chunks.

**Last updated**: 2026-07-15

## The Communication Chain

```text
designer's model -> system image -> user's mental model -> action
```

The designer cannot rely on intent. The user sees only the system image: the
interface, physical form, labels, documentation, state, and feedback. If that
image is incomplete or contradictory, a reasonable user can form the wrong
model and take the wrong action. Training may compensate, but it does not erase
the design defect.

## Six Elements of an Understandable System

| Element | Exact working question |
|---|---|
| Affordance | What actions does the object or interface appear to permit? |
| Visibility | Can the user see the relevant controls, choices, and system state? |
| Conceptual model | Can the user predict what the system will do and why? |
| Mapping | Is the relationship between a control and its result apparent? |
| Feedback | Does the system promptly show what action occurred and what state changed? |
| Constraint | Does the design eliminate or narrow invalid actions before instructions are needed? |

A label can clarify an unfamiliar control, but repeated instructions pasted
onto an object or workflow are evidence that the system image is not carrying
enough of the explanation.

## The Seven-Stage Action Cycle

Norman separates action into one goal plus three execution and three evaluation
stages:

```text
goal
  -> form intention
  -> specify action sequence
  -> execute
  -> perceive system state
  -> interpret state
  -> evaluate result against goal
```

The **gulf of execution** is the distance between what the user wants and the
actions the system makes discoverable. The **gulf of evaluation** is the
distance between what the system did and the user's ability to perceive and
interpret it. Good design narrows both.

## Knowledge in the Head and in the World

People often perform accurately without memorizing every detail because the
environment carries part of the knowledge. Calendars, checklists, templates,
labels, visible status, standard placement, and meaningful structure reduce the
amount of arbitrary recall required.

The tradeoff:

- Knowledge in the head is fast and portable once learned, but it requires
  learning and is vulnerable to forgetting.
- Knowledge in the world is easier to retrieve and can act as its own reminder,
  but only when it is visible, correctly placed, and available at the moment of
  action.
- Strong systems combine both. They use stable conventions and repeated practice
  while keeping critical state and next actions visible.

This directly supports `.ROOT`'s Chris profile: precise terms, physical anchors,
checklists, named status owners, and one visible next action are not remedial
extras. They are sound human-centered system design.

## Four Constraint Types

- **Physical**: geometry or mechanics make invalid assembly/action impossible.
- **Semantic**: the meaning of the situation narrows what makes sense.
- **Cultural**: learned conventions narrow expected behavior.
- **Logical**: remaining parts or choices imply the only valid completion.

Use natural constraints before warnings. Use training and standards when the
relationship is necessarily arbitrary.

## Audit Translation

For each failure point, ask:

1. What did the operator reasonably believe the system state was?
2. What in the system image produced that belief?
3. Which execution or evaluation gulf was open?
4. Could mapping, feedback, visible state, or a constraint close it?
5. Is the workflow asking memory to carry information the environment should hold?

## Connects to

[[designing-for-human-error-and-recovery]],
[[user-centered-system-design-principles-and-tradeoffs]], and
[[modeling-process-and-client-ethics]].

## Use / Retrieval Notes

**Use when**: A person says a tool or process is confusing, training-dependent,
or easy to operate incorrectly.

**Proof**: Redesign one real control, state display, template, or handoff so a
new user can infer the correct action and verify the result without explanation.
