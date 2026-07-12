---
type: concept
stage: 9
chapter: 9
---

# Concept: Conservation of Linear Momentum

## The Law

The total linear momentum of an isolated system is constant in time:

```
p⃗_total = constant   (when ΣF_ext = 0)
```

For a two-object system:

```
m₁v⃗₁ᵢ + m₂v⃗₂ᵢ = m₁v⃗₁f + m₂v⃗₂f
```

## What "Isolated" Means

An isolated system has **no net external force** acting on it. Internal forces between objects inside the system cancel by Newton's 3rd law — every force is paired with an equal and opposite reaction force. Only external forces (from outside the system) can change the total momentum.

## Why It Works (Newton's 3rd Law Connection)

During a collision, Object 1 pushes Object 2 with force F. By Newton's 3rd law, Object 2 pushes back on Object 1 with −F. These forces act over the same time interval Δt. So the impulse on Object 1 is −F·Δt (momentum decreases), and the impulse on Object 2 is +F·Δt (momentum increases by the same amount). The total change is zero.

## When to Apply It

The collision must be brief enough that external forces (gravity, friction, air resistance) deliver negligible impulse during the collision time. This is almost always satisfied for "collision" problems unless the problem explicitly says otherwise.

## Direction: Apply Component by Component

In 2D or 3D, momentum is separately conserved in each direction:

```
x: p_x,before = p_x,after
y: p_y,before = p_y,after
```

## Real-World Anchors

- A gun firing: bullet goes forward, gun recoils backward. Total momentum of gun+bullet system remains zero (they start at rest).
- A skater on frictionless ice throws a ball: the skater slides backward. No external horizontal force → momentum conserved.
- A rocket: exhaust is ejected backward, rocket accelerates forward. Total momentum of rocket+exhaust stays constant.

## Common Confusion

Momentum is conserved even in inelastic collisions. Students often think "inelastic means momentum isn't conserved" — that is wrong. Inelastic means kinetic energy is not conserved. Momentum is always conserved when ΣF_ext = 0, regardless of whether the collision is elastic or not.

## Links

- [[../concepts/linear-momentum]]
- [[../concepts/collision-types]]
- [[../equations/collision-equations]]
- [[../problem-types/perfectly-inelastic-collision]]
- [[../problem-types/elastic-collision]]
