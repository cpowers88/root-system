---
type: problem-type
timeline: reference
status: draft
---

# Polar ↔ Cartesian Coordinate Conversion

## How to Recognize This Problem Type

The problem gives a point or vector as either "(x, y)" or as "r at angle θ" and asks for the other description. Watch for phrases like "find the polar coordinates," "express in Cartesian form," or "find the distance and direction."

## Given Information Usually Present

Either an (x, y) pair, or an (r, θ) pair — never both.

## Unknown Usually Requested

The missing pair: (r, θ) if given (x, y), or (x, y) if given (r, θ).

## Diagram to Draw

A right triangle with the origin at one vertex, the point at the opposite vertex, r as the hypotenuse, θ measured from the +x axis, and x/y as the two legs. See [[../concepts/coordinate-systems]].

## Equations Commonly Used

[[../equations/polar-cartesian-conversion]]

## Step-by-Step Solving Pattern

1. Sketch the point on x-y axes — even a rough sketch shows which quadrant it's in.
2. Decide which direction you're converting (polar → Cartesian, or Cartesian → polar).
3. Polar → Cartesian: plug r and θ into x = r cos θ, y = r sin θ.
4. Cartesian → polar: compute r = √(x² + y²) first (always positive), then θ = tan⁻¹(y/x).
5. Check the quadrant from your sketch. If the calculator's θ doesn't match the sketch's quadrant, add 180°.

## Unit Checks

r carries the same length unit as x and y. θ has no unit but must be labeled degrees or radians — state which.

## Common Traps

- Forgetting to check the quadrant after tan⁻¹ (the single most common error in this problem type).
- Mixing degree mode and radian mode on the calculator.
- Reporting r as negative — r is always defined as positive (it's a distance).

## Practice Drills

[[../drills/polar-cartesian-conversion-drill]]

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Section 3.1, Example 3.1.
