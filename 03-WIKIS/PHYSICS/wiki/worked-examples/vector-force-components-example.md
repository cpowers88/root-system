---
type: worked-example
status: draft
---

# Worked Example — Vector Force Components

## Physical Situation

Two teams are in a tug-of-war on ice, but they aren't pulling on the same rope. Team A pulls on a puck with a force of 50 N at 30° above the horizontal (+x axis). Team B pulls on the same puck with 30 N at 120° from the +x axis. Find the net force on the puck.

## Step 1 — Identify what you know

| Quantity | Value |
|---|---|
| F⃗_A | 50 N, θ = 30° from +x |
| F⃗_B | 30 N, θ = 120° from +x |
| Unknown | R⃗ = F⃗_A + F⃗_B (magnitude and direction) |

## Step 2 — Diagram

Draw the coordinate system. Sketch F⃗_A pointing up and to the right (30° above +x). Sketch F⃗_B pointing up and to the left (120° from +x, which is 60° above the −x axis). Label everything before computing.

## Step 3 — Decompose each force

**Force A:**
```
F_Ax = 50 cos 30° = 50 × 0.866 = 43.3 N
F_Ay = 50 sin 30° = 50 × 0.500 = 25.0 N
```

**Force B:**
```
F_Bx = 30 cos 120° = 30 × (−0.500) = −15.0 N     ← negative x
F_By = 30 sin 120° = 30 × 0.866  = +26.0 N
```

Note: cos 120° is negative because 120° is in the second quadrant (the x-component points left).

## Step 4 — Add components

```
Rx = F_Ax + F_Bx = 43.3 + (−15.0) = 28.3 N
Ry = F_Ay + F_By = 25.0 + 26.0   = 51.0 N
```

## Step 5 — Find magnitude and direction

```
|R⃗| = √(Rx² + Ry²) = √(28.3² + 51.0²) = √(800.9 + 2601.0) = √3401.9 ≈ 58.3 N

θ = tan⁻¹(Ry / Rx) = tan⁻¹(51.0 / 28.3) = tan⁻¹(1.80) ≈ 61°
```

Both Rx and Ry are positive, so the resultant is in the first quadrant — no adjustment needed.

## Step 6 — Write the answer

The net force on the puck is **58.3 N at 61° above the +x axis**.

In unit-vector notation: **R⃗ = 28.3 î + 51.0 ĵ N**.

## Unit Check

Each component has units of N. Magnitude = √(N² + N²) = N. ✓

## Common Traps Avoided

- Did NOT add magnitudes (50 + 30 = 80 N — wrong).
- DID use cos 120° = −0.500 (not +0.500) because the x-component points left.
- DID verify the quadrant of the resultant with the sign of Rx and Ry before reporting θ.

## Practice Next

[[../drills/vector-addition-drill]] — problems 2 and 7 are direct practice of this exact procedure.
