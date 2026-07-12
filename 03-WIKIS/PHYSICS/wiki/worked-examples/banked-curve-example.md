---
type: worked-example
status: draft
---

# Banked Curve — Finding the Ideal Banking Angle (Worked Example)

## Problem Statement

A NASCAR oval track has turns with radius r = 300 m. Engineers want cars to navigate the turns at v = 45 m/s (≈ 162 km/h) without requiring any friction. At what angle θ should the track be banked?

## Problem Type

[[../problem-types/horizontal-circular-motion]] — banked curve, no friction variant.

## Given

- Radius: r = 300 m
- Design speed: v = 45 m/s
- No friction (the banking alone must provide the centripetal force)
- g = 9.80 m/s²

## Unknown

Banking angle θ.

## Diagram

```
         n (normal force, perpendicular to banked surface)
         /
        / ← angle θ from vertical
       /
      [car]
      /////banked surface/////

Resolve n into components:
  Vertical: n cos θ = mg         (no vertical acceleration)
  Horizontal (inward): n sin θ = mv²/r   (centripetal direction)
```

## Model / Equation Choice

Newton's second law applied in two directions:
- Vertical: ΣF_y = 0 (no vertical acceleration)
- Horizontal inward: ΣF_x = mv²/r (centripetal acceleration)

## Solution Steps

**Step 1:** Write the vertical equation.

```
n cos θ = mg      ... (1)
```

**Step 2:** Write the horizontal (centripetal) equation.

```
n sin θ = mv²/r   ... (2)
```

**Step 3:** Divide equation (2) by equation (1) to eliminate n and m.

```
(n sin θ)/(n cos θ) = (mv²/r)/(mg)
tan θ = v²/(rg)
```

**Step 4:** Substitute numbers.

```
tan θ = (45)²/(300 × 9.80)
tan θ = 2025/2940
tan θ = 0.6888
θ = tan⁻¹(0.6888) = 34.5°
```

## Units Check

v²/(rg) = (m/s)² / (m · m/s²) = m²/s² / (m²/s²) = dimensionless ✓ (tangent is dimensionless)

## Final Answer

θ = 34.5° — the track should be banked at about 35°. This is steeper than a typical highway (usually ≤ 10°) because NASCAR speeds are much higher.

## Explain-Back Prompt

Explain why the mass cancels. What does that mean physically? (A heavier car and a lighter car need the same banking angle for the same speed — because both the centripetal force requirement and the weight scale with m.)

Why does higher speed require a steeper bank? (More centripetal force is needed. With no friction, only the horizontal component of the normal force can provide it. A steeper angle tilts more of the normal force horizontally.)

## Common Trap

**Forgetting to divide equations to eliminate n.** Students sometimes try to solve for n first and then substitute. Dividing directly is faster and cleaner because it eliminates both n and m simultaneously.

**Using the banking angle as the angle between the surface and the horizontal, vs. the angle from the vertical.** In this problem, θ is measured from the vertical (perpendicular to the flat ground). Check your diagram carefully.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 6.2, Example 6.4.
