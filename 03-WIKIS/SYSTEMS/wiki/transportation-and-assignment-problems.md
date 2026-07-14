---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/ksu-support, subject/linear-programming, subject/transportation-problem, subject/assignment-problem, subject/operations-research]
---

# Transportation and Assignment Problems: Special-Structure LPs Solved Faster Than General Simplex

**Summary**: Two named, highly common LP sub-types — moving a commodity from supply points to demand points at minimum cost (transportation), and matching *n* assignees to *n* tasks one-to-one at minimum cost (assignment) — that share a special all-0/1 constraint structure. That structure lets a streamlined "transportation simplex method" skip the Big M/artificial-variable machinery entirely, and guarantees integer solutions automatically, without ever needing integer-programming techniques.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 9 ("The Transportation and Assignment Problems"), sections 9.1 and 9.3 in full, 9.2 at conceptual/summary level (pp. 319–351 printed / physical pp. 348–380)

**Last updated**: 2026-07-13

---

## The Transportation Problem Model

Given a set of **sources** (each with a fixed supply si) and **destinations** (each with a fixed demand dj), and a per-unit shipping cost cij between every source-destination pair, minimize total distribution cost:

```
Minimize   Z = Σi Σj cij·xij
subject to  Σj xij = si   for each source i   (supply constraints)
            Σi xij = dj   for each destination j  (demand constraints)
and         xij ≥ 0
```

Two assumptions define whether a problem actually fits this model:

- **The requirements assumption**: every source's *entire* supply must be shipped out, and every destination's *entire* demand must be met — no partial slack allowed.
- **The cost assumption**: shipping cost is strictly proportional to quantity shipped (no fixed/setup costs per route).

**The feasible-solutions property**: a transportation problem has any feasible solution at all if and only if total supply exactly equals total demand (Σsi = Σdj). Real problems where supply/demand are *maximums* rather than fixed amounts can be forced to fit by adding a **dummy source** or **dummy destination** that silently absorbs the slack.

**Any problem — regardless of whether it involves literal shipping — that can be described as a parameter table of sources/destinations/supplies/demands/costs fitting this structure is "a transportation problem."** That generality (not the shipping context) is what makes this pattern broadly reusable — the assignment problem below is one such reuse.

**The integer solutions property**: whenever every si and dj is an integer, *every* basic feasible solution — including the optimal one — automatically has integer xij values, with no need to add explicit integer constraints or use integer-programming methods. This falls directly out of the special 0/1 constraint-coefficient structure (Table 9.6 in the source): each variable's column has exactly two 1's (one supply row, one demand row), everything else 0.

## The Transportation Simplex Method (Why It's Faster)

Because every constraint is an equality with this special 0/1 structure, running the *general* simplex method (Big M, artificial variables, full tableau) works but wastes enormous effort relative to what's actually needed. The **transportation simplex method** exploits the structure directly:

- **No artificial variables needed** — a simple direct procedure builds an initial BF solution without the Big M machinery from [[simplex-method-mechanics]].
- **Row 0 is computed directly**, not by row-reduction: for every *basic* cell (i,j), solve `cij − ui − vj = 0` for the dual variables ui (source) and vj (destination) — these have a direct duality-theory interpretation (see [[duality-theory-and-economic-interpretation]]). For every *nonbasic* cell, `cij − ui − vj` is exactly its entering-variable evaluation, at zero extra tableau-manipulation cost.
- **The leaving variable and new solution follow directly from the transportation structure** — no explicit row operations needed.

The efficiency gain is dramatic and grows with problem size: a general simplex tableau for *m* sources and *n* destinations needs roughly (m+n+1) rows by (mn+1) columns, while the transportation simplex tableau needs just *m* rows by *n* columns — for a typical medium problem (m=10, n=100), that's an enormous reduction in what has to be tracked.

## The Assignment Problem: A Special Case of Transportation

Matching *n* assignees to *n* tasks one-to-one at minimum total cost — the assignment problem — is defined by five assumptions: equal numbers of assignees and tasks; each assignee gets exactly one task; each task gets exactly one assignee; a cost cij per assignee-task pairing; minimize total cost. Reformulation tricks handle violations: **dummy assignees/tasks** absorb a count mismatch; **splitting** an assignee or task into identical duplicates handles "assigned to more than one task" cases.

**The model is literally a transportation problem** with m = n, every si = 1, and every dj = 1 — decision variables xij are conceptually binary (1 = assigned, 0 = not), but the **integer solutions property already guarantees binary output** from the plain (non-integer-constrained) LP relaxation, since every supply/demand is exactly 1. This is *why* the assignment problem is covered alongside transportation rather than in the integer-programming chapter — no special integer-programming machinery is ever needed.

**Solving it**: small assignment problems solve fine via general simplex/Solver directly on the binary-relaxed LP. Larger ones are faster via the transportation simplex method (converting the cost table into an equivalent transportation parameter table) or, faster still, the specialized **Hungarian algorithm** — purpose-built for assignment problems and not covered in mechanical detail in this ingest pass (flagged for a future targeted read if hands-on use is needed).

## Key Takeaways

- Transportation and assignment problems are LPs with a name because their constraint structure is common and special (every variable's column has exactly two 1's) — recognizing a real decision as fitting this pattern unlocks a much faster solution method than general simplex.
- The feasible-solutions property (supply = demand) and the dummy-source/destination trick are the standard way real-world supply/demand *imbalances* still get forced into this clean model.
- The integer solutions property is the load-bearing fact that makes the assignment problem solvable as a plain LP relaxation — no integer programming needed, despite assignments obviously being yes/no decisions.
- The transportation simplex method is a worked example of a broader OR technique: exploit a problem's special structure to strip out unnecessary general-purpose machinery (here, the Big M/artificial-variable apparatus) rather than treating every LP as equally hard.

## Connects to

- [[linear-programming-formulation-and-graphical-solution]] — transportation/assignment problems are LPs in standard form once written out in full; the parameter-table shorthand just avoids writing that out explicitly.
- [[simplex-method-mechanics]] — the general method this streamlined variant specializes and accelerates.
- [[duality-theory-and-economic-interpretation]] — the ui/vj values in the transportation simplex are literally the dual variables (shadow prices) for supply/demand constraints, interpretable the same way.
- [[sensitivity-analysis-and-postoptimality]] — the same allowable-range and shadow-price logic applies directly to transportation/assignment solutions.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Resource-to-destination and worker-to-task matching are extremely common SMB operational questions — routing, staffing, territory assignment |
| Current usefulness | 3 | Immediately applicable to any client engagement involving shipping/routing/staffing-assignment decisions |
| KSU support | 5 | Standard, heavily-tested chapter in intro OR — the named special-structure LP every course covers |
| Tech-stack relevance | 4 | Directly implementable via `scipy.optimize.linear_sum_assignment` (assignment) or any LP solver with the transportation parameter table (transportation) — genuinely fast to stand up as a client tool |
| Business audit value | 4 | "Which worker should cover which route/shift/territory to minimize cost" is a concrete, quantified, sellable audit deliverable |
| Data/workflow value | 4 | Requires only a cost/distance matrix plus supply and demand totals — commonly available or easy to estimate from client data |
| Reading urgency | 5 | Fifth and final chunk of this textbook's deterministic-OR ingest — closes out the queued scope (LP formulation → simplex → duality → sensitivity → transportation/assignment) |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Recognizing a client's routing, shipping-allocation, or one-to-one staffing/task-matching decision as a transportation or assignment problem, then solving it directly via `scipy.optimize.linear_sum_assignment` (assignment) or an LP solver's transportation formulation — much faster to build and solve than a general LP setup.

**Use when**:
The decision has a clean "each source ships to multiple destinations" (transportation) or "each assignee gets exactly one task" (assignment) structure with linear costs.

**Do not use when**:
The requirements assumption doesn't hold even after adding dummy sources/destinations (e.g., genuinely flexible partial fulfillment with nonlinear costs), or when assignments aren't strictly one-to-one and can't be reformulated via splitting.

**Fast retrieval query**:
`subject/transportation-problem` + `subject/assignment-problem` — or search "requirements assumption" / "dummy source destination" / "integer solutions property" / "transportation simplex method" / "Hungarian algorithm"

## North Star Connection

- How this applies to the audit business: routing (which truck serves which stop), staffing (which worker covers which shift/route/client), and territory assignment are common SMB operational-waste findings — this gives a fast, named, quantified method to recommend an actual optimal assignment rather than a qualitative suggestion.
- Track relevance: Systems / KSU / Business — high across all three; this is genuinely one of the most directly client-applicable pieces of the whole deterministic-OR sequence.
- Possible future Second Brain use: Yes — a `scipy.optimize.linear_sum_assignment`-based Python template for staffing/routing assignment is a near-ready reusable audit tool.
