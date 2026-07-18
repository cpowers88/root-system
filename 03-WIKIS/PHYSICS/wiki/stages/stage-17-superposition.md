---
type: stage
timeline: later
stage: 17
status: draft
tags: [physics, math]
---

# Stage 17 — Superposition and Standing Waves

## One-Sentence Goal

Understand how two waves combine algebraically, produce constructive and destructive interference and standing waves, and calculate harmonic frequencies for strings and pipes.

---

## Syllabus Alignment

- Topic: Superposition and Standing Waves
- Chapter: Serway & Jewett, 10th ed., Ch 17, sections 17.1–17.7
- Lectures: correspond to the "Waves" topic block (follow Stage 16)
- Exam relevance: standing wave harmonics and beats are standard multiple-choice and free-response problems

---

## Textbook Alignment

| Section | Topic |
|---------|-------|
| 17.1 | Waves in interference |
| 17.2 | Standing waves |
| 17.3 | Boundary effects: reflection and transmission |
| 17.4 | Waves under boundary conditions |
| 17.5 | Resonance |
| 17.6 | Standing waves in air columns |
| 17.7 | Beats: interference in time |
| 17.8 | Parked: nonsinusoidal waveforms and Fourier series |

---

## Prerequisite Physics

| Stage | What You Must Know |
|-------|--------------------|
| Stage 16 | Wave function y = A sin(kx − ωt): what k, ω, A, λ, f, T mean |
| Stage 16 | Wave speed on string: v = √(T/μ) |
| Stage 16 | Sound speed in air: v ≈ 343 m/s at 20°C |
| Stage 16 | Relationship: v = fλ |

If any of those feel uncertain, go back to Stage 16 before continuing.

---

## Prerequisite Math

- Trig identity: sin A + sin B = 2 sin((A+B)/2) cos((A−B)/2)
- This is used once to derive the standing wave formula. You do not need to reproduce it, but you must understand what the result means.
- Basic algebra and unit analysis.
- No new calculus in this stage.

---

## Core Concepts (Links)

- [[../concepts/superposition-principle]]
- [[../concepts/interference]]
- [[../concepts/standing-waves]]
- [[../concepts/beats]]

---

## Vocabulary

| Term | Plain-English Meaning |
|------|-----------------------|
| Superposition | When two waves overlap, their displacements add at every point |
| Constructive interference | Waves add up — resultant amplitude is larger |
| Destructive interference | Waves cancel — resultant amplitude is smaller or zero |
| Standing wave | A wave pattern with fixed nodes and antinodes that does not travel |
| Node | A point on a standing wave that never moves — zero displacement always |
| Antinode | A point on a standing wave with the largest oscillation |
| Harmonic | An allowed resonant frequency of the system; n = 1 is the fundamental |
| Fundamental frequency (f₁) | The lowest allowed frequency; also called the first harmonic |
| Beat | A slow pulsing in loudness caused by two slightly different frequencies |
| Beat frequency | How many beats per second; equals the frequency difference |
| Open end (pipe) | A pipe end open to air — always a displacement antinode |
| Closed end (pipe) | A sealed pipe end — always a displacement node |
| Linear mass density (μ) | Mass per unit length of a string, in kg/m |

---

## Equations

### Superposition Principle

```
y_total(x, t) = y₁(x, t) + y₂(x, t)
```

At every point x and every instant t, just add the individual displacements. This is all superposition is — algebraic addition.

---

### Standing Wave Formula (on a string)

```
y(x, t) = 2A sin(kx) cos(ωt)
```

This result comes from adding two traveling waves going in opposite directions:
- y₁ = A sin(kx − ωt) going right
- y₂ = A sin(kx + ωt) going left

The sin(kx) part fixes the node locations in space. The cos(ωt) part makes every point oscillate in time. No part of this wave travels — it is stationary.

---

### Standing Waves — String Fixed at Both Ends

Boundary condition: both ends must be nodes.

```
Allowed wavelengths:   λ_n = 2L / n          n = 1, 2, 3, ...

Harmonic frequencies:  f_n = n × v / (2L)    n = 1, 2, 3, ...
```

ALL positive integers are allowed. n = 1 is the fundamental (lowest frequency).

---

### Standing Waves — Pipe Open at Both Ends

Both ends are antinodes (air is free to move). Same boundary as string → same formula.

```
f_n = n × v / (2L)    n = 1, 2, 3, ...
```

ALL harmonics allowed.

---

### Standing Waves — Pipe Open at One End, Closed at the Other

Closed end = node. Open end = antinode. This geometry only fits odd quarter-wavelengths.

```
f_n = n × v / (4L)    n = 1, 3, 5, ... (ODD only)
```

ODD harmonics only. No even harmonics exist in this pipe.

---

### Beat Frequency

```
f_beat = |f₁ − f₂|
```

The absolute value ensures f_beat is always positive. The number of beats per second equals how many times per second the two waves go in and out of phase.

---

### Wave Speed on String (from Stage 16)

```
v = √(T / μ)
```

Needed to calculate f_n for string problems.

---

### Sound Speed in Air (from Stage 16)

```
v ≈ 343 m/s at 20°C
```

Needed to calculate f_n for pipe problems.

---

## Variables and Units

| Symbol | Meaning | Unit |
|--------|---------|------|
| y | Displacement of medium at point x, time t | m |
| y₁, y₂ | Individual wave displacements | m |
| y_total | Total displacement (superposition result) | m |
| A | Amplitude of each individual wave | m |
| k | Wave number = 2π/λ | rad/m |
| ω | Angular frequency = 2πf | rad/s |
| x | Position along the medium | m |
| t | Time | s |
| f_n | Frequency of the nth harmonic | Hz |
| f₁ | Fundamental frequency (first harmonic) | Hz |
| n | Harmonic number (positive integer) | dimensionless |
| v | Wave speed in the medium | m/s |
| L | Length of string or pipe | m |
| λ_n | Wavelength of the nth harmonic | m |
| T | Tension in string | N |
| μ | Linear mass density of string | kg/m |
| f₁, f₂ | Two close frequencies producing beats | Hz |
| f_beat | Beat frequency = |f₁ − f₂| | Hz |

---

## Diagrams

### Standing Wave Modes — String Fixed at Both Ends

```
n = 1  Fundamental (1 antinode, nodes at both ends)
                                         λ = 2L
         A
    _____|_____
   /           \
  /             \
N                 N
|<——————L————————>|

n = 2  Second harmonic (2 antinodes, 3 nodes)
                                         λ = L
       A         A
  ____|____   ____|____
 /         \ /         \
N           N            N
|<——————L————————————————>|

n = 3  Third harmonic (3 antinodes, 4 nodes)
                                         λ = 2L/3
     A      A      A
  __|__   __|__   __|__
 /     \ /     \ /     \
N        N       N        N
|<——————L————————————————————>|

Rule: L = n × (λ/2)  →  the string holds exactly n half-wavelengths.
```

---

### Standing Wave Modes — Open-Closed Pipe

```
OPEN end = displacement ANTINODE (A)
CLOSED end = displacement NODE (N)

n = 1  Fundamental (λ = 4L)
  A ~~~~~~~~~~~~~~~~~~~~~~~~~~~ N
  |<————————— L = λ/4 —————————>|

n = 3  Third harmonic (λ = 4L/3)
  A ~~~~~~~~ N ~~~~~~~~ A ~~~~~~ N
  |<————————— L = 3λ/4 ————————>|

n = 5  Fifth harmonic (λ = 4L/5)
  A ~~~~ N ~~~~ A ~~~~ N ~~~~ A ~~~~ N
  |<————————— L = 5λ/4 ————————>|

n = 2 is NOT ALLOWED:
  Would require the closed end to be an antinode — impossible.
```

---

### Constructive vs. Destructive Interference

```
CONSTRUCTIVE (waves in phase — peaks align):
  Wave 1:   /\/\/\/\/\
  Wave 2:   /\/\/\/\/\
  Total:   /\/\/\/\/\/\   ← amplitude 2A (larger peaks)

DESTRUCTIVE (waves 180° out of phase — peak meets trough):
  Wave 1:   /\/\/\/\/\
  Wave 2:   \/\/\/\/\/
  Total:   ————————————   ← amplitude zero (flat line)
```

---

### Beats — Amplitude Envelope

```
f₁ slightly different from f₂:

  Wave 1:  |||||||||||||||||||||||||||||||||||
  Wave 2:  ||| ||| ||| ||| ||| ||| ||| ||| |

  Combined (listen for loudness pulsing):
  LOUD    quiet   LOUD    quiet   LOUD    quiet
  |||||||  .....  |||||||  .....  |||||||  .....

  One beat = one loud-quiet-loud cycle
  f_beat = |f₁ − f₂| beats per second
```

---

## Calculus Connections

No new calculus is introduced in Stage 17.

- Superposition is algebraic: y_total = y₁ + y₂. No derivatives, no integrals.
- The standing wave formula y = 2A sin(kx)cos(ωt) is derived using a trig identity, not calculus.
- The Stage 16 ideas of ∂y/∂t (transverse velocity) and ∂²y/∂x² (wave equation) still apply to standing waves if needed, but are not new here.
- Fourier series — decomposing a complex waveform into harmonics — does use integrals. That topic is parked.

---

## Problem Types

- [[../problem-types/standing-wave-harmonics]] — finding f₁, f₂, f₃... for strings and pipes
- [[../problem-types/beats-problems]] — finding f_beat, identifying unknown frequency

---

## Worked Examples

- [[../worked-examples/guitar-string-harmonics]] — full harmonic series for a string with given T, μ, L
- [[../worked-examples/open-closed-pipe]] — resonant frequencies for a 0.5 m closed pipe

---

## Drills

- [[../drills/standing-waves-drill]] — 7 harmonic problems
- [[../drills/beats-interference-drill]] — 5 beat and interference problems

---

## Common Errors

See [[../common-errors/stage-17-superposition]]

Top traps:
1. Applying f_n = nv/4L to an open-open pipe (wrong — that's open-closed).
2. Using even n in the open-closed pipe formula.
3. Swapping node and antinode definitions.
4. Forgetting the absolute value in f_beat = |f₁ − f₂|.
5. Computing f_n without first computing v from v = √(T/μ) for a string.

---

## Flashcards

See [[../flashcards/stage-17-superposition]] — 14 Q&A cards.

---

## Mastery Checklist

Before moving on, Chris must be able to:

- [ ] State the superposition principle in one sentence without looking at notes.
- [ ] Explain the difference between constructive and destructive interference using the word "phase."
- [ ] Draw a standing wave for n = 1, 2, and 3 on a fixed string. Label every node and antinode.
- [ ] Write f_n = nv/(2L) from memory. State what n, v, and L mean with correct units.
- [ ] Write f_n = nv/(4L) and state which pipe it applies to, and why n must be odd.
- [ ] Given L = 0.8 m, T = 80 N, μ = 0.005 kg/m for a string: compute v, then f₁, f₂, f₃.
- [ ] Given L = 0.6 m for an open-open pipe: compute f₁, f₂, f₃ (use v = 343 m/s).
- [ ] Given L = 0.6 m for an open-closed pipe: compute f₁, f₃, f₅.
- [ ] Given f₁ = 440 Hz and f₂ = 437 Hz: compute f_beat and describe what you would hear.
- [ ] Explain in plain English why a closed pipe cannot have even harmonics.

---

## Do Not Move On Until

- You can solve all 7 standing wave drill problems without looking at formulas.
- You can solve all 5 beat/interference drill problems correctly.
- You can explain the node/antinode boundary conditions for all three cases (string, open-open pipe, open-closed pipe) from memory.
- You can draw and label a standing wave pattern for any given harmonic n.

---

## Parked Material

| Topic | Source | Why Parked | Unlock Condition |
|-------|--------|-----------|------------------|
| Fourier series and nonsinusoidal waveforms | Serway §17.8 | Requires integration beyond the packet's assessed core | After the course scope is confirmed or during later mathematics |
| Normal mode analysis for 2D systems | Advanced mechanics | Requires linear algebra | After linear algebra |
| Resonance with damping (driven oscillator) | Serway Ch 15 extension | Requires differential equations | After ODEs course |
| Chladni patterns (2D standing waves) | Demonstration physics | Conceptually interesting but not examined | Any time for fun |

---

*Stage 17 of the PHYS 2211 offline study packet — built for 10-day cruise, 2026.*
