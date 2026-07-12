---
type: problem-type
status: draft
---

# Constant-Acceleration Problem

## How to Recognize This Problem Type

The problem involves motion along a line with a constant (non-zero) acceleration. Look for:
- "uniformly accelerating," "constant force," "brakes uniformly"
- a known value of acceleration (e.g., "acceleration of 3.0 m/s²")
- free fall (a special case — see [[free-fall]])
- three of the five kinematic quantities given; one or two are unknown

Not this type when: "acceleration increases," "force varies," object is on a spring.

## Given Information Usually Present

Three of the five kinematic quantities: x₀, x (or Δx), v₀, v, a, t. One or two are unknown.

## Unknown Usually Requested

Most commonly: final velocity v, time t, or displacement Δx. Occasionally: finding a from given motion data.

## Diagram to Draw

Motion diagram: dots that get farther apart (speeding up) or closer together (slowing down). Label initial and final positions, direction of positive x, initial and final velocities, and direction of acceleration.

```
Speeding up (+x, +a):
→ →  →   →    →     →
x₀                  x_f

Slowing down (+x, −a):
→     →   →  → →
x₀              x_f
```

## Equations

The five kinematic equations — see [[../equations/kinematic-equations]]:

```
1. v = v₀ + at                  (no Δx)
2. x = x₀ + v₀t + ½at²         (no v_f)
3. v² = v₀² + 2a(x − x₀)       (no t)
4. x = x₀ + ½(v₀ + v)t         (no a)
```

## Step-by-Step Solving Pattern

1. **Draw the diagram.** Label direction of positive x. Label x₀, x_f, v₀, v, a, t — write "?" for the unknown.

2. **List the five kinematic quantities:**
   - x₀ = ?
   - x_f = ?
   - v₀ = ?
   - v = ?
   - a = ?
   - t = ?

3. **Mark givens and unknowns.** You need three knowns to solve for one unknown.

4. **Pick the equation** that contains your unknown and all three knowns, but does NOT contain the fifth quantity (the one you neither know nor need).

5. **Solve algebraically**, keeping symbols until the last step.

6. **Substitute numbers with units.** Check units throughout.

7. **Check the answer:** Does the sign make sense? Is the magnitude reasonable?

## Unit Checks

- [v] = [m/s]: check v₀ + at → m/s + (m/s²)(s) = m/s ✓
- [x] = [m]: check x₀ + v₀t + ½at² → m + (m/s)(s) + (m/s²)(s²) = m ✓
- [v²] = [m²/s²]: check v₀² + 2aΔx → m²/s² + (m/s²)(m) = m²/s² ✓

## Common Traps

- **Using the equations when acceleration is not constant.** They fail — you must integrate instead.
- **Forgetting to take the square root** when solving v² = v₀² + 2aΔx for v. v = ±√(result); pick the physically correct sign.
- **Picking the wrong sign for a.** Deceleration means a is opposite to the direction of v. If car moves in +x and brakes, a is negative.
- **Two-stage problems:** if acceleration changes partway through (e.g., brakes after coasting), solve each stage separately. The final state of Stage 1 becomes the initial state of Stage 2.

## Practice Drills

- [[../drills/constant-acceleration-drill]]

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 2.6, Table 2.2, pp. 39–44.
