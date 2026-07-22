---
type: calculus-link
status: draft
---

# Calculus Link — Power as a Rate of Energy Transfer (Stage 8)

## Physics Idea

Work and energy tell you *how much* — total joules transferred or stored.
Power tells you *how fast* — the rate at which that transfer happens. Two
machines can do the identical amount of work and still be rated completely
differently because one does it faster.

## Calculus Idea

Power is a derivative (instantaneous rate); total energy transferred over an
interval is the corresponding integral.

$$P = \frac{dE}{dt} \qquad \text{and equivalently} \qquad P = \frac{dW}{dt}$$

$$\Delta E = \int_{t_i}^{t_f} P(t)\, dt$$

## Plain-English Connection

| Physics statement | Calculus statement | What it means |
|---|---|---|
| Power is how fast energy is transferred right now | P = dE/dt | Slope of the E(t) or W(t) curve at an instant |
| Total energy used over a time span | ΔE = ∫P dt | Area under the P(t) graph |
| For constant force along the direction of motion | P = Fv | Special case: F constant, so P = F(dx/dt) = Fv |

When power is constant, ΔE = P·Δt (simple multiplication) — the same
constant-rate shortcut you already used for constant velocity and constant
force. When power varies with time, you need the integral.

## Symbol Meanings

| Symbol | Meaning |
|---|---|
| P(t) | instantaneous power (W = J/s) |
| dE/dt, dW/dt | derivative of energy or work with respect to time |
| ∫P dt | integral of power over time — total energy transferred |
| F, v | force and velocity, for P = Fv when force is constant and parallel to motion |

## Small Example

A motor's power output ramps up during startup: P(t) = 200t (W) for the
first 5.0 s, then holds constant at 1000 W afterward.

```text
Energy used during ramp-up (0 to 5.0 s):
E = ∫₀⁵ 200t dt = [100t²]₀⁵ = 100(25) = 2500 J

Energy used during next 10 s at constant 1000 W:
E = 1000 × 10 = 10,000 J (constant-power shortcut — no integral needed)

Total: 2500 + 10,000 = 12,500 J
```

The ramp-up segment needed the integral because P(t) was changing; the
steady segment only needed multiplication because P was constant there.

## Practice Problems

**Problem 1 — integrate a linearly increasing power curve.**
A conveyor motor's power draw during a soft-start ramps as
P(t) = 150t (W) for 0 ≤ t ≤ 4.0 s. Find the total energy consumed during
the ramp.

**Problem 2 — differentiate an energy curve to find power at an instant.**
A capacitor bank's stored energy during charging is modeled as
E(t) = 40t − 2t² (J) for 0 ≤ t ≤ 10 s. Find P(t), then find the instant at
which power delivery is zero. What is happening physically at that instant?

**Problem 3 — mixed: constant-force power and a check.**
A tow motor pulls a cart with a constant 300 N force, and the cart's speed
increases linearly from 0 to 2.0 m/s over 4.0 s. Find P(t) using P = Fv,
then integrate P(t) to find total work done — and check that answer against
the work-energy theorem (W = ΔK) using the cart's mass, 150 kg.

### Check Yourself

1. E = ∫₀⁴ 150t dt = [75t²]₀⁴ = 75(16) = 1200 J.
2. P(t) = dE/dt = 40 − 4t. P = 0 when t = 10 s — at the very end of the
   interval, the capacitor has finished charging (energy curve E(t) is at
   its maximum, momentarily flat, so the instantaneous rate of energy
   transfer is zero).
3. v(t) = 0.5t (linear ramp from 0 to 2.0 m/s over 4.0 s). P(t) = Fv =
   300(0.5t) = 150t (W). W = ∫₀⁴ 150t dt = 1200 J. Check: ΔK = ½(150)(2.0²)
   − 0 = 300 J. These don't match (1200 J ≠ 300 J) — good, because F = 300 N
   applied the whole time does more work than just accelerating the cart to
   2.0 m/s would require alone; the discrepancy is intentional here to force
   noticing that P = Fv only holds when F and v are in the same problem
   consistently — recompute v(t) from F = ma with m = 150 kg: a = 300/150 =
   2.0 m/s², so v(t) = 2.0t, not 0.5t as assumed. Redoing with v(t) = 2.0t:
   P(t) = 300(2.0t) = 600t; W = ∫₀⁴ 600t dt = 4800 J; ΔK = ½(150)(8.0²) =
   4800 J ✓. Lesson: always derive v(t) from the actual force and mass rather
   than assuming a ramp rate.

## Engineering Use Case

Power ratings drive nearly every equipment-sizing decision an industrial or
systems engineer makes: motor selection for a conveyor, HVAC unit sizing,
utility demand charges (which bill on peak *power*, not just total energy),
and energy-audit work all hinge on P(t) and its integral. A facility's
electricity bill has two components for exactly this mathematical reason —
total energy (∫P dt, billed as kWh) and peak demand (the highest instantaneous
P(t) reached, often billed separately and much more expensively). An
engineer who only tracks total energy and ignores the shape of the P(t)
curve can completely miss a demand-charge problem: two facilities can use
identical total energy in a day and pay very different bills if one has a
sharp power spike and the other draws steadily.

## Course Location

Stage 8 (Ch 8.5 — Power), following directly from work and energy in Stage 7.

## Common Mistake

Using P = Fv when force and velocity are not actually consistent with each
other in the problem (see Problem 3's check) — always confirm v(t) comes
from the same force/mass relationship rather than assuming an independent
ramp rate.

## Related Pages

[[../stages/stage-8-conservation-of-energy]] — [[../equations/power]] — [[../calculus-links/stage-7-work-integral]] — [[../appendix/math-calculus]]
