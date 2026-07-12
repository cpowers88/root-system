---
type: equation
status: draft
---

# Work by a Force

## Equations

```text
Constant force:  W = F d cos θ  =  F⃗ · d⃗

Varying force:   W = ∫(x_i → x_f) F_x dx
```

## Meaning in Plain English

Work is the transfer of energy to an object by a force acting over a displacement. Only the component of force *along* the direction of motion does work. A force perpendicular to motion does zero work.

The varying-force form says: if the force changes as the object moves (like a spring), add up (integrate) all the tiny contributions F_x dx over the path.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| W | work done by the force | J (joule = N·m = kg·m²/s²) |
| F | magnitude of the force | N |
| d | magnitude of the displacement | m |
| θ | angle between the force vector and the displacement vector | degrees or rad (dimensionless) |
| F_x | x-component of force (along direction of motion) | N |
| x | position along the direction of motion | m |

## Units Check

W = F d cos θ → [N][m][dimensionless] = N·m = J ✓

## Sign Convention

| Situation | Sign of W | Physical meaning |
|---|---|---|
| Force has component in direction of motion (θ < 90°) | + | Energy added to object |
| Force perpendicular to motion (θ = 90°) | 0 | No energy transfer |
| Force opposes motion (θ > 90°, e.g., friction) | − | Energy removed from object |

## When to Use It

- Any time a force acts on an object over a displacement and you need to find the energy transferred.
- Use W = Fd cos θ when the force is constant in magnitude and direction.
- Use W = ∫ F_x dx when the force varies with position (spring, non-uniform field).

## When Not to Use It

- When no displacement occurs (W = 0 by definition — wall example).
- When you want the *total* energy change — then use the work-energy theorem W_net = ΔK instead.

## Required Assumptions

- For W = Fd cos θ: force is constant (fixed magnitude, fixed direction) over the entire displacement.
- For W = ∫F dx: force may vary, but must be expressible as a function of position.

## Calculus Origin

The constant-force form is derived by taking W = ∫F_x dx and pulling the constant F cos θ outside the integral: W = F cos θ ∫dx = F cos θ · d.

The varying-force form is the general definition. For a spring: F_x = −kx, so W_spring = ∫₀ˣ (−kx) dx = −½kx² (spring does negative work when being compressed — you do positive work on it, and it stores that as potential energy Us = +½kx²).

## Example Problem Type

- "A person pulls a suitcase at 25° above horizontal with 80 N force for 15 m. How much work does the person do?" → W = 80 × 15 × cos 25° ≈ 1088 J.

## Common Mistake

Using the angle between the rope and the *surface* instead of the angle between the force vector and the displacement vector. Draw both vectors from the same starting point and measure the enclosed angle.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Equations 7.1 and 7.7.
