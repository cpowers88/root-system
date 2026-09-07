---
type: calculus-link
timeline: reference
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

## Practice Problems

**Problem 1 — integrate a given force-time function.**
During an impact, the force on a part is modeled as F(t) = 5000t − 2500t²
(N) for 0 ≤ t ≤ 2.0 ms (t in seconds). Find the impulse by integrating over
the full contact time.

**Problem 2 — same Δp, different Δt (the crumple-zone idea).**
A 70 kg crash-test dummy decelerates from 15 m/s to 0 m/s. Case A: contact
time 0.080 s (rigid structure). Case B: contact time 0.400 s (crumple zone
absorbs the impact). Find the impulse in each case, then find the average
force in each case. What does comparing the two forces tell you about why
crumple zones reduce injury?

**Problem 3 — read impulse off a graph.**
A force-time graph for a bat-ball contact is roughly triangular: it rises
linearly from 0 to a peak of 8000 N at t = 1.0 ms, then falls linearly back
to 0 N at t = 3.0 ms. Find the impulse using the area of the triangle, then
find the resulting change in velocity of a 0.145 kg ball.

### Check Yourself

1. J = ∫₀^0.002 (5000t − 2500t²) dt = [2500t² − (2500/3)t³]₀^0.002
   = 2500(0.002)² − 833.3(0.002)³ ≈ 0.0100 − 0.0000067 ≈ 0.0100 N·s.
2. Δp = mΔv = 70(15 − 0) = 1050 kg·m/s in both cases — impulse (and momentum
   change) does not depend on contact time. Case A: F_avg = 1050/0.080 =
   13,125 N. Case B: F_avg = 1050/0.400 = 2,625 N. Same impulse, but Case B's
   average force is 5× smaller — this is exactly why crumple zones and
   airbags work: extending Δt for the same Δp reduces the peak/average force
   the body experiences.
3. J = ½(base)(height) = ½(0.003 − 0)(8000) = 12.0 N·s. Δv = J/m =
   12.0/0.145 ≈ 82.8 m/s.

## Engineering Use Case

The impulse-momentum theorem is the working principle behind essentially all
crash and impact safety engineering: crumple zones, airbags, packaging
cushioning, and sports protective equipment all exist to increase the
contact time Δt for a fixed, unavoidable Δp — which directly and
proportionally lowers the average force a person or product experiences
(F_avg = Δp/Δt). This is not an approximation of the physics; it is the
physics. A packaging engineer designing drop-test protection or a safety
engineer specifying a machine guard's energy-absorbing material is solving
"what Δt do I need to keep peak force under the injury/damage threshold for
this known Δp?" — the same calculation as Problem 2 above, run in reverse to
solve for a design requirement instead of a result.

## Related Pages

[[../stages/stage-9-linear-momentum]] — [[../calculus-links/kinematics-derivatives]] — [[../calculus-links/stage-7-work-integral]] — [[../appendix/math-calculus]]
