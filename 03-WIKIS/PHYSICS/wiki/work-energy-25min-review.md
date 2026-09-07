---
type: reference
timeline: reference
tags: [physics, work-energy, calculus, vectors, review]
status: complete
---

# Work & Energy — 25-Minute Compressed Review

Reviewed with Claude, 2026-09-06. Covers the vector math, the calculus, and how the
pieces connect. Read top to bottom; each block is the prerequisite for the next.

> [!NOTE] Evidence status
> This was a successful **reactivation after more than six months**, not a mastery
> test. The two errors below occurred during guided work and remain diagnostic
> observations; no cold or durability gate was run.

**Canonical concept owner:** [[stages/stage-7-energy-of-a-system]]. This page is the
compressed session aid and exact resume point, not a replacement for Stage 7.

**The spine:** dot product -> integral -> W = dKE -> move conservative forces to the
other side of the ledger as U.

---

## Block 1 — The dot product (the gate)

$$\vec{A}\cdot\vec{B} = |A||B|\cos\theta = A_xB_x + A_yB_y + A_zB_z$$

Left form for reasoning, right form for computing from components.

**Meaning:** how much of A points along B, times how long B is. Output is a **scalar** —
a plain number, no direction. That is why energy has no direction.

**Construction analogy.** Dragging a loaded sled with a rope at 30 deg above horizontal,
pulling 100 lb, sled moves horizontally. The vertical component (50 lb) does not move
the sled along its path — it only unweights it. Only the horizontal component,
100 cos30 = 86.6 lb, does work. The dot product throws away the part of the force that
is not in the direction of travel.

**Memorize cold:**

| Angle | cos | Work | Example |
|---|---|---|---|
| 0 deg | +1 | max positive | cable lifting a rising beam |
| 90 deg | 0 | **zero** | normal force on a sliding block; tension on a swinging mass |
| 180 deg | -1 | max negative | gravity on a rising beam; friction |

---

## Block 2 — Why work is an integral

Constant force, straight line:

$$W = \vec{F}\cdot\vec{d} = Fd\cos\theta$$

Force usually is not constant (springs get harder, cable angles change), so you cannot
multiply once.

**Construction analogy.** Estimating concrete for a footing whose depth changes along
its length. You cannot do depth x length. You chop it into 1-ft segments, treat depth as
constant over each foot, multiply, add up the segments, then shrink the segments toward
zero and the error vanishes. That is the integral.

$$W = \int_a^b \vec{F}\cdot d\vec{r}$$

Read left to right: chop the path into tiny steps dr, dot the force with each step to get
a sliver of work, sum the slivers.

In 1-D — what you will actually compute most of the time:

$$W = \int_{x_1}^{x_2} F(x)\,dx$$

which is **the area under the force-vs-POSITION graph.** Not force vs. time. Position.

---

## Block 3 — Work-energy theorem, derived

KE is not a definition handed down. It falls out of Newton's second law plus a chain-rule
trick.

$$W_{net} = \int F\,dx = \int ma\,dx$$

The trick — acceleration is written in time, but we are integrating over position:

$$a = \frac{dv}{dt} = \frac{dv}{dx}\cdot\frac{dx}{dt} = v\frac{dv}{dx}$$

Substitute; the dx cancels and the limits change from positions to velocities:

$$W_{net} = \int m v \frac{dv}{dx} dx = \int_{v_1}^{v_2} mv\,dv = \tfrac{1}{2}mv_2^2 - \tfrac{1}{2}mv_1^2 = \Delta KE$$

**The 1/2 is not arbitrary — it is the power rule.** integral of v dv = v^2/2.

**Why this matters:** energy lets you skip the middle of the motion. You only need the
start state and the end state. No kinematics equations, no tracking acceleration.

---

## Block 4 — Potential energy as bookkeeping

Some forces (gravity, springs) do work that depends **only on start and end points, never
on the route.** Carry a beam up a ramp or straight up a hoist — gravity's work is
identical. Those are **conservative** forces. For them you can pre-compute the work and
store it as a number: potential energy.

$$\Delta U = -\int_{\vec r_1}^{\vec r_2} \vec{F}_{conservative}\cdot d\vec{r}
\qquad U_{grav} = mgh \qquad U_{spring} = \tfrac{1}{2}kx^2$$

The minus sign is the whole trick: instead of leaving gravity's work on the left of the
ledger, flip its sign and move it to the right as stored energy. Then:

$$KE_1 + U_1 = KE_2 + U_2$$

Friction does **not** get this treatment — the longer the path, the more it takes — so it
stays on the left as work.

---

## Worked example carried through all four blocks

**Stretch:** spring force F = -kx, stretched from 0 to d.

$$W_{spring} = \int_0^d (-kx)\,dx = -k\left[\frac{x^2}{2}\right]_0^d = -\tfrac{1}{2}kd^2$$

Negative — the spring pulls back while the hand moves forward. This result is **the
work done by the spring**, not the stored potential energy. The relationship is

$$W_{spring} = -\Delta U_{spring} = -\tfrac{1}{2}kd^2$$

The hand's quasi-static external work is positive, $+\tfrac{1}{2}kd^2$, and that is
the energy stored in the spring: $\Delta U_{spring}=+\tfrac{1}{2}kd^2$. The spring PE
formula is therefore derived rather than memorized.

Symbolic answer is a complete answer, and more useful than a number: work scales with the
**square** of the stretch. Double the stretch, quadruple the energy.

**Release from $x=d$ toward equilibrium at $x=0$:** spring force and displacement both
point left, so the spring does positive work, $+\tfrac{1}{2}kd^2$.

$$W_{net} = \Delta KE \Rightarrow \tfrac{1}{2}kd^2 = \tfrac{1}{2}mv^2 - 0 \Rightarrow v = d\sqrt{k/m}$$

F = ma never appeared. That is the point of the chapter.

---

## Misses from this session — drill these

### Miss 1: sign of work read off the force direction

**What happened.** Asked for the sign of work by gravity and by cable tension on a beam
being lifted at constant speed, the answer came from where each force points (gravity
points down, therefore negative).

**The rule.** Work's sign never comes from the force's own direction. It comes from
**the force compared to the DISPLACEMENT.**

- Beam rising: tension positive, gravity negative.
- Same beam being **lowered**: tension **negative**, gravity **positive**. The force
  directions never changed. The displacement did.

**Error class:** concept — wrong reference for a sign convention. Right answer, wrong
reason, so it breaks the moment the problem reverses.

**Second half of that same problem:** constant speed -> end speed = start speed -> dKE = 0
-> the two works cancel exactly. That is the work-energy theorem stated before it was
derived.

### Miss 2: substitution not written into the integrand

**What happened.** Setting up spring work, F(x) was left inside the integral AND the
whole integral was multiplied by -k:

$$\left(\int_{x_1}^{x_2} F(x)\,dx\right)\cdot(-k) \qquad \text{WRONG — counts k twice}$$

The intent was right (pull the constant out of integral of x dx). The notation said
something different, and notation is what gets graded.

**The rule.** F(x) is not a separate object multiplied by -k. **F(x) IS -kx.** The
substitution replaces the symbol:

$$\int_0^d F(x)\,dx = \int_0^d (-kx)\,dx = -k\int_0^d x\,dx$$

Every work problem in this chapter is the same three moves: **identify the function the
force is, put it in the integrand, put start and end positions in the limits.**

**Error class:** notation — correct reasoning, ambiguous written form.

---

## Exact resume point — one faded transfer

A block is released from rest at $x=d>0$ on a horizontal spring and moves toward
equilibrium at $x=0$ while kinetic friction acts; choose values for which it reaches
$x=0$. The agent supplies values but **does not supply the setup**. Before any arithmetic,
Chris must:

1. state the displacement direction;
2. state the sign of the spring's work and friction's work;
3. write the force functions and limits directly in both work integrals; and
4. use $W_{net}=\Delta KE$ to predict whether the final kinetic energy is greater or
   less than the no-friction case.

**Pass for this rep:** directions, signs, and integrands are correct before arithmetic.
After a successful faded rep, use a changed-parameter cold transfer in a later session;
only that later evidence can begin a mastery claim.

## Related pages

- [[dot-product]]
- [[conservation-of-energy]]
- [[conservative-vs-nonconservative-forces]]

## Sources

- Live tutoring session, 2026-09-06, 25-minute constraint.
- Chris's post-session classification: first work-energy problem family in more than six
  months; reactivation win, mastery not tested.
