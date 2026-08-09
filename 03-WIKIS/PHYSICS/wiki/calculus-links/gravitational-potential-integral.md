---
type: calculus-link
timeline: reference
status: draft
---

# Calculus Link — Gravitational Potential Energy as an Integral (Stage 13)

## Physics Idea

Near the ground, gravitational potential energy is `U = mgh`. That formula works
only because gravity is essentially constant over a few meters. Once you move far
enough that gravity actually weakens, `mgh` breaks — and the real expression
`U = −GMm/r` has to be built by integrating the force over distance.

## Calculus Idea

**Integrating a variable force to get potential energy**, and the inverse
relationship `F = −dU/dr`. This is the Stage 7 work integral (`W = ∫F dx`) applied
to a force that follows an inverse-square law instead of being constant.

## Plain-English Connection

| Physics statement | Calculus statement | What it means |
|---|---|---|
| Potential energy is minus the work gravity does bringing you in from far away | `U(r) = −∫_∞^r F_r dr` | Accumulate the force over the whole trip |
| Gravity weakens as the square of distance | `F_r = −GMm/r²` | Negative because it pulls inward |
| The result | `U(r) = −GMm/r` | Zero at infinity, more negative closer in |
| Force is the downhill slope of the energy curve | `F_r = −dU/dr` | Differentiating undoes the integration |

## The Derivation

Set `U = 0` at `r = ∞` — this is a **choice**, not a fact, and it is what makes
every bound orbit have negative energy.

```text
U(r) = −∫_∞^r F_r dr
     = −∫_∞^r (−GMm/r²) dr
     =  GMm ∫_∞^r r⁻² dr
     =  GMm [−1/r]_∞^r
     =  GMm (−1/r − 0)
     = −GMm/r
```

The only calculus used is the power rule on `r⁻²`. Check it backwards:

```text
F_r = −dU/dr = −d/dr(−GMm/r) = −(GMm/r²)
```

Negative, so inward. ✓

### Why `mgh` is the near-surface special case

At height `h` above a planet of radius `R`, with `h ≪ R`:

```text
U = −GMm/(R+h) = −(GMm/R)(1 + h/R)⁻¹ ≈ −(GMm/R)(1 − h/R)
  = −GMm/R + GMmh/R²
```

The first term is a constant, so it drops out of any `ΔU`. In the second,
`GM/R² = g`, leaving **`ΔU ≈ mgh`**. That is where `mgh` comes from — a
first-order binomial approximation, `(1+x)⁻¹ ≈ 1 − x`, valid only when `h/R` is
tiny.

## Symbol Meanings

| Symbol | Meaning |
|---|---|
| `G` | universal gravitational constant, 6.674×10⁻¹¹ N·m²/kg² |
| `M`, `m` | the two masses; `M` is usually the planet |
| `r` | **center-to-center** distance — not altitude |
| `U(r)` | gravitational potential energy, negative for any bound pair |
| `R` | planet radius, used when converting to the `mgh` form |

## Small Example

Escape speed from Earth's surface. Escaping means arriving at `r = ∞` with zero
speed, so total energy is exactly zero:

```text
½mv² + (−GMm/R) = 0
v = √(2GM/R)
```

With `M = 5.97×10²⁴ kg` and `R = 6.37×10⁶ m`: `v ≈ 1.12×10⁴ m/s`, about
11.2 km/s. Notice the escaping mass `m` cancels — a marble and a spacecraft need
the same speed.

## Course Location

Stage 13 (Ch 13). **The `calculus-map.md` roadmap previously marked Stage 13 as
"none new."** That holds only if `U = −GMm/r` is handed to you as a formula. It
is not new *technique* — the power rule and the work integral both come from
Stage 7 — but it is the first place where the Stage 7 machinery is aimed at a
force that actually varies, and skipping the derivation is what makes orbital
energy problems feel arbitrary later.

## Common Mistake

**Using `mgh` for anything orbital.** A satellite at 400 km is at `r = 6770 km`
versus `R = 6370 km` — `h/R ≈ 0.06`, and the approximation that produced `mgh`
has already started to fail. Any problem naming an orbit, an escape, or a
planetary distance needs `−GMm/r`.

**Measuring `r` from the surface.** `r` is center-to-center. "Altitude 400 km"
means `r = R + 400 km`, and forgetting to add `R` produces answers off by orders
of magnitude.

**Reading the negative sign as an error.** `U < 0` means *bound*. A pair with
`U + K < 0` cannot escape; `U + K ≥ 0` can. The sign is the physics.

## Practice Problems

**Problem 1 — do the integral yourself.**
Starting from `F_r = −GMm/r²`, derive `U(r) = −GMm/r` without looking at the
derivation above. State explicitly where you chose `U = 0`.

**Problem 2 — differentiate back.**
Given `U(r) = −GMm/r`, compute `−dU/dr` and confirm you recover Newton's law of
gravitation. Say in one sentence what the minus sign in `F = −dU/dr` is doing.

**Problem 3 — where `mgh` fails.**
Compute `ΔU` for lifting a 1200 kg satellite from Earth's surface to a 400 km
orbit, first with `mgh` and then with `−GMm/r`. Report the percent error. Then
repeat for a 10 m lift and explain the difference.

### Check Yourself

1. `U(r) = −∫_∞^r (−GMm/r')dr'/r'² = GMm[−1/r']_∞^r = −GMm/r`, with `U(∞) = 0`
   as the chosen reference.
2. `−d/dr(−GMm/r) = −GMm/r²`, which is Newton's law of gravitation. The minus
   sign says force points **down** the potential-energy slope — toward lower `U`,
   which for gravity is inward.
3. `mgh`: `1200(9.8)(4.0×10⁵) ≈ 4.70×10⁹` J. Exact:
   `GMm(1/R − 1/r) = 1200(3.986×10¹⁴)(1/6.37×10⁶ − 1/6.77×10⁶) ≈ 4.44×10⁹` J.
   About 6% high. For a 10 m lift the two agree to roughly one part in a million,
   because `h/R ≈ 1.6×10⁻⁶`.

## Real-World Use Case

Every launch and every orbital transfer is budgeted in this equation. Mission
planners work in **delta-v**, and a delta-v budget is `U(r)` bookkeeping: how much
energy to climb out of a gravity well, how much to circularize, how much held in
reserve. The reason geostationary satellites cost more to place than low-orbit
ones is entirely the `1/r` term. The same math sets the fuel margin on a Hohmann
transfer and explains why a launch site nearer the equator is worth real money —
Earth's rotation contributes free kinetic energy against a fixed potential-energy
climb.

## Related Pages

[[stage-7-work-integral]] — [[../stages/stage-13-universal-gravitation]] —
[[../equations/gravitational-pe-general]] — [[../equations/orbital-mechanics]] —
[[../concepts/potential-energy]]

---

*Draft. Derivations are standard; section/page citations against Serway & Jewett
10e have not been added yet. Verify chapter placement when Stage 13 activates —
note the syllabus opens Stage 13's force foundation before Stage 6.*
