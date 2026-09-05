---
type: equation
timeline: reference
status: draft
---

# Moment of Inertia

## Equations

**Discrete (point masses):**
```
I = Σ mᵢ rᵢ²
```

**Continuous object:**
```
I = ∫ r² dm
```

**Parallel-axis theorem:**
```
I = I_cm + Md²
```

## Meaning in Plain English

Moment of inertia quantifies how hard it is to angularly accelerate a rigid object. The further mass is from the rotation axis, the more it resists being spun up (because it contributes r² per unit mass, not just r). The parallel-axis theorem lets you find I for any axis once you know I_cm.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| I | moment of inertia | kg·m² |
| I_cm | moment of inertia about axis through center of mass | kg·m² |
| m, M | mass | kg |
| r | perpendicular distance from rotation axis to mass element | m |
| d | distance from center of mass to new parallel axis | m |
| R | radius of cylinder, hoop, or sphere | m |
| L | length of rod | m |

## Units Check

[I] = kg × m² = kg·m² ✓ (from Σmr²)

## Standard Moment of Inertia Table

**Memorize these — they appear in nearly every problem.**

| Object | Axis location | Formula | Coefficient |
|---|---|---|---|
| Point mass at radius R | distance R from axis | MR² | 1 |
| Thin hoop / hollow cylinder | central symmetry axis | MR² | 1 |
| Solid cylinder / disk | central symmetry axis | ½MR² | 0.5 |
| Thin rod | through center, ⊥ to rod | (1/12)ML² | 1/12 ≈ 0.083 |
| Thin rod | through one end, ⊥ to rod | (1/3)ML² | 1/3 ≈ 0.333 |
| Hollow sphere (thin shell) | through center | (2/3)MR² | 0.667 |
| Solid sphere | through center | (2/5)MR² | 0.4 |

**Memory pattern:** More mass at the rim → larger coefficient. Hoop (all mass at R) → coefficient 1. Solid sphere (mass spread throughout volume) → coefficient 2/5 = 0.4.

## Parallel-Axis Theorem

```
I = I_cm + Md²
```

- d = perpendicular distance between the center-of-mass axis and the new axis
- The new axis must be parallel to the cm axis
- I is always **larger** than I_cm (you can't move the axis to make rotation easier than through cm)

**Example — rod spun about one end:**
```
I_cm = (1/12)ML²    (through center)
d = L/2             (end is L/2 from center)
I_end = (1/12)ML² + M(L/2)² = (1/12)ML² + (3/12)ML² = (4/12)ML² = (1/3)ML²  ✓
```

## When to Use It

- τ = Iα: whenever you apply Newton's second law for rotation, I is the "rotational mass"
- K_rot = ½Iω²: whenever you compute rotational kinetic energy
- Use the parallel-axis theorem whenever the rotation axis is not through the object's center of mass

## When Not to Use It

These formulas apply to rigid objects rotating about a fixed axis. For complex 3D rotation (precession, tumbling), the full inertia tensor is needed — well beyond this course.

## Calculus Origin

I = ∫r² dm is derived by integrating the contribution of each infinitesimal mass element at distance r from the axis. The factor r² (not r) means mass at 2× the distance contributes 4× as much.

## Common Mistake

1. Using the wrong geometry formula (solid disk ≠ hollow ring — both are "cylinders" but have different distributions).
2. Omitting the Md² term in the parallel-axis theorem.
3. Confusing R (radius for cylinders/spheres) with L (length for rods).

## Sources

Serway & Jewett, 10th ed., Table 10.2, Eqs. 10.15–10.18, Section 10.5.
