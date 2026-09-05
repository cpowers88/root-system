---
type: concept
timeline: reference
status: draft
---

# Hooke's Law

## What it is

Hooke's Law describes the force exerted by a spring (or any elastic material in its linear region) when it is stretched or compressed from its natural (equilibrium) length. The force is proportional to displacement and always directed *back toward equilibrium*.

## Real-world physical situation

Compressing a car's suspension spring, stretching a rubber band, pressing on a mattress. All of these follow Hooke's Law for small displacements.

## Objects and system

The spring exerts a force on whatever is attached to or pressing on it. The spring constant k is a property of the spring itself (how stiff it is).

## Equation

```text
F_s = −kx
```

- F_s is the force the spring exerts on the attached object (N).
- k is the spring constant (N/m) — larger k = stiffer spring.
- x is the displacement of the end of the spring from its equilibrium (natural) length (m). Positive x = stretched; negative x = compressed (by convention).

The minus sign means the force is always **opposite** to the displacement — restoring.

## Variables and units

| Symbol | Meaning | Unit |
|---|---|---|
| F_s | spring force | N |
| k | spring constant | N/m |
| x | displacement from equilibrium | m |

## Calculus connection

The spring force is a position-varying force. Its work is found by integration:

```text
W_spring = ∫₀ˣ (−kx) dx = −½kx²
```

This is why the spring potential energy is U_s = ½kx² — it's the negative of the work done by the spring (work done *against* the spring = PE stored in it).

## F-x graph

```
F_s (N)
  ↑
  |  / (stretched: F_s negative = restoring force toward center)
  | /
  |/
——+————————————→ x (displacement)
  |\
  | \
  |  \ (compressed: F_s positive = restoring force toward center)

Slope = −k  (the steeper the slope, the stiffer the spring)
```

Area of the triangle under the graph from 0 to x = ½kx² = the spring PE.

## Problem type

See [[../problem-types/spring-energy-problems]].

## Beginner mistake

1. **Forgetting the minus sign** in F_s = −kx and getting the direction wrong.
2. **Using total spring length** for x instead of the displacement from natural length. If a spring is naturally 20 cm long and is compressed to 12 cm, then x = −8 cm = −0.08 m, not 0.12 m.
3. **Confusing k with F**: k is the spring constant (a property of the spring); F_s is the force (depends on how far you push).

## What to practice next

- [[../equations/spring-pe]] — spring potential energy
- [[../drills/spring-energy-drill]]
