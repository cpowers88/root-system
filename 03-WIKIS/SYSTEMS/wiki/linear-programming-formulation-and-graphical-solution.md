---
domain: systems
type: framework
tags: [subject/linear-programming, subject/operations-research, subject/optimization]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, operations-research, ksu-support]
---

# Linear Programming: Formulation, Standard Form, and the Graphical Method

**Summary**: How to turn a resource-allocation decision into a linear programming (LP) model — using Hillier & Lieberman's canonical Wyndor Glass Co. product-mix problem — plus the general "standard form" terminology (decision variables, objective function, constraints, feasible region, CPF solutions) and the four assumptions (proportionality, additivity, divisibility, certainty) that determine whether a real problem actually fits LP.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 3 ("Introduction to Linear Programming"), sections 3.1–3.3 (pp. 26–52 printed / physical pp. 55–81)

**Last updated**: 2026-07-13

---

## The Prototype Example: Wyndor Glass Co.

Wyndor Glass Co. has three plants (Plant 1: aluminum frames, Plant 2: wood frames, Plant 3: glass + assembly) and wants to launch two new products — an aluminum-framed glass door (Product 1) and a wood-framed window (Product 2) — that compete for the same limited plant capacity. The OR team's job: pick production rates that maximize profit without exceeding any plant's available hours.

Letting x1 = batches of Product 1/week, x2 = batches of Product 2/week, Z = weekly profit ($000s), the data (1 hr/batch of Product 1 in Plant 1, 4 hrs available; 2 hrs/batch of Product 2 in Plant 2, 12 hrs available; 3 hrs + 2 hrs/batch in Plant 3, 18 hrs available; profit $3,000 and $5,000/batch) becomes:

```
Maximize   Z = 3x1 + 5x2
subject to      x1        ≤ 4
               2x2        ≤ 12
            3x1 + 2x2      ≤ 18
and         x1 ≥ 0, x2 ≥ 0
```

This is a **resource-allocation problem** — the most common LP type. Its signature: functional constraints are all resource constraints (amount-used-on-the-left ≤ amount-available-on-the-right).

## The Graphical Method

With only two decision variables, the feasible region can be plotted directly: each constraint becomes a boundary line, nonnegativity confines the region to the first quadrant, and the intersection of all the half-plane restrictions is the **feasible region** (for Wyndor: a five-cornered polygon).

The objective function Z = 3x1 + 5x2 traces a family of *parallel* lines as Z varies (slope fixed at −3/5, since Z = 3x1 + 5x2 ⟺ x2 = −(3/5)x1 + Z/5). Sliding this line through the feasible region in the improving direction and stopping at the last point still inside the region finds the optimum — for Wyndor, the line passes through **(x1, x2) = (2, 6)** last, giving **Z = 36** ($36,000/week). This "sliding ruler" procedure generalizes to any two-variable LP but doesn't extend past three variables — that's what the simplex method (see [[simplex-method-mechanics]]) is for.

## Standard Form and General Terminology

Generalizing Wyndor's structure to *m* resources and *n* activities:

- **Z** = overall measure of performance (the objective)
- **xj** = level of activity *j* (the decision variables, *j* = 1...n)
- **cj** = increase in Z per unit increase in activity *j*
- **bi** = amount of resource *i* available (*i* = 1...m)
- **aij** = amount of resource *i* consumed per unit of activity *j*

**Standard form:**
```
Maximize   Z = c1x1 + c2x2 + ... + cnxn
subject to  a11x1 + a12x2 + ... + a1nxn ≤ b1
            a21x1 + a22x2 + ... + a2nxn ≤ b2
            ⋮
            am1x1 + am2x2 + ... + amnxn ≤ bm
and         x1 ≥ 0, x2 ≥ 0, ..., xn ≥ 0
```

The maximized function is the **objective function**; the resource limits are **functional constraints** (or structural constraints); the xj ≥ 0 lines are **nonnegativity constraints**. A problem is still "linear programming" even if it mixes in the other legitimate forms: **minimizing** instead of maximizing, **≥** constraints, **=** constraints (equality), or **unrestricted-in-sign** variables (nonnegativity dropped for some xj).

### Solution Vocabulary

- **Solution** — any specification of values for the decision variables, feasible or not (unlike everyday usage, this isn't "the final answer").
- **Feasible solution** — satisfies every constraint. **Infeasible** — violates at least one.
- **Feasible region** — the set of all feasible solutions. A problem can have *no* feasible solutions (an over-constrained model, e.g. adding "3x1+5x2 ≥ 50" to Wyndor eliminates the entire region).
- **Optimal solution** — a feasible solution with the best objective value. A problem can have zero optimal solutions if (1) it's infeasible, or (2) Z is **unbounded** — nothing stops it from improving forever in the favorable direction (e.g. Wyndor with only the "x1 ≤ 4" constraint: x2 can rise without limit).
- **Multiple optimal solutions** are possible (an entire line segment tied for best Z) — but if they exist, there are infinitely many, all sharing the same optimal Z.
- **Corner-point feasible (CPF) solution** — a solution sitting at a corner (vertex/extreme point) of the feasible region.

**The load-bearing theorem the simplex method is built on**: for any LP with feasible solutions and a bounded feasible region, at least one optimal solution exists, and *the best CPF solution is always an optimal solution*. A single unique optimum must be a CPF solution; if there are multiple optima, at least two of them are CPF solutions. This is *why* the simplex method only ever needs to search among corner points rather than the entire (infinite) feasible region — see [[simplex-method-mechanics]].

## The Four Assumptions of Linear Programming

Every LP model implicitly assumes all four of these hold. When they don't (beyond minor, tolerable disparities), a different model class is needed — knowing which assumption breaks tells you which alternative technique to reach for.

1. **Proportionality** — each activity's contribution to Z (the cjxj term) and to each constraint (the aijxj term) is strictly proportional to its level xj; no exponents other than 1. Violated by start-up costs (a fixed cost hit the moment xj > 0), increasing marginal returns (economies of scale — the profit curve bends *up*), or decreasing marginal returns (rising marketing cost per additional unit sold — the curve bends *down*). **Break this assumption → nonlinear programming**, or (if the violation is only a start-up cost) **mixed integer programming** (the "fixed-charge problem").
2. **Additivity** — every function (objective or constraint) is the *sum* of each activity's individual contribution — no cross-product terms. Violated when products interact: complementary products (a shared ad campaign makes their joint profit *more* than the sum of solo profits) or competing products (shared machinery requires costly changeovers, making joint profit or joint resource use *less/more* than the simple sum). **Break this assumption → nonlinear programming.**
3. **Divisibility** — decision variables may take *any* value, including fractions, satisfying the constraints; activities can run at fractional levels. Breaks when variables must be integers (a discrete number of machines, trucks, or projects). **Break this assumption → integer programming.**
4. **Certainty** — every parameter (cj, aij, bi) is a known constant. In practice this is *almost never* exactly true, since parameters are usually predictions of future conditions. This is why **sensitivity analysis** (identifying which parameters are "sensitive" — i.e., a change in them would change the optimal solution) is treated as a near-mandatory follow-up step after solving any real LP — see [[sensitivity-analysis-and-postoptimality]]. When uncertainty is too large for sensitivity analysis alone, LP-under-uncertainty techniques (robust optimization, chance constraints, stochastic programming with recourse) apply instead.

**In practice**: almost no real LP satisfies all four assumptions *perfectly* — minor disparities are expected and tolerated (divisibility is usually the exception — it's often exactly true or exactly false). The discipline is checking how *large* each disparity actually is, not whether it's technically zero.

## Key Takeaways

- LP formulation always starts the same way: name the decision variables, write Z as a linear combination of them, then express every resource/policy limit as a linear inequality or equation in those same variables.
- The graphical method (2 variables only, extendable with difficulty to 3) works by sliding a family of parallel objective-function lines through the feasible region — mechanically identical in spirit to what the simplex method does algebraically in higher dimensions.
- The CPF-solution theorem is the reason the simplex method is efficient at all: instead of searching an infinite feasible region, it only ever needs to check corner points.
- The four assumptions are a diagnostic checklist, not a pass/fail gate — knowing which one is violated (and by how much) tells you whether plain LP is still good enough, or whether you need nonlinear, integer, or stochastic programming instead.

## Connects to

- [[simplex-method-mechanics]] — the general n-variable algorithm that formalizes the "slide along corner points" logic this page introduces graphically.
- [[duality-theory-and-economic-interpretation]] — every LP formulated here has an associated "dual" problem with its own economic meaning.
- [[sensitivity-analysis-and-postoptimality]] — the direct answer to the certainty assumption almost never holding exactly.
- [[transportation-and-assignment-problems]] — a structured special case of the same standard-form LP, solvable faster than general simplex.
- [[eoq-model-and-lot-sizing]] and [[wagner-whitin-dynamic-lot-sizing]] — inventory-theory models that are themselves optimization problems, though solved by specialized methods rather than general LP.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | LP formulation is a genuinely reusable audit/analysis skill (resource allocation, product mix, staffing) once a client engagement involves any constrained-optimization decision |
| Current usefulness | 3 | No active client engagement needs this yet, but it's immediately applicable the moment one does |
| KSU support | 5 | Canonical opening chapter of the ISYE operations-research sequence — foundational, testable, unavoidable |
| Tech-stack relevance | 3 | Directly implementable in Python (PuLP/SciPy) or Excel Solver for real client deliverables |
| Business audit value | 3 | Product-mix, staffing-mix, and resource-allocation questions are common enough in SMB audits to make this reusable |
| Data/workflow value | 3 | Requires per-unit resource usage and availability data — obtainable from most operational clients |
| Reading urgency | 5 | First of a five-page chunked ingest of this textbook's deterministic-OR core; everything downstream (simplex, duality, sensitivity, transportation) assumes this page's vocabulary |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Formulating a real constrained-optimization decision (product mix, staffing mix, resource allocation) as an LP model before solving it — either graphically (2 variables, for intuition) or via simplex/software (general case).

**Use when**:
A client or ISYE problem set presents a "maximize/minimize subject to limited resources" decision with linear costs/benefits and linear resource consumption.

**Do not use when**:
Any of the four assumptions is badly violated — reach instead for nonlinear programming (proportionality/additivity broken), integer programming (divisibility broken), or LP-under-uncertainty techniques (certainty badly broken, beyond what sensitivity analysis can absorb).

**Fast retrieval query**:
`subject/linear-programming` + `use-case/operations-research` — or search "Wyndor Glass" / "corner-point feasible solution" / "standard form linear programming" / "four assumptions proportionality additivity divisibility certainty"

## North Star Connection

- How this applies to the audit business: any client decision phrased as "how much of X vs. Y should we produce/staff/allocate, given limited Z" is a candidate LP formulation — a fast, credible, quantified recommendation instead of a gut call.
- Track relevance: Systems / KSU — this is the entry point to the entire deterministic-OR sequence (Ch. 3–10) that ISYE 2600 and later courses build on.
- Possible future Second Brain use: Yes — a Python (PuLP) LP-formulation template is a plausible reusable audit tool once a resource-allocation engagement occurs.
