---
type: problem-type
timeline: reference
status: draft
---

# Projectile — Horizontal Launch

## How to Recognize This Problem Type

The object is launched horizontally (no upward angle — it leaves a cliff, table, or moving vehicle moving purely sideways). This means v₀ᵧ = 0 at launch.

Key phrases: "dropped from a moving plane," "rolls off a table," "fired horizontally from a height," "launched horizontally."

## Given Information Usually Present

- Initial height h (or vertical distance to fall)
- Initial horizontal speed v₀ₓ (or equivalently v₀, since θ₀ = 0°)
- g = 9.80 m/s²

## Unknown Usually Requested

- Time of flight (how long until it hits the ground)
- Horizontal range (how far horizontally from the launch point)
- Velocity at impact (magnitude and direction)

## Diagram to Draw

```
   v₀ₓ →
   +---------+
   |         |
 h |         | (falls freely while moving horizontally)
   |         |
   |         |
   +---------+--------→
   cliff     R (range)

x-axis: rightward = positive
y-axis: upward = positive (so y₀ = h, y_f = 0, and ay = -g)
```

## Equations Commonly Used

With y₀ = h, y_f = 0, v₀ᵧ = 0:
```
Vertical:    0 = h - ½g t²     →     t = √(2h/g)
Horizontal:  R = v₀ₓ t          →     R = v₀ₓ √(2h/g)

Landing velocity components:
  vₓ = v₀ₓ          (unchanged)
  vᵧ = -gt          (downward, so negative)

Landing speed:  |v| = √(vₓ² + vᵧ²)
Landing angle:  θ = tan⁻¹(|vᵧ|/vₓ)   (below horizontal)
```

## Step-by-Step Solving Pattern

1. Draw diagram; label h, v₀ₓ, and the coordinate system (up positive, rightward positive).
2. Use vertical equation to find time of flight: t = √(2h/g).
3. Use horizontal equation to find range: R = v₀ₓ × t.
4. Find landing velocity components if asked: vₓ = v₀ₓ, vᵧ = -g × t.
5. Compute speed and angle if asked: |v| = √(vₓ² + vᵧ²), θ below horizontal.
6. Check units.

## Unit Checks

- t = √(2h/g) → √(m / (m/s²)) = √(s²) = s ✓
- R = v₀ₓ × t → (m/s)(s) = m ✓
- |v| = √((m/s)² + (m/s)²) = m/s ✓

## Common Traps

- Forgetting that v₀ᵧ = 0 (the horizontal launch means NO initial upward velocity).
- Using the range formula R = v₀² sin 2θ / g — this formula requires launch and landing at the same height; cliff problems violate that condition.
- Taking g as negative in t = √(2h/g) — the formula uses the magnitude (g = +9.80); sign convention is handled in the y equation.
- Not accounting for both vₓ and vᵧ when asked for the total landing velocity.

## Practice Drills

- [[../drills/projectile-motion-drill]]

## Sources

- Serway & Jewett, 10th ed., Ch. 4.3, Examples 4.2–4.3, pp. 90–94.
