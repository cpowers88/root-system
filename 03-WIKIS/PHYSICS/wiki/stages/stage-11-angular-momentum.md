---
type: stage
timeline: reference
status: draft
---

# Stage 11 — Angular Momentum (Ch 11)

## Goal

Apply conservation of angular momentum to systems where the net external torque is zero — the rotational analogue of momentum conservation from Stage 9.

## Syllabus Alignment

Chapter 11. Lecture dates TBD from D2L calendar (follows Stage 10 in sequence).

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 11. File: `raw/textbook/Physics book-0301-0400.pdf`.

## Prerequisite Physics

- Stage 10: torque, moment of inertia, rotational kinetic energy, angular velocity/acceleration — required before any of this makes sense.
- Stage 9: linear momentum conservation — angular momentum conservation is the rotational parallel; knowing both helps you see the pattern.

## Prerequisite Math

- Cross product (for L = r × p): direction via right-hand rule, magnitude = |r||p|sin θ.
- Derivatives: τ = dL/dt requires understanding rate of change.

## Core Concepts

- [[../concepts/angular-momentum]]
- [[../concepts/conservation-of-angular-momentum]]

## Required Vocabulary

Angular momentum (L), torque as rate of change of L, conservation of angular momentum, right-hand rule, cross product.

## Equations

- [[../equations/angular-momentum]] — L = Iω and L = mvr sin θ
- [[../equations/conservation-angular-momentum]] — I_i ω_i = I_f ω_f

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| L | angular momentum | kg·m²/s |
| I | moment of inertia | kg·m² |
| ω | angular velocity | rad/s |
| τ | torque | N·m |
| r | position vector from axis to particle | m |
| p | linear momentum (mv) | kg·m/s |
| m | mass | kg |
| v | speed of particle | m/s |
| θ | angle between r and v vectors | rad or ° |

## Diagrams / Visual Models

1. **Right-hand rule for L:** curl the fingers of the right hand in the direction of rotation (the direction ω points). Your thumb points in the direction of L.
2. **Skater pulling arms in:** two positions — arms extended (large I, slow ω) and arms pulled in (small I, fast ω). L is the same in both because no external torque acts.
3. **Merry-go-round + person:** person walks from rim toward center → I_system decreases → ω increases → platform spins faster.

## Calculus Connections

The general form of Newton's second law for rotation is:

```
Στ_ext = dL/dt
```

This is the rotational analogue of ΣF = dp/dt. When Στ_ext = 0, dL/dt = 0, so L is constant — this is conservation of angular momentum.

For a rigid body with constant I: dL/dt = I(dω/dt) = Iα = Στ, recovering τ = Iα from Stage 10.

## Problem Types

- [[../problem-types/angular-momentum-conservation]]

## Worked Examples

- [[../worked-examples/spinning-skater-example]]

## Drills

- [[../drills/angular-momentum-drill]]

## Common Errors

See [[../common-errors/stage-11-angular-momentum]].

## Mastery Checklist

- [ ] State the definition L = Iω (rigid body) and L = mvr sin θ (particle) from memory.
- [ ] Apply the right-hand rule to determine the direction of L for a given rotation.
- [ ] State the condition that makes angular momentum conserved (Στ_ext = 0).
- [ ] Write τ = dL/dt and explain its physical meaning in words.
- [ ] Solve a conservation problem (e.g., skater pulling arms in) using I_i ω_i = I_f ω_f.
- [ ] Compute the angular momentum of a point particle given m, v, r, and angle θ.
- [ ] Explain why the skater spins faster when arms are pulled in, in terms of I and ω — not just "conservation."
- [ ] Identify when NOT to apply conservation (when there is a net external torque).

## Do Not Move On Until

Chris can set up and solve a conservation of angular momentum problem from scratch, correctly compute I_total for a system, and explain both the equation and the physical reason for the result — without prompting.

## Parked for Later

Gyroscopes and precession (also Ch 11) involve 3D angular momentum vectors changing direction under torque — interesting but not required for standard PHYS 2211 exam problems. Revisit if time permits.
