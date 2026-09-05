---
type: concept
timeline: reference
status: draft
---

# Concept — Coordinate Systems (Cartesian and Polar)

## What is the physical idea?

Every physics problem that involves position needs a way to say *where* something is. A coordinate system is the labeled grid you lay over the physical situation so "where" becomes a number you can compute with. The same point in space can be described two equivalent ways: **Cartesian** (x, y) or **polar** (r, θ).

## What real-world situation does it describe?

Cartesian coordinates answer "how far over, how far up" (like city blocks: 3 east, 4 north). Polar coordinates answer "how far away, in what direction" (like radar: 5 miles out, at a bearing). Both describe the exact same point — pick whichever is more convenient for the problem in front of you.

## Objects / System Involved

A single point (or the tip of a vector) located relative to a fixed origin O and a fixed reference axis (almost always the +x axis).

## Quantities That Change

- Cartesian: x (horizontal position), y (vertical position)
- Polar: r (straight-line distance from the origin), θ (angle from the +x axis, measured counterclockwise)

## Model or Equation

Right triangle trigonometry connects the two systems — see [[../equations/polar-cartesian-conversion]]:

```text
x = r cos θ          y = r sin θ
r = √(x² + y²)        tan θ = y / x
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| x, y | Cartesian (rectangular) coordinates | m (or whatever length unit the problem uses) |
| r | radial distance from the origin | m |
| θ | angle from the +x axis, counterclockwise positive | degrees or radians |
| O | the origin — the fixed reference point | n/a |

## Calculus Connection

None yet. This is pure trigonometry (Appendix B.4, [[../appendix/math-geometry-trig]]). Polar coordinates return with a calculus flavor much later if Chris ever takes a course covering polar-coordinate integrals — out of scope for PHYS 2211.

## Diagram / Visual Model

```
        ^ y
        |
        |  • (x, y)
        | /|
        |/ | y = r sin θ
   -----+--+--------> x
     O  |  x = r cos θ
        |
```

r is the hypotenuse (the straight line from O to the point). θ is measured from the +x axis, going counterclockwise, to that line.

## Problem Types That Use This

[[../problem-types/polar-cartesian-conversion]] — and this is the same triangle Chris already uses for [[vector-components]]: a vector's magnitude/angle pair (A, θ) IS a polar-coordinate pair, and its (Ax, Ay) components ARE Cartesian coordinates. Coordinate systems and vector components are the same math applied to two different objects (a point vs. an arrow).

## Common Beginner Mistake

Using tan⁻¹(y/x) without checking the quadrant. A calculator's tan⁻¹ only returns angles between −90° and +90°, but a point can be anywhere in 360°. If x is negative, the true angle is 180° away from what the calculator shows — always sketch the point first and reason about which quadrant it's in (same trap as vector direction — see [[../common-errors/stage-3-vectors]]).

## Practice Next

[[../drills/polar-cartesian-conversion-drill]]

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Section 3.1 (Coordinate Systems), `raw/textbook/Physics book-0001-0100.pdf`.
