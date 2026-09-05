---
type: equation
timeline: reference
status: draft
---

# Energy of a Simple Harmonic Oscillator

## Equations

```text
E_total = ½kA²                      [total mechanical energy]
KE = ½mv²                           [kinetic energy]
PE = ½kx²                           [spring potential energy]
E_total = KE + PE = ½mv² + ½kx²    [energy conservation at any point]
v = ω√(A² − x²)                    [speed at position x, from energy]
v_max = ωA                          [maximum speed, at x = 0]
```

## Meaning in Plain English

Total mechanical energy is constant throughout the oscillation — it is fully determined by the amplitude A and the spring constant k. The energy sloshes back and forth between kinetic (maximum at equilibrium) and potential (maximum at the turning points), but the sum never changes.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| E | total mechanical energy | J |
| k | spring constant | N/m |
| A | amplitude | m |
| m | mass | kg |
| v | speed at position x | m/s |
| x | displacement from equilibrium | m |
| ω | angular frequency = √(k/m) | rad/s |

## Units Check

[½kA²] = (N/m)(m²) = N·m = J ✓

[½mv²] = kg·(m/s)² = kg·m²/s² = J ✓

## Energy at Key Positions

| Position | KE | PE | Description |
|---|---|---|---|
| x = +A (right turning point) | 0 | ½kA² | momentarily stopped |
| x = 0 (equilibrium) | ½kA² | 0 | moving fastest |
| x = −A (left turning point) | 0 | ½kA² | momentarily stopped |
| any x | ½k(A²−x²) | ½kx² | KE + PE = ½kA² |

## When to Use These Equations

Use these equations when the problem gives you position x and asks for speed (or vice versa), without specifying time. Energy is the fastest path — you do not need x(t) or v(t) and do not need to know the phase constant.

## When Not to Use These Equations

These equations apply to undamped SHM only. With damping, total energy is not conserved (it decreases over time).

## Required Assumptions

Undamped SHM with a linear restoring force F = −kx. Potential energy formula U = ½kx² is Hooke's Law PE (introduced in Stage 7).

## Calculus Origin

The potential energy U = ½kx² is obtained by integrating the spring force: U = −∫F dx = −∫(−kx) dx = ½kx². Total energy E = KE + PE = constant is a consequence of conservation of mechanical energy, which holds when only conservative forces act. See [[../concepts/conservation-of-energy]].

## Deriving v = ω√(A² − x²)

From energy conservation:
```text
½mv² + ½kx² = ½kA²
½mv² = ½k(A² − x²)
v² = (k/m)(A² − x²) = ω²(A² − x²)
v = ω√(A² − x²)
```

At x = 0: v = ωA = v_max ✓. At x = ±A: v = 0 ✓.

## Common Mistake

- Setting KE = ½mv_max² at a position other than x = 0. v_max only occurs at equilibrium.
- Forgetting that E = ½kA² — amplitude doubles → energy quadruples (E ∝ A²).
- Using v = ωA as the speed everywhere, instead of as only the maximum speed.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 15.3, Equations 15.18–15.21.
