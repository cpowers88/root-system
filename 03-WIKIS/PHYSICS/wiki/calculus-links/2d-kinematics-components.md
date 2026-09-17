---
type: calculus-link
timeline: reference
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

## Practice Problems

**Problem 1 — build v(t) and a(t) from a given r(t).**
A part on a transfer arm has position r⃗(t) = (3.0t) î + (5.0t − 4.9t²) ĵ (m).
Find v⃗(t) and a⃗(t) by differentiating each component separately. What does
a⃗(t) tell you about the type of motion this is?

**Problem 2 — independence in action.**
Two balls are launched from the same height at the same instant: Ball A
straight up at 8.0 m/s (pure 1D), Ball B horizontally at 8.0 m/s off a
platform. Using only the y-component equations (independent of any
x-motion), show that both balls hit the ground at the same time.

**Problem 3 — reconstruct the trajectory from acceleration.**
A projectile has a⃗(t) = 0 î − 9.80 ĵ (m/s²) and initial velocity
v⃗₀ = 15.0 î + 6.0 ĵ (m/s) from the origin. Integrate to find v⃗(t) and
r⃗(t). At what time does the y-component of velocity become zero, and what
is the (x, y) position at that instant?

### Check Yourself

1. v⃗(t) = 3.0 î + (5.0 − 9.8t) ĵ; a⃗(t) = 0 î − 9.8 ĵ. Since a⃗ is constant
   and has no x-component, this is projectile motion — constant horizontal
   velocity, constant downward acceleration.
2. Both balls have the same initial vertical velocity component in the
   *vertical* direction they care about... Ball A: v_y0 = 8.0 m/s straight up.
   Ball B: v_y0 = 0 (launched horizontally). These are NOT the same problem —
   the real point: Ball B's fall time depends only on its y-equation
   y = h − 4.9t², identical to a ball simply dropped from height h with
   v_y0 = 0, regardless of its horizontal speed. Its horizontal motion (any
   x-velocity) never appears in that equation — that's the independence
   principle, demonstrated by the fact that x drops out of the y-equation
   entirely.
3. v⃗(t) = 15.0 î + (6.0 − 9.8t) ĵ. r⃗(t) = 15.0t î + (6.0t − 4.9t²) ĵ.
   v_y = 0 when t = 6.0/9.8 ≈ 0.612 s. At that time: x = 15.0(0.612) ≈ 9.18 m,
   y = 6.0(0.612) − 4.9(0.612)² ≈ 1.84 m.

## Real-World Use Case

This is exactly how a **material-handling transfer point** is designed — the
spot where a part leaves one conveyor and must land accurately on the next
one, a chute, or a bin. The part becomes a projectile the instant it leaves
the belt: its horizontal velocity (belt speed) is fixed and independent, and
gravity takes over the vertical component. An industrial engineer sizing the
gap and drop height between two conveyors is solving this exact r⃗(t)
problem — too short a drop and the part doesn't clear the gap; too long and
it overshoots or the impact is too hard. The same math sizes sprinkler
throw distance, packaging drop-test trajectories, and ballistic delivery
systems.

## Related Pages

[[../stages/stage-4-motion-in-two-dimensions]] — [[../calculus-links/kinematics-derivatives]] — [[../calculus-links/tangential-radial-acceleration-derivative]] — [[../appendix/math-calculus]]
