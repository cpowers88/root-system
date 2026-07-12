---
type: worked-example
status: draft
---

# Worked Example — Block Sliding Down an Inclined Plane with Friction

## Problem

A 3.0 kg block slides down a rough inclined plane that makes a 37° angle with the horizontal. The kinetic coefficient of friction is μ_k = 0.25. Find the acceleration of the block. (g = 9.80 m/s²; sin37° = 0.602, cos37° = 0.799)

## Physical Situation

Block moving down a slope. Forces: weight (straight down), normal force (perpendicular to slope, away from surface), kinetic friction (up the slope — opposes the downward motion).

## Step 1: Coordinate System

Set +x along the slope, pointing DOWN (the direction of motion). Set +y perpendicular to the slope, pointing AWAY from the surface.

## Step 2: Free Body Diagram

```
     +y ^  n
        |/
       [•]
      / |
     /  v
    /  mg sinθ (along slope, +x direction)
   /
  /θ  mg cosθ (perpendicular to slope, −y direction)
 /____
 
Also: f_k (friction, up the slope, −x direction)
```

Weight components:
- Along slope (+x): mg sinθ = 3.0 × 9.80 × 0.602 = **17.7 N** (down slope)
- Perpendicular (−y): mg cosθ = 3.0 × 9.80 × 0.799 = **23.5 N** (into surface)

## Step 3: Normal Force (from perpendicular axis)

$$\sum F_y = n - mg\cos\theta = 0$$
$$n = mg\cos\theta = 23.5 \text{ N}$$

## Step 4: Kinetic Friction

$$f_k = \mu_k \cdot n = 0.25 \times 23.5 = 5.88 \text{ N} \quad \text{(up the slope, −x direction)}$$

## Step 5: Newton's Second Law Along the Slope

$$\sum F_x = mg\sin\theta - f_k = ma$$
$$17.7 - 5.88 = 3.0 \times a$$
$$11.82 = 3.0a$$
$$a = 3.94 \text{ m/s}^2 \quad \text{(down the slope)}$$

## Step 6: Unit Check and Sanity Check

a = 3.94 m/s² — positive in the +x (down-slope) direction. ✓

If frictionless: a = g sinθ = 9.80 × 0.602 = 5.90 m/s². With friction, we get 3.94 m/s² — less, as expected. ✓

If friction were so large the block couldn't slide: a would be zero or negative (meaning the block wouldn't slide at all). Since a > 0, the block does slide. ✓

## Key Insight

The inclined-plane procedure is always:
1. Tilt the axes to align with the slope.
2. Decompose weight into sinθ (along) and cosθ (perpendicular).
3. Find n from the perpendicular equation.
4. Use n to find friction.
5. Apply Newton's 2nd Law along the slope.

The sinθ/cosθ decomposition is the critical step — never skip it.

## Stage Reference

[[../stages/stage-5-laws-of-motion]] — [[../problem-types/inclined-plane]] — [[../equations/kinetic-friction]]
