---
type: worked-example
timeline: reference
status: draft
---

# Worked Example — Cartesian to Polar Conversion

## Physical Situation

A drone's flight-control software logs its position relative to the launch pad as Cartesian coordinates (x, y) = (−4.00 m, 3.00 m). The pilot's display needs to show distance and bearing instead. Find the polar coordinates (r, θ).

## Step 1 — Identify what you know

| Quantity | Value |
|---|---|
| x | −4.00 m |
| y | 3.00 m |
| Unknown | r, θ |

## Step 2 — Diagram

Sketch the point: negative x (left of origin), positive y (above origin) — this puts the point in the **second quadrant**. Expect θ between 90° and 180°.

## Step 3 — Find r

```
r = √(x² + y²) = √((−4.00)² + (3.00)²) = √(16.0 + 9.00) = √25.0 = 5.00 m
```

## Step 4 — Find θ (raw calculator output)

```
tan θ = y / x = 3.00 / (−4.00) = −0.750
θ_calculator = tan⁻¹(−0.750) = −36.9°
```

## Step 5 — Check the quadrant and correct

The sketch says the point is in the second quadrant (90°–180°), but the calculator gave −36.9° (fourth quadrant). Since x is negative, add 180°:

```
θ = −36.9° + 180° = 143.1°
```

## Step 6 — Write the answer

The polar coordinates are **(r, θ) = (5.00 m, 143.1°)**.

## Units Check

r has units of meters — matches x and y. θ is dimensionless (degrees). ✓

## Final Answer

(r, θ) = (5.00 m, 143.1°)

## Explain-Back Prompt

Without looking at your notes: why did the calculator's tan⁻¹ give the wrong quadrant, and how did the sketch catch it?

## Common Trap Avoided

Did NOT report θ = −36.9° (fourth quadrant — wrong side of the origin entirely). The sketch, done before any calculation, made the error obvious immediately.

## Practice Next

[[../drills/polar-cartesian-conversion-drill]]
