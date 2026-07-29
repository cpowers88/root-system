---
type: concept
timeline: reference
status: draft
---

# Acceleration (1D)

## What is the physical idea?

Acceleration is the rate at which velocity changes with time. It is the answer to: "how quickly is the object speeding up, slowing down, or changing direction?"

Key insight: an object can be moving fast but not accelerating (constant velocity), or barely moving but accelerating strongly (just launched from rest). Acceleration and velocity are independent quantities.

## What real-world situation does it describe?

- A car pressing the gas pedal: velocity increases → positive acceleration (in the direction of motion)
- A car braking: velocity decreases → acceleration is opposite to direction of motion
- A ball thrown upward: while in the air, a = −9.80 m/s² the entire time — downward, even at the top when v = 0

## Objects / System Involved

Any object that has a changing velocity. No changing velocity → no acceleration.

## Quantities That Change

Acceleration itself can vary over time, but in most Stage 2 problems, acceleration is **constant**. The kinematic equations are only valid for constant acceleration.

## Model or Equation

**Average acceleration** over a time interval:

```
a_avg = Δv / Δt = (v_f − v₀) / (t_f − t₀)
```

**Instantaneous acceleration:**

```
a = dv/dt = d²x/dt²
```

In plain English: acceleration is the slope of the v-t graph at a single point.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| a | acceleration | m/s² |
| a_avg | average acceleration | m/s² |
| Δv | change in velocity | m/s |
| Δt | time interval | s |

Dimensional check: [a] = (m/s)/s = m/s² = L/T². ✓

## Calculus Connection

- a = dv/dt (first derivative of velocity)
- a = d²x/dt² (second derivative of position)
- Reverse: integrate constant acceleration to get velocity: v(t) = v₀ + ∫a dt = v₀ + at
- Integrate again to get position: x(t) = x₀ + v₀t + ½at²

These are the kinematic equations, derived directly from integration.

## Diagram / Visual Model

**v-t graph:** the slope at each point is the acceleration.

```
v (m/s)
|       /
|      /   ← positive slope = positive acceleration (speeding up in +x)
|     /
|    /
|___/
+————————→ t (s)
```

A negative slope on the v-t graph = negative acceleration. The object could still be moving in the positive direction — it's just slowing down.

**a-t graph:** for constant acceleration, this is a horizontal line.

```
a (m/s²)
|————————————  ← constant acceleration
+————————→ t (s)
```

Area under the a-t graph = change in velocity.

## Problem Types That Use This

- [[../problem-types/constant-acceleration]]
- [[../problem-types/free-fall]]
- [[../problem-types/motion-graphs]]

## Critical Distinction: Sign of Acceleration vs. Speeding/Slowing

| v sign | a sign | What happens |
|---|---|---|
| + | + | Moving in +x, speeding up |
| + | − | Moving in +x, slowing down |
| − | − | Moving in −x, speeding up (in that direction) |
| − | + | Moving in −x, slowing down |

**Slowing down = acceleration opposite to velocity direction.** "Deceleration" is not a physics term — use "acceleration in the direction opposite to motion."

## Common Beginner Mistake

Thinking acceleration is zero at the highest point of a thrown object. At the top, v = 0 but a = −9.80 m/s². The ball is still under gravity — it's just momentarily stationary. A = 0 would mean no net force, which is not the case.

## Practice Next

Move to [[free-fall]] — a specific case of constant acceleration where a = −9.80 m/s².

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 2.4–2.5, pp. 32–39.
