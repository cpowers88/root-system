---
type: equation
status: draft
---

# Spring-Mass Period and Angular Frequency

## Equations

```text
ω = √(k/m)          [angular frequency, rad/s]
T = 2π√(m/k)        [period, s]
f = (1/2π)√(k/m)    [frequency, Hz]
```

## Meaning in Plain English

A heavier mass oscillates more slowly (longer period). A stiffer spring oscillates more quickly (shorter period). The period does not depend on amplitude — a big swing and a tiny swing take the same time if m and k are the same.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| ω | angular frequency | rad/s |
| T | period (time for one complete cycle) | s |
| f | frequency (cycles per second) | Hz = 1/s |
| k | spring constant (stiffness) | N/m |
| m | mass attached to spring | kg |

## Units Check

[√(k/m)] = √[(N/m) / kg] = √[(kg·m/s²/m) / kg] = √[1/s²] = 1/s = rad/s ✓

[2π√(m/k)] = √[kg / (N/m)] = √[kg·m/N] = √[kg·m/(kg·m/s²)] = √[s²] = s ✓

## When to Use It

Any time you know k and m for a spring-mass system and need the oscillation period, frequency, or angular frequency. Also use to find k if T and m are known, or to find m if T and k are known.

## When Not to Use It

Do not use for a pendulum (use T = 2π√(L/g)). Do not use if the spring has significant mass compared to the hanging mass (textbook ignores spring mass in Ch 15). Do not use if the system is overdamped or critically damped.

## Required Assumptions

- Hooke's Law applies: F = −kx (spring is not stretched beyond its elastic limit).
- Spring mass is negligible compared to mass m.
- No friction or air resistance (undamped).
- Motion is along a single axis.

## Calculus Origin

Newton's 2nd law: F = ma → −kx = m(d²x/dt²) → d²x/dt² = −(k/m)x. Comparing to the SHM condition d²x/dt² = −ω²x identifies ω² = k/m, giving ω = √(k/m). See [[../calculus-links/shm-differential-equation]].

## Example Problem Type

A 0.500 kg mass hangs on a spring with k = 20.0 N/m. Find T:

```text
T = 2π√(m/k) = 2π√(0.500/20.0) = 2π√(0.0250) = 2π(0.158) ≈ 0.993 s ≈ 1.00 s
```

## Common Mistake

Forgetting the 2π factor: writing T = √(m/k) instead of T = 2π√(m/k). This produces a value of ω, not T. Also: confusing ω (angular frequency, rad/s) with f (ordinary frequency, Hz) — ω = 2πf.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 15.2, Equations 15.13–15.14.
