---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/ksu-support, subject/linear-programming, subject/duality-theory, subject/shadow-prices, subject/operations-research]
---

# Duality Theory: The Dual Problem, Shadow Prices, and What the Simplex Method Is Really Doing

**Summary**: Every LP (the "primal") has an associated "dual" LP built from the same parameters, arranged differently — and the dual's optimal solution turns out to be exactly the shadow prices (marginal value per unit of each resource). This isn't a mathematical curiosity: it gives a free-by-product economic interpretation of every simplex tableau, a way to sanity-check a proposed solution without solving anything, and (via the dual simplex method) a computational shortcut when a problem has far fewer variables than constraints.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 6 ("Duality Theory"), sections 6.1–6.2 in full, 6.3–6.5 at summary level (pp. 197–210 printed / physical pp. 226–239)

**Last updated**: 2026-07-13

---

## Constructing the Dual

Given a primal problem in standard form (max Z = cx, subject to Ax ≤ b, x ≥ 0), its **dual** is:

```
Minimize   W = yb
subject to  yA ≥ c
and         y ≥ 0
```

The dual uses *exactly the same parameters* as the primal, just relocated:

1. The primal's objective-function coefficients (c) become the dual's right-hand sides.
2. The primal's right-hand sides (b) become the dual's objective-function coefficients.
3. The primal's constraint coefficient of variable *j* in constraint *i* (aij) is the dual's constraint coefficient of *variable i* in *constraint j* — rows and columns swap roles.

For Wyndor Glass Co. (max Z = 3x1+5x2, s.t. x1≤4, 2x2≤12, 3x1+2x2≤18): the dual has one variable per primal constraint (y1, y2, y3) and one constraint per primal variable — `min W = 4y1+12y2+18y3`, s.t. `y1+3y3 ≥ 3`, `2y2+2y3 ≥ 5`, y ≥ 0.

**A maximization primal always pairs with a minimization dual** (and vice versa — the **symmetry property** means the dual-of-the-dual is the original primal, so which problem gets called "primal" is arbitrary).

## Where the Dual Actually Comes From

The dual isn't an arbitrary construction — it falls directly out of what the simplex method's optimality test is already checking. Row 0 of any simplex tableau already contains a complete dual solution (the coefficients under the slack-variable columns are exactly y1...ym), for free, at every iteration — not just at the end. The simplex method's optimality condition (every row-0 coefficient ≥ 0) is *identical* to dual feasibility. This is why the dual problem can be read informally as "a restatement, in LP terms, of the goal the simplex method is chasing in the primal."

## The Three Duality Properties

- **Weak duality**: for *any* feasible x (primal) and *any* feasible y (dual), `cx ≤ yb` — always. The dual objective is an upper bound on the primal, no matter how far either is from optimal.
- **Strong duality**: at the *optimal* x* and y*, `cx* = y*b` exactly — the optimal objective values are identical for both problems (Wyndor: Z* = 36 = W*).
- **Complementary solutions**: at every iteration (not just the final one), the simplex method's current primal CPF solution x and the dual solution y read off row 0 satisfy `cx = yb` — even while x is feasible and y usually isn't yet (dual feasibility is reached exactly when the primal optimality test passes).

**The duality theorem** (the complete picture of what can happen): if either problem has a bounded optimal solution, so does the other (both properties apply); if one problem is feasible but unbounded, the other has *no* feasible solutions at all; if one problem is infeasible, the other is either also infeasible or unbounded.

## Practical Applications

- **Free sanity-check on a proposed solution.** If someone proposes primal solution x, and you can find *any* feasible dual y (by inspection, no simplex needed) with `cx = yb`, x is proven optimal on the spot. Even if `cx < yb`, the gap `yb − cx` bounds how far x could possibly be from optimal — useful for deciding whether a "good enough" solution is worth formally optimizing further.
- **Solve whichever problem is smaller.** Simplex computational effort scales mainly with the number of *constraints*, not variables. If the dual has fewer constraints than the primal (i.e., the primal has more constraints than variables, m > n), solving the dual directly is computationally cheaper — and its solution hands you the primal's optimum for free via complementary solutions.
- **The dual simplex method** (Ch. 8) runs the same tableau logic but starts from a tableau with a nonnegative row 0 and a negative right-hand side — effectively running the simplex method on the dual while displaying the primal's tableau. This is the natural tool for **reoptimization**: when a solved model's parameters change slightly, the revised final tableau often already fits this "dual-feasible, primal-infeasible" shape, making the dual simplex method faster than resolving from scratch. This is also central to sensitivity analysis — see [[sensitivity-analysis-and-postoptimality]].

## Economic Interpretation: Shadow Prices

This is the single most client-facing-useful part of duality theory. In the standard resource-allocation reading of the primal (xj = level of activity j, cj = unit profit, bi = amount of resource i available, aij = resource i consumed per unit of activity j):

**The dual variable yi is the shadow price of resource i** — the marginal contribution to profit of having one more unit of resource i available, evaluated at the current (or optimal, for yi*) solution. For Wyndor, y2* = 3/2 and y3* = 1 mean: one more hour of Plant 2 capacity is worth $1,500/week more profit; one more hour of Plant 3 capacity is worth $1,000/week more; Plant 1 capacity (y1* = 0) is worthless at the margin — some of it is already going unused.

This reading extends to the whole dual problem:
- Each dual constraint (`Σ aij·yi ≥ cj`) says: *the total marginal value of the resource bundle consumed by one unit of activity j must be at least as large as the profit that activity generates* — otherwise, those resources are being wasted on a less profitable use than they could support.
- **yi ≥ 0** says a resource's marginal value can't be negative — if it were, you'd be better off not using any of that resource at all.
- Minimizing W = Σ bi·yi means minimizing the *total implicit value* of all resources currently being consumed by the chosen activity mix.

**Complementary slackness (the economic punchline)**: at optimality, whenever an activity is actually run (xj > 0), the marginal value of the resources it consumes exactly equals its unit profit (no slack — using the resource there is exactly as good as its next-best use). And whenever a resource isn't fully used up (its slack variable > 0), its shadow price is exactly zero — an unconstrained resource is a "free good" in the same sense supply-and-demand drives the price of an oversupplied good to zero.

**Economic reading of the simplex method itself**: at each iteration, the algorithm is checking every unused activity (nonbasic xj) — is the resource bundle it would consume currently worth *less* than the profit that activity would generate (zj − cj < 0, meaning switch to it — it's a better use of those resources)? Or is it already worth *more* elsewhere (zj − cj > 0, leave it alone)? The entering-variable rule (pick the most negative row-0 coefficient) is just "switch resources toward whichever underused activity would improve profitability the most."

## Key Takeaways

- The dual isn't extra work — every simplex tableau already contains it in row 0, at every iteration, for free.
- Weak duality (`cx ≤ yb` always) + strong duality (`cx* = y*b` at optimality) together mean the dual objective is both a running upper bound on the primal *and* exactly equal to it once both are solved.
- Shadow prices (the dual's optimal solution) directly answer "which resource constraint is actually worth paying to relax, and by how much per unit" — a genuinely client-ready deliverable, distinct from and complementary to the primal solution itself.
- Complementary slackness is the formal version of "a resource that's fully used has value; a resource with slack left over has none" — matching ordinary economic intuition about scarcity and price.

## Connects to

- [[linear-programming-formulation-and-graphical-solution]] — the primal problem and Wyndor Glass Co. example this page builds directly on.
- [[simplex-method-mechanics]] — row 0 of every tableau this page reinterprets as a live dual solution.
- [[sensitivity-analysis-and-postoptimality]] — duality theory's central practical role: reasoning about how the optimal solution changes as parameters change, via the dual simplex method.
- [[transportation-and-assignment-problems]] — transportation problems have their own specialized dual interpretation (node "prices") that follows the identical logic.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Shadow prices are a genuinely client-ready deliverable: "which constraint should you actually pay to relax, and what's it worth" is a sharper, more quantified recommendation than the primal solution alone |
| Current usefulness | 2 | No active client engagement needs this yet |
| KSU support | 5 | Core, heavily-tested ISYE material — duality is one of the two or three ideas an intro OR course is actually built around |
| Tech-stack relevance | 3 | Most LP solvers (PuLP, SciPy, Excel Solver) report shadow prices/dual values automatically as part of standard solution output |
| Business audit value | 4 | "Which resource constraint is worth relaxing, and what's the $/unit value" is a direct, prioritized recommendation for a capacity-investment decision |
| Data/workflow value | 3 | Requires the same data as the primal LP — no extra data collection needed to get the dual's insight |
| Reading urgency | 5 | Third of five chunks in this textbook's deterministic-OR ingest; sensitivity analysis (next chunk) is built directly on duality theory |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Reading shadow prices off a solved LP's dual to answer "which resource constraint would it actually be worth paying to relax, and how much is one more unit of it worth" — a sharper, quantified capacity-investment recommendation.

**Use when**:
An LP has already been formulated and solved (see [[linear-programming-formulation-and-graphical-solution]]) and the client question shifts from "what's the best mix" to "what should we invest in expanding."

**Do not use when**:
The primal hasn't been solved yet, or shadow prices are being extrapolated far beyond the current solution's basis — shadow prices are only valid over the range where the current set of basic variables stays optimal (the actual range is a sensitivity-analysis question — see [[sensitivity-analysis-and-postoptimality]]).

**Fast retrieval query**:
`subject/duality-theory` + `subject/shadow-prices` — or search "weak duality strong duality" / "complementary slackness" / "shadow price marginal value resource" / "dual simplex method"

## North Star Connection

- How this applies to the audit business: shadow prices convert a solved LP into a prioritized capacity-investment recommendation — "expanding Plant 2 by one hour/week is worth $1,500/week, Plant 3 is worth $1,000/week, Plant 1 is worth nothing" is a much stronger client deliverable than just handing over the optimal production plan.
- Track relevance: Systems / KSU — core OR curriculum, directly testable, and the audit application is genuinely deployable once any LP-based engagement exists.
- Possible future Second Brain use: Yes — any Python LP template (PuLP/SciPy) built for audit work should surface dual values/shadow prices alongside the primal solution by default, since most solvers compute them at no extra cost.
