---
type: problem-type
timeline: reference
stage: 9
chapter: 9
---

# Problem Type: Perfectly Inelastic Collision

## How to Recognize

Two objects collide and **stick together** — they move as one unit after the collision.

Keywords: "stick together," "couple together," "embed," "lump of clay," "ballistic pendulum" (collision phase), "train cars coupling."

## Given Information

- Masses of both objects: m₁, m₂
- Initial velocities: v₁ᵢ and v₂ᵢ (often v₂ᵢ = 0)
- Sometimes: kinetic energy lost is asked

## Unknown Requested

- Final velocity vf of the combined system
- OR kinetic energy lost in the collision

## Diagram to Draw

Before-and-after diagram:
```
Before:  [m₁ → v₁ᵢ]  [m₂ v₂ᵢ]
After:   [m₁+m₂ → vf]
```
Label the positive direction. Mark v₂ᵢ with a minus sign if it moves opposite to v₁ᵢ.

## Equations

```
m₁v₁ᵢ + m₂v₂ᵢ = (m₁ + m₂)vf
```

Solving for vf:

```
vf = (m₁v₁ᵢ + m₂v₂ᵢ) / (m₁ + m₂)
```

For kinetic energy lost:

```
ΔKE = KE_f − KE_i = ½(m₁ + m₂)vf² − [½m₁v₁ᵢ² + ½m₂v₂ᵢ²]
```

ΔKE is always **negative** (energy is lost, not gained).

## Solving Pattern

1. Draw before-and-after diagram with signed velocities.
2. Write m₁v₁ᵢ + m₂v₂ᵢ = (m₁ + m₂)vf.
3. Substitute and solve for vf.
4. If asked for energy lost: compute ΔKE.
5. Check: vf should be between v₁ᵢ and v₂ᵢ in magnitude (a perfectly inelastic final speed is always less than or equal to the maximum initial speed).

## Unit Check

```
(kg)(m/s) / (kg) = m/s ✓
```

## Traps

- **Forgetting direction:** If v₂ᵢ is in the opposite direction, it must have a negative sign. A common error is adding both speeds: m₁v₁ + m₂v₂ ≠ (m₁+m₂)vf if the signs are dropped.
- **Calling this "elastic":** If objects stick together, the collision is perfectly inelastic — do not use both momentum and KE conservation together.
- **Energy check confusion:** The final KE is always less than the initial KE in a perfectly inelastic collision. If you compute ΔKE and get a positive number (energy gain), you have a sign error.

## Drill

[[../drills/collision-drill]] — Part A
