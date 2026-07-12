---
type: concept
status: draft
---

# Angular Momentum

## What is the physical idea?

Angular momentum is the rotational quantity that stays constant when no external torque acts on a system. It measures how much "spinning tendency" an object or system has, taking into account both how fast it's spinning and how its mass is distributed around the rotation axis.

## What real-world situation does it describe?

- A spinning figure skater who pulls her arms in and speeds up.
- A diver who tucks into a ball to spin faster.
- Earth rotating on its axis — nearly constant L because there's almost no torque acting on it.
- A planet sweeping equal areas in equal times as it orbits (Kepler's second law is conservation of angular momentum).

## Objects / System Involved

Any rotating object or system: a rigid body spinning on an axis, or a particle moving along a curved path. The key is identifying the axis and which external torques (if any) act on the system.

## Quantities That Change

When the moment of inertia I changes (mass moves closer to or farther from the axis), the angular velocity ω changes in the opposite direction to keep L = Iω constant — provided no external torque acts.

## Model or Equation

**For a rigid body rotating about a fixed axis:**
```
L = Iω
```
- L points along the rotation axis (direction given by the right-hand rule).
- Units: kg·m²/s

**For a single particle:**
```
L = r × p = r × mv
|L| = mvr sin θ
```
- r is the position vector from the axis (or chosen origin) to the particle.
- θ is the angle between r and v.
- r sin θ = r⊥, the perpendicular distance from the axis to the line of the velocity vector.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| L | angular momentum | kg·m²/s |
| I | moment of inertia | kg·m² |
| ω | angular velocity | rad/s |
| r | distance from axis to particle | m |
| m | mass | kg |
| v | speed | m/s |
| θ | angle between r⃗ and v⃗ | rad |

## Calculus Connection

Newton's second law for rotation in its most general form:
```
Στ_ext = dL/dt
```
When Στ_ext = 0, dL/dt = 0, meaning L = constant. This is conservation of angular momentum.

For a rigid body with constant I, this reduces to τ = Iα (from Stage 10).

## Diagram / Visual Model

**Right-hand rule:** Point your right hand in the direction of rotation (fingers curl in the direction of spin). Your thumb points in the direction of the angular momentum vector L.

```
        ↑ L (out of page)
        |
   ----[O]----   spinning counterclockwise
```

**Particle angular momentum:**
```
   v ←
        \
    θ    \  (particle)
          \
    r      *
           |
          axis
```
L = mvr sin θ = mv(r sin θ) — perpendicular distance from axis to velocity line.

## Problem Types That Use This

- [[../problem-types/angular-momentum-conservation]]

## Common Beginner Mistake

Confusing angular momentum L (kg·m²/s, a vector) with angular velocity ω (rad/s, also a vector) or angular speed. L = Iω — they are not the same thing. A heavier object at the same ω has more L than a lighter one.

## Practice Next

After understanding L = Iω conceptually, move to [[conservation-of-angular-momentum]] to see what happens when L is constant.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 11.1–11.2.
