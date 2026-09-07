---
type: worked-example
timeline: reference
stage: 13
---

# Worked Example: Orbital Period of the International Space Station

## Physical Situation

The International Space Station (ISS) orbits Earth at an altitude of approximately 408 km above Earth's surface. Find:
(a) The orbital radius
(b) The orbital speed
(c) The orbital period
(d) The number of orbits per day

## Given Constants

- G = 6.674×10⁻¹¹ N·m²/kg²
- M_Earth = 5.97×10²⁴ kg
- R_Earth = 6.37×10⁶ m
- Altitude h = 408 km = 4.08×10⁵ m

## Part (a): Orbital Radius

The orbital radius is measured from Earth's CENTER, not its surface:

```
r = R_Earth + h = 6.37×10⁶ + 4.08×10⁵ = 6.778×10⁶ m
```

## Part (b): Orbital Speed

For a circular orbit, gravity provides the centripetal force:

```
GMm/r² = mv²/r
```

Mass m of the ISS cancels:

```
v² = GM/r
v = √(GM/r) = √[(6.674×10⁻¹¹)(5.97×10²⁴) / (6.778×10⁶)]
v = √[3.983×10¹⁴ / 6.778×10⁶]
v = √(5.876×10⁷)
v = 7.666×10³ m/s ≈ 7,666 m/s ≈ 7.67 km/s
```

That's about 17,150 mph — 22 times the speed of sound.

## Part (c): Orbital Period

Time for one orbit = circumference / speed:

```
T = 2πr / v = 2π(6.778×10⁶) / 7666
T = 4.259×10⁷ / 7666
T = 5556 s ≈ 92.6 minutes
```

## Part (d): Orbits per Day

```
Orbits/day = (24 h × 60 min/h) / 92.6 min = 1440/92.6 ≈ 15.5 orbits/day
```

The ISS completes about 15–16 orbits per day. Astronauts see 15–16 sunrises each day.

## Verification Using Kepler's Third Law

T² = (4π²/GM) r³

```
(4π²) / [(6.674×10⁻¹¹)(5.97×10²⁴)] = 4π² / (3.983×10¹⁴) = 9.902×10⁻¹³ s²/m³

T² = (9.902×10⁻¹³)(6.778×10⁶)³ = (9.902×10⁻¹³)(3.113×10²⁰) = 3.083×10⁸ s²

T = √(3.083×10⁸) = 5552 s ≈ 5556 s ✓
```

Agrees with the direct calculation.

## Key Lessons

1. **Orbital radius is from Earth's CENTER.** Always add R_Earth to the altitude.
2. **The ISS mass cancels.** Orbital speed and period don't depend on the spacecraft's mass.
3. **Two methods agree:** Direct v-then-T calculation and Kepler's Third Law give the same answer — always good to verify.
4. **Physical intuition:** Lower orbit → smaller r → faster speed → shorter period. Higher orbit → slower, longer period. Geostationary orbit (T = 24 h) is at r ≈ 42,000 km.
