---
type: calculus-link
timeline: reference
status: draft
---

# Calculus Link — Torque as the Derivative of Angular Momentum (Stage 11)

## Physics Idea

Newton's Second Law in rotational form isn't just τ = Iα. At a deeper level, torque is the rate of change of angular momentum — the rotational analogue of F = dp/dt (force is the rate of change of linear momentum).

## Calculus Idea

A **derivative** gives the instantaneous rate of change. The relationship τ = dL/dt says torque is how quickly angular momentum is changing.

## Plain-English Connection

| Linear form | Rotational analogue | What it means |
|---|---|---|
| F = dp/dt | τ = dL/dt | Net force/torque = rate of change of momentum |
| If ΣF = 0 then Δp = 0 (momentum conserved) | If Στ = 0 then ΔL = 0 (angular momentum conserved) | Conservation law follows directly from the derivative form |

The conservation law is not a separate rule — it's the consequence of setting the derivative to zero: if dL/dt = 0, then L is constant.

## Symbol Meanings

| Symbol | Meaning |
|---|---|
| L | angular momentum (kg·m²/s) |
| τ | net torque (N·m) |
| dL/dt | rate of change of angular momentum |
| L = Iω | angular momentum for rigid body rotating about fixed axis |

## Small Example

A spinning skater extends her arms (increasing I) while no external torque acts (τ = 0):

dL/dt = 0 → L = constant → I₁ω₁ = I₂ω₂

The calculus basis: since τ = dL/dt = 0, L doesn't change. The algebra L = Iω then gives the conservation equation directly.

## Course Location

Stage 11 (Ch 11 — Angular Momentum). This is the first time the full derivative form of Newton's Law (rather than just τ = Iα) becomes essential.

## Common Mistake

Using τ = Iα when the moment of inertia I is itself changing (like the spinning skater changing arm position). When I is not constant: τ = dL/dt = d(Iω)/dt = I(dω/dt) + ω(dI/dt) ≠ Iα. For conservation-of-angular-momentum problems, always use L = Iω = constant (not τ = Iα).

## Related Pages

[[../stages/stage-11-angular-momentum]] — [[../calculus-links/impulse-integral]] — [[../appendix/math-calculus]]
