---
domain: technology
type: concept
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, use-case/business-model, use-case/audit, subject/data-science, subject/data-driven-decision-making, stack/ai-frameworks-apis]
---

# Data-Driven Decision-Making: What It Actually Buys You, and Why "Big Data" Isn't "Data Science"

**Summary**: A precise vocabulary for separating data science (the principles), data mining (the techniques that embody those principles), data engineering/"big data" technology (the infrastructure that supports both but isn't either), and data-driven decision-making (the actual business goal all of this serves) — plus real, peer-reviewed economic evidence that this distinction matters: data-driven firms and big-data-technology adopters are measurably more productive, not just trendier.

**Sources**: DataScienceforBusiness.pdf (Provost & Fawcett, *Data Science for Business*, O'Reilly, 2013), Chapter 1 ("Introduction: Data-Analytic Thinking")

**Last updated**: 2026-06-22

---

## The Vocabulary, Precisely Defined

**Data science**: a set of fundamental *principles* that guide the extraction of knowledge from data. **Data mining**: the *extraction* of knowledge from data, via technologies that embody those principles — i.e., data mining is data science's applied/technical layer, not a separate discipline. **Data-driven decision-making (DDD)**: the practice of basing decisions on data analysis rather than purely on intuition — explicitly **not an all-or-nothing practice**; firms exist along a spectrum, and most real decisions blend analysis with experience and judgment. **The diagram worth keeping in mind**: data science *supports* DDD and *overlaps* with it (since, increasingly, decisions are made automatically by the data-mining system itself, not just informed by its output) — but data engineering and "big data" technology (Hadoop, HBase, MongoDB-era tools) sit one layer further out, supporting data science without *being* data science, in the same way a chemistry lab's glassware supports chemistry without being chemistry itself.

**Why this distinction is worth defending, not just pedantic**: job postings and vendor pitches routinely blur "data science" with "the tools used to do data science at scale" — but a model that genuinely extracts useful, actionable knowledge from data is the actual asset; the storage/processing technology underneath it is necessary infrastructure, replaceable on a much shorter cycle. **The book's own explicit prediction, worth testing against what's happened since 2013**: "in 10 years' time the predominant technologies will likely have changed or advanced enough that a discussion here would be obsolete, while the general principles are the same as they were 20 years ago" — a direct claim that the *principles* (not the specific tool stack) are the durable, transferable asset worth actually learning.

## Two Distinct Types of Decision DDD Actually Improves

**Type 1 — discovery decisions**: situations where you need to find a pattern you didn't already know to look for. Walmart's pre-Hurricane-Frances data mining (discovering strawberry Pop-Tarts sell ~7x normal rate ahead of a hurricane, alongside the expected flashlights and water) and Target's pregnancy-prediction model (inferring pregnancy from shifts in diet, wardrobe, and vitamin purchases, ahead of competitors who waited for public birth records) are both this type — the value is in surfacing something genuinely non-obvious, not confirming an existing hypothesis. **Type 2 — repeated-at-scale decisions**: situations where even a small accuracy improvement, applied across millions of repetitions, compounds into large aggregate value. The book's running churn example is this type — MegaTelCo doesn't need a brilliant one-off insight; it needs a marginally better way to rank which of its **millions** of contract-expiring customers should get a retention offer, since that small edge gets multiplied by the sheer volume of decisions. **This Type 1 / Type 2 distinction is directly useful for scoping any audit engagement involving data**: a client asking "what's actually going on in our data" wants Type 1 work; a client asking "how do we make this routine decision slightly better, at the volume we make it" wants Type 2 — and the right analytical approach, timeline, and success metric differ substantially between the two.

## The Real Evidence: DDD and Big Data Adoption Both Measurably Pay Off

**Two separate, peer-reviewed studies are cited as direct evidence, not just plausible-sounding claims — worth keeping as citable numbers for any client conversation about whether analytics investment is worth it**: Brynjolfsson, Hitt, and Kim (2011, MIT/Wharton) built a DDD-intensity scale across firms and found that **one standard deviation higher on that scale corresponds to a 4-6% increase in productivity**, controlling for a wide range of confounding factors — plus correlated increases in return on assets, return on equity, and market value, with evidence the relationship is genuinely causal, not just correlated with some other underlying firm quality. Separately, Tambe (2012, NYU Stern) found that, after controlling for confounders, **one standard deviation higher big-data-technology utilization correlates with 1-3% higher productivity** than the average firm (and one SD lower correlates with 1-3% lower) — a real, if smaller, additional effect specifically from the technology layer, distinct from the DDD-practice effect.

## Big Data 1.0 → Big Data 2.0: A Useful Historical Analogy for Where a Client Actually Sits

**The book's own framing, directly borrowed from the Web 1.0/2.0 transition and worth using verbatim with any client assessing their own analytics maturity**: "Big Data 1.0" is the phase where a firm is mainly occupied with *building the capability* to process large volumes of data, generally in support of operations already happening (efficiency gains on existing processes). "Big Data 2.0" is the subsequent phase, reached only once the 1.0 capability is thoroughly in place, where the real question becomes **"what can I now do that I couldn't do before, or do better than before"** — genuinely new capabilities, not just faster versions of old ones. **The explicit warning that this transition isn't automatic or guaranteed**: most firms were still squarely in the 1.0 phase as of this book's writing (2013), with only a handful of precocious companies (Amazon's early embrace of customer ratings/reviews/recommendations; real-time-bidding online advertisers processing billions of daily ad impressions in tens of milliseconds) already operating in the 2.0 mode. **A directly useful audit-scoping question this generates**: is this client still building basic data-processing capability (1.0), or do they already have that capability and are failing to ask the harder "what new thing could this let us do" question (2.0)? The right intervention is completely different depending on which phase a client is actually in.

## Connects to

- [[data-asset-strategy-signet-bank-capital-one-case]] — the companion page covering the chapter's strategic-asset framing and the Signet Bank/Capital One case study.
- [[owner-dependency-diagnostic|the Gap Method & Comfort Zone diagnostic]] — the Big Data 1.0/2.0 distinction is structurally similar to Gerber's current-state/target-state gap framework, applied specifically to a firm's data-analytics maturity rather than its overall business operations.
- business-development-process-overview — the "what can I now do that I couldn't do before" question at the 2.0 transition is the same innovation-orientation question central to the Innovation/Quantification/Orchestration engine already in the wiki.

## North Star Connection

- How this applies to the audit business: the Type 1/Type 2 decision distinction is a fast, useful scoping question for any client analytics conversation — clarifying upfront whether the engagement is "find something we don't know" (Type 1, open-ended, exploratory) or "make this routine decision slightly better at scale" (Type 2, narrower, ROI-quantifiable) prevents scope confusion later. The Big Data 1.0/2.0 framing gives Chris a quick maturity-assessment lens for any SMB client's data/analytics situation, almost all of which will be squarely in 1.0 (or pre-1.0) — meaning the audit opportunity is usually building basic capability, not chasing 2.0-style innovation prematurely.
- Track relevance: Tech / Business — directly useful vocabulary and scoping framework for the data-workflow and automation use cases central to the audit business model.
- Possible future Second Brain use: a "Type 1 vs. Type 2" client-scoping question and a "1.0 or 2.0" data-maturity quick-assessment are both strong candidates for a standalone audit discovery-phase checklist.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Directly useful scoping vocabulary for any client engagement involving data analytics |
| Current usefulness | 4 | The Type 1/Type 2 and 1.0/2.0 framings are immediately usable in any client discovery conversation |
| KSU support | 3 | Conceptual/strategic content rather than quantitative ISYE material, but foundational for the technology track |
| Tech-stack relevance | 4 | Directly maps to the `stack/ai-frameworks-apis` category and frames how to think about any future data/automation tooling decision |
| Business audit value | 5 | The 4-6% productivity number (Brynjolfsson) is a directly citable, credible business case for recommending DDD investment to a skeptical client |
| Data/workflow value | 4 | Core conceptual foundation for any data-workflow-focused audit work |
| Reading urgency | 4 | Foundational opening chapter for the entire data science track |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Client-scoping and business-case tool — use the Type 1/Type 2 decision distinction to clarify the actual goal of any analytics engagement upfront, and cite the Brynjolfsson (4-6% productivity) and Tambe (1-3% productivity) findings as credible, peer-reviewed evidence when building a business case for a client skeptical of analytics investment.

**Use when**:
Scoping a new data/analytics engagement with a client, or building a business case for why a client should invest in basic data-driven decision-making capability.

**Do not use when**:
The client's need is purely operational/transactional data processing with no decision-improvement goal — that's the data-engineering layer this chapter explicitly distinguishes from data science itself.

**Fast retrieval query**:
`subject/data-driven-decision-making` — or search "Type 1 Type 2 decisions data science" / "Brynjolfsson DDD productivity 4 to 6 percent" / "Big Data 1.0 2.0" / "data science vs data mining vs big data technology"
