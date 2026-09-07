---
type: problem-type
timeline: reference
status: draft
---

# Problem Type — Inclined Plane

## How to Recognize It

An object on a slope (ramp, incline) at angle θ. The problem asks for acceleration along the slope, the normal force, the required tension to pull something up the ramp, or whether the object slides.

**Keywords:** "inclined at angle θ," "ramp," "slope," "block slides down," "force to pull up the incline."

## Given Information

- Angle of incline θ
- Mass of object m
- Coefficient of friction (μ_s or μ_k if friction is involved)
- Applied force (if any — tension, push, pull)
- Whether object is moving or stationary

## Unknown Requested

- Acceleration (up or down the slope)
- Normal force n
- Required force to hold stationary or to pull at constant speed or given acceleration
- Whether object slides (compare mg sinθ to max static friction)

## Diagram

Tilt your coordinate system: set +x along the slope (positive = up-slope or down-slope, your choice), +y perpendicular to slope.

```
         ^ +y (perpendicular to slope)
         |
       [block]---> +x (along slope, up-slope positive)
        /  \
       /    \
      / θ    \
     /________\

Weight decomposition (weight points straight down):
  Component along slope:     w_∥ = mg sinθ  (down the slope)
  Component perp to slope:   w_⊥ = mg cosθ  (into the surface)
```

## Equations

**Perpendicular axis (usually no acceleration perpendicular to slope):**
$$\sum F_y = n - mg\cos\theta = 0 \quad \Rightarrow \quad n = mg\cos\theta$$

**Along slope (up = positive):**
$$\sum F_x = F_{\text{up}} - mg\sin\theta - f_k = ma$$

Where f_k = μ_k n = μ_k mg cosθ (if kinetic friction), and F_up is any applied force up the slope (0 if none).

## Solving Pattern

1. Draw FBD with tilted axes.
2. Decompose weight: mg sinθ (along slope, downward) and mg cosθ (perpendicular, into slope).
3. Apply ΣF_perp = 0 → find n = mg cosθ.
4. Compute friction (if any): f = μ × n.
5. Apply ΣF_along = ma → solve for a (or the unknown force).
6. Check direction: if a is negative with "up = positive" chosen, the object accelerates downhill.

## Frictionless Shortcut

For frictionless incline, the only along-slope force is gravity's component:

$$a = g\sin\theta \quad \text{(down the slope)}$$

## Unit Check

n should be in N (less than mg for any θ > 0). Acceleration in m/s². Friction force in N (must be less than n for μ < 1).

## Traps

- Using mg instead of mg cosθ for the normal force (the most common inclined-plane error).
- Forgetting that friction acts up the slope when the object slides down, and down the slope when the object is being pushed up.
- Using the wrong angle: θ is measured from the horizontal. sin and cos may switch if you define θ from the vertical.
- Assuming the block slides (kinetic friction) without first checking if it slides (static friction check).

## Drills

[[../drills/inclined-plane-drill]], [[../drills/friction-problems-drill]] (Problems 3, 4)
