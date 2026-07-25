---
type: map
timeline: reference
reference_priority: core
tags: [physics, math]
---

# Calculus Map

## Purpose

Explain calculus only as it appears in physics.

For the stage-gated practice sequence, physical anchors, and current three-rep
bridge, use [[math-readiness-path]]. This map answers *where calculus appears*;
that path answers *what to practice next*.

## Stage 1 — Physics and Measurement (Ch 1)

No calculus required yet. Chapter 1 is the only stage in the course where calculus does not appear — a clean on-ramp before it shows up in Stage 2.

## Where calculus first appears: Stage 2 (Ch 2 — Motion in One Dimension)

| Physics idea | Calculus idea | Plain-English connection | Symbols | Unit/stage | Common mistake |
|---|---|---|---|---|---|
| Position to velocity | derivative | velocity is how position changes with time — the slope of the x-t graph at a point | `v = dx/dt` | Stage 2 | Confusing average velocity (slope between two points) with instantaneous velocity (slope at one point) |
| Velocity to acceleration | derivative | acceleration is how velocity changes with time — the slope of the v-t graph | `a = dv/dt` | Stage 2 | Assuming zero velocity means zero acceleration (true only at a turning point) |
| Velocity to displacement | integral | displacement is accumulated velocity over time — area under the v-t graph | `Δx = ∫v dt` | Stage 2 | Confusing area under v-t graph with the value of v itself |
| Constant acceleration kinematics | integration of a constant | integrating a(t) = constant once gives v(t); integrating again gives x(t) | `v=v₀+at`, `x=x₀+v₀t+½at²` | Stage 2 | Forgetting the constant of integration (v₀, x₀) |

## Calculus Roadmap (course-wide, all 18 stages)

```text
Stage 1  (Ch 1)  -> none — calculus-free on-ramp
Stage 2  (Ch 2)  -> derivatives: v = dx/dt, a = dv/dt = d²x/dt²
                    integrals: x = ∫v dt, v = ∫a dt (area under v-t and a-t graphs)
Stage 3  (Ch 3)  -> none new (trig, not calculus)
Stage 4  (Ch 4)  -> derivatives/integrals applied independently to x(t) and y(t);
                    a_t = dv/dt for nonuniform circular motion first appears here (Sec 4.5)
Stage 5  (Ch 5)  -> none new (algebra on F = ma)
Stage 6  (Ch 6)  -> a_t = dv/dt reused from Stage 4/2, applied to circular paths
                    with changing speed
Stage 7  (Ch 7)  -> integral for work by varying force: W = ∫F dx
                    dot product W = F·d cos θ (vector calculus, conceptual)
Stage 8  (Ch 8)  -> power as a rate of energy transfer: P = dE/dt = dW/dt
                    (energy conservation itself is algebra on the Stage 7 result)
Stage 9  (Ch 9)  -> impulse as time integral of force: J = ∫F dt
Stage 10 (Ch 10) -> rotational derivatives: α = dω/dt, ω = dθ/dt
                    integration to find moment of inertia: I = ∫r² dm
                    rotational work: W = ∫τ dθ
Stage 11 (Ch 11) -> torque as derivative of angular momentum: τ = dL/dt
                    (rotational analogue of F = dp/dt from Stage 9)
Stage 12 (Ch 12) -> none new (equilibrium is algebra on forces and torques)
Stage 13 (Ch 13) -> none new (algebra on inverse-square law; energy from Stage 7–8)
Stage 14 (Ch 14) -> continuity equation from conservation of mass (dV/dt = Av)
                    Bernoulli's equation from work-energy theorem applied to fluid element
Stage 15 (Ch 15) -> differential equation: d²x/dt² = −ω²x (solution is sinusoidal)
                    derivatives of sin/cos to find v(t) and a(t) for SHM
Stage 16 (Ch 16) -> wave equation as partial differential: ∂²y/∂x² = (1/v²) ∂²y/∂t²
                    (conceptual — not solving PDEs, only reading the structure)
Stage 17 (Ch 17) -> none new (superposition is algebraic combination of wave functions)
Stage 18 (Ch 38) -> none new (Lorentz algebra, but gives up Galilean intuition)
```

## Later Stages

Full calculus-link pages for each stage are generated when that stage packet is built, per the one-stage-at-a-time rule in [[../OPERATIONS.md]]. The roadmap above is the preview — each row becomes a detailed page in `wiki/calculus-links/` as Chris reaches it.

## Calculus-Link Pages Built So Far

Each page below includes a full derivation, a small worked example, a
multi-problem practice set, and a real-world/engineering use case.

| Page | Stage(s) | Covers |
|---|---|---|
| [[calculus-links/kinematics-derivatives]] | 2 | v = dx/dt, a = dv/dt, integration of constant a |
| [[calculus-links/2d-kinematics-components]] | 4 | vector differentiation applied to projectile motion |
| [[calculus-links/tangential-radial-acceleration-derivative]] | 4, 6 | a_t = dv/dt on a curved path, combined with a_r = v²/r |
| [[calculus-links/stage-7-work-integral]] | 7 | W = ∫F dx, F = −dU/dx |
| [[calculus-links/power-derivative]] | 8 | P = dE/dt, ΔE = ∫P dt |
| [[calculus-links/impulse-integral]] | 9 | J = ∫F dt = Δp |
| [[calculus-links/rotational-kinematics-derivatives]] | 10 | ω = dθ/dt, α = dω/dt, I = ∫r² dm, W = ∫τ dθ |
| [[calculus-links/angular-momentum-derivative]] | 11 | τ = dL/dt |
| [[calculus-links/shm-differential-equation]] | 15 | d²x/dt² = −ω²x |
