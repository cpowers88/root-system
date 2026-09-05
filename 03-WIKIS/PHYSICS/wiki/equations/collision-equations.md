---
type: equation
timeline: reference
status: draft
---

# Equations: Collision Equations (Ch 9)

## Overview

All collision types share momentum conservation. Elastic collisions also conserve kinetic energy. Inelastic collisions do not.

---

## 1. Conservation of Momentum (all collisions)

```
m₁v⃗₁ᵢ + m₂v⃗₂ᵢ = m₁v⃗₁f + m₂v⃗₂f
```

**Always valid** when ΣF_ext = 0 during the collision.

---

## 2. Perfectly Inelastic Collision (objects stick together)

```
m₁v₁ᵢ + m₂v₂ᵢ = (m₁ + m₂)vf
```

Solving for final velocity:

```
vf = (m₁v₁ᵢ + m₂v₂ᵢ) / (m₁ + m₂)
```

**One equation, one unknown.** Kinetic energy is NOT conserved — some converts to heat/deformation.

---

## 3. Conservation of Kinetic Energy (elastic collisions only)

```
½m₁v₁ᵢ² + ½m₂v₂ᵢ² = ½m₁v₁f² + ½m₂v₂f²
```

Combined with momentum conservation, this gives two equations and two unknowns (v₁f, v₂f).

---

## 4. Elastic Collision Solution Formulas (1D, both moving)

Derived by solving momentum + kinetic energy simultaneously:

```
v₁f = [(m₁ − m₂)/(m₁ + m₂)] v₁ᵢ + [2m₂/(m₁ + m₂)] v₂ᵢ

v₂f = [2m₁/(m₁ + m₂)] v₁ᵢ + [(m₂ − m₁)/(m₁ + m₂)] v₂ᵢ
```

### Special case: m₂ initially at rest (v₂ᵢ = 0)

```
v₁f = [(m₁ − m₂)/(m₁ + m₂)] v₁ᵢ

v₂f = [2m₁/(m₁ + m₂)] v₁ᵢ
```

---

## Special Elastic Cases to Memorize

| Condition | Result |
|---|---|
| m₁ = m₂ (identical masses) | v₁f = 0, v₂f = v₁ᵢ (objects exchange velocities) |
| m₁ >> m₂ (heavy hits light) | v₁f ≈ v₁ᵢ (barely slows), v₂f ≈ 2v₁ᵢ |
| m₁ << m₂ (light hits heavy) | v₁f ≈ −v₁ᵢ (bounces back), v₂f ≈ 0 (target barely moves) |

---

## 5. 2D Collisions (component form)

Apply momentum conservation in each direction independently:

```
x: m₁v₁ᵢ cos θ₁ᵢ + m₂v₂ᵢ cos θ₂ᵢ = m₁v₁f cos θ₁f + m₂v₂f cos θ₂f

y: m₁v₁ᵢ sin θ₁ᵢ + m₂v₂ᵢ sin θ₂ᵢ = m₁v₁f sin θ₁f + m₂v₂f sin θ₂f
```

---

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| m₁, m₂ | masses of objects 1 and 2 | kg |
| v₁ᵢ, v₂ᵢ | initial velocities (signed in 1D) | m/s |
| v₁f, v₂f | final velocities (signed in 1D) | m/s |
| vf | final velocity of combined system (perfectly inelastic) | m/s |
| θ | angle of velocity vector from x-axis | degrees or radians |

---

## When to Use Which Equation

| Problem says... | Use |
|---|---|
| "stick together" or "perfectly inelastic" | Eq. 2 only (momentum, combined mass) |
| "elastic" or "bounces without energy loss" | Eqs. 1 + 3 simultaneously (or Eq. 4 formulas) |
| "coefficient of restitution given" | Partially inelastic — momentum + given energy loss |
| "2D" or "at an angle" | Component form (Eq. 5) |

---

## Common Mistake

For elastic collisions, students sometimes only write the momentum equation and forget kinetic energy — giving them one equation and two unknowns (unsolvable). Always check: do you have enough equations for your number of unknowns?
