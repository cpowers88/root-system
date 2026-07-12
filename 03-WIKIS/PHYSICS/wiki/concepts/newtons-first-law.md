---
type: concept
status: draft
---

# Newton's First Law (Law of Inertia)

## What is the physical idea?

An object at rest remains at rest, and an object moving at constant velocity continues moving at constant velocity, unless acted on by a net external force.

The key idea: **inertia**. Objects resist changes to their state of motion. A net force is required to change velocity (start, stop, speed up, slow down, or change direction). Zero net force → zero acceleration → constant velocity (which includes rest as the special case v = 0).

## What real-world situation does it describe?

- A hockey puck sliding across frictionless ice keeps going at constant speed.
- You lurch forward in a car that suddenly stops — your body wanted to keep moving at the car's original speed.
- A book on a table at rest stays at rest because the normal force and gravity exactly cancel (no net force).
- A spacecraft far from any planet drifts at constant velocity indefinitely.

## Objects / System Involved

Any object. The law applies universally: the key is identifying whether the net force is zero.

## Quantities That Change

If ΣF = 0: velocity is constant (zero acceleration).
If ΣF ≠ 0: velocity changes (nonzero acceleration) — that's Newton's Second Law.

## Model or Equation

$$\text{If } \sum \vec{F} = 0, \text{ then } \vec{a} = 0 \text{ (constant velocity)}$$

This is the special case of F = ma when the left side is zero.

## Variables and Units

| Concept | Symbol | Unit |
|---|---|---|
| Net force | ΣF | N |
| Acceleration | a | m/s² |
| Constant velocity | v = constant | m/s |

## Calculus Connection

If ΣF = 0, then a = dv/dt = 0, which means v = constant (integrating gives v = v₀ with no change).

## Diagram / Visual Model

```
Case 1: At rest, ΣF = 0
         T (up)
         ^
         |
       [block]       <- stays at rest
         |
         v
         w (down)
T = w, no net force

Case 2: Moving at constant velocity, ΣF = 0
Applied force -->  [block] --> v = constant
               <-- friction
Forces balance: no net force, no acceleration
```

## Problem Types That Use This

- [[../problem-types/fbd-single-object]] (equilibrium case: ΣF = 0)
- [[../problem-types/friction-problems]] (finding friction when object moves at constant velocity)

## Common Beginner Mistake

Thinking that a moving object requires a continuous force to keep it moving. This is the Aristotelian error that Newton corrected. An object moving at constant velocity has zero net force — the applied force exactly cancels friction. Without any friction, zero force is needed to maintain constant motion.

## Practice Next

Identify whether each scenario has ΣF = 0 or ΣF ≠ 0: (1) book on table, (2) car at constant highway speed, (3) ball thrown upward at its peak, (4) satellite in circular orbit. Then see [[../drills/fbd-drawing-drill]].

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 5.2, pp. 112–114.
