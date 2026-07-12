---
type: concept
status: draft
---

# Displacement vs. Distance

## What is the physical idea?

These are two completely different ways of describing "how much did the object move?"

- **Displacement** (Δx) — the straight-line change in position from start to finish. It is a vector: it has a sign (direction). It does not care about the path taken.
- **Distance** (d) — the total length of the path traveled. It is always positive. It accumulates every meter of path.

## What real-world situation does it describe?

You drive 5 km east to a store, then 5 km back home.

- Distance traveled: 10 km (you drove that many kilometers of road)
- Displacement: 0 km (you're back where you started)

These two numbers can be vastly different. Only displacement is used in kinematics equations.

## Objects / System Involved

Any object moving along a path. The same object produces different displacement and distance numbers whenever its path is not a straight line in one direction.

## Quantities That Change

| Quantity | Formula | Vector or Scalar | Can be negative? |
|---|---|---|---|
| Displacement | Δx = x_f − x₀ | Vector (in 1D, ± sign) | Yes |
| Distance | Total path length | Scalar | Never |

## Model or Equation

```
Δx = x_f − x₀
```

This is the displacement equation. Simple subtraction of coordinates.

Distance has no single formula — it is the total accumulated path length, which may require adding up segments.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| Δx | displacement (change in position) | m |
| x_f | final position | m |
| x₀ | initial position | m |
| d | distance (path length) | m |

## Calculus Connection

Displacement is the integral of velocity over time:

```
Δx = ∫ v dt    (from t₀ to t_f)
```

Distance is the integral of speed (the absolute value of velocity):

```
d = ∫ |v| dt
```

The difference matters if the object reverses direction — then |v| ≠ v in sign, and distance > |displacement|.

## Diagram / Visual Model

```
Object moves: → → → ← ← ← (goes right 6 m, comes back 4 m)

Start         Turn          End
  |           point          |
  0 ——————————6——————————> +x
  |←————————Δx = +2 m—————→|
  |←—distance = 6 + 4 = 10 m—→|
```

Displacement: 0 to 2 = +2 m. Distance: 6 + 4 = 10 m. Different.

## Problem Types That Use This

- [[../problem-types/constant-velocity]]
- [[../problem-types/constant-acceleration]]

## Common Beginner Mistake

Plugging distance into a kinematic equation in place of displacement. The kinematic equations use Δx (displacement). If an object reverses direction, these are not the same, and the answer will be wrong.

## Practice Next

Move to [[velocity-1d]] — velocity is displacement divided by time, not distance divided by time.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 2.1, pp. 22–24.
