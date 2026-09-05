---
type: concept
timeline: reference
status: draft
---

# Work

## What it is

Work is the energy transferred to or from an object by a force acting through a displacement. Work is a scalar — it has magnitude and sign, but no direction.

## Real-world physical situation

You push a box across the floor. Your force does positive work — energy flows from you into the box's motion. Friction does negative work — energy flows out of the box (into thermal energy). The normal force does zero work — it's perpendicular to the motion.

## Objects and system

Work is done *by* a specific force *on* a specific object. Always name both.

## Quantities involved

- Force F (N) — the agent doing work
- Displacement d (m) — the distance the object moves while the force acts
- Angle θ — between the force vector and the displacement vector

## Equation

For a constant force:

```text
W = F d cos θ
```

For a force that varies with position (like a spring):

```text
W = ∫(x_i → x_f) F_x dx
```

Unit: joule (J = N·m = kg·m²/s²)

## Why this equation applies

Only the component of force *parallel* to the displacement does work. The component perpendicular to displacement causes no energy transfer. F cos θ extracts that parallel component.

## Calculus connection

When force varies with position, we can't use a single F. Instead we add up infinitesimal contributions: dW = F_x dx, and the total work is ∫F_x dx. Graphically, this is the area under the F-x curve.

## Diagram

```
         F
          \   θ
           \
            \→ d (displacement)

W = F d cos θ   (component of F along d times d)
```

## Problem type

See [[../problem-types/work-calculation]].

## Beginner mistake

Assuming any force that acts on an object does work on it. A force only does work if there is a displacement component along the force's direction. A wall being pushed doesn't move → zero work. A person carrying a box horizontally → gravity does zero work (perpendicular). Normal force → always zero work on level ground.

## What to practice next

- Work calculation drill: [[../drills/work-calculation-drill]]
- Then work-energy theorem: [[../equations/work-energy-theorem]]
