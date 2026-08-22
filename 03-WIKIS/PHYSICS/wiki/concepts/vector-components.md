---
type: concept
timeline: reference
status: draft
---

# Concept — Vector Components

## What it is

A **component** is the projection of a vector onto a coordinate axis. Every 2D vector can be broken into an x-component and a y-component using trigonometry. The two components together carry exactly the same information as the original vector — neither more nor less.

## Physical anchor

Imagine walking from your starting point to a destination that is 5.0 km to the northeast (45° above east). You could also reach the exact same point by walking 3.54 km east, then turning and walking 3.54 km north. Those two legs are the x and y components of your displacement vector.

## The decomposition diagram

Always draw this before plugging into formulas:

```
        ^ y
        |
        |  /  A (magnitude A, at angle θ)
        | /
        |/ θ
   -----+--------------> x
```

- Horizontal leg (x-component): Ax = A cos θ
- Vertical leg (y-component): Ay = A sin θ
- Reconstruction: A = √(Ax² + Ay²), θ = tan⁻¹(Ay/Ax)

θ is always measured counterclockwise from the positive x-axis unless stated otherwise.

## Why components work

Because the x and y axes are perpendicular, the x- and y-components are independent of each other. This independence is the key that makes projectile motion solvable (Stage 4): horizontal and vertical motions obey the same kinematic equations, but they run in parallel without affecting each other.

## Unit vectors

The unit vectors î (pronounced "i-hat"), ĵ ("j-hat"), and k̂ ("k-hat") point in the +x, +y, and +z directions respectively. Each has magnitude 1 and no units — they are just direction markers.

Any vector can be written: **A⃗ = Ax î + Ay ĵ** (in 2D) or **A⃗ = Ax î + Ay ĵ + Az k̂** (in 3D).

This notation makes addition transparent: just add like terms.

## Depends on

[[../concepts/scalar-vs-vector]], trigonometry (Appendix math-geometry-trig)

## Unlocks

Vector addition, projectile motion (Stage 4), Newton's 2nd law in 2D (Stage 5), work via dot product (Stage 7).

## Common Mistake

Swapping sin and cos — forgetting that cos belongs with the axis the angle is measured FROM. If the angle is from the +x axis, cos goes with x and sin goes with y. Sketch the right triangle every time.
