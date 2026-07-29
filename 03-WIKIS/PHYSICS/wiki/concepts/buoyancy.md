---
type: concept
timeline: reference
status: draft
---

# Buoyancy (Archimedes' Principle)

## What is the physical idea?

When an object is submerged in a fluid, the fluid pushes harder on the bottom of the object than on the top (because the bottom is deeper). The net upward force from these pressure differences is the buoyant force.

**Archimedes' Principle:** The buoyant force on an object equals the weight of the fluid displaced by the object.

```text
B = ρ_fluid · V_displaced · g
```

This is always upward.

## What real-world situation does it describe?

Ships floating on water, helium balloons rising in air, fish adjusting depth using a swim bladder, hydrometers measuring fluid density, a block of ice floating with most of its volume below the surface.

## Objects / System Involved

An object (any shape, any density) partially or fully immersed in a fluid.

## Quantities That Change

- If V_displaced changes (e.g., object sinks deeper), B changes.
- The object's own properties (mass, volume, density) determine whether it floats or sinks.

## Model or Equations

**Buoyant force:**
```text
B = ρ_fluid · V_displaced · g
```

**Does it float or sink?**
- If B < mg (weight): object sinks
- If B = mg: object is in neutral equilibrium (hovers)
- If B > mg: object rises (or floats at the surface)
- At the surface (floating): B = mg exactly → ρ_fluid · V_submerged · g = ρ_object · V_total · g

**Fraction submerged (floating object):**
```text
V_submerged / V_total = ρ_object / ρ_fluid
```

An ice cube (ρ_ice ≈ 917 kg/m³, ρ_water = 1000 kg/m³) floats with 917/1000 = 91.7% submerged — consistent with what you see: most of an iceberg is underwater.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| B | buoyant force | N (upward) |
| ρ_fluid | density of the surrounding fluid | kg/m³ |
| V_displaced | volume of fluid displaced by the object | m³ |
| g | gravitational field | 9.80 m/s² |
| ρ_object | density of the object | kg/m³ |
| V_total | total volume of the object | m³ |

## Calculus Connection

Buoyancy is derived by integrating the pressure over the entire surface of the submerged object. For a uniform fluid and a submerged object, this integral reduces exactly to ρ_fluid V_displaced g — the simple formula.

## Diagram / Visual Model

**Fully submerged:**
```
         ↑ B = ρ_fluid · V_object · g
    ┌──────────┐
    │  object  │
    └──────────┘
         ↓ w = ρ_object · V_object · g

If ρ_fluid > ρ_object → B > w → rises.
If ρ_fluid < ρ_object → B < w → sinks.
```

**Floating (partially submerged):**
```
   ───────────────── water surface
   ┌────────────┐
   │ submerged  │   V_sub
   └────────────┘
   [  above surface: V_total - V_sub  ]

B = ρ_water · V_sub · g = mg = ρ_object · V_total · g
→ V_sub/V_total = ρ_object/ρ_water
```

## Problem Types That Use This

- [[../problem-types/buoyancy-problems]]

## Common Beginner Mistake

**Using total volume when partially submerged.** B = ρ_fluid · **V_displaced** · g. For a floating object, V_displaced = V_submerged, NOT V_total. Only when fully submerged does V_displaced = V_total.

**Forgetting buoyancy acts on objects in any fluid, including air.** A helium balloon floats because B (from displaced air) > w (weight of balloon + helium). The formula is the same — just use ρ_air instead of ρ_water.

## Practice Next

After buoyancy, study [[continuity-equation]] and [[bernoullis-equation]] for moving fluids.
