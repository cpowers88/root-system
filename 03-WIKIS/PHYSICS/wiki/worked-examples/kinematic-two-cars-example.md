---
type: worked-example
timeline: reference
status: draft
---

# Two Cars on a Highway (Kinematic Equations Worked Example)

## Problem Statement

Car A is traveling at a constant 25.0 m/s on a highway. Car B is initially at rest at a gas station 50.0 m ahead of Car A. At the moment Car A passes a reference post, Car B pulls onto the highway and accelerates at 2.00 m/s².

**(a)** How long does it take for Car A to catch Car B?

**(b)** How far has Car A traveled when it catches Car B?

**(c)** What is Car B's speed when Car A catches it?

## Problem Type

[[../problem-types/constant-velocity]] (Car A) combined with [[../problem-types/constant-acceleration]] (Car B). Two-object meeting problem.

## Given

- Car A: v_A = 25.0 m/s (constant), x_A0 = 0
- Car B: v_B0 = 0 (starts from rest), a_B = 2.00 m/s², x_B0 = 50.0 m (already 50 m ahead)

## Unknown

(a) t when x_A = x_B
(b) x at that moment
(c) v_B at that moment

## Diagram

```
Reference post           Gas station (Car B's start)
     |                           |
     0 ———————————————————————— 50 m ——————————————→ +x
     ↑                           ↑
   Car A (t=0)               Car B (t=0)
   v_A = 25.0 m/s            v_B = 0, a = 2.00 m/s²
```

Positive direction: to the right (+x).

## Model / Equation Choice

Write position as a function of time for each car, then set equal.

Car A (constant velocity): x_A = x_A0 + v_A · t = 0 + 25.0t

Car B (constant acceleration): x_B = x_B0 + v_B0 · t + ½ a_B t² = 50.0 + 0 + ½(2.00)t² = 50.0 + t²

## Solution Steps

### Part (a): When does Car A catch Car B?

Set x_A = x_B:

```
25.0t = 50.0 + t²
```

Rearrange to standard quadratic form:

```
t² − 25.0t + 50.0 = 0
```

Apply the quadratic formula (a = 1, b = −25.0, c = 50.0):

```
t = [25.0 ± √(625 − 200)] / 2
  = [25.0 ± √425] / 2
  = [25.0 ± 20.6] / 2
```

Two solutions:
- t₁ = (25.0 − 20.6)/2 = 4.40/2 = **2.20 s**
- t₂ = (25.0 + 20.6)/2 = 45.6/2 = **22.8 s**

**Which root?** t₁ = 2.20 s: at this moment, x_A = 25.0 × 2.20 = 55.0 m and x_B = 50.0 + (2.20)² = 54.8 m ≈ 55 m. ✓ They meet.

t₂ = 22.8 s gives a second crossing later — Car B accelerates past Car A after t₁, but Car A catches it again. Both are valid physics; the problem asks for the first catch.

**Answer: t = 2.20 s** (first encounter)

### Part (b): Position at catch

```
x_A = 25.0 × 2.20 = 55.0 m
```

**Car A has traveled 55.0 m from the reference post.**

### Part (c): Car B's speed

```
v_B = v_B0 + a_B · t = 0 + (2.00)(2.20) = 4.40 m/s
```

Car B is still slower than Car A (25.0 m/s) at this moment — which is why Car A catches it.

## Units Check

- [x_A] = (m/s)(s) = m ✓
- [x_B] = m + (m/s²)(s²) = m ✓
- [v_B] = (m/s²)(s) = m/s ✓

## Final Answers

(a) t = **2.20 s**
(b) x = **55.0 m** from the reference post
(c) v_B = **4.40 m/s**

## Explain-Back Prompt

Close the page and answer these without looking:
1. Why did we set x_A = x_B rather than Δx = 0?
2. Why did the quadratic give two answers? What does each root mean physically?
3. If Car B's acceleration were larger, would Car A catch it faster or slower?

## Common Trap

Forgetting that Car B starts at x = +50.0 m, not x = 0. Students who set x_B0 = 0 get the wrong answer. The 50.0 m head start must appear in Car B's position equation.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 2, Example-style problem; see also Example 2.7–2.9, pp. 41–47.
