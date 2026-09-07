---
domain: technology
type: concept
timeline: reference
status: wiki-only
tags: [subject/experimental-design, subject/data-science, subject/statistics]
source_role: primary
stack: [r]
---

# Space-Filling, Screening, and Sequential Designs — the DOE Decision Map

**Summary**: Which experimental-design family to use for which job, and why —
from *Experimental Design for Data Science and Engineering* (Joseph, 2026).
Covers the model-based criteria that motivate everything (IMSE/MMSE/entropy),
the space-filling designs that make them practical (minimax, maximin, Latin
hypercube, MaxPro), screening designs for finding the few factors that matter
(Sobol indices, Morris, MOFAT), sequential/active-learning designs including
Bayesian optimization, and the classical fractional-factorial essentials for
physical experiments.

## The decision map

> **First question: what is the experiment for?** The optimal design differs
> by objective, not just by budget.

| Objective | Design family | Workhorse method |
|---|---|---|
| Approximate an unknown response surface (first pass, no data yet) | Space-filling initial design | Maximin Latin hypercube (MmLHD) or MaxPro |
| Find which of many factors matter | Screening design | Morris / MOFAT (cheap), Sobol indices (thorough) |
| Optimize an expensive black-box function | Sequential design | Bayesian optimization via expected improvement |
| Propagate input uncertainty through a model | Distribution-matching design | Support points (see [[data-splitting-twinning-and-subsampling]]) |
| Small, noisy, expensive physical experiment | Fractional factorial | Minimum-aberration 2^(p−k) design |

Two-stage strategy throughout: **space-filling initial design → model → 
sequential refinement**. Rule of thumb for the initial design size: n ≈ 10p
runs for p factors (Loeppky et al.), then let cross-validation error decide
when to stop adding sequential points.

## Why model-based optimal designs fail in practice (Ch 3)

Under a GP model you can define principled criteria: minimize average
prediction variance (**IMSE**), minimize worst-case variance (**MMSE**), or
maximize the information in the runs (**maximum entropy**, ≡ maximize |R|).
The catch: all of them depend on the GP's correlation parameters — which you
cannot know *before* collecting data — and none is robust to guessing them
wrong. The escape: as correlation → 0 these criteria stop needing the unknown
parameters, and the limiting designs are purely **geometric**. Those are the
space-filling designs; they behave reasonably across the whole parameter range
while any tuned "optimal" design can fail badly off its assumption.

## Space-filling designs (Ch 4) — the gas-station anchor

A petroleum company placing stations in a region:

- **Minimax** design minimizes the distance from the *farthest customer* to
  their nearest station — customer-focused, a **covering** design (identical
  minimal balls around the points cover the whole region). Best when you must
  predict everywhere; hard to construct.
- **Maximin** design maximizes the minimum distance *between stations* —
  supplier-focused, a **packing** design (non-overlapping balls as large as
  possible). Easier to build, supports one-point-at-a-time augmentation, tends
  to push points to the boundaries.
- **Latin hypercube (LHD)**: the effect-sparsity insurance policy. Most
  systems obey the Pareto principle — only a few factors matter. A plain
  maximin design collapses to duplicated runs if an unimportant factor drops
  out; an LHD guarantees every factor gets n distinct values (each row and
  column of the grid holds exactly one point), so no run is wasted whichever
  factors turn out dead. A *random* LHD can still be terrible (perfectly
  correlated columns), so optimize within the LHD class → **MmLHD**, the
  de-facto standard for computer experiments.
- **MaxPro** designs (Joseph et al. 2015) go one further: good projections in
  *all* subspace dimensions, not just 1-D, by minimizing
  Σ 1/Π(x_ik − x_jk)² — derived as a Bayesian average of weighted maximin
  criteria over unknown factor importance. Preferred initial design when you
  expect only an unknown subset of factors to be active.

R: `SFDesign` (clustering, minimax, maximin, MmLHD, MaxPro),
`minimaxdesign`, `SLHD`, `LHD`.

## Screening designs (Ch 6) — find the vital few cheaply

- **Sobol sensitivity indices** decompose output variance by functional ANOVA.
  First-order index S_i = share of variance from factor i's main effect;
  **total index T_i** adds every interaction involving i. Screening rule: drop
  a factor only when T_i is small (a small S_i alone can hide interactions).
  Estimation is Monte Carlo (pick-and-freeze/Jansen), cost m(p+1) evaluations
  — e.g. 90,000 runs on the 8-factor borehole test function.
- **Derivative-based measures** (ν_i) bound the total index: ν_i = 0 ⇒
  T_i = 0, so they can *screen out* factors — but they **cannot rank**
  importance: a wiggly-but-flat factor scores high on derivatives while a
  smooth-but-large-effect factor scores low. Screening yes, ordering no.
- **Morris one-factor-at-a-time (OFAT)**: a collection of randomized OFAT
  paths estimating "elementary effects"; plot mean |effect| (μ*) vs its
  variability (σ) to separate important, interacting, and dead factors. Found
  the same borehole answer in **36 runs instead of 90,000**. OFAT done right —
  the classical objection to OFAT (inefficiency, no interactions) is overcome
  by using many randomized paths.
- **MOFAT** (Xiao et al. 2023): recognizes the Sobol pick-and-freeze design is
  itself a collection of OFATs, then optimizes it — LHD columns arranged to
  maximize the expected total-Sobol estimate. Provably optimal under a
  Brownian-motion prior; construct from a single MaxPro/maximin LHD via a
  deterministic transformation. R: `sensitivity` (morris, soboljansen).

## Sequential designs (Ch 7) — active learning

Once data starts arriving, estimate the GP's parameters from the data so far
and pick the next run where it buys the most:

- **Emulation** (approximate the surface): add the point that most reduces
  integrated variance (**ALC**, expensive but even-handed) or sits at maximum
  posterior variance (**ALM**, ~200× faster, drifts to boundaries). Sequential
  designs automatically concentrate effort in the *active* subspace — inactive
  factors get ignored for free, which no fixed design can do.
- **Optimization = Bayesian optimization.** The **expected improvement (EI)**
  acquisition (Jones et al. 1998) has a closed form
  EI = (y_min − ŷ)Φ(u) + s·φ(u), u = (y_min − ŷ)/s, and provably balances
  **exploitation** (low predicted value) against **exploration** (high
  uncertainty) — the same explore/exploit trade seen everywhere from A/B
  testing to RL. Practical notes: batch versions exist for parallel runs; add
  a small nugget λ to the correlation matrix when points crowd together.
- **Inverse design**: to hit arbitrary future targets in output space, build a
  space-filling design *in the output space* (sequential perturbation) and use
  it as a lookup table — 24,000 simulations sufficed against 5.6×10¹⁴ possible
  acoustic metasurface configurations.
- Sequential is not always feasible: a 30-run rocket-injector study at one
  week per simulation ran as a single parallel MaxPro batch (6 weeks) instead
  of sequentially (30+ weeks). Parallelism can beat adaptivity.

## Fractional factorials (Ch 8) — the physical-experiment classics

Physical experiments are expensive, noisy, and slow ⇒ few runs, two levels
per factor, linear models — plus **replication, randomization, blocking**
(all irrelevant to deterministic computer experiments). Essentials that
survive into any ISYE course:

- A 2^(p−k) design runs a 1/2^k fraction of the full factorial; the price is
  **aliasing** — effects sharing a column and becoming inseparable (e.g.
  d4 = d1d2d3 aliases α₄ with α₁₂₃). The **defining relation** generates all
  aliases.
- **Resolution** = shortest word in the defining contrast subgroup (higher is
  better: resolution IV keeps main effects clear of 2-factor interactions);
  **minimum aberration** breaks resolution ties by minimizing the count of
  short words.
- Disentangling aliases uses two empirical principles: **effect hierarchy**
  (lower-order effects more likely to matter) and **effect heredity** (an
  interaction needs at least one active parent). Analysis via half-normal
  plots + Lenth's method; nonregular designs (Plackett-Burman) need variable
  selection (lasso/Dantzig) instead.
- The book's twist: place the prior on the *function* (GP) and derive the
  induced prior on regression coefficients — Bayesian-inspired designs that
  reconnect the classical machinery to Parts I–II. R: `FrF2`.

## Retrieval triggers

- Designing any real test plan (scanner parameter sweep, physics lab,
  client process trial) → decision map above, then the owning chapter.
- KSU DOE/quality coursework → fractional-factorial section first.
- "Too many knobs, which matter?" → screening section (Morris first).
- Expensive optimization loop anywhere (hyperparameters, simulations) →
  Bayesian optimization / EI.

Source: [[experimental-design-for-data-science-and-engineering]]. Related:
[[ab-testing-hypothesis-tests-and-p-values]],
[[generalization-overfitting-and-fitting-graphs]],
[[data-splitting-twinning-and-subsampling]].
