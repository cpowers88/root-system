---
type: worked-example
stage: 11
---

# Worked Example: The Spinning Skater

## Physical Situation

A figure skater spins on frictionless ice with arms extended. She pulls her arms in close to her body. Find her new angular velocity and her new kinetic energy. Compare with the initial kinetic energy.

## Why Angular Momentum is Conserved

The ice exerts no torque on the skater (frictionless pivot, and the normal force passes through her rotation axis). There are no external torques, so angular momentum L = Iω is conserved.

## Given

- Initial moment of inertia (arms out): Iᵢ = 4.0 kg·m²
- Initial angular velocity: ωᵢ = 2.0 rad/s
- Final moment of inertia (arms pulled in): If = 1.5 kg·m²
- Find: ωf, KE_i, KE_f

## Diagram

```
Arms out:                      Arms in:
  [o]                           [o]
 /   \   ωᵢ = 2.0 rad/s        | |   ωf = ?
I = 4.0 kg·m²                  I = 1.5 kg·m²
```

## Step 1: Apply Conservation of Angular Momentum

```
Lᵢ = Lf
Iᵢωᵢ = Ifωf
```

Solving for ωf:

```
ωf = (Iᵢ/If) · ωᵢ = (4.0/1.5) · 2.0 = 2.667 · 2.0 ≈ 5.33 rad/s
```

The skater spins about 2.67 times faster after pulling in her arms.

## Step 2: Calculate Initial Kinetic Energy

```
KE_i = ½Iᵢωᵢ² = ½(4.0)(2.0)² = ½(4.0)(4.0) = 8.0 J
```

## Step 3: Calculate Final Kinetic Energy

```
KE_f = ½Ifωf² = ½(1.5)(5.33)² = ½(1.5)(28.4) = 21.3 J
```

## Step 4: Compare Kinetic Energies

```
ΔKE = KE_f − KE_i = 21.3 − 8.0 = +13.3 J
```

The kinetic energy increased by 13.3 J — about 2.7 times the original KE.

## Where Did the Extra Energy Come From?

The extra 13.3 J came from the skater's muscles doing internal work as she pulled her arms inward against the centrifugal tendency. Angular momentum is conserved (no external torque), but mechanical energy is NOT conserved because internal biological work is done.

This is why the skater feels more tired after the spin — she expended real muscular energy.

## The Pattern (L = Iω conserved, I decreases)

```
Lᵢ = Lf     →    Iᵢωᵢ = Ifωf     →     ωf/ωᵢ = Iᵢ/If

KE = L²/(2I)    →    as I decreases, KE increases
```

When I decreases, ω increases proportionally, and KE increases by the same factor as I decreases. If I is halved, ω doubles and KE doubles.

## Key Lessons

1. Angular momentum conservation (not energy conservation) applies when there is no external torque.
2. Internal work can change kinetic energy even in a system with conserved angular momentum.
3. The ratio ωf/ωᵢ = Iᵢ/If — memorize this relationship for the spinning-skater class of problems.
4. Always state why the conservation law applies before using it.
