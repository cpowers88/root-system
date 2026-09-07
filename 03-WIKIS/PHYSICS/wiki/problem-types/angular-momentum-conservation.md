---
type: problem-type
timeline: reference
status: draft
---

# Angular Momentum Conservation Problems

## How to Recognize This Problem Type

- An object changes its shape or mass distribution while rotating.
- A person walks on a rotating platform.
- Two rotating objects collide and stick together (rotational inelastic collision).
- The phrase "no external torque" or "on frictionless bearings" appears.
- You are asked to find the new angular velocity after a mass redistribution.
- Kepler's 2nd law problems: planet moves closer to Sun, find new orbital speed.

## Given Information Usually Present

- Initial moment of inertia I_i and initial angular velocity ω_i.
- A description of how the mass distribution changes (arms pulled in, person walks inward, object added to rim).
- The new moment of inertia I_f, or enough information to calculate it.

## Unknown Usually Requested

- ω_f (final angular velocity after the change).
- Sometimes: the final kinetic energy (to show energy is not conserved — only L is conserved).

## Diagram to Draw

Two-state diagram showing the system before and after the change:

```
BEFORE                          AFTER
I_i = ___  ω_i = ___           I_f = ___  ω_f = ?
Rotation axis ↑                Rotation axis ↑
L = I_i ω_i                    L = I_f ω_f  (same L)
```

Label what changed (arms pulled in, person moved, object added).

## Equations

```
Condition: Στ_ext = 0

Conservation: L_i = L_f
              I_i ω_i = I_f ω_f

Solve for ω_f: ω_f = (I_i / I_f) × ω_i
```

Common moment of inertia formulas needed:
- Solid disk/cylinder: I = ½MR²
- Hoop (all mass at rim): I = MR²
- Solid sphere: I = (2/5)MR²
- Point mass at radius r: I = mr²
- Rod about center: I = (1/12)ML²
- Rod about end: I = (1/3)ML²

## Step-by-Step Solving Pattern

1. **Identify the system** — what objects are included?
2. **Check the condition** — is Στ_ext = 0? (frictionless bearings, no external torque)
3. **Compute I_i** — add up moments of inertia of all parts in the initial state.
4. **Compute I_f** — add up moments of inertia of all parts in the final state. Note what changed.
5. **Apply conservation:** I_i ω_i = I_f ω_f.
6. **Solve for ω_f:** ω_f = I_i ω_i / I_f.
7. **Unit check:** ω_f should be in rad/s.
8. **Sanity check:** if I_f < I_i, then ω_f > ω_i (spins faster). If I_f > I_i, then ω_f < ω_i (slows down).

## Unit Checks

- L: kg·m²/s both sides ✓
- ω_f = (kg·m²)(rad/s) / (kg·m²) = rad/s ✓

## Common Traps

**Trap 1:** Not including all parts in I_total. A person at radius r on a disk: I_total = I_disk + mr². Don't forget the person.

**Trap 2:** Applying conservation when external torque is not zero. Friction at a bearing, or an unbalanced external force with a moment arm, means L changes.

**Trap 3:** Assuming energy is conserved. In these problems, kinetic energy is NOT conserved (internal forces do work when the skater pulls her arms in — her muscles do work). Only L is conserved.
```
KE_i = ½I_i ω_i²   vs.   KE_f = ½I_f ω_f²
KE_f / KE_i = I_i / I_f ≠ 1 in general
```

**Trap 4:** Mixing rpm with rad/s. Always convert to rad/s before plugging into L = Iω.

## Practice Drills

- [[../drills/angular-momentum-drill]]

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 11.4.
