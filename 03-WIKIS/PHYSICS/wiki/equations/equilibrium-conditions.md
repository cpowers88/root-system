---
type: equation
status: draft
---

# Equation — Conditions for Static Equilibrium

## Equations

```
ΣFx = 0    (net x-force = 0)
ΣFy = 0    (net y-force = 0)
Στ  = 0    (net torque about any chosen axis = 0)
```

These three equations must all be satisfied simultaneously for an object to be in static equilibrium.

## Plain-English Meaning

- ΣF⃗ = 0: the object does not accelerate (no translation). All forces balance.
- Στ = 0: the object does not rotate (no angular acceleration). All torques balance.

An object can satisfy one condition without the other — you need both.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| ΣFx, ΣFy | sum of all x and y force components | N |
| Στ | sum of all torques about the chosen pivot | N·m |
| τᵢ = rᵢFᵢ sin φᵢ | individual torque (r = distance from pivot to force, φ = angle between r and F) | N·m |

## When to Use

Any problem where an object is completely at rest under multiple forces and/or torques: beams, ladders, hinged structures, bridges, cranes, leaning objects.

## Solving Strategy

1. Draw an extended free body diagram (show WHERE each force acts).
2. Choose a pivot point (smart choice: where an unknown force acts, to zero out its torque).
3. Write Στ = 0 about the chosen pivot — solve for one unknown.
4. Write ΣFx = 0 and ΣFy = 0 — solve for remaining unknowns.

## Common Mistake

Using only ΣF⃗ = 0 and forgetting Στ = 0. An object can be translationally still but spinning if only force balance is satisfied.
