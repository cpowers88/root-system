---
type: concept
timeline: reference
status: draft
---

# Kinetic Energy

## What it is

Kinetic energy is the energy an object has because it is moving. It is stored in the motion itself — not in a position, not in a field, but in the speed of the object.

## Real-world physical situation

A moving car, a flying baseball, a sliding hockey puck. The faster they move or the more massive they are, the more kinetic energy they carry.

## Objects and system

Applies to any object with mass and nonzero speed. In Stage 7, treat objects as particles with translational motion only. (Rotational KE is a separate story — Stage 10.)

## Equation

```text
K = ½mv²
```

Unit: J (joule = kg·m²/s²). Always ≥ 0.

## Why this equation applies

Derived from integrating F = ma over a displacement. The ½ comes from integrating v dv = d(½v²). It's not arbitrary — it's a mathematical result of Newton's second law combined with the definition of work.

## Calculus connection

K = ½mv² comes from:

```text
W = ∫F dx = ∫ma dx = ∫m(dv/dt)dx = ∫m v dv = ½mv²
```

This is also how the work-energy theorem is derived.

## Key behavior

- Doubling mass → doubles K.
- Doubling speed → **quadruples** K (because v²).
- K is never negative.
- K is a property of the object's state at one instant — not a rate, not a change.

## Diagram

Energy bar chart (before/after):

```
Before:    |K_i|        After:    |K_f|
If W_net > 0: K_f > K_i
If W_net < 0: K_f < K_i
If W_net = 0: K_f = K_i (no change in speed)
```

## Problem type

Kinetic energy appears in all work-energy problems. See [[../problem-types/work-energy-theorem-problems]].

## Beginner mistake

Using v instead of v²: K ≠ mv/2. The speed must be squared. Always write out the squaring step explicitly to avoid this error.

## What to practice next

- Work-energy theorem: [[../equations/work-energy-theorem]]
- Work-energy theorem drill: [[../drills/work-energy-theorem-drill]]
