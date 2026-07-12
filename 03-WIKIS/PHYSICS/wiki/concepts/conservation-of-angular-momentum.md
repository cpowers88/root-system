---
type: concept
status: draft
---

# Conservation of Angular Momentum

## What is the physical idea?

If the net external torque on a system is zero, the total angular momentum of that system does not change. This is the rotational counterpart of conservation of linear momentum (Stage 9).

## What real-world situation does it describe?

- **Spinning skater:** pulls arms in → moment of inertia I decreases → angular velocity ω increases, so L = Iω stays constant.
- **Diver:** leaves the board with arms extended, then tucks → I decreases → spins faster → opens up to land feet-first.
- **Merry-go-round:** person walks from the rim to the center → total I decreases → platform spins faster.
- **Kepler's second law:** a planet sweeps equal areas in equal times because its angular momentum about the Sun is conserved (gravity exerts zero torque because it acts along r).

## Objects / System Involved

Any rotating system where you can identify that external torques are absent or negligible: a spinning skater on frictionless ice, a diver in mid-air, a rotating platform with a person walking on it.

## Quantities That Change

I and ω change — but their product L = Iω does not, as long as Στ_ext = 0.

## Model or Equation

**Condition:** Στ_ext = 0 on the system.

**Conservation law:**
```
L_i = L_f
I_i ω_i = I_f ω_f        (single rotating body changing shape)
```

**System of objects:**
```
I_total,i × ω_i = I_total,f × ω_f
```
where I_total includes every rotating part. Don't forget to add the moment of inertia of all objects in the system.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| L_i, L_f | initial and final angular momentum | kg·m²/s |
| I_i, I_f | initial and final moment of inertia | kg·m² |
| ω_i, ω_f | initial and final angular velocity | rad/s |

## Calculus Connection

From Newton's 2nd for rotation: Στ_ext = dL/dt.
If Στ_ext = 0, then dL/dt = 0, which means L = constant.
Conservation of angular momentum is the integrated form of this differential law.

## Diagram / Visual Model

**Skater scenario:**

```
Before (arms out):              After (arms in):
  I_i = large                    I_f = small
  ω_i = slow                     ω_f = fast
  L = I_i ω_i             =      L = I_f ω_f  ← same value
```

Always: if I goes down, ω goes up. If I goes up, ω goes down. L stays the same.

## Problem Types That Use This

- [[../problem-types/angular-momentum-conservation]]

## Common Beginner Mistake

Applying conservation of angular momentum when an external torque IS present (e.g., friction at the axle). Always check: is Στ_ext = 0? If not, L changes and you cannot use I_i ω_i = I_f ω_f.

Second mistake: forgetting that I_total includes ALL parts of the system. If a person is standing on the rotating disk, the disk + person form the system, and I_total = I_disk + I_person.

## Practice Next

Work through the spinning-skater worked example, then tackle [[../drills/angular-momentum-drill]].

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 11.4.
