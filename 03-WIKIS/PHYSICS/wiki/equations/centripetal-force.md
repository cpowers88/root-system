---
type: equation
status: draft
---

# Centripetal Force Equation

## Equation

```
ΣF_c = mv²/r
```

Also written as:

```
ΣF_c = ma_c     where   a_c = v²/r
```

## Meaning in Plain English

The net inward force required to keep an object moving in a circle equals its mass times its speed squared divided by the radius of the circle. Bigger speed, bigger force needed. Bigger radius, smaller force needed (gentler curve requires less force).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| ΣF_c | net force pointing toward center of circle | N |
| m | mass of object | kg |
| v | speed (magnitude of velocity) | m/s |
| r | radius of circular path | m |
| a_c | centripetal acceleration | m/s² |

## Units Check

[mv²/r] = kg · (m/s)² / m = kg · m/s² = N ✓

## When to Use It

Whenever an object is moving in a circular arc and you need to find one of: the net inward force, speed, radius, or mass. Always write it as a Newton's-2nd-law equation summing real forces in the inward direction.

## When Not to Use It

Do not apply it along the tangential direction (along the circle). Centripetal force only governs the inward direction. If speed is changing (nonuniform circular motion), there is also a tangential force component that this equation does not capture.

## Required Assumptions

- Object moves in a circle (or circular arc) at radius r.
- v is the instantaneous speed at the point of interest.
- For a complete vertical circle, apply this equation separately at each position.

## Calculus Origin

Centripetal acceleration a_c = v²/r is derived by taking the second derivative of the position vector for circular motion. The result is a vector that always points inward with magnitude v²/r. Plugging into ΣF = ma gives the centripetal force equation.

## Example Problem Type

A 0.50 kg ball on a 0.80 m string moves in a horizontal circle at 4.0 m/s. Find the tension.

```
T = mv²/r = (0.50)(4.0²)/(0.80) = (0.50)(16)/(0.80) = 10 N
```

## Common Mistake

Writing ΣF_c as a single "centripetal force" on the FBD and then writing ΣF_c = mv²/r — this double-counts. Instead, draw ALL real forces (T, mg, n, f), identify which ones point inward, sum them, and set that sum equal to mv²/r.

For a horizontal circle: T = mv²/r (tension is the only inward force)
For the bottom of a vertical circle: T − mg = mv²/r (tension inward, gravity outward)

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 6.1, Eq. 6.1.
