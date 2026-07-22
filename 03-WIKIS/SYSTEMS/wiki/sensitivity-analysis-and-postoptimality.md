---
domain: systems
type: framework
tags: [subject/linear-programming, subject/sensitivity-analysis, subject/operations-research]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, operations-research, ksu-support]
---

# Sensitivity Analysis: Allowable Ranges, the 100% Rule, and Why "Optimal" Is Only a Starting Point

**Summary**: An LP's parameters (aij, bi, cj) are almost never known constants in real life — they're estimates. Sensitivity analysis is the systematic follow-up to solving any real LP: which parameters can move without changing the optimal solution ("allowable range"), which ones are dangerous (sensitive) if the estimate is off, and how to cheaply re-derive the new optimum from the old one instead of resolving from scratch. Plus a conceptual pass over LP-under-uncertainty extensions (robust optimization, chance constraints, stochastic programming with recourse) for when sensitivity analysis alone isn't enough.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 7 ("Linear Programming Under Uncertainty"), sections 7.1–7.2 in full (allowable ranges, 100% rules); sections 7.4–7.6 and Chapter 8 at conceptual/summary level (pp. 226–277 printed / physical pp. 255–306, plus summary coverage of 290–313)

**Last updated**: 2026-07-13

---

## Why This Step Is Not Optional

Real LP parameters are usually quick estimates from busy line personnel, sometimes deliberately biased to protect the estimator — not measured constants. An "optimal" solution is only optimal *with respect to the specific numbers fed into the model*; it becomes a reliable guide for action only after checking it still holds up under reasonable parameter uncertainty. **The two deliverables of sensitivity analysis**: (1) identify the *sensitive parameters* — ones whose value can't move without changing the optimal solution — so they get better estimation effort and closer monitoring during implementation; (2) for parameters that aren't sensitive, find the **allowable range** — how far that parameter can move before the optimal solution (or its feasibility) actually changes.

## Why You Don't Re-Solve From Scratch

For small problems, just re-running the simplex method after each hypothetical parameter change is fine (this is literally what clicking "Solve" again in Excel Solver does). For large real problems, this is wasteful. Because of the same "fundamental insight" that makes duality theory work (see [[duality-theory-and-economic-interpretation]]), the *unchanged* portions of the final simplex tableau (the y* dual-variable vector and S* matrix, i.e., the slack-variable coefficients) let you compute exactly what the revised final tableau would look like — **without repeating any of the original simplex iterations.**

**The general procedure**: (1) revise the model; (2) use the fundamental-insight formulas to directly compute the revised final tableau from the unchanged y*/S* and the new parameters; (3) if needed, apply Gaussian elimination to restore proper form; (4) feasibility test (all basic-variable values still ≥ 0?); (5) optimality test (all row-0 coefficients still ≥ 0?); (6) if either test fails, reoptimize — using the current (revised) tableau as the *starting* tableau for the simplex or dual simplex method, rather than starting over from the origin. Because the starting point is already close to the new answer, reoptimization from here is typically only a handful of iterations, even for a large model.

## Case 1 — Changes in bi (Right-Hand Sides)

Changing a resource-availability value bi only ever changes the **right-side column** of the final tableau (row 0's structure and the coefficient matrix are untouched), so the optimality test never needs re-checking — only feasibility. The revised right-side values come directly from `Z* = y*b_new` and `b* = S*b_new` (or, more cheaply, from an *incremental* version of the same formulas using only Δb).

**The allowable range for bi** is the range of values over which the current optimal *basis* (which variables are basic, not their values) stays feasible — equivalently, the range over which the current shadow price yi* remains a valid predictor of the profit impact of changing bi. Outside this range, the shadow price is no longer trustworthy and the model needs reoptimizing. For Wyndor Glass Co., the allowable range for b2 (Plant 2 capacity) works out to 6 ≤ b2 ≤ 18 — go past 18, and the previously-optimal basis becomes infeasible (some basic variable would go negative).

**The 100% rule for simultaneous bi changes**: shadow prices remain valid for predicting the effect of *several* right-hand-side changes at once, as long as, for each change, you compute what percentage of its individual allowable range (increase or decrease) was used, and those percentages **sum to ≤ 100%**. Above 100%, validity isn't guaranteed (though it might still happen to hold).

## Cases 2–3 — Changes in cj (Objective Function Coefficients)

**For a nonbasic variable xj** (not currently in the solution), the current solution stays optimal as long as `cj ≤ z*j = y*Aj` — i.e., as long as the profit from activating that variable still wouldn't beat what its resource bundle is already earning elsewhere. The quantity `z*j − cj` is called the **reduced cost**: the minimum amount cj's unit cost would need to drop (or unit profit rise) before it becomes worth activating that variable at all — directly readable off row 0 of the final tableau at zero extra computational cost.

**Introducing a brand-new variable/activity** (Case 2b) is handled identically to a nonbasic-variable coefficient change: pretend it was in the original model all along with all-zero coefficients, then check whether its new (nonzero) coefficients satisfy the corresponding dual constraint.

**For a basic variable xj** (currently in the solution, Case 3), it's more involved: since the tableau must stay in *proper form* (the basic variable's own column must be a unit vector), changing its coefficients generally requires re-applying Gaussian elimination to restore proper form — which can itself change the current basic solution's values and trigger the same feasibility/optimality/reoptimization sequence as Case 1.

**The 100% rule for simultaneous cj changes** works identically to the bi version: sum the percentage of each coefficient's allowable range actually used; ≤100% guarantees the original solution is still optimal.

## Reading a Solver's Sensitivity Report

Every mainstream LP solver (Excel Solver, LINGO, LINDO, PuLP/SciPy-adjacent tools) outputs this information automatically after solving: for each constraint, its **shadow price** + **allowable increase/decrease** on its right-hand side; for each variable, its **reduced cost** + **allowable increase/decrease** on its objective coefficient. This is the direct, practical payoff of everything above — a client-ready table answering "how much can each estimate be wrong before the recommendation changes" without re-running anything.

## Beyond Sensitivity Analysis: When Uncertainty Is Too Large

Sensitivity analysis (checking a solved model's robustness to parameter drift) is the default follow-up, but three extensions exist for when uncertainty is too large or too structural for that to be enough:

- **Robust optimization** — reformulates the model to remain feasible and near-optimal across an entire *set* of plausible parameter values simultaneously, rather than checking one solution's tolerance to drift after the fact.
- **Chance constraints** — relax a constraint to require only a high *probability* of being satisfied (rather than certainty), appropriate when occasional, bounded constraint violation is tolerable.
- **Stochastic programming with recourse** — splits decisions into stages (e.g., commit now, adjust later), letting later-stage decisions compensate for early parameter-estimate errors instead of committing to one rigid plan up front.
- **The dual simplex method** (see [[duality-theory-and-economic-interpretation]]) is the standard computational engine for reoptimization after a sensitivity-analysis change — it starts from a dual-feasible, primal-infeasible tableau (exactly the shape a revised final tableau usually takes) and reaches the new optimum in very few iterations.

## Key Takeaways

- Sensitivity analysis isn't optional cleanup — it's the actual deliverable that makes an LP's "optimal solution" trustworthy for real decision-making, given that every input was an estimate.
- The fundamental insight (same one underlying duality theory) means a revised tableau can be computed directly from the *old* final tableau's y*/S*, without repeating any simplex iterations — this is what makes sensitivity analysis computationally cheap even for huge models.
- "Allowable range" has a precise, identical structure for both bi (right-hand sides → feasibility of the current basis) and cj (objective coefficients → optimality of the current basis) — and both come with a 100% rule for handling simultaneous changes.
- Zero allowable increase/decrease on any parameter is itself a signal — it means the current solution is one of multiple tied optimal solutions, not a uniquely robust one.

## Connects to

- [[linear-programming-formulation-and-graphical-solution]] — the four assumptions (especially certainty) this entire chapter directly addresses.
- [[simplex-method-mechanics]] — the tableau structure (row 0, right-side column, basic/nonbasic variables) every sensitivity calculation reads from or revises.
- [[duality-theory-and-economic-interpretation]] — shadow prices, reduced costs, and the dual simplex method are all duality-theory concepts this page directly builds on and reuses.
- [[transportation-and-assignment-problems]] — the same sensitivity-analysis logic (allowable ranges, shadow prices) applies to the specialized transportation/assignment tableau, just computed via the streamlined transportation simplex instead.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | This is the single most client-deliverable-ready piece of the entire deterministic-OR sequence — "here's how much your numbers can be wrong before my recommendation changes" is exactly the kind of credible, honest finding that differentiates real analysis from a guess |
| Current usefulness | 3 | Directly usable the moment any LP-based audit deliverable exists; no engagement currently active |
| KSU support | 5 | Core, heavily-tested ISYE material, and the most practically emphasized chapter of the deterministic-OR sequence in most courses |
| Tech-stack relevance | 4 | Every mainstream solver (Excel Solver, LINGO, PuLP, SciPy) outputs this automatically — knowing how to read it, not compute it by hand, is the real skill |
| Business audit value | 5 | Directly converts a "black box optimal answer" into a defensible, credibility-building client deliverable that names its own limits |
| Data/workflow value | 3 | No new data needed beyond what the base LP already required |
| Reading urgency | 5 | Fourth of five chunks in this textbook's deterministic-OR ingest; the last chunk (transportation/assignment) reuses this page's allowable-range logic directly |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Turning a solved LP's "optimal solution" into a credible client deliverable by stating exactly how much each estimated input (resource availability, unit profit) could be wrong before the recommendation would actually change — read directly off standard solver output (Solver, LINGO, PuLP).

**Use when**:
An LP has been solved (see [[linear-programming-formulation-and-graphical-solution]] and [[simplex-method-mechanics]]) and the deliverable needs to state its own robustness, or when re-solving after a small model change without wanting to start from scratch.

**Do not use when**:
Parameter uncertainty is too large or too structural for a "how far can this drift" framing — reach for robust optimization, chance constraints, or stochastic programming with recourse instead.

**Fast retrieval query**:
`subject/sensitivity-analysis` + `use-case/operations-research` — or search "allowable range shadow price" / "100 percent rule" / "reduced cost" / "reoptimization dual simplex"

## North Star Connection

- How this applies to the audit business: sensitivity analysis is the difference between handing a client a single fragile number and handing them a defensible range — "this recommendation holds even if your cost estimate is off by up to $X" is a materially stronger, more trustworthy deliverable, and it costs nothing extra since every mainstream solver computes it automatically.
- Track relevance: Systems / KSU / Business — genuinely the highest cross-track-relevance page in this whole textbook ingest.
- Possible future Second Brain use: Yes — any Python (PuLP/SciPy) audit LP template should surface the sensitivity report (shadow prices, reduced costs, allowable ranges) as standard output, not an optional extra.
