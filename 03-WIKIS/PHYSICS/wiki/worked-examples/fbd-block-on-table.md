---
type: worked-example
status: draft
---

# Worked Example — Block on Table with Applied Force and Friction

## Problem

A 5.0 kg block sits on a horizontal table with μ_s = 0.45 and μ_k = 0.30. A horizontal force of 18 N is applied to the right. Find: (a) Does the block move? (b) If it moves, find its acceleration. (g = 9.80 m/s²)

## Physical Situation

Block on a flat horizontal surface. Forces: weight (down), normal (up), applied force (right), friction (opposes motion or tendency — left).

## Step 1: Free Body Diagram

```
         n (upward)
         ^
         |
f ← [block] → F = 18 N
         |
         v
        mg = 49 N
```

## Step 2: Find the Normal Force

$$\sum F_y = n - mg = 0$$
$$n = mg = 5.0 \times 9.80 = 49 \text{ N}$$

## Step 3: Check Static Friction

Maximum static friction:
$$f_{s,\text{max}} = \mu_s \cdot n = 0.45 \times 49 = 22.1 \text{ N}$$

Applied force = 18 N < 22.1 N (maximum static friction).

**Answer (a): The block does NOT move.**

The static friction adjusts to exactly 18 N (leftward) to maintain equilibrium. The block stays stationary.

---

## Part (b): Modified Problem — Applied Force = 30 N

If the applied force is 30 N instead:

30 N > 22.1 N (maximum static friction) → **block slides (kinetic friction takes over).**

Kinetic friction:
$$f_k = \mu_k \cdot n = 0.30 \times 49 = 14.7 \text{ N}$$

Newton's Second Law (x-direction):
$$\sum F_x = F - f_k = ma$$
$$30 - 14.7 = 5.0 \times a$$
$$a = \frac{15.3}{5.0} = 3.06 \text{ m/s}^2 \quad \text{(to the right)}$$

## Step 4: Unit Check

Force: N = kg·m/s² ✓
Acceleration: 3.06 m/s² ✓ (reasonable — less than g, more than zero)

## Step 5: Sanity Check

If there were no friction: a = 30/5 = 6.0 m/s². With friction opposing, we get 3.06 m/s² — less, as expected. ✓

## Key Insight

Static friction adjusts to match the applied force, up to its maximum. Once exceeded, the block begins moving and kinetic friction (smaller) takes over. That's why it's harder to start sliding something than to keep it sliding.

## Stage Reference

[[../stages/stage-5-laws-of-motion]] — [[../problem-types/friction-problems]] — [[../problem-types/fbd-single-object]]
