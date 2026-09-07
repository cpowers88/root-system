---
type: problem-type
timeline: reference
status: draft
---

# Problem Type — Orbital Motion and Gravitation

## How to Recognize It

A moon, satellite, or planet moves in a circular (or approximately circular) orbit around a central body. May involve: period, orbital radius, speed, escape speed, Kepler's third law, or gravitational force. Signal words: "satellite," "orbit," "moon," "period," "orbital speed," "escape."

## Typical Given Information

- Mass of the central body M (or g at a known altitude)
- Orbital radius r (or altitude above surface — remember to add R_planet)
- Orbital period T (for Kepler problems) or speed

## Unknown Requested

- Orbital speed, period, altitude, mass of central body, or escape speed

## Equations

```
F_g = GMm/r²                  (gravitational force — always present)
For circular orbit: F_g = F_c  → GMm/r² = mv²/r
Orbital speed:   v_c = √(GM/r)
Orbital period:  T = 2πr/v = 2π√(r³/GM)
Kepler 3rd law:  T² = (4π²/GM) r³    [ratio form for two orbits: T₁²/T₂² = r₁³/r₂³]
Escape speed:    v_e = √(2GM/r)
```

## Solving Pattern

**For orbital speed/period from radius:**
1. Identify M (central body) and r (center-to-center orbital radius).
2. Compute v_c = √(GM/r).
3. Compute T = 2πr/v_c if period is needed.

**For Kepler comparison between two satellites around the same body:**
1. Use T₁²/T₂² = r₁³/r₂³ (M cancels, no need to know it).

**For escape speed:**
1. v_e = √(2GM/r) — set total energy to zero and solve.

## Unit Check

G in N·m²/kg², M in kg, r in m → v in m/s, T in s.

## Common Traps

- Using altitude instead of center-to-center distance for r.
- Applying Kepler's 3rd law ratios to orbits around different central bodies (the constant 4π²/GM depends on M).
- Forgetting that higher orbit → lower speed (v_c decreases as r increases).

## Drill

[[../drills/gravitation-drill]]
