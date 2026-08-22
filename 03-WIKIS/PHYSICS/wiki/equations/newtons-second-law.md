---
type: equation
timeline: reference
status: draft
---

# Equation — Newton's Second Law

## Equation

$$\sum \vec{F} = m\vec{a}$$

Component form (the form you'll actually use):

$$\sum F_x = ma_x \qquad \sum F_y = ma_y$$

## Plain-English Meaning

The net force on an object equals its mass times its acceleration. More force → more acceleration. More mass → less acceleration for the same force. The direction of acceleration is always in the direction of the net force.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| ΣF | vector sum of all forces acting on the object (net force) | N (newton = kg·m/s²) |
| m | mass of the object | kg |
| a | acceleration produced | m/s² |

## When to Use

- Any time you know some forces and want to find acceleration, or know acceleration and want to find a force.
- After drawing a free body diagram and identifying every force on the object.
- Used in both directions (x and y) simultaneously when forces act in 2D.

## When NOT to Use

- Do not apply it to the whole system and then mix up individual tensions or contact forces — draw separate FBDs for each object.
- Do not use it with forces acting on other objects; only forces ON the chosen object.
- If forces are not constant (they vary with position or velocity), you need the calculus form: F = m(dv/dt).

## Assumptions

- The mass is constant (doesn't change over time — valid for all Ch 5 problems).
- The reference frame is inertial (not accelerating itself — e.g., not a car going around a curve at high speed, which introduces fictitious forces).

## Calculus Origin

For constant force: ΣF = ma is a direct algebraic statement.
For varying force: F = ma = m(dv/dt) = m(d²x/dt²). The kinematic equations of Stage 2 are the integrals of this for the constant-force case. See [[../calculus-links/work-by-varying-force]] (Stage 7) for the next step.

## Example Problem Type

**Flat surface with friction:** A 5 kg block is pulled right by 30 N with μ_k = 0.25.

Step 1 — FBD: weight (49 N down), normal (49 N up, since no vertical acceleration), friction (0.25 × 49 = 12.25 N, left).

Step 2 — ΣF_x = ma_x: 30 − 12.25 = 5 × a → a = 3.55 m/s² to the right.

## Common Mistake

Writing ΣF = ma with the total external force but then solving for an acceleration that belongs to just one piece of a multi-object system. Always be precise about which object you are applying the equation to, using that object's mass.
