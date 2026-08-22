---
type: concept
timeline: reference
status: draft
---

# Projectile Motion

## What is the physical idea?

When an object is launched into the air and the only force acting on it is gravity (no air resistance), its horizontal and vertical motions are completely independent. The horizontal motion is constant velocity; the vertical motion is free fall. These two independent motions share the same clock — the time elapsed is the same for both.

## What real-world situation does it describe?

A ball thrown at an angle, a rock dropped from a moving car, a bullet fired horizontally, a soccer ball kicked across a field, water from a hose. Any object that is launched and then moves freely under gravity follows a parabolic path.

## Objects / System Involved

A single object (the projectile), treated as a particle. The Earth exerts a constant downward force (gravity). No rope, no surface, no air — just gravity.

## Quantities That Change

- Vertical velocity vᵧ changes continuously (decreases going up, increases going down).
- Vertical position y changes (rises, peaks, falls).
- Horizontal velocity vₓ does NOT change.
- Horizontal position x changes at a constant rate.
- Total speed |v| = √(vₓ² + vᵧ²) changes (except at special instants).

## Model or Equation

**Decompose the initial velocity first:**
```
v₀ₓ = v₀ cos θ₀    (horizontal component)
v₀ᵧ = v₀ sin θ₀    (vertical component)
```

**Horizontal (ax = 0, constant velocity):**
```
x = x₀ + v₀ₓ t
vₓ = v₀ₓ  (unchanged throughout flight)
```

**Vertical (ay = -g, free fall):**
```
y = y₀ + v₀ᵧ t - ½g t²
vᵧ = v₀ᵧ - g t
vᵧ² = v₀ᵧ² - 2g(y - y₀)
```

**At maximum height:**
```
vᵧ = 0   →   t_peak = v₀ᵧ / g
```

**Range (same launch and landing height):**
```
R = v₀² sin(2θ₀) / g
Maximum range when θ₀ = 45°
```

**Maximum height:**
```
h = v₀ᵧ² / (2g) = (v₀ sin θ₀)² / (2g)
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| v₀ | initial speed | m/s |
| θ₀ | launch angle | degrees (convert to rad for calculus) |
| v₀ₓ, v₀ᵧ | initial velocity components | m/s |
| vₓ, vᵧ | velocity components at time t | m/s |
| x, y | position at time t | m |
| g | free-fall acceleration magnitude | 9.80 m/s² |
| t | time | s |
| R | range | m |
| h | maximum height | m |

## Calculus Connection

The kinematic equations are derived by integrating ay = -g:
```
vᵧ(t) = ∫(-g)dt = -gt + v₀ᵧ
y(t) = ∫vᵧ dt = -½gt² + v₀ᵧt + y₀
```
The parabolic shape y(x) comes from eliminating t between x(t) and y(t).

## Diagram / Visual Model

```
vᵧ↑  vₓ→          vₓ→           vₓ→
     /              |peak           \
    /               | (vᵧ=0)        \
   /                                 \
  O θ₀                               landing
  |<-------------- R --------------->|

At every point: vₓ stays the same; only vᵧ changes.
The trajectory is a parabola.
```

At launch: v⃗ points at angle θ₀.
At peak: v⃗ is purely horizontal (vₓ only).
At landing: same speed as launch (same height), but angle is -θ₀ (mirror image below horizontal).

## Problem Types That Use This

- [[../problem-types/projectile-horizontal-launch]]
- [[../problem-types/projectile-angled-launch]]

## Common Beginner Mistake

Thinking that horizontal velocity decreases during flight "because the object slows down." It doesn't — there is no horizontal force. Only the vertical component changes. The projectile never decelerates horizontally (in the no-air-resistance model).

Also: forgetting that at the peak, vᵧ = 0 but vₓ ≠ 0. The object is still moving — it is not momentarily at rest, it is momentarily moving purely horizontally.

## Practice Next

Work the cliff example ([[../worked-examples/projectile-cliff-example]]), then the projectile motion drill ([[../drills/projectile-motion-drill]]).

## Sources

- Serway & Jewett, 10th ed., Ch. 4.2–4.3, pp. 83–95.
