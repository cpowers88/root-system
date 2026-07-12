---
type: equation
status: draft
---

# Equation — Standing Waves and Harmonics

## Equations

**Standing wave on a string (both ends fixed, or open pipe — both ends open):**
```
Allowed wavelengths:   λ_n = 2L/n,     n = 1, 2, 3, ...
Harmonic frequencies:  f_n = n × v/2L = n × f₁
Fundamental:           f₁ = v/2L
```

**Pipe closed at one end, open at the other:**
```
Allowed wavelengths:   λ_n = 4L/n,     n = 1, 3, 5, ... (ODD only)
Harmonic frequencies:  f_n = n × v/4L = n × f₁
Fundamental:           f₁ = v/4L
```

**Beat frequency (two sources with slightly different frequencies):**
```
f_beat = |f₁ − f₂|
```

## Plain-English Meanings

- Standing waves form when a wave reflects and the reflected wave interferes with the incoming wave. Nodes (zero displacement) and antinodes (maximum displacement) are fixed in space.
- Only certain wavelengths "fit" the boundary conditions — those are the harmonic frequencies.
- String/open pipe: all harmonics (n = 1, 2, 3…). Closed pipe: odd harmonics only (n = 1, 3, 5…).
- Beats: two nearby frequencies combine and the amplitude oscillates at the difference frequency — you hear a "wah-wah-wah" sound.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| L | length of string or pipe | m |
| n | harmonic number (1 = fundamental) | dimensionless |
| v | wave speed in the medium | m/s |
| λ_n | wavelength of nth harmonic | m |
| f_n | frequency of nth harmonic | Hz |
| f₁ | fundamental frequency | Hz |
| f_beat | beat frequency | Hz |

## String/Pipe Comparison Table

| System | Boundary conditions | Fundamental | Harmonics |
|---|---|---|---|
| String fixed at both ends | nodes at both ends | f₁ = v/2L | all: 1,2,3,… |
| Open pipe (both open) | antinodes at both ends | f₁ = v/2L | all: 1,2,3,… |
| Pipe closed at one end | node at closed, antinode at open | f₁ = v/4L | odd only: 1,3,5,… |

## Common Mistake

Using the open-pipe formula f_n = nv/2L for a closed pipe. The closed-pipe formula is f_n = nv/4L with odd n only.
