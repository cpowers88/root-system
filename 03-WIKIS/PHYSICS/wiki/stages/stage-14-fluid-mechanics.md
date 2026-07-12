---
type: stage
status: draft
---

# Stage 14 — Fluid Mechanics (Ch 14)

## Goal

Apply pressure, buoyancy, and flow concepts to liquids and gases. Understand why objects float or sink, how pressure changes with depth, and how fluid speed and pressure trade off in a pipe.

## Syllabus Alignment

Ch 14. Confirmed in scope by Chris (2026-06-25). Lecture dates to be confirmed from D2L calendar.

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 14. File: `raw/textbook/Physics book-0301-0400.pdf` (partial) and `raw/textbook/Physics book-0401-0500.pdf`.

## Prerequisite Physics

- Stage 5: force, Newton's laws (buoyancy is a force problem)
- Stage 7–8: energy and work (Bernoulli is derived from work-energy theorem)
- Stage 1: density (ρ = m/V — used constantly in this chapter)

## Prerequisite Math

- Algebra (isolate variables in multi-term equations)
- Area formulas (circles, rectangles — for pipe cross-sections)

## Core Concepts

- [[../concepts/pressure]]
- [[../concepts/pressure-vs-depth]]
- [[../concepts/buoyancy]]
- [[../concepts/continuity-equation]]
- [[../concepts/bernoullis-equation]]

## Required Vocabulary

Pressure, gauge pressure, Pascal's law, buoyancy, Archimedes' principle, continuity, Bernoulli, streamline, ideal fluid, viscosity.
See [[../flashcards/stage-14-fluid-mechanics]].

## Equations

- [[../equations/pressure]] — P = F/A
- [[../equations/buoyancy]] — B = ρ_fluid V_displaced g
- [[../equations/continuity]] — A₁v₁ = A₂v₂
- [[../equations/bernoulli]] — P + ½ρv² + ρgy = constant

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| P | pressure | Pa = N/m² |
| F | force on surface | N |
| A | surface area | m² |
| ρ | fluid density | kg/m³ |
| g | gravitational field | m/s² = 9.80 m/s² |
| h | depth below surface | m |
| B | buoyant force | N |
| V_displaced | volume of fluid displaced | m³ |
| v | fluid speed | m/s |
| P₀ | surface (atmospheric) pressure | Pa; 1 atm = 1.013 × 10⁵ Pa |

**Common densities to memorize:**
- Water: ρ = 1000 kg/m³
- Seawater: ρ ≈ 1025 kg/m³
- Air (at sea level): ρ ≈ 1.29 kg/m³
- Aluminum: ρ ≈ 2700 kg/m³
- Iron/steel: ρ ≈ 7860 kg/m³
- Ice: ρ ≈ 917 kg/m³ (less than water → floats)

## Diagrams / Visual Models

**Pressure at depth:**
```
Surface  ←  P₀ (atmospheric)
   |
   h         P increases downward
   |
Point   ←  P = P₀ + ρgh
```

**Buoyancy (submerged object):**
```
        ↑ B (buoyant force, upward)
   ┌────────┐
   │ object │
   └────────┘
        ↓ w = mg (weight, downward)
Fluid displaced = volume of object
```

**Continuity (narrowing pipe):**
```
Wide pipe  →  Narrow pipe
A₁, v₁ (slow)   A₂, v₂ (fast)
A₁v₁ = A₂v₂  →  if A₂ < A₁, then v₂ > v₁
```

**Bernoulli (horizontal pipe, height constant):**
```
High pressure, low speed  →  Low pressure, high speed
```

## Calculus Connections

- Continuity equation is the steady-state form of conservation of mass: dV/dt = Av = constant.
- Bernoulli's equation is derived by applying the work-energy theorem to a moving fluid element along a streamline — it is the energy equation for ideal fluid flow.

## Problem Types

- [[../problem-types/pressure-depth-problems]]
- [[../problem-types/buoyancy-problems]]
- [[../problem-types/fluid-flow-problems]]

## Worked Examples

- [[../worked-examples/floating-object-example]]
- [[../worked-examples/pipe-flow-bernoulli-example]]

## Drills

- [[../drills/pressure-buoyancy-drill]]
- [[../drills/bernoulli-continuity-drill]]

## Common Errors

See [[../common-errors/stage-14-fluid-mechanics]].

## Mastery Checklist

- [ ] State the definition of pressure and its SI unit without hesitation
- [ ] Derive the pressure-at-depth formula P = P₀ + ρgh from a force balance on a fluid column
- [ ] State Archimedes' principle in plain English: buoyant force = weight of displaced fluid
- [ ] Calculate buoyant force for a fully submerged object given ρ_fluid and V_object
- [ ] Determine the fraction submerged for a floating object given ρ_object and ρ_fluid
- [ ] Apply the continuity equation to find speed in a narrowing or widening pipe
- [ ] Apply Bernoulli's equation to find pressure difference in a pipe or speed of draining fluid
- [ ] State the assumptions of the ideal fluid model (incompressible, no viscosity, steady, streamline)
- [ ] Check units for all four terms in Bernoulli's equation and confirm they all have units of Pa

## Do Not Move On Until

Chris can solve a buoyancy problem (floating and fully-submerged cases) and a Bernoulli + continuity pipe problem without referring to notes.

## Parked for Later

- Viscosity and Poiseuille's Law: applies to real (non-ideal) fluids; not required for PHYS 2211.
- Turbulent flow: beyond ideal fluid model; mentioned in text but not testable at this level.
