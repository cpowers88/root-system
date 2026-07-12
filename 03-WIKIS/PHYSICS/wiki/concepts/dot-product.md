---
type: concept
status: draft
---

# Concept — Dot Product (Scalar Product)

## What it is

The **dot product** is a mathematical operation on two vectors that produces a single number (a scalar). It measures how much one vector "aligns with" or "projects onto" the other.

## Physical anchor

Imagine pushing a heavy box across a floor. If you push straight horizontally in the direction of motion, all your force contributes to the work done. If you push at an angle (partly horizontal, partly downward into the floor), only the horizontal component contributes. The dot product captures exactly this idea:

**W = F⃗ · d⃗ = Fd cos θ**

The cos θ factor reduces the force contribution as the angle between the push and the motion grows. At 90° (push perpendicular to motion), no work is done: cos 90° = 0.

## Formulas

Two equivalent forms — use whichever is convenient:

```
Geometric:   A⃗·B⃗ = AB cos θ
Component:   A⃗·B⃗ = AxBx + AyBy + AzBz
```

## Key results to remember

| Situation | Dot product |
|---|---|
| Parallel vectors (θ = 0°) | AB (maximum positive) |
| Antiparallel (θ = 180°) | −AB (maximum negative) |
| Perpendicular (θ = 90°) | 0 |
| î·î = ĵ·ĵ = k̂·k̂ | 1 |
| î·ĵ = î·k̂ = ĵ·k̂ | 0 |

## The result is always a scalar

The dot product of two vectors is a number — not a vector. It has no direction. The unit of A⃗·B⃗ is the product of the units of A and B (e.g., N·m = joule for work).

## Contrast with cross product

The **cross product** A⃗×B⃗ produces a vector perpendicular to both A and B. It appears in torque (Stage 10) and angular momentum (Stage 11). For now, the dot product is the primary tool.

## Depends on

[[../concepts/vector-components]], [[../concepts/scalar-vs-vector]]

## Unlocks

Work by a constant force W = F⃗·d⃗ (Stage 7); work by a varying force W = ∫F⃗·dr⃗ (Stage 7); checking perpendicularity of vectors; finding angles between vectors from known components.

## Common Mistake

Computing A⃗·B⃗ = AB (forgetting the cos θ factor in the geometric form), or confusing the dot product (scalar) with the cross product (vector).
