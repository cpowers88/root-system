---
type: equation
timeline: reference
status: draft
---

# Projectile Motion Equations

## Equations

**Initial velocity decomposition:**
```
v₀ₓ = v₀ cos θ₀
v₀ᵧ = v₀ sin θ₀
```

**Horizontal motion (ax = 0):**
```
x = x₀ + v₀ₓ t
vₓ = v₀ₓ          (constant — no horizontal force)
```

**Vertical motion (ay = -g = -9.80 m/s²):**
```
y = y₀ + v₀ᵧ t - ½g t²
vᵧ = v₀ᵧ - g t
vᵧ² = v₀ᵧ² - 2g(y - y₀)
```

**At maximum height:**
```
vᵧ = 0   →   t_peak = v₀ᵧ / g = (v₀ sin θ₀) / g
h_max = v₀ᵧ² / (2g) = (v₀ sin θ₀)² / (2g)
```

**Range and total flight time (same launch and landing height, y₀ = y_f = 0):**
```
t_flight = 2v₀ᵧ / g = 2v₀ sin θ₀ / g
R = v₀² sin(2θ₀) / g       [maximum when θ₀ = 45°]
```

## Meaning in Plain English

The x-equations are just constant-velocity motion (Stage 2 equations with a = 0). The y-equations are exactly free fall from Stage 2 applied to the vertical direction. Both share the same variable t.

The range formula R = v₀² sin 2θ / g is a compact result but only works when launch and landing heights are equal.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| v₀ | initial speed | m/s |
| θ₀ | launch angle above horizontal | degrees or rad |
| v₀ₓ, v₀ᵧ | initial velocity components | m/s |
| vₓ, vᵧ | velocity components at time t | m/s |
| x, y | position at time t | m |
| g | free-fall acceleration (use 9.80 m/s²) | m/s² |
| t | time elapsed | s |
| R | horizontal range | m |
| h_max | maximum height reached | m |

## Units Check

- x = v₀ₓ t → (m/s)(s) = m ✓
- y = v₀ᵧ t - ½g t² → (m/s)(s) - (m/s²)(s²) = m - m = m ✓
- R = v₀² sin(2θ₀)/g → (m/s)²/(m/s²) = m ✓

## When to Use It

Any problem where an object is launched into the air with gravity as the only force (no air resistance, no thrust), and you are asked about position, velocity, height, or time of flight.

## When Not to Use It

- When launch height ≠ landing height and you try to use the range formula — it will give the wrong answer. Use the full y(t) equation and solve the resulting quadratic instead.
- When air resistance is significant (stated in the problem).
- For objects on surfaces (use Newton's laws, Stage 5).

## Required Assumptions

- No air resistance.
- g is constant (valid near Earth's surface).
- Object is a particle (no spin, no size effects).

## Calculus Origin

The equations come from integrating ay = -g twice:
```
vᵧ = ∫(-g)dt = -gt + v₀ᵧ
y = ∫vᵧ dt = -½gt² + v₀ᵧ t + y₀
```
The x-equations come from integrating aₓ = 0:
```
vₓ = v₀ₓ (constant)
x = v₀ₓ t + x₀
```

## Example Problem Type

A ball is kicked from the ground at 25 m/s at 40° above horizontal. Find: (a) max height, (b) time of flight, (c) range.

```
v₀ₓ = 25 cos 40° = 19.2 m/s
v₀ᵧ = 25 sin 40° = 16.1 m/s

t_peak = 16.1/9.80 = 1.64 s
h_max  = 16.1²/(2×9.80) = 13.2 m

t_flight = 2(1.64) = 3.28 s
R = 19.2 × 3.28 = 63.0 m
[Check: R = 25² sin(80°)/9.80 = 63.0 m ✓]
```

## Common Mistake

Using the range formula when the launch and landing heights are different (e.g., cliff problem). Always check whether the start and end heights are equal before applying R = v₀² sin 2θ / g.

Also: using g = 9.80 m/s² as a negative value in formulas where the minus sign is already built in (e.g., vᵧ = v₀ᵧ - gt). If you plug in g = -9.80, you get the wrong sign.

## Sources

- Serway & Jewett, 10th ed., Ch. 4.3, Eqs. 4.9–4.15, pp. 89–94.
