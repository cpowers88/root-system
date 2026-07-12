---
type: problem-type
status: draft
---

# Energy Conservation — With Friction

## How to Recognize This Problem Type

Like the no-friction version, but friction (or another nonconservative force) is present. The problem states a coefficient of friction, mentions a rough surface, or asks you to find how much energy is "lost." Mechanical energy decreases — it doesn't disappear but becomes thermal energy.

**Keywords:** rough surface, coefficient of friction (μ_k), friction force, "energy lost to heat," "how far does it travel before stopping."

## Given Information Usually Present

- Mass, initial speed or height
- Friction force f_k, or coefficient of kinetic friction μ_k plus normal force N
- Distance over which friction acts (d), or the unknown is d itself

## Unknown Usually Requested

- Final speed after friction acts over distance d
- Distance traveled before stopping
- Coefficient of friction (given initial and final speeds)
- Energy "lost" to friction

## Diagram to Draw

```
STATE 1 (initial)                 STATE 2 (final)
  y = y_i, v = v_i                y = y_f, v = v_f
         |——— distance d ———|
         ←  f_k friction →   (friction acts opposite to motion)

Reference line: y = 0 at lowest point
f_k d = energy converted to thermal energy
```

Note the geometry of height on an incline:
```
Incline of length d, angle θ above horizontal:
   h = d sin θ    (vertical rise)
   N = mg cos θ   (normal force on incline)
   f_k = μ_k N = μ_k mg cos θ
```

## Equations Commonly Used

```
Ki + Ui - f_k d = Kf + Uf
½mv_i² + mgy_i - f_k d = ½mv_f² + mgy_f
```

To find f_k:
```
f_k = μ_k N
```

On flat surface: N = mg → f_k = μ_k mg

On incline angle θ: N = mg cos θ → f_k = μ_k mg cos θ

Energy lost to friction:
```
ΔE_thermal = f_k d  (always positive — energy is always lost, never gained, by friction)
```

## Step-by-Step Solving Pattern

1. **Draw** initial and final states. Label all energies.
2. **Identify** the friction force: is the surface flat or inclined? Compute N, then f_k = μ_k N.
3. **Identify** the distance d over which friction acts (along the surface, not the vertical height).
4. **Set** reference height y = 0 at the lowest point.
5. **Write:** Ki + Ui − f_k d = Kf + Uf
6. **Expand** all K and U terms.
7. **Substitute** known values.
8. **Solve** for unknown.
9. **Check units** and **check sign**: final speed must be less than it would be without friction; final height must be less than initial.

## Unit Checks

f_k d: N × m = J ✓ (energy units, as required — it subtracts from mechanical energy)

## Common Traps

1. **Using d (incline length) as the height h.** On an incline: h = d sin θ, NOT h = d. The friction term uses d (along surface); the gravitational PE uses h = d sin θ. These are different.
2. **Forgetting friction on a curved path.** If the path curves (e.g., bowl shape), d is the arc length, not the straight-line displacement. Usually the problem will give d explicitly.
3. **Subtracting f_k d from the wrong side.** The friction term always reduces mechanical energy: it goes on the left as Ki + Ui − f_k d. Don't add it to the right side.
4. **Confusing μ_s and μ_k.** Use kinetic friction (μ_k) when the object is sliding. Use static friction (μ_s) only for objects that are not sliding — static friction doesn't appear in energy problems because it does no work when there's no sliding.

## Practice Drills

- [[../drills/energy-conservation-drill]] Problems 4–6

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 8.3.
