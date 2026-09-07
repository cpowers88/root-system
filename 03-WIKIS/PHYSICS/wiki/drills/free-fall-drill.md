---
type: drill
timeline: reference
status: draft
---

# Free-Fall Drill

## Skill Being Practiced

Applying the kinematic equations with a = −9.80 m/s², maintaining consistent sign conventions (up = positive), and handling both "dropped" and "thrown" cases.

## Prerequisites

[[../concepts/free-fall]], [[../equations/kinematic-equations]]

## Instructions

Use g = 9.80 m/s². Take **upward as positive** for all problems. List your known and unknown quantities before choosing an equation. Show your sign reasoning explicitly.

---

## Problem 1 — Dropped Object

A stone is dropped from rest from a bridge 45.0 m above the water.

**(a)** How long does it take to hit the water?

**(b)** What is the stone's velocity just before impact?

**Given:** y₀ = 45.0 m, y = 0 (water), v₀ = 0 (dropped), a = −9.80 m/s²
**Unknown (a):** t   **Unknown (b):** v

**(a)** y = y₀ + v₀t + ½at²
0 = 45.0 + 0 + ½(−9.80)t²
−45.0 = −4.90t²
t² = 9.184
**t = 3.03 s**

**(b)** v = v₀ + at = 0 + (−9.80)(3.03) = **−29.7 m/s**

Negative sign: moving downward at impact. Speed = 29.7 m/s. ✓

---

## Problem 2 — Thrown Upward

A ball is thrown straight upward from the ground with initial speed 18.0 m/s.

**(a)** What is the maximum height?

**(b)** How long is it in the air before returning to the ground?

**Given:** y₀ = 0, v₀ = +18.0 m/s, a = −9.80 m/s²

**(a)** At maximum height, v = 0.
v² = v₀² + 2a(y − y₀)
0 = (18.0)² + 2(−9.80)(y)
0 = 324 − 19.6y
y = 324/19.6 = **16.5 m**

**(b)** Returns to ground: y = 0 again.
y = y₀ + v₀t + ½at²
0 = 0 + 18.0t + ½(−9.80)t²
0 = 18.0t − 4.90t²
0 = t(18.0 − 4.90t)
t = 0 (launch) or t = 18.0/4.90 = **3.67 s** ← total flight time

---

## Problem 3 — Thrown Downward from Height

A window washer's squeegee falls from a 22.0 m tall scaffold and is thrown downward (by accident) at 3.00 m/s.

**(a)** How long does it take to hit the ground?

**(b)** How fast is it moving on impact?

**Given:** y₀ = 22.0 m, y = 0, v₀ = −3.00 m/s (downward!), a = −9.80 m/s²

**(a)** y = y₀ + v₀t + ½at²
0 = 22.0 + (−3.00)t + ½(−9.80)t²
0 = 22.0 − 3.00t − 4.90t²
4.90t² + 3.00t − 22.0 = 0

Quadratic formula: t = [−3.00 ± √(9.00 + 4·4.90·22.0)] / (2·4.90)
= [−3.00 ± √(9.00 + 431.2)] / 9.80
= [−3.00 ± √440.2] / 9.80
= [−3.00 ± 20.98] / 9.80

Positive root: t = (−3.00 + 20.98)/9.80 = 17.98/9.80 = **1.84 s**
(Negative root is before launch — discard.)

**(b)** v = v₀ + at = −3.00 + (−9.80)(1.84) = −3.00 − 18.0 = **−21.0 m/s**

Speed on impact: 21.0 m/s downward.

---

## Problem 4 — Finding Initial Velocity from Apex

A ball is thrown upward and reaches a maximum height of 12.0 m. What was its initial velocity?

**At maximum height:** v = 0, y = 12.0 m, y₀ = 0, a = −9.80 m/s²

v² = v₀² + 2a(y − y₀)
0 = v₀² + 2(−9.80)(12.0)
0 = v₀² − 235.2
v₀² = 235.2
**v₀ = 15.3 m/s** (upward)

---

## Problem 5 — Multi-Point Problem

A ball is thrown upward at 20.0 m/s from the top of a 15.0 m building.

**(a)** What is its maximum height above the ground?

**(b)** How long until it hits the ground?

**(c)** What is its speed just before impact?

**Given:** y₀ = 15.0 m (top of building), v₀ = +20.0 m/s, a = −9.80 m/s²

**(a)** v = 0 at max height:
v² = v₀² + 2a(y − y₀)
0 = (20.0)² + 2(−9.80)(y − 15.0)
0 = 400 − 19.6(y − 15.0)
y − 15.0 = 400/19.6 = 20.4
**y_max = 35.4 m above ground**

**(b)** Ball hits ground: y = 0.
0 = 15.0 + 20.0t − 4.90t²
4.90t² − 20.0t − 15.0 = 0
t = [20.0 ± √(400 + 4·4.90·15.0)] / (2·4.90)
= [20.0 ± √(400 + 294)] / 9.80
= [20.0 ± √694] / 9.80
= [20.0 ± 26.3] / 9.80

Positive root: t = (20.0 + 26.3)/9.80 = 46.3/9.80 = **4.73 s**

**(c)** v = v₀ + at = 20.0 + (−9.80)(4.73) = 20.0 − 46.4 = **−26.4 m/s**

Speed on impact: 26.4 m/s downward.

---

## Mastery Signal

Chris can set up sign conventions without being told, recognize when v₀ = 0 (dropped) vs. v₀ ≠ 0 (thrown), correctly discard the negative root of the quadratic, and get the right sign on velocity at impact — all without prompting.
