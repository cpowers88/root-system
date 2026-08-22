---
type: concept
timeline: reference
status: draft
---

# Force

## What is the physical idea?

A **force** is a push or a pull — an interaction between two objects that can cause acceleration, deformation, or both. Forces are vectors: they have both magnitude and direction.

## What real-world situation does it describe?

Every interaction: your hand pushing a door, gravity pulling you toward Earth, a rope pulling a crate, a floor pushing up on your feet, air resistance slowing a moving car.

## Objects / System Involved

A force always involves two objects: the one exerting the force and the one receiving it. Newton's Third Law says these interactions are always paired.

## Quantities That Change

Net force (ΣF) → acceleration (via F = ma). A single force by itself doesn't tell you what happens — you need the net of all forces.

## Model or Equation

$$\sum \vec{F} = m\vec{a}$$

The net force is the vector sum of all forces acting on the object.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| F | force | N (newton) = kg·m/s² |
| m | mass | kg |
| a | acceleration | m/s² |

1 newton is the force needed to accelerate a 1 kg object at 1 m/s². A nickel coin weighs about 0.05 N; you weigh about 700 N.

## Calculus Connection

For constant force: F = ma is algebraic. For a force that changes over time or position: F(t) = m · dv/dt. Integration gives velocity from force history. This is the foundation of Stage 7 (work by a varying force).

## Diagram / Visual Model

Forces are drawn as arrows (vectors) on a free body diagram. The arrow starts at the object, points in the direction of the force, and has a label (T, n, w, f, F_app).

```
     T (tension, upward)
     ^
     |
   [box]
     |
     v
   w = mg (weight, downward)
```

## Problem Types That Use This

- [[../problem-types/fbd-single-object]]
- [[../problem-types/fbd-connected-objects]]
- [[../problem-types/inclined-plane]]

## Common Beginner Mistake

Treating force as a property of an object ("the block has a force of 10 N") rather than as an interaction between two objects ("gravity exerts 10 N on the block"). Forces always come in source–recipient pairs.

## Practice Next

Draw free body diagrams for a book on a table, then a hanging mass, then a block on an incline. See [[../drills/fbd-drawing-drill]].

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 5.1–5.2, pp. 109–115.
