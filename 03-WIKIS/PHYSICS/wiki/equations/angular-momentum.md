---
type: equation
timeline: reference
status: draft
---

# Angular Momentum

## Equations

**For a rigid body rotating about a fixed axis:**
```
L = Iω
```

**For a single particle:**
```
L = r × p = r × mv
|L| = mvr sin θ
```

## Meaning in Plain English

Angular momentum L is the rotational equivalent of linear momentum p = mv. It measures how much spinning tendency an object has, accounting for both its angular speed and how its mass is arranged around the rotation axis.

For the particle form: |L| = mvr sin θ tells you that only the component of the velocity that is perpendicular to the radial direction contributes to angular momentum. A particle moving directly toward or away from the axis has L = 0.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| L | angular momentum | kg·m²/s |
| I | moment of inertia | kg·m² |
| ω | angular velocity | rad/s |
| r | distance from axis to particle | m |
| m | mass of particle | kg |
| v | speed of particle | m/s |
| θ | angle between r⃗ and v⃗ | rad |

## Units Check

For L = Iω: [I][ω] = (kg·m²)(rad/s) = kg·m²/s. Radians are dimensionless, so L has units kg·m²/s. ✓

For L = mvr sin θ: [m][v][r] = kg·(m/s)·m = kg·m²/s. ✓ Same units.

## When to Use It

- L = Iω: when dealing with a rigid body rotating about a fixed axis with known I and ω.
- L = mvr sin θ: when dealing with a particle (or a point mass) moving along a path, with a known position relative to the rotation axis.
- Use both together when a system has rigid bodies AND individual particles (e.g., a disk with a bug sitting on it at radius r).

## When Not to Use It

Do not use L = Iω for a system that is not rotating as a rigid body. Do not use L = mvr for a distributed object — you must integrate or use L = Iω.

## Required Assumptions

- L = Iω requires the body to be rigid and rotating about a fixed, known axis.
- L = mvr sin θ applies to a point particle or an object treated as a point.

## Calculus Origin

Newton's 2nd for rotation: Στ_ext = dL/dt.
For a rigid body with constant I: dL/dt = I(dω/dt) = Iα = Στ, recovering τ = Iα.
The particle form L = r × p can be differentiated: dL/dt = r × F = τ, which is consistent.

## Example Problem Type

Find the angular momentum of a 60 kg skater rotating at 3 rad/s with arms extended (I = 4.0 kg·m²):
```
L = Iω = (4.0 kg·m²)(3 rad/s) = 12 kg·m²/s
```

## Common Mistake

Using ω in revolutions/minute (rpm) without converting to rad/s. Always convert: ω (rad/s) = rpm × (2π/60).

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 11.1–11.2, Eqs. 11.10–11.14.
