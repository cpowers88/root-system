---
type: equation
timeline: reference
status: draft
---

# Spring (Elastic) Potential Energy and Hooke's Law

## Equations

```text
Hooke's Law:       F_s = −kx

Spring PE:         U_s = ½kx²

Force from PE:     F_x = −dU_s/dx = −kx  ✓ (consistent with Hooke's Law)
```

## Meaning in Plain English

A spring stores energy when it is compressed or stretched. Hooke's Law says the restoring force is proportional to how far the spring is displaced from its natural (equilibrium) length. The further the stretch or compression, the stronger the pull/push back toward center.

Spring PE is always positive or zero — the spring stores energy whether stretched or compressed.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| F_s | spring force (restoring force) | N |
| k | spring constant (stiffness) | N/m |
| x | displacement from equilibrium | m |
| U_s | spring (elastic) potential energy | J |

## Units Check

Hooke: [k][x] = (N/m)(m) = N ✓
Spring PE: [k][x²] = (N/m)(m²) = N·m = J ✓

## Sign Convention for F_s = −kx

| Displacement | Force direction | Physical meaning |
|---|---|---|
| x > 0 (stretched) | F_s < 0 (toward equilibrium) | Spring pulls back |
| x < 0 (compressed) | F_s > 0 (toward equilibrium) | Spring pushes back |
| x = 0 (equilibrium) | F_s = 0 | No net force |

The minus sign is essential — it means the force always *opposes* the displacement.

## When to Use It

- Any spring, rubber band, or elastic device problem.
- Whenever an object is attached to a spring and displaced from rest.
- As a potential energy source in Stage 8 energy conservation problems.
- As the driver of simple harmonic motion (Stage 15, SHM).

## When Not to Use It

- When spring force is not proportional to displacement (non-linear springs) — only valid in the linear (Hooke's Law) regime.
- When x exceeds the spring's elastic limit (real springs break or deform permanently).

## Required Assumptions

Spring obeys Hooke's Law (force is linear in displacement). Mass of the spring itself is neglected unless stated.

## Calculus Origin

Spring PE comes from integrating the spring force (work done against it):

```text
U_s = −W_spring = −∫₀ˣ F_s dx = −∫₀ˣ (−kx) dx = ∫₀ˣ kx dx = ½kx²
```

And verifying with the F = −dU/dx relation: −d(½kx²)/dx = −kx = F_s ✓

## Example Problem Type

"A spring with k = 800 N/m is compressed 0.05 m. What force does it exert and how much energy is stored?"
→ F_s = −(800)(0.05) = −40 N (restoring force of 40 N back toward equilibrium).
→ U_s = ½(800)(0.05²) = ½(800)(0.0025) = 1.0 J.

## Common Mistake

1. Forgetting the ½ in U_s = ½kx² (the most common arithmetic error in spring problems).
2. Dropping the minus sign in Hooke's Law and getting the force direction backward.
3. Using the full length of the spring as x — x is the *change* from equilibrium, not the total length.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Equations 7.9 and 7.21, Sections 7.4 and 7.6.
