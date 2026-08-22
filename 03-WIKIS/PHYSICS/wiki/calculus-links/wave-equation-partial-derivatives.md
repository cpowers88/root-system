---
type: calculus-link
timeline: reference
status: draft
---

# Calculus Link — The Wave Equation and Partial Derivatives (Stage 16)

## Physics Idea

Everything before this stage had one independent variable: time. A wave has
**two**. The displacement of a point on a string, `y`, depends on where you are
along the string (`x`) *and* what time it is (`t`). You need a way to ask "how is
`y` changing?" that specifies which variable you mean.

## Calculus Idea

**Partial derivatives.** `∂y/∂t` means differentiate with respect to `t` while
holding `x` fixed. `∂y/∂x` means the reverse. That is the entire new idea — a
partial derivative is an ordinary derivative with the other variable frozen.

The wave equation itself is:

```text
∂²y/∂x² = (1/v²) ∂²y/∂t²
```

You are never asked to *solve* this in PHYS 2211. You are asked to read it and to
**verify** that a sinusoidal wave satisfies it.

## Plain-English Connection

| Physics statement | Calculus statement | What it means |
|---|---|---|
| Freeze time, photograph the string | `∂y/∂x` | Slope of the string's shape at one instant |
| Watch one point, ignore the rest | `∂y/∂t` | Transverse velocity of that single piece of string |
| Curvature of the string shape | `∂²y/∂x²` | How sharply the string is bent there |
| Transverse acceleration of a point | `∂²y/∂t²` | What the tension has to produce |
| The wave equation | `∂²y/∂x² = (1/v²)∂²y/∂t²` | Curvature drives acceleration — bend the string, it snaps back |

The physics in one sentence: **a bent piece of string accelerates, and the
constant relating bend to acceleration is `1/v²`.**

## Verifying the Sinusoidal Solution

This is the actual exercise, and the chain rule does all of it. Take
`y(x,t) = A sin(kx − ωt)`.

Differentiate twice in `x`, holding `t` fixed:

```text
∂y/∂x   = Ak cos(kx − ωt)
∂²y/∂x² = −Ak² sin(kx − ωt) = −k² y
```

Differentiate twice in `t`, holding `x` fixed:

```text
∂y/∂t   = −Aω cos(kx − ωt)
∂²y/∂t² = −Aω² sin(kx − ωt) = −ω² y
```

Substitute into the wave equation:

```text
−k² y = (1/v²)(−ω² y)
   k² = ω²/v²
    v = ω/k
```

The sinusoid satisfies the equation **only if** `v = ω/k`. And since `ω = 2πf`
and `k = 2π/λ`:

```text
v = 2πf / (2π/λ) = fλ
```

`v = fλ` is not a separate formula to memorize. It is the condition under which a
sine wave is allowed to exist.

## Symbol Meanings

| Symbol | Meaning | Unit |
|---|---|---|
| `y(x,t)` | transverse displacement — how far that point moved sideways | m |
| `∂` | partial derivative — other variable held fixed | — |
| `k` | wave number, `2π/λ` — radians of phase per meter | rad/m |
| `ω` | angular frequency, `2πf` — radians of phase per second | rad/s |
| `v = ω/k` | **wave speed** — how fast the pattern travels along `x` | m/s |
| `∂y/∂t` | **transverse speed** — how fast one point moves sideways | m/s |

## Small Example

A wave on a string: `y(x,t) = 0.050 sin(3.0x − 12t)` (SI units).

- `k = 3.0` rad/m → `λ = 2π/k = 2.09` m
- `ω = 12` rad/s → `f = ω/2π = 1.91` Hz
- `v = ω/k = 12/3.0 = 4.0` m/s
- Check: `fλ = 1.91(2.09) = 4.0` m/s ✓
- Maximum transverse speed: `|∂y/∂t|max = Aω = 0.050(12) = 0.60` m/s

The pattern travels at 4.0 m/s. No piece of string ever exceeds 0.60 m/s. Those
are different numbers describing different things.

## Course Location

Stage 16 (Ch 16). **This page was listed as `missing` in `calculus-map.md`'s
just-in-time readiness gate** — it is on the active Fall path (Ch 15–17) and now
exists. It builds directly on [[shm-differential-equation]]: SHM is what a single
point on the string does, and a wave is what you get when neighboring points do it
slightly out of phase.

## Common Mistake

**Confusing wave speed with transverse speed.** This is the defining Chapter 16
error. The wave moves along `x` at `v = ω/k`. A point on the string only moves
up and down, at `∂y/∂t`, and never travels along `x` at all. A question asking
"how fast is the wave moving" and one asking "how fast is that point moving" have
different answers and different formulas.

**Treating `∂` as harder mathematics.** It is not. `∂/∂t` on `sin(kx − ωt)` is the
same chain rule you already use, with `kx` behaving as a constant because `x` is
held fixed. If you can differentiate `sin(5 − ωt)`, you can do this.

**Losing the minus sign in `(kx − ωt)`.** The chain rule pulls out `−ω` each
time. Two derivatives give `(−ω)² = +ω²`, which is why `∂²y/∂t²` comes back
positive-signed as `−ω²y` and not `+ω²y`. Sign slips here break the verification.

## Practice Problems

**Problem 1 — read the wave.**
For `y(x,t) = 0.020 sin(8.0x − 40t)` (SI), find `k`, `λ`, `ω`, `f`, `v`, and the
direction of travel. State how you know the direction from the sign alone.

**Problem 2 — verify the solution.**
Show by direct partial differentiation that the wave in Problem 1 satisfies
`∂²y/∂x² = (1/v²)∂²y/∂t²`, and confirm the `v` you get matches `ω/k`.

**Problem 3 — the two speeds.**
For the same wave, find the maximum transverse speed of a point on the string and
compare it to the wave speed. Then find the transverse speed at `x = 0`,
`t = 0`, and explain physically why it is at its maximum there while the
displacement is zero.

### Check Yourself

1. `k = 8.0` rad/m, `λ = 2π/8.0 = 0.785` m; `ω = 40` rad/s, `f = 6.37` Hz;
   `v = 40/8.0 = 5.0` m/s. The `(kx − ωt)` form travels in **+x**: to hold the
   phase constant as `t` grows, `x` must grow.
2. `∂²y/∂x² = −64y`; `∂²y/∂t² = −1600y`. Then `−64y = (1/v²)(−1600y)` gives
   `v² = 25`, `v = 5.0` m/s ✓.
3. `|∂y/∂t|max = Aω = 0.020(40) = 0.80` m/s, versus a wave speed of 5.0 m/s —
   the pattern outruns the string by more than 6×. At `x = 0, t = 0`:
   `∂y/∂t = −Aω cos(0) = −0.80` m/s, the maximum magnitude. Displacement is zero
   at the equilibrium crossing, which is exactly where a point moves fastest —
   the same trade you already know from SHM.

## Real-World Use Case

This equation is the reason a bridge deck, a turbine blade, a guitar string, and
a data cable are all analyzed with the same mathematics. In structural and
mechanical work, the practical question is where the standing-wave nodes and
antinodes land — because an antinode is where fatigue cracks start, and a
resonance driven near a natural frequency is how a component fails without ever
being overloaded. In signal work, the same `v = ω/k` relation is what makes cable
length matter: a reflection off an impedance mismatch returns as a standing wave
and corrupts the signal. Vibration analysts read `∂²y/∂t²` off an accelerometer
and work backwards to find which mode is being excited.

## Related Pages

[[shm-differential-equation]] — [[../stages/stage-16-wave-motion]] —
[[../stages/stage-15-oscillatory-motion]] — [[../concepts/wave-model]] —
[[../equations/standing-wave-equations]]

---

*Draft. Derivations are standard; section/page citations against Serway & Jewett
10e have not been added yet. Verify chapter placement when Stage 16 activates.*
