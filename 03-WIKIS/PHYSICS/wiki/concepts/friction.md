---
type: concept
status: draft
---

# Friction

## What is the physical idea?

**Friction** is a contact force that opposes relative motion (or the tendency toward relative motion) between two surfaces in contact. It is caused by microscopic interlocking of surface irregularities and intermolecular forces.

There are two types:
- **Static friction** (f_s): prevents surfaces from sliding. Adjusts from 0 to a maximum; acts while surfaces are stationary relative to each other.
- **Kinetic friction** (f_k): opposes sliding. Acts once surfaces are moving relative to each other. Fixed value: f_k = μ_k × n.

Key fact: **μ_s > μ_k** always. It takes more force to start sliding than to maintain sliding.

## What real-world situation does it describe?

- Walking: static friction between shoe and ground propels you forward.
- Sliding a box across the floor: kinetic friction slows it down.
- A car braking without skidding: static friction (tires roll, not slide) — maximum braking force.
- A car skidding: kinetic friction — less braking force, which is why ABS prevents skidding.
- A block sitting on an inclined ramp: static friction holds it in place.

## Objects / System Involved

Two objects whose surfaces are in contact. Friction acts on both (Newton's Third Law): the floor exerts friction on the box leftward, the box exerts friction on the floor rightward.

## Quantities That Change

The friction force direction always opposes the motion (or tendency of motion). The magnitude depends on:
- Whether the object is moving: kinetic → f_k = μ_k n; static → f_s ≤ μ_s n.
- The normal force n (increases on an incline if you press harder onto the surface).
- The coefficient μ (a property of the surface pair, not the object).

## Model or Equations

$$f_k = \mu_k n \quad \text{(kinetic — exact, once sliding)}$$

$$f_s \leq \mu_s n \quad \text{(static — up to the maximum)}$$

See [[../equations/kinetic-friction]] and [[../equations/static-friction]].

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| f_k | kinetic friction | N |
| f_s | static friction | N |
| μ_k | kinetic coefficient (dimensionless) | — |
| μ_s | static coefficient (dimensionless) | — |
| n | normal force | N |

Typical μ values: rubber on dry concrete: μ_s ≈ 1.0, μ_k ≈ 0.80; steel on steel: μ_s ≈ 0.74, μ_k ≈ 0.57; ice on ice: μ_s ≈ 0.10, μ_k ≈ 0.03.

## Calculus Connection

None in Stage 5. Friction is treated as a constant force. In Stage 6 (Ch 6), velocity-dependent resistive forces (air drag: F = −bv or F = −Dv²) are introduced as the next level of friction modeling.

## Diagram / Visual Model

```
Static: object at rest, tendency to slide right
         f_s <--[object]--> F_applied
         f_s adjusts to equal F_applied (up to μ_s × n max)

Kinetic: object sliding right
         f_k <--[object]-->   v (rightward)
         f_k = μ_k × n (fixed value)
```

## Problem Types That Use This

- [[../problem-types/friction-problems]]
- [[../problem-types/inclined-plane]]
- [[../problem-types/fbd-connected-objects]]

## Common Beginner Mistake

Using f_s = μ_s n (equality) when the object is at rest but not on the verge of sliding. Static friction adjusts itself — it's only at its maximum right before the object starts moving. For an object merely sitting on a surface, find f_s from the net-force balance, not from the formula.

## Practice Next

[[../drills/friction-problems-drill]] — seven problems from "is it moving?" to stacked-block scenarios.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 5.8, pp. 136–142.
