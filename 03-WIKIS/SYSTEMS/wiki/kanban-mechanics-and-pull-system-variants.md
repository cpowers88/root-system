---
domain: systems
type: framework
tags: [priority/next, status/wiki-only, domain/systems, source-role/primary, use-case/process-design, use-case/systems-analysis, use-case/ksu-support, subject/kanban, subject/pull-systems, subject/inventory-control, subject/factory-physics]
---

# Kanban Mechanics: Two-Card, One-Card, and the Base Stock Equivalence

**Summary**: The literal mechanics of Toyota-style kanban — the two-card system's production/move-card choreography, why some plants simplify to one card or no cards at all, and the book's key theoretical move: showing that a one-card kanban system is mathematically almost identical to the base stock model from Chapter 2, with the card count playing the role of the base stock level.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 4 ("From the JIT Revolution to Lean Manufacturing"), sections 4.6.1-4.6.3

**Last updated**: 2026-06-21

---

## The Two-Card System: Production Cards and Move Cards

Classic Toyota-style kanban uses two distinct card types, because when workstations are spatially distributed, in-process inventory must be staged in **two** places — an outbound stockpoint (just finished at the upstream machine) and an inbound stockpoint (moved to, but not yet processed by, the next machine):

- A **production card** authorizes a workstation to process a part. An operator picks up a production card and the necessary materials; if materials aren't available, the operator switches to a different production card instead of idling on that one.
- A **move card** authorizes movement of materials from an outbound stockpoint to the downstream inbound stockpoint. Periodically, a **mover** checks the box of move cards, retrieves the indicated materials from their outbound stockpoints, swaps each part's production card for a move card, and carries the materials to the appropriate inbound stockpoint. The removed production cards return to their home workstation's box — signaling that the outbound stock there needs replenishing.

**The closed-loop logic**: every card is always attached to either a physical part or sitting in a box waiting to authorize work — cards are never created or destroyed, only circulated. This fixed, finite card count is the entire mechanism by which kanban enforces a hard WIP ceiling.

## One-Card Kanban and the Two-Card/One-Card Equivalence

When workstations sit close enough together that WIP can effectively be "handed" directly from one process to the next, the two separate stockpoints (and the move-card layer) become unnecessary, and a simpler **one-card system** suffices: an operator still needs a production card and materials to begin work, but instead of removing a move card from incoming materials, the worker removes the production card from the *upstream* process and sends it back upstream directly.

**The book's key structural insight**: a two-card system is mathematically identical to a one-card system in which the move operation is itself treated as a workstation. The choice between them therefore reduces to a single practical question — **how much do we need to regulate the WIP tied up in the move operation itself?** If moves are fast and predictable, the extra move-card layer is unnecessary overhead; if moves are slow or irregular, the move card gives useful, direct control over that WIP.

## Cardless Variants: Kanban Squares and Electronic Kanban

Many real implementations dispense with physical cards entirely while keeping the same WIP-limiting logic:
- A simple count limit on the number of containers allowed in a line.
- A **kanban square** — a marked floor location specifying exactly what and how much WIP may sit there.
- **Electronic kanban** — WIP tracked in and out via bar codes, IR tags, or RF transponders, with software enforcing the same limits a physical card would.

All of these are functionally equivalent: a fixed cap on WIP at each station, enforced by whatever signaling mechanism is most convenient for that environment.

## Kanban Is a Base Stock System With a WIP Cap

The book draws a precise and important equivalence to material already established in [[qr-model-and-lead-time-variability]] and [[statistical-inventory-models-newsvendor-base-stock]]: consider a one-card kanban system with **m** production cards at a station. Each time the downstream stockpoint's inventory drops below m, a production card frees up, authorizing replenishment. **This is mechanically almost identical to the base stock model**, with the downstream station acting as the demand source and the card count m serving as the base stock level.

**The one critical difference**: a pure base stock system places no limit on the amount of work that can be in process at once — backlog can grow without bound. A kanban system *does* limit it, because the backlog (unfilled demand) can never exceed the production card count m. This single distinction is the entire reason kanban behaves differently from an unconstrained base stock policy under variability or disruption — but otherwise, the intuition already built for base stock systems (safety-stock-like buffering of demand variability) carries over directly to kanban.

## Why JIT/Kanban Eventually Lost Ground to ERP

By the late 1980s, JIT/kanban had become a well-defined, mature practice that appeared to fully eclipse MRP II — but it did not last, eventually losing out to management's preference for a single integrated information-technology framework spanning all business processes (manufacturing included): enterprise resource planning. See [[erp-and-scm-history-and-tradeoffs]] for the resulting ERP/SCM era, and [[goodbye-jit-hello-lean]] for what replaced JIT's branding (and Six Sigma's replacement of TQM) once the pendulum swung again.

## Key Takeaways

- The two-card system exists specifically to manage WIP across two distinct stockpoints (outbound and inbound) when workstations are spatially separated; a one-card system collapses this when stations are close enough for direct hand-off.
- A two-card system is provably equivalent to a one-card system that treats the move operation itself as a workstation — the real decision is whether move-operation WIP needs independent regulation.
- Kanban squares and electronic kanban are functionally identical to physical cards: a fixed WIP cap, enforced by whatever mechanism fits the environment.
- The single most important theoretical result in this material: one-card kanban is a base stock system with an added hard cap on backlog (limited by the card count m) — everything already known about base stock dynamics from Chapter 2 transfers directly to kanban, with this one structural difference.

## Connects to

- [[statistical-inventory-models-newsvendor-base-stock]] — the base stock model this page shows kanban to be mathematically equivalent to (with a backlog cap added).
- [[qr-model-and-lead-time-variability]] — the broader inventory-control intuition (safety stock vs. cycle stock, variability buffering) that the book says carries over directly to kanban.
- [[mrp-history-and-push-pull-paradigm]] — the original push-vs-pull framing that this page's card mechanics make concrete.
- [[capacity-planning-and-shop-floor-control]] — the I/O-control-vs-kanban contrast (kanban controls WIP directly and continuously; I/O control reacts after the fact) is the practical payoff of this page's mechanics.
- [[jit-implementation-tactics-and-quality-revolution]] — kanban's hard WIP cap is the mechanism that forces the quality discipline described there (no buffer to hide a bad part behind).

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Kanban-square / electronic-kanban variants are directly implementable for a client without needing a literal card system |
| Current usefulness | 3 | Useful whenever a client's WIP-control problem could be solved with a simple visual or electronic cap rather than a software scheduling system |
| KSU support | 5 | Canonical pull-system mechanics and the base-stock equivalence is a genuinely elegant, exam-relevant result |
| Tech-stack relevance | 3 | Electronic kanban (bar codes, RF tags) is a plausible lightweight-automation build for a client |
| Business audit value | 4 | The "is this really two systems or one" simplification logic (two-card vs. one-card) is a useful diagnostic for over-engineered WIP-control systems |
| Data/workflow value | 3 | The base-stock equivalence gives a concrete quantitative handle (m = base stock level) for sizing a kanban system |
| Reading urgency | 3 | Finishes Chapter 4's core technical content |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Systems-analysis / process-design — sizing or simplifying a client's WIP-control mechanism (deciding card count, or whether two-card complexity is even needed), or recommending a lightweight kanban-square/electronic-kanban implementation instead of a full software scheduling system

**Use when**:
A client has excess WIP and no direct control mechanism for it (relying instead on after-the-fact reports), or is over-engineering a two-stockpoint card system where stations are actually close enough for a simpler one-card or kanban-square approach.

**Do not use when**:
A client's demand or routing is too irregular for any fixed-WIP-cap system to make sense (e.g., true job-shop, highly variable routings) — kanban assumes a relatively stable, repetitive flow.

**Fast retrieval query**:
`subject/kanban` + `use-case/process-design` — or search "two-card kanban" / "kanban square" / "base stock equivalence" / "production card move card"

## North Star Connection

- How this applies to the audit business: the one-card vs. two-card simplification question ("do we actually need to regulate WIP in the move operation, or can we hand off directly?") is a fast, concrete diagnostic for any client with a multi-stage process and visible WIP buildup — often a kanban-square or electronic-kanban fix is far cheaper than a software project. The base-stock equivalence also gives a defensible quantitative method (size m using base-stock-style reasoning) for actually sizing a recommended WIP cap, rather than guessing.
- Track relevance: Systems / KSU — strong; this is some of the most quantitatively elegant material in the chapter.
- Possible future Second Brain use: Not yet — but a strong future candidate for an audit "WIP cap sizing" worksheet once base-stock/kanban math is in regular use.
