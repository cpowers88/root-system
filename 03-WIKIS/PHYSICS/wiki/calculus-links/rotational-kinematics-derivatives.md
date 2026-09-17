---
type: calculus-link
timeline: reference
status: draft
---

# Calculus Link — Rotational Kinematics and Derivatives (Stage 10)

## Physics Idea

Rotation has exact analogues of linear kinematics. Angular position θ, angular velocity ω, and angular acceleration α are related by derivatives and integrals — the same way x, v, and a are related in linear motion.

Additionally, moment of inertia I depends on how mass is distributed — you add up (integrate) contributions from every mass element in the body.

## Calculus Ideas

1. **Derivatives** relate angular quantities the same way they do for linear ones.
2. **Integration** over a mass distribution gives I = ∫r² dm.
3. **Rotational work** is an integral of torque over angle: W = ∫τ dθ.

## Plain-English Connection

| Rotational physics statement | Calculus statement | Linear analogue |
|---|---|---|
| Angular velocity is rate of change of angle | ω = dθ/dt | v = dx/dt |
| Angular acceleration is rate of change of ω | α = dω/dt = d²θ/dt² | a = dv/dt |
| Moment of inertia sums r² over all mass | I = ∫r² dm | (no linear analogue) |
| Rotational work is accumulated torque × angle | W = ∫τ dθ | W = ∫F dx |

## Symbol Meanings

| Symbol | Meaning |
|---|---|
| θ | angular position (radians) |
| ω | angular velocity (rad/s) |
| α | angular acceleration (rad/s²) |
| dθ/dt | derivative of angle — instantaneous angular velocity |
| dω/dt | derivative of ω — instantaneous angular acceleration |
| I = ∫r² dm | integral of r² over the mass distribution — moment of inertia |
| τ | torque (N·m) |
| W = ∫τ dθ | rotational work |

## Small Example — Moment of Inertia of a Uniform Rod

For a thin rod of mass M and length L, rotating about one end:

$$I = \int_0^L r^2 \frac{M}{L}\, dr = \frac{M}{L} \cdot \frac{L^3}{3} = \frac{1}{3}ML^2$$

You don't need to derive these — the textbook provides a table of standard moments of inertia. But understanding that I comes from integrating r² dm helps you see WHY mass far from the axis matters more than mass near the axis.

## Small Example — Constant Angular Acceleration

Just like linear kinematics, integrating α = constant gives:
ω = ω₀ + αt and θ = θ₀ + ω₀t + ½αt²

These are the rotational kinematic equations (direct analogues of v = v₀ + at and x = x₀ + v₀t + ½at²).

## Course Location

Stage 10 (Ch 10 — Rotation of a Rigid Object About a Fixed Axis).

## Common Mistake

Forgetting that the moment of inertia integral gives different results depending on where the axis of rotation is — not just on the shape of the object. The parallel-axis theorem (I = I_cm + Md²) lets you shift the axis without redoing the integral.

## Related Pages

[[../stages/stage-10-rotation]] — [[../calculus-links/kinematics-derivatives]] — [[../appendix/math-calculus]]
