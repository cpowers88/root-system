---
domain: systems
type: concept
tags: [subject/mrp, subject/erp, subject/manufacturing-history, subject/factory-physics]
timeline: next
status: wiki-only
source_role: primary
use_cases: [audit, business-model, ksu-support]
---

# From MRP II to ERP and Supply Chain Management: History, Tradeoffs, and the Unresolved Core Problem

**Summary**: How MRP's successors (MRP II, then ERP, then SCM) grew from a narrow production-scheduling tool into company-wide and then cross-company integration platforms — driven by three coincident trends (supply chain management's rise, business process reengineering, and distributed computing) — while the chapter's closing argument insists none of this resolved MRP's foundational infinite-capacity, fixed-lead-time assumptions.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 3 ("The MRP Crusade"), sections 3.3-3.4

**Last updated**: 2026-06-21

---

## MRP II: A Hierarchy, Not Just a Bigger MRP

Manufacturing resources planning (MRP II) wasn't simply "MRP plus capacity checks" — it organized production planning into an explicit **three-level time-scale hierarchy**, a structural insight the book treats as MRP II's real contribution:

- **Long-range planning** (6 months–5 years, replanned a few times a year, part-family level of detail): resource planning (capacity expansion decisions like new plants) and aggregate planning (production/staffing/inventory/overtime levels, often optimized via linear programming), fed by long-range forecasting.
- **Intermediate planning** (the bulk of production planning functions): demand management (tracking actual orders against forecast via **available-to-promise (ATP)** — letting sales know which forecasted capacity is still open to commit to new orders), master production scheduling, rough-cut capacity planning, MRP itself, and capacity requirements planning.
- **Short-term control**: job release, job dispatching, and input/output control — the floor-level execution layer covered in [[capacity-planning-and-shop-floor-control]].

**Without this hierarchy, the book argues, coordinating thousands of orders for hundreds of tools across thousands of end items and components would be essentially intractable** — the hierarchy's real function is making an otherwise impossibly large coordination problem tractable by handling different levels of detail at different time scales.

## ERP and SCM: From Manufacturing Tool to Enterprise Platform

MRP III and "business requirements planning" (BRP) — two would-be successors to MRP II — never caught on. **Enterprise resources planning (ERP)** did, largely on the strength of vendors like SAP who extended the scope from manufacturing alone to *the entire enterprise* (accounting, finance, personnel, distribution). SAP's R/3 was marketed (per a 1997 BusinessWeek profile) as letting managers "act as a powerful network that can speed decision-making, slash costs, and give managers control over global empires at the click of a mouse" — trade-press hype, the book notes, but with "a kernel of truth": ERP genuinely did make it dramatically easier for upper management to get a near-real-time global picture of operations.

**Documented tradeoffs of the integrated-ERP approach**:

| Advantages | Disadvantages |
|---|---|
| Integrated functionality | Incompatibility with existing systems |
| Consistent user interfaces | Long, expensive implementation |
| Integrated database | Incompatibility with existing management practices |
| Single vendor and contract | Loss of flexibility to use specialized point solutions |
| Unified architecture/tool set | Long product development/implementation cycles |
| Unified product support | Long payback period; lack of technological innovation |

**A concrete cost data point**: in a survey of Fortune 1000 firms that had implemented ERP, **44% reported spending at least 4x as much on implementation help (consultants) as on the software itself** — and the book notes firsthand knowledge of companies that canceled multi-million-dollar ERP projects rather than "throw good money after bad."

## Three Coincident Trends That Drove ERP's Adoption

1. **Supply chain management (SCM)** — extending traditional inventory control to span distribution, warehousing, and multiple production locations, recognized as its own field (the Council of Logistics Management grew from 6,256 members in 1990 to almost 14,000 by 1997). Eventually the *term* SCM displaced "ERP" in industry usage, coinciding with the rise of the web and e-commerce, even though the underlying logic stayed largely MRP-rooted.
2. **Business process reengineering (BPR)** (Hammer and Champy 1993) — taught managers to accept radically restructuring their own management practices to fit a software package, a willingness that hadn't existed in most companies before the 1990s. BPR itself later "died a buzzword death," but its legacy — the expectation that ERP implementation is also an opportunity to re-engineer operations — persisted.
3. **Distributed computing** — an MRP run that took an entire weekend on a million-dollar 1960s computer can now run on a laptop in seconds; modern ERP architecture assumes data is stored locally where it's used and shared across an intracompany network rather than centralized.

**Market data showing the hype/reality gap**: MRP II sales hit $1.2 billion in 1989 (nearly a third of all US software sales that year). ERP sales for the top 10 vendors grew from $2.8B (1995) to $5.8B (1997); SAP alone reported >4.3 billion euros in 2001. Sales *dropped* once Y2K fears passed (-9% worldwide in 2002 per Gartner; SAP -5% in 2003) before recovering to ~14% growth by 2004 (AMR Research) — a pattern consistent with a real chunk of the late-1990s ERP boom being **defensive Y2K-bug spending rather than organic demand.** SCM software took even longer to gain traction, shrinking in 2002-2003 before growing 4% in 2004 to ~$5.5B, dominated by SAP, Oracle, and i2.

**Advanced planning systems (APS / APO)** emerged as add-on optimization layers (finite capacity scheduling, forecasting, ATP, warehouse/distribution management) sitting on top of the core ERP/SCM data integration layer — the book notes this add-on pattern "frequently resembled the earlier MRP II approach to 'fixing' the MRP problem of infinite [...] scheduling... after it has been generated" — i.e., the industry kept bolting capacity-feasibility fixes onto a core engine that was never designed to model capacity in the first place.

## The Chapter's Closing Argument

MRP, MRP II, ERP, and SCM represent real, substantial contributions to manufacturing-management practice — MRP itself, the book reiterates, was the first major application of modern computing to production control, and remains genuinely well-suited to coordinating purchasing against a master schedule and bill of materials. **But the chapter's explicit closing claim is that none of these successive generations actually resolved MRP's foundational flaw**: the assumption of infinite capacity and fixed lead times persists "even in some of the most sophisticated ERP/SCM systems" on the market today. Resolving that — while keeping MRP's prized simplicity and broad applicability — is named as a genuinely open, long-term problem the book defers to its later critique (Chapter 5) and its development of factory-behavior fundamentals (Part II), informed first by the JIT/lean insights covered next in Chapter 4.

## Key Takeaways

- MRP II's real innovation was the long-range/intermediate/short-term planning hierarchy, which made an otherwise intractable coordination problem (thousands of orders, hundreds of tools, thousands of end items/components) tractable — not just additional capacity-checking features.
- ERP's success was driven by three coincident trends (SCM's rise, BPR's cultural permission to restructure around software, and distributed computing) more than by any single technical breakthrough in the core MRP logic.
- The 44%-spend-4x-on-consultants statistic and the documented advantage/disadvantage table are concrete, citable numbers for any conversation about real ERP implementation cost and risk.
- A meaningful share of the late-1990s ERP sales boom was defensive Y2K spending, not organic demand growth — a useful historical caution against reading any software-adoption wave as pure value-driven demand.
- The chapter's central, unresolved claim: every MRP successor — MRP II, ERP, SCM, and even APS add-ons — still runs on the same infinite-capacity, fixed-lead-time core MRP logic from the 1960s. This is presented as a genuinely open problem, not a solved one.

## Connects to

- [[mrp-history-and-push-pull-paradigm]] — the independent/dependent-demand insight and push-system framing that MRP II, ERP, and SCM all inherit unchanged.
- [[capacity-planning-and-shop-floor-control]] — RCCP, CRP, and I/O control are the specific MRP II-era tools built (imperfectly) to patch the infinite-capacity assumption this page's closing argument says was never actually fixed.
- [[mrp-problems-nervousness-and-yield-losses]] — the capacity-infeasibility problem this page traces through MRP's entire software lineage.
- [[manufacturing-peak-decline-resurgence]] — MRP/ERP/SCM is explicitly named there as the "integration" trend running alongside lean's "efficiency" trend and Six Sigma's "quality" trend.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Directly useful when advising any client on ERP adoption, cost expectations, or evaluating an existing ERP implementation's real capabilities vs. marketing claims |
| Current usefulness | 3 | Useful background for any client conversation involving ERP/SCM software decisions |
| KSU support | 4 | Solid, citable software-industry and production-control history |
| Tech-stack relevance | 4 | Directly informs the `stack/industry-platforms` research category — ERP/SCM vendor evaluation |
| Business audit value | 4 | The advantage/disadvantage table and the 44%-consultant-spend statistic are concrete, client-ready talking points for any ERP-adoption conversation |
| Data/workflow value | 2 | Historical/conceptual rather than a data-handling technique |
| Reading urgency | 3 | Completes Chapter 3 |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Audit diagnostic / client advisory — setting realistic expectations for an ERP/SCM adoption or evaluation, grounded in the documented cost/risk tradeoffs rather than vendor marketing

**Use when**:
A client is considering adopting, replacing, or upgrading an ERP/SCM system, or needs help separating genuine capability from marketing claims about "real-time global control."

**Do not use when**:
The client's scale doesn't warrant ERP-level integration (most small SMB clients won't) — the advantage/disadvantage table is calibrated for larger, multi-function organizations.

**Fast retrieval query**:
`subject/erp` + `use-case/business-model` — or search "MRP II hierarchy" / "available to promise" / "business process reengineering" / "Y2K ERP sales"

## North Star Connection

- How this applies to the audit business: the documented ERP cost/risk tradeoffs (especially the 44%-spend-4x-on-consultants figure) are directly useful talking points for advising a client weighing an ERP investment, and the chapter's central claim — that no ERP/SCM system has actually fixed MRP's core capacity-modeling flaw — is a sharp corrective against assuming a bigger, more expensive software platform automatically solves a scheduling or capacity problem.
- Track relevance: Business / Systems / KSU — strong across all three; directly informs `stack/industry-platforms` research.
- Possible future Second Brain use: Yes — the advantage/disadvantage table and cost statistics are strong candidates for an ERP-adoption-advisory checklist once that kind of client engagement happens.
