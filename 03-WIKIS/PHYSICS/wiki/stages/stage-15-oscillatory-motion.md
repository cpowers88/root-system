---
type: stage
timeline: reference
status: draft
---

# Unit/Stage 15 — Oscillatory Motion / Simple Harmonic Motion (Ch 15)

## Goal

Recognize and solve simple harmonic motion problems using the spring-mass and pendulum models; understand the energy of an oscillator.

## Syllabus Alignment

Ch 15, lectures following Stage 14 (approximate: Nov / early Dec 2026). The syllabus mentions "simple harmonic motion, oscillations."

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 15, sections 15.1–15.5.

## Prerequisite Physics

Stage 5 (Hooke's Law as a force, F = −kx), Stage 7–8 (potential energy of a spring U = ½kx²; energy conservation in oscillating systems).

## Prerequisite Math

Sinusoidal functions (sin, cos), second derivative of sin/cos, angular frequency ω = 2πf = 2π/T.

## Core Concepts

- [[../concepts/simple-harmonic-motion]]
- [[../concepts/shm-energy]]
- [[../concepts/pendulum]]

## Required Vocabulary

Simple harmonic motion, amplitude, angular frequency, period, frequency, phase constant, spring-mass system, restoring force, simple pendulum, physical pendulum, damped oscillation. See [[../flashcards/stage-15-oscillatory-motion]].

## Equations

- [[../equations/shm-position]] — x(t) = A cos(ωt + φ)
- [[../equations/shm-velocity]] — v(t) = −Aω sin(ωt + φ)
- [[../equations/shm-acceleration]] — a(t) = −Aω² cos(ωt + φ) = −ω²x
- [[../equations/shm-period-spring]] — T = 2π√(m/k), ω = √(k/m)
- [[../equations/shm-period-pendulum]] — T = 2π√(L/g) (simple pendulum, small angle)
- [[../equations/shm-energy]] — E = ½mv² + ½kx² = ½kA² = constant

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| x | displacement from equilibrium | m |
| A | amplitude (maximum displacement) | m |
| ω | angular frequency | rad/s |
| f | frequency (cycles per second) | Hz |
| T | period (time for one full cycle) | s |
| φ | phase constant (initial phase angle) | rad |
| k | spring constant | N/m |
| m | mass on spring | kg |
| L | pendulum length | m |
| E | total mechanical energy of oscillator | J |

## Diagrams / Visual Models

**SHM position graph:**
```
x(t)
 A |      ****
   |   *       *
 0 |*               *  t
   |               *
-A |           ****
     |<-- T -->|
```

**Energy bar chart:**
At x = +A: all PE (½kA²), zero KE.
At x = 0 (equilibrium): all KE (½mv_max²), zero PE.
At any x: KE + PE = ½kA² (constant total energy).

**The restoring force arrow always points BACK toward equilibrium** — this is what makes it SHM.

## Calculus Connections

Key calculus link in Stage 15:

The equation of motion for a spring-mass system is Newton's 2nd law: F = ma → −kx = m(d²x/dt²), giving:

```
d²x/dt² = −(k/m)x = −ω²x
```

This is a **differential equation** whose solution is x(t) = A cos(ωt + φ). The pattern to recognize: whenever acceleration is proportional to displacement and opposite in sign, the motion is SHM. See [[../calculus-links/shm-differential-equation]].

## Problem Types

- [[../problem-types/shm-spring-mass]]
- [[../problem-types/shm-energy]]
- [[../problem-types/pendulum-period]]

## Worked Examples

- [[../worked-examples/spring-mass-shm-example]]

## Drills

- [[../drills/shm-equations-drill]]
- [[../drills/shm-energy-drill]]

## Common Errors

See [[../common-errors/stage-15-oscillatory-motion]].

## Mastery Checklist

- [ ] Write x(t), v(t), and a(t) for SHM with a given amplitude, angular frequency, and phase constant
- [ ] Calculate ω, f, and T from spring constant k and mass m
- [ ] Identify the phase constant φ from initial conditions (x₀ and v₀ at t = 0)
- [ ] Explain why a(t) = −ω²x(t) is the defining condition of SHM
- [ ] Calculate total energy E = ½kA² and find speed or position at any point
- [ ] Derive the pendulum period T = 2π√(L/g) and identify its small-angle limitation
- [ ] State what changes (and what doesn't) when amplitude is doubled in SHM

## Do Not Move On Until

Chris can write x(t) for a spring-mass system from initial conditions, calculate its period and total energy, find speed at any position using energy conservation, and explain why the period of a simple pendulum does not depend on amplitude (for small angles).

## Parked for Later

Damped oscillations (b-drag term in the equation of motion) and forced oscillations/resonance are covered in section 15.6–15.7 and may appear on the final exam. Park until basic SHM is mastered. Coupled oscillators are beyond PHYS 2211 scope.
