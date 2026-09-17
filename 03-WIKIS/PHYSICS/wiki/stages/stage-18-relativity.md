---
type: stage
timeline: reference
status: draft
---

# Stage 18 — Special Relativity (Ch 38, Capstone)

## Goal

Understand why Galilean mechanics breaks down at speeds near light, apply Einstein's two postulates, calculate time dilation and length contraction, use relativistic velocity addition, and compute relativistic momentum and energy.

## Syllabus Alignment

Topic: "Explain the basic ideas of special relativity"
Textbook: Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 38 (sections 38.1–38.8)
Position: Capstone unit of PHYS 2211, KSU, Dr. Behera, Fall 2026.

## Textbook Alignment

| Section | Topic |
|---|---|
| 38.1 | The Principle of Galilean Relativity |
| 38.2 | The Michelson-Morley Experiment |
| 38.3 | Einstein's Principle of Relativity |
| 38.4 | Consequences of the Special Theory — Time Dilation |
| 38.5 | Length Contraction |
| 38.6 | The Lorentz Transformation Equations |
| 38.7 | The Lorentz Velocity Transformation Equations |
| 38.8 | Relativistic Momentum and Energy |

## Prerequisite Physics

- Stage 1–2: Displacement, velocity, reference frames (Galilean version — this is what breaks)
- Stage 3–4: Acceleration and kinematics — relativity re-examines these at high speed
- Stage 5–6: Newton's laws — relativistic momentum replaces classical mv
- Stage 9: Energy — relativistic KE replaces ½mv²

If those stages feel blurry, review velocity and kinetic energy definitions before starting here.

## Prerequisite Math

- Algebra and square roots (Lorentz factor requires no calculus)
- Ratio reasoning — practice thinking in fractions of c
- Scientific notation — c = 3.00 × 10⁸ m/s appears in every problem

No new calculus is introduced in this stage.

---

## Core Concepts List

1. [[../concepts/galilean-relativity]] — the before-Einstein version; explains what breaks
2. [[../concepts/einsteins-postulates]] — the two foundational assumptions
3. [[../concepts/time-dilation]] — moving clocks run slow; light clock thought experiment
4. [[../concepts/length-contraction]] — moving objects are shorter along the direction of motion
5. [[../concepts/relativistic-energy]] — rest energy, kinetic energy, total energy, E-p relation

---

## Required Vocabulary

| Term | Plain-English Definition |
|---|---|
| Inertial reference frame | A non-accelerating frame; Newton's laws hold in it |
| Aether | The supposed medium for light waves — shown not to exist by Michelson-Morley |
| Postulate | A starting assumption accepted without proof; everything else derived from it |
| Lorentz factor γ | The number 1/√(1 − v²/c²); appears in every SR formula; always ≥ 1 |
| Proper time Δt₀ | Time measured by a clock at rest with respect to both events (the shorter time) |
| Proper length L₀ | Length measured in the rest frame of the object (the longer length) |
| Time dilation | Moving clocks tick more slowly than stationary ones |
| Length contraction | Moving objects are shorter in the direction of motion |
| Simultaneity | Two events happening at the same time — this is relative, not absolute |
| Rest energy | The energy in mass at rest: E₀ = mc² |
| Total energy | All energy of a moving object: E = γmc² |
| Relativistic momentum | p = γmv — greater than classical mv at high speed |

See [[../flashcards/stage-18-relativity]] for drill-ready definitions.

---

## Equations

| Equation | Name | When to Use |
|---|---|---|
| γ = 1/√(1 − v²/c²) | Lorentz factor | First step in every SR calculation |
| Δt = γ Δt₀ | Time dilation | Clock moving relative to observer; Δt > Δt₀ |
| L = L₀ / γ | Length contraction | Object moving relative to observer; L < L₀ |
| u' = (u − v)/(1 − uv/c²) | Lorentz velocity addition | Adding velocities when either is a large fraction of c |
| p = γmv | Relativistic momentum | Momentum of a fast-moving particle |
| K = (γ − 1)mc² | Relativistic kinetic energy | KE of a fast-moving object |
| E₀ = mc² | Rest energy | Energy stored in mass alone |
| E = γmc² | Total relativistic energy | K + rest energy together |
| E² = (pc)² + (mc²)² | Energy-momentum relation | Relates E and p without needing γ or v explicitly |

---

## Variables and Units Table

| Symbol | Meaning | Unit |
|---|---|---|
| γ | Lorentz factor | Dimensionless (always ≥ 1) |
| v | Speed of the moving frame or object | m/s |
| c | Speed of light in vacuum | 3.00 × 10⁸ m/s |
| β = v/c | Speed as fraction of c | Dimensionless |
| Δt | Dilated time (measured by observer watching a moving clock) | s |
| Δt₀ | Proper time (measured by clock at rest with both events) | s |
| L | Contracted length (measured when object moves past observer) | m |
| L₀ | Proper length (measured in the rest frame of the object) | m |
| u | Velocity of object in original frame | m/s |
| u' | Velocity of object in new frame | m/s |
| p | Relativistic momentum | kg·m/s |
| m | Rest mass | kg |
| K | Relativistic kinetic energy | J |
| E₀ | Rest energy | J |
| E | Total relativistic energy | J |

---

## Diagrams

### Diagram 1 — Lorentz Factor vs. Speed

```
γ
 |                                   *
 |                               *
 |                           *
5|                       *
 |                   *
 |               *
3|           *
 |       *
2|     *
 |   *
1| *
 +---.2---.4---.6---.8---1.0 → v/c
```

Key values:
- v = 0: γ = 1.00 (no effect)
- v = 0.5c: γ = 1.15 (15% effect)
- v = 0.8c: γ = 1.67 (67% effect)
- v = 0.9c: γ = 2.29
- v = 0.99c: γ = 7.09
- v = 0.999c: γ = 22.4
- v = c: γ = ∞ (impossible for massive objects)

Everyday objects move at v/c ≈ 10⁻⁸ to 10⁻⁵. At these speeds γ ≈ 1.000000001 — classical mechanics is an excellent approximation. Relativistic effects only become significant above about v = 0.1c.

---

### Diagram 2 — Light Clock (Time Dilation Thought Experiment)

**In the rest frame of the clock (observer S'):**

```
  ┌─────┐  ← mirror
  │     │
  │  ↕  │  light bounces straight up and down
  │     │
  └─────┘  ← mirror (distance d apart)
```

One tick: Δt₀ = 2d/c (light travels 2d at speed c)

**In the lab frame (observer S) watching the clock move sideways at speed v:**

```
 ┌──────────────────────┐  ← mirror (moved to the right)
  \                    /
   \                  /   light must travel a longer diagonal path
    \                /
     \              /
      ┌────────────┐  ← mirror
```

By the Pythagorean theorem, the diagonal path length = √(d² + (vΔt/2)²) > d.

Since c is the same in both frames, more time must pass:
Δt = γ Δt₀  ← the lab observer measures a LONGER time between ticks.

The moving clock ticks more slowly. This is not an optical illusion. It is confirmed by every particle-physics experiment ever run.

---

### Diagram 3 — Muon Decay (Real-World Time Dilation Evidence)

```
~15,000 m
┌──────────────────────────────────┐ ← cosmic ray hits atmosphere here
│  Muon created, v = 0.998c       │
│  Rest half-life: τ₀ = 2.2 μs   │
│                                  │
│  Classical expected distance:    │
│  d = vτ₀ = (0.998c)(2.2μs)      │
│     ≈ 659 m  ← muon "should"    │
│       decay long before surface  │
│                                  │
│  But muons ARE detected below:   │
│                                  │
│  γ at v = 0.998c ≈ 15.8         │
│  Δt (Earth frame) = γτ₀ ≈ 34.8μs│
│  Distance = (0.998c)(34.8μs)    │
│           ≈ 10,400 m ✓           │
│                                  │
└──────────────────────────────────┘ ← Earth's surface
```

The muon's own internal "clock" runs slow by factor γ = 15.8. In its own frame, only 2.2 μs passes — but in the Earth frame, 34.8 μs passes, and the muon travels far enough to reach the surface. Both frames agree: muon reaches Earth.

---

## Calculus Connections

No new calculus is introduced in Chapter 38.

The Lorentz algebra involves only square roots, fractions, and algebraic manipulation.

One calculus link worth noting (for understanding, not calculation):
- Relativistic KE = K = (γ−1)mc² is derived by integrating relativistic force F = dp/dt over displacement, but the integral is done in the textbook. You use only the result.

Historical connection: p = γmv replaces p = mv (Stage 5). K = (γ−1)mc² replaces K = ½mv² (Stage 9). At low speeds, γ ≈ 1 and these reduce to the familiar classical forms via Taylor expansion. Stages 1–9 are low-speed approximations of the general relativistic equations.

---

## Problem Types

- [[../problem-types/time-dilation-problems]] — recognize proper time, apply Δt = γΔt₀
- [[../problem-types/relativistic-energy-problems]] — rest energy, KE, total energy, E-p relation
- [[../problem-types/length-contraction-problems]] — recognize proper length, apply L = L₀/γ

---

## Worked Examples

- [[../worked-examples/muon-decay-time-dilation]] — real muon experiment: v = 0.998c, time dilation + length contraction from two frames
- [[../worked-examples/relativistic-kinetic-energy]] — electron at 0.8c: classical vs. relativistic KE comparison

---

## Drills

- [[../drills/time-dilation-length-contraction-drill]] — 6 problems with answers
- [[../drills/relativistic-energy-momentum-drill]] — 5 problems with answers

---

## Common Errors

See full list: [[../common-errors/stage-18-relativity]]

Top traps:
1. Confusing proper time vs. dilated time (proper time is the SHORTER one)
2. Thinking "proper" means "correct" — it means "measured at rest with the events"
3. Using classical velocity addition at high speed (wrong above ~0.1c)
4. Forgetting rest energy mc² in total energy calculations
5. Applying length contraction in the wrong direction (only along motion)
6. Thinking relativistic effects are optical illusions — they are physically real
7. Using K = ½mv² at high speed — this formula fails above ~0.1c
8. Getting γ < 1 — this is always an arithmetic error; γ ≥ 1 always

---

## Mastery Checklist

Before moving on, Chris must be able to:

- [ ] State Einstein's two postulates in plain English without looking
- [ ] Explain what the Michelson-Morley experiment showed and why it matters
- [ ] Compute γ for any given v/c from scratch
- [ ] Identify the proper time in a word problem (the shorter elapsed time)
- [ ] Apply Δt = γ Δt₀ correctly (result must be ≥ Δt₀)
- [ ] Identify the proper length in a word problem (the longer length, rest frame)
- [ ] Apply L = L₀/γ correctly (result must be ≤ L₀)
- [ ] Apply Lorentz velocity addition u' = (u−v)/(1−uv/c²) instead of classical u' = u−v
- [ ] Calculate relativistic momentum p = γmv
- [ ] Calculate relativistic KE using K = (γ−1)mc²
- [ ] Calculate rest energy E₀ = mc² and total energy E = γmc²
- [ ] Use E² = (pc)² + (mc²)² when v (or γ) is not given but p is
- [ ] Explain the muon decay experiment from both frames (Earth frame and muon frame)
- [ ] Identify and avoid the top 8 common errors

---

## Do Not Move On Until

- You can set up a time dilation problem from scratch — correctly identifying which time is proper — without matching formulas by keyword.
- You can set up a relativistic energy problem from scratch.
- You can explain why classical velocity addition fails and write the correct Lorentz formula.
- You score 5/6 or better on the time dilation/length contraction drill.
- You score 4/5 or better on the relativistic energy/momentum drill.

---

## Parked Material (Beyond PHYS 2211 Scope)

| Topic | Why Parked | Unlock Condition |
|---|---|---|
| General relativity | Requires curved spacetime geometry and tensor calculus | Upper-division mechanics + multivariable calculus |
| Spacetime (Minkowski) diagrams | Powerful geometric tool; not required for this course | After mastering the algebraic SR equations here |
| Relativistic electrodynamics | Maxwell's equations in covariant 4-vector form | After PHYS 2212 (E&M) + linear algebra |
| Twin paradox (full resolution) | Requires careful handling of accelerating frames | After mastering the basics here |
| Four-vectors | The compact algebraic notation for SR in 4D | Advanced mechanics or modern physics course |
| Gravitational time dilation | From GR, not SR | After General Relativity |
| Relativistic Doppler effect | Extension of SR kinematics | After mastering time dilation |

See [[../parking-lot]] for details.

---

## Glossary Links

[[../glossary/lorentz-factor]] | [[../glossary/proper-time-proper-length]] | [[../glossary/rest-energy]] | [[../glossary/time-dilation]] | [[../glossary/length-contraction]]

## Equation Links

[[../equations/lorentz-factor]] | [[../equations/time-dilation]] | [[../equations/length-contraction]] | [[../equations/relativistic-energy]] | [[../equations/lorentz-velocity-addition]]
