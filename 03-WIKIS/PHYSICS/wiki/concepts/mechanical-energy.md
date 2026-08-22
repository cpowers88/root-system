---
type: concept
timeline: reference
status: draft
---

# Mechanical Energy

## What Is the Physical Idea?

Mechanical energy is the total energy a system has due to motion and position. It combines kinetic energy (energy of motion) and potential energy (energy stored by position or configuration). The key fact: in an isolated system with only conservative forces, mechanical energy stays constant — it converts between K and U but never disappears.

## What Real-World Situation Does It Describe?

Any moving object that also changes height or compresses a spring. A ball thrown upward slows down (K decreasing) while rising (U_g increasing) — the total E_mech stays the same at every point. A roller coaster is the textbook model.

## Objects / System Involved

One or more objects, plus the Earth (for gravitational PE) or a spring (for elastic PE). The system boundary must include everything contributing potential energy.

## Quantities That Change

K and U trade off continuously. Their sum E_mech stays constant if no friction or external forces do work on the system.

## Model / Equation

```
E_mech = K + U
```

Where:
- K = ½mv² (kinetic energy)
- U_g = mgy (gravitational PE; y = height above reference)
- U_s = ½kx² (elastic PE from a spring; x = compression or stretch)

Both may be present simultaneously: E_mech = ½mv² + mgy + ½kx²

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| E_mech | total mechanical energy | J |
| K | kinetic energy | J |
| U | potential energy (gravitational + spring) | J |
| m | mass | kg |
| v | speed | m/s |
| g | 9.80 m/s² | m/s² |
| y | height above reference level | m |
| k | spring constant | N/m |
| x | spring stretch/compression | m |

## Calculus Connection

None in the definition itself. Power (how fast E_mech changes) uses P = dE/dt, but computing E_mech at a given state requires only algebra.

## Diagram / Visual Model

```
Ball at position A (height y_A, speed v_A):
   E_mech = ½mv_A² + mgy_A

Ball at position B (height y_B, speed v_B):
   E_mech = ½mv_B² + mgy_B

If no friction:  E_mech at A = E_mech at B
```

Draw the two states. Label K and U at each. The total bar (K+U) must be the same height if conservative forces only.

## Problem Types That Use This

- [[../problem-types/energy-conservation-no-friction]]
- [[../problem-types/energy-conservation-with-friction]]

## Common Beginner Mistake

**Forgetting which PE terms are present.** If a spring is compressed at the bottom of a ramp and launches an object up, both U_s (at launch) and U_g (at top) are present — but at different states. At the initial state write U_s; at the final state write U_g. Never mix states on the same side of the equation.

## Practice Next

Apply the conservation equation to a pendulum at two points — bottom and top of the swing. Then try a ramp with friction. See [[../drills/energy-conservation-drill]].

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 8.1–8.2.
