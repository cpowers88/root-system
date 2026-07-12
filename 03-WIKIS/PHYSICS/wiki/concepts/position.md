---
type: concept
status: draft
---

# Position

## What is the physical idea?

Position is the location of an object along a number line relative to a chosen reference point called the **origin**. In one dimension it is a single number — positive or negative depending on which side of the origin the object is on.

## What real-world situation does it describe?

A car at mile marker 42 on a highway. A ball sitting 3 m to the left of a wall. A runner at the 100 m mark on a track. All of these are positions — a location, measured from some agreed-upon zero.

## Objects / System Involved

Any single object whose internal structure we can ignore (particle model). Position describes where the particle is, not how it got there or how fast it's moving.

## Quantities That Change

Position changes with time whenever the object moves. The function x(t) — position as a function of time — is the core description of motion in this chapter.

## Model or Equation

No single equation. Position is defined as a coordinate:

```
x = (distance from origin)(with sign for direction)
```

Typical convention: rightward or upward is positive (+x); leftward or downward is negative (−x).

You choose the origin and the positive direction. Once chosen, stick to them for the entire problem.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| x | position along x-axis | m |
| x₀ or xᵢ | initial position | m |
| x_f | final position | m |

## Calculus Connection

Position x(t) is the function from which everything else in kinematics is derived.

- Take the first derivative → velocity: v = dx/dt
- Take the second derivative → acceleration: a = d²x/dt²

If you are given v(t), integrate to recover x(t): x = ∫v dt + x₀.

## Diagram / Visual Model

Draw a number line (your x-axis). Mark the origin (x = 0). Then a single dot on the line represents the object at one instant. As time passes, the dot moves along the line — that's 1D motion.

```
      x₀          x_f
← − − | − − − − − • − − − − − → +x
       origin
(object started at x₀, is now at x_f)
```

## Problem Types That Use This

- [[../problem-types/constant-velocity]]
- [[../problem-types/constant-acceleration]]
- [[../problem-types/free-fall]]
- [[../problem-types/motion-graphs]]

## Common Beginner Mistake

Forgetting that position is measured from the **origin**, not from the object's previous location. If an object moves from x = 5 m to x = 2 m, its position is now 2 m — its displacement is −3 m. These are different numbers.

## Practice Next

Once you understand position, move to [[displacement-vs-distance]] — the distinction between where you ended up versus how far you traveled.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 2.1, pp. 22–24.
