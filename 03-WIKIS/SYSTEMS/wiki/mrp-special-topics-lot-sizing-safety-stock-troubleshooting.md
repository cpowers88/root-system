---
domain: systems
type: framework
tags: [priority/next, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/ksu-support, subject/mrp, subject/inventory-control, subject/factory-physics]
---

# MRP Special Topics: Lot-Sizing Rules, Troubleshooting, and the Honest Limits of Safety Stock/Lead Time

**Summary**: A deeper look at how real MRP systems handle the messy parts the basic algorithm glosses over — which lot-sizing rule to actually use (and why the "optimal" Wagner-Whitin algorithm is rarely implemented in commercial software), how planners patch a disrupted schedule (pegging, bottom-up replanning, firm planned orders), and why safety stock and safety lead time are honest workarounds, not real fixes, for MRP's deterministic assumptions.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 3 ("The MRP Crusade"), sections 3.1.5-3.1.7

**Last updated**: 2026-06-21

---

## Lot-Sizing Rules: Why Wagner-Whitin Isn't Actually Used

[[wagner-whitin-dynamic-lot-sizing]] solves the lot-sizing problem optimally under its stated assumptions (known setup cost, known holding cost, no capacity constraint). The book makes a pointed observation: **despite the Wagner-Whitin (WW) algorithm being held up as the benchmark every other lot-sizing rule gets measured against, the authors know of no commercial MRP package that actually implements it.** The two excuses usually given — too complicated, too slow — don't hold up against modern computing power; a more honest explanation offered is **"people would rather live with a problem they cannot solve than accept a solution they do not understand."** In practice, "setup cost" is also frequently used as a *proxy for limited capacity* rather than a real dollar figure anyone has measured — which undermines the entire premise the WW algorithm is built on.

Three simpler rules dominate in practice, all already introduced in [[mrp-mechanics-netting-lot-sizing-bom-explosion]]:

- **Lot-for-lot (LFL)** — minimizes inventory (no leftover carried between periods) but maximizes setup cost (a "setup" effectively occurs every period with demand). Simple, JIT-aligned, and produces the smoothest production schedule — the recommended default when setup costs/times are minimal.
- **Fixed order quantity (FOQ)**, often sized via EOQ using *average* demand in place of EOQ's constant-rate assumption — useful when physical handling constraints (totes, carts, transport fixtures) favor standardized lot sizes, and a natural fit for **powers-of-2 lot sizing** (see [[eoq-model-and-lot-sizing]]). Plain FOQ violates the Wagner-Whitin property (it can carry inventory into a period that doesn't avoid a setup), but restricting the fixed quantity to exact multiples of period demand recovers the property.
- **Fixed order period (FOP)**, a.k.a. period order quantity — combine P periods' worth of net demand into one lot; correctly skips periods with zero demand rather than blindly firing every P periods. An "optimal" P can be estimated the same EOQ-with-average-demand way as FOQ.
- **Part-period balancing (PPB)** — combines the WW-style trade-off framing with EOQ-style mechanics: define a **part-period** as one unit held for one period, then choose lot sizes so the total part-periods carried (inventory carrying cost) lands as close as possible to the setup cost, evaluated only across quantity choices that already preserve the Wagner-Whitin property. In the worked example, PPB and FOP arrived at the *same* final schedule — illustrating that several "different" heuristics often converge on similar real-world results.

**The literature's own verdict is genuinely mixed**: Bahl et al. (1987) found that plain fixed order quantity *without* the WW-property modification often outperforms WW-property-respecting rules in multilevel systems with real capacity limits — because the "wasted" leftover inventory those rules avoid actually functions as a form of safety stock, helping end items ship on time. **The theoretically tidy property (WW) is not automatically the practically superior rule once capacity constraints are real** — a recurring theme: elegant OR results assume away exactly the friction that matters most in practice.

## Troubleshooting: Pegging, Bottom-Up Replanning, and Firm Planned Orders

Real shop floors deviate from plans constantly (late jobs, scrap, demand changes), and MRP has accumulated three core tools for coping:

- **Pegging** links a given planned order release back to every source of demand that generated it, level by level, all the way to the master production schedule. This lets a planner trace *why* a particular order exists and who it ultimately serves.
- **Bottom-up replanning** uses pegging in reverse: when a scheduled receipt is discovered to be at risk (e.g., a purchase order was never actually sent — literally lost behind a file cabinet in the book's own example), pegging shows exactly which downstream end-item demands will go uncovered, letting the planner make a deliberate judgment call about which orders to prioritize (lowest-level items first to limit disruption spread? actual paying customers first over forecast-driven demand? split the available stock?) rather than discovering the failure only after a regeneration run.
- **Firm planned orders (FPOs)** convert a planned order release into something held fixed regardless of subsequent MRP reruns — treated as if it were already a scheduled receipt. This deliberately trades some optimization flexibility for **schedule stability**, which matters because workers and managers need a stable-enough plan to actually prepare (shift staffing, setups) rather than chasing a schedule that changes every run.

**Updating frequency (regeneration frequency)** is the structural tension underneath all of this: update too often and the shop drowns in exception reports and constantly shifting planned orders (excessive **MRP nervousness**); update too rarely and the plan goes stale relative to reality. Firm planned orders are one of the main levers for damping nervousness without simply slowing down the whole system.

## Safety Stock vs. Safety Lead Time — and Why Both "Lie" to the System

MRP's deterministic core assumes known demand, known production timing, and known yields. Reality has at least three sources of uncertainty it ignores: demand quantity/timing, production timing (breakdowns, quality problems, staffing), and production quantity (**yield loss/fallout** — fewer good parts finish than were started). Vollmann et al. (1992)'s widely-cited framing: **safety stock protects against quantity uncertainty; safety lead time protects against timing uncertainty.**

**Mechanically**: safety stock subtracts a fixed cushion from projected on-hand before netting (so the system "thinks" it needs to cover demand plus the cushion); safety lead time pulls planned order *receipts* in earlier by a fixed offset before the standard lead-time-based release calculation runs. The book's own framing is blunt: **both procedures work by deliberately lying to the MRP system** — safety stock means intentionally producing quantities with no actual customer behind them; safety lead time means telling the system a job is needed earlier than it really is. Useful, but not a free fix.

**A sharp illustration of why lead-time variability compounds badly across an assembly**: suppose 10 components must all arrive on time for an assembly to start, manufacturing lead times are normal with mean 3 weeks and std dev 1 week, and the target is 95% on-time assembly starts. If all 10 components must independently hit their due dates, the *per-component* service level s required is s^10 = 0.95, so s = 0.95^(1/10) ≈ 0.9949 — a single component needs to be on time roughly 99.5% of the time, which (under the normal approximation) requires a safety lead time of about 2.6 standard deviations above the mean, or roughly 5.6 weeks — **nearly double the nominal 3-week lead time**, just to protect a 10-component assembly at a 95% level. **This is the same multiplicative-variability lesson as the (Q,r) lead-time-variance result** (see [[qr-model-and-lead-time-variability]]), expressed differently: combining many independently-variable inputs into a single downstream event demands disproportionately high individual reliability.

## Key Takeaways

- The "optimal" Wagner-Whitin lot-sizing rule is essentially never implemented in commercial MRP software — simpler heuristics (lot-for-lot, FOQ, FOP, part-period balancing) dominate in practice, and the evidence on whether WW-property-preserving rules even perform better under real capacity constraints is genuinely mixed.
- Pegging + bottom-up replanning give a planner the ability to see exactly which downstream demands a supply disruption will affect, and to make a deliberate prioritization call, rather than discovering the damage only after the fact.
- Firm planned orders trade some scheduling optimality for stability — a direct, practical tool against "MRP nervousness" from over-frequent replanning.
- Safety stock and safety lead time are honest workarounds (the book calls them "lies" to the system) for MRP's deterministic core — useful, but they don't actually resolve the underlying uncertainty, just buffer against it at a cost.
- Multi-component assemblies need dramatically higher per-component reliability than the assembly's own target service level — a 95% on-time assembly with 10 independent components needs ~99.5% per-component reliability, which can require a safety lead time nearly double the nominal lead time.

## Connects to

- [[mrp-mechanics-netting-lot-sizing-bom-explosion]] — the basic four-step algorithm this page adds operational nuance to.
- [[wagner-whitin-dynamic-lot-sizing]] and [[eoq-model-and-lot-sizing]] — the formal lot-sizing theory that real MRP lot-sizing rules approximate, deviate from, or (per Bahl et al.) sometimes deliberately ignore.
- [[qr-model-and-lead-time-variability]] — the same "variability compounds" lesson, here shown across multiple components feeding one assembly rather than across one item's own lead time.
- [[mrp-history-and-push-pull-paradigm]] — the deterministic-demand assumption this page repeatedly works around traces directly back to MRP's foundational independent/dependent demand framing.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | The multi-component reliability math and the "safety stock/lead time lie to the system" framing are both directly usable in diagnosing a client's late-delivery or schedule-instability problems |
| Current usefulness | 3 | Most relevant once a client's ERP/MRP scheduling behavior is under active diagnosis |
| KSU support | 5 | Canonical, detailed production-control-systems content |
| Tech-stack relevance | 2 | Conceptual more than a direct coding/data task |
| Business audit value | 4 | The independent-component-reliability calculation is a sharp, quantifiable explanation for "why do my assemblies keep starting late even though each supplier is usually on time" |
| Data/workflow value | 3 | The lot-sizing rule comparison is directly applicable to evaluating/configuring a client's actual MRP/ERP settings |
| Reading urgency | 3 | Mid-ingest of Chapter 3, actively in progress |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Audit diagnostic / KSU support — explaining schedule instability ("MRP nervousness"), diagnosing why multi-component assemblies start late even when individual suppliers seem reliable, and evaluating whether a client's lot-sizing rule fits their actual situation

**Use when**:
A client's MRP/ERP system seems to be generating constantly-shifting schedules, or assemblies/projects with many converging inputs (subcontractors, material deliveries) are chronically late despite each individual input usually being on time.

**Do not use when**:
The client has no multi-level assembly structure or doesn't use a formal MRP/ERP system at all — the underlying probability math is still valid conceptually (any process with many independent "must all succeed" inputs faces this), but the MRP-specific mechanics (pegging, firm planned orders) won't directly apply.

**Fast retrieval query**:
`subject/mrp` + `use-case/systems-analysis` — or search "MRP nervousness" / "part-period balancing" / "safety lead time" / "bottom-up replanning"

## North Star Connection

- How this applies to the audit business: the multi-component independent-reliability calculation (0.95^(1/10) ≈ 99.5% per-component) is a genuinely powerful, transferable diagnostic — it explains, with real numbers, why any project or assembly with many converging inputs (subcontractor trades on a job site, multiple material deliveries before a pour, etc.) is structurally prone to lateness even when each individual input is "usually" on time. This generalizes well beyond MRP/manufacturing to general project coordination problems Chris will see in construction and field-service clients.
- Track relevance: Systems / Business / KSU — strong across all three, with a notably portable diagnostic insight.
- Possible future Second Brain use: Yes — the multi-component reliability framing is a strong candidate for a client-facing "why does my project keep slipping" explanation tool/one-pager.
