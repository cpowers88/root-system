---
type: problem-type
timeline: reference
status: draft
---

# Free-Fall Problem

## How to Recognize This Problem Type

The problem involves an object moving only vertically (or asks only about the vertical component) with no air resistance. Key phrases: "dropped," "thrown upward," "falls freely," "height of a cliff," "thrown off a building."

Free-fall is constant-acceleration with a specific known value: a = −9.80 m/s² (taking up as positive).

## Given Information Usually Present

Some combination of: initial height y₀, final height y, initial vertical velocity v₀, time t, and the constraint a = −9.80 m/s². Usually one or two of these are missing.

Common setups:
- Object dropped (v₀ = 0, falls some height h)
- Object thrown upward (v₀ > 0, reaches a maximum height where v = 0 momentarily)
- Object thrown from a height (v₀ can be up or down)

## Unknown Usually Requested

- How long until impact? → find t
- How high does it go? → find y where v = 0
- How fast on impact? → find v at y_f
- Time to reach a certain height? → find t

## Diagram to Draw

Draw the vertical axis (y, positive upward). Mark the starting position y₀, the final position y_f, and the direction of the initial velocity. Draw a downward arrow for acceleration (g, downward = negative).

```
         v₀ (upward if thrown up)
          ↑
   top → ( ) ← v = 0 here, a = −g still
          |
          |  a = −g throughout
          |
          ↓
   y = 0  _  ← ground (or whatever reference)
```

## Equations

Use the kinematic equations (see [[../equations/kinematic-equations]]) substituting a = −g:

```
1. v = v₀ − gt
2. y = y₀ + v₀t − ½gt²
3. v² = v₀² − 2g(y − y₀)
4. y = y₀ + ½(v₀ + v)t
```

where g = +9.80 m/s² (the magnitude; the minus signs above handle direction).

## Step-by-Step Solving Pattern

1. **Define positive direction** (up is almost always positive — makes g positive and acceleration negative).
2. **Draw and label the diagram:** y₀, y_f, v₀, v, a = −9.80 m/s², and t.
3. **List knowns:** mark the four known quantities, identify the unknown.
4. **At the highest point**, if needed: v = 0 is your extra equation. Substitute and solve for t_up or y_max.
5. **Pick the kinematic equation** that matches your known/unknown set.
6. **Solve algebraically first, then substitute numbers.**
7. **Check sign of answer:** time must be positive; height of highest point must be above starting height.

## Common Two-Stage Setup

Object thrown up: rises to top, comes back down. Solve in two stages OR use the full flight as one stage (y_f = y₀ if it returns to the same height → simplifies Eq. 2).

## Unit Checks

[y] = m: check y₀ + v₀t − ½gt² → m + (m/s)(s) − (m/s²)(s²) = m ✓
[v] = m/s: check v₀ − gt → m/s − (m/s²)(s) = m/s ✓

## Common Traps

1. **Setting a = 0 at the top.** Acceleration is −9.80 m/s² the entire flight, not just up or down portions.
2. **Mixing up v₀ = 0 (dropped) with v₀ = 0 (top of flight).** Both have v = 0 at that instant, but for different reasons. Dropped: v₀ = 0 as initial condition. Top: v = 0 is the final condition at that instant.
3. **Forgetting the sign on v₀ for downward throws.** If you throw an object downward with speed 5 m/s and up is positive, v₀ = −5 m/s.
4. **Not choosing the physically correct root** of the quadratic t² equation — always two solutions, one may be negative (in the past) or extraneous.

## Practice Drills

- [[../drills/free-fall-drill]]

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 2.7, pp. 44–49.
