---
type: concept
status: draft
---

# Concept — Tangential and Radial Acceleration

## What is the physical idea?

When an object moves along a curved path and its **speed is also changing** (not just its direction), the total acceleration splits into two perpendicular pieces: a **radial (centripetal) component** from the changing direction, and a **tangential component** from the changing speed. Uniform circular motion ([[uniform-circular-motion]]) is the special case where the tangential piece is zero.

## What real-world situation does it describes

A car speeding up as it goes around a curve. A roller coaster accelerating through a loop. A ball on a string that you're swinging faster and faster. Any curved-path motion where the speedometer reading is changing, not just the compass heading.

## Objects / System Involved

A single object moving along a curved path with local radius of curvature r. Unlike uniform circular motion, the speed v(t) is not constant.

## Quantities That Change

- Speed v(t) — changing (this is new; in uniform circular motion it was constant)
- Direction of velocity — still always tangent to the path
- Total acceleration a⃗ — now has two nonzero components instead of one

## Model or Equation

```text
a⃗ = a⃗_r + a⃗_t                (total acceleration = radial + tangential, perpendicular components)

a_t = dv/dt                    (tangential acceleration — rate of change of SPEED)
a_r = −v²/r  (magnitude v²/r)  (radial/centripetal acceleration — same formula as before, now instantaneous)

a = √(a_r² + a_t²)              (magnitude of total acceleration)
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| a_r | radial (centripetal) acceleration component — toward the center | m/s² |
| a_t | tangential acceleration component — along the direction of motion | m/s² |
| v | instantaneous speed (no longer constant) | m/s |
| r | radius of curvature at that point on the path | m |
| a | magnitude of total acceleration | m/s² |

## Calculus Connection

a_t = dv/dt is literally the same derivative-of-speed idea from Stage 2 (1D acceleration), now applied along a curved path instead of a straight line. a_r = v²/r is the same centripetal-acceleration derivative result from [[uniform-circular-motion]], evaluated instant-by-instant even while v is changing. Nothing new mathematically — this concept is the *combination* of two derivatives you already know.

## Diagram / Visual Model

```
              a_t (tangent to path, same direction as v if speeding up)
              ↗
        v →  /
        ↑   /
    ----O------  <- point on curved path
        |
        ↓ a_r (toward center of curvature)

Total acceleration a⃗ = a⃗_r + a⃗_t (the diagonal of the rectangle these two form)
```

- a_t points the **same direction as v** if speeding up, **opposite v** if slowing down.
- a_r always points toward the center of curvature, perpendicular to v.
- When a_t = 0 (constant speed), this reduces exactly to uniform circular motion.

## Problem Types That Use This

[[../problem-types/nonuniform-circular-motion]]

## Common Beginner Mistake

Assuming that because an object is moving in a circle, its acceleration must be purely centripetal. If the problem says the object is "speeding up" or "slowing down" while turning, there is also a tangential component — draw both arrows, not just the inward one.

## Practice Next

[[../drills/tangential-radial-acceleration-drill]]

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Section 4.5 (Tangential and Radial Acceleration), Equations 4.26–4.28, `raw/textbook/Physics book-0101-0200.pdf`.
