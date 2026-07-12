---
type: worked-example
stage: 15
---

# Worked Example: Spring-Mass SHM — Full Analysis

## Physical Situation

A 0.40 kg mass is attached to a horizontal spring with spring constant k = 64 N/m. The mass is pulled 0.15 m from the equilibrium position and released from rest at t = 0.

Find:
(a) The angular frequency ω, period T, and frequency f
(b) The position equation x(t)
(c) The velocity and acceleration equations v(t) and a(t)
(d) The maximum speed and maximum acceleration
(e) The total mechanical energy
(f) The speed when x = 0.09 m

## Step (a): Angular Frequency, Period, Frequency

```
ω = √(k/m) = √(64/0.40) = √160 = 12.65 rad/s

T = 2π/ω = 2π/12.65 = 0.497 s ≈ 0.50 s

f = 1/T = 1/0.497 = 2.01 Hz ≈ 2.0 Hz
```

## Step (b): Position Equation

The mass starts at maximum displacement (x₀ = A = 0.15 m) and is released from rest. At t = 0:
- x(0) = A → cosine starts at maximum
- v(0) = 0 → at turning point

Therefore φ = 0 and we use cosine:

```
x(t) = A cos(ωt) = 0.15 cos(12.65t) m
```

(where t is in seconds)

## Step (c): Velocity and Acceleration

Differentiate x(t):

```
v(t) = dx/dt = −Aω sin(ωt) = −(0.15)(12.65) sin(12.65t) = −1.90 sin(12.65t) m/s

a(t) = dv/dt = −Aω² cos(ωt) = −ω²x(t) = −(160)(0.15) cos(12.65t) = −24.0 cos(12.65t) m/s²
```

## Step (d): Maximum Values

```
v_max = Aω = (0.15)(12.65) = 1.90 m/s    (at x = 0, equilibrium)

a_max = Aω² = (0.15)(160) = 24.0 m/s²    (at x = ±A, turning points)
```

## Step (e): Total Mechanical Energy

```
E = ½kA² = ½(64)(0.15)² = ½(64)(0.0225) = 0.720 J
```

Check with v_max: E = ½mv_max² = ½(0.40)(1.90)² = ½(0.40)(3.61) = 0.722 J ✓ (small rounding difference)

## Step (f): Speed at x = 0.09 m

Use energy conservation:

```
½mv² + ½kx² = ½kA²
½(0.40)v² = 0.720 − ½(64)(0.09)²
0.20v² = 0.720 − 0.259
0.20v² = 0.461
v² = 2.305
v = 1.52 m/s
```

## Summary Table

| Quantity | Value |
|---|---|
| ω | 12.65 rad/s |
| T | 0.50 s |
| f | 2.0 Hz |
| A | 0.15 m |
| v_max | 1.90 m/s (at x = 0) |
| a_max | 24.0 m/s² (at x = ±A) |
| E_total | 0.720 J |
| v at x = 0.09 m | 1.52 m/s |

## Key Lessons

1. **Phase constant:** if the mass starts at maximum displacement and is released from rest, φ = 0 and x(t) = A cos(ωt). If it starts at equilibrium moving in the + direction, x(t) = A sin(ωt) [i.e., φ = −π/2 in the cosine form].
2. **Energy method:** fastest way to find speed at a specific position — skip the trig entirely.
3. **Maximum values:** v_max and a_max occur at complementary positions (equilibrium vs. turning point).
4. **Period doesn't depend on amplitude:** if A doubled to 0.30 m, ω, T, and f would be unchanged.
