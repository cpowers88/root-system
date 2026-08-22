---
type: equation
timeline: reference
status: draft
---

# Equation — Tangential and Radial Acceleration

## Equation

```text
a_t = dv/dt              (tangential component — rate of change of speed)
a_r = v²/r                (radial/centripetal component, magnitude)
a = √(a_r² + a_t²)         (total acceleration magnitude)
```

## Meaning in Plain English

Splits total acceleration on a curved path into "how fast the speed is changing" (tangential) and "how fast the direction is changing" (radial/centripetal). The two components are always perpendicular to each other.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| a_t | tangential acceleration | m/s² |
| a_r | radial (centripetal) acceleration | m/s² |
| v | instantaneous speed | m/s |
| r | radius of curvature at that point | m |
| a | magnitude of total acceleration | m/s² |

## Units Check

a_t = dv/dt → (m/s)/s = m/s² ✓. a_r = v²/r → (m/s)²/m = m/s² ✓. Both add in quadrature (Pythagorean theorem) since they're perpendicular, giving m/s². ✓

## When to Use It

Any curved-path motion where speed is changing — "speeding up around a curve," "slowing down through a turn," a roller coaster loop with varying speed.

## When Not to Use It

If speed is explicitly constant, a_t = 0 and this reduces to plain centripetal acceleration — use [[../equations/centripetal-acceleration]] directly, no need to invoke the tangential term.

## Required Assumptions

r is the instantaneous radius of curvature of the path at that point (for a circle, this is just the circle's radius; for a general curve it can change point to point — not tested at this level in PHYS 2211).

## Calculus Origin

a_t = dv/dt is the 1D derivative of speed from Stage 2, applied along the path direction. a_r = v²/r comes from the same vector-derivative argument as [[../equations/centripetal-acceleration]] (differentiating a rotating position vector), evaluated at each instant even as v(t) changes.

## Example Problem Type

[[../problem-types/nonuniform-circular-motion]]

## Common Mistake

Forgetting the tangential component entirely and computing only a_r when the problem states the object is speeding up or slowing down. Also: adding a_r and a_t directly (they're perpendicular — combine with the Pythagorean theorem, not simple addition).

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Section 4.5, Equations 4.26–4.28.
