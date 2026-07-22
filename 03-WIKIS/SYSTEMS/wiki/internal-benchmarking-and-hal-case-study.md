---
domain: systems
type: framework
tags: [subject/factory-physics, subject/internal-benchmarking, subject/throughput-wip-cycle-time]
timeline: now
status: wiki-only
source_role: [primary, example]
use_cases: [audit, data-workflow, systems-analysis]
---

# Internal Benchmarking, and the HAL Printed-Circuit-Board Case

**Summary**: Section 7.3.5's explicit step-by-step internal-benchmarking procedure — compute a line's bottleneck rate and raw process time, sanity-check the data with Little's Law, then compare actual throughput/WIP/cycle-time against the best-case, worst-case, and Practical Worst Case (PWC) curves — worked through a full real case (HAL, a printed-circuit-board manufacturer) where actual performance turns out to be dramatically worse than even the worst-case benchmark would predict for a line this slow.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 7 ("Basic Factory Dynamics"), section 7.3.5

**Last updated**: 2026-06-21

---

## The Internal Benchmarking Procedure

Having established the best-case, worst-case, and Practical Worst-Case (PWC) bounding curves (see [[littles-law-and-best-case-performance]], [[worst-case-performance-and-batch-moves]], [[practical-worst-case-and-bottleneck-investment-tradeoffs]]), the chapter states the actual diagnostic method directly: **compare actual performance to that of the best, worst, and practical worst cases. The PWC serves as the benchmark — performance worse than this indicates problems (opportunities), while performance better than this suggests the line is not vastly inefficient.**

This is **internal** benchmarking — distinct from external benchmarking against other companies' lines — because every comparison point (best case, worst case, PWC) is computed purely from the line's own measured bottleneck rate (rb) and raw process time (T0). No outside data is needed.

**The procedure, made concrete**:
1. Determine rb (bottleneck rate) and T0 (raw process time) from process-level data.
2. Compute the critical WIP, W0 = rb × T0.
3. Sanity-check the available throughput/WIP/cycle-time data against Little's Law (WIP = TH × CT) — if the three measured quantities are wildly inconsistent with each other, something is wrong with the data before any benchmarking conclusion can be trusted.
4. Compute THpwc at the line's actual WIP level, using THpwc = w/(W0 + w − 1) × rb.
5. Compare actual throughput to THpwc. If actual throughput is well below THpwc (or, equivalently, actual cycle time is well above CTpwc), the line is performing in "bad" territory — worse than even the maximum-randomness benchmark predicts — and is a strong candidate for the three improvement levers from the PWC page (unbalance the line, use parallel machines, reduce variability).

## The HAL Case: A Real Line Performing Worse Than the Worst Case

**HAL** manufactures printed-circuit boards (PCBs) sold to other plants for component assembly. The process: lamination (pressing copper/prepreg layers into blank cores), machining (trimming to size), circuitize (etching circuitry into the copper, via a photographic exposure/etch process — this is the step that gives boards their unique "personality" and the point at which they become "panels"), optical test/repair, drilling (connecting circuitry between layers on multilayer boards — note: multilayer panels must cycle back through lamination after circuitizing, while single-layer panels skip drilling and copper plating entirely), copper plate, procoat (protective coating), sizing (cutting panels into final individual boards — as few as 2 or as many as 20 per panel), and a final end-of-line electrical test.

**HAL's measured capacity data** (Table 7.4, averaged across all the different PCB types and routings the line handles, and net of "detractors" like machine failures, setup times, and operator inefficiency):

| Process | Rate (panels/hr) | Time (hrs) |
|---|---:|---:|
| Lamination | 191.5 | 4.7 |
| Machining | 186.2 | 0.5 |
| Internal circuitize | 114.0 | 3.6 |
| Optical test/repair — int. | 150.5 | 1.0 |
| Lamination — composites | 158.7 | 2.0 |
| External circuitize | 159.9 | 4.3 |
| Optical test/repair — ext. | 150.5 | 1.0 |
| Drilling | 185.9 | 10.2 |
| Copper plate | 136.4 | 1.0 |
| Procoat | 117.3 | 4.1 |
| Sizing | 126.5 | 1.1 |
| EOL test | 169.5 | 0.5 |
| **rb, T0 (line totals)** | **114.0** | **33.9** |

**Internal circuitize is the bottleneck** (lowest rate, 114 panels/hour), giving rb = 114 panels/hour and T0 = 33.9 hours (the sum of all process times — note the process *rate* of a step is not simply the inverse of its process *time*, because panels are processed in batches and many steps have parallel machines).

**Critical WIP**: W0 = rb × T0 = 114 × 33.9 = 3,869 panels.

**HAL's actual measured performance**: throughput averages ~1,400 panels/day, or 71.8 panels/hour (HAL runs three shifts/day, netting to 19.5 productive hours/day after breaks, shift changes, and meetings); WIP averages ~47,000 panels; cycle time averages ~34 days (816 hours); customer service (on-time delivery) averages 75%, against a corporate goal of 90%.

**Step 1 — the easy diagnostic**: customer service (75% vs. a 90% goal) is already clearly bad on its face — though the chapter flags an important caveat: this alone doesn't prove the *line* is the problem. Overzealous salespeople promising unrealistic due dates could also produce a low on-time rate even on a well-run line. Customer-service shortfalls need a second, independent check before blaming the production system.

**Step 2 — the Little's Law sanity check**: TH × CT = 1,400 panels/day × 34 days = 47,600 panels — very close to the actual measured WIP of 47,000. Since Little's Law applies precisely only to long-term averages, exact agreement isn't expected, but this level of agreement is well within the data's precision and indicates no obvious data-quality problem.

**Step 3 — comparing actual throughput to THpwc at the same WIP level**: THpwc = w/(W0 + w − 1) × rb = 47,000/(3,869 + 47,000 − 1) × 114 ≈ **105.3 panels/hour**.

**The verdict**: HAL's actual throughput (71.8 panels/hour) is dramatically below the PWC benchmark (105.3 panels/hour) — and the chapter is explicit that this means HAL is performing **worse than even the worst-case benchmark would suggest is reasonable for a line with this WIP level**. Plotting all three curves (best, worst, PWC) against the actual (WIP, TH) = (47,000, 71.8) point places it squarely in the "bad" region between the worst case and the practical worst case.

**The key limitation the chapter states outright**: this diagnostic tells you *that* a line is performing poorly, and gives a rigorous, data-backed basis for saying so — but it does **not** explain *why*, or *how to fix it*. Answering that requires "a deeper investigation of what causes some lines to be very efficient at converting WIP to throughput and others to be very inefficient" — explicitly the subject of [[littles-law-and-best-case-performance|the variability material]] developed further in Chapters 8 and 9.

## Key Takeaways

- Internal benchmarking is a five-step, fully self-contained diagnostic: measure rb and T0, compute W0, sanity-check with Little's Law, compute THpwc at the actual WIP level, then compare actual throughput/cycle time against the PWC.
- The HAL case shows the diagnostic can reveal a line performing far worse than even the maximum-randomness (PWC) benchmark predicts — HAL's actual throughput (71.8 panels/hour) was barely 68% of its PWC-predicted throughput (105.3 panels/hour) at the same WIP level.
- A poor customer-service number alone is not sufficient evidence the production line itself is the problem — sales-side overpromising can produce the same symptom. The internal-benchmarking procedure (computed independently from process data) is what actually isolates the production system as the cause.
- This diagnostic identifies *that* a line is underperforming, with rigor — but identifying *why* (and what to fix) requires the variability analysis that follows in subsequent chapters.

## Connects to

- [[practical-worst-case-and-bottleneck-investment-tradeoffs]] — this page is the explicit worked application of that page's PWC formula and its stated role as the dividing line between "good" and "bad" line performance.
- [[littles-law-and-best-case-performance]] — Little's Law supplies the necessary data-validation step (TH × CT ≈ WIP) before any benchmarking conclusion can be trusted.
- [[factory-dynamics-definitions-bottleneck-rate-and-critical-wip]] — the HAL case is a direct, real-world application of identifying the bottleneck by rate (not raw speed) and computing W0 = rb × T0.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | This is the exact diagnostic Chris would run on a real client's production data — a fully worked template for "is this line good or bad, and how do I prove it with the client's own numbers?" |
| Current usefulness | 5 | Directly computable from any client's process-rate/process-time data, with a built-in data-quality check (Little's Law) |
| KSU support | 4 | Reinforces queueing-theory benchmarking as applied analysis, not just formula derivation |
| Tech-stack relevance | 3 | A natural Python/spreadsheet calculator: input a process-rate table, output bottleneck, W0, THpwc, and a good/bad classification |
| Business audit value | 5 | The HAL case is a ready-made template for a client deliverable: "your line is running at X% of what maximum-randomness theory would predict at your current WIP level" |
| Data/workflow value | 5 | The five-step procedure (including the Little's Law sanity check) is directly reusable as a structured audit worksheet |
| Reading urgency | 4 | Completes the chapter's diagnostic toolkit — the explicit "how to actually use everything in 7.3" payoff |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit diagnostic — walking a client's own process-rate and process-time data through the five-step internal-benchmarking procedure to produce a rigorous, defensible "your line is performing better/worse than theory predicts" finding, backed by the client's own numbers.

**Use when**:
A client has (or can produce) basic process-rate/process-time data and you need an objective, theory-backed answer to "is this production line actually inefficient, or does it just feel that way?" — especially useful when a customer-service or on-time-delivery complaint needs to be separated from a true production-capacity problem.

**Do not use when**:
The client's process data is too noisy, too aggregated, or too inconsistent (failing the Little's Law sanity check) to trust — fix the data collection first, per [[littles-law-and-best-case-performance]]'s applications.

**Fast retrieval query**:
`subject/internal-benchmarking` + `use-case/audit` — or search "internal benchmarking procedure" / "HAL printed circuit board case" / "PWC worse than worst case"

## North Star Connection

- How this applies to the audit business: this is a literal, ready-to-run audit worksheet — collect a client's bottleneck rate and raw process time, sanity-check their WIP/throughput/cycle-time data with Little's Law, then compute and present a "your line vs. the maximum-randomness benchmark" finding, exactly as demonstrated on HAL's real PCB line.
- Track relevance: Business / Systems — directly deployable on any client engagement involving a measurable production flow.
- Possible future Second Brain use: Yes — strong candidate for a reusable "Internal Benchmarking Worksheet" template (Python script or spreadsheet) once a production-flow client engagement exists.
