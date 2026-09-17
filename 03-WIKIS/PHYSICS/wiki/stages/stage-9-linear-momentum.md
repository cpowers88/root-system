---
type: stage
timeline: later
stage: 9
status: draft
tags: [physics, math]
---

# Stage 9 — Linear Momentum and Collisions (Ch 9)

## Goal

Use momentum conservation to analyze collisions and explosions — situations where forces are unknown, vary wildly with time, or act for too short an interval to track directly.

## Syllabus Alignment

Ch 09. Prerequisite for Stage 10 (rotation) and Stage 11 (angular momentum).

## Textbook Alignment

Serway & Jewett, 10th ed., Chapter 9, sections 9.1–9.6. **2026-07-21 decision:**
sections 9.7–9.9 (systems of many particles, deformable systems, rocket
propulsion) are parked, not built — see Parked for Later below. Both 2026-07-21
neighbor syllabi jump straight from collisions/center-of-mass to Chapter 10
(rotation) without stopping at these sections, which corroborates the park
decision; final confirmation still depends on Section 54.

## Prerequisite Physics

- Stage 5: Newton's 2nd and 3rd laws (momentum conservation is Newton's 3rd law applied over time)
- Stage 7: kinetic energy (needed to classify collision types)
- Stage 8: energy conservation (used alongside momentum in elastic collisions)

## Prerequisite Math

Vector algebra (signs and components), simultaneous equations for elastic collisions.

## Core Concepts

- [[../concepts/linear-momentum]]
- [[../concepts/impulse]]
- [[../concepts/conservation-of-momentum]]
- [[../concepts/collision-types]]
- [[../concepts/center-of-mass]]

## Required Vocabulary

Momentum, impulse, isolated system, elastic collision, inelastic collision, perfectly inelastic collision, center of mass. See [[../flashcards/stage-9-linear-momentum]].

## Equations

- [[../equations/momentum]] — p⃗ = mv⃗
- [[../equations/impulse-momentum-theorem]] — J⃗ = FΔt = Δp⃗
- [[../equations/collision-equations]] — all collision formulas

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| p⃗ | linear momentum | kg·m/s |
| m | mass | kg |
| v⃗ | velocity | m/s |
| J⃗ | impulse | N·s = kg·m/s |
| F | force (average during collision) | N |
| Δt | time interval (collision duration) | s |
| x_cm | center of mass position | m |

## Calculus Connection

Impulse as the integral of a time-varying force:

```
J⃗ = ∫ F⃗ dt = Δp⃗
```

This is why a short, large force (like a bat hitting a ball) can produce the same impulse as a small, long force — what matters is the area under the F-t graph, not the peak force.

Newton's 2nd law in its general form:

```
ΣF⃗ = dp⃗/dt
```

F = ma is the special case when mass is constant.

Full worked derivations, multi-problem practice, and a real-world use case:
[[../calculus-links/impulse-integral]].

## Diagrams to Draw

**Before-and-after diagram:** always draw the system at the moment before the collision and immediately after. Label every mass, velocity (with arrow showing direction), and sign convention.

```
Before:           [m₁ →v₁ᵢ]    [m₂ v₂ᵢ=0]

After (inelastic): [m₁ + m₂ →vf]

After (elastic):   [m₁ →v₁f]   [m₂ →v₂f]
```

## Problem Types

- [[../problem-types/impulse-problems]]
- [[../problem-types/perfectly-inelastic-collision]]
- [[../problem-types/elastic-collision]]
- [[../problem-types/2d-collision]]

## Worked Examples

- [[../worked-examples/ballistic-pendulum-example]] — combines perfectly inelastic collision + energy conservation
- [[../worked-examples/2d-collision-example]] — 2D momentum conservation with components

## Drills

- [[../drills/momentum-impulse-drill]]
- [[../drills/collision-drill]]

## Common Errors

See [[../common-errors/stage-9-linear-momentum]].

## Mastery Checklist

- [ ] Define linear momentum as a vector quantity and give its units
- [ ] State the impulse-momentum theorem and explain what impulse physically represents
- [ ] Read a F-t graph and identify the impulse as the area under the curve
- [ ] State the condition required for momentum conservation (ΣF_ext = 0)
- [ ] Distinguish elastic, inelastic, and perfectly inelastic collisions — state what is conserved in each
- [ ] Solve a perfectly inelastic collision (1D) for final velocity
- [ ] Solve an elastic collision (1D, one object initially at rest) for both final velocities
- [ ] Solve a 2D collision by applying momentum conservation separately in x and y
- [ ] Verify kinetic energy is or is not conserved after a collision
- [ ] Find the center of mass position of a two-body system
- [ ] State the relationship p_total = M_total·v_cm and explain why an isolated system's total momentum staying constant is the same fact as its center-of-mass velocity staying constant

## Do Not Move On Until

Chris can classify any collision (given problem statement), write the correct equations, and solve for unknowns — without being told which type of collision it is. Must also be able to draw the before-and-after diagram with correct signs before writing a single equation, and connect center-of-mass velocity to total system momentum.

## Parked for Later

- **Sections 9.7–9.9 (systems of many particles, deformable systems, rocket
  propulsion).** Parked 2026-07-21 — see [[../parking-lot]]. Rocket propulsion in
  particular (v_f = v_i + v_e ln(m_i/m_f)) is a genuinely useful real-world
  momentum application, but neither newly obtained neighbor syllabus schedules
  it and the core Stage 9 skills (impulse, collision types, center of mass) do
  not depend on it. Unlock condition: Section 54's real D2L scope confirms it is
  assessed, or Chris asks for it directly as an engineering-interest topic.
- **Angular momentum** (L = Iω, conservation of L) is the rotational analogue of
  everything in this stage — it belongs to Stage 11, after torque and moment of
  inertia exist in Stage 10.
