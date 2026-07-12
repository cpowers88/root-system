---
domain: systems
type: case-study
tags: [priority/next, status/wiki-only, domain/systems, source-role/primary, use-case/audit, use-case/business-model, use-case/ksu-support, subject/mrp, subject/erp, subject/scientific-management, subject/manufacturing-history, subject/factory-physics]
---

# MRP/ERP's Empirical Failure Record, and Why BPR, Lean's VSM, and Six Sigma's DMAIC All Fall Short of a Real Systems Paradigm

**Summary**: The hard evidence behind Chapter 5's critique — decades of flat inventory-turns data and dismal adoption surveys showing MRP rarely delivered on its promises, the precise mechanical reason why (fixed lead times that ignore plant loading), the historical/technical reasons MRP was nonetheless a reasonable response to 1960s computing constraints, and a structured five-point critique of value stream mapping plus a parallel critique of Six Sigma's DMAIC — both shown to fall short of a true systems-analysis paradigm despite real value as starting tools.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 5 ("What Went Wrong?"), sections 5.3-5.5

**Last updated**: 2026-06-21

---

## Scientific Management's Real Flaw: It Was Never Actually Scientific

Frederick Taylor and his contemporaries placed great faith in science at a moment (the 1890s-1900s) when leading physicists genuinely believed physics was nearly complete — Albert Michelson (1894) wrote that "the more important fundamental laws and facts of physical science have all been discovered," and Lord Kelvin (1900) claimed "there is nothing new to be discovered in physics now." It was both plausible and fashionable to believe science could bring management the same triumph it had brought physics.

**The book's pointed irony**: scientific management had more in common with today's buzzword movements than with actual science. Real science requires three activities — observation of phenomena, conjecture of causes, and logical deduction of further effects — producing models that genuinely deepen understanding of the world. **Taylor made many measurements but did little true experimentation; he developed formulas but never unified them into a general theory; neither he nor his contemporaries ever asked the *descriptive* question of how manufacturing systems actually behave — they jumped straight to the *prescriptive* question of how to improve efficiency.** The entire stream of work that followed inherited this same frameless, prescriptive approach: Harris's 1913 EOQ paper (see [[eoq-model-and-lot-sizing]]) established a precise mathematical standard for lot-sizing, but rested on assumptions — a fixed known setup cost, constant deterministic demand, instantaneous (infinite-capacity) delivery, and a single product with no interactions — that make far more sense for *purchasing* environments than for actual *production* environments, where setups create mix, capacity, and variability effects EOQ simply ignores.

**An even more consequential cost than the unrealistic assumptions themselves**: by treating setups as a fixed, exogenous constraint to optimize *around*, EOQ and its successors blinded operations researchers and practitioners to the possibility of directly *reducing* setups — it took the Japanese, approaching from an entirely different ("environment as a control," see [[jit-origins-goals-and-environment-as-control]]) perspective, to recognize setup reduction's real strategic value. The same pattern repeated with Wagner-Whitin, base stock, and (Q,r) — each began with a genuinely real insight (see [[wagner-whitin-dynamic-lot-sizing]], [[statistical-inventory-models-newsvendor-base-stock]], [[qr-model-and-lead-time-variability]]), but the fascination with mathematical elegance and computational speed gradually crowded out the original insight, with researchers narrowing their focus to ever-smaller, more tractable subproblems under the banner of **operations research** for decades, rather than broadening and integrating the insights into a strategic framework.

By the late 1980s, intensifying Japanese and German competition forced a reckoning. Harvard's Hayes, Wheelwright, and Clark (1988) argued that even tactical decisions like lot size and department layout have a significant cumulative strategic impact, and that a well-integrated manufacturing system — being hard to acquire or copy — can become a genuine source of sustainable competitive advantage. MIT's Dertouzos, Lester, and Solow (1989) similarly argued that business schools' historical belief that "a good manager could manage anything" had wrongly marginalized production/operations management in business curricula. **But increased consensus that operations mattered strategically did not translate into agreement on what to teach or how** — the old pure-mathematical-models approach had been discredited, and the pure-case-study alternative, while offering some realistic insight, risks reinforcing the false impression that executive decisions can be made competently with little or no operational-detail knowledge.

## The Empirical Record on MRP: A Stunning Software Success, an Uncertain Operational One

**MRP's adoption growth is undeniable**: from a handful of systems in the early 1960s to 150 by 1971; APICS's "MRP Crusade" launched in 1972; claims of 8,000 US systems by 1981; $400 million in MRP software sold by 16 companies in 1984 alone; $1.2 billion (nearly a third of the entire US computer-services market) in 1989; ERP grew to a $10 billion industry by the late 1990s with SAP becoming the world's fourth-largest software company; ERP revenue exceeded $24 billion by 2005.

**But did it actually work?** The evidence is weak at best:

- **Macro level**: American manufacturing inventory turns stayed roughly flat through the 1970s-80s, during and after the MRP Crusade (Figure 5.1 in the source); turns *did* rise in the 1990s, but the book attributes this to JIT's downward pressure on inventory, not MRP.
- **Micro level — adoption surveys**: Booz, Allen, and Hamilton (1980) surveyed over 1,100 firms and found fewer than 10% recouped their MRP investment within two years (Fox 1980). A 1982 APICS-funded survey of 679 members — using Oliver Wight's own A/B/C/D effectiveness classification — found only 9.5% rated as fully effective Class A users, while 60% were Class C or D (marginal-to-modestly-effective). **The book stresses these respondents were APICS members and materials managers with every incentive to portray MRP favorably — making the pessimism especially telling.** A South Carolina survey of 33 MRP users found similar effectiveness numbers, plus an average total implementation cost of $795,000 (with a standard deviation of $1,191,000 — extreme variance even among "successful" implementations).
- **Critics' verdict**: MRP was called the "$100 billion mistake," with claims that 90% of users were unhappy and that MRP actually *perpetuated* the plant inefficiencies (high inventory) it was supposed to solve (Whiteside and Arbose 1984).

## Kanet's "Litany of Excuses" and the Real Diagnosis

John Kanet — a former Black & Decker materials manager who wrote glowingly about MRP in 1984 but turned sharply critical by 1988 — catalogued a decade-long sequence of excuses for MRP's repeated failure to deliver: inaccurate computer records (fixed — still failed) → unrealistic master schedules (fixed — still failed) → insufficient top-management involvement (fixed — still failed) → insufficient training (fixed, spawning "the golden age of MRP-based consulting" — still failed). **Each excuse blamed implementation, never the underlying model itself.**

**The book's actual diagnosis**: MRP is built on a flawed model, specifically its reliance on fixed lead times to back out release dates from due dates — lead times that depend only on part number, never on actual plant loading. Orlicky's own 1975 book stated this was *deliberate*: "An MRP system is capacity-insensitive, and properly so... there can be only one correct answer to that, and it cannot therefore vary depending on what capacity does or does not exist." **But unless capacity is truly infinite, the time for a part to actually move through the plant does depend on loading — the fixed-lead-time assumption is at best only an approximation.** This produces a destructive feedback loop: because releasing jobs too late wrecks downstream coordination, there's strong incentive to inflate MRP lead times as a buffer against contingencies (queueing behind other jobs, machine outages) — but inflated lead times let more work into the plant, increasing congestion and *actual* flow time, generating yet more pressure to inflate lead times further. **The book notes pointedly that the flaws Kanet identified more than 20 years before still persist in most MRP and ERP systems today.**

## Why MRP Was Nonetheless a Historically Reasonable Choice

The book is careful not to treat this as simple incompetence: MRP's original goal — explicitly distinguishing dependent from independent demand — was genuinely sound (see [[mrp-history-and-push-pull-paradigm]]), and the alternative (treating all demand as independent, using reorder-point methods at every BOM level) required tedious manual BOM explosion and netting that strongly incentivized computerization. **But the computer MRP met was the computer of the 1960s**: an IBM 360 using core memory (each bit a magnetic doughnut the size of a letter "o"), with even a 1979 mainframe rarely exceeding 1 million bytes of RAM. With memory this constrained, performing full MRP processing in RAM was impossible — the only viable design was **transaction-based**, bringing individual part records in from tape storage, processing, and writing back. MRP's logic is exquisitely well-suited to this transaction-based constraint — making MRP, in its own historical context, a genuinely sensible engineering response. **The problem is that MRP is now poorly suited to 21st-century computing environments and capabilities it was never designed to exploit.**

MRP II's capacity-checking modules (RCCP, CRP — see [[capacity-planning-and-shop-floor-control]]) were explicitly meant to patch this flaw, but were widely criticized through the 1980s even as Japanese firms succeeded with methods resembling the *old* reorder-point approach (kanban — see [[kanban-mechanics-and-pull-system-variants]]). **MRP nonetheless survived because MRP II handled important nonproduction data-maintenance and transaction-processing functions JIT never replaced** — persisting into the 1990s, expanding into other business functions, and getting rechristened ERP once the transaction-based memory constraint was no longer binding. Independent finite-capacity scheduler vendors emerged in the 1990s but struggled for adoption until bundled into comprehensive ERP suites — producing today's more monolithic systems, often requiring firms to restructure their *business* to fit the software (a legacy of BPR's "think in revolutionary terms" conditioning).

**Concrete documented ERP/SCM failures**: SAP, the world's largest ERP vendor, suffered two well-publicized 1999 implementation failures (Whirlpool, Hershey) that delayed appliance and candy shipments — leaving candy-store shelves empty before Halloween; multiple companies abandoned SAP installations costing $100-250 million; a Meta Group survey of 63 companies found an average ERP ROI of **negative $1.5 million**. The 1995 "Chaos Report" (Standish Group) found over 31% of all IT projects canceled before completion and 53% running 189% over original budget, with only 16% delivered on time and on budget; a 2001 Robbins-Gioia survey found 51% of companies considered their ERP implementation unsuccessful. The well-publicized 2001 Nike/i2 public finger-pointing, and Fed Chairman Alan Greenspan's February 2001 congressional testimony anticipating an inventory buildup *despite* supply-chain automation advances, both signal how widely felt the disappointment became — even at the level of national economic policy commentary.

**The book's bottom line on the entire MRP→ERP→SCM lineage**: the hierarchical planning structure central to MRP II (and inherited by ERP/SCM) does provide genuine coordination value and a logical data-sharing structure. But the evolution from MRP to ERP/SCM represents an impressive sequence of *information-technology* advances riding on top of an unchanged, never-fixed flawed material-flow model — and the ultimate payoff of the SCM movement depends far more on whatever modeling progress it eventually promotes than on any further IT sophistication.

## BPR, Value Stream Mapping, and DMAIC: Each a Useful Tool, None a Complete Systems Paradigm

**Business process re-engineering (BPR)**, at its core, was systems analysis applied to management — but emphasized *radical* change in the characteristically American "big and bold" style (Hammer and Champy 1993: "fundamental rethinking and radical redesign... to achieve dramatic improvements"). Because most BPR redesigns eliminated jobs, it became synonymous with downsizing and fell out of corporate vocabulary by the late 1990s as quickly as it arose. **Its lasting legacy was double-edged**: 1990s layoffs (in good times and bad) measurably raised labor productivity, but at the cost of undermining worker loyalty by hitting both labor and middle management at unprecedented scale — and BPR's normalization of "radical change" thinking is what the book credits with conditioning firms to accept the kind of business-process restructuring late-1990s ERP systems demanded.

**Lean's value stream mapping (VSM)**, a descendant of older "process flow mapping," visualizes a current-state process flow, compares value-added time against total cycle time (often revealing value-added time under 1% of total — genuinely useful low-hanging-fruit insight), then projects a future-state map. **The book identifies five specific reasons VSM falls short of a complete systems-analysis paradigm**:
1. There's no exact definition of "value-added," frequently wasting time in unproductive debate over what counts.
2. Value-added time is often so short it offers no reasonable target for cycle time.
3. VSM provides no means for diagnosing the *causes* of long cycle times.
4. Even though VSM collects capacity and demand data, it never computes *utilization* and so never discovers when a process faces demand beyond its capacity.
5. There's no feasibility check for the proposed "future state."
**This is not a wholesale dismissal — VSM is a genuinely good first step, and hundreds of companies have found real opportunities simply by carefully mapping their current process. But once the easy improvements are exhausted, VSM offers no path to further gains**, because that requires a model systematically connecting policies to performance — which nothing in the current lean movement provides.

**Six Sigma's DMAIC** (define-measure-analyze-improve-control) claims roots in the scientific method, but the book argues it emphasizes only the experimentation step while treating each production system as a "black box" with no retained underlying model — DMAIC practitioners are, in this regard, like scientists who discard their old data every time they make a new observation, building no cumulative theory and sharing almost nothing between companies. **A further structural problem**: DMAIC artificially separates "measure" from "analyze" as sequential steps, when in real practice measurement and analysis must proceed together, iteratively, since it's never possible to collect all necessary data upfront — each analysis step generates new questions requiring more data.

**A pointed real classroom anecdote**: the authors taught Factory Physics fundamentals to a group of Six Sigma black-belt candidates who had just completed two weeks of conventional Six Sigma training (including design of experiments and analysis of variance). After four days specifically studying the basic behavior of manufacturing systems (i.e., Part II's content), the group was assigned a cycle-time-reduction case study — and **every single member, despite the explicit Factory Physics instruction on root causes, defaulted to designing a statistical experiment to discover the cause of long cycle times**, rather than applying the theory they had just been taught. **The book's own conclusion**: strict devotion to DMAIC had blinded the group to seeing *why* cycle times were long — an ironic illustration that movements rooted in ultrarational systems analysis (BPR, Six Sigma) may have left manufacturing professionals just as vulnerable to irrational buzzword-following as anyone else.

## Key Takeaways

- Scientific management's actual flaw was that it was never genuinely scientific — Taylor measured extensively but never built a unifying theory or asked the descriptive "how do these systems behave" question, a pattern the entire stream of operations-research work that followed inherited.
- The hard MRP adoption-effectiveness data (sub-10% ROI recoupment, <10% Class A users in 1982, the "$100 billion mistake" critique) is concrete, citable evidence for any conversation skeptical of treating software adoption alone as proof of operational improvement.
- MRP's core flaw (fixed lead times ignoring actual plant loading) creates a specific, named, self-reinforcing failure loop: inflate lead times to buffer contingencies → more WIP enters the plant → more congestion → longer actual flow time → more pressure to inflate lead times further — and this flaw persists unchanged through MRP II, ERP, and SCM.
- MRP was a defensible engineering response to 1960s computing constraints (core memory, transaction-based processing) — useful historical context against treating its designers as simply wrong, even though the resulting model is now badly mismatched to 21st-century capability.
- VSM's five named limitations and DMAIC's "black box, no retained model" critique are both concrete, structured frameworks for evaluating any client's existing lean or Six Sigma program rather than accepting it at face value.

## Connects to

- [[what-went-wrong-three-trends-critique-and-case-for-science]] — this page's empirical evidence and case-by-case tool critiques (BPR/VSM/DMAIC) are the support for that page's higher-level diagnostic argument.
- [[eoq-model-and-lot-sizing]], [[wagner-whitin-dynamic-lot-sizing]], [[statistical-inventory-models-newsvendor-base-stock]], [[qr-model-and-lead-time-variability]] — the specific Chapter 2 models this page identifies as real insights subsequently narrowed by operations research's mathematical-elegance fascination.
- [[mrp-history-and-push-pull-paradigm]] — the original MRP insight (dependent vs. independent demand) this page reaffirms as genuinely sound even while critiquing the model built around it.
- [[capacity-planning-and-shop-floor-control]] — RCCP/CRP, the MRP II-era patches for the exact flaw diagnosed here, already covered in detail.
- [[erp-and-scm-history-and-tradeoffs]] — the full ERP/SCM history; this page adds the harder failure-rate evidence (Chaos Report, Meta Group ROI, SAP/Whirlpool) the earlier page didn't yet include.
- [[goodbye-jit-hello-lean]] — the VSM critique here pairs directly with that page's account of lean's rise; together they cover lean's strengths and its real limitations.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The MRP/ERP failure statistics and the VSM/DMAIC structured critiques are both immediately deployable in real client-advisory conversations |
| Current usefulness | 5 | Concrete, citable numbers (sub-10% ROI, negative $1.5M average ERP ROI, Chaos Report stats) for any software-adoption-skepticism conversation |
| KSU support | 5 | Canonical operations-management history with genuinely rich primary-source citations |
| Tech-stack relevance | 4 | Directly informs how to evaluate any `stack/industry-platforms` vendor claim skeptically |
| Business audit value | 5 | The five-point VSM critique is a ready-made checklist for auditing any client's existing lean program; the MRP failure-loop mechanism is a concrete diagnostic for "why does our system keep getting worse" |
| Data/workflow value | 3 | Mostly historical/conceptual, though the failure-loop mechanism has real diagnostic-workflow value |
| Reading urgency | 5 | Completes the chapter's evidentiary case, directly setting up Part II |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit diagnostic / client advisory — bringing hard evidence and structured critiques to bear when a client's lean program, Six Sigma initiative, or ERP/SCM system isn't delivering the results it was sold on

**Use when**:
A client cites an existing lean program, Six Sigma black belt, or recent ERP/SCM implementation as evidence their operations are already optimized, or needs a concrete diagnostic for why their "modern" software system still produces excess WIP, missed due dates, or poor service.

**Do not use when**:
A client's specific tool (VSM, DMAIC, an ERP module) genuinely fits their situation and is working — these are real critiques of *over-reliance*, not blanket condemnations of the tools themselves.

**Fast retrieval query**:
`subject/mrp` + `subject/scientific-management` — or search "Kanet litany of excuses" / "value stream mapping five limitations" / "DMAIC black box" / "Chaos Report ERP failure"

## North Star Connection

- How this applies to the audit business: the MRP/ERP failure statistics (sub-10% recoupment, negative average ROI, the Chaos Report) are powerful, source-backed ammunition for any conversation where a client over-trusts a software vendor's claims; the five-point VSM critique and the DMAIC black-box critique both give Chris structured, specific ways to evaluate (rather than simply praise or dismiss) a client's existing improvement program — exactly the kind of nuanced, evidence-grounded judgment that differentiates a real audit from generic consulting.
- Track relevance: Business / KSU — very strong; among the most citation-dense and audit-actionable pages in the ingest so far.
- Possible future Second Brain use: Yes — the VSM five-point critique and the MRP failure-loop mechanism are both strong candidates for audit checklists once Chris formalizes his methodology documents.
