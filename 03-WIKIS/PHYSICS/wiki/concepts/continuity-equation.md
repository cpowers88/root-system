---
type: concept
timeline: reference
status: draft
---

# Continuity Equation

## What is the physical idea?

For an ideal (incompressible) fluid flowing steadily through a pipe, the same volume of fluid must pass every cross-section per second. If the pipe gets narrower, the fluid must speed up to keep the same volume flowing through.

This is conservation of mass applied to fluid flow.

## What real-world situation does it describe?

Water flowing through a garden hose (pinching the hose makes it squirt faster), blood flowing through arteries (narrowed artery → higher flow speed), rivers narrowing between canyon walls and speeding up, air flowing over an airplane wing.

## Objects / System Involved

An incompressible fluid flowing through a pipe or channel that changes cross-sectional area.

## Quantities That Change

As cross-sectional area A decreases, flow speed v increases (and vice versa), such that their product remains constant.

## Model or Equation

```text
A₁v₁ = A₂v₂
```

- A₁, A₂ = cross-sectional areas at two points (m²)
- v₁, v₂ = fluid speeds at those points (m/s)
- The product Av = volume flow rate (m³/s) = constant

**Volume flow rate:** Q = Av (units: m³/s)

**Assumptions (ideal fluid):**
1. Incompressible: density is constant (good for liquids; only approximate for gases at low speed)
2. Steady flow: conditions at any point don't change with time
3. Non-viscous: no internal friction (idealization)
4. Streamline (laminar) flow: fluid moves in smooth layers, not turbulently

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| A | cross-sectional area of pipe | m² |
| v | fluid speed | m/s |
| Q | volume flow rate | m³/s |

## Calculus Connection

The continuity equation is the integral form of conservation of mass for steady, incompressible flow: dV/dt = Av = constant. For a more general derivation (compressible fluids), it involves the divergence of the velocity field — beyond this course.

## Diagram / Visual Model

```
  A₁ (large)     A₂ (small)
  v₁ (slow)      v₂ (fast)
   ─────────┐  ┌──────
            │  │
  ═════════════════════>
            │  │
   ─────────┘  └──────

A₁v₁ = A₂v₂
If A₂ = A₁/2, then v₂ = 2v₁ (doubles the speed)
```

## Problem Types That Use This

- [[../problem-types/fluid-flow-problems]]

## Common Beginner Mistake

**Confusing area and radius.** Pipe cross-sections are circles: A = πr². If the radius halves, the area quarters (A ∝ r²), so the speed quadruples. Don't just compare radii — compute actual areas.

**Using the continuity equation when flow is not steady or the fluid is compressible.** The simple form A₁v₁ = A₂v₂ only holds for steady, incompressible flow.

## Practice Next

Continuity is always combined with [[bernoullis-equation]] to solve pipe-flow problems — learn both before attempting pressure-speed problems.
