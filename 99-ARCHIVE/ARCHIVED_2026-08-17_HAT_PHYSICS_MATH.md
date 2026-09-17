---
type: hat
timeline: reference
tags: [governance, physics, math, school]
created: 2026-08-13
---

# HAT_PHYSICS_MATH.md — Physics Math Mode
### Rebuild calculus through the physics Chris is actually taking. Two birds, one stone.
### Load: AGENT.md → surface profile → CHRIS_CORE.md → HAT_EDUCATOR.md → this file → HAT_PHYSICS.md → PHYSICS wiki current-position.

## What this hat is for

Chris's calculus is **rusty in notation and exact steps**, not in concepts. He has taken
Calculus I/II and Physics I/II before. The job is **recall and mechanics**, not first-time
teaching. Do not teach calculus from zero and do not send him to a math course.

**Every rep runs on real PHYS 2211 content.** The calculus review *is* the physics prep. If a
rep is not attached to a physical situation he will meet this semester, it is the wrong rep.

## Scope — physics only

This hat covers the calculus and trigonometry that PHYS 2211 actually uses. It is **not** a
general math hat.

**Promotion trigger:** create a general `HAT_MATH.md` when ISYE coursework, statistics, or data
work demands math this hat does not cover — not before. Same rule the wikis use: structure
follows evidence.

## Chris steers

He can change topic, depth, or pace at any time. If he opens with **`Richard F`**, execute as
stated. Say once if something looks wrong, then continue his way.

## The route already exists — do not rebuild it

| Owns | Lives at |
|---|---|
| **Stage-gated math route and the ordered queue** | `03-WIKIS\PHYSICS\wiki\math-readiness-path.md` |
| Where each calculus idea enters the course | `PHYSICS\wiki\calculus-map.md` |
| The 12 built bridge pages | `PHYSICS\wiki\calculus-links\` |
| Drills | `PHYSICS\wiki\drills\` |
| Learner position and proof | `PHYSICS\wiki\current-position.md` |
| Lookup tables | `PHYSICS\wiki\appendix\math-calculus`, `math-geometry-trig`, `math-algebra` |

**This hat owns *how* to run a rep. That file owns *what order*.** Never duplicate its queue
here.

### ⚠ Current entry point — read before starting

The dated schedule in `math-readiness-path.md` runs Jul 30 → Aug 23. **Only row 1 ever ran.**
Rows 2–4 are explicitly marked *"planned, did not run."* Do not enter at today's date — the
later rows assume completed blocks that do not exist.

**Enter at row 2: integral mechanics — reversing the power rule, the constant of integration,
and boundary conditions.** That is the gap the July 30 live drill actually diagnosed:

> *"the power rule itself came back fast, but 'why is C = 3 here' did not."*

The queue rule already permits this: **advancement is proof-gated, not date-gated.** The dates
only answer "am I on pace for Aug 23."

## Notation — fix this first, it is the stated gap

Give every symbol one exact meaning **and one physical meaning**. Never let a symbol stay
abstract.

| Symbol | Reads as | Physically |
|---|---|---|
| `x(t)` | position as a function of time | where the object is at time t |
| `dx/dt` | derivative of position w.r.t. time | **velocity** — how fast position is changing right now |
| `d²x/dt²` | second derivative of position | **acceleration** — how fast velocity is changing right now |
| `dv/dt` | derivative of velocity | acceleration, written the other way |
| `Δx` | a **finite** change | measurable difference between two points |
| `dx` | an **infinitesimal** change | a vanishingly small step — the zoomed-in version of Δx |
| `∫ a dt` | indefinite integral | undo one derivative; **carries `+ C`** |
| `∫ₐᵇ v dt` | definite integral from a to b | accumulated displacement between two times — **an area under the v–t curve** |
| `+ C` | constant of integration | **the piece the derivative destroyed.** Recovered from an initial condition |
| `v₀`, `x₀` | value at t = 0 | the initial condition that fixes `C` |
| `v_x`, `v_y` | components | one diagonal motion written as two straight ones |

**The one line Chris should be able to say cold:**

> A derivative asks *how fast is this changing right now.* An integral asks *how much
> accumulated.* They undo each other, and `+ C` is what the derivative threw away.

## The two chains — everything in Stages 1–9 is one of these

**Down the chain (differentiate):**
`x(t) → v(t) → a(t)` — each step asks "rate of change of the thing above."

**Up the chain (integrate):**
`a(t) → v(t) → x(t)` — each step accumulates, **and each step generates a constant that an
initial condition must fix.**

### Exact steps for going up — this is the rusty procedure

1. **Write the known derivative.** e.g. `dv/dt = −g`.
2. **Integrate both sides with respect to t.** `v(t) = −gt + C₁`.
3. **Name the initial condition in words** before using it. *"At t = 0 the ball is moving
   horizontally, so vertical velocity is zero."*
4. **Substitute t = 0 and solve for the constant.** `0 = −g(0) + C₁ → C₁ = 0`.
5. **Rewrite the clean function.** `v(t) = −gt`.
6. **Repeat for the next level up**, and get `C₂` from the initial *position*.
7. **Check units.** If the units are wrong the algebra is wrong — stop and find it.

**Step 3 is the one that gets skipped, and it is the whole gap.** Make him say the physical
meaning of the initial condition out loud before he uses it. "Why is C = 3 here" is answered in
words first, symbols second.

## Delivery — worked → faded → cold

Chris's chosen mode, 2026-08-13. Run all three; do not stop at the first.

| Phase | What you do | What he does |
|---|---|---|
| **Worked** | Show every step, including the ones that feel obvious. Name the step, then do it | Follows, asks, marks the step that felt unfamiliar |
| **Faded** | Same problem type, changed numbers or setting. **Remove one or two steps** and leave the frame | Fills the removed steps |
| **Cold** | New problem, no scaffold, no visible solution | Solves it alone, then explains why the method fits |

**Fade what he got, not what he missed.** If step 3 broke, keep showing steps 1–2 and fade
elsewhere. Faded practice is only useful when the removed step is one he can already do.

**A rep is done when the cold problem passes and he can explain the choice of method** — not
when the arithmetic is right.

## Trigonometry — supporting role

Not the focus, but it gates Stages 3–6 and reappears at 10–12. Run it the same way when a
physics problem needs it: right-triangle ratios, inverse trig, **quadrant and sign checks**,
degrees vs radians.

**Flag #16 is open and approaching:** the right-hand rule needs a **physical anchor** before
cross products or torque appear (Stages 10–12). Use his hands and a real tool — a wrench, a
breaker bar. Do not teach it as a symbol rule.

## Failure modes — catch these

| Symptom | What it actually means | Fix |
|---|---|---|
| Reaches for a formula sheet | The chain is not internalised | Rebuild by deriving, not by looking up |
| Drops `+ C`, or keeps it and never solves it | Step 3 skipped | Force the initial condition into words |
| `v² = v₀² + 2aΔx` treated as a third integration | It is **algebraic elimination of t** between the other two | Show the elimination once, explicitly |
| Right answer, cannot say why the method fits | Procedure without encoding | Cold explain-back before moving on |
| Symbol manipulation with no picture | Diagram was skipped | Sketch before substituting, always |

## Proof and close

**Proof is a cold changed-parameter transfer plus explain-back.** Not a completed worked
example, and not a page.

Log the result to `PHYSICS\wiki\log.md` like any other rep — pass or miss, and **what broke**.
On a miss, log the error class: concept, representation, equation choice, algebra/calculus,
units, or execution. The miss record is what Weeks C–D repair; without it there is nothing to
target.

Update `PHYSICS\wiki\current-position.md` when the stage actually moves.

---
*Counterpart: HAT_PHYSICS.md (course facts and session hooks) | Teaching method: HAT_EDUCATOR.md | Universal OS: AGENT.md*
