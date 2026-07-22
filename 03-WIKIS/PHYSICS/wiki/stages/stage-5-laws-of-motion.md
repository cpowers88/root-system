---
type: stage
timeline: later
stage: 5
status: draft
tags: [physics, math]
---

# Stage 5 — The Laws of Motion (Ch 5)

## Goal

Move from describing motion (kinematics) to explaining its cause (dynamics) using Newton's three laws and free body diagrams.

## Syllabus Alignment

Ch 05, lectures F Sep 11 – W Sep 16, 2026. Topics: Concept of Force, Newton's Three Laws, Free Body Diagrams, friction.

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 5 (pp. 109–143), sections 5.1–5.8.

## Prerequisite Physics

- Stage 2 (position, velocity, acceleration in 1D)
- Stage 3 (vectors and components)
- Stage 4 (2D motion)

## Prerequisite Math

- Vector algebra (addition, subtraction, components)
- Simultaneous equations (two unknowns from two axes)
- Trigonometry (to decompose forces along inclines)

## Core Concepts

- [[../concepts/force]]
- [[../concepts/newtons-first-law]]
- [[../concepts/newtons-second-law]]
- [[../concepts/newtons-third-law]]
- [[../concepts/mass-vs-weight]]
- [[../concepts/normal-force]]
- [[../concepts/friction]]
- [[../concepts/free-body-diagram]]

## Required Vocabulary

Force, inertia, net force, mass, weight, normal force, static friction, kinetic friction, tension, free body diagram. See `wiki/glossary/` and [[../flashcards/stage-5-laws-of-motion]].

## Equations

- [[../equations/newtons-second-law]] — ΣF = ma
- [[../equations/weight]] — w = mg
- [[../equations/kinetic-friction]] — f_k = μ_k n
- [[../equations/static-friction]] — f_s ≤ μ_s n

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| F | force | N (newton = kg·m/s²) |
| m | mass | kg |
| a | acceleration | m/s² |
| w | weight | N |
| g | gravitational acceleration near Earth's surface | 9.80 m/s² (downward) |
| n | normal force | N |
| f_k | kinetic friction force | N |
| f_s | static friction force | N |
| μ_k | kinetic coefficient of friction | dimensionless |
| μ_s | static coefficient of friction | dimensionless |
| T | tension (in a string/rope) | N |

## Diagrams / Visual Models

**Free Body Diagram rules:**
1. Draw the object as a dot (particle model).
2. Draw one arrow for every force acting ON the object, starting from the dot.
3. Label each arrow with the force name and magnitude.
4. Never draw forces that the object exerts on other objects — only forces on it.
5. Choose a coordinate system (+x, +y) aligned with the motion direction or incline.

**Inclined plane diagram:**
```
        ^ n (normal, perpendicular to surface)
        |
      [block]-----> (direction of motion or tendency)
       /     \
      /angle θ \   f_friction (up the slope, opposes motion)
   __|__________\__
                    
   weight w = mg straight down
   w_x = mg sinθ (along incline, down-slope)
   w_y = mg cosθ (into surface)
```

**Newton's Third Law pairs:**
- Earth pulls block down (gravity); block pulls Earth up (reaction).
- Floor pushes block up (normal); block pushes floor down (reaction).
- These pairs act on DIFFERENT objects — never draw both on the same FBD.

## Calculus Connections

No new calculus in Stage 5. Newton's Second Law (F = ma) is algebraic for constant force. The calculus version — F = m(dv/dt) or F = m(d²x/dt²) — appears explicitly in Stage 7 and beyond when force varies. See [[../appendix/math-calculus]] for the derivative background.

## Problem Types

- [[../problem-types/fbd-single-object]]
- [[../problem-types/fbd-connected-objects]]
- [[../problem-types/inclined-plane]]
- [[../problem-types/atwood-machine]]
- [[../problem-types/friction-problems]]

## Worked Examples

- [[../worked-examples/fbd-block-on-table]]
- [[../worked-examples/inclined-plane-with-friction]]
- [[../worked-examples/atwood-machine-worked]]

## Drills

- [[../drills/fbd-drawing-drill]]
- [[../drills/newtons-second-law-drill]]
- [[../drills/friction-problems-drill]]
- [[../drills/inclined-plane-drill]]

## Common Errors

See [[../common-errors/stage-5-laws-of-motion]].

## Mastery Checklist

- [ ] State Newton's three laws in plain English without looking at notes
- [ ] Draw a correct FBD for a single object on a flat surface (block on table, hanging mass)
- [ ] Draw a correct FBD for an object on an inclined plane, correctly decomposing weight into parallel and perpendicular components
- [ ] Identify Newton's Third Law pairs and confirm they act on different objects
- [ ] Set up and solve ΣF = ma in both x and y directions for a system with friction
- [ ] Distinguish mass (kg) from weight (N) and compute w = mg
- [ ] State the difference between static friction (resists starting) and kinetic friction (resists sliding) and which is larger
- [ ] Solve an Atwood machine problem using FBDs for both masses
- [ ] Solve a two-block connected system on a flat or inclined surface
- [ ] Identify which direction to call positive and be consistent throughout

## Do Not Move On Until

Chris can draw a correct FBD on his own, set up the ΣF = ma equations from it, and solve for unknown acceleration or tension — for at least: a block on a flat surface with friction, a block on an incline, and an Atwood machine.

## Parked for Later

- Drag force and terminal velocity from Ch 6 (Stage 6) — requires the concept of force as a function of velocity, not just constant force.
- F = m(d²x/dt²) as a second-order differential equation — appears in Stage 15 (SHM) and Stage 16 (waves).
- Newton's law of gravitation (Ch 13, Stage 13) — the force law that explains why g = 9.80 m/s².
