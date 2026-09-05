---
type: equation
timeline: reference
status: draft
---

# Conservation of Angular Momentum

## Equation

```
If Στ_ext = 0:    L_i = L_f

For a single body changing shape:
    I_i ω_i = I_f ω_f

For a system of objects:
    (I_disk + I_person)_i × ω_i = (I_disk + I_person)_f × ω_f
```

## Meaning in Plain English

When nothing outside the system exerts a torque on it, the total angular momentum stays fixed. If any part of the system changes shape or redistributes mass (changing I), the angular velocity must change in the opposite direction to compensate.

Intuitively: pull mass toward the axis → harder for it to "reach out" → spins faster. Push mass away from the axis → easier to "reach out" → slows down.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| L_i | initial total angular momentum | kg·m²/s |
| L_f | final total angular momentum | kg·m²/s |
| I_i | initial moment of inertia | kg·m² |
| I_f | final moment of inertia | kg·m² |
| ω_i | initial angular velocity | rad/s |
| ω_f | final angular velocity | rad/s |

## Units Check

[I_i][ω_i] = kg·m²/s = [I_f][ω_f] ✓

## When to Use It

Use I_i ω_i = I_f ω_f when:
1. The net external torque on the system is zero (or negligible).
2. Some internal redistribution of mass causes I to change (person walks on platform, skater moves arms).
3. Two rotating objects collide and stick (like a linear perfectly inelastic collision, but rotational).

## When Not to Use It

Do not apply if there is a significant external torque acting on the system (friction at bearings, external forces with moment arms). In that case L changes and you need τ = dL/dt = Iα to track the change.

## Required Assumptions

- Isolated system with respect to torque: Στ_ext ≈ 0.
- For collisions: use conservation only at the instant of collision, before external forces have time to act.

## Calculus Origin

Στ_ext = dL/dt → if Στ_ext = 0, then dL/dt = 0 → L = constant.
This is the integrated form of Newton's second law for rotation.

## Example Problem Type

A 60 kg skater has I = 4.0 kg·m² with arms out and spins at ω_i = 1.0 rad/s. She pulls her arms in so I_f = 1.5 kg·m². Find ω_f.

```
I_i ω_i = I_f ω_f
(4.0)(1.0) = (1.5)(ω_f)
ω_f = 4.0/1.5 = 2.67 rad/s
```
She spins 2.67 times faster.

## Common Mistake

Forgetting that I_total must include all parts of the system. A person standing on a rotating disk: I_total = I_disk + mr² (for the person treated as a point mass at radius r). If the person moves to a different radius, I_person changes, so I_total changes.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 11.4, Eq. 11.32.
