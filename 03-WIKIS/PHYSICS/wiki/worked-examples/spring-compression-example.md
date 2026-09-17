---
type: worked-example
timeline: reference
status: draft
---

# Worked Example: Spring Compression — Force and Energy Stored

## Physical Situation

A spring with spring constant k = 500 N/m is initially at its natural length. You push a 0.20 kg ball against the spring, compressing it by 0.08 m. Find: (a) the spring force at maximum compression, (b) the elastic potential energy stored in the spring, and (c) if the spring releases the ball from rest on a frictionless surface, what speed does the ball reach when the spring returns to its natural length?

## Diagram

```
 Natural length:   |—spring—| ○ ball
 Compressed:  |—spring—|○
               |← x = 0.08 m →|
```

## Part (a) — Spring force at maximum compression

Hooke's Law: F_s = −kx

Here x = −0.08 m (compression, taking stretched = +x direction).
The *magnitude* of the restoring force:

```text
|F_s| = k|x| = 500 × 0.08 = 40 N
```

Direction: toward equilibrium (away from the wall, toward the ball). So the spring pushes the ball with 40 N.

## Part (b) — Elastic PE stored

```text
U_s = ½kx² = ½ × 500 × (0.08)²
     = ½ × 500 × 0.0064
     = 250 × 0.0064
     = 1.6 J
```

**U_s = 1.6 J** is stored in the compressed spring.

## Part (c) — Speed of ball when spring returns to natural length

When the spring is released, the stored elastic PE converts to kinetic energy. At natural length, U_s = 0.

Apply work-energy theorem (or energy conservation, previewing Stage 8):

```text
U_s(initial) = K(final)    [frictionless, no height change]

½kx² = ½mv²

1.6 = ½(0.20)v²

1.6 = 0.10 v²

v² = 16

v = 4.0 m/s
```

**v = 4.0 m/s** when the ball leaves the spring.

## Unit check

U_s in J = kg·m²/s². Then v² = (2 × J) / kg = m²/s² → v in m/s. ✓

## Key insight

The spring constant k tells you both the force (via F = kx) and the energy (via U = ½kx²) — two different things from the same k. A common mistake is to use F = kx to find energy, or to use U = ½kx² to find force. Use the right equation for the right question.

## Mastery signal

If Chris can solve both parts independently and explain why U_s = ½kx² gives energy while F_s = −kx gives force, Stage 7 spring content is solid.
