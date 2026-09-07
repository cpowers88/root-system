---
type: stage
timeline: later
stage: 8
status: draft
tags: [physics, math]
---

# Stage 8 — Conservation of Energy (Ch 8)

## Goal

Use conservation of mechanical energy and energy bookkeeping (including friction losses) to solve systems problems without tracking every force at every instant.

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 8. File: `raw/textbook/Physics book-0201-0300.pdf`.

## Prerequisite Physics

Stage 7 — Energy of a System (work, kinetic energy, potential energy, conservative vs. nonconservative forces). You must know what K, U_g, and U_s mean and how they're calculated before this stage.

## Prerequisite Math

Algebra (solving for one unknown). Square roots (for solving K = ½mv² for v). Recognizing when to use incline geometry (h = d sin θ).

## Core Concepts

- [[../concepts/mechanical-energy]]
- [[../concepts/conservation-of-energy]]
- [[../concepts/power]]

## Required Vocabulary

Mechanical energy, isolated system, nonisolated system, conservation of energy, power, watt, horsepower. See `wiki/glossary/` and [[../flashcards/stage-8-conservation-of-energy]].

## Equations

- [[../equations/conservation-of-mechanical-energy]]
- [[../equations/power]]

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| E_mech | total mechanical energy = K + U | J |
| K | kinetic energy = ½mv² | J |
| U_g | gravitational potential energy = mgy | J |
| U_s | spring potential energy = ½kx² | J |
| f_k | kinetic friction force | N |
| d | distance over which friction acts | m |
| P | power (rate of energy transfer) | W = J/s |
| W | work | J |
| Δt | time interval | s |
| v | speed | m/s |
| m | mass | kg |
| g | gravitational acceleration (9.80 m/s²) | m/s² |
| y | height above chosen reference level | m |
| k | spring constant | N/m |
| x | spring compression/extension | m |

## Diagrams / Visual Models

**Before-and-after energy diagram:** Draw two snapshots — initial state and final state. Label all energies (K, U_g, U_s) in each snapshot. Draw a friction arrow if present. This makes the energy equation almost automatic.

```
INITIAL STATE           FINAL STATE
height y_i              height y_f
speed v_i               speed v_f
spring stretch x_i      spring stretch x_f
|                       |
Ki + Ui  ---friction---> Kf + Uf
```

**Reference level rule:** Draw a horizontal dashed line at the lowest point the object reaches. Set y = 0 there. All heights are measured from this line.

## Calculus Connections

- **Power** is the only calculus idea introduced here: P = dE/dt (power is the instantaneous rate of energy transfer). For a constant force: P = Fv.
- No new integrals or derivatives beyond Stage 7.
- Energy conservation itself is algebra — it doesn't require calculus to apply.
- Full worked derivations, multi-problem practice, and a real-world use case: [[../calculus-links/power-derivative]].

## Problem Types

- [[../problem-types/energy-conservation-no-friction]]
- [[../problem-types/energy-conservation-with-friction]]
- [[../problem-types/power-problems]]

## Worked Examples

- [[../worked-examples/roller-coaster-energy-example]]

## Drills

- [[../drills/energy-conservation-drill]]
- [[../drills/power-drill]]

## Common Errors

See [[../common-errors/stage-8-conservation-of-energy]].

## Mastery Checklist

- [ ] State the conservation of mechanical energy equation and explain every symbol
- [ ] Identify whether a system is isolated (conservative forces only) or nonisolated (friction present)
- [ ] Choose a reference height, justify it, and apply it consistently throughout a problem
- [ ] Set up a before-and-after energy diagram for any roller-coaster/pendulum/ramp problem
- [ ] Solve for unknown speed, height, or distance using energy conservation (no friction)
- [ ] Solve for unknown speed when friction acts, using Ki + Ui − f_k d = Kf + Uf
- [ ] Calculate height on an incline: h = d sin θ — and know why this comes from geometry
- [ ] Calculate average power given work and time, or given force and speed
- [ ] Explain why friction does not violate conservation of energy — it converts mechanical energy to thermal energy
- [ ] Identify the two beginner traps: inconsistent reference height and forgetting to square v

## Do Not Move On Until

Chris can solve a two-state problem (roller coaster, pendulum, incline with friction) by writing the energy equation, substituting correctly, and solving for the unknown — without needing to track any forces at intermediate points. Energy conservation is a *shortcut* — he must internalize when to reach for it instead of Newton's laws.

## Parked for Later

- Thermal energy and its relationship to temperature (thermodynamics, beyond Stage 18)
- Work done by the system on the environment (full energy transfer picture beyond this course)
