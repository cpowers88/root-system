---
type: concept
status: draft
---

# Free Fall

## What is the physical idea?

Free fall is a special case of constant-acceleration motion in which the only force acting on an object is gravity, and air resistance is negligible. Under these conditions, every object — regardless of mass — falls with the same acceleration: 9.80 m/s² downward.

This is a model. Real objects have air resistance, so free fall is approximate. But for a rock, ball, or person (on the way down), the approximation is excellent for most problems.

## What real-world situation does it describe?

- A ball dropped from a window
- A baseball thrown upward (the entire flight, not just on the way down)
- A stone launched horizontally off a cliff (vertical component only)
- An object tossed in any direction — the vertical component behaves as free fall

Key insight: the object is in free fall the entire time it is in the air, not just on the way down. A ball thrown upward is in free fall the instant it leaves your hand.

## Objects / System Involved

Any object in the air with negligible air resistance. Applies to the object as a system; Earth's gravity is the external influence.

## Quantities That Change

Position (y, taken as vertical) changes with time. Velocity changes at a constant rate. Acceleration is constant throughout.

## Model or Equation

Use the kinematic equations with:

```
a = −g = −9.80 m/s²   (taking upward as positive)
```

The five kinematic equations become (replacing x with y and a with −g):

```
1. v = v₀ − gt
2. y = y₀ + v₀t − ½gt²
3. v² = v₀² − 2g(y − y₀)
4. y = y₀ + ½(v₀ + v)t
```

**Convention:** positive direction = upward. This makes g positive (9.80 m/s²) and the acceleration term −g (downward).

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| y | vertical position | m |
| y₀ | initial vertical position | m |
| v | vertical velocity | m/s |
| v₀ | initial vertical velocity | m/s |
| g | free-fall acceleration magnitude | 9.80 m/s² |
| a | acceleration (= −g if up is positive) | −9.80 m/s² |
| t | time | s |

## Calculus Connection

Same as the general kinematic case — integrate constant a = −g:

```
v(t) = v₀ + at = v₀ − gt
y(t) = y₀ + v₀t + ½at² = y₀ + v₀t − ½gt²
```

## Diagram / Visual Model

Object thrown upward from y₀ = 0 with initial velocity v₀:

```
y
|       *       ← highest point: v = 0, a = −g (still!)
|     *   *
|   *       *
|  *         *
| *           *
|*             *
+———————————————→ t
```

The path is a parabola in y vs. t. The velocity-time graph is a straight line with slope −9.80 m/s².

```
v
|v₀
|  \
|   \       ← slope = −g throughout
|    \
|     \ 0 ← crosses zero at the top
|      \
|       \−v₀ (same magnitude on return if same height)
+————————→ t
```

## Key Fact: Symmetry of Free Fall

If an object is thrown upward from a height and returns to the same height:
- Time going up = time coming down
- Speed when it returns = speed when it was thrown (same magnitude, opposite sign)

## Problem Types That Use This

- [[../problem-types/free-fall]]
- [[../problem-types/constant-acceleration]]

## Common Beginner Mistakes

1. **Saying acceleration = 0 at the top.** Wrong. v = 0 at the top, but a = −9.80 m/s² the whole time.
2. **Using g = +9.80 m/s² for a when taking upward as positive.** Always use a = −g when up is positive.
3. **Thinking heavier objects fall faster.** In free fall (no air resistance), all objects fall identically. Mass cancels out of the equations.
4. **Forgetting the initial velocity for objects thrown, not dropped.** Dropped → v₀ = 0. Thrown → v₀ ≠ 0.

## Practice Next

Solve the free-fall drills: [[../drills/free-fall-drill]]. Then attempt the [[../problem-types/free-fall]] recognizer.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 2.7, pp. 44–49.
