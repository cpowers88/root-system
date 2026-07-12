---
type: equation
status: draft
---

# Equation — Orbital Mechanics (Kepler's 3rd Law, Orbital Speed, Escape Speed)

## Equations

```
Orbital (circular) speed:    v_c = √(GM/r)
Orbital period:              T   = 2πr / v_c = 2π√(r³/GM)
Kepler's Third Law:          T²  = (4π²/GM) × r³
Escape speed:                v_e = √(2GM/r)
```

Note: v_e = v_c × √2

## Plain-English Meanings

**Orbital speed v_c:** The exact speed needed so that gravity provides all the centripetal force for a circular orbit. Too fast → object escapes; too slow → object falls inward.

**Kepler's Third Law:** The square of the orbital period is proportional to the cube of the orbital radius. This holds for all satellites/planets orbiting the same central mass M.

**Escape speed v_e:** The minimum launch speed (at radius r) needed to escape to infinity with zero speed left over. It does NOT depend on the object's mass — a rocket and a baseball have the same escape speed from the same point.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| G | gravitational constant = 6.674×10⁻¹¹ | N·m²/kg² |
| M | mass of the central body (planet, star) | kg |
| r | orbital radius (center-to-center) | m |
| v_c | circular orbital speed | m/s |
| T | orbital period | s |
| v_e | escape speed | m/s |

## Quick Numbers for Earth

- M_E = 5.97×10²⁴ kg, R_E = 6.371×10⁶ m
- Low Earth orbit speed ≈ 7.9 km/s
- Escape speed from Earth's surface ≈ 11.2 km/s

## Derivation Sketch

For circular orbit: F_g = F_centripetal → GMm/r² = mv²/r → v² = GM/r → v_c = √(GM/r).
For escape: set total energy = 0 → ½mv² − GMm/r = 0 → v_e = √(2GM/r).

## Common Mistake

Using diameter instead of radius for r. Also: using Earth's g (9.8 m/s²) in orbital calculations far from the surface instead of computing g = GM/r² at the correct altitude.
