---
type: equation
status: draft
---

# Torque

## Equation

```
τ = rF sin φ
```

Equivalent forms:
```
τ = r⊥ F       where r⊥ = r sin φ (lever arm)
τ = r F⊥       where F⊥ = F sin φ (perpendicular force component)
```

## Meaning in Plain English

Torque measures how effectively a force causes rotation. A large force applied far from the pivot at a perpendicular angle creates the most torque. A force aimed directly at (or away from) the pivot creates zero torque.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| τ | torque | N·m |
| r | distance from pivot to point of force application | m |
| F | magnitude of applied force | N |
| φ | angle between r⃗ and F⃗ | ° or rad |
| r⊥ | lever arm = perpendicular distance from pivot to line of action | m |
| F⊥ | component of F perpendicular to r⃗ | N |

## Units Check

[τ] = m × N = m × (kg·m/s²) = kg·m²/s²

Note: this is the same as joules (J), but torque is **not** energy. Energy is a scalar; torque has a rotational direction. Units are written N·m for torque, J for energy, to keep the distinction clear.

## Sign Convention

- Counterclockwise torque → **positive**
- Clockwise torque → **negative**

Define the positive direction at the start of every problem and be consistent.

## When to Use It

Any time a force causes or tends to cause rotation about a pivot. Combined with Στ = Iα to find angular acceleration. Combined with equilibrium condition Στ = 0 for static problems (Stage 12).

## When Not to Use It

When a force is applied directly at the pivot (r = 0 → τ = 0). When force is parallel to r⃗ (φ = 0° or 180°, sin φ = 0 → τ = 0).

## Required Assumptions

Rotation about a fixed axis. In Stage 10, torque is a signed scalar. (In 3D rotation — Stage 11 — torque becomes a full vector via the cross product: τ⃗ = r⃗ × F⃗.)

## Calculus Origin

In Stage 11: τ = dL/dt (torque is the rate of change of angular momentum), the rotational analogue of F = dp/dt.

## Example Problem Type

A 2.0 m wrench has a 50 N force applied at its end at φ = 30° to the wrench.
```
τ = (2.0 m)(50 N)(sin 30°) = (2.0)(50)(0.5) = 50 N·m
```

## Common Mistake

Writing τ = rF without the sin φ factor. This is only valid when the force is perpendicular to the position vector (φ = 90°, sin 90° = 1). In general, always include sin φ or identify the lever arm r⊥.

## Sources

Serway & Jewett, 10th ed., Eq. 10.19, Section 10.6.
