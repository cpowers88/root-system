---
type: stage
status: draft
---

# Stage 16 — Wave Motion (Ch 16)

## Goal

Describe traveling waves mathematically and physically: understand the wave model, read and write wave functions, calculate wave speed, and apply the Doppler effect.

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 16.

## Prerequisite Physics

Stage 15 (oscillatory motion) — oscillation is the source of a wave. Stage 7–8 (energy) — waves carry energy.

## Prerequisite Math

Sinusoidal functions (sin, cos), partial derivatives (conceptual recognition only), logarithms (for decibels).

## Core Concepts

- [[../concepts/wave-model]]
- [[../concepts/sinusoidal-wave]]
- [[../concepts/wave-speed]]
- [[../concepts/doppler-effect]]

## Required Vocabulary

Wave, transverse, longitudinal, amplitude, wavelength, frequency, period, wave number, angular frequency, phase constant, wave speed, intensity, decibel, Doppler effect. See [[../flashcards/stage-16-wave-motion]].

## Equations

- [[../equations/wave-function]] — y(x,t) = A sin(kx − ωt)
- [[../equations/wave-speed-on-string]] — v = √(T/μ)
- [[../equations/doppler-effect]] — f_obs = f_s(v ± v_o)/(v ∓ v_s)

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| A | amplitude | m |
| λ | wavelength | m |
| f | frequency | Hz = s⁻¹ |
| T | period | s |
| k | wave number | rad/m |
| ω | angular frequency | rad/s |
| v | wave speed | m/s |
| φ | phase constant | rad |
| μ | linear mass density | kg/m |
| β | sound intensity level | dB (decibels) |
| I | intensity | W/m² |
| I₀ | threshold of hearing | 10⁻¹² W/m² |

## Calculus Connections

The wave equation is a partial differential equation: ∂²y/∂x² = (1/v²) ∂²y/∂t². You are not required to derive or solve it — but recognize that y(x,t) = A sin(kx − ωt) satisfies it, which is why sinusoidal waves are the natural form.

Particle velocity of the medium: vy = ∂y/∂t = −Aω cos(kx − ωt). This is different from the wave speed v.

## Diagrams / Visual Models

```
Transverse wave on string (snapshot at t = 0):

  A |     *     *
    |   *   * *   *
  0 |*           *   *
    |               * *
 -A |                   *

  ←—λ—→  (one full wavelength)

Wave moves in +x direction at speed v = λf.
Each particle of string moves vertically (up-down) only.
```

```
Longitudinal wave (sound):

  Compression → Rarefaction → Compression → ...
  |||||  .  .  .  |||||  .  .  .  |||||

Particles move horizontally (parallel to propagation).
Wavelength = distance between adjacent compressions.
```

## Problem Types

- [[../problem-types/wave-properties-problems]]
- [[../problem-types/doppler-problems]]

## Worked Examples

- [[../worked-examples/wave-function-reading-example]]

## Drills

- [[../drills/wave-properties-drill]]
- [[../drills/doppler-drill]]

## Common Errors

See [[../common-errors/stage-16-wave-motion]].

## Mastery Checklist

- [ ] State the difference between a transverse and longitudinal wave with a physical example of each
- [ ] Given y(x,t) = A sin(kx − ωt + φ), identify A, k, ω, λ, f, T, v, and direction of travel
- [ ] Calculate wave speed using v = λf AND v = ω/k and get the same answer
- [ ] Calculate wave speed on a string given tension T and linear density μ
- [ ] Explain why wave speed ≠ particle speed of the medium
- [ ] Apply the Doppler formula correctly, choosing signs by asking "approaching or receding?"
- [ ] Convert between intensity I (W/m²) and intensity level β (dB)
- [ ] Explain why sound is a longitudinal wave, not a transverse wave

## Do Not Move On Until

Chris can read a wave function and extract all wave properties from it in under two minutes, correctly apply the Doppler formula for all four cases (source moving, observer moving, both), and state in plain English why wave speed and particle speed are different things.
