---
type: calculus-link
status: draft
---

# Calculus Link — Kinematics and Derivatives (Stage 2)

## Physics Idea

In one-dimensional motion, position x changes with time. The rate of that change is velocity. The rate at which velocity changes is acceleration.

## Calculus Idea

The **derivative** of a function gives its instantaneous rate of change. The **integral** gives the accumulated change (area under the curve).

## Plain-English Connection

| Physics statement | Calculus statement | What it means |
|---|---|---|
| Velocity is how position changes over time | v = dx/dt | Slope of the x-vs-t graph at a single instant |
| Acceleration is how velocity changes over time | a = dv/dt = d²x/dt² | Slope of the v-vs-t graph at a single instant |
| Displacement is accumulated velocity over time | Δx = ∫v dt | Area under the v-vs-t graph between two times |
| Velocity is accumulated acceleration over time | v = ∫a dt | Area under the a-vs-t graph |

## Symbol Meanings

| Symbol | Meaning |
|---|---|
| dx/dt | derivative of x with respect to t — instantaneous rate of position change |
| d²x/dt² | second derivative — how the slope of x(t) itself is changing |
| ∫v dt | integral of velocity — area under v-t curve, gives displacement |
| Δx | change in position (displacement) |

## Small Example

If x(t) = 3t² + 2t (position in meters, t in seconds):

- v(t) = dx/dt = 6t + 2 (m/s)
- a(t) = dv/dt = 6 m/s² (constant)
- Displacement from t = 0 to t = 3 s: ∫₀³ (6t + 2) dt = [3t² + 2t]₀³ = 33 m

Constant acceleration kinematics (Stage 2 equations) are just the result of integrating a = constant:
∫ a dt = v₀ + at → v = v₀ + at
∫ v dt = x₀ + v₀t + ½at²

## Course Location

First appears Stage 2 (Ch 2). Used in every subsequent stage that involves motion. Graphical interpretation (slopes on x-t, v-t, a-t graphs) is the most important intuition for all of Stage 2.

## Common Mistake

Confusing average velocity (Δx/Δt = slope of a chord between two points on x-t graph) with instantaneous velocity (dx/dt = slope of the tangent line at one point). Average velocity uses a finite interval; instantaneous velocity uses an infinitesimally small interval — that's what the derivative captures.

## Related Pages

[[../stages/stage-2-motion-in-one-dimension]] — [[../appendix/math-calculus]]
