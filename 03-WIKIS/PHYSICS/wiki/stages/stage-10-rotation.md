---
type: stage
timeline: reference
status: draft
---

# Stage 10 — Rotation of a Rigid Object About a Fixed Axis (Ch 10)

## Goal

Extend Newton's second law to rotating objects. Rotation is a complete parallel system: every linear quantity has a rotational counterpart, and every linear equation has a rotational analogue. Master the analogy table and you master this chapter.

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 10. Located in `raw/textbook/Physics book-0301-0400.pdf` (textbook pp. ~271–320).

## Prerequisite Physics

- Stage 2 (Ch 2): kinematic equations — same structure reused for angular kinematics
- Stage 5 (Ch 5): Newton's second law F = ma — extended to τ = Iα
- Stage 7–8 (Ch 7–8): work-energy theorem and energy conservation — extended to rotational KE and rolling objects

## Prerequisite Math

- Algebra with squared terms
- Integration for moment of inertia: I = ∫r² dm (concept-level; standard results are tabulated)
- Trigonometry: sin φ in the torque formula τ = rF sin φ
- Radians: all angular quantities are in radians, not degrees

## The Key Idea: Linear–Rotational Analogy

Every linear quantity and equation has a rotational twin. Memorize this table — it is the backbone of the entire chapter.

| Linear quantity | Symbol | Units | Rotational twin | Symbol | Units |
|---|---|---|---|---|---|
| Position | x | m | Angular position | θ | rad |
| Velocity | v | m/s | Angular velocity | ω | rad/s |
| Acceleration | a | m/s² | Angular acceleration | α | rad/s² |
| Mass (inertia) | m | kg | Moment of inertia | I | kg·m² |
| Force | F | N | Torque | τ | N·m |
| Newton's 2nd law | F = ma | — | Rotational 2nd law | τ = Iα | — |
| Momentum | p = mv | kg·m/s | Angular momentum | L = Iω | kg·m²/s |
| Kinetic energy | K = ½mv² | J | Rotational KE | K = ½Iω² | J |
| Work | W = Fd | J | Rotational work | W = τθ | J |
| Power | P = Fv | W | Rotational power | P = τω | W |

## Core Concepts

- [[../concepts/angular-kinematics]]
- [[../concepts/torque]]
- [[../concepts/moment-of-inertia]]
- [[../concepts/rotational-kinetic-energy]]
- [[../concepts/rolling-without-slipping]]

## Required Vocabulary

angular position, angular velocity, angular acceleration, torque, lever arm, moment of inertia, parallel-axis theorem, rotational kinetic energy, rolling without slipping.

See [[../flashcards/stage-10-rotation]] for all 18 flashcards.

## Equations

- [[../equations/angular-kinematics-equations]] — ω = ω₀ + αt and the four kinematic equations
- [[../equations/torque]] — τ = rF sin φ
- [[../equations/moment-of-inertia]] — I = Σmr² and the standard table
- [[../equations/rotational-newtons-second-law]] — Στ = Iα
- [[../equations/rolling-without-slipping]] — v_cm = Rω, K_total = ½mv² + ½Iω²

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| θ | angular position | rad |
| ω | angular velocity | rad/s |
| α | angular acceleration | rad/s² |
| τ | torque | N·m |
| I | moment of inertia | kg·m² |
| r | distance from axis | m |
| φ | angle between r⃗ and F⃗ | rad or ° |
| r⊥ | lever arm (moment arm) | m |
| K_rot | rotational kinetic energy | J |
| v_cm | center-of-mass speed (rolling) | m/s |
| R | radius of rolling object | m |
| d | distance from cm to new axis | m |

## Diagrams / Visual Models

**Torque diagram:** Draw the pivot, the position vector r⃗ from pivot to where force is applied, and the force F⃗. The angle φ is between r⃗ and F⃗. The lever arm r⊥ = r sin φ is the perpendicular distance from the pivot to the line of action of F.

```
   pivot
     |
     r⃗ (at angle φ to F)
      \
       \  φ
        +-------> F⃗
        |
       r⊥ = r sinφ (perpendicular distance)
```

**Rolling object:** At any instant, the contact point is stationary. The top of the wheel moves at 2v_cm. The center moves at v_cm = Rω.

**Moment of inertia table:** See [[../equations/moment-of-inertia]] — do not guess these from memory until you've used them enough to remember; look them up until they are automatic.

## Calculus Connections

- [[../calculus-links/rotation-derivatives]]
- ω = dθ/dt (angular velocity is the derivative of angular position)
- α = dω/dt (angular acceleration is the derivative of angular velocity)
- I = ∫r² dm (moment of inertia for continuous objects — standard results tabulated)
- W = ∫τ dθ (work done by a varying torque)

## Problem Types

- [[../problem-types/angular-kinematics-problems]]
- [[../problem-types/torque-angular-acceleration]]
- [[../problem-types/rotational-energy-problems]]
- [[../problem-types/rolling-problems]]

## Worked Examples

- [[../worked-examples/wheel-angular-acceleration-example]]
- [[../worked-examples/rolling-cylinder-incline-example]]

## Drills

- [[../drills/angular-kinematics-drill]]
- [[../drills/torque-drill]]
- [[../drills/rotational-energy-drill]]

## Common Errors

See [[../common-errors/stage-10-rotation]].

## Mastery Checklist

- [ ] State the rotational analogue for every linear quantity (the full analogy table from memory)
- [ ] Write all four angular kinematic equations and identify when each applies
- [ ] Calculate torque given force magnitude, radius, and the angle between them
- [ ] Identify the lever arm on a diagram and compute it from r and φ
- [ ] Look up the correct moment of inertia formula for a given geometry
- [ ] Apply the parallel-axis theorem to shift an axis away from the center of mass
- [ ] Apply Στ = Iα to find angular acceleration or required torque
- [ ] Use energy conservation with both K_trans and K_rot for rolling objects
- [ ] State the rolling-without-slipping condition and explain what it means physically
- [ ] Solve a rolling-on-incline problem using energy methods
- [ ] Check every answer's units (rad/s, N·m, kg·m², J)
- [ ] Explain the solution out loud — why does a hollow cylinder roll slower than a solid one?

## Do Not Move On Until

Chris can set up and solve a problem involving a wheel or rolling object using Στ = Iα and energy conservation without prompting — and can explain why the shape of an object (how I depends on geometry) affects the outcome.

## Parked for Later

- **Three-dimensional rotation:** torque and angular momentum as vectors (cross products, right-hand rule). Full 3D treatment is in Ch 11 (Stage 11). Here, torque is treated as a signed scalar.
- **Non-constant torque problems** requiring ∫τ dθ explicitly: introduced conceptually here, computed in Stage 11 and beyond.
