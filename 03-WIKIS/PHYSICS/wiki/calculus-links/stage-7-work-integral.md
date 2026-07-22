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

## Practice Problems

**Problem 1 — integrate a varying force directly.**
A force varies with position as F_x(x) = 4.0x + 2.0 (N, x in m). Find the
work done as the object moves from x = 0 to x = 3.0 m by integrating —
do not use a shortcut formula.

**Problem 2 — spring, but starting from a nonzero stretch.**
A spring with k = 250 N/m is already stretched 0.10 m. Find the work needed
to stretch it further, from x = 0.10 m to x = 0.25 m. (This is not the same
as ½kx² evaluated at 0.25 m alone — set up the definite integral with the
correct limits.)

**Problem 3 — go the other direction: force from potential energy.**
A system's potential energy is given by U(x) = 3x² − 12x + 7 (J, x in m).
Find F_x(x) = −dU/dx. At what value of x is the force zero (equilibrium),
and is it a stable or unstable equilibrium there?

### Check Yourself

1. W = ∫₀³ (4.0x + 2.0) dx = [2.0x² + 2.0x]₀³ = (18.0 + 6.0) − 0 = 24.0 J.
2. W = ∫₀.₁⁰·²⁵ (−250x) dx magnitude... using U_s = ½kx²: ΔU = ½(250)(0.25²)
   − ½(250)(0.10²) = 7.8125 − 1.25 = 6.5625 J ≈ 6.56 J. Confirms the definite
   integral must use both limits, not just the final position.
3. F_x = −d(3x² − 12x + 7)/dx = −(6x − 12) = 12 − 6x. Zero when x = 2.0 m.
   Since U(x) = 3x² − 12x + 7 is an upward-opening parabola (positive
   coefficient on x²), x = 2.0 m is a minimum of U — a stable equilibrium
   (nudge the system away and the force pushes it back).

## Engineering Use Case

Anything designed to absorb or store energy through a *changing* force —
mechanical springs, shock absorbers, elevator buffers, packaging cushioning,
vehicle bumpers — is sized with exactly this integral, not the constant-force
formula. A packaging engineer choosing foam thickness for a drop-test
certification is really solving "how much work (= area under the F-x curve)
can this cushion absorb before the force on the product exceeds its damage
threshold?" The F_x = −dU/dx direction matters too: reading a manufacturer's
force-deflection curve for an isolator and finding where dF/dx changes sign
tells you where the mount transitions from soft to stiff — critical for
tuning vibration isolation on rotating machinery.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 7.3, 7.6–7.8.
