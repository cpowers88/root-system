---
type: problem-type
status: draft
---

# Horizontal Circular Motion Problems

## How to Recognize This Problem Type

- Object moves in a horizontal circle (or a circle in a horizontal plane).
- Usually involves one of: ball on a string, car rounding a flat curve, car on a banked curve, coin on a turntable.
- Asked to find: tension, speed, friction force, radius, maximum speed, or banking angle.

## Given Information Usually Includes

- Mass m of object
- Speed v or radius r (sometimes both, sometimes one is the unknown)
- One of: string length (= r), coefficient of friction, banking angle θ

## Unknown Usually Asked For

Tension T, normal force n, friction force f, maximum safe speed, or minimum radius.

## Diagram

Draw a top-down view showing the object moving in a circle. Then draw a side-view or front-view FBD showing all forces. The key question: which direction is "inward" for this specific setup?

**Ball on string (horizontal plane):**
```
Top view:   object → (moving tangent)
            ←—— T (inward, toward center)

FBD: T acts inward. If perfectly horizontal, mg is balanced by normal in vertical (or ignored in idealized case).
```

**Car on flat curve:**
```
FBD: static friction f_s acts inward (toward center of curve).
n acts upward, mg acts downward.
Vertical: n = mg
Horizontal: f_s = mv²/r ≤ μ_s mg
```

**Car on banked curve (no friction):**
```
FBD: Normal force n at angle θ from vertical.
n cos θ = mg   (vertical balance)
n sin θ = mv²/r (horizontal = centripetal)
Divide: tan θ = v²/(rg)
```

## Equations Used

**Ball on string (horizontal, tension is only centripetal force):**
```
T = mv²/r
```

**Flat curve, max speed:**
```
f_s = mv²/r  and  f_s,max = μ_s mg
→ v_max = √(μ_s g r)
```

**Banked curve (no friction):**
```
tan θ = v²/(rg)
```

**General (set up FBD, sum inward):**
```
ΣF_inward = mv²/r
```

## Solving Pattern

1. Draw FBD. Label every real force: weight mg downward, normal force n perpendicular to surface, tension or friction as applicable.
2. Choose axes: inward (toward center) and perpendicular to inward.
3. Write Newton's 2nd law in inward direction: ΣF_inward = mv²/r.
4. Write Newton's 2nd law in vertical (or perpendicular) direction: ΣF = 0 (if no vertical acceleration).
5. Solve the system for the unknown.

## Unit Checks

v in m/s, r in m, m in kg: mv²/r → kg·(m/s)²/m = kg·m/s² = N ✓

## Traps

- **Using the string length as the radius for a conical pendulum (ball on string swinging in a tilted cone).** The radius of the circle is r = L sin θ, not L, where L is string length and θ is the angle from vertical.
- **For a flat curve, maximum speed, not the actual speed, is what friction sets.** The problem asks for maximum speed; at lower speeds, less friction is needed.
- **Banked curve with no friction: only one specific speed works.** Too fast or too slow and you need friction to maintain the curve.

## Drills

[[../drills/circular-motion-forces-drill]]
