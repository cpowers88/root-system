---
type: drill
timeline: reference
status: draft
---

# Motion Graphs Drill

## Skill Being Practiced

Reading velocity and acceleration from position-time graphs; reading displacement and acceleration from velocity-time graphs; and translating between graph types.

## Prerequisites

[[../concepts/velocity-1d]], [[../concepts/acceleration-1d]], [[../problem-types/motion-graphs]]

## Instructions

For each problem, describe what you see in the graph using the rules: slope = rate of change, area = accumulated quantity. No calculators needed — these are conceptual and small-number problems.

---

## Problem 1 — Reading a v-t Graph

An object's velocity vs. time is shown below (describe the graph from the data):

| Time (s) | Velocity (m/s) |
|---|---|
| 0 | 0 |
| 2 | 8 |
| 4 | 8 |
| 6 | 0 |

**(a)** What is the acceleration from t = 0 to t = 2 s?

**(b)** What is the acceleration from t = 2 to t = 4 s?

**(c)** What is the acceleration from t = 4 to t = 6 s?

**(d)** What is the total displacement from t = 0 to t = 6 s?

**Solutions:**

**(a)** a = Δv/Δt = (8 − 0)/(2 − 0) = **+4.0 m/s²** (speeding up)

**(b)** a = (8 − 8)/(4 − 2) = **0 m/s²** (constant velocity)

**(c)** a = (0 − 8)/(6 − 4) = **−4.0 m/s²** (slowing down)

**(d)** Total displacement = area under the v-t graph:
- Triangle (0 to 2 s): ½ × 2 × 8 = 8 m
- Rectangle (2 to 4 s): 2 × 8 = 16 m
- Triangle (4 to 6 s): ½ × 2 × 8 = 8 m
- Total = **32 m** (all positive; object never reversed)

---

## Problem 2 — Reading an x-t Graph

An object's position is described by the following data:

| Time (s) | Position (m) |
|---|---|
| 0 | 0 |
| 3 | 12 |
| 6 | 12 |
| 9 | 0 |

**(a)** What is the object's velocity from t = 0 to t = 3 s?

**(b)** What is the object's velocity from t = 3 to t = 6 s?

**(c)** What is the object's velocity from t = 6 to t = 9 s?

**(d)** What is the total displacement from t = 0 to t = 9 s?

**(e)** What is the total distance traveled?

**Solutions:**

**(a)** v = Δx/Δt = (12 − 0)/(3 − 0) = **+4.0 m/s**

**(b)** v = (12 − 12)/(6 − 3) = **0 m/s** (object at rest at x = 12 m)

**(c)** v = (0 − 12)/(9 − 6) = **−4.0 m/s** (object returned)

**(d)** Displacement: Δx = x_f − x₀ = 0 − 0 = **0 m**

**(e)** Distance: 12 m out + 12 m back = **24 m**

---

## Problem 3 — Sketch the v-t Graph

An object starts at rest at x = 0. It accelerates uniformly at +3.0 m/s² for 4 s, then moves at constant velocity for 3 s, then decelerates at −6.0 m/s² until it stops.

**(a)** What is the final velocity after the first 4 s?

**(b)** How long does the deceleration phase last?

**(c)** Sketch the v-t graph (describe it in words if you can't draw).

**Solutions:**

**(a)** v = v₀ + at = 0 + (3.0)(4) = **12 m/s**

**(b)** Deceleration from 12 m/s to 0 at −6.0 m/s²:
v = v₀ + at → 0 = 12 + (−6.0)t → t = **2.0 s**

**(c)** Description of v-t graph:
- t = 0 to 4 s: straight line rising from 0 to 12 m/s (slope = +3.0 m/s²)
- t = 4 to 7 s: horizontal line at v = 12 m/s (slope = 0)
- t = 7 to 9 s: straight line falling from 12 m/s to 0 (slope = −6.0 m/s²)

---

## Problem 4 — Acceleration from Curved x-t

The x-t data for an object are: (0 s, 0 m), (1 s, 2 m), (2 s, 8 m), (3 s, 18 m), (4 s, 32 m).

**(a)** Calculate the average velocity in each 1-second interval.

**(b)** Are these velocities constant or changing? What does that tell you about acceleration?

**(c)** Estimate the acceleration from the velocity data.

**Solutions:**

**(a)** Average velocities:
- 0→1 s: Δx/Δt = 2/1 = 2 m/s
- 1→2 s: (8−2)/1 = 6 m/s
- 2→3 s: (18−8)/1 = 10 m/s
- 3→4 s: (32−18)/1 = 14 m/s

**(b)** Velocities are increasing by 4 m/s per second → **acceleration is constant (not zero).**

**(c)** a ≈ Δv/Δt = (6−2)/1 = **4 m/s²** (same for every interval → confirms constant acceleration)

Check: x = ½at² → 32 = ½(4)(4²) = ½(4)(16) = 32 ✓

---

## Mastery Signal

Chris can extract velocity from any x-t segment by computing slope, find displacement as area under v-t, and tell from the shape of an x-t curve (straight vs. curving) whether acceleration is zero or nonzero — without needing to memorize a separate rule for each.
