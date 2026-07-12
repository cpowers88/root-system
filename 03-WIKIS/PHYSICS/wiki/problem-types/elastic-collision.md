---
type: problem-type
stage: 9
chapter: 9
---

# Problem Type: Elastic Collision

## How to Recognize

Objects collide, separate, and **kinetic energy is conserved** (no permanent deformation or heat).

Keywords: "elastic collision," "bounces off without energy loss," "perfectly elastic," "billiard balls," "kinetic energy conserved."

## Given Information

- Masses m₁, m₂
- Initial velocities v₁ᵢ and v₂ᵢ (often v₂ᵢ = 0)

## Unknown Requested

- Both final velocities v₁f and v₂f (two unknowns — need two equations)

## Diagram to Draw

```
Before:  [m₁ → v₁ᵢ]  [m₂ v₂ᵢ]
After:   [m₁ → v₁f]  [m₂ → v₂f]
```

Note: v₁f may be negative (m₁ reverses direction) if m₁ < m₂.

## Equations

Two conservation laws apply:

```
(1) Momentum:       m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f

(2) Kinetic energy: ½m₁v₁ᵢ² + ½m₂v₂ᵢ² = ½m₁v₁f² + ½m₂v₂f²
```

## Solution Formulas (1D, v₂ᵢ = 0)

These are derived from the two equations above:

```
v₁f = [(m₁ − m₂)/(m₁ + m₂)] v₁ᵢ

v₂f = [2m₁/(m₁ + m₂)] v₁ᵢ
```

## Special Cases to Memorize

| Condition | v₁f | v₂f |
|---|---|---|
| m₁ = m₂ | 0 (stops) | v₁ᵢ (takes on full speed) |
| m₁ >> m₂ | ≈ v₁ᵢ (barely changes) | ≈ 2v₁ᵢ (flung forward) |
| m₁ << m₂ | ≈ −v₁ᵢ (bounces back) | ≈ 0 (barely moves) |

## Solving Pattern

1. Draw before-and-after diagram with signed velocities.
2. Write equation (1) and equation (2).
3. Use the solution formulas directly (1D, target at rest) OR solve the system simultaneously.
4. Check: compute KE_before and KE_after — they should match. If not, recheck signs.

## Unit Check

All velocity terms in m/s; substituting into the formulas produces m/s. ✓

## Traps

- **Using only one equation:** One equation gives one relationship but two unknowns. You need BOTH conservation laws. Students who write only momentum get stuck.
- **Forgetting that v₁f can be negative:** If m₁ < m₂ and m₂ is at rest, m₁ bounces backward. The formula gives a negative value — this is correct, not an error.
- **Assuming all collisions are elastic:** Only if the problem explicitly says "elastic" or "kinetic energy conserved." Real collisions almost always lose energy.
- **Using elastic formulas for inelastic problems:** The solution formulas only work when KE is conserved. Applying them to a "stick together" problem will give wrong answers.

## Drill

[[../drills/collision-drill]] — Parts B and C
