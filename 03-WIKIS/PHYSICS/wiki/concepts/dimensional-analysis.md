---
type: concept
timeline: reference
status: draft
---

# Dimensional Analysis

## What is the physical idea?

**Dimension** describes the physical *nature* of a quantity (length, mass, time) independent of the specific unit used to measure it. Dimensional analysis is the technique of checking whether an equation is even physically plausible by comparing the dimensions on both sides — without plugging in any numbers.

## What real-world situation does it describe?

Any time you derive or are given a formula and want to sanity-check it before trusting it. If the dimensions don't match, the equation is definitely wrong — full stop, no need to check numbers.

## Objects / System Involved

N/A — this is a method applied to equations, not a physical object.

## Quantities That Change

N/A.

## Model or Equation

Dimensions are written in brackets: [length] = L, [mass] = M, [time] = T. An equation is dimensionally correct only if both sides reduce to the same combination of L, M, T.

General check form: if x ∝ aⁿtᵘ (position related to acceleration and time by unknown powers n, m), substitute dimensions:

```text
[x] = L
[a] = L/T²
[t] = T
```

Then solve for n and m by requiring the dimensions to balance on both sides.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| L | dimension of length | (not a unit — a dimension; the unit is meters) |
| M | dimension of mass | (unit: kilograms) |
| T | dimension of time | (unit: seconds) |

## Calculus Connection

None directly, but every kinematic equation introduced in Chapter 2 (which *does* come from calculus) can — and should — be checked this way.

## Diagram / Visual Model

No diagram. Mental model: treat L, M, T like algebra variables. You can multiply and divide them, but you can only add/subtract terms that have identical L/M/T combinations — exactly like you can't add "3 apples + 2 oranges" and call it 5 of anything.

## Problem Types That Use This

- [[../problem-types/dimensional-consistency-check]]

## Common Beginner Mistake

Thinking dimensional analysis can find the *numerical* constant in an equation (like the ½ in x = ½at²). It cannot — dimensionless numbers carry no dimension, so they're invisible to this check. Dimensional analysis confirms the *shape* of an equation, not the exact constants in it.

## Practice Next

Take any equation from the syllabus's upcoming chapters and verify it's dimensionally consistent before you've even learned what it means physically — this is a skill you can use as a safety net all semester.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 1.3, pp. 10–11.
