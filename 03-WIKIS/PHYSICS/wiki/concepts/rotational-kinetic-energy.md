---
type: concept
timeline: reference
status: draft
---

# Rotational Kinetic Energy

## What is the physical idea?

A spinning object has kinetic energy due to its rotation, even if its center of mass isn't moving. This rotational kinetic energy K_rot = ½Iω² is the direct rotational analogue of translational kinetic energy K_trans = ½mv². For rolling objects, both types of kinetic energy exist simultaneously and must both be accounted for.

## What real-world situation does it describe?

A flywheel storing energy in an energy system. A bowling ball rolling down a lane (it has both rolling-forward and spinning energy). A wheel that takes more energy to spin up if it's heavier at the rim (larger I).

## Objects / System Involved

Any rotating object. For rolling objects: a rigid body rotating about its center while the center moves along a surface.

## Quantities That Change

K_rot changes when ω changes. It can convert to/from translational KE (in rolling) and to/from gravitational PE (energy conservation problems on inclines).

## Equations

**Rotational kinetic energy:**
```
K_rot = ½Iω²
```

**Total kinetic energy of a rolling object:**
```
K_total = K_trans + K_rot = ½mv_cm² + ½Iω²
```

Using the rolling condition v_cm = Rω (so ω = v_cm/R):
```
K_total = ½mv_cm² + ½I(v_cm/R)² = ½v_cm²(m + I/R²)
```

**Energy conservation for rolling down an incline** (starting from rest at height h):
```
mgh = ½mv_cm² + ½Iω² = ½v_cm²(m + I/R²)
```

Solving for v_cm at the bottom:
```
v_cm = √(2gh / (1 + I/(mR²)))
```

The factor (1 + I/(mR²)) shows that a larger I (more rotational inertia) means a smaller final speed. Shape matters.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| K_rot | rotational kinetic energy | J |
| I | moment of inertia | kg·m² |
| ω | angular speed | rad/s |
| K_trans | translational (linear) kinetic energy | J |
| v_cm | center-of-mass speed | m/s |
| m | total mass | kg |
| R | radius | m |
| h | height of incline | m |
| g | gravitational acceleration, 9.80 m/s² | m/s² |

**Units check:** [K_rot] = kg·m² × (rad/s)² = kg·m²/s² = J ✓ (radians are dimensionless)

## Calculus Connection

K_rot = ½Iω² is derived by summing ½mᵢvᵢ² over all mass elements, where vᵢ = rᵢω:
```
K_rot = Σ½mᵢvᵢ² = Σ½mᵢrᵢ²ω² = ½ω²Σmᵢrᵢ² = ½Iω²
```

## Diagram / Visual Model

```
ROLLING BALL on incline:

        • ← ball (both spinning and moving)
       /|
      / |  h
     /  |
    /θ  |
   ------

   PE lost = mgh
   = K_trans gained + K_rot gained
   = ½mv² + ½Iω²

   If I is larger → more energy goes to rotation → less translational speed at bottom
```

**Shape race result (equal mass, equal radius, released from same height):**
1. Solid sphere (I = 2/5 MR²) — fastest
2. Solid cylinder (I = 1/2 MR²)
3. Hollow sphere (I = 2/3 MR²)
4. Hollow cylinder/hoop (I = MR²) — slowest

## Problem Types That Use This

- [[../problem-types/rotational-energy-problems]]
- [[../problem-types/rolling-problems]]

## Common Beginner Mistake

1. **Forgetting K_rot entirely for rolling objects.** Setting mgh = ½mv² alone misses half the energy. For rolling, always write ½mv² + ½Iω².
2. **Using the wrong I for the geometry.** A solid disk is not a hoop — use the correct formula from the table.
3. **Not using the rolling condition to eliminate ω.** Substitute ω = v/R to get everything in terms of one variable.
4. **Treating radians as having units in the energy equation.** rad²/s² = s⁻² for purposes of units — J = kg·m²·s⁻² comes out correctly.

## Practice Next

[[../drills/rotational-energy-drill]] and [[../worked-examples/rolling-cylinder-incline-example]].

## Sources

Serway & Jewett, 10th ed., Ch. 10.4 and 10.8.
