---
domain: systems
type: framework
tags: [subject/network-optimization, subject/shortest-path, subject/maximum-flow, subject/operations-research]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, operations-research, ksu-support]
---

# Network Optimization Models: Shortest Path, Minimum Spanning Tree, and Maximum Flow

**Summary**: Four classic network problems, each solvable by a dedicated, highly efficient algorithm rather than general LP — the shortest-path problem (fan out from the origin, iteratively find the nth-nearest node), the minimum spanning tree problem (a rare OR problem where a purely greedy algorithm is provably optimal), the maximum flow problem (repeatedly find an "augmenting path" through a residual network until none remain), and the minimum cost flow problem (the general framework unifying transportation, assignment, and shortest-path as special cases).

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 10 ("Network Optimization Models"), sections 10.2–10.5 in full (terminology, shortest path, minimum spanning tree, maximum flow — pp. 372–401 printed / physical ~403–432); sections 10.6–10.7 (minimum cost flow, network simplex method) at conceptual level

**Last updated**: 2026-07-13**

---

## Network Terminology

A network is **nodes** (vertices) connected by **arcs** (links/edges). Arcs are **directed** (one-way flow, labeled from→to) or **undirected/links** (either-way, but actual flow is a net difference — assigning flow "the wrong way" through a directed or undirected arc is a legitimate bookkeeping trick to *reduce* a previously assigned flow, used heavily in the max-flow algorithm below). A **path** is a sequence of distinct arcs connecting two nodes (**directed path** if flow the whole way is feasible, **undirected path** otherwise — undirected paths matter even in directed networks, per the flow-cancellation trick). A **cycle** is a path that returns to its start. Two nodes are **connected** if any undirected path joins them.

A **spanning tree**: starting from *n* nodes with no arcs, add arcs one at a time (each new arc joining an already-connected node to a previously-unconnected one) until all *n* nodes are connected — this always takes exactly **n−1 arcs**, and the result is a *tree* (connected, no cycles). Spanning trees are the structural basis for both the minimum spanning tree problem and the network simplex method's basic feasible solutions.

**Node roles**: a **supply/source node** generates more flow than it receives; a **demand/sink node** receives more than it generates; a **transshipment node** conserves flow (in = out).

## The Shortest-Path Problem

Given an undirected, connected network with nonnegative link distances, find the minimum-total-distance path from an **origin** to a **destination**. **Algorithm** (equivalent to Dijkstra's algorithm): iteratively find the *n*th-nearest node to the origin, fanning outward — at each iteration, every already-solved node's shortest connecting link to an unsolved node is a candidate; the candidate with the smallest (distance-to-solved-node + link distance) becomes the next solved node, and its shortest path/distance is recorded. Stop when the destination becomes solved. This scales efficiently to very large networks and is the workhorse behind real applications like Canadian Pacific Railway's daily shipment routing (an Edelman Award-winning application saving ~$100M/year).

**Variants handled with minor modification**: directed-only shortest paths (restrict candidates to directed arcs), shortest paths from the origin to *every* node (don't stop until all nodes are solved), or all-pairs shortest paths. The "distance" metric doesn't have to be literal distance — cost or time works identically, and shortest-path solving is a common subroutine inside larger combinatorial problems (vehicle routing, network design).

## The Minimum Spanning Tree Problem

Given nodes and *potential* links (each with a positive length/cost), choose exactly n−1 links forming a spanning tree that minimizes total length — i.e., design the cheapest network that still connects everything. Classic applications: telecom network design, transportation/pipeline/power-line network design, circuit-board wiring.

**Algorithm** (equivalent to Prim's algorithm) — one of the few OR problems where a purely **greedy** procedure is provably optimal: (1) pick any node, connect it to its nearest neighbor; (2) repeatedly find the closest *unconnected* node to *any* currently-connected node, and connect it; (3) ties may be broken arbitrarily (a signal of possible — not certain — multiple optimal solutions) and the result is still guaranteed optimal. No lookahead, no backtracking — just always take the cheapest available connection.

## The Maximum Flow Problem

Given a directed network with a single **source**, a single **sink**, all other nodes as transshipment, and a capacity on each arc, find the maximum total flow from source to sink. Classic applications: distribution-network capacity, supply-chain throughput, pipeline flow.

**The residual network**: track, for every arc, how much *additional* flow could still be pushed in each direction — the original direction's residual capacity shrinks as flow is assigned, while the *reverse* direction's residual capacity grows by the same amount (since assigning reverse flow is really just canceling forward flow already committed — the same bookkeeping trick from the terminology section).

**The augmenting path algorithm**: (1) find any directed path from source to sink in the residual network where every arc has strictly positive residual capacity — an **augmenting path**; if none exists, the current solution is already optimal, stop. (2) The path's residual capacity is the *minimum* residual capacity among its arcs — assign that much additional flow along the whole path. (3) Update residual capacities (decrease forward, increase reverse) and repeat. **The key correctness property**: because augmenting paths can partially cancel previously-assigned flow (via the reverse-residual-capacity mechanism), an early suboptimal or "greedy" choice of path never traps the algorithm — it can always be corrected by a later augmenting path that partially undoes it.

## Minimum Cost Flow: The Unifying Framework (Conceptual)

The **minimum cost flow problem** generalizes shortest path, transportation, assignment, and maximum flow into one framework: a directed network with supply/demand nodes, arc capacities, and a per-unit cost on each arc, minimizing total cost while respecting supply/demand and capacity constraints. Because of this generality, it's solved by the **network simplex method** — a specialized version of the general simplex method (see [[simplex-method-mechanics]]) that exploits the network's structure the same way the transportation simplex method does (see [[transportation-and-assignment-problems]]): basic feasible solutions correspond directly to spanning trees, and iterations move between adjacent spanning trees rather than requiring general tableau algebra.

## Key Takeaways

- Each of these four problems has a purpose-built algorithm that vastly outperforms general LP/simplex on the same problem — recognizing which named network-structure a real decision fits is what unlocks the efficient solution method, exactly like recognizing a transportation/assignment problem does (see [[transportation-and-assignment-problems]]).
- The minimum spanning tree problem is a rare, genuinely useful example of "greedy is optimal" in OR — most combinatorial problems punish greedy heuristics, this one doesn't.
- The residual-network / augmenting-path mechanism (assign flow, then track the "undo" capacity in reverse) is a reusable pattern that shows up again in the network simplex method and other flow-based algorithms.
- Minimum cost flow is the unifying generalization — transportation, assignment, and shortest path are all special cases of it, which is why the network simplex method can solve all of them efficiently with one algorithm.

## Connects to

- [[transportation-and-assignment-problems]] — special cases of the general minimum cost flow framework; the transportation simplex method and network simplex method share the same "spanning tree = basic feasible solution" structural insight.
- [[simplex-method-mechanics]] — the network simplex method is a structure-exploiting specialization of general simplex, the same relationship the transportation simplex method has to it.
- [[linear-programming-formulation-and-graphical-solution]] — every network optimization problem here is technically an LP; these algorithms are purpose-built alternatives that are dramatically faster on the network-structured special case.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Routing, network design, and capacity/throughput questions are common real operational-improvement findings — shortest path and max flow especially are broadly applicable |
| Current usefulness | 3 | Immediately applicable to any client engagement involving routing, logistics, or network-capacity questions |
| KSU support | 5 | Standard, heavily-tested intro-OR chapter |
| Tech-stack relevance | 4 | Directly implementable via `networkx` in Python (shortest path, min spanning tree, max flow all have built-in solvers) — very fast to stand up as a working tool |
| Business audit value | 4 | "What's the fastest/cheapest route" (shortest path), "how do we connect everything most cheaply" (min spanning tree), and "what's our true throughput capacity" (max flow) are all concrete, sellable audit questions |
| Data/workflow value | 4 | Requires only a distance/cost/capacity matrix between locations or stages — commonly available or easy to estimate |
| Reading urgency | 4 | First of "chunk 3" — genuinely novel, no overlap with anything in this wiki |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Recognizing a client's routing, network-design, or throughput-capacity question as one of these four named problems, then solving it directly via `networkx` (Python) rather than a general LP setup — dramatically faster to build and solve.

**Use when**:
The decision involves finding a best path (shortest path), designing a minimum-cost connected network (min spanning tree), or determining true throughput capacity through a constrained network (max flow).

**Do not use when**:
The problem doesn't actually have a clean single-source/single-sink or connect-everything structure — a messier multi-commodity or multi-objective network problem may need general LP or a different specialized technique instead.

**Fast retrieval query**:
`subject/network-optimization` + `subject/shortest-path` + `subject/maximum-flow` — or search "augmenting path residual network" / "minimum spanning tree greedy algorithm" / "nth nearest node"

## North Star Connection

- How this applies to the audit business: shortest-path and max-flow algorithms give fast, concrete answers to routing and capacity questions that are common SMB operational-waste findings — "here's your true bottleneck throughput" or "here's the minimum-cost way to connect all your sites" are quantified, credible audit deliverables.
- Track relevance: Systems / KSU / Business — high across all three; genuinely practical and fast to implement.
- Possible future Second Brain use: Yes — a `networkx`-based routing/capacity-analysis Python template is a strong, fast-to-build capability-library candidate.
