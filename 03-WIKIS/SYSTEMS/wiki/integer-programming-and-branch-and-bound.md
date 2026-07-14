---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/ksu-support, subject/integer-programming, subject/branch-and-bound, subject/operations-research]
---

# Integer Programming: Binary Formulation Patterns and the Branch-and-Bound Algorithm

**Summary**: Extends LP to yes/no (binary) and whole-number decisions — a natural fit for capital budgeting, site selection, network design, scheduling, and fleet/crew assignment, where fractional answers (0.6 of a warehouse) are meaningless. Covers the standard binary-variable formulation vocabulary (mutually exclusive alternatives, contingent decisions) and the branch-and-bound algorithm — the general divide-and-conquer solving method behind every practical integer-programming solver.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 12 ("Integer Programming"), sections 12.1–12.2 and 12.6 in full (formulation, applications, branch-and-bound — pp. 474–486 and 502–508 printed / physical ~505–517 and ~533–539); section 12.4 (formulation examples) at conceptual level

**Last updated**: 2026-07-13**

---

## When Integer Programming Is the Right Tool

LP's divisibility assumption (see [[linear-programming-formulation-and-graphical-solution]]) breaks whenever a decision variable genuinely can't take fractional values — a yes/no investment decision, a whole number of trucks, a discrete choice among sites. **Binary Integer Programming (BIP)** restricts variables to {0,1}; **general Integer Programming (IP)** restricts them to any integer; **mixed IP** combines integer-restricted and continuous variables in one model.

## Standard Binary-Variable Formulation Patterns

- **Basic yes/no decision**: `xj = 1 if yes, 0 if no`.
- **Mutually exclusive alternatives** (at most/exactly one choice from a group): `Σ xj ≤ 1` (at most one) or `Σ xj = 1` (exactly one).
- **Contingent decisions** (decision B only makes sense if decision A was also "yes" — e.g., only consider a warehouse in a city if a factory is also being built there): `xB ≤ xA`. This single-inequality pattern is the standard building block for any "B requires A" relationship.

## Real Applications (Why This Matters Practically)

Binary integer programming is one of the most commercially deployed OR techniques, precisely because so many real business decisions are naturally yes/no: **investment analysis** (which fixed investments to make under a budget — a South African defense-capability study saved $1.1B/year; a portfolio-rebalancing model manages $8B+ in assets while minimizing transaction costs); **site selection** (open/close which facilities — AT&T helped 46 customers site telemarketing centers; Norske Skog closed underperforming paper mills, saving $100M/year); **network design** (which plants/distribution centers stay open, and which serve which markets — MISO's massive mixed-BIP electricity dispatch model, 450,000 binary variables, saved ~$2.5B over four years, a Franz Edelman Award winner); **dispatching/routing** (which route/truck/timing combination — Petrobras optimizes daily helicopter routing for offshore oil workers, saving $20M/year); **scheduling interrelated activities** (when to start each activity — Swedish municipalities save $30-45M/year scheduling home care workers); and **airline fleet/crew assignment** (which aircraft type or crew sequence covers which flight leg — Delta saves ~$100M/year on fleet assignment; Netherlands Railways won an Edelman Award for BIP-based timetabling, crew, and rolling-stock scheduling).

## The Branch-and-Bound Algorithm

Any bounded IP problem technically has a finite number of feasible solutions, so brute-force enumeration would *eventually* find the optimum — but that number is typically astronomically large. **Branch-and-bound** is a divide-and-conquer method that examines only a tiny fraction of the full solution space while still guaranteeing optimality, via three repeated steps:

1. **Branching** — partition the remaining solution space into smaller subproblems by fixing one variable's value (e.g., x1 = 0 in one subproblem, x1 = 1 in the other). This builds a **branching tree** (root = "all solutions," each node = a subproblem with some variables fixed).
2. **Bounding** — for each new subproblem, quickly solve its **LP relaxation** (the same subproblem with the integer/binary restriction *removed*, solvable directly by ordinary simplex — see [[simplex-method-mechanics]]). Since the relaxation's feasible region is a superset of the true integer-restricted feasible region, its optimal Z value is a guaranteed **bound** — the true integer-restricted subproblem can never do better than this. (If the objective's coefficients are all integers, the bound can be safely rounded down.)
3. **Fathoming** — discard (fathom) a subproblem, without branching it further, whenever any of three tests is met:
   - **Test 1**: its bound ≤ Z* (the best integer-feasible solution found anywhere so far, the **incumbent**) — it can't possibly beat what's already been found.
   - **Test 2**: its LP relaxation is infeasible — then the more-restricted integer subproblem is certainly infeasible too.
   - **Test 3**: its LP relaxation's optimal solution happens to already be integer-valued — then that's both the relaxation's optimum *and* the true subproblem's optimum, no further branching needed. If it beats the current incumbent, it becomes the new incumbent (which makes Test 1 more powerful for every other still-open subproblem).

**Stopping rule**: continue branching/bounding/fathoming until no unfathomed subproblems remain — the current incumbent is then proven optimal (not just a good candidate).

**Practical branching-order note**: branching from the *most recently created* subproblem (rather than always the best-bound one) lets each new LP relaxation be solved by cheap **reoptimization** from the previous, closely-related tableau (the same technique used in sensitivity analysis — see [[sensitivity-analysis-and-postoptimality]]) rather than resolving from scratch — a major speed factor in large-scale implementations.

## Key Takeaways

- The core insight of branch-and-bound is using the LP relaxation's optimal value as a *provable ceiling* on what any integer solution in that branch could achieve — this is what lets huge swaths of the solution space be discarded (fathomed) without ever being examined individually.
- Fathoming Test 3 (the relaxation's solution happens to already be integer) is why LP relaxations are worth solving at all — sometimes the "hard" integer problem's answer falls out of the "easy" continuous relaxation for free.
- Real-world BIP models are often enormous (hundreds of thousands of binary variables) and still tractable — because branch-and-bound (plus reoptimization) avoids ever needing to enumerate anywhere close to the full solution space.
- The mutually-exclusive-alternatives and contingent-decision formulation patterns cover the large majority of real binary-decision structures — most complex-looking IP models decompose into combinations of these two simple building blocks.

## Connects to

- [[linear-programming-formulation-and-graphical-solution]] — the divisibility assumption this chapter directly relaxes; every LP relaxation solved during branch-and-bound is exactly this page's standard-form LP.
- [[simplex-method-mechanics]] — the algorithm actually used to solve each LP relaxation at the bounding step.
- [[sensitivity-analysis-and-postoptimality]] — the reoptimization technique that makes branch-and-bound fast in practice is the same technique introduced there.
- [[transportation-and-assignment-problems]] — the assignment problem's binary yes/no decision variables are a special case where the integer solutions property makes branch-and-bound unnecessary (the LP relaxation is already guaranteed integer).

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Yes/no business decisions (which investment, which site, which vendor) are extremely common in SMB audit work, and BIP formulation is directly applicable |
| Current usefulness | 4 | Immediately usable the moment a client engagement involves a discrete choice among alternatives under a budget/capacity constraint |
| KSU support | 5 | Standard, heavily-tested intro-OR chapter, natural extension of the LP sequence already ingested |
| Tech-stack relevance | 4 | Directly implementable via PuLP or `scipy.optimize.milp` in Python — branch-and-bound itself is what the solver runs internally, no need to hand-code it |
| Business audit value | 5 | "Which of these N investment options should we fund under this budget" is one of the most directly sellable, quantified audit deliverables in the entire OR toolkit |
| Data/workflow value | 4 | Requires cost/benefit estimates per option plus budget/capacity limits — commonly available or estimable from client data |
| Reading urgency | 4 | Second of "chunk 3" — genuinely novel, natural extension of the deterministic-OR core already ingested |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Formulating a client's discrete "which of these options should we choose" decision (investments, sites, vendors, routes) as a BIP model with mutually-exclusive and contingent-decision constraints, then solving via PuLP/`scipy.optimize.milp`.

**Use when**:
The decision is genuinely discrete (a whole investment, a specific site, a specific route) rather than a continuously divisible quantity — if fractional answers would actually be meaningful, plain LP is faster and simpler.

**Do not use when**:
The problem is actually continuous (use LP) or has the special transportation/assignment structure where the integer solutions property already guarantees integer LP-relaxation answers (see [[transportation-and-assignment-problems]]) — branch-and-bound machinery is unnecessary overhead there.

**Fast retrieval query**:
`subject/integer-programming` + `subject/branch-and-bound` — or search "mutually exclusive alternatives" / "contingent decisions binary" / "LP relaxation bound" / "fathoming test" / "incumbent solution"

## North Star Connection

- How this applies to the audit business: "which subset of these N possible investments/sites/vendors should we choose under this budget" is a directly sellable, quantified deliverable — BIP formulation with mutually-exclusive and contingent-decision constraints turns a qualitative gut call into a defensible optimal recommendation.
- Track relevance: Systems / KSU / Business — high across all three; a natural, practical extension of the LP work already ingested.
- Possible future Second Brain use: Yes — a PuLP-based BIP template (mutually-exclusive-alternatives and contingent-decision constraint patterns pre-built) is a strong, fast-to-build capability-library candidate for investment/site-selection audit deliverables.
