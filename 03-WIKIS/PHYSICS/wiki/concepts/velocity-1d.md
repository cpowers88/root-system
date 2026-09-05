---
type: concept
timeline: reference
status: draft
---

# Velocity (1D)

## What is the physical idea?

Velocity describes how fast an object's position is changing, and in which direction. In one dimension, the direction is captured by the sign: positive velocity means moving in the +x direction; negative means moving in the −x direction.

There are two versions:
- **Average velocity** — a single rate over a time interval
- **Instantaneous velocity** — the rate at one specific instant (the calculus definition)

## What real-world situation does it describe?

A car's speedometer shows speed (magnitude of velocity). If the car moves north at 25 m/s, its velocity is +25 m/s (taking north as positive). If it reverses, velocity becomes −25 m/s — same speed, opposite direction.

## Objects / System Involved

Any object in one-dimensional motion (or analyzed one dimension at a time).

## Quantities That Change

Velocity itself can change with time. When velocity changes, the object has acceleration (Stage 2 concept). If velocity is constant, acceleration is zero.

## Model or Equation

**Average velocity** over a time interval from t₀ to t_f:

```
v_avg = Δx / Δt = (x_f − x₀) / (t_f − t₀)
```

**Instantaneous velocity** at one moment:

```
v = dx/dt    (derivative of position with respect to time)
```

In plain English: instantaneous velocity is the slope of the x-t graph at a single point.

**Speed** = |v| — the magnitude of velocity, always positive or zero.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| v | instantaneous velocity | m/s |
| v_avg | average velocity | m/s |
| v₀ | initial velocity | m/s |
| Δx | displacement | m |
| Δt | time interval | s |

## Calculus Connection

- Instantaneous velocity is defined as the derivative: v = dx/dt
- Graphically: velocity is the slope of the tangent line to the x-t curve at a given point
- Reverse: if you know v(t), integrate to get position: x = x₀ + ∫v dt

For constant velocity, v = const, so x(t) = x₀ + v·t — a straight line on the x-t graph.

## Diagram / Visual Model

**x-t graph:** the slope at each point is the velocity at that moment.

```
x (m)
|         /  ← steep slope = high velocity
|        /
|   ____/   ← flat = zero velocity (object stopped)
|  /
| /   ← shallow slope = low velocity
+————————→ t (s)
```

If the x-t curve bends upward, velocity is increasing (positive acceleration). If it flattens, velocity is decreasing.

**v-t graph:** velocity is plotted directly. A horizontal line = constant velocity.

## Problem Types That Use This

- [[../problem-types/constant-velocity]]
- [[../problem-types/constant-acceleration]]
- [[../problem-types/motion-graphs]]

## Common Beginner Mistake

Confusing velocity (a vector — has sign, direction) with speed (a scalar — always positive).

If a car moves 30 m/s to the left and you say "velocity = 30 m/s," you've described speed, not velocity. Velocity is −30 m/s (if left is negative x).

## Practice Next

Move to [[acceleration-1d]] — acceleration is to velocity what velocity is to position (another derivative).

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 2.2–2.3, pp. 25–31.
