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

## Practice Problems

**Problem 1 — differentiate, don't guess.**
A cart's position is x(t) = 2t³ − 9t² + 12t (m). Find v(t) and a(t). At what
time(s) is the cart momentarily at rest (v = 0)?

**Problem 2 — integrate a nonconstant acceleration.**
A test sled has acceleration a(t) = 6t (m/s²), starting from rest at x = 0.
Find v(t) and x(t) by integrating. This is NOT constant acceleration, so the
Stage 2 kinematic equations (v = v₀+at, etc.) do not apply directly — only
the derivative/integral relationships do.

**Problem 3 — read a graph, then check it against the formula.**
A v-t graph shows velocity ramping linearly from 0 to 20 m/s over 5 s, then
holding constant at 20 m/s for the next 3 s. Find the displacement over the
full 8 s using the area-under-the-curve rule, then verify the first segment
against x = v₀t + ½at².

### Check Yourself

1. v(t) = 6t² − 18t + 12; a(t) = 12t − 18. Setting v = 0: 6t²−18t+12 = 0 →
   t²−3t+2 = 0 → (t−1)(t−2) = 0 → t = 1 s and t = 2 s.
2. v(t) = ∫6t dt = 3t² (+0, starts from rest). x(t) = ∫3t² dt = t³ (+0, starts
   at x=0).
3. Area = triangle (½·5·20 = 50 m) + rectangle (3·20 = 60 m) = 110 m total.
   First segment check: a = 20/5 = 4 m/s²; x = 0 + ½(4)(5²) = 50 m ✓.

## Real-World Use Case

Every motion-control system — a robotic arm, a CNC gantry, an elevator, a
conveyor's start/stop ramp — is programmed as a **velocity profile**, and that
profile is exactly this derivative/integral relationship running in reverse.
An engineer specifies how fast something should be moving at each instant
(v(t)), and the controller integrates that to know where the part should be
(x(t)) and differentiates it to know how hard to accelerate (a(t)) without
exceeding a motor's torque limit or jerking a fragile payload. Reading a
logged v-t curve off a piece of equipment and diagnosing *where* the jerk or
overshoot happens — a sudden change in the slope of v(t), meaning a spike in
a(t) — is a real, everyday systems-engineering skill built directly on this
page.

## Related Pages

[[../stages/stage-2-motion-in-one-dimension]] — [[../appendix/math-calculus]]
