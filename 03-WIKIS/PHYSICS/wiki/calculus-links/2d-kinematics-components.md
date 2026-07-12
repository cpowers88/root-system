---
type: calculus-link
status: draft
---

# Calculus Link — 2D Kinematics and Independent Components (Stage 4)

## Physics Idea

In two-dimensional motion (projectile motion, circular motion), position, velocity, and acceleration are all vectors. The calculus applies independently to each component — the x-component equations work exactly like Stage 2's 1D equations, and so do the y-component equations.

## Calculus Idea

Vector differentiation: the derivative of a vector is taken component-by-component.

$$\vec{v} = \frac{d\vec{r}}{dt} = \frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j} = v_x\hat{i} + v_y\hat{j}$$

$$\vec{a} = \frac{d\vec{v}}{dt} = \frac{dv_x}{dt}\hat{i} + \frac{dv_y}{dt}\hat{j} = a_x\hat{i} + a_y\hat{j}$$

## Plain-English Connection

For projectile motion: horizontal and vertical motion are independent because their accelerations are independent (a_x = 0; a_y = −g).

| Direction | Physics | Calculus form |
|---|---|---|
| x (horizontal) | constant velocity, no acceleration | v_x = dx/dt = constant; x = x₀ + v_x t |
| y (vertical) | constant downward acceleration g | v_y = dy/dt = v₀y − gt; y = y₀ + v₀y t − ½gt² |

The x and y equations are two separate Stage-2-style problems running simultaneously.

## Symbol Meanings

| Symbol | Meaning |
|---|---|
| r⃗ | position vector (m) |
| v⃗ | velocity vector (m/s) |
| a⃗ | acceleration vector (m/s²) |
| dr⃗/dt | vector derivative — velocity |
| dv⃗/dt | vector derivative — acceleration |
| î, ĵ | unit vectors in x and y directions |

## Small Example — Projectile

Ball launched at v₀ = 20 m/s at 30° above horizontal.

v₀x = 20 cos30° = 17.3 m/s; v₀y = 20 sin30° = 10.0 m/s.

x(t) = 17.3t (no x-acceleration)
y(t) = 10.0t − 4.9t² (a_y = −9.80 m/s²)

v_x(t) = dx/dt = 17.3 m/s (constant)
v_y(t) = dy/dt = 10.0 − 9.80t (changes linearly)

Time to peak: v_y = 0 → t = 10.0/9.80 = 1.02 s.
Peak height: y = 10.0(1.02) − 4.9(1.02)² = 5.10 m.

## Course Location

Stage 4 (Ch 4 — Motion in Two Dimensions). The independence of x and y components — each obeying its own differential equation — is the key insight that makes projectile problems solvable by treating them as two simultaneous 1D problems.

## Common Mistake

Treating the total speed as constant (constant velocity in x doesn't mean constant total speed — the y-component is still changing). Also: using the total launch speed in one direction instead of decomposing into x and y components first.

## Related Pages

[[../stages/stage-4-motion-in-two-dimensions]] — [[../calculus-links/kinematics-derivatives]] — [[../appendix/math-calculus]]
