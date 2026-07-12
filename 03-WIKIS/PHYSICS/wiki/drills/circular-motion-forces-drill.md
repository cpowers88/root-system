---
type: drill
status: draft
---

# Circular Motion Forces Drill

## Skill Being Practiced

Applying ΣF_inward = mv²/r to horizontal and vertical circular motion problems.

## Prerequisites

[[../concepts/centripetal-force]], [[../concepts/vertical-circular-motion]], [[../equations/centripetal-force]]

## Instructions

For each problem: (1) draw the FBD and label all forces, (2) write Newton's 2nd law in the inward direction, (3) solve for the unknown, (4) check units.

---

## Problem 1 — Ball on a Horizontal String

A 0.50 kg ball is tied to a 1.2 m string and swings in a horizontal circle. The ball's speed is 3.6 m/s. Find the tension in the string.

**Solution:**
```
Inward direction: toward center of circle.
Only force with an inward component: tension T.
ΣF_inward = T = mv²/r
T = (0.50)(3.6²)/(1.2) = (0.50)(12.96)/1.2 = 5.4 N
```

---

## Problem 2 — Car on a Flat Curve

A 1200 kg car rounds a flat curve of radius 55 m. The coefficient of static friction between tires and road is μ_s = 0.75. What is the maximum safe speed?

**Solution:**
```
Inward direction: horizontal, toward center of curve.
Real force providing centripetal force: static friction f_s.
f_s = mv²/r  and  f_s,max = μ_s mg
Set f_s = f_s,max:
μ_s mg = mv²_max/r   (mass cancels!)
v_max = √(μ_s g r) = √(0.75 × 9.80 × 55) = √(404) = 20 m/s ≈ 72 km/h
```

---

## Problem 3 — Banked Curve (No Friction)

A highway curve of radius 200 m is banked at an angle θ. At what angle should it be banked for a design speed of 25 m/s?

**Solution:**
```
FBD: Normal force n at angle θ from vertical.
Vertical: n cos θ = mg
Horizontal (inward): n sin θ = mv²/r
Divide: tan θ = v²/(rg) = (25²)/(200 × 9.80) = 625/1960 = 0.319
θ = tan⁻¹(0.319) = 17.7°
```

---

## Problem 4 — Top of a Vertical Circle

A 0.20 kg ball on a 0.80 m string is swung in a vertical circle. At the top of the circle, its speed is 4.0 m/s. Find the tension.

**Solution:**
```
At the top: both T and mg point inward (downward).
T + mg = mv²/r
T = mv²/r - mg = (0.20)(16)/(0.80) - (0.20)(9.80)
T = 4.0 - 1.96 = 2.0 N
```

---

## Problem 5 — Bottom of a Vertical Circle

For the same ball at the bottom of the circle at 4.0 m/s, find the tension.

**Solution:**
```
At the bottom: T points inward (up), mg points outward (down).
T - mg = mv²/r
T = mv²/r + mg = 4.0 + 1.96 = 5.96 N ≈ 6.0 N
Note: T_bottom > T_top — the string is most likely to break at the bottom.
```

---

## Problem 6 — Minimum Speed at Top

What is the minimum speed at the top of the vertical circle (r = 0.80 m) for the string to remain taut?

**Solution:**
```
At minimum speed, T = 0:
0 + mg = mv²_min/r   →   v_min = √(gr)
v_min = √(9.80 × 0.80) = √7.84 = 2.8 m/s
```

---

## Mastery Signal

Chris can draw a correct FBD for any circular motion geometry (horizontal, top of loop, bottom of loop), correctly label which forces are inward and which are outward, and solve for unknowns in under 4 minutes per problem.
