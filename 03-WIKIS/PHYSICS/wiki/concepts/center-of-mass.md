---
type: concept
stage: 9
chapter: 9
---

# Concept: Center of Mass

## What It Is

The center of mass (CM) is the weighted average position of all the mass in a system. For a system of particles:

```
x_cm = (m₁x₁ + m₂x₂ + ... + mₙxₙ) / (m₁ + m₂ + ... + mₙ)
     = Σ(mᵢxᵢ) / M_total
```

In 2D, apply separately for x and y.

## Why It Matters

The center of mass moves as if all the system's mass were located there, acted on by only the net external force. Internal forces (collisions between parts) do not change the motion of the center of mass.

```
v_cm = (m₁v₁ + m₂v₂) / (m₁ + m₂)
a_cm = ΣF_ext / M_total
```

This gives a direct link to momentum: the **total momentum of a system equals its
total mass times the center-of-mass velocity**, p_total = M_total·v_cm. That is
why an isolated system's total momentum stays constant even as individual objects
inside it collide — v_cm itself never changes when ΣF_ext = 0.

## Real-World Anchors

- A thrown wrench tumbles chaotically, but its center of mass follows a perfect parabolic arc — exactly as if it were a point particle.
- A diver tucking and extending looks complex, but the center of mass always follows a parabola.
- A binary star system: both stars orbit the system's center of mass.

## Physical Meaning in Collisions

Before a collision, the center of mass moves at v_cm = (m₁v₁ + m₂v₂)/(m₁ + m₂). After an isolated collision (no external forces), the center of mass continues at the same velocity. Individual objects change velocity; the CM does not.

## Center of Mass vs. Center of Gravity

For uniform gravitational fields (normal Earth situations), they are the same point. For very large objects (planetary scale), they can differ.

## Calculation Example

Two objects: m₁ = 3.0 kg at x₁ = 1.0 m, and m₂ = 1.0 kg at x₂ = 5.0 m.

```
x_cm = (3.0·1.0 + 1.0·5.0) / (3.0 + 1.0) = (3.0 + 5.0)/4.0 = 8.0/4.0 = 2.0 m
```

The CM is at 2.0 m — closer to the heavier object (at 1.0 m), as expected.

## Common Confusion

The center of mass is not necessarily where any mass is actually located. For a donut-shaped object, the CM is at the center of the hole — a point with no material at all.

## Links

- [[../concepts/conservation-of-momentum]]
- [[../equations/momentum]]
