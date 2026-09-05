---
type: equation
timeline: reference
status: draft
---

# Equation: Impulse-Momentum Theorem — J⃗ = Δp⃗

## Equations

```
J⃗ = Δp⃗ = p⃗_f − p⃗_i

J⃗ = F⃗_avg · Δt          (constant or average force)

J⃗ = ∫ F⃗ dt              (time-varying force — area under F-t graph)
```

## Plain-English Meaning

The impulse delivered to an object equals its change in momentum. A large force acting briefly, or a small force acting for a long time, can produce the same change in motion — what matters is the area under the F-t graph, not just the peak force.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| J⃗ | impulse | N·s = kg·m/s |
| F⃗_avg | average force during the interaction | N |
| Δt | duration of the interaction | s |
| Δp⃗ | change in momentum = p⃗_f − p⃗_i | kg·m/s |

Note: N·s and kg·m/s are equivalent — both are valid for impulse.

## When to Use

- When a force acts over a time interval and you need to find either the resulting velocity change, the average force, or the duration
- When reading a F-t graph and need to find the velocity change (area = impulse = Δp)
- During collisions where force magnitude isn't constant but impulse is needed

## When Not to Use

- For problems where position change matters — use kinematics or work-energy theorem instead
- Do not use F_avg · Δt = Δp if you know the work done (that's energy, not impulse)

## Assumptions

- All forces involved are external to the object in question
- The time interval Δt is well-defined

## Calculus Origin

From Newton's 2nd law: ΣF⃗ = dp⃗/dt, therefore ΣF⃗ dt = dp⃗. Integrating both sides from tᵢ to tf:

```
∫[tᵢ to tf] F⃗ dt = ∫[pᵢ to pf] dp⃗ = Δp⃗
```

The left side is the definition of impulse J⃗.

## F-t Graph Connection

On a Force vs. time graph:
- Area under the curve = impulse = Δp
- Constant force → rectangle: area = F · Δt
- Triangular pulse: area = ½ · F_max · Δt

## Example Problem Type

A 0.145 kg baseball initially at rest is hit by a bat. The bat exerts an average force of 9000 N for 1.5 ms. Find the ball's final speed.

```
J = F · Δt = (9000 N)(0.0015 s) = 13.5 N·s
Δp = 13.5 kg·m/s
vf = Δp/m = 13.5/0.145 = 93 m/s (≈ 208 mph)
```

## Common Mistake

Forgetting direction. If a ball bounces back (e.g., wall problem), vf and vi have opposite signs. The change in momentum is Δp = m(vf − vi), which is larger in magnitude than either momentum alone. Students often forget to subtract (not add) when the ball reverses.
