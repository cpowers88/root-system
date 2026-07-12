---
type: concept
status: draft
---

# Pressure

## What is the physical idea?

Pressure is the amount of force applied per unit area. The same force spread over a large area produces low pressure; concentrated on a small area produces high pressure.

## What real-world situation does it describe?

A nail driven into wood (small area → high pressure), a snowshoe on snow (large area → low pressure), a diver feeling the weight of water above them, a hydraulic car lift.

## Objects / System Involved

Any surface in contact with a fluid, or any surface on which a force is applied.

## Quantities That Change

Force, area, pressure — any one can change while the others respond.

## Model or Equation

```text
P = F / A
```

- P = pressure (Pa = N/m²)
- F = force perpendicular to the surface (N)
- A = area of the surface (m²)

**Key property in a fluid:** pressure at any point acts equally in all directions. Push on a fluid and it pushes back equally in every direction — this is Pascal's principle.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| P | pressure | Pa = N/m² |
| F | force perpendicular to surface | N |
| A | area | m² |

**Common pressure units and conversions:**
- 1 Pa = 1 N/m²
- 1 atm = 1.013 × 10⁵ Pa (standard atmosphere)
- 1 atm = 760 mm Hg (torr) = 14.7 psi
- 1 bar = 10⁵ Pa ≈ 1 atm
- Gauge pressure = absolute pressure − atmospheric pressure (a tire gauge reads gauge pressure)

## Calculus Connection

None in this basic definition. The pressure at depth arises from integrating the weight of a fluid column above a point, but at constant density this gives the simple formula P = P₀ + ρgh directly.

## Diagram / Visual Model

```
     Force F (perpendicular, downward)
          ↓ ↓ ↓
  ┌──────────────────┐
  │   Area A         │   P = F/A
  └──────────────────┘

  Same force, half the area → double the pressure.
```

## Problem Types That Use This

- [[../problem-types/pressure-depth-problems]]
- [[../problem-types/buoyancy-problems]]
- [[../problem-types/fluid-flow-problems]]

## Common Beginner Mistake

Confusing pressure with force. A large force doesn't always mean large pressure — it depends on the area it's spread over. A thumb tack and a flat-ended rod might be pushed with the same force, but the tack (tiny area) produces far more pressure and penetrates wood while the rod doesn't.

## Practice Next

Move immediately to [[pressure-vs-depth]] — pressure-at-depth is the first application in nearly every fluid mechanics problem.
