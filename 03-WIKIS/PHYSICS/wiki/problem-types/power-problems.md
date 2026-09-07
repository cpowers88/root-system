---
type: problem-type
timeline: reference
status: draft
---

# Power Problems

## How to Recognize This Problem Type

The problem mentions watts, horsepower, "rate of doing work," "how long does it take," or gives you force + speed and asks for power (or gives power and asks for force or speed). Any time rate-of-energy-transfer appears, you are in a power problem.

**Keywords:** watts (W), kilowatts (kW), horsepower (hp), "rate," "how long," "how fast does the engine do work," "what force at this speed."

## Given Information Usually Present

- Work done (or energy transferred) and time: use P = W/Δt
- Force and speed: use P = Fv
- Power and time: find total energy/work W = PΔt
- Power and force: find speed v = P/F

## Unknown Usually Requested

- Power output (in W or kW)
- Time needed to do a specified amount of work
- Force an engine exerts at a given speed
- Speed a vehicle reaches against a given resistance force at a given power

## Diagram to Draw

Usually none. For vehicle problems, draw a free-body diagram to identify the driving force and any resistive forces. In steady-state (constant speed), net force = 0, so driving force = resistive force.

```
Vehicle at constant speed:
   F_engine  →  [car]  ← F_resistance
   Net F = 0 (constant v)
   P = F_engine × v
```

## Equations Commonly Used

```
P_avg = W / Δt       (given work and time)
P = Fv               (given force and speed, F ∥ v)
P = Fv cos θ         (if F not parallel to v)
W = P × Δt           (find work from power and time)
v = P / F            (find speed from power and force)
F = P / v            (find force from power and speed)
1 hp = 746 W
```

## Step-by-Step Solving Pattern

**If given W and Δt:**
1. P = W / Δt. Convert units as needed (J and s give W).

**If given F and v:**
1. Is F parallel to v? If yes: P = Fv. If no: P = Fv cos θ.

**If given P and time Δt:**
1. W = P × Δt. This gives total energy transferred.

**If given P and the problem has a vehicle at constant speed:**
1. Draw FBD. At constant speed, F_drive = F_resistance.
2. Use P = F_drive × v to find either F or v.

## Unit Checks

- P = W/Δt: J/s = W ✓
- P = Fv: N × m/s = J/s = W ✓
- W = PΔt: W × s = J ✓

## Common Traps

1. **Forgetting to convert horsepower to watts.** 1 hp = 746 W. Don't leave the answer in hp if the equation requires SI units.
2. **Confusing energy (J) with power (W).** A 1000 W motor can deliver 1000 J in 1 second — but that's energy. Power tells you the rate, not the total.
3. **Assuming constant power means constant force.** If the vehicle speeds up, v increases so F = P/v decreases (engine must work less hard at higher speed to maintain the same power output).
4. **Using net force vs. driving force.** If a car accelerates, F_net ≠ F_engine. If asked for engine power, use F_engine × v. If asked for power delivered to acceleration, use F_net × v.

## Practice Drills

- [[../drills/power-drill]]

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 8.5.
