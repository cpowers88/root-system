---
type: calculus-link
timeline: reference
status: draft
---

# Calculus Link — Newton's Second Law as a Rate Equation (Stage 5)

## Physics Idea

A net force does not "cause motion." It causes **momentum to change**. The real
statement of Newton's second law is a rate equation: net force is the rate at
which momentum changes with time. `ΣF = ma` is the special case that appears when
mass is constant.

## Calculus Idea

The **derivative of a product**. Momentum is `p = mv`, a product of two things
that could both change with time. Differentiating it:

```text
dp/dt = m(dv/dt) + v(dm/dt)
```

If mass is constant, `dm/dt = 0`, the second term vanishes, and what is left is
`m(dv/dt) = ma`.

## Plain-English Connection

| Physics statement | Calculus statement | What it means |
|---|---|---|
| Net force changes momentum | `ΣF = dp/dt` | The general law. Always true. |
| For constant mass, force = mass × acceleration | `ΣF = m dv/dt = ma` | The special case you use all semester |
| Force applied over time changes momentum | `Δp = ∫ΣF dt` | Integrate the law and you get impulse — Stage 9 |
| Zero net force means momentum is constant | `dp/dt = 0 → p = constant` | Newton's first law is a corollary, not a separate rule |

Notice what this buys you: **Newton's first law, `F = ma`, and the
impulse-momentum theorem are all the same equation** read three ways —
undifferentiated, differentiated with constant mass, and integrated. That is one
idea to hold instead of three.

## Symbol Meanings

| Symbol | Meaning |
|---|---|
| `p = mv` | linear momentum — mass times velocity, a vector |
| `dp/dt` | rate of change of momentum with time |
| `ΣF` | **net** force — the vector sum of all forces, summed before differentiating |
| `dm/dt` | rate of mass change — zero for every standard Stage 5 problem |

## Small Example

A 2.0 kg cart moves with `v(t) = 3t²` m/s.

- Momentum: `p(t) = mv = 2.0(3t²) = 6t²` kg·m/s
- Net force: `ΣF = dp/dt = 12t` N
- At `t = 2.0 s`: `ΣF = 24 N`

Cross-check with `F = ma`: `a = dv/dt = 6t`, so `F = ma = 2.0(6t) = 12t` N. ✓

Same answer, because mass was constant. The point of the exercise is that the
first route works whether or not it is.

## Course Location

Stage 5 (Ch 5). **The `calculus-map.md` roadmap previously marked Stage 5 as
"none new."** That is true only if you accept `F = ma` as a definition rather
than a consequence. It is not — and the Week B breadth block "Newton's second law
as a differential relationship" is exactly this page. Reading `ΣF = dp/dt` first
makes Stage 9 (impulse) a restatement rather than a new topic.

## Common Mistake

**Differentiating one force instead of the net force.** `ΣF` is the vector sum of
every force acting — normal, weight, tension, friction — and the sum comes first.
Students who write `dp/dt` for gravity alone and then "add friction later" get
signs wrong on inclines every time.

Second mistake: **using `F = ma` when mass genuinely changes.** A cart filling
with rain, a rocket burning fuel, a conveyor being loaded — those need
`dp/dt = m dv/dt + v dm/dt`. PHYS 2211 rarely assigns them, but recognizing *why*
`F = ma` fails there is the point of knowing the general form.

## Practice Problems

**Problem 1 — differentiate to find the force.**
A 0.50 kg puck has `v(t) = 4t − t²` m/s along a straight line. Find `p(t)` and
`ΣF(t)`. At what time is the net force zero, and what is the puck doing at that
instant?

**Problem 2 — integrate to find the momentum change.**
A 3.0 kg block is struck by a force `F(t) = 60t` N for 0.40 s, starting from
rest. Use `Δp = ∫F dt` to find its final speed. Do **not** use `F = ma` with an
average force — integrate.

**Problem 3 — the two-term case, conceptually.**
An open railcar of mass 500 kg rolls at 4.0 m/s through vertical rain, collecting
water at 2.0 kg/s. No horizontal force acts on it. Using `ΣF = dp/dt = 0`, argue
what must happen to its speed, and explain in one sentence why `F = ma` cannot
answer this.

### Check Yourself

1. `p(t) = 0.50(4t − t²) = 2t − 0.5t²`; `ΣF = dp/dt = 2 − t` N. Zero at
   `t = 2.0 s`, which is when velocity `4t − t² = 4(2) − 4 = 4` m/s is at its
   **maximum** — the puck is moving fastest, not stopped. Zero force means
   momentum is momentarily unchanging, not zero.
2. `Δp = ∫₀^0.4 60t dt = [30t²]₀^0.4 = 30(0.16) = 4.8` kg·m/s. From rest,
   `v = Δp/m = 4.8/3.0 = 1.6` m/s.
3. Horizontal momentum is conserved: `p = mv = constant`. Mass increases, so
   speed must decrease — `v = p₀/m(t)`. `F = ma` cannot answer it because it
   assumes `dm/dt = 0`, which is precisely the term doing all the work here.

## Real-World Use Case

Every crash-test result, airbag calibration, and packaging drop-test spec is a
`dp/dt` argument. The momentum change in a collision is fixed by the mass and
speed — you cannot negotiate it. The only free variable is the **time** over
which it happens, and force is what falls out. Crumple zones, helmet foam,
pallet cushioning, and the give in a climbing rope all do the same job: stretch
`dt` so `dp/dt` lands below what a body or a component can survive. An engineer
sizing a shock mount is choosing a deceleration time, not a force.

## Related Pages

[[../stages/stage-5-laws-of-motion]] — [[impulse-integral]] —
[[../equations/newtons-second-law]] — [[../concepts/newtons-second-law]]

---

*Draft. Derivations are standard; section/page citations against Serway & Jewett
10e have not been added yet. Verify chapter placement when Stage 5 activates.*
