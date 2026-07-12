---
type: calculus-link
status: draft
---

# Calculus Link — Stage 7: Work as an Integral

## Physics idea

Work done by a force that changes with position (like a spring).

## Calculus idea

Definite integral — accumulating infinitely many tiny contributions over an interval.

## Plain-English connection

When force is constant, W = Fd. But if F changes as the object moves (F is a function of x), you can't just multiply — you need to add up all the tiny works dW = F_x dx done over each infinitesimal step dx. That total is the integral.

```text
W = ∫(x_i → x_f) F_x dx
```

Geometrically: the area under the F-x graph between x_i and x_f.

## Symbol meaning

| Symbol | Meaning |
|---|---|
| ∫ | "sum up" — integration symbol |
| F_x | force component in the x direction (can change with x) |
| dx | infinitesimal displacement step (like a tiny slice of the x axis) |
| x_i, x_f | starting and ending position |

## Small worked example — the spring

Spring force: F_x = −kx (Hooke's Law). Compress from x = 0 to x = −A (by distance A):

```text
W_spring = ∫₀⁻ᴬ (−kx) dx = [−kx²/2]₀⁻ᴬ = −k(A²/2) = −½kA²
```

The spring does NEGATIVE work when being compressed — you push energy IN, it stores it. The PE stored = U_s = +½kA² (negative of the spring's work on you → your work on spring is positive).

## F-x graph — visual integration

```
F_x (N)
  ↑
  |
0 |——————————————————→ x (m)
  |      /
  |     / ← spring force line F = −kx
  |    /
Area = ½ base × height = ½(x)(kx) = ½kx²  ← this is U_s
```

The triangle below the x-axis (or above it for compression) is the integral. Area = ½kx².

## Force from potential energy — inverse relationship

If you know the potential energy function U(x), you can get the force by differentiating:

```text
F_x = −dU/dx
```

This means force is the negative slope of the PE curve. Where U is steep, the force is large. Where U is flat, force is zero.

Check on spring: U_s = ½kx² → F_x = −d(½kx²)/dx = −kx ✓ (Hooke's Law recovered).
Check on gravity: U_g = mgy → F_y = −d(mgy)/dy = −mg ✓ (downward gravity recovered).

## Course location

- Introduced: Stage 7, Ch 7 (Sections 7.3 and 7.6–7.8)
- Used next: Stage 8 (Conservation of energy), Stage 9 (impulse = ∫F dt), Stage 15 (SHM differential equation)

## Common mistake

Computing work by a varying force as W = F × d (constant-force formula) when F changes over the interval. The constant formula only works when F doesn't change. For a spring: using F_max × d instead of ½kx².
