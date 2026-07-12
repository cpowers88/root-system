---
type: equation
status: draft
---

# Equation — Dot Product (Scalar Product)

## Equation

```
A⃗ · B⃗ = AB cos θ               (geometric form)
A⃗ · B⃗ = AxBx + AyBy + AzBz    (component form)
```

The two forms give the same result and can be used interchangeably.

## Plain-English Meaning

The dot product measures how much of vector A points in the direction of vector B (or vice versa — the dot product is symmetric). It collapses two vectors into a single number (a scalar).

When θ = 0° (parallel), the dot product is maximum = AB.
When θ = 90° (perpendicular), the dot product = 0.
When θ = 180° (antiparallel), the dot product is minimum = −AB.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| A, B | magnitudes of the two vectors | same as the physical quantities |
| θ | angle between the two vectors | degrees or radians |
| AxBx, AyBy | products of corresponding components | square of the unit |
| A⃗·B⃗ | result: the dot product | product of the two units (e.g., N·m = J for work) |

## When to Use

- Computing **work**: W = F⃗·d⃗ = Fd cos θ (Stage 7) — the dot product automatically picks out the component of force along the direction of motion.
- Checking whether two vectors are perpendicular (if A⃗·B⃗ = 0, they are).
- Finding the angle between two vectors when you know the components.

## When NOT to Use

Use the **cross product** instead when the result must be a vector perpendicular to both inputs — e.g., torque τ⃗ = r⃗×F⃗ (Stage 10), angular momentum L⃗ = r⃗×p⃗ (Stage 11).

## Assumptions

Both vectors must be in the same vector space. θ is the angle between them when placed tail-to-tail.

## Calculus Origin

No calculus in the definition. The dot product appears inside integrals in Stage 7: W = ∫F⃗·dr⃗ (work by a varying force along a path).

## Unit Vector Identities (memorize these)

```
î·î = ĵ·ĵ = k̂·k̂ = 1     (parallel unit vectors)
î·ĵ = î·k̂ = ĵ·k̂ = 0     (perpendicular unit vectors)
```

## Common Mistake

Confusing the dot product (gives a scalar) with the cross product (gives a vector). Also: computing AB cos θ with θ as the angle one vector makes with the x-axis rather than the angle **between** the two vectors.
