---
type: equation
status: draft
---

# Equation — Polar ↔ Cartesian Coordinate Conversion

## Equation

```text
x = r cos θ          y = r sin θ            (polar → Cartesian)
r = √(x² + y²)        tan θ = y / x          (Cartesian → polar)
```

## Meaning in Plain English

Two ways to locate the same point. Go one direction with the first pair (you know distance and angle, want horizontal/vertical); go the other direction with the second pair (you know horizontal/vertical, want distance and angle).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| x, y | Cartesian coordinates | m |
| r | radial distance from origin | m |
| θ | angle from +x axis, counterclockwise | degrees or radians |

## Units Check

r has the same unit as x and y (length). θ is dimensionless (an angle), but always track whether it's in degrees or radians before touching a calculator.

## When to Use It

- Converting a position or vector given as (magnitude, angle) into (x, y) components, or back.
- Any problem that states a location as "r meters at θ degrees" or gives you (x, y) and asks for distance/direction.

## When Not to Use It

Don't use this for adding two vectors directly — convert each to Cartesian first, add components, then convert the resultant back to polar if the answer needs to be reported as magnitude/direction. See [[../equations/vector-addition-by-components]].

## Required Assumptions

θ is measured counterclockwise from the +x axis, and the origin is the same for both coordinate descriptions. If a problem defines θ differently (e.g., from the +y axis, or clockwise), the equations must be adjusted — always re-derive from a sketch rather than memorizing blindly.

## Calculus Origin

None — this is trigonometry (right-triangle definitions of sine, cosine, tangent), not calculus.

## Example Problem Type

[[../problem-types/polar-cartesian-conversion]]

## Common Mistake

Using tan⁻¹(y/x) and accepting the calculator's answer without checking the quadrant. The calculator only returns −90° to +90°; if x < 0, add 180° to get the true angle.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Equations 3.1–3.4, Section 3.1. `raw/textbook/Physics book-0001-0100.pdf`.
