---
domain: systems
type: framework
tags: [priority/next, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/ksu-support, subject/transshipment-problem, subject/transportation-problem, subject/operations-research]
---

# The Transshipment Problem

**Summary**: An extension of the transportation problem ([[transportation-and-assignment-problems]]) for when shipments can route through intermediate transfer points rather than going directly from source to destination — genuinely useful whenever the cheapest route isn't obvious in advance. Solved by a clean reformulation trick: treat every location (source, destination, or junction) as simultaneously a potential source *and* destination, then hand the result to the ordinary transportation simplex method.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 23 ("Additional Special Types of Linear Programming Problems"), section 23.1 ("The Transshipment Problem") — physical ~1177 of the book

**Last updated**: 2026-07-13**

---

## Why the Plain Transportation Model Isn't Enough

The transportation problem (see [[transportation-and-assignment-problems]]) assumes each source ships directly to each destination at a known fixed cost. In reality, routing through **intermediate transfer points (junctions)** — other sources, other destinations, or dedicated hub locations — can be cheaper than any direct route, but figuring out the cheapest routing by hand becomes intractable fast as the number of possible junctions grows. The **transshipment problem** extends the transportation model to let a solver figure out both *how much* to ship between every pair of locations *and* what route each shipment should follow, simultaneously, as one optimization.

**Formally**: the transshipment problem is the special case of the minimum cost flow problem (see [[network-optimization-models]]) with no limits on shipping-lane capacity — every arc can carry unlimited flow, so the only thing being optimized is which routes to use and how much to route through each.

## The Reformulation Trick

**Treat every location — sources, destinations, and junctions alike — as both a potential source and a potential destination simultaneously.** A shipment that actually travels cannery → junction → warehouse is modeled as *two separate transportation-problem shipments*: cannery-to-junction (first leg), then junction-to-warehouse (second leg), with the junction acting as a destination for the first leg and a source for the second. Because every location plays both roles, the reformulated parameter table is *square* (n sources × n destinations, where n = the total location count), with the diagonal entries (a location "shipping to itself") assigned zero cost — a bookkeeping fiction representing "no shipment happens here."

**The demand/supply values for junctions and true transfer volume need a safe upper bound**, since the actual amount transshipped through any given location isn't known in advance — a large enough bound (e.g., the total system-wide shipment volume) added to that location's demand and supply ensures the reformulation doesn't accidentally constrain a valid routing.

**Once reformulated this way, the transshipment problem is solved directly by the ordinary transportation simplex method** (see [[transportation-and-assignment-problems]]) — no new solution algorithm is needed, only the reformulation. (It's equally solvable via the more general network simplex method, since it's also a minimum cost flow special case.)

## Key Takeaways

- The transshipment problem is not a new algorithm — it's a clever reformulation that makes an apparently harder problem (routing through unknown intermediate points) solvable by machinery already built for the simpler transportation problem.
- Treating every location as simultaneously a source and a destination, with zero-cost "self-shipment" on the diagonal, is the general pattern for handling this kind of "which route, not just which amount" decision within a transportation-style model.
- This directly generalizes to any logistics network where the cheapest path between two points isn't obvious and might legitimately route through a third location.

## Connects to

- [[transportation-and-assignment-problems]] — the transshipment problem is solved by direct reformulation into (and reuse of) this exact model and its transportation simplex solution method.
- [[network-optimization-models]] — the transshipment problem is the unlimited-arc-capacity special case of the general minimum cost flow problem, and is equally solvable via the network simplex method.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | Real logistics/routing value for any client with a multi-hop distribution network, though narrower than the base transportation/assignment case |
| Current usefulness | 3 | Directly applicable the moment a client's distribution network has real intermediate transfer points |
| KSU support | 3 | A recognized, testable extension of the transportation problem, though a smaller topic than the base model |
| Tech-stack relevance | 4 | Trivial to implement once recognized — just expand the parameter table to a square source=destination form and hand it to any transportation/LP solver already covered |
| Business audit value | 3 | Directly useful for any client whose distribution network genuinely has multiple viable routing options through intermediate points |
| Data/workflow value | 3 | Requires the same cost/supply/demand data as a transportation problem, just for a larger (all-locations-squared) network |
| Reading urgency | 2 | Small, clean extension rather than a major new topic — appropriately scoped as a short page |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Optimizing a distribution network where shipments can legitimately route through intermediate transfer points/hubs, not just directly from source to destination — reformulate as a square all-locations transportation problem and solve with the transportation simplex method.

**Use when**:
A client's logistics network has genuine multi-hop routing options and the cheapest routing isn't obvious by inspection.

**Do not use when**:
Every shipment genuinely must go direct (no real transfer points exist) — the plain transportation problem is simpler and sufficient.

**Fast retrieval query**:
`subject/transshipment-problem` — or search "junction transfer point" / "square parameter table diagonal zero cost" / "reformulate as transportation problem"

## North Star Connection

- How this applies to the audit business: distribution-network clients with real multi-hop routing options (not just direct source-to-destination shipping) benefit from this extension — it's the natural next step once a client's logistics question is more complex than a plain transportation problem.
- Track relevance: Systems / Business — a clean, practical extension of the transportation model already covered.
- Possible future Second Brain use: Low priority as a standalone tool — best folded into a broader transportation/logistics optimization template as an option, not built separately.
