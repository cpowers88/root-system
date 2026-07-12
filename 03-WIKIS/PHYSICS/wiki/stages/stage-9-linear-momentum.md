---
type: stage
status: draft
---

# Stage 9 — Linear Momentum and Collisions (Ch 9)

## Goal

Use momentum conservation to analyze collisions and explosions — situations where forces are unknown, vary wildly with time, or act for too short an interval to track directly.

## Syllabus Alignment

Ch 09. Prerequisite for Stage 10 (rotation) and Stage 11 (angular momentum).

## Textbook Alignment

Serway & Jewett, 10th ed., Chapter 9.

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

## Do Not Move On Until

Chris can classify any collision (given problem statement), write the correct equations, and solve for unknowns — without being told which type of collision it is. Must also be able to draw the before-and-after diagram with correct signs before writing a single equation.
