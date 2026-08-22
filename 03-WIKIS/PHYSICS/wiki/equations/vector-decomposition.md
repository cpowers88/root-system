---
type: equation
timeline: reference
status: draft
---

# Equation — Vector Decomposition

## Equations

```
Ax = A cos θ
Ay = A sin θ
A = √(Ax² + Ay²)
θ = tan⁻¹(Ay / Ax)
```

In unit-vector notation: **A⃗ = Ax î + Ay ĵ**

## Plain-English Meaning

Any vector in 2D can be broken into two perpendicular pieces (components) along the x and y axes. The components are just the legs of the right triangle formed by the vector and the axes. Knowing the components is equivalent to knowing the full vector — nothing is lost.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| A | magnitude of the vector | same as the physical quantity (m, N, m/s, etc.) |
| Ax | x-component (horizontal projection) | same as A |
| Ay | y-component (vertical projection) | same as A |
| θ | angle measured counterclockwise from the +x axis | degrees (or radians) |
| î, ĵ | unit vectors along +x and +y | dimensionless |

## When to Use

Any time a problem gives you a vector as magnitude + angle and you need to work with components (e.g., vector addition, Newton's 2nd law in 2D, projectile motion).

## When NOT to Use

- If the angle is not measured from the +x axis, you must adjust (θ from +y means sin and cos swap).
- For 3D problems, add a z-component: Az = A cos φ, where φ is the angle from the z-axis.

## Assumptions

- 2D (x-y plane). θ is measured counterclockwise from the +x axis.
- The vector is well-defined (has a clear magnitude and direction).

## Calculus Origin

No calculus needed — this is pure trigonometry. The derivative/integral forms appear in Stage 4 when position, velocity, and acceleration become vector functions of time.

## Example Problem Type

Decomposing a velocity vector into horizontal/vertical components before applying projectile motion equations (Stage 4).

## Common Mistake

Using sin for the x-component and cos for the y-component. The rule: **x goes with cos, y goes with sin** — ONLY when θ is from the +x axis. Always draw the triangle first to avoid this.
