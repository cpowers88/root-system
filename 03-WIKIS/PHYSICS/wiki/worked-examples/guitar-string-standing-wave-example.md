---
type: worked-example
stage: 17
---

# Worked Example: Guitar String — Standing Waves and Harmonics

## Physical Situation

A guitar string is 0.640 m long and has a linear mass density μ = 4.00×10⁻³ kg/m. It is under a tension of F_T = 360 N.

Find:
(a) The wave speed on the string
(b) The fundamental frequency (1st harmonic)
(c) The frequencies of the 2nd and 3rd harmonics
(d) The wavelengths of all three harmonics
(e) Sketch the standing wave patterns for n = 1, 2, 3

## Part (a): Wave Speed

For a wave on a string under tension:

```
v = √(F_T / μ) = √(360 / 4.00×10⁻³) = √(90,000) = 300 m/s
```

## Part (b): Fundamental Frequency (n = 1)

Both ends are fixed — both are nodes. The fundamental mode has ONE half-wavelength fitting in the string length:

```
L = λ₁/2  →  λ₁ = 2L = 2(0.640) = 1.28 m

f₁ = v/λ₁ = 300/1.28 = 234 Hz
```

Or directly: f₁ = v/(2L) = 300/(2×0.640) = 234 Hz

## Part (c): 2nd and 3rd Harmonic Frequencies

```
f₂ = 2f₁ = 2(234) = 468 Hz

f₃ = 3f₁ = 3(234) = 703 Hz
```

All harmonics are integer multiples of f₁.

## Part (d): Wavelengths

```
λ_n = 2L/n

λ₁ = 2(0.640)/1 = 1.28 m

λ₂ = 2(0.640)/2 = 0.640 m = L (one full wavelength fits in the string)

λ₃ = 2(0.640)/3 = 0.427 m
```

## Part (e): Standing Wave Patterns

```
n = 1 (fundamental — one loop):
   ___
  /   \
 /     \
|-------| ← string, length L
Nodes: both ends (2 nodes total)
Antinodes: 1 (center)

n = 2 (2nd harmonic — two loops):
  ___   ___
 /   \ /   \
/     X     \
|-----+-----| 
Nodes: both ends + midpoint (3 nodes total)
Antinodes: 2

n = 3 (3rd harmonic — three loops):
  _ _ _
 / / \ \
/ /   \ \
|--+---+--| 
Nodes: 4 total (both ends + 2 interior)
Antinodes: 3
```

## General Pattern

For mode n:
- Number of loops (antinodes): n
- Number of nodes: n + 1
- Wavelength: λ_n = 2L/n
- Frequency: f_n = n × f₁

## What Makes a Guitar Sound Different on Different Strings?

The strings have different μ (linear mass density) and different F_T (tension, controlled by tuning pegs). Changing either changes v, which changes f₁ = v/(2L). That's why tightening a string (increasing tension) raises the pitch — it raises v, which raises f₁.

## Key Lessons

1. **Both ends are nodes for a string fixed at both ends** — this is the boundary condition.
2. **Fundamental = first harmonic = n = 1** (one loop, one antinode).
3. **All harmonics present** for a string fixed at both ends — unlike a closed pipe which skips even harmonics.
4. **f_n = n·f₁**: harmonics are integer multiples of the fundamental.
5. **Wave speed v = √(F_T/μ)** connects string properties to frequency.
