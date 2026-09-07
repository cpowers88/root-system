---
type: problem-type
timeline: reference
status: draft
---

# Problem Type — Simple Harmonic Motion (Spring-Mass and Pendulum)

## How to Recognize It

An object oscillates back and forth around an equilibrium position. Signal words: "spring," "oscillates," "period," "frequency," "amplitude," "simple harmonic," "pendulum." The key condition: restoring force ∝ displacement (F = −kx for spring, or F = −(mg/L)x for pendulum small angle).

## Typical Given Information

- Spring constant k and mass m, OR pendulum length L
- Amplitude A and/or initial position x₀ and velocity v₀
- Period T or frequency f or angular frequency ω
- Position at a specific time, or time to reach a specific position

## Unknown Requested

- Period, frequency, amplitude, position at time t, speed at a given position, maximum speed/acceleration, total energy

## Equations

```
ω = √(k/m)            (spring)
ω = √(g/L)            (pendulum, small angle)
T = 2π/ω = 2π√(m/k)   or   2π√(L/g)
f = 1/T

x(t) = A cos(ωt + φ)
v(t) = −Aω sin(ωt + φ)
a(t) = −Aω² cos(ωt + φ) = −ω²x

E = ½kA² = ½mv² + ½kx²    (energy at any position)
v = ω√(A² − x²)            (speed at position x)
```

## Solving Pattern

**Period/frequency from system parameters:**
1. Identify k, m (or L) → ω → T → f.

**Position as function of time:**
1. Find A and ω.
2. Apply initial conditions: x₀ = A cos φ, v₀ = −Aω sin φ → solve for φ.
3. Write x(t) = A cos(ωt + φ).

**Speed at a given position:**
1. Use energy: v = ω√(A² − x²). No need to find φ.

**Maximum speed and acceleration:**
1. v_max = Aω (at x = 0); a_max = Aω² (at x = ±A).

## Unit Check

k in N/m, m in kg → ω in rad/s, T in s. Energy in J. Position in m, speed in m/s.

## Common Traps

- Confusing T and ω: T = 2π/ω, NOT 1/ω.
- Applying the pendulum formula T = 2π√(L/g) for angles > ~15° (it overestimates frequency).
- Using K = ½mv² for the total energy instead of ½kA² (total energy stays constant; using K alone gives the energy only at x = 0).
- Forgetting the phase constant φ when x₀ ≠ A (object doesn't start at maximum displacement).

## Drill

[[../drills/shm-equations-drill]]
