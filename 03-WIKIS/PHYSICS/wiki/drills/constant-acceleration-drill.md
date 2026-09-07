---
type: drill
timeline: reference
status: draft
---

# Constant-Acceleration Drill

## Skill Being Practiced

Selecting the correct kinematic equation, applying sign conventions, and solving for an unknown in constant-acceleration problems.

## Prerequisites

[[../concepts/velocity-1d]], [[../concepts/acceleration-1d]], [[../equations/kinematic-equations]]

## Instructions

For each problem:
1. Define your positive direction.
2. List the five kinematic quantities and mark what's given and what's unknown.
3. Write the equation you'll use (not all five — just the one).
4. Solve algebraically, then substitute numbers.
5. Check units and sign.

---

## Problem 1 — Constant Velocity (warm-up)

A train moves at a constant 22.0 m/s. How far does it travel in 15.0 s?

**Known:** v₀ = 22.0 m/s, v = 22.0 m/s, a = 0, t = 15.0 s, x₀ = 0
**Unknown:** x

**Solution:** x = x₀ + v₀t = 0 + (22.0)(15.0) = **330 m**

---

## Problem 2 — Finding Final Velocity

A car starts from rest and accelerates at 2.50 m/s² for 8.00 s. What is its final velocity?

**Known:** v₀ = 0 m/s, a = 2.50 m/s², t = 8.00 s
**Unknown:** v

**Solution:** v = v₀ + at = 0 + (2.50)(8.00) = **20.0 m/s**

---

## Problem 3 — Finding Displacement

A car starts from rest and accelerates at 2.50 m/s² for 8.00 s (same car as Problem 2). How far does it travel?

**Known:** v₀ = 0, a = 2.50 m/s², t = 8.00 s, x₀ = 0
**Unknown:** x

**Solution:** x = x₀ + v₀t + ½at² = 0 + 0 + ½(2.50)(8.00)² = ½(2.50)(64.0) = **80.0 m**

*Check:* Use Eq. 3: v² = v₀² + 2aΔx → (20.0)² = 0 + 2(2.50)Δx → 400 = 5.00Δx → Δx = 80.0 m ✓

---

## Problem 4 — Finding Acceleration (no time given)

A car traveling at 28.0 m/s brakes and stops in 95.0 m. What is the acceleration?

**Known:** v₀ = 28.0 m/s, v = 0 m/s, x₀ = 0, x = 95.0 m
**Unknown:** a (t not given, not needed)

**Equation:** v² = v₀² + 2a(x − x₀)

**Solution:** 0 = (28.0)² + 2a(95.0)
→ −784 = 190a
→ a = **−4.13 m/s²**

Negative sign: deceleration (opposing motion in +x direction). ✓

---

## Problem 5 — Finding Time

A motorcycle accelerates from 10.0 m/s to 25.0 m/s at 3.00 m/s². How long does this take?

**Known:** v₀ = 10.0 m/s, v = 25.0 m/s, a = 3.00 m/s²
**Unknown:** t

**Equation:** v = v₀ + at

**Solution:** 25.0 = 10.0 + 3.00t
→ 15.0 = 3.00t
→ t = **5.00 s**

---

## Problem 6 — Two-Stage Problem

A car is traveling at 15.0 m/s. The driver sees a dog 40.0 m ahead and reacts for 0.500 s (constant velocity during reaction), then brakes at 7.00 m/s².

**(a)** How far does the car travel during the reaction time?

**(b)** How far does the car travel while braking?

**(c)** Does the car stop before reaching the dog?

**Stage 1 (reaction, constant velocity):**
x₁ = v₀t = (15.0)(0.500) = 7.50 m

**Stage 2 (braking, a = −7.00 m/s²):**
v₀₂ = 15.0 m/s, v = 0, a = −7.00 m/s²

v² = v₀² + 2aΔx₂
0 = (15.0)² + 2(−7.00)Δx₂
0 = 225 − 14.0 Δx₂
Δx₂ = 225/14.0 = **16.1 m**

**Total:** 7.50 + 16.1 = 23.6 m < 40.0 m → **Yes, the car stops with 16.4 m to spare.**

---

## Mastery Signal

Chris can solve Problems 4–6 without looking at the kinematic equation table, identify the correct equation immediately from the given/unknown list, and apply correct signs throughout.
