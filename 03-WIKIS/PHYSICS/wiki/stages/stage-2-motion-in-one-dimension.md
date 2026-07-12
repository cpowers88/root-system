---
type: stage
status: draft
---

# Stage 2 — Motion in One Dimension (Ch 2)

## Goal

Describe straight-line motion precisely using position, velocity, and acceleration, and connect each quantity to its calculus definition.

## Syllabus Alignment

Ch 02, lectures W/F Aug 26, 2026.

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 2 (pp. 21–55), sections 2.1–2.8.

## Prerequisite Physics

Stage 1 — units (m, kg, s), dimensional analysis, significant figures.

## Prerequisite Math

Algebra; slope of a line (Δy/Δx); basic concept of a derivative as a rate of change; area under a curve as an integral.

## Core Concepts

- [[../concepts/position]]
- [[../concepts/displacement-vs-distance]]
- [[../concepts/velocity-1d]]
- [[../concepts/acceleration-1d]]
- [[../concepts/free-fall]]

## Required Vocabulary

Position, displacement, distance, average velocity, instantaneous velocity, speed, average acceleration, instantaneous acceleration, kinematics, free fall, g. See `wiki/glossary/` and [[../flashcards/stage-2-motion-in-one-dimension]].

## Equations

- [[../equations/kinematic-equations]] (the five kinematic equations for constant acceleration)

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| x, x₀ | position (final, initial) | m |
| Δx | displacement | m |
| v, v₀ | velocity (final, initial) | m/s |
| v_avg | average velocity | m/s |
| a | acceleration (constant) | m/s² |
| t | time interval | s |
| g | free-fall acceleration | 9.80 m/s² |

## Diagrams / Visual Models

- **Motion diagram:** a series of dots showing position at equal time intervals — widely spaced = fast, closely spaced = slow, increasing spacing = speeding up.
- **x-t graph:** position on the y-axis, time on the x-axis. Slope = velocity. Positive slope = moving in +x direction.
- **v-t graph:** velocity on the y-axis, time on the x-axis. Slope = acceleration. Area under curve = displacement.
- **a-t graph:** acceleration on the y-axis, time on the x-axis. Area under curve = change in velocity.

## Calculus Connections

This is the first stage where calculus appears in physics.

| Physics quantity | Calculus definition | What it means graphically |
|---|---|---|
| Instantaneous velocity | v = dx/dt | slope of x-t graph at one point |
| Instantaneous acceleration | a = dv/dt = d²x/dt² | slope of v-t graph at one point |
| Displacement from velocity | Δx = ∫v dt | area under v-t graph |
| Change in velocity from acceleration | Δv = ∫a dt | area under a-t graph |
| Kinematic equations (origin) | integrate a = constant once → v(t); again → x(t) | constant a produces linear v-t, parabolic x-t |

## Problem Types

- [[../problem-types/constant-velocity]]
- [[../problem-types/constant-acceleration]]
- [[../problem-types/free-fall]]
- [[../problem-types/motion-graphs]]

## Worked Examples

- [[../worked-examples/kinematic-two-cars-example]]

## Drills

- [[../drills/constant-acceleration-drill]]
- [[../drills/free-fall-drill]]
- [[../drills/motion-graphs-drill]]

## Common Errors

See [[../common-errors/stage-2-motion-in-one-dimension]].

## Mastery Checklist

- [ ] Define position, displacement, and distance — and state which is a vector and which is a scalar
- [ ] Calculate average velocity and average acceleration from data
- [ ] State what the slope and area mean on each of the three motion graphs (x-t, v-t, a-t)
- [ ] Identify which kinematic equation to use given a set of known and unknown quantities
- [ ] Solve a constant-acceleration problem with three known quantities to find a fourth
- [ ] Solve a free-fall problem (object thrown up, dropped, or launched at an angle) using a = −9.80 m/s²
- [ ] State the velocity and acceleration at the highest point of a thrown object (v = 0, a ≠ 0)
- [ ] Write v = dx/dt and a = dv/dt and explain in plain English what each means
- [ ] Explain out loud why the kinematic equations cannot be used when acceleration changes

## Do Not Move On Until

Chris can identify the correct kinematic equation from the given/unknown list, apply it correctly with consistent sign conventions, and explain why the equations fail when acceleration is not constant — all without prompting.

## Parked for Later

- Non-constant acceleration problems (require integration or numerical methods — beyond this stage).
- Relative motion in one dimension (briefly in Ch 2; returns more fully in Ch 4).
