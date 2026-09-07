---
type: drill
timeline: reference
status: draft
---

# Terminal Velocity Drill

## Skill Being Practiced

Calculating terminal velocity using the quadratic drag model. Interpreting what happens physically as an object approaches v_t.

## Prerequisites

[[../concepts/terminal-velocity]], [[../equations/terminal-velocity]]

## Instructions

Set up Newton's 2nd law. At terminal velocity, net force = 0. Solve for v_t. Show all unit work.

---

## Problem 1 — Skydiver

A skydiver of mass 80 kg is in free fall in a spread-eagle position. D = 0.70, A = 0.70 m², ρ_air = 1.20 kg/m³.

(a) Calculate terminal velocity.
(b) What force does the air exert on the skydiver at terminal velocity?

**Solution:**
```
(a) v_t = √(2mg / DρA)
    v_t = √(2 × 80 × 9.80 / (0.70 × 1.20 × 0.70))
    v_t = √(1568 / 0.588)
    v_t = √(2666) ≈ 51.6 m/s ≈ 52 m/s (~186 km/h)

(b) At terminal velocity, drag = weight:
    R = mg = 80 × 9.80 = 784 N
```

---

## Problem 2 — Raindrop (Linear Drag)

A small raindrop of mass 3.4 × 10⁻⁵ kg falls at terminal velocity. The linear drag coefficient b = 2.5 × 10⁻⁴ kg/s.

(a) Find the terminal velocity.
(b) Is this physically reasonable for a raindrop?

**Solution:**
```
(a) Linear model: v_t = mg/b
    v_t = (3.4 × 10⁻⁵ × 9.80) / (2.5 × 10⁻⁴)
    v_t = (3.332 × 10⁻⁴) / (2.5 × 10⁻⁴)
    v_t = 1.33 m/s ≈ 1.3 m/s

(b) Yes — typical raindrop terminal velocity is 2–9 m/s depending on size.
    This small drop falls slowly, which is consistent.
```

---

## Problem 3 — Effect of Crouching

The skydiver from Problem 1 tucks into a ball (A = 0.18 m², D = 0.50). Find the new terminal velocity and compare to Problem 1.

**Solution:**
```
v_t = √(2 × 80 × 9.80 / (0.50 × 1.20 × 0.18))
    = √(1568 / 0.108)
    = √(14519)
    ≈ 120 m/s (~435 km/h)

Ratio: 120/52 ≈ 2.3×. Tucking more than doubles terminal velocity.
This is why skydivers can "fly" toward each other by adjusting their body position.
```

---

## Mastery Signal

Chris can set drag force equal to weight at terminal velocity, solve for v_t without a formula sheet, and correctly explain why a heavier object of the same shape has a higher terminal velocity.
