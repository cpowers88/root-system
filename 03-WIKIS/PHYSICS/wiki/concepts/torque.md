---
type: concept
timeline: reference
status: draft
---

# Torque

## What is the physical idea?

Torque is the rotational equivalent of force. Just as a net force causes linear acceleration (F = ma), a net torque causes angular acceleration (τ = Iα). Torque depends on three things: how large the force is, how far from the pivot it acts, and what angle it makes with the position vector.

## What real-world situation does it describe?

Opening a door (pushing far from the hinge is easier than pushing near it). Using a wrench to tighten a bolt. A see-saw where one side has more torque than the other. Any time a force makes something rotate.

## Objects / System Involved

A rigid object that can rotate about a fixed pivot (axis). The force is applied at some point on the object.

## Quantities That Change

A net torque causes α (angular acceleration) to change. If Στ = 0, the object does not accelerate rotationally (it may still spin at constant ω, or be at rest).

## Model / Equation

```
τ = rF sin φ
```

Where:
- r = distance from the pivot (axis) to the point where force is applied
- F = magnitude of the applied force
- φ = angle between the position vector r⃗ (pivot to point) and the force vector F⃗

**Equivalent forms:**
```
τ = r⊥ F          (r⊥ = r sin φ is the lever arm = perpendicular distance from pivot to line of action of F)
τ = r F⊥          (F⊥ = F sin φ is the component of force perpendicular to r⃗)
```

All three forms give the same result — use whichever is easiest given the diagram.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| τ | torque | N·m |
| r | distance from pivot to force application point | m |
| F | magnitude of force | N |
| φ | angle between r⃗ and F⃗ | rad (or °) |
| r⊥ | lever arm = r sin φ | m |

**Units check:** [τ] = m × N = m × kg·m/s² = kg·m²/s² → same dimensions as energy (J), but torque is NOT energy. Do not confuse them.

## Sign Convention

- **Counterclockwise (CCW) torque → positive**
- **Clockwise (CW) torque → negative**

Always define which direction is positive at the start of a problem and stick to it.

## Calculus Connection

In Stage 11, torque is the time-derivative of angular momentum: τ = dL/dt (the rotational analogue of F = dp/dt). In Stage 10, torque is primarily used as a cause of angular acceleration via τ = Iα.

## Diagram / Visual Model

```
     PIVOT
       |
       r⃗  (length r, pointing to where F is applied)
        \
         \  ← φ is the angle here between r⃗ and F⃗
          \
           •----> F⃗

   r⊥ = r sin φ = perpendicular distance from pivot to the dashed line extending F⃗
```

**The lever arm trick:** Extend the line of action of F⃗ in both directions. Drop a perpendicular from the pivot to that line. That perpendicular distance is r⊥ — the lever arm. τ = r⊥ × F.

**Key insight:** Only the component of F perpendicular to r⃗ produces torque. A force directed straight toward or away from the pivot produces zero torque (sin 0° = 0 or sin 180° = 0).

## Problem Types That Use This

- [[../problem-types/torque-angular-acceleration]]

## Common Beginner Mistake

1. **Forgetting sin φ:** writing τ = rF instead of τ = rF sin φ. This overcounts torque unless the force is perpendicular to r (φ = 90°, sin 90° = 1).
2. **Using the wrong r:** r must be from the pivot to the point where force is applied — not the total length of an object if the force is applied partway along.
3. **Losing track of signs:** forgetting to assign + (CCW) or − (CW) before summing torques.
4. **Confusing torque with energy:** N·m is the unit of both, but torque is not energy. Energy is a scalar; torque is a (signed) quantity with a specific axis direction.

## Practice Next

[[../problem-types/torque-angular-acceleration]] and [[../drills/torque-drill]].

## Sources

Serway & Jewett, 10th ed., Ch. 10.6–10.7.
