---
type: drill
status: draft
---

# Angular Momentum Drill

## Skill Being Practiced

Computing angular momentum, applying conservation of angular momentum, checking whether conservation applies.

## Prerequisites

[[../concepts/angular-momentum]], [[../concepts/conservation-of-angular-momentum]], [[../equations/angular-momentum]], [[../equations/conservation-angular-momentum]]

## Instructions

Work each problem fully. Show all steps: identify the system, check the condition for conservation, set up the equation, solve, and check units. Do not skip the condition check.

---

## Problems

**Problem 1 — Basic L calculation**

A solid disk of mass M = 5.0 kg and radius R = 0.40 m spins at ω = 8.0 rad/s about its central axis. Calculate its angular momentum L.

Use: I_disk = ½MR²

---

**Problem 2 — Skater (arms in)**

A figure skater rotates at ω_i = 1.5 rad/s with arms extended. Her moment of inertia in this position is I_i = 5.4 kg·m². She pulls her arms in, reducing her moment of inertia to I_f = 1.8 kg·m².

(a) What is her angular velocity after pulling her arms in?
(b) What is the ratio of final kinetic energy to initial kinetic energy? (Energy is not conserved — explain why it increased.)

---

**Problem 3 — Person on rotating platform**

A horizontal platform (I_platform = 200 kg·m², ω_i = 2.0 rad/s) has a 70 kg person standing at the rim at r = 2.5 m. The person walks to the center (r = 0). No external torque acts.

(a) Calculate I_total before and after.
(b) Find the final angular velocity of the platform.

---

**Problem 4 — Rotational collision**

A disk of moment of inertia I_disk = 3.0 kg·m² is spinning freely at ω_i = 10.0 rad/s. A second disk with I_2 = 1.5 kg·m², initially not rotating, is dropped onto the first and they stick together (friction between them couples them to the same ω). No external torque acts.

(a) Find the final angular velocity ω_f.
(b) Find the fraction of kinetic energy lost. Where did it go?

---

**Problem 5 — Particle angular momentum**

A 0.25 kg ball moves at 6.0 m/s in a straight line that passes at a perpendicular distance of 3.0 m from a fixed axis.

(a) Calculate the angular momentum of the ball about that axis.
(b) Explain why L is constant even though the ball moves in a straight line (no curved path).

---

## Solutions

**Problem 1:**
```
I = ½MR² = ½(5.0)(0.40²) = ½(5.0)(0.16) = 0.40 kg·m²
L = Iω = (0.40)(8.0) = 3.2 kg·m²/s
```

**Problem 2:**
```
(a) Conservation: I_i ω_i = I_f ω_f
    (5.4)(1.5) = (1.8)(ω_f)
    ω_f = 8.1/1.8 = 4.5 rad/s

(b) KE_i = ½I_i ω_i² = ½(5.4)(1.5²) = 6.075 J
    KE_f = ½I_f ω_f² = ½(1.8)(4.5²) = 18.225 J
    Ratio KE_f/KE_i = 18.225/6.075 = 3.0

    The skater's muscles did work pulling her arms in against centrifugal
    tendency — this internal work added kinetic energy to the system.
    Only L is conserved; KE is not.
```

**Problem 3:**
```
I_person,i = mr² = (70)(2.5²) = 437.5 kg·m²
I_total,i = 200 + 437.5 = 637.5 kg·m²

When person is at center (r = 0): I_person,f = 0
I_total,f = 200 + 0 = 200 kg·m²

Conservation: I_total,i × ω_i = I_total,f × ω_f
(637.5)(2.0) = (200)(ω_f)
ω_f = 1275/200 = 6.375 rad/s ≈ 6.4 rad/s
```

**Problem 4:**
```
(a) Conservation: I_disk ω_i + I_2 × 0 = (I_disk + I_2) ω_f
    (3.0)(10.0) = (3.0 + 1.5) ω_f
    ω_f = 30.0/4.5 = 6.67 rad/s

(b) KE_i = ½(3.0)(10.0²) = 150 J
    KE_f = ½(4.5)(6.67²) = ½(4.5)(44.5) = 100 J
    Fraction lost = (150 - 100)/150 = 50/150 = 1/3 ≈ 33%

    Energy was lost to friction between the disks as they
    coupled to a common angular velocity.
```

**Problem 5:**
```
(a) The perpendicular distance from the axis to the line of velocity is
    r⊥ = 3.0 m (given directly).
    L = mvr⊥ = (0.25)(6.0)(3.0) = 4.5 kg·m²/s

(b) No torque acts on the ball (it moves in a straight line — no force).
    Since τ = dL/dt = 0, L is constant. The perpendicular distance r⊥
    from the axis to the straight-line path is constant even as the ball
    moves, so mvr⊥ stays constant. This is a non-obvious result: a
    particle moving in a straight line has constant angular momentum about
    any off-axis point.
```

## Mastery Signal

Chris can solve Problems 1–3 independently in under 10 minutes each. Problem 4 (rotational collision) and Problem 5 (straight-line L) represent exam-level difficulty.
