---
type: equation
status: draft
---

# Centripetal Acceleration

## Equation

```
a_c = v²/r = ω²r
```

**Centripetal force (Newton's 2nd law applied inward):**
```
F_c = m a_c = mv²/r
```

**Period and speed relationship:**
```
T = 2πr/v      →      v = 2πr/T
```

## Meaning in Plain English

An object moving in a circle at constant speed experiences an acceleration directed toward the center of the circle. This acceleration exists because the direction of velocity is constantly changing — even though speed is constant.

The centripetal force is not a new type of force. It is whatever real force (tension, gravity, friction, normal force) acts inward to keep the object on the circular path.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| a_c | centripetal acceleration | m/s² |
| v | speed (constant magnitude) | m/s |
| r | radius of circular path | m |
| ω | angular speed | rad/s |
| F_c | net inward (centripetal) force | N |
| m | mass of object | kg |
| T | period (time per revolution) | s |

## Units Check

a_c = v²/r → (m/s)²/m = m²/s² / m = m/s² ✓

F_c = mv²/r → kg · m/s² = N ✓

## When to Use It

Any situation where an object is moving along a circular arc (even just part of a circle) at constant or nearly constant speed.

## When Not to Use It

When the object is speeding up or slowing down along the circle — then there is also a tangential acceleration component. In that case, a_c gives only the inward (radial) piece; you also need a_t = dv/dt and must combine them. This is still **Chapter 4 material** (Section 4.5) — see [[../equations/tangential-and-radial-acceleration]] and [[../concepts/tangential-and-radial-acceleration]]. (Corrected 2026-07-07 — previously miscited as Stage 10 material; Stage 10 is rotational dynamics, a different topic.)

## Required Assumptions

Constant speed along a circular arc of constant radius.

## Calculus Origin

If the position on the circle is r⃗(t) = r(cos ωt, sin ωt), then:
```
v⃗ = dr⃗/dt = rω(-sin ωt, cos ωt)     |v⃗| = rω = v
a⃗ = dv⃗/dt = -rω²(cos ωt, sin ωt) = -ω²r⃗
```
The acceleration vector has magnitude ω²r = v²/r and points opposite to r⃗ — i.e., toward the center.

## Example Problem Type

A car travels at 20 m/s around a curve of radius 50 m. Find the centripetal acceleration and the minimum friction force required.

```
a_c = v²/r = (20)²/50 = 400/50 = 8.0 m/s²

For friction to supply centripetal force (flat road):
F_c = ma_c = m(8.0 N/kg)
Minimum friction: f = m(8.0) → μmg = m(8.0) → μ = 8.0/9.80 = 0.82
```

## Common Mistake

Thinking centripetal acceleration is zero because speed is constant. Acceleration is the rate of change of the velocity vector, not just its magnitude. Constant speed ≠ zero acceleration when direction changes.

Also: listing "centripetal force" as a separate force on a free body diagram. It is the net inward force, not an additional force. Identify which real force provides it (tension, gravity, normal force, friction) and draw that instead.

## Sources

- Serway & Jewett, 10th ed., Ch. 4.4, Eq. 4.19, pp. 96–98.
