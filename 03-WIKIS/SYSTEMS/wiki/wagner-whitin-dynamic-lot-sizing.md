---
domain: systems
type: framework
tags: [subject/wagner-whitin, subject/inventory-control, subject/factory-physics]
timeline: later
status: wiki-only
source_role: primary
use_cases: [systems-analysis, operations-research, ksu-support]
---

# Wagner-Whitin: Optimal Lot Sizing When Demand Varies

**Summary**: The Wagner-Whitin algorithm extends the EOQ tradeoff (setup cost vs. holding cost) to the realistic case where demand is known but varies period to period — common in MRP-driven environments — and proves a structural property that makes the problem tractable to solve exactly.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 2 ("Inventory Control: From EOQ to ROP"), dynamic lot-sizing section

**Last updated**: 2026-06-21

---

## The Problem EOQ Can't Solve

[[eoq-model-and-lot-sizing]] assumes demand is constant over time. In practice, demand often varies by period in a *known* way — a known production schedule, known seasonal pattern, or a parent-item's MRP-generated requirements cascading down to a component. The question becomes: given a sequence of known period demands, when should you place replenishment orders, and how large should each be, to minimize total setup-plus-holding cost over the planning horizon?

## The Wagner-Whitin Property

The algorithm's tractability rests on a key structural insight, the **Wagner-Whitin Property**: in an optimal solution, **it is never optimal to order in a period and also carry inventory into that period from a previous order.** Every period's beginning inventory is either zero (a new order is placed to cover it) or carried entirely from the most recent order — orders are never "topped up." This collapses what looks like a combinatorial explosion of possible ordering patterns into a much smaller, well-defined set of candidate solutions: each period either starts a new "order horizon" or is covered by exactly one prior order.

## The Algorithm

Wagner-Whitin uses this property to solve the lot-sizing problem exactly via a form of dynamic programming: working forward period by period, it computes the minimum-cost way to cover demand through each period, considering only candidate plans where an order in some period j covers demand for periods j through k without any leftover carried into period j from an earlier order. The optimal solution is read off by tracing back through the lowest-cost path.

**Practically**: this is the same setup-cost-vs-holding-cost tradeoff as EOQ, but solved exactly for a finite horizon of *known, varying* demands rather than assuming a constant rate forever. This is the theoretical basis for the lot-sizing logic inside most MRP systems — when MRP software decides "produce 340 units in week 3 to cover weeks 3-5," it is (in principle) solving a Wagner-Whitin-style problem, even if in practice many MRP implementations use cruder heuristics (lot-for-lot, fixed order quantity, period order quantity) instead of running the full algorithm.

## Why This Matters Operationally

- It formalizes exactly the lot-sizing decision MRP systems automate, which is directly relevant to understanding (and auditing) how a client's MRP/ERP system is configured to size its production or purchase orders (see [[american-manufacturing-origins-and-system]] and the broader MRP discussion in the book's Chapter 3).
- The Wagner-Whitin Property itself — never top up an existing order — is a useful sanity check on any client's actual ordering behavior: if a client is placing small replenishment orders *while* still holding leftover stock from a previous large order, that pattern is provably suboptimal under this model, regardless of the specific numbers.

**Audit-usable framing**: if a client's purchasing or production-order pattern shows orders being placed before existing stock from a prior order is exhausted, with no documented reason (e.g., supplier minimums, transportation consolidation), that's a flag worth investigating — it's the literal violation of the property that makes dynamic lot-sizing solvable, and a likely sign of ad hoc rather than systematic ordering.

## Key Takeaways

- Wagner-Whitin solves the same cost tradeoff as EOQ (setup vs. holding) but for known, time-varying demand instead of a constant rate.
- The Wagner-Whitin Property — never order while carrying leftover inventory from a previous order into the same period — is what makes an otherwise huge combinatorial problem solvable exactly, and doubles as a quick real-world audit check.
- This is the conceptual ancestor of the lot-sizing logic inside MRP systems, even though many real MRP implementations substitute simpler heuristics for the full algorithm.

## Connects to

- [[eoq-model-and-lot-sizing]] — the constant-demand special case Wagner-Whitin generalizes; both solve the identical setup-vs-holding cost tradeoff.
- [[statistical-inventory-models-newsvendor-base-stock]] — Wagner-Whitin assumes demand is known in advance; the statistical models pick up where that assumption breaks down (uncertain demand).
- [[american-manufacturing-origins-and-system]] — MRP's rise as a computerized planning system (touched on in Chapter 1's "integration" trend) depends on lot-sizing logic like this running underneath it.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 2 | Useful conceptual grounding for MRP/ERP-configuration audits, but rarely a standalone deliverable for SMB clients |
| Current usefulness | 2 | Mostly background until an MRP/ERP-using client engagement arises |
| KSU support | 4 | Standard dynamic-programming/OR example, likely to appear in coursework |
| Tech-stack relevance | 1 | Not tied to the current tech stack directly |
| Business audit value | 3 | The "never top up an order" check is a quick, concrete real-world audit test |
| Data/workflow value | 2 | Requires a known multi-period demand schedule, which most SMB clients won't have readily formalized |
| Reading urgency | 3 | Mid-ingest of Chapter 2, actively in progress |

**Overall priority**: LATER

## Use / Retrieval Notes

**Best use**:
KSU support / MRP-configuration audit background — understanding what a client's MRP/ERP lot-sizing settings are actually trying to approximate

**Use when**:
A client uses an MRP/ERP system and you need to evaluate whether its lot-sizing rule (lot-for-lot, fixed order quantity, etc.) is a reasonable approximation, or when a client's known production/demand schedule varies enough period-to-period that EOQ's constant-rate assumption clearly doesn't fit.

**Do not use when**:
Demand is roughly constant (use [[eoq-model-and-lot-sizing]] instead) or genuinely uncertain rather than known in advance (use [[statistical-inventory-models-newsvendor-base-stock]] instead).

**Fast retrieval query**:
`subject/wagner-whitin` + `use-case/operations-research` — or search "dynamic lot sizing" / "Wagner-Whitin property"

## North Star Connection

- How this applies to the audit business: this is mainly useful as theoretical grounding for evaluating a client's existing MRP/ERP lot-sizing configuration, and as a one-line practical check (orders placed while stock remains from a prior order = a red flag) that requires no formal modeling to apply in the field.
- Track relevance: Systems / KSU — solid OR/dynamic-programming content, more academically central than immediately client-deliverable.
- Possible future Second Brain use: Not yet — no clear conversion path until an MRP/ERP-configuration audit is actually underway.
