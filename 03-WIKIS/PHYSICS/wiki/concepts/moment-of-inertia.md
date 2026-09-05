---
type: concept
timeline: reference
status: draft
---

# Moment of Inertia

## What is the physical idea?

Moment of inertia I is the rotational analogue of mass. Just as mass measures resistance to linear acceleration (large m → small a for the same F), moment of inertia measures resistance to angular acceleration (large I → small α for the same τ). The difference from mass: I depends not only on how much mass an object has, but on how that mass is distributed relative to the rotation axis. Mass far from the axis contributes much more to I than mass close to the axis.

## What real-world situation does it describe?

Why a figure skater spins faster when arms are pulled in (smaller I → larger ω for fixed L). Why a solid ball rolls down a ramp faster than a hollow ball of the same mass (solid ball has lower I). Why a door is harder to open if you push near the hinge than near the edge (effective I is larger).

## Objects / System Involved

Any rigid object rotating about a defined axis.

## Quantities That Change

I itself is fixed for a given object and axis. It appears in τ = Iα (determines how much α results from a given torque) and in K_rot = ½Iω².

## Equations

**For a collection of discrete point masses:**
```
I = Σ mᵢ rᵢ²
```
where rᵢ is the perpendicular distance from mass i to the rotation axis.

**For a continuous object:**
```
I = ∫ r² dm
```

In practice you use the tabulated results below — the integral is done once in the textbook derivation.

## Standard Moment of Inertia Values (Memorize These)

| Object | Axis | I |
|---|---|---|
| Point mass | distance R from axis | MR² |
| Thin hoop / hollow cylinder | central axis (through center, along axis of symmetry) | MR² |
| Solid cylinder / disk | central axis | ½MR² |
| Thin rod | through center, perpendicular to rod | (1/12)ML² |
| Thin rod | through one end, perpendicular to rod | (1/3)ML² |
| Hollow sphere (thin shell) | through center | (2/3)MR² |
| Solid sphere | through center | (2/5)MR² |
| Thin rectangular plate | through center, parallel to side b | (1/12)Ma² |

**Pattern to notice:** objects with more mass concentrated near the rim have larger I coefficients (hoop = 1) than objects with mass spread toward the center (solid disk = 1/2, solid sphere = 2/5).

## Parallel-Axis Theorem

If you know I_cm (moment of inertia about the axis through the center of mass), you can find I about any parallel axis at distance d from the center of mass:

```
I = I_cm + Md²
```

This always makes I larger than I_cm — you're always farther from the center of mass.

**Example:** Thin rod, axis through one end. I_cm = (1/12)ML². Distance from center to end = L/2. So:
```
I_end = (1/12)ML² + M(L/2)² = (1/12)ML² + (1/4)ML² = (1/3)ML²  ✓
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| I | moment of inertia | kg·m² |
| m, M | mass | kg |
| r | distance from rotation axis to mass element | m |
| d | distance from cm to new axis (parallel-axis theorem) | m |
| R | radius (for cylinders, hoops, spheres) | m |
| L | length (for rods) | m |

**Units check:** [I] = kg·m² ✓ (from Σmr²: kg × m²)

## Calculus Connection

I = ∫r² dm is the defining integral. For a uniform rod of length L and mass M:
```
dm = (M/L)dx,  r = x  (taking axis at x = 0, center)
I = ∫_{-L/2}^{L/2} x² (M/L) dx = (M/L)[x³/3]_{-L/2}^{L/2} = (1/12)ML²
```
The standard results in the table above are all derived this way — you read the table, you don't re-derive them each time.

## Diagram / Visual Model

```
HOOP (I = MR²)          SOLID DISK (I = ½MR²)
  All mass at r = R       Mass spread from 0 to R
     ___                     ___
    /   \                   /***\
   |  •  |   axis →        |*****|   axis →
    \___/                   \***/
                          Less I because inner mass
                          contributes less (r² < R²)
```

## Problem Types That Use This

- [[../problem-types/torque-angular-acceleration]]
- [[../problem-types/rotational-energy-problems]]
- [[../problem-types/rolling-problems]]

## Common Beginner Mistake

1. **Using the wrong I formula for the geometry.** A solid disk and a hoop have the same mass and radius but completely different I values (½MR² vs. MR²). Always identify the geometry first.
2. **Using I about the wrong axis.** The formula depends on which axis you're rotating around. A rod spun about its center has I = (1/12)ML²; about its end it's (1/3)ML².
3. **Forgetting the parallel-axis theorem when the axis is not through the center of mass.** I = I_cm + Md² — you cannot skip the Md² term.
4. **Thinking a heavier object always has larger I.** I also depends on r². A less massive but larger object can have more resistance to rotation.

## Practice Next

[[../problem-types/torque-angular-acceleration]], then [[../drills/rotational-energy-drill]].

## Sources

Serway & Jewett, 10th ed., Ch. 10.5–10.6.
