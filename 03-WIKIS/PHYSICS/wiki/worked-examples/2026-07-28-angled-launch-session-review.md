---
type: worked-example
timeline: reference
status: draft
tags: [physics, trig, calculus, review]
---

# Angled Launch — Trig + Calculus + Formula Review (2026-07-28 session)

Personal review note tying together the three pieces Chris actually used solving
[[../drills/projectile-motion-drill]] Problems 3–4, anchored to the two real
mistakes made that session so they're easier to recall than a bare formula list.
Canonical detail lives in the three linked pages below — this page is the
synthesis, not a replacement.

## 1. Trig — decomposing the launch velocity

Full reference: [[../appendix/math-geometry-trig]] § B.4.

A launch at speed v₀ and angle θ₀ above horizontal is a right triangle: v₀ is
the hypotenuse, the horizontal and vertical velocities are the legs.

```
v₀ₓ = v₀ cos θ₀     (adjacent — SOH-CAH-TOA: CAH)
v₀ᵧ = v₀ sin θ₀     (opposite — SOH)
```

Physical anchor: cos always goes with the axis the angle is measured **from**
(horizontal, here); sin goes with the other one. Draw the little right
triangle under the angle every single time — don't do this from memory alone.

## 2. Calculus — where the equations come from

Full reference: [[../equations/projectile-motion-equations]] § Calculus Origin.

Acceleration is constant and known (aₓ = 0, aᵧ = −g). Integrate twice:

```
vᵧ(t) = ∫ aᵧ dt = −gt + v₀ᵧ
y(t)  = ∫ vᵧ dt = −½gt² + v₀ᵧt + y₀
```

Same pattern for x, but aₓ = 0 so integrating just gives constants:

```
vₓ(t) = v₀ₓ                (constant — no horizontal force)
x(t)  = v₀ₓt + x₀
```

Every formula below is just this integration evaluated at a specific
condition (vᵧ = 0, or y = some target height).

## 3. The formulas — and which condition each one comes from

| Formula | Comes from setting... | Use for |
|---|---|---|
| `t_peak = v₀ᵧ/g` | vᵧ(t) = 0 | time to reach the top only |
| `h_max = v₀ᵧ²/(2g)` | y(t_peak) | max height |
| `t_flight = 2v₀ᵧ/g` | y(t) = 0, launch = landing height | **total** round-trip time — symmetric case only |
| `R = v₀² sin(2θ₀)/g` | x(t_flight) | range — symmetric case only |
| `4.90t² − v₀ᵧt + (y_target − y₀) = 0` | y(t) = y_target directly, any height | general case — always works, gives up to two roots |

## 4. The two real mistakes from today — the part worth memorizing

**Mistake 1 — t_peak vs. t_flight.** First pass at Problem 3, computed time
of flight as `v₀ᵧ/g` (got 1.77 s) instead of `2v₀ᵧ/g` (correct: 2.04 s).
`v₀ᵧ/g` only gets you to the **peak** — half the trip. For a symmetric
launch/landing, the trip down mirrors the trip up, so total time is always
double the time to the peak. Height and range came out right because those
formulas don't depend on this mistake; time of flight is the one formula
where forgetting the factor of 2 shows up directly.

**Mistake 2 — using v₀ instead of v₀ᵧ.** Also plugged the raw launch speed
(15.0 m/s) into a time formula instead of its vertical component (13.0 m/s)
first. Always decompose *before* touching any of the y-equations — v₀ never
appears alone in a y(t) or vᵧ(t) expression, only v₀ᵧ does.

**What worked — the sanity check.** On Problem 4's quadratic, a bad
calculator entry gave t = 3.31 s for the "way down" root. Checking that
against `t_flight = 2v₀ᵧ/g ≈ 2.65 s` (the ball can't still be in the air at
3.31 s if it lands by 2.65 s) caught the error before it became a final
answer. This is a fast, free check any time a quadratic root comes out of a
projectile problem: compare it to the symmetric-case total flight time as an
upper bound.

## 5. Explain-back prompt

Close this page and answer: why does `t_peak` use `v₀ᵧ` alone but `R` uses
`v₀²`? Why does the quadratic in §3 always have `4.90` as the leading
coefficient? If launch and landing height are different, which formulas in
the table still work and which don't?

## Sources

- [[../equations/projectile-motion-equations]]
- [[../problem-types/projectile-angled-launch]]
- [[../appendix/math-geometry-trig]]
- [[../drills/projectile-motion-drill]] — today's Problems 3–4
