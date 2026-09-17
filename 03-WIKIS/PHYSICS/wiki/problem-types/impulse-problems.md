---
type: problem-type
timeline: reference
stage: 9
chapter: 9
---

# Problem Type: Impulse Problems

## How to Recognize

The problem involves a force acting over a time interval, and asks for one of: final velocity, change in momentum, average force, or duration of contact. Often includes a F-t graph where you must find the area.

Keywords: "impulse," "average force during collision," "time of contact," "hits/bounces," "F-t graph," "area under the curve."

## Given Information

Typically some combination of:
- Mass of object
- Initial and/or final velocity
- Average force and duration
- OR a F-t graph (for area calculation)

## Unknown Requested

One of: impulse J, change in momentum Δp, average force F_avg, time interval Δt, or final speed vf.

## Diagram to Draw

Draw the object before and after the interaction. Mark velocities with arrows and signs. If a F-t graph is given, shade the area you will calculate.

## Equations

```
J⃗ = Δp⃗ = p⃗_f − p⃗_i = m(v⃗_f − v⃗_i)

J = F_avg · Δt             (constant or average force)

J = area under F-t graph   (time-varying force)
```

## Solving Pattern

1. Define positive direction.
2. Write vᵢ and vf with correct signs (negative if opposite to positive direction).
3. Calculate Δp = m(vf − vᵢ).
4. Use J = F_avg · Δt to find the missing quantity.
5. Check units: N·s = kg·m/s.

## Unit Check

Force (N) × time (s) = N·s = kg·m/s ✓

## Traps

- **Direction flip:** If a ball bounces off a wall, vf is in the opposite direction from vᵢ. Calculate Δp = m(vf − vᵢ) — the minus sign is built in if you use signed velocities. Do NOT compute m|vf| + m|vᵢ| — that double-counts momentum change magnitude.
- **F-t graph area:** For a triangular pulse, area = ½ base × height. Students often use base × height (missing the ½).
- **Average vs. maximum force:** Some problems give the peak (maximum) force on a graph — but what you need is the area, not the peak value.

## Drill

[[../drills/momentum-impulse-drill]]
