---
type: concept
status: draft
---

# Potential Energy

## What it is

Potential energy is stored energy associated with the *configuration* or *position* of an object within a system. It is energy that hasn't yet been converted to kinetic energy — it's waiting.

The word "potential" means it *could* become kinetic — like a ball at the top of a ramp, a compressed spring, or a stretched rubber band.

## Real-world physical situations

| Type | Physical situation | Stored in... |
|---|---|---|
| Gravitational (U_g = mgy) | Ball held above the floor | Height in Earth's gravity field |
| Spring (U_s = ½kx²) | Compressed spring | Deformation of the spring |

## Key equations

```text
Gravitational:  U_g = mgy      (near Earth's surface)
Spring:         U_s = ½kx²
```

## Why potential energy is associated with conservative forces

Potential energy can only be defined for **conservative forces** — forces where the work done is independent of path. For gravity: it doesn't matter how you bring an object up to height y (straight up, spiral ramp, etc.) — the work gravity does is always −mgy. That path-independence is exactly what lets us define a stored energy (potential energy) associated with position.

**Nonconservative forces** (friction, air drag) do NOT have potential energy. Their work depends on path length — longer path → more friction work. You can't store friction energy and get it back.

## Reference point matters — but only for absolute values

U_g = mgy depends on where y = 0. Setting y = 0 at the floor gives different numbers than setting y = 0 at the ceiling. But **ΔU_g = mg Δy** is the same regardless of reference. Physics only uses changes in PE, not absolute values.

## Calculus connection

Force from potential energy: F_x = −dU/dx

- For gravity: F_y = −d(mgy)/dy = −mg (downward force) ✓
- For spring: F_x = −d(½kx²)/dx = −kx (Hooke's Law) ✓

This is the general connection: PE stores the "accumulated force" that is ready to do work when released.

## Diagram

```
Compressed spring:      Ball at height y:

 |—spring—|○     →    release → KE    ○ at height y → fall → KE
 U_s = ½kx²                           U_g = mgy
```

## Problem type

See [[../problem-types/spring-energy-problems]] and [[../problem-types/work-energy-theorem-problems]].

## Beginner mistake

Confusing potential energy with force. "The spring has potential energy 1.6 J" is NOT the same as "the spring exerts a force of 1.6 N." Energy (J) and force (N) are completely different quantities — use the right equation for each.

## What to practice next

- [[../drills/spring-energy-drill]]
- Conservation of energy (Stage 8): this concept is the foundation for that entire stage.
