---
type: concept
status: draft
---

# Pressure vs. Depth

## What is the physical idea?

The deeper you go in a fluid, the more fluid is sitting above you, and its weight pushes down — increasing the pressure. Pressure increases linearly with depth in a fluid of uniform density.

## What real-world situation does it describe?

A scuba diver feels increasing pressure as they descend. A dam wall must be thicker at the bottom than the top. Deep-sea submarines require thick reinforced hulls. Your ears pop when you dive to the bottom of a pool.

## Objects / System Involved

Any fluid (liquid or gas) with a submerged object or point of interest at depth h below the surface.

## Quantities That Change

Depth h increases → pressure P increases linearly.

## Model or Equation

```text
P = P₀ + ρgh
```

- P₀ = pressure at the surface (Pa). At the top of a lake or ocean open to air, P₀ = 1 atm = 1.013 × 10⁵ Pa.
- ρ = density of the fluid (kg/m³). For water: 1000 kg/m³.
- g = 9.80 m/s²
- h = depth below the surface (m) — positive downward

**Pascal's Law (extension):** If you change the pressure at the surface (e.g., push on a piston), that pressure change is transmitted unchanged throughout the entire fluid. Hydraulic lifts use this: F₁/A₁ = F₂/A₂.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| P | pressure at depth h | Pa |
| P₀ | surface pressure | Pa |
| ρ | fluid density | kg/m³ |
| g | gravitational field | 9.80 m/s² |
| h | depth below surface | m |

## Calculus Connection

The formula P = P₀ + ρgh is derived by integrating the weight of a thin horizontal fluid layer from the surface down to depth h:
```
dP/dy = -ρg  →  integrating:  P = P₀ + ρgh
```
For constant ρ (incompressible fluid), this gives the linear relationship directly.

## Diagram / Visual Model

```
Surface ────────────────  P₀ (atmospheric)
         |
         h  (depth)
         |
Point ──────────────────  P = P₀ + ρgh

The pressure is the SAME at any two points at the same depth,
regardless of horizontal position or the shape of the container.
```

## Problem Types That Use This

- [[../problem-types/pressure-depth-problems]]
- [[../problem-types/buoyancy-problems]] (pressure difference creates buoyancy force)

## Common Beginner Mistake

**Forgetting P₀.** Writing P = ρgh is wrong unless you're asked for gauge pressure (excess above atmospheric). Absolute pressure always includes atmospheric pressure at the surface. In most textbook problems, P₀ = 1.013 × 10⁵ Pa unless otherwise stated.

**h is depth, not height.** h is measured positive downward from the surface. If you define a coordinate y upward from the bottom, then h = (depth of surface) − y.

## Practice Next

After mastering pressure at depth, move to [[buoyancy]] — the buoyant force arises directly from the pressure difference between the bottom and top of a submerged object.
