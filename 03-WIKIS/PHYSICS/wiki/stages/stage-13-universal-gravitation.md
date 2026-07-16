---
type: stage
timeline: reference
stage: 13
status: draft
tags: [physics, math]
---

# Stage 13 — Universal Gravitation

## Syllabus Alignment

**Textbook:** Serway & Jewett, 10th ed. — Chapter 13
**Course:** KSU PHYS 2211, Fall 2026, Dr. Behera
**Topic coverage:** Newton's law of universal gravitation, gravitational field, gravitational potential energy, Kepler's three laws, orbital mechanics, escape speed
**Syllabus note:** "law of universal gravitation... falling objects and objects in orbital motion"

---

## Stage Goal

By the end of this stage, you will:

- Apply Newton's law of gravitation to any two masses at any separation
- Calculate gravitational field strength at any altitude or on any planet
- Use gravitational potential energy (with the correct sign) in energy conservation problems
- Calculate orbital speed, orbital period, and escape speed
- State and apply all three of Kepler's laws
- Explain why a bound orbit has negative total energy

---

## Prerequisites

Before starting this stage, you must be comfortable with:

- [[stage-5-laws-of-motion]] — Newton's second and third laws, free-body diagrams
- [[stage-6-circular-motion]] — centripetal acceleration a_c = v^2/r, centripetal force
- [[stage-7-energy-of-a-system]] and [[stage-8-conservation-of-energy]] — kinetic
  energy, potential energy, and energy conservation
- [[stage-11-angular-momentum]] — angular momentum (needed for Kepler's 2nd law)

---

## Vocabulary to Master

| Term | Plain-English Meaning |
|---|---|
| gravitational constant G | Universal number that sets how strong gravity is; G = 6.674 x 10^-11 N*m^2/kg^2 |
| gravitational field | Force per unit mass that a body creates in the space around it; points toward the mass |
| inverse square law | Force drops by factor of 4 when distance doubles; factor of 9 when distance triples |
| gravitational potential energy | Energy stored in the gravitational configuration; negative for any bound pair |
| escape speed | Minimum speed to launch an object so it never returns; total mechanical energy = 0 |
| circular orbit | Closed path where gravity provides exactly the centripetal force needed |
| orbital period T | Time for one complete orbit |
| semi-major axis a | Half the longest diameter of an ellipse; equals r for circular orbits |
| bound orbit | Orbit with total mechanical energy E < 0; the object cannot escape |
| geosynchronous orbit | Orbit whose period matches Earth's rotation; only a circular, equatorial, prograde **geostationary** orbit stays above one point |

---

## Core Equations

| Equation | What It Calculates | Notes |
|---|---|---|
| F_g = G*m1*m2/r^2 | Gravitational force | r is center-to-center distance |
| g = GM/r^2 | Field strength at distance r from center of M | g decreases as r increases |
| U_g = -G*m1*m2/r | Gravitational PE | Zero at r -> infinity; negative everywhere else |
| v_esc = sqrt(2GM/R) | Escape speed from surface of M, radius R | Set E_total = 0 |
| v_orbit = sqrt(GM/r) | Circular orbital speed | Derived from F_g = mv^2/r |
| T^2 = (4*pi^2/GM)*r^3 | Orbital period (Kepler's 3rd law) | M = mass of central body |
| E_total = -G*M*m/(2r) | Total mechanical energy of circular orbit | Always negative (bound) |

---

## Constants You Must Know

| Symbol | Value | Units |
|---|---|---|
| G | 6.674 x 10^-11 | N*m^2/kg^2 |
| M_Earth | 5.972 x 10^24 | kg |
| R_Earth | 6.371 x 10^6 | m |
| g_surface | 9.80 | m/s^2 |
| M_Sun | 1.989 x 10^30 | kg |

---

## Variables and Units

| Symbol | Quantity | SI Unit | Notes |
|---|---|---|---|
| F_g | Gravitational force | N | Attractive; both masses feel equal magnitude |
| G | Gravitational constant | N*m^2/kg^2 | 6.674 x 10^-11 |
| m1, m2 | Masses of two bodies | kg | Any positive value |
| r | Center-to-center distance | m | Includes planet radius if object is on surface |
| g | Gravitational field / free-fall acceleration | m/s^2 or N/kg | 9.80 at Earth's surface |
| U_g | Gravitational potential energy | J | Always <= 0 with this formula |
| v_esc | Escape speed | m/s | ~11,200 m/s for Earth |
| v_orbit | Orbital speed | m/s | ~7,900 m/s for low Earth orbit |
| T | Orbital period | s | Convert hours or days to seconds |
| E | Total mechanical energy | J | Negative for bound orbits |

---

## Physical Situation: What Is Happening?

Any two objects with mass attract each other through gravity. This is not just Earth pulling down on you — it is you pulling up on Earth with the same force magnitude (Newton's 3rd law).

The attraction weakens quickly with distance (inverse square law), but it never fully disappears.

When an object is launched fast enough, it can escape the gravitational pull permanently. When it moves too slowly to escape, it enters a bound orbit — a closed path where gravity continuously curves the trajectory back around.

Planets, moons, and satellites all move in these bound orbits. The entire solar system is held together by this one force.

---

## Conceptual Flow

```
Two masses exist in the universe
        |
        v
They attract: F_g = G*m1*m2/r^2   (inverse square law)
        |
        v
Each mass creates a gravitational field: g = GM/r^2
        |
        v
Moving a test mass through the field stores/releases energy
        |
        v
Gravitational PE: U_g = -GMm/r   (zero at infinity)
        |
        v
Launched object escapes when total energy >= 0
Escape: (1/2)mv^2 + (-GMm/R) = 0  ->  v_esc = sqrt(2GM/R)
        |
        v
Object moving sideways at the right speed orbits:
F_g = mv^2/r  ->  v_orbit = sqrt(GM/r)
        |
        v
Period follows Kepler's 3rd law: T^2 = (4*pi^2/GM)*r^3
        |
        v
Total orbital energy: E = -GMm/(2r)  (negative = bound)
```

---

## Diagrams

### Diagram 1 — Inverse Square Force

```
    m1 <--F-----------------------------F--> m2
                         r

    Forces attract: arrows point toward the other mass
    Double r -> Force becomes (1/4) of original
    Triple r -> Force becomes (1/9) of original
```

### Diagram 2 — Gravitational Field Strength vs. Altitude

```
    g (m/s^2)
    9.80 |*
         | *
         |  *
         |    *
         |       *
         |            *
    0    |_____________________  r (distance from Earth center)
         R_E   2R_E    3R_E

    g = GM_E / r^2   (falls off as 1/r^2)
```

### Diagram 3 — Circular Orbit

```
         v ->  (tangent to circle, perpendicular to r)
        *
       /|
      / |
     /  | F_g (toward center, provides centripetal force)
    /   v
   * M  *      orbit circle
    \
     *
```

Velocity is always perpendicular to the radius.
Gravity provides centripetal force. Speed is constant throughout.

### Diagram 4 — Energy vs. Orbital Radius

```
  Energy
    +
    |    KE = +GMm/(2r)   (positive, decreases as r increases)
    |
    0 --------------------------------------------- r
    |
    |    E_total = -GMm/(2r)  (negative, less negative as r grows)
    |
    |    U = -GMm/r           (negative, twice as large as E_total)
    -

    Note: U = 2 * E_total  (at all radii for circular orbits)
```

---

## Calculus Connections

### Where Does U_g = -GMm/r Come From?

Potential energy equals the negative of the work done by gravity bringing mass m from infinity to r:

    U(r) = -W_grav = -INT[inf to r] F_g dr

    With F_g = -GMm/r^2 (force opposes increasing r in 1D radial):

    U(r) = INT[inf to r] (GMm/r^2) dr = GMm[-1/r] from inf to r = -GMm/r

The negative sign tells you that pulling two masses apart from r to infinity requires positive work input — you must add energy to break the bond.

### Why g = GM/r^2 From Newton's Law

Gravitational field is force per unit test mass:

    g = F_g / m = (GMm/r^2) / m = GM/r^2

This is the free-fall acceleration any mass experiences at distance r from center of M.

### Kepler's 2nd Law and Angular Momentum

Angular momentum: L = m * v_perp * r

In a gravity-only orbit, the torque about the center is zero (force is radial):
    tau = dL/dt = 0   so   L = constant

Equal areas swept in equal times is a direct geometric consequence of constant L.
At perihelion (closest): r small, v large.
At aphelion (farthest): r large, v small.
L = m*v*r stays the same.

---

## Concept Pages

- [[../concepts/gravitational-field]]
- [[../concepts/keplers-laws]]
- [[../concepts/orbital-energy]]

## Equation Pages

- [[../equations/newtons-gravitation-law]]
- [[../equations/gravitational-potential-energy]]
- [[../equations/orbital-mechanics]]

## Problem-Type Pages

- [[../problem-types/orbital-mechanics-problems]]
- [[../problem-types/surface-gravity-variation]]

## Worked Examples

- [[../worked-examples/satellite-orbit-period]]
- [[../worked-examples/escape-speed-calculation]]

## Flashcards

[[../flashcards/stage-13-universal-gravitation]]

## Common Errors

[[../common-errors/stage-13-universal-gravitation]]

## Drills

[[../drills/gravitation-drill]]

---

## Mastery Checklist

Work through this list in order. Do not check a box until you can do it without looking.

- [ ] Write Newton's law of gravitation from memory and identify every symbol
- [ ] Explain the inverse square law using a specific numerical example
- [ ] Calculate the gravitational force between Earth and Moon (given masses and distance)
- [ ] Show algebraically that g = GM_E/R_E^2 = 9.80 m/s^2
- [ ] Calculate g at an altitude of 500 km above Earth's surface
- [ ] Explain why U_g is negative and what U = 0 means physically
- [ ] Calculate escape speed from Earth's surface from scratch
- [ ] Explain why total orbital energy is negative for a bound orbit
- [ ] Derive v_orbit by setting gravitational force equal to centripetal force
- [ ] Calculate the orbital period of the ISS (altitude approximately 400 km)
- [ ] State all three of Kepler's laws in plain English without looking at notes
- [ ] Use Kepler's 3rd law to find the period of a planet given its orbital radius
- [ ] Explain why a satellite in a higher orbit moves more slowly
- [ ] Solve a conservation-of-energy problem involving escape from a planet

---

## Do Not Move On Until

1. You can derive v_orbit = sqrt(GM/r) from first principles using Newton's 2nd law.
2. You can calculate orbital period for any circular orbit using T^2 = (4*pi^2/GM)*r^3.
3. You understand why a satellite that gains energy moves to a higher, slower orbit.
4. You can calculate escape speed for Earth and for any planet given mass and radius.
5. You can explain Kepler's 2nd law using angular momentum conservation.

---

## Parked Advanced Topics

| Topic | Why Parked | Prerequisite Needed | Unlock Condition |
|---|---|---|---|
| Elliptical orbit full mechanics | Requires conic section treatment | Advanced calculus | Later courses |
| Tidal forces | Requires gradient of gravitational field | Multivariable calculus | After PHYS 2212 |
| General relativistic corrections | Beyond classical mechanics scope | Modern physics course | Upper-division |
| Gravitational slingshot | Requires 3-body problem methods | Numerical methods | Engineering electives |
| Roche limit | Requires tidal force derivation | Graduate-level math | Graduate physics |
| Lagrange points | Rotating reference frame required | Classical mechanics II | PHYS 3xxx |
