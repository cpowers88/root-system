---
type: equation
timeline: reference
status: draft
---

# Rotational Newton's Second Law

## Equation

```
Στ_ext = Iα
```

## Meaning in Plain English

The net external torque on a rigid object equals the object's moment of inertia times its angular acceleration. This is the rotational twin of ΣF = ma: torque plays the role of force, moment of inertia plays the role of mass, and angular acceleration plays the role of linear acceleration.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| Στ_ext | net external torque (sum of all torques about the same axis) | N·m |
| I | moment of inertia about the rotation axis | kg·m² |
| α | angular acceleration | rad/s² |

## Units Check

[Iα] = kg·m² × rad/s² = kg·m²/s² = N·m ✓ (radians are dimensionless)

## When to Use It

Any rigid-body rotation problem where you need to find α given known torques, or find required torque for a given α. Direct analogue of ΣF = ma.

## Procedure: How to Apply Στ = Iα

1. **Identify the axis of rotation.** All torques and the moment of inertia must be about the same axis.
2. **Draw a free-body diagram.** Show all forces on the object.
3. **Identify which forces produce torques.** Only forces with a moment arm (r⊥ ≠ 0) contribute.
4. **Calculate each torque:** τ = rF sin φ with sign (+ CCW, − CW).
5. **Sum all torques:** Στ = τ₁ + τ₂ + ...
6. **Look up or calculate I** for the object's geometry and axis location.
7. **Solve for α:** α = Στ / I

## Connection to Linear System

For a system with both linear and rotational motion (e.g., a mass hanging from a string wrapped around a pulley), write both equations:
```
ΣF = ma         (for the hanging mass, linear)
Στ = Iα         (for the pulley, rotational)
```
Then link them with the constraint: a = Rα (if the string doesn't slip on the pulley).

## When Not to Use It

When the axis is not fixed (e.g., a thrown football tumbling in 3D — requires angular momentum vector approach).

## Required Assumptions

- Fixed rotation axis
- Rigid body (all parts rotate together with the same α)
- α is measured in rad/s²

## Calculus Origin

Στ = Iα is the rotational analogue of F = dp/dt with p = mv. In rotational form: Στ = dL/dt = d(Iω)/dt = I(dω/dt) = Iα (when I is constant). See [[../calculus-links/rotation-derivatives]].

## Example Problem Type

A solid disk (mass M = 5.0 kg, radius R = 0.30 m) has a tangential force of 8.0 N applied at its rim. Find α.
```
τ = RF (force perpendicular to r, so sin 90° = 1)
τ = (0.30 m)(8.0 N) = 2.4 N·m

I = ½MR² = ½(5.0)(0.30²) = 0.225 kg·m²

α = Στ/I = 2.4/0.225 = 10.7 rad/s²
```

## Common Mistake

Forgetting that Στ and I must be computed about the **same axis**. Using a moment of inertia about one axis with torques computed about a different axis gives a wrong answer.

## Sources

Serway & Jewett, 10th ed., Eq. 10.21, Section 10.7.
