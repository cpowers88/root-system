---
type: problem-type
status: draft
---

# Constant-Velocity Problem

## How to Recognize This Problem Type

The problem states or implies the object moves at a constant (unchanging) speed in one direction: "moving at 15 m/s," "traveling at a steady pace," "no acceleration." Alternatively, the problem gives zero net force (from Stage 5 onward).

Special case: two objects moving at different constant velocities — often asks when or where they meet.

## Given Information Usually Present

Two of the three quantities: initial position x₀, final position x (or displacement Δx), velocity v, and time t. One is unknown.

Acceleration is zero (even if not stated — it is implied by "constant velocity").

## Unknown Usually Requested

- How far did it travel in time t? → find x or Δx
- How long did it take to travel distance d? → find t
- Where did two constant-velocity objects meet? → set x₁(t) = x₂(t) and solve for t

## Diagram to Draw

A motion diagram (dots equally spaced in time = constant velocity). Label x₀, x_f, and the direction of motion.

```
→ → → → → → →  (equal spacing = constant velocity)
x₀             x_f
```

## Equations

```
x = x₀ + v·t        (or Δx = v·t when x₀ = 0)
```

This is kinematic Equation 2 with a = 0, or equivalently: Δx = v_avg·Δt since v_avg = v when a = 0.

## Step-by-Step Solving Pattern

1. **Define positive direction** — choose and label it on a diagram.
2. **List knowns:** x₀, x (or Δx), v, t — mark what's given, what's unknown.
3. **Write** x = x₀ + vt.
4. **Solve algebraically** for the unknown.
5. **Check units:** [m] = [m] + [m/s][s] = [m] ✓
6. **Check sign:** Is the final position on the correct side of the origin?

## Two-Object Variant (Meeting Problem)

Set position equations equal: x₁(t) = x₂(t)

```
Object 1: x₁ = x₀₁ + v₁t
Object 2: x₂ = x₀₂ + v₂t

Set equal: x₀₁ + v₁t = x₀₂ + v₂t
Solve for t: t = (x₀₂ − x₀₁) / (v₁ − v₂)
```

Then substitute t back to find meeting position.

## Unit Checks

Final position: m = m + (m/s)·s = m ✓
Time: s = m / (m/s) ✓

## Common Traps

- Using the full kinematic Δx = v₀t + ½at² and forgetting to set a = 0 — it still works, but adds unnecessary complexity.
- In two-object problems: writing both objects' positions using the same origin but choosing inconsistent starting times. Fix: define t = 0 as the moment both are being tracked simultaneously.

## Practice Drills

- [[../drills/constant-acceleration-drill]] (first two problems are constant-velocity cases)

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 2.3–2.4, pp. 30–33.
