---
type: concept
timeline: reference
status: draft
---

# Conservative vs. Nonconservative Forces

## What it is

The distinction between conservative and nonconservative forces determines whether a potential energy can be defined for a force — and whether energy is stored and retrievable, or permanently lost as heat.

## Conservative force — definition

A force is conservative if:

1. **Path independence**: the work it does between two points is the same regardless of which path is taken.
2. **Closed loop = zero work**: if an object returns to its starting point, the net work done by the force is zero.

Both statements are equivalent — if one holds, the other does too.

**Examples**: gravity, spring force, electric force.

## Nonconservative force — definition

A force is nonconservative if the work it does *depends on the path* — specifically, on the length of the path or the route taken.

**Examples**: kinetic friction, air drag, applied forces from an engine or person.

## Side-by-side comparison

| Property | Conservative | Nonconservative |
|---|---|---|
| Work depends on path? | No — only on endpoints | Yes — longer path → more work |
| Potential energy exists? | Yes | No |
| Round-trip net work | Zero | Not zero (always negative for friction) |
| Energy "retrievable"? | Yes (stored as PE) | No (lost as heat or sound) |
| Physics examples | Gravity, spring force | Friction, air drag |

## Why this matters for problem-solving

Only conservative forces let you define a potential energy (U_g or U_s). The full mechanical energy conservation law (Stage 8) only applies when NO nonconservative forces act — or when you account for their energy losses separately.

Friction degrades mechanical energy into thermal energy permanently. You can't "get it back" as useful kinetic or potential energy.

## Physical world anchor

- **Conservative**: A ball thrown upward and returning to the same height has the same speed it started with (gravity did −W going up, +W coming down, net = 0).
- **Nonconservative**: A box pushed along a rough floor in a closed loop returns to start with less kinetic energy than it began with — friction consumed energy every meter, both ways.

## Diagram

```
Two paths between A and B:

Path 1 (short):   A ——→ B
Path 2 (long):    A ——→ ——→ B

Conservative force: W₁ = W₂  (same work, different paths)
Friction:           W₁ ≠ W₂  (longer path → more energy lost)
```

## Calculus connection

A conservative force can be derived from a potential energy function: F_x = −dU/dx. This relationship cannot be written for nonconservative forces because their work depends on path (not just position), so no single U(x) function exists for them.

## Beginner mistake

Calling gravity "conservative" and thinking that means gravity is somehow special or "good." Conservative just describes a mathematical property of the work integral — path independence. It has nothing to do with moral judgment about the force.

## What to practice next

Stage 8 (Conservation of Energy) — that entire stage is built on this distinction.
