---
type: worked-example
timeline: reference
stage: 9
---

# Worked Example: The Ballistic Pendulum

## Physical Situation

A bullet is fired into a wooden block hanging from a string. The bullet embeds in the block (perfectly inelastic collision), and the combined system swings upward to a maximum height h. This is the classic setup for measuring bullet speed from an observable swing.

## Why Two Conservation Laws

The collision itself is perfectly inelastic — kinetic energy is NOT conserved during the collision. But immediately after the collision, the block+bullet system swings up — now mechanical energy IS conserved (from just-after-collision to the peak of the swing). This is a two-phase problem requiring a different law for each phase.

## Given

- Mass of bullet: m = 0.010 kg
- Mass of block: M = 2.0 kg
- Bullet initial speed: v₀ = ? (what we want)
- Maximum height of swing: h = 0.15 m

*(Alternatively, sometimes v₀ is given and h is the unknown.)*

## Diagram

```
Phase 1 — Collision:
[bullet → v₀] ——> [Block M at rest]
           ↓ (stick together)
[(m + M) → vf]       (perfectly inelastic)

Phase 2 — Swing:
[(m + M) at vf] → rises to height h
```

## Step 1: Apply Conservation of Momentum (during collision)

The bullet embeds in the block. External forces (string tension, gravity) act during the collision, but the collision is so brief that their impulse is negligible. Therefore:

```
m·v₀ = (m + M)·vf
```

Solving for vf:

```
vf = m·v₀ / (m + M)
```

## Step 2: Apply Conservation of Mechanical Energy (after collision, during swing)

After the collision, the block+bullet system rises from height 0 to height h. At the peak, all kinetic energy has converted to gravitational potential energy:

```
½(m + M)vf² = (m + M)g·h
```

The (m + M) cancels:

```
vf = √(2gh)
```

## Step 3: Substitute Back for v₀

From Step 1: vf = m·v₀ / (m + M)

Set equal to Step 2 result:

```
m·v₀ / (m + M) = √(2gh)

v₀ = [(m + M)/m] · √(2gh)
```

## Numerical Solution

```
v₀ = [(0.010 + 2.0)/0.010] · √(2 · 9.8 · 0.15)

v₀ = [2.010/0.010] · √(2.94)

v₀ = 201 · 1.715

v₀ ≈ 345 m/s
```

## Unit Check

```
[(kg)/(kg)] · √(m/s² · m) = √(m²/s²) = m/s ✓
```

## How Much Kinetic Energy Was Lost?

Before collision: KE_i = ½(0.010)(345)² = 595 J

After collision (just after): KE_f = ½(2.010)(1.715)² = 2.96 J

Energy lost to bullet embedding in wood: 595 − 2.96 = 592 J (≈ 99.5% of the kinetic energy!)

This confirms that the collision was indeed inelastic — nearly all kinetic energy was lost in the collision phase, not the swing phase.

## What to Remember

1. Identify the two phases: (a) collision → momentum conservation, (b) swing → energy conservation.
2. The order matters — momentum first, then energy.
3. The key is recognizing that "collision" and "subsequent motion" require different conservation laws.
4. Always check: does your answer for vf (just after collision) match what you'd expect? Here vf = 1.7 m/s for a 345 m/s bullet makes sense given the mass ratio.
