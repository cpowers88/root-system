---
type: equation
timeline: reference
status: draft
---

# Terminal Velocity

## Equations

**Quadratic drag (high speed — standard for most physics problems):**
```
v_t = √(2mg / DρA)
```

**Linear drag (low speed — small/slow objects):**
```
v_t = mg / b
```

## Meaning in Plain English

Terminal velocity is the constant falling speed at which air resistance exactly cancels gravity. Derived by setting drag force equal to weight (net force = 0).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| v_t | terminal velocity | m/s |
| m | mass of object | kg |
| g | gravitational acceleration (9.80) | m/s² |
| D | drag coefficient (dimensionless, depends on shape) | — |
| ρ | density of fluid/air (air ≈ 1.20 kg/m³) | kg/m³ |
| A | cross-sectional area (projected area facing the flow) | m² |
| b | linear drag coefficient | kg/s |

## Units Check

Quadratic: √(kg · m/s² / (1 · kg/m³ · m²)) = √(kg·m/s² / (kg/m)) = √(m²/s²) = m/s ✓

## When to Use It

When a falling (or moving through fluid) object has reached constant speed. Also used to find the steady-state speed of an object being pushed by a constant force against drag (car, bicycle).

## When Not to Use It

During the acceleration phase before terminal velocity is reached, the full drag equation must be used with Newton's second law at each speed: ma = mg − ½DρAv² (or mg − bv). Terminal velocity gives only the endpoint.

## Required Assumptions

- Object falling vertically through a uniform fluid.
- Steady-state (reached after a long time, net force = 0).
- D, ρ, A, m, g all constant during the fall.

## Calculus Origin

The equation comes from setting the drag force equal to weight:

Quadratic: ½DρAv_t² = mg  →  v_t = √(2mg/DρA)
Linear:    bv_t = mg      →  v_t = mg/b

No calculus is needed to use the result, but deriving how the speed approaches v_t over time requires solving a differential equation (not required in PHYS 2211).

## Example Problem Type

A 75 kg skydiver (D = 0.70, A = 0.70 m², ρ = 1.2 kg/m³) is in free fall. Find terminal velocity.

```
v_t = √(2 × 75 × 9.80 / (0.70 × 1.2 × 0.70))
    = √(1470 / 0.588)
    = √(2500)
    = 50 m/s  ≈  180 km/h
```

## Common Mistake

Using the wrong drag model. Quadratic drag (½DρAv²) is the correct model for skydivers, cars, and baseballs. Linear drag (bv) is only for very slow or very small objects. When in doubt, the problem will specify which model to use.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 6.4, Eqs. 6.2, 6.4, 6.7.
