---
type: equation
status: draft
---

# Gravitational Potential Energy (near Earth's surface)

## Equation

```text
U_g = mgy

Force from potential energy:  F_y = −dU_g/dy = −mg (pointing downward)
```

## Meaning in Plain English

Gravitational potential energy is stored energy associated with an object's position in Earth's gravitational field. Higher position = more stored energy. When the object falls, potential energy converts to kinetic energy.

The reference point (y = 0) can be chosen freely — only *changes* in U_g matter physically.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| U_g | gravitational potential energy | J |
| m | mass | kg |
| g | gravitational acceleration near surface | m/s² (≈ 9.80 m/s²) |
| y | height above the chosen reference point | m |

## Units Check

[U_g] = kg × (m/s²) × m = kg·m²/s² = J ✓

## Sign and Reference Point Rules

- U_g = 0 at whatever height you call y = 0. Choose a convenient point (ground, floor, table edge).
- U_g > 0 when the object is above the reference.
- U_g < 0 when the object is below the reference (like a ball on a cliff dropped below cliff level).
- Only ΔU_g = mg Δy is physically meaningful. The absolute value of U_g depends on reference choice.

## When to Use It

- Any time an object moves vertically (or has a vertical component of displacement).
- As part of total mechanical energy E = K + U in Stage 8.

## When Not to Use It

- At heights far from Earth's surface — use the general form U_g = −GMm/r (Stage 13, Universal Gravitation).
- When height is zero throughout (U_g doesn't change, so it cancels out of the problem).

## Required Assumptions

Object is near Earth's surface (g is approximately constant). This breaks down for heights comparable to Earth's radius (~6400 km).

## Calculus Origin

The general relationship F = −dU/dx shows that:

```text
F_y = −dU_g/dy = −d(mgy)/dy = −mg
```

This gives the downward gravitational force, confirming the equation is consistent with gravity.

## Connection to Conservative Forces

Gravity is conservative because the work it does depends only on the *vertical* displacement Δy, not on the path. Going up a ramp vs. straight up to the same height: gravity does the same work either way.

## Example Problem Type

"A 3.0 kg book is lifted 1.5 m above the floor. How much gravitational potential energy does it gain?"
→ ΔU_g = mgy = 3.0 × 9.80 × 1.5 = 44.1 J.

## Common Mistake

Using the slant distance (along a ramp) instead of the *vertical* height y. Gravity cares only about vertical displacement, not path length.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Equation 7.18, Section 7.6.
