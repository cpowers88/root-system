---
type: calculus-link
status: draft
---

# Calculus Link — SHM as a Differential Equation (Stage 15)

## Physics Idea

Simple Harmonic Motion (SHM) occurs when a restoring force is proportional to displacement from equilibrium: F = −kx. By Newton's Second Law, this gives an equation connecting acceleration to position.

## Calculus Idea

A **differential equation** relates a function to its own derivative(s). The SHM equation is a second-order differential equation — it connects position x to its own second derivative (acceleration).

## Plain-English Connection

Start from F = ma with F = −kx (Hooke's Law):

$$ma = -kx \quad \Rightarrow \quad m\frac{d^2x}{dt^2} = -kx \quad \Rightarrow \quad \frac{d^2x}{dt^2} = -\frac{k}{m}x = -\omega^2 x$$

This says: "the second derivative of x equals −ω² times x itself."

The solution to this equation is a sinusoidal function:

$$x(t) = A\cos(\omega t + \phi)$$

Why? Because the second derivative of cosine gives −cosine:

$$\frac{d}{dt}[A\cos(\omega t + \phi)] = -A\omega\sin(\omega t + \phi) = v(t)$$
$$\frac{d}{dt}[-A\omega\sin(\omega t + \phi)] = -A\omega^2\cos(\omega t + \phi) = -\omega^2 x(t) \checkmark$$

It checks out — x(t) = A cos(ωt + φ) satisfies the differential equation.

## Symbol Meanings

| Symbol | Meaning |
|---|---|
| d²x/dt² | second derivative of position — the acceleration |
| ω | angular frequency (rad/s) = √(k/m) for spring-mass |
| A | amplitude — maximum displacement from equilibrium |
| φ | phase constant — determines position at t = 0 |
| x(t) | position as a function of time |

## Small Example — Spring Mass

Spring constant k = 400 N/m, mass m = 1.0 kg.

ω = √(k/m) = √400 = 20 rad/s.

If released from x = 0.05 m at rest: A = 0.05 m, φ = 0.

x(t) = 0.05 cos(20t) meters
v(t) = −0.05 × 20 sin(20t) = −1.0 sin(20t) m/s
a(t) = −0.05 × 400 cos(20t) = −20 cos(20t) m/s²

Check: a(0) = −20 m/s²; F = ma = 1.0 × (−20) = −20 N = −kx = −400 × 0.05 = −20 N ✓

## Course Location

Stage 15 (Ch 15 — Oscillatory Motion). You are not expected to solve the differential equation from scratch — you are expected to recognize that SHM arises from any F = −kx situation and that the solution form is always sinusoidal.

## Common Mistake

Thinking that because the solution is sinusoidal you can just guess any sine/cosine and be done. The phase constant φ and amplitude A must be set by the initial conditions (x at t = 0, v at t = 0). Not setting φ correctly is the most frequent Stage 15 algebra error.

## Related Pages

[[../stages/stage-15-oscillatory-motion]] — [[../appendix/math-calculus]]
