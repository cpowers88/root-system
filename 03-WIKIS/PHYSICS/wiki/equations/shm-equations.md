---
type: equation
status: draft
---

# SHM Kinematic Equations — x(t), v(t), a(t)

## Equations

```text
x(t) = A cos(ωt + φ)         [position]
v(t) = −Aω sin(ωt + φ)       [velocity]
a(t) = −Aω² cos(ωt + φ)      [acceleration]
```

Note: a(t) = −ω²x(t) — acceleration is always proportional to position and opposite in sign.

## Meaning in Plain English

**x(t):** The object's displacement from equilibrium at time t oscillates smoothly between +A and −A like a cosine wave.

**v(t):** The velocity is the derivative of position — it oscillates 90° out of phase with x. When x is at a maximum (+A), v = 0 (momentarily stopped). When x = 0, |v| is maximum.

**a(t):** The acceleration is the derivative of velocity — it oscillates 180° out of phase with x. When displacement is most positive, acceleration is most negative (the restoring force pulls hardest back toward zero).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| x | displacement from equilibrium | m |
| A | amplitude (maximum displacement) | m |
| ω | angular frequency | rad/s |
| φ | phase constant (set by initial conditions) | rad |
| t | time | s |
| v | velocity | m/s |
| a | acceleration | m/s² |

## Maximum Values

| Quantity | Maximum magnitude | Where it occurs |
|---|---|---|
| Position | A | at turning points x = ±A |
| Velocity | Aω | at equilibrium x = 0 |
| Acceleration | Aω² | at turning points x = ±A |

## Units Check

- [Aω] = m · (rad/s) = m/s ✓ (velocity)
- [Aω²] = m · (rad/s)² = m/s² ✓ (acceleration)

## When to Use These Equations

Use x(t) when asked for position at a specific time. Use v(t) when asked for velocity at a specific time. Use a(t) when asked for acceleration at a specific time. To find speed at a given position (no time needed), use energy: v = ω√(A² − x²) instead.

## When Not to Use These Equations

Do not use these equations if the system is NOT in SHM (for example, a pendulum at large angle, or a spring with significant damping). These equations assume ideal, undamped SHM.

## Required Assumptions

Undamped simple harmonic motion. Force law: F = −kx (linear restoring force). No friction.

## Calculus Origin

x(t) is the solution to the differential equation d²x/dt² = −ω²x. Differentiating x(t) once gives v(t); differentiating v(t) once gives a(t). See [[../calculus-links/shm-differential-equation]].

## Finding the Phase Constant φ

At t = 0:
- x₀ = A cos φ
- v₀ = −Aω sin φ

Divide: v₀/x₀ = −ω tan φ → φ = arctan(−v₀/ωx₀)

Always check the signs of both x₀ and v₀ to select the correct quadrant for φ.

## Common Mistake

Using sin instead of cos (or vice versa) without checking initial conditions. The choice of cosine vs. sine form is a matter of convention — what matters is that x₀ and v₀ are both satisfied at t = 0. Also, forgetting the negative sign in v(t) = −Aω sin(ωt + φ).

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 15.2, Equations 15.6, 15.15, 15.16.
