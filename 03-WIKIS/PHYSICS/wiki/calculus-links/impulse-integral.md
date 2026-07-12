---
type: calculus-link
status: draft
---

# Calculus Link — Impulse as a Time Integral of Force (Stage 9)

## Physics Idea

Newton's Second Law says F = m(dv/dt). In a collision, the force between objects varies rapidly with time — it's not constant. The total effect of that varying force over the collision duration is the **impulse**.

## Calculus Idea

An **integral** accumulates a varying quantity over an interval. When force varies with time, the total effect is the area under the F-vs-t graph.

## Plain-English Connection

If force is constant: impulse J = F × Δt (simple multiplication).

If force varies with time: 

$$J = \int_{t_i}^{t_f} F(t)\, dt$$

This integral equals the area under the F-vs-t curve between t_i and t_f. In a collision, F(t) peaks briefly at a very large value then drops back to zero — the area under that spike is the impulse.

The result equals the change in momentum:

$$J = \Delta p = m v_f - m v_i$$

## Symbol Meanings

| Symbol | Meaning |
|---|---|
| J | impulse (N·s = kg·m/s) |
| F(t) | force as a function of time |
| ∫ F dt | area under F-vs-t graph — impulse |
| Δp | change in momentum |

## Small Example

A baseball bat hits a ball over a contact time of 1.5 ms. The average force is 9000 N.

**Constant-force approximation:** J = F_avg × Δt = 9000 × 0.0015 = 13.5 N·s

**Meaning:** If the ball had mass 0.145 kg and was initially moving at −20 m/s (toward batter), its final velocity is:
J = m(v_f − v_i) → 13.5 = 0.145(v_f − (−20)) → v_f = 73 m/s (away from batter)

The integral form handles a varying F(t) exactly; the average-force approximation works when you know F_avg.

## Course Location

Stage 9 (Ch 9 — Linear Momentum and Collisions). The impulse-momentum theorem is derived directly from integrating F = m(dv/dt) over time.

## Common Mistake

Treating the force in a collision as constant and using F × Δt without thinking about what that approximation assumes. In reality, collision forces vary enormously over the contact interval — the impulse integral handles this correctly; the average-force approximation is a useful simplification.

## Related Pages

[[../stages/stage-9-linear-momentum]] — [[../calculus-links/kinematics-derivatives]] — [[../appendix/math-calculus]]
