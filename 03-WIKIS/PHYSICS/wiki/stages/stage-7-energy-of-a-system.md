---
type: stage
timeline: later
stage: 7
status: draft
tags: [physics, math]
---

# Stage 7 — Energy of a System (Ch 7)

## Goal

Introduce work and energy as an alternative — and often simpler — path to solving motion problems, bypassing force-and-acceleration analysis when force details are messy.

## Syllabus Alignment

Ch 07 in Serway & Jewett 10th ed. Follows Ch 6 (Circular Motion) in the course sequence.

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 7,
sections 7.1–7.9. Section 7.9, Energy Diagrams and Equilibrium of a System, is
required source coverage; the energy/potential diagrams below are its entry point.

## Prerequisite Physics

- Stage 5 (Ch 5): Newton's laws, force, the concept of a net force causing acceleration.
- Stage 6 (Ch 6): Applications of Newton's second law (so force is already fluent).
- Stage 3 (Ch 3): Dot product of two vectors (needed for W = F · d).

## Prerequisite Math

- Dot product: A · B = AB cos θ.
- Definite integral ∫ F dx (conceptual level — finding area under an F-x graph).
- Basic algebra (isolating variables).

## Core Concepts

- [[../concepts/work]] — Work W by a constant force; W by a varying force
- [[../concepts/kinetic-energy]] — K = ½mv²
- [[../concepts/potential-energy]] — Gravitational Ug = mgy; spring Us = ½kx²
- [[../concepts/conservative-vs-nonconservative-forces]] — what distinguishes them; why it matters
- [[../concepts/hookes-law]] — F = −kx; restoring force; spring constant k

## Required Vocabulary

work, kinetic energy, potential energy, conservative force, nonconservative force, spring constant, restoring force, work-energy theorem, dot product.

See [[../flashcards/stage-7-energy-of-a-system]] and `wiki/glossary/`.

## Equations

| Equation | What it computes | Page |
|---|---|---|
| W = F d cos θ | Work by a constant force | [[../equations/work-constant-force]] |
| W = ∫ F dx | Work by a varying force (F changes with position) | [[../equations/work-constant-force]] |
| K = ½mv² | Kinetic energy | [[../equations/kinetic-energy]] |
| W_net = ΔK | Work-energy theorem | [[../equations/work-energy-theorem]] |
| U_g = mgy | Gravitational potential energy (near Earth's surface) | [[../equations/gravitational-pe]] |
| U_s = ½kx² | Spring (elastic) potential energy | [[../equations/spring-pe]] |
| F_s = −kx | Hooke's Law — spring restoring force | [[../equations/spring-pe]] |
| F_x = −dU/dx | Force from potential energy (general) | [[../equations/gravitational-pe]] |

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| W | work | J (joule = N·m = kg·m²/s²) |
| F | force magnitude | N |
| d | displacement magnitude | m |
| θ | angle between F and d vectors | degrees or radians (dimensionless) |
| K | kinetic energy | J |
| m | mass | kg |
| v | speed | m/s |
| U_g | gravitational potential energy | J |
| g | gravitational acceleration | m/s² (≈ 9.80 m/s²) |
| y | height above reference point | m |
| U_s | spring potential energy | J |
| k | spring constant | N/m |
| x | spring displacement from equilibrium | m |

## Diagrams / Visual Models

1. **Work diagram**: Draw the force vector F and the displacement vector d with angle θ between them. Label F cos θ as the component that does work.
2. **F-x graph (Hooke's Law)**: Horizontal axis = x (spring displacement); vertical axis = F = −kx. The work done by the spring equals the area under this graph (a triangle = ½kx²).
3. **Energy bar charts**: Before/after columns showing K and U bars — a visual bookkeeping tool for energy problems.

## Calculus Connections

See [[../calculus-links/stage-7-work-integral]].

Work by a varying force requires integration:

```text
W = ∫(x_i → x_f) F_x dx
```

- The spring force F_s = −kx is a varying force. Integrating: W_spring = ∫₀ˣ (−kx) dx = −½kx²
- The area under an F vs. x graph equals the work done.
- Force from potential energy: F_x = −dU/dx (derivative of potential energy with respect to position).

## Problem Types

- [[../problem-types/work-calculation]] — find work done by one or more forces
- [[../problem-types/work-energy-theorem-problems]] — use W_net = ΔK to find speed or distance
- [[../problem-types/spring-energy-problems]] — Hooke's Law + spring potential energy

## Worked Examples

- [[../worked-examples/work-energy-speed-example]] — use work-energy theorem to find final speed
- [[../worked-examples/spring-compression-example]] — compress a spring, find energy stored and force

## Drills

- [[../drills/work-calculation-drill]] — five problems computing work with various force/angle/displacement combos
- [[../drills/work-energy-theorem-drill]] — six problems using W_net = ΔK
- [[../drills/spring-energy-drill]] — four problems with Hooke's Law and Us = ½kx²

## Common Errors

See [[../common-errors/stage-7-energy-of-a-system]].

## Mastery Checklist

- [ ] State the definition of work in plain English and write the formula with all variables and units
- [ ] Identify the angle θ correctly when F and d are not parallel
- [ ] Explain when work is zero (F ⊥ d, or no displacement) and give a real example
- [ ] Compute kinetic energy from mass and speed; compute speed from kinetic energy
- [ ] Apply the work-energy theorem W_net = ΔK to find final speed or stopping distance
- [ ] Write Hooke's Law with correct sign and units; identify k from a graph or problem statement
- [ ] Compute Us = ½kx² for a compressed or stretched spring
- [ ] Compute Ug = mgy and state what reference point means
- [ ] Distinguish conservative from nonconservative forces with a real-world example for each
- [ ] Use F_x = −dU/dx to find force direction from a potential energy function (conceptual level)
- [ ] Read a potential-energy diagram and identify stable equilibrium, unstable equilibrium, turning points, and allowed motion
- [ ] Draw an energy bar chart for a before/after problem
- [ ] Solve a multi-step problem using the work-energy theorem without confusing W and K

## Do Not Move On Until

Chris can apply W_net = ΔK to any problem involving forces at an angle to displacement, correctly compute spring potential energy using Us = ½kx², and identify whether a force is conservative or not — all without prompting.

## Parked for Later

- **Power (P = W/t = Fv)** — introduced in Ch 8 (Stage 8) where it fits naturally alongside conservation of energy.
- **Non-conservative force energy losses (friction in energy equations)** — Ch 8 (Stage 8).
- **General potential energy from F_x = −dU/dx at an advanced calculus level** — parked until Ch 13 (gravity) and Ch 15 (SHM) where it reappears naturally.
