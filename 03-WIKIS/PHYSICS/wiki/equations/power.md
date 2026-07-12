---
type: equation
status: draft
---

# Power

## Equations

**Average power (from work and time):**
```
P_avg = W / Δt
```

**Instantaneous power (from force and velocity):**
```
P = F v cos θ
```

**Simplified (when F is parallel to v):**
```
P = Fv
```

**Calculus form:**
```
P = dW/dt = dE/dt
```

## Meaning in Plain English

Power tells you how fast energy is being transferred or work is being done. A machine with high power can do the same job faster, or do more work in the same time.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| P | power | W = J/s |
| W | work done | J |
| Δt | time elapsed | s |
| F | force applied | N |
| v | speed of object | m/s |
| θ | angle between F and v | degrees or rad |

## Units Check

P = W/Δt → J/s = W (watt) ✓

P = Fv → N × m/s = N·m/s = J/s = W ✓

1 horsepower = 746 W ≈ 750 W (good to know for conversions)

## When to Use It

- Given force and speed: use P = Fv (if F ∥ v)
- Given work done and time taken: use P = W/Δt
- Given power and time: find work done with W = P × Δt
- Given power and force: find speed with v = P/F

## When Not to Use It

- When you need total energy stored (use E_mech = K + U instead).
- Power alone doesn't tell you how much total energy has been transferred — you need both P and Δt.

## Required Assumptions

- For P = Fv: the force must be constant and parallel to the velocity (or θ must be known).
- For P = W/Δt: W is the net work done during Δt.

## Calculus Origin

P = dW/dt is a derivative — power is the instantaneous rate of doing work. In most Stage 8 problems, force and velocity are constant so the average and instantaneous forms give the same result.

## Example Problem Type

A car engine produces a driving force of 4000 N at a speed of 30 m/s. Find the power output. → P = Fv = 4000 × 30 = 120 000 W = 120 kW.

## Common Mistake

**Forgetting to divide by time.** W = Fd gives work (joules), not power. Power always involves time: P = W/Δt.

**Using P = Fv when F is not parallel to v.** If force and velocity point in different directions, you must use P = Fv cos θ.
