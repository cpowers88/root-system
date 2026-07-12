---
type: equation
status: draft
---

# Angular Kinematic Equations

## Equations (for constant angular acceleration α)

```
ω = ω₀ + αt                          (1)
θ = θ₀ + ω₀t + ½αt²                  (2)
ω² = ω₀² + 2α(θ − θ₀)               (3)
θ = θ₀ + ½(ω₀ + ω)t                  (4)
```

Plus the definitions:
```
ω = dθ/dt        (angular velocity — rate of change of angle)
α = dω/dt        (angular acceleration — rate of change of ω)
```

## Meaning in Plain English

These four equations describe how a rotating object's angle, angular speed, and angular acceleration relate during constant-α rotation. They are structurally identical to the four linear kinematic equations — just swap x→θ, v→ω, a→α.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| θ | angular position (current) | rad |
| θ₀ | angular position (initial) | rad |
| ω | angular velocity (current) | rad/s |
| ω₀ | angular velocity (initial) | rad/s |
| α | angular acceleration (constant) | rad/s² |
| t | time elapsed | s |

## Units Check

Eq. 1: [ω] = rad/s; [αt] = (rad/s²)(s) = rad/s ✓
Eq. 2: [θ] = rad; [ω₀t] = (rad/s)(s) = rad; [½αt²] = (rad/s²)(s²) = rad ✓
Eq. 3: [ω²] = rad²/s²; [2αΔθ] = (rad/s²)(rad) = rad²/s² ✓

## Conversion: Linear ↔ Angular for a point at radius r

| Linear | Angular | Relation |
|---|---|---|
| s (arc length, m) | θ (angle, rad) | s = rθ |
| v_t (tangential speed, m/s) | ω (rad/s) | v_t = rω |
| a_t (tangential accel, m/s²) | α (rad/s²) | a_t = rα |
| a_c (centripetal accel, m/s²) | ω (rad/s) | a_c = rω² = v_t²/r |

## When to Use It

Any situation where a rigid object rotates about a fixed axis with constant angular acceleration. Example: a motor spinning up from rest, a wheel decelerating uniformly, a disk rotating at constant ω (α = 0, simplest case).

## When Not to Use It

When α is not constant (e.g., torque varies with angle or time). Then you need to integrate α(t) directly.

## Required Assumptions

- Rotation about a fixed axis (axis doesn't wobble or translate)
- Constant angular acceleration α throughout the time interval

## Calculus Origin

Exactly parallel to linear kinematics derivation:
```
α = dω/dt  →  ∫dω = ∫α dt  →  ω = ω₀ + αt          (Eq. 1)
ω = dθ/dt  →  ∫dθ = ∫ω dt  →  θ = θ₀ + ω₀t + ½αt²   (Eq. 2)
Eliminating t between Eq. 1 and Eq. 2  →  ω² = ω₀² + 2αΔθ  (Eq. 3)
```

## Choosing the Right Equation

| You know | You want | Use |
|---|---|---|
| ω₀, α, t | ω | Eq. 1 |
| ω₀, α, t | θ | Eq. 2 |
| ω₀, ω, α | θ (no t) | Eq. 3 |
| ω₀, ω, t | θ (no α) | Eq. 4 |

## Common Mistake

Using degrees instead of radians. Every angular kinematic equation assumes radians. Convert first: θ(rad) = θ(°) × π/180.

## Sources

Serway & Jewett, 10th ed., Eqs. 10.6–10.9, Table 10.1.
