---
type: calculus-link
timeline: reference
status: draft
---

# Calculus Link — Tangential Acceleration as a Derivative (Stage 4 / Stage 6)

## Physics Idea

An object moving on a curved path can change in two independent ways: its
**direction** (captured by radial/centripetal acceleration) and its **speed**
(captured by tangential acceleration). Uniform circular motion only has the
first. The moment speed also changes — a car accelerating out of a curve, a
roller coaster slowing through a loop — the second component appears.

## Calculus Idea

Tangential acceleration is nothing new mathematically: it is the exact same
"derivative of speed with respect to time" idea from Stage 2 (a = dv/dt),
just evaluated along a curved path instead of a straight line.

$$a_t = \frac{dv}{dt} \qquad a_r = \frac{v^2}{r} \qquad a = \sqrt{a_r^2 + a_t^2}$$

## Plain-English Connection

| Physics statement | Calculus statement | What it means |
|---|---|---|
| How fast the speedometer reading is changing | a_t = dv/dt | Slope of the v(t) graph, same as Stage 2 |
| How fast the direction is changing (curvature) | a_r = v²/r | Not a derivative you compute live here — it's a standing result from differentiating a rotating position vector, used algebraically |
| Total acceleration combines both, at right angles | a = √(a_r² + a_t²) | Pythagorean sum because a_r ⊥ a_t always |

The two components are independent: knowing v(t) at an instant gives you a_r
immediately (plug into v²/r); knowing how v(t) is *changing* gives you a_t
(take the derivative). A problem can hand you either piece numerically, or it
can hand you v(t) as a function and expect you to differentiate for a_t.

## Symbol Meanings

| Symbol | Meaning |
|---|---|
| v(t) | instantaneous speed as a function of time |
| dv/dt | derivative of speed — tangential acceleration a_t |
| v²/r | radial acceleration a_r, evaluated at the instantaneous speed |
| a_t, a_r | perpendicular acceleration components (tangent to path, toward center) |

## Small Example — Differentiating a Given Speed Function

A car enters a curve of radius r = 50.0 m with speed given by
v(t) = 8.00 + 1.50t (m/s), where t is measured from the moment it enters
the curve.

```text
a_t = dv/dt = 1.50 m/s²                         (constant — v(t) is linear)

At t = 4.0 s:  v = 8.00 + 1.50(4.0) = 14.0 m/s
a_r = v²/r = (14.0)²/50.0 = 3.92 m/s²

a = √(a_r² + a_t²) = √(3.92² + 1.50²) = √(15.4 + 2.25) = √17.6 ≈ 4.20 m/s²
```

Notice a_t came directly from differentiating v(t); a_r came from plugging
the resulting speed into v²/r. Two different operations, one combined answer.

## Practice Problems

**Problem 1 — differentiate a nonlinear speed function.**
A conveyor transfer arm carries a part around a curved guide of radius
r = 0.80 m. Its speed along the path is v(t) = 0.50t² (m/s) for the first
2.0 s of the cycle. Find a_t and a_r at t = 1.5 s, then the total acceleration.

**Problem 2 — work backward from acceleration components.**
At a given instant on a curved track, a_r = 6.0 m/s² and a = 10.0 m/s².
Find a_t (there are two possible signs — explain what each one means
physically).

**Problem 3 — recognize when the derivative is zero.**
A centrifuge spins a sample at a constant 1200 rpm for a 30-second test. A
technician asks whether the sample experiences tangential acceleration
during the steady 30 seconds. Answer using the derivative definition, not a
memorized rule.

### Check Yourself

1. a_t = dv/dt = d(0.50t²)/dt = 1.00t → at t=1.5s, a_t = 1.50 m/s².
   v(1.5) = 0.50(1.5)² = 1.125 m/s → a_r = v²/r = (1.125)²/0.80 ≈ 1.58 m/s².
   a = √(1.58² + 1.50²) ≈ √(2.50+2.25) = √4.75 ≈ 2.18 m/s².
2. a_t = √(a² − a_r²) = √(100 − 36) = √64 = ±8.0 m/s². Positive means speeding
   up (a_t same direction as v); negative means slowing down (a_t opposite v).
   The magnitude is the same either way — the problem needs more context (is
   the object speeding up or slowing down?) to pick the sign.
3. No tangential acceleration: constant rpm means v(t) is constant, so
   dv/dt = 0 for the entire 30 seconds. There is still centripetal (radial)
   acceleration throughout — the sample is not accelerating tangentially, but
   it is still accelerating.

## Engineering Use Case

This exact a_t/a_r split is how curve design and ride/vehicle comfort limits
get set in practice. A highway curve, a conveyor transfer arc, or an amusement
ride loop all have a maximum *total* acceleration the design tolerates —
structurally, or for passenger/product safety. A civil or industrial engineer
sizing that curve doesn't just check the centripetal term; if the vehicle or
part is also speeding up or braking through the curve, the tangential term
adds in quadrature and can push the total over the limit even when a_r alone
looks fine. This is exactly why highway ramps post lower speed limits than the
open road even though the curve itself could handle more speed at *constant*
velocity — real vehicles brake and accelerate through the turn, adding a_t on
top of a_r.

## Course Location

Stage 4 (Ch 4.5 — the nonuniform-circular-motion generalization introduced
alongside projectile motion) and reused directly in Stage 6 (Ch 6.1)
whenever circular motion also involves changing speed.

## Common Mistake

Assuming a_t must be given numerically. If a problem gives v(t) as a
function of time, a_t is a differentiation, not a lookup — compute dv/dt
before reaching for v²/r.

## Related Pages

[[../concepts/tangential-and-radial-acceleration]] — [[../stages/stage-4-motion-in-two-dimensions]] — [[../stages/stage-6-circular-motion]] — [[../calculus-links/kinematics-derivatives]] — [[../appendix/math-calculus]]
