---
domain: systems
type: source-summary
tags: [priority/next, status/wiki-only, domain/systems, source-role/primary, use-case/audit, use-case/business-model, use-case/ksu-support, subject/lean-manufacturing, subject/six-sigma, subject/quality-management, subject/manufacturing-history, subject/factory-physics]
---

# Goodbye JIT, Hello Lean: How JIT Got Rebranded, Six Sigma Replaced TQM, and Chapter 4's Closing Lessons

**Summary**: How JIT was effectively renamed and repackaged as "lean manufacturing" (1990) once ERP's "repetitive manufacturing" modules revealed they captured JIT's software mechanics but missed its philosophy entirely, how TQM lost momentum and was likewise rebranded as Six Sigma (Motorola → GE), and the chapter's own explicit closing list of the durable insights JIT/lean and TQM/Six Sigma actually contributed to manufacturing management.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 4 ("From the JIT Revolution to Lean Manufacturing"), sections 4.7-4.8

**Last updated**: 2026-06-21

---

## "Goodbye JIT, Hello Lean": A Rebranding, Not a New Idea

ERP vendors built modules with names like "repetitive manufacturing" that could level-load the MPS and implement pull — at least on the surface, ERP seemed to absorb JIT. **But the book is explicit that this revealed a real gap in understanding**: the repetitive manufacturing module provided *software* for production smoothing and kanban, but the *philosophy* of continual improvement, plus JIT's essential non-software elements (visual controls, mistake-proofing/poka-yoke, one-piece flow), were missing entirely.

In 1990, after a five-year MIT study of the auto industry, *The Machine That Changed the World* (Womack, Jones, Roos) introduced a new label for JIT: **lean manufacturing**. A 1996 follow-up, *Lean Thinking* (Womack and Jones), formalized the lean "philosophy" — and, in the book's judgment, **lean actually provided a neater conceptual package than the various scattered collections of JIT techniques had**, centered on *flow*, the *value stream*, and eliminating *muda* (waste) through *kaizen* events (see [[lean-methodology|lean thinking — the five principles]] and [[lean-methodology#The Seven Wastes (plus an eighth)|the seven wastes (muda)]], already in the wiki from a direct Lean Thinking ingest).

**A practical reason lean spread faster than JIT ever had**: lean required no computer and no software development, so there was almost no barrier to entry for would-be lean consultants — and the trade press filled with stories of slashed inventories, shortened lead times, and fattened bottom lines, all without a single line of code. **The book's frank verdict**: lean has been more successful than JIT in achieving results, even though it is, in substance, the same set of ideas — "JIT never really went away; it was simply renamed and repackaged and worked better the second time around." A real cost of the rebranding, though, was that much of the original clarity Ohno and Shingo brought to JIT's philosophy and mechanics was lost in the process — leaving "great confusion" about why pull and level scheduling actually matter.

## Six Sigma and Beyond: TQM's Parallel Rebranding

TQM, like JIT, never fully disappeared, but its momentum outlasted JIT's only by a delay — by the mid-1990s, TQM too was losing its shine, for two compounding reasons: once JIT's popularity faded, the high-quality requirements that JIT itself created became less visible/urgent (see [[jit-implementation-tactics-and-quality-revolution]] for why low WIP forces quality), and many managers grew weary of ISO 9000's documentation burden relative to its visible payoff.

Into that vacuum rose **Six Sigma**, developed at Motorola in 1985-87 under CEO Bob Galvin's mandate that product and service quality improve by a factor of 10 every two years — an aggressive target that produced the **measure-analyze-improve-control (MAIC)** methodology for reducing process variation, aiming for a defect rate orders of magnitude better than the prevailing standard (technically ≤3.4 defects per million opportunities, corresponding to roughly 4.5-6 sigma control limits). Motorola became one of the first Malcolm Baldridge National Quality Award recipients in 1988 on the strength of this approach.

**Six Sigma might have stayed a Motorola-specific program had it not been adopted and pushed further by other firms' charismatic leadership** — ABB, Allied Signal, and especially Jack Welch's GE, which in 1995 launched a company-wide initiative to move GE from "a great business" to "the greatest company in the world," making Six Sigma training a literal promotion requirement. GE's own annual reports estimate $1-2 billion/year in savings from 1996-99, and GE's stock value quadrupled in the years following 1995. By the turn of the millennium, MAIC had matured into **DMAIC** (adding a "define" phase), while a parallel variant, **design for Six Sigma (DFSS)**, applies a different methodology (**DMADV**: define-measure-analyze-design-verify) to designing *new* products and processes rather than improving existing ones. Industries far beyond manufacturing — health care, financial services, software development, home improvement — eventually adopted Six Sigma as a basis for process improvement.

**The book's framing of Six Sigma's place in the lineage**: some practitioners consider it a complete management system in its own right, successful precisely because of its bottom-line orientation; others see it more accurately as an evolutionary extension of TQM and JIT, and a worthy successor to the earlier quality work of Deming, Juran, Crosby, and even Shewhart (see [[manufacturing-peak-decline-resurgence]] for this same quality lineage from the trend-cycle perspective).

## Chapter 4's Closing Lessons (Stated Directly by the Book)

The book explicitly states that JIT/lean is not a coherent, well-defined management strategy — it is an assortment of attitudes, philosophies, priorities, and methodologies collectively labeled JIT and now lean, whose only real common thread is that they all trace back to Toyota and a handful of other Japanese companies. Even so, the book draws out six specific, durable insights that it argues deserve a permanent place in manufacturing-management history:

1. **The production environment itself is a control.** Strategies that reduce setups, redesign products with manufacturing in mind, or level production schedules can have more impact on process effectiveness than any decision made on the factory floor itself (see [[jit-origins-goals-and-environment-as-control]]).
2. **Operational details matter strategically.** Echoing Carnegie's century-old insight, attention to the smallest, most mundane details of the production process can confer real competitive advantage.
3. **Controlling WIP is important.** The smooth, rapid flow of materials — recognized by Ford in the 1910s and re-emphasized by Ohno in the 1980s — underlies virtually every JIT benefit: some are a direct consequence of low WIP (short cycle times), others are spurred by the pressure low WIP creates (high quality, per [[jit-implementation-tactics-and-quality-revolution]]).
4. **Flexibility is an asset.** JIT in its essential form is inherently inflexible (steady rate and mix, virtually minute by minute) — but JIT's own advocates, reacting against that inflexibility, developed a host of practices that promote flexibility instead: short setup times, capacity cushions, worker cross-training, cellular layout, and more (see [[jit-implementation-tactics-and-quality-revolution]]).
5. **Quality can come first.** Many of the basic quality concepts Japanese firms used had long been championed by American quality experts — but Japanese firms were far more effective at actually putting them into practice, proving that a system prioritizing quality over throughput, assured at the source, can be both reliable and profitable.
6. **Continual improvement is a condition for survival.** In sharp contrast to Henry Ford's belief in a perfectible product/process, the Japanese treated manufacturing as a continually changing game — standards that sufficed yesterday won't suffice tomorrow. It took roughly 25 years (1940s to late 1960s) of constant attention for Toyota to cut setups from 3 hours to 3 minutes; the lesson is sustained incremental devotion, not a single breakthrough.

The book draws three further insights specifically from the TQM/Six Sigma side:

1. **Quality and logistics must be improved together** — a system can't be lean with poor internal quality (parts must be made right the first time), and it can't consistently produce quality output unless it's also lean (low WIP).
2. **"If you don't have time to do it right, when will you find time to do it over?"** — succinctly captures the case for quality-first thinking.
3. **Variability must be identified and reduced** — Six Sigma's method is to find the root cause of variability and eliminate it, though the book flags that many real production problems are only indirectly related to variability, a theme it says will become a major focus of Part II's quantitative treatment.

## Key Takeaways

- "Lean manufacturing" is JIT under a new name, not a new idea — but the rebranding succeeded commercially where JIT itself stalled, partly because lean requires no software investment and so has almost no consulting barrier to entry.
- Six Sigma followed the identical pattern as TQM's successor: same underlying quality-improvement substance, repackaged with a new methodology (MAIC → DMAIC, plus DFSS/DMADV for new-product design) and a new set of high-profile corporate champions (Motorola, then GE under Jack Welch).
- The book's six numbered JIT/lean insights (environment-as-control, operational details matter, WIP control, flexibility-as-compensating-practice, quality-first, continual improvement) function as a compact summary checklist of everything Chapter 4 covered — useful as a fast review or audit-framing reference.
- The three TQM/Six Sigma insights point directly at Part II's stated agenda: the book explicitly previews that understanding *how* variability degrades performance (not just that it does) will be a major focus of the book's quantitative chapters.

## Connects to

- [[jit-origins-goals-and-environment-as-control]] — directly supplies insight #1 (environment as a control) and the seven zeros this section's closing lessons summarize.
- [[jit-implementation-tactics-and-quality-revolution]] — directly supplies insights #3, #4, and #5 (WIP control, flexibility-as-compensating-practice, quality-first) in full mechanical detail.
- [[kanban-mechanics-and-pull-system-variants]] — the pull-system mechanics that lean's "flow" concept and this chapter's WIP-control insight are built on.
- [[lean-methodology|lean thinking — the five principles]] and [[lean-methodology#The Seven Wastes (plus an eighth)|the seven wastes (muda)]] — the existing wiki's direct Lean Thinking source pages; this page is the book's own account of how and why that label came to replace "JIT" in the first place.
- [[manufacturing-peak-decline-resurgence]] — the quality lineage (Shewhart → TQM → Six Sigma) and efficiency lineage (JIT → lean → TPS) both trace the same three-trend pattern this page documents in detail.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | The lean-as-JIT-rebrand history and the explicit six-insight checklist are both directly usable in client conversations and audit framing |
| Current usefulness | 4 | The six-insight summary list is an immediately quotable, high-density audit-framing tool |
| KSU support | 5 | Canonical lean/Six Sigma history, core to any operations-management sequence |
| Tech-stack relevance | 1 | Not tech-stack related |
| Business audit value | 5 | The closing six-insight list is essentially a ready-made audit framework distilled directly from the source |
| Data/workflow value | 1 | Conceptual/historical |
| Reading urgency | 3 | Completes Chapter 4 |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit framing / client education — using the six-insight checklist as a fast diagnostic lens on any client's operation, or explaining to a client why "lean" and "Six Sigma" branding shouldn't be treated as something fundamentally newer or different from JIT/TQM

**Use when**:
A client references "lean" or "Six Sigma" as if it's a distinct, modern methodology unrelated to older JIT/TQM practices — useful context for grounding the conversation in what's actually durable substance versus rebranding. The six-insight list is also directly usable as a structured audit-observation checklist.

**Do not use when**:
A client needs the detailed mechanics behind any one insight (setup reduction, kanban, quality principles) rather than the summary — route to [[jit-origins-goals-and-environment-as-control]] or [[jit-implementation-tactics-and-quality-revolution]] instead.

**Fast retrieval query**:
`subject/lean-manufacturing` + `subject/six-sigma` — or search "goodbye JIT hello lean" / "DMAIC DFSS" / "six insights JIT" / "Jack Welch Six Sigma"

## North Star Connection

- How this applies to the audit business: the six-insight closing checklist is one of the most directly reusable frameworks in the entire Factory Physics ingest so far — it compresses an entire chapter's findings into a fast mental audit lens (environment-as-control, operational-detail discipline, WIP visibility, flexibility-as-compensation, quality-first sequencing, continual-improvement mindset). It is also a sharp, source-backed caution against treating "lean" or "Six Sigma" branding as inherently more sophisticated than the JIT/TQM substance underneath it.
- Track relevance: Business / KSU — very strong; directly usable both as client-facing framing and as exam-relevant operations-management history.
- Possible future Second Brain use: Yes — the six-insight list is a strong, near-ready candidate for an audit framework/checklist artifact once that Second Brain template exists.
