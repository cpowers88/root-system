---
type: concept
timeline: reference
status: draft
---

# Uniform Circular Motion

## What is the physical idea?

An object moving in a circle at constant speed is still accelerating — because the direction of its velocity is constantly changing even though its magnitude isn't. This acceleration points toward the center of the circle and is called centripetal acceleration.

## What real-world situation does it describe?

A car rounding a curve at constant speed, a ball on a string swung in a horizontal circle, a satellite in circular orbit, the Moon around the Earth, a point on a spinning wheel.

## Objects / System Involved

A single object moving along a circular path of fixed radius r at constant speed v. There must be a net inward force causing this — a string, gravity, friction, or a normal force provides the centripetal force.

## Quantities That Change

- The direction of the velocity vector changes continuously (it always points tangent to the circle).
- The direction of the acceleration vector changes continuously (it always points toward the center).
- Speed does NOT change.
- Kinetic energy does NOT change (speed is constant).

## Model or Equation

**Centripetal acceleration:**
```
a_c = v²/r        (directed inward toward center)
a_c = ω²r         (using angular speed ω = v/r)
```

**Period (time for one complete revolution):**
```
T = 2πr / v
```

**Centripetal force** (the net inward force required — Newton's 2nd law applied):
```
F_c = ma_c = mv²/r     (inward)
```

**Angular speed:**
```
ω = v/r    (in rad/s)
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| v | speed (constant) | m/s |
| r | radius of circular path | m |
| a_c | centripetal acceleration | m/s² |
| T | period | s |
| ω | angular speed | rad/s |
| F_c | centripetal force | N |
| m | mass of object | kg |

## Calculus Connection

Even though speed |v⃗| is constant, the velocity vector v⃗ changes direction. Acceleration is defined as dv⃗/dt — the derivative of a vector, not just its magnitude. A vector can change even if its magnitude stays constant. This is why dv⃗/dt ≠ 0 and centripetal acceleration is real and non-zero.

The mathematical derivation: write v⃗(t) = v(-sin θ, cos θ) where θ = ωt. Taking dv⃗/dt gives a⃗ = -vω(cos θ, sin θ) — a vector of magnitude vω = v²/r pointing inward.

## Diagram / Visual Model

```
              v (tangent, pointing up here)
              ↑
              |
    ←—a_c——  O  ← object on circle
              |
              |
         center of circle (below)
         
The acceleration a_c always points from the object toward the center.
The velocity v always points tangent to the circle (perpendicular to a_c).
```

At every instant, v and a_c are perpendicular to each other. This is why speed stays constant — the force (and acceleration) does no work on the object (W = F·d cos 90° = 0).

## Problem Types That Use This

- [[../problem-types/circular-motion]]
- Also used in Stage 6 (circular motion forces) and Stage 10 (rotation)

## Common Beginner Mistake

Thinking centripetal acceleration is zero because speed is constant. Speed is constant, not velocity. Velocity is a vector; its direction changes every instant. Acceleration is the rate of change of the velocity vector, not just its magnitude.

Also: "centripetal force" is not a new type of force — it is always provided by something real (gravity, tension, friction, normal force). Never draw "centripetal force" on a free body diagram as a separate force. The net inward force equals mv²/r.

## Practice Next

Try the circular motion drill ([[../drills/circular-motion-drill]]). If speed is changing rather than constant, this is the special case — see [[tangential-and-radial-acceleration]] (still Chapter 4, Section 4.5) for the general version. Revisit this concept again when studying Stage 6 (where the force that provides centripetal acceleration is identified for different setups).

## Sources

- Serway & Jewett, 10th ed., Ch. 4.4, pp. 96–100.
