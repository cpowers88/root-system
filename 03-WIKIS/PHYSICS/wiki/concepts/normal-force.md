---
type: concept
status: draft
---

# Normal Force

## What is the physical idea?

The **normal force** is the contact force that a surface exerts on an object perpendicular to the surface. It prevents the object from passing through the surface. "Normal" means perpendicular — it is always directed away from the surface, into the object.

## What real-world situation does it describe?

- Floor pushing up on you as you stand.
- Table pushing up on a book.
- A ramp pushing perpendicularly on a sliding block.
- Your back pressing into a seat when a car accelerates forward.
- A wall pushing horizontally on a ladder leaning against it.

## Objects / System Involved

Any object in contact with a surface. The surface provides the normal force; the object provides the equal-and-opposite reaction (Newton's Third Law).

## Quantities That Change

The normal force adjusts to maintain the no-penetration constraint. On a horizontal floor with only weight and normal force, n = mg. Add a downward push or pull, and n changes. Accelerate vertically, and n changes.

## Model or Equation

Found by applying Newton's Second Law perpendicular to the surface. For a block on a horizontal surface with only weight and normal:

$$\sum F_y = n - mg = 0 \quad \Rightarrow \quad n = mg$$

On an incline at angle θ (no other perpendicular forces, no perpendicular acceleration):

$$n = mg\cos\theta$$

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| n | normal force | N |
| m | mass | kg |
| g | gravitational acceleration | m/s² |
| θ | angle of incline from horizontal | degrees or radians |

## Calculus Connection

None. Normal force is found algebraically from the perpendicular component of Newton's Second Law.

## Diagram / Visual Model

```
Horizontal surface:          Inclined surface (angle θ):
    n (perpendicular           n (perpendicular
    to surface = vertical)     to slope = tilted)
    ^                            ^
    |                           /
  [block]                    [block]
    |                          /
    v                         /
   mg                     mg (straight down)

n = mg                  n = mg cosθ (component perpendicular to slope)
```

## Problem Types That Use This

- [[../problem-types/fbd-single-object]] (finding n from ΣF_y = 0)
- [[../problem-types/friction-problems]] (n feeds directly into f = μn)
- [[../problem-types/inclined-plane]] (n = mg cosθ is always step 1)

## Common Beginner Mistake

Assuming the normal force always equals mg. This is only true on a flat horizontal surface with no other vertical forces and no vertical acceleration. Common situations where n ≠ mg:

- Inclined plane: n = mg cosθ < mg
- Elevator accelerating upward: n = m(g + a) > mg
- Elevator accelerating downward: n = m(g − a) < mg
- Someone pushing down on the object: n > mg
- Someone pulling up on the object: n < mg

The correct approach: always derive n from ΣF_perp = 0.

## Practice Next

Work through [[../drills/inclined-plane-drill]] Problem 3, which requires finding n on an incline first before computing friction.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 5.7, pp. 132–135.
