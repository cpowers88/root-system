---
type: concept
status: draft
---

# Power

## What Is the Physical Idea?

Power measures how fast work is done or how fast energy is transferred. Two systems may do the same total work, but the faster one delivers more power. A sports car and a slow truck may both eventually reach highway speed, but the sports car does it with much higher power output.

## What Real-World Situation Does It Describe?

- A motor lifting a box: more powerful motor = same height, less time.
- An athlete sprinting vs. walking: same displacement, but sprinting requires much greater power.
- A light bulb: 100 W means 100 joules of electrical energy converted to light + heat every second.
- Engine ratings: car engines rated in horsepower or watts.

## Objects / System Involved

Any system where energy is being transferred or work is being done over a time interval.

## Quantities That Change

Energy (or work done) changes over time. Power is the rate of that change.

## Model / Equation

**Average power:**
```
P_avg = W / Δt = ΔE / Δt
```

**Instantaneous power (force and velocity):**
```
P = F v cos θ
```
Where θ is the angle between the force vector and velocity vector.

**Simplest case (F parallel to v, θ = 0):**
```
P = Fv
```

**Calculus form:**
```
P = dW/dt = dE/dt
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| P | power | W (watt) = J/s |
| W | work done | J |
| Δt | time interval | s |
| F | applied force | N |
| v | speed of the object | m/s |
| θ | angle between F and v | degrees or rad |

**Unit conversions:**
- 1 W = 1 J/s
- 1 kW = 1000 W
- 1 hp (horsepower) = 746 W ≈ 750 W

## Calculus Connection

P = dW/dt and P = dE/dt — power is the derivative of work (or energy) with respect to time. This is the only calculus idea introduced in Stage 8.

When force is constant and the object moves at constant velocity, P = Fv is all you need. When either varies, use the derivative.

## Diagram / Visual Model

None needed — power problems are algebraic. The key is identifying which form of the power equation applies: do you have work + time? Or force + velocity?

```
If you know W and Δt:   use P = W/Δt
If you know F and v:    use P = Fv  (if F ∥ v)
If you know P and v:    solve for F = P/v
If you know P and F:    solve for v = P/F
```

## Problem Types That Use This

- [[../problem-types/power-problems]]

## Common Beginner Mistake

**Confusing energy with power.** Energy (joules) is a total amount; power (watts) is a rate. A 100 W bulb doesn't "have" 100 joules — it *uses* 100 joules per second. You can have a lot of power with very little total energy (short burst) or very little power with a large total energy (slow process).

Second trap: forgetting to use θ in P = Fv cos θ when the force is not parallel to velocity. If a car engine pushes the car forward but wind resistance acts backward, only the net force dotted with velocity gives net power.

## Practice Next

See [[../drills/power-drill]].

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 8.5.
