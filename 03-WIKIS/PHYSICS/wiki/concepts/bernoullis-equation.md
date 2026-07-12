---
type: concept
status: draft
---

# Bernoulli's Equation

## What is the physical idea?

For an ideal fluid flowing steadily along a streamline, the total "energy per unit volume" is conserved. When fluid speeds up (kinetic energy per unit volume increases), its pressure must decrease — energy is trading form, not appearing from nowhere.

**Bernoulli's equation is the energy conservation equation for flowing fluids.**

## What real-world situation does it describe?

- Airplane wings: air moves faster over the curved top → lower pressure on top → net upward lift force
- A carburetor: fast-moving air past a fuel nozzle creates low pressure that draws fuel into the airstream
- A Venturi meter: measure flow speed by reading a pressure difference in a constriction
- Water draining from a tank: speed depends on the height of water above the opening
- A perfume atomizer: blowing air over a tube creates low pressure that draws perfume up

## Objects / System Involved

An ideal (incompressible, non-viscous, steady, streamline) fluid moving along a streamline from point 1 to point 2.

## Quantities That Change

Pressure P, fluid speed v, and height y all vary along a streamline, but in a specific compensating way.

## Model or Equation

```text
P₁ + ½ρv₁² + ρgy₁ = P₂ + ½ρv₂² + ρgy₂
```

Or equivalently:
```text
P + ½ρv² + ρgy = constant   (along a streamline)
```

**Each term has units of Pa = N/m² = J/m³ (energy per unit volume):**
- P = pressure energy per unit volume
- ½ρv² = kinetic energy per unit volume
- ρgy = gravitational potential energy per unit volume

**Important special cases:**

*Horizontal pipe (y₁ = y₂):*
```
P₁ + ½ρv₁² = P₂ + ½ρv₂²
```
Where v is large, P is small; where v is small, P is large.

*Fluid at rest (v = 0 everywhere):*
```
P₁ + ρgy₁ = P₂ + ρgy₂  →  P = P₀ + ρgh
```
Recovers the pressure-at-depth formula.

*Torricelli's theorem (tank draining through small hole):*
Take point 1 = surface (v₁ ≈ 0, P₁ = P₀) and point 2 = hole (P₂ = P₀, y₂ = 0):
```
ρgy_surface = ½ρv²_hole  →  v_hole = √(2gh)
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| P | pressure | Pa |
| ρ | fluid density | kg/m³ |
| v | fluid speed | m/s |
| g | gravitational field | 9.80 m/s² |
| y | height above reference level | m |
| ½ρv² | dynamic pressure | Pa |

## Calculus Connection

Bernoulli's equation is derived by applying the work-energy theorem to a small fluid element moving along a streamline. The work done by pressure forces minus the work against gravity equals the change in kinetic energy. For steady, incompressible, non-viscous flow, this integrates to the constant-sum form above.

## Diagram / Visual Model

```
    Point 1                    Point 2
    (wide, slow, high P)       (narrow, fast, low P)
    
    y₁ ─────────────────────── y₂ (same height)
    
    P₁ high                   P₂ low
    v₁ slow                   v₂ fast
    
    Energy trade: less pressure → more kinetic
```

## Problem Types That Use This

- [[../problem-types/fluid-flow-problems]]

## Common Beginner Mistakes

**Applying Bernoulli between two points NOT on the same streamline.** Bernoulli holds along a streamline. For an ideal fluid, all streamlines have the same total, so this often works anyway — but be aware of the assumption.

**Forgetting the assumptions.** Bernoulli ONLY applies to ideal fluid (incompressible, non-viscous, steady, streamline flow). Don't use it in turbulent flow situations.

**Units check before solving:** every term must have units of Pa. Check: ρgy = (kg/m³)(m/s²)(m) = kg/(m·s²) = Pa ✓. Half ρv² = (kg/m³)(m/s)² = kg/(m·s²) = Pa ✓.

**Not using continuity first.** In pipe-flow problems, you almost always need A₁v₁ = A₂v₂ to find v₂ before plugging into Bernoulli.

## Practice Next

Always combine with [[continuity-equation]]. Work [[../problem-types/fluid-flow-problems]] problems using both equations together.
