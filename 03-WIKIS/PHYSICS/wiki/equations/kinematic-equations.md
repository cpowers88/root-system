---
type: equation
timeline: reference
status: draft
---

# Kinematic Equations (Constant Acceleration)

## The Five Equations

These five equations describe all one-dimensional motion under constant acceleration. Each equation is missing exactly one of the five kinematic quantities — use that to pick the right one.

| # | Equation | Missing quantity |
|---|---|---|
| 1 | v = v₀ + at | Δx (position change) |
| 2 | x = x₀ + v₀t + ½at² | v (final velocity) |
| 3 | v² = v₀² + 2a(x − x₀) | t (time) |
| 4 | x = x₀ + ½(v₀ + v)t | a (acceleration) |
| 5 | x = x₀ + vt − ½at² | v₀ (initial velocity) — less commonly used |

## Meaning in Plain English

These equations answer: given what I know about an object's motion (where it started, how fast it was going, how hard it's accelerating), where will it be and how fast will it be going?

They are derived by integrating a = constant:
- Integrate once: v(t) = v₀ + at → Equation 1
- Integrate again: x(t) = x₀ + v₀t + ½at² → Equation 2
- Combine 1 and 2 to eliminate t → Equation 3

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| x | final position | m |
| x₀ | initial position | m |
| Δx | displacement = x − x₀ | m |
| v | final velocity | m/s |
| v₀ | initial velocity | m/s |
| a | acceleration (must be constant) | m/s² |
| t | time elapsed | s |

## Units Check

Equation 1: v = v₀ + at → [m/s] = [m/s] + [m/s²][s] = [m/s] + [m/s] ✓

Equation 2: x = x₀ + v₀t + ½at² → [m] = [m] + [m/s][s] + [m/s²][s²] = [m] ✓

Equation 3: v² = v₀² + 2aΔx → [m²/s²] = [m²/s²] + [m/s²][m] = [m²/s²] ✓

## When to Use

Use when acceleration is **constant** throughout the motion. That includes:
- Objects sliding on frictionless surfaces under constant force
- Free fall (a = −g = −9.80 m/s²)
- Cars accelerating uniformly

## When NOT to Use

- When acceleration changes with time (e.g., object on a spring, object with air resistance)
- When force is not constant (check Stage 7 and beyond)

If acceleration is not constant, you must integrate a(t) directly.

## How to Choose the Right Equation

Step 1: List all five quantities: x₀, x (or Δx), v₀, v, a, t.

Step 2: Mark which ones are given. Mark which one is unknown (what the problem asks for).

Step 3: Pick the equation that contains your unknown and all your givens, but NOT the one quantity you neither know nor need.

**Example decision:** Given v₀, a, t — want x. The unknown x appears in Eq. 2 (x = x₀ + v₀t + ½at²). Eq. 3 also has x but also has v, which you don't know. Use Eq. 2.

## Required Assumptions

- Acceleration is constant (or zero) during the entire time interval
- One-dimensional motion (or you're working on one axis at a time)
- Time t is measured from the moment the initial conditions (v₀, x₀) apply

## Calculus Origin

Starting from a = constant:

```
Integrate a = const once:    v(t) = v₀ + at             [Eq. 1]
Integrate v(t) once more:    x(t) = x₀ + v₀t + ½at²    [Eq. 2]
Eliminate t from 1 and 2:    v² = v₀² + 2aΔx            [Eq. 3]
Substitute Eq. 1 into Eq. 2 differently → Eq. 4, 5
```

## Common Mistake

Picking an equation without listing knowns and unknowns first. Students often grab Eq. 2 by habit and get stuck because they have two unknowns in it (v and a), then guess rather than systematically finding the equation that fits.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Table 2.2, p. 40. Section 2.6, pp. 39–44.
