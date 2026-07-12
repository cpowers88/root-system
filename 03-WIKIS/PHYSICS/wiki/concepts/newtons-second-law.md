---
type: concept
status: draft
---

# Newton's Second Law

## What is the physical idea?

The acceleration of an object is directly proportional to the net force on it and inversely proportional to its mass. Bigger net force → bigger acceleration. More massive object → smaller acceleration for the same force. The direction of acceleration is always in the direction of the net force.

## What real-world situation does it describe?

Every situation where something speeds up, slows down, or changes direction: a car accelerating from a stoplight, a ball falling under gravity, a rocket launching, a block sliding down a ramp, an elevator accelerating upward.

## Objects / System Involved

One object (or one system treated as a unit). Apply Newton's Second Law separately to each object in a multi-body system.

## Quantities That Change

Net force (ΣF) produces acceleration (a). Mass (m) is the resistance to that change.

## Model or Equation

$$\sum \vec{F} = m\vec{a}$$

Component form (the working form for most problems):

$$\sum F_x = ma_x \qquad \sum F_y = ma_y$$

See [[../equations/newtons-second-law]] for full details.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| ΣF | net (vector sum) of all forces on the object | N = kg·m/s² |
| m | mass | kg |
| a | acceleration | m/s² |

## Calculus Connection

For constant force: F = ma is algebraic.
For time-varying force: F(t) = m · dv/dt, which means F(t) = m · d²x/dt².
Integrating: v(t) = v₀ + (1/m)∫F dt. This is the foundation of the impulse-momentum theorem (Stage 9) and work (Stage 7).

## Diagram / Visual Model

**Solving procedure:**
1. Draw FBD — identify all forces on object.
2. Choose coordinate axes (align one axis with the acceleration direction when possible).
3. Write ΣF_x = ma_x and ΣF_y = ma_y.
4. Substitute all forces with signs, plug in known values, solve for unknown.

```
       +y
        ^
        | n (normal)
        |
[block]---> +x (direction of acceleration)
        |
        v
       w = mg (weight)

x: F_applied − f_friction = ma_x
y: n − mg = 0 (no vertical acceleration)
```

## Problem Types That Use This

- [[../problem-types/fbd-single-object]]
- [[../problem-types/fbd-connected-objects]]
- [[../problem-types/inclined-plane]]
- [[../problem-types/atwood-machine]]
- [[../problem-types/friction-problems]]

## Common Beginner Mistake

Applying ΣF = ma to the whole system and then using the wrong mass to find an internal force (like tension). The total-system equation gives total acceleration, but tensions or contact forces require a FBD for one part of the system only, with that part's mass.

## Practice Next

[[../drills/newtons-second-law-drill]] — seven problems from simple to compound systems.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 5.4–5.5, pp. 117–127.
