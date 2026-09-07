---
type: drill
timeline: reference
status: draft
---

# Projectile Motion Drill

## Skill Being Practiced

Setting up and solving projectile problems by separating x and y motion, applying kinematic equations in each direction independently.

## Prerequisites

[[../concepts/projectile-motion]], [[../equations/projectile-motion-equations]], [[../problem-types/projectile-horizontal-launch]], [[../problem-types/projectile-angled-launch]]

## Instructions

Draw a diagram for every problem. Label v₀ₓ, v₀ᵧ, and the coordinate system before writing any equation. Show all steps — do not jump to numbers until the algebra is set up with symbols.

---

## Problems

**Problem 1 — Horizontal launch from a cliff**
A ball rolls off a table 1.20 m high with a horizontal speed of 2.50 m/s. How far from the base of the table does it land?

**Problem 2 — Horizontal launch from height**
A package is dropped from a plane flying horizontally at 80.0 m/s at an altitude of 490 m. (a) How long does the package take to reach the ground? (b) How far horizontally does it travel during the fall?

**Problem 3 — Angled launch: max height and range**
A soccer ball is kicked at 20.0 m/s at an angle of 30.0° above the horizontal. Find: (a) maximum height, (b) time of flight, (c) range.

**Problem 4 — Angled launch: find time to reach a height**
A ball is launched at 15.0 m/s at 60.0° above horizontal. When is the ball at a height of 5.00 m? (There are two answers — find both and interpret each physically.)

**Problem 5 — Symmetric launch, find angle**
A projectile must travel a horizontal distance of 80.0 m and is launched at 30.0 m/s from ground level. Find the two launch angles that achieve this range.

**Problem 6 — Cliff with angled launch**
A ball is launched at 12.0 m/s at 25.0° above horizontal from the edge of a cliff 30.0 m above the ground. Find: (a) time of flight until it hits the ground, (b) horizontal range from the base of the cliff.

---

## Solutions

**Problem 1:**
```
Time to fall: 0 = 1.20 - ½(9.80)t²  →  t = √(2×1.20/9.80) = 0.495 s
Range: R = 2.50 × 0.495 = 1.24 m
```

**Problem 2:**
```
(a) 0 = 490 - ½(9.80)t²  →  t = √(2×490/9.80) = √(100) = 10.0 s
(b) R = 80.0 × 10.0 = 800 m
```

**Problem 3:**
```
v₀ₓ = 20.0 cos 30° = 17.3 m/s
v₀ᵧ = 20.0 sin 30° = 10.0 m/s

(a) h = v₀ᵧ²/(2g) = (10.0)²/(2×9.80) = 5.10 m
(b) t_flight = 2v₀ᵧ/g = 2(10.0)/9.80 = 2.04 s
(c) R = v₀ₓ × t = 17.3 × 2.04 = 35.3 m
    [Check: R = 20² sin 60°/9.80 = 400(0.866)/9.80 = 35.4 m ✓]
```

**Problem 4:**
```
v₀ₓ = 15 cos 60° = 7.50 m/s
v₀ᵧ = 15 sin 60° = 13.0 m/s
y equation: 5.00 = 13.0t - ½(9.80)t²
4.90t² - 13.0t + 5.00 = 0
t = [13.0 ± √(169 - 4(4.90)(5.00))] / (2×4.90)
  = [13.0 ± √(169 - 98.0)] / 9.80
  = [13.0 ± √71.0] / 9.80
  = [13.0 ± 8.43] / 9.80

t₁ = (13.0 - 8.43)/9.80 = 0.466 s  [on the way up]
t₂ = (13.0 + 8.43)/9.80 = 2.19 s   [on the way down]
```

**Problem 5:**
```
R = v₀² sin 2θ / g
sin 2θ = Rg/v₀² = (80.0)(9.80)/(30.0)² = 784/900 = 0.871
2θ = sin⁻¹(0.871) = 60.5°  →  θ₁ = 30.3°
Or 2θ = 180° - 60.5° = 119.5°  →  θ₂ = 59.8°
[Two complementary angles give the same range]
```

**Problem 6:**
```
v₀ₓ = 12.0 cos 25° = 10.9 m/s
v₀ᵧ = 12.0 sin 25° = 5.07 m/s

y: 0 = 30.0 + 5.07t - ½(9.80)t²
4.90t² - 5.07t - 30.0 = 0
t = [5.07 ± √(25.7 + 4(4.90)(30.0))] / (2×4.90)
  = [5.07 ± √(25.7 + 588)] / 9.80
  = [5.07 ± √613.7] / 9.80
  = [5.07 ± 24.77] / 9.80

Take positive root: t = (5.07 + 24.77)/9.80 = 3.04 s
R = 10.9 × 3.04 = 33.2 m
```

## Mastery Signal

Chris can set up the x and y equations independently, handle both horizontal-launch and angled-launch cases, and solve for any of: time, height, range, or landing velocity — without prompting for the equation setup.
