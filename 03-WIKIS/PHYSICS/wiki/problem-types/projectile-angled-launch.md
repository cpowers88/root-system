---
type: problem-type
timeline: reference
status: draft
---

# Projectile — Angled Launch

## How to Recognize This Problem Type

An object is launched at an angle θ₀ above the horizontal from ground level (or a known height). Both v₀ₓ and v₀ᵧ are non-zero. Most classic projectile problems are this type.

Key phrases: "launched at an angle of __° above the horizontal," "fired at 30°," "thrown at an angle," "kicked with speed v at angle θ."

## Given Information Usually Present

- Initial speed v₀ and launch angle θ₀ (OR separately stated v₀ₓ and v₀ᵧ)
- Whether launch and landing heights are the same (symmetric) or different
- g = 9.80 m/s²

## Unknown Usually Requested

Choose one or more of:
- Maximum height h_max
- Time of flight t_flight
- Horizontal range R
- Velocity at a specific time or height
- Angle and speed at landing

## Diagram to Draw

```
           peak (vᵧ=0)
          /  \
         /    \
        /      \
       /        \
      / θ₀       \
launch          landing
```

Label: v₀ₓ = v₀ cos θ₀ (right), v₀ᵧ = v₀ sin θ₀ (up).

## Equations Commonly Used

```
v₀ₓ = v₀ cos θ₀
v₀ᵧ = v₀ sin θ₀

x(t) = v₀ₓ t
y(t) = v₀ᵧ t - ½g t²    (taking launch point as origin, y₀ = 0)

vₓ(t) = v₀ₓ
vᵧ(t) = v₀ᵧ - g t

At peak:  vᵧ = 0  →  t_peak = v₀ᵧ / g
h_max = v₀ᵧ² / (2g)

Symmetric launch/landing (y_final = 0):
t_flight = 2t_peak = 2v₀ᵧ / g = 2v₀ sin θ₀ / g
R = v₀ₓ × t_flight = v₀² sin(2θ₀) / g
```

## Step-by-Step Solving Pattern

1. Draw diagram; set launch point as origin (x₀ = 0, y₀ = 0), up positive, right positive.
2. Decompose: v₀ₓ = v₀ cos θ₀, v₀ᵧ = v₀ sin θ₀.
3. Decide which unknown you are solving for first.
4. For max height: set vᵧ = 0, solve for t_peak, then plug into y(t).
5. For range (same height): find t_flight = 2t_peak, then R = v₀ₓ × t_flight.
6. For time at a given y (different heights): use quadratic y = v₀ᵧ t - ½g t², solve for t (quadratic formula if needed — take the positive root).
7. For velocity at a given time: compute vₓ = v₀ₓ and vᵧ = v₀ᵧ - gt.
8. Check all units.

## Unit Checks

- t = v₀ᵧ/g → (m/s)/(m/s²) = s ✓
- h = v₀ᵧ²/(2g) → (m/s)²/(m/s²) = m ✓
- R = v₀² sin 2θ / g → (m/s)²/(m/s²) = m ✓

## Common Traps

- Applying R = v₀² sin 2θ / g when launch and landing heights differ — only valid for symmetric (same-height) flights.
- Forgetting to take the positive root from the quadratic for t when solving y(t) = h.
- Using θ in degrees when a calculator expects radians — always check calculator mode.
- Losing track of sign on vᵧ: above peak vᵧ > 0, below peak vᵧ < 0.
- Forgetting that at peak the object still has horizontal velocity vₓ = v₀ₓ — it is not stopped.

## Practice Drills

- [[../drills/projectile-motion-drill]]

## Sources

- Serway & Jewett, 10th ed., Ch. 4.3, pp. 89–95.
