---
type: concept
status: draft
---

# Angular Kinematics

## What is the physical idea?

Angular kinematics describes how a rotating object's angle, angular velocity, and angular acceleration are related over time — without yet asking *why* the rotation happens (that's torque). It is the direct rotational parallel to the linear kinematics of Ch 2.

## What real-world situation does it describe?

A spinning wheel, a rotating motor, a CD slowing down, a figure skater completing a spin. Any object rotating about a fixed axis.

## Objects / System Involved

A rigid object rotating about a fixed axis. Every point on the object sweeps through the same angle θ in the same time — that's what "rigid" means.

## Quantities That Change

- θ (angular position) changes as the object rotates.
- ω (angular velocity) changes if the rotation is speeding up or slowing down.
- α (angular acceleration) may be constant or varying.

## The Analogy to Linear Kinematics

This is the most important thing to understand about this chapter: **the angular kinematic equations are identical in structure to the linear kinematic equations.** Just swap symbols:

| Linear | Rotational |
|---|---|
| x (position, m) | θ (angle, rad) |
| v (velocity, m/s) | ω (angular velocity, rad/s) |
| a (acceleration, m/s²) | α (angular acceleration, rad/s²) |
| v = v₀ + at | ω = ω₀ + αt |
| x = x₀ + v₀t + ½at² | θ = θ₀ + ω₀t + ½αt² |
| v² = v₀² + 2a(x − x₀) | ω² = ω₀² + 2α(θ − θ₀) |
| x = x₀ + ½(v₀ + v)t | θ = θ₀ + ½(ω₀ + ω)t |

If you can solve a linear kinematics problem, you can solve an angular kinematics problem by substitution alone.

## Key Definitions

- **Angular position θ:** measured in radians from a reference line. One full revolution = 2π rad = 360°.
- **Angular velocity ω = dθ/dt:** rate of change of angle. Units: rad/s. Positive = counterclockwise (by convention).
- **Angular acceleration α = dω/dt:** rate of change of angular velocity. Units: rad/s².

## Relating Linear and Angular (for a point at radius r from axis)

A point at distance r from the rotation axis has:

| Relationship | Equation | Notes |
|---|---|---|
| Arc length | s = rθ | θ must be in radians |
| Tangential speed | v_t = rω | m/s = m × rad/s |
| Tangential acceleration | a_t = rα | tangential = changing speed |
| Centripetal acceleration | a_c = rω² = v²/r | centripetal = direction change |
| Total linear acceleration | a = √(a_t² + a_c²) | two perpendicular components |

**Critical point:** different points on the same rigid body have different v_t and a_t (because they are at different r), but they all have the same ω and α.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| θ | angular position | rad |
| ω | angular velocity | rad/s |
| α | angular acceleration | rad/s² |
| t | time | s |
| r | radius (distance from axis) | m |
| s | arc length | m |
| v_t | tangential speed of a point | m/s |
| a_t | tangential acceleration of a point | m/s² |
| a_c | centripetal acceleration of a point | m/s² |

## Calculus Connection

- ω = dθ/dt — angular velocity is the time-derivative of angular position (slope of θ-t graph)
- α = dω/dt = d²θ/dt² — angular acceleration is the time-derivative of angular velocity
- For constant α: integrating α once gives ω(t) = ω₀ + αt; integrating again gives θ(t)
- This is identical to the calculus derivation of linear kinematics equations in Stage 2

## Diagram / Visual Model

```
     CCW positive (+)
          ↑
     _____|_____
    /     |θ    \
   |      |------•  ← point at radius r
    \_____|_____/
          |
    CW negative (−)

   ω = rate θ sweeps out
   α = rate ω changes
```

## Problem Types That Use This

- [[../problem-types/angular-kinematics-problems]]

## Common Beginner Mistake

1. Using degrees instead of radians. All angular kinematic equations require radians. Convert at the start: θ(rad) = θ(°) × π/180.
2. Confusing angular speed ω (rad/s, same for all points on body) with tangential speed v_t = rω (m/s, different for each point depending on r).
3. Using the wrong kinematic equation — same mistake pattern as linear kinematics: write down what's given, identify the unknown, pick the equation that connects them.

## Practice Next

Work [[../drills/angular-kinematics-drill]] before moving to torque.

## Sources

Serway & Jewett, 10th ed., Ch. 10.1–10.2.
