---
type: drill
status: draft
---

# Energy Conservation Drill

## Skill Being Practiced

Applying Ki + Ui = Kf + Uf (no friction) and Ki + Ui − f_k d = Kf + Uf (with friction) to find unknown speed, height, or friction force.

## Prerequisites

[[../concepts/mechanical-energy]], [[../concepts/conservation-of-energy]], [[../equations/conservation-of-mechanical-energy]]

## Instructions

For every problem: (1) Draw initial and final states. (2) Set y = 0. (3) Write the energy equation. (4) Substitute and solve. (5) Check units.

---

## Problem 1 — Ball Dropped from Rest

A 3.0 kg ball is released from rest at a height of 8.0 m above the floor on a frictionless track. Find its speed just before it reaches the floor.

**Solution:**
```
Initial: K_i = 0 (at rest), U_i = mgh = (3.0)(9.80)(8.0) = 235.2 J
Final: K_f = ½mv_f², U_f = 0 (y = 0 at floor)

Ki + Ui = Kf + Uf
0 + 235.2 = ½(3.0)v_f² + 0
v_f² = 235.2 / 1.5 = 156.8
v_f = √156.8 ≈ 12.5 m/s
```
Note: mass cancels → v_f = √(2gh) = √(2 × 9.80 × 8.0) = √156.8 ≈ 12.5 m/s

---

## Problem 2 — Ball Thrown Upward

A 0.20 kg ball is thrown straight upward with an initial speed of 15.0 m/s from ground level (y = 0). Find the maximum height it reaches. Ignore air resistance.

**Solution:**
```
Initial: Ki = ½(0.20)(15.0²) = ½(0.20)(225) = 22.5 J, Ui = 0
Final: Kf = 0 (momentarily at rest at max height), Uf = mgy_max

Ki + Ui = Kf + Uf
22.5 + 0 = 0 + (0.20)(9.80)y_max
y_max = 22.5 / 1.96 ≈ 11.5 m
```
Or: y_max = v_i²/(2g) = 225/(19.6) ≈ 11.5 m ✓

---

## Problem 3 — Pendulum

A 0.50 kg pendulum bob is released from rest at a height of 0.30 m above its lowest point. Find its speed at the lowest point.

**Solution:**
```
Set y = 0 at the lowest point.
Initial: Ki = 0, Ui = mgh = (0.50)(9.80)(0.30) = 1.47 J
Final: Kf = ½mv_f², Uf = 0

0 + 1.47 = ½(0.50)v_f²
v_f² = 1.47 / 0.25 = 5.88
v_f = √5.88 ≈ 2.42 m/s
```

---

## Problem 4 — Block on Rough Incline

A 2.0 kg block starts from rest at the top of a 5.0 m long ramp inclined at 30° above horizontal. The coefficient of kinetic friction is 0.20. Find the block's speed at the bottom of the ramp.

**Solution:**
```
Geometry:
  h = d sin θ = 5.0 × sin 30° = 5.0 × 0.5 = 2.5 m
  N = mg cos θ = (2.0)(9.80)(cos 30°) = (2.0)(9.80)(0.866) = 16.97 N
  f_k = μ_k N = 0.20 × 16.97 = 3.39 N

Energy equation (Ki = 0, Uf = 0 at bottom):
  Ki + Ui − f_k d = Kf + Uf
  0 + mgh − f_k d = ½mv_f²
  (2.0)(9.80)(2.5) − (3.39)(5.0) = ½(2.0)v_f²
  49 − 16.95 = v_f²
  v_f² = 32.05
  v_f ≈ 5.66 m/s

(Without friction: v_f = √(2gh) = √(2 × 9.80 × 2.5) = √49 = 7.0 m/s — friction reduced the final speed.)
```

---

## Problem 5 — Find Friction Coefficient

A 1.5 kg block slides along a horizontal floor, starting at 6.0 m/s and coming to rest after traveling 3.0 m. Find the coefficient of kinetic friction.

**Solution:**
```
Set y = 0 (flat floor — no height change). Uf = Ui = 0.

Ki − f_k d = Kf
½mv_i² − μ_k mg d = 0
½(1.5)(6.0²) − μ_k (1.5)(9.80)(3.0) = 0
27 = μ_k × 44.1
μ_k = 27 / 44.1 ≈ 0.61
```

---

## Problem 6 — Spring Launches Block up Ramp

A spring (k = 800 N/m) is compressed by 0.15 m and launches a 0.50 kg block from rest along a frictionless ramp. The ramp rises to a height of 0.30 m. Find the speed of the block at the top of the ramp.

**Solution:**
```
Initial: Ki = 0, U_spring = ½kx² = ½(800)(0.15²) = ½(800)(0.0225) = 9.0 J, U_g = 0 (at bottom)
Final: Kf = ½mv_f², U_spring = 0 (spring released), U_g = mgh = (0.50)(9.80)(0.30) = 1.47 J

Ki + U_s,i + U_g,i = Kf + U_s,f + U_g,f
0 + 9.0 + 0 = ½(0.50)v_f² + 0 + 1.47
9.0 − 1.47 = 0.25 v_f²
7.53 = 0.25 v_f²
v_f² = 30.12
v_f ≈ 5.49 m/s
```

---

## Mastery Signal

Chris can set up the energy equation for any combination of height, speed, and spring — with or without friction — within 2 minutes, without prompting. All unit checks pass.
