---
domain: systems
type: concept
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/audit, use-case/business-model, use-case/ksu-support, subject/manufacturing-history, subject/scientific-management, subject/factory-physics]
---

# What Went Wrong? The Three-Trends Critique and the Case for a Science of Manufacturing

**Summary**: Chapter 5's central argument — why "Newton's law of consultants" (for every expert there is an equal and opposite expert) still rules manufacturing management despite decades of "progress": each of the three historical trends (efficiency/lean, quality/Six Sigma, integration/SCM) offers a genuinely valuable component, but all three are missing the one thing that would let them work together — an actual scientific framework connecting policies to performance. This is the book's direct setup for Part II's "Factory Physics" project.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 5 ("What Went Wrong?"), sections 5.1, 5.2, 5.6

**Last updated**: 2026-06-21

---

## "Newton's Law of Consultants": Why Expertise Hasn't Converged

The chapter opens by naming the central puzzle directly: after so much manufacturing "progress" across scientific management, JIT/lean, TQM/Six Sigma, MRP/ERP/SCM, why does "for every expert there is an equal and opposite expert" still hold? The book's answer requires revisiting the **three historical trends** first identified in Chapter 1 and traced through Chapters 2-4:

1. **Efficiency trend** — scientific management (1900s) → JIT (1970s-80s) → lean manufacturing/TPS (1990s-present). Emphasizes visual management, smooth flow, low inventory, and (unlike the original scientific management movement) tends to deemphasize mathematical modeling in favor of overall philosophy and shop-floor methods.
2. **Quality trend** — Shewhart's statistical methods (1930s) → Juran/Deming (1950s-80s) → TQM (1980s) → Six Sigma (1990s-present, via Motorola and GE). Reconnected the quality trend to its statistical origins while evolving into a broader systems-analysis framework that places quality in the context of overall efficiency.
3. **Integration trend** — began in the 1960s with the computer's introduction into manufacturing → MRP (1970s "MRP Crusade") → MRP II → ERP (1990s) → SCM (2000s). See [[mrp-history-and-push-pull-paradigm]] and [[erp-and-scm-history-and-tradeoffs]] for the full lineage.

## Each Trend's Real Flaw, in the Book's Own Diagnostic Terms

**Lean manufacturing**: its current tools are largely simple — value stream mapping (VSM) to find *muda*, a future-state map, then a standard set of kaizen events (setup reduction, 5S, visual controls, kanban). When the current situation closely resembles a past success and the practitioner is skilled at recognizing the analogy, this works. **But in genuinely new situations, an experience-based, imitation-driven approach is unlikely to be innovative enough to find a useful solution.**

**Six Sigma**: in sharp contrast, has migrated from simple to sophisticated — heavy statistical training (four 36-hour-week "waves"), borrowed motivational/marketing techniques (black belts, champions), and full upper-management funding commitments. **But Six Sigma provides training in advanced statistics without providing education in how manufacturing systems actually behave.** The book's worked illustration: faced with a plant showing high inventory, poor service, and low productivity, a Six Sigma black belt would define the problem, measure, design an experiment to find the "drivers," implement changes, and institute controls — a process that *might* eventually work, but is tedious and slow precisely because it has to rediscover, from scratch, causal relationships (WIP↔service↔productivity) that are already known principles. **Managers and engineers need to be able to invoke known principles for addressing generic problems like high WIP and poor customer service — but those principles are not currently part of the Six Sigma methodology.**

**Supply chain management (the integration trend's current form)**: because of its historical roots in computing, this movement has always framed manufacturing in IT terms — collect enough data, install enough hardware, implement the right software, and the problem is solved. **What goes consistently unsaid is that any software package relies on some underlying model — and the model behind SCM, ERP, MRP II, and MRP all the way back to its 1960s origin has almost always been wrong** (see [[mrp-erp-empirical-failure-and-other-scientific-approaches]] for the specific flaw and its persistence). The original MRP insight — that independent and dependent demand should be treated differently — remains genuinely fundamental, and the MRP II planning hierarchy still provides real coordination value. **But making effective use of ERP/SCM's data and scheduling sophistication requires tailoring the information system to a firm's actual business needs, not the reverse** — and the ultimate success of the SCM movement will depend far more on the modeling progress it promotes than on any further IT advances.

## "The Solution": What Each Trend Gets Right, and the One Thing Missing From All Three

The book is explicit that the three trends already contain valuable components of an integrated solution:

1. **Six Sigma offers a genuine improvement *methodology*** — engaging both upper management and front-line workers, acknowledging that improvement is genuinely difficult, and providing detailed, serious training (rather than empty "rah rah").
2. **Lean philosophy promotes the right *incentives*** — focus on the customer, set aside unit-cost obsession, find and eliminate obviously wasteful practices, and actively modify/improve the production environment (see [[jit-origins-goals-and-environment-as-control]]).
3. **IT systems (SCM/ERP) provide the *data*** needed to make rational manufacturing decisions.

**The missing component, stated as plainly as the book ever states anything: a scientific framework that can make sense of the underlying manufacturing operations.** Unlike circuit designers (who have Ohm's law) or bridge engineers (who have established principles of stress, compression, and tension), most Six Sigma black belts, lean practitioners, and SCM salespeople simply lack a working knowledge of the basic relationships governing manufacturing systems — cycle time, production rate, utilization, inventory, WIP, capacity, and variability (in both demand and process). **Without this knowledge, practitioners are left with exactly three fallback options**: (1) analyze the system statistically to find cause and effect, then implement and control changes (the Six Sigma approach); (2) imitate what worked elsewhere and hope it works again (the lean approach); or (3) install a new software application (the IT approach). **Success under any of these three approaches depends on luck or local genius** (an in-house Ohno) — neither of which is a reliable, repeatable source of competitive advantage. The remainder of us need an actual framework.

## The Closing Synthesis: Five Points, and the Call for a Real Science

The chapter's own explicit five-point summary of "what went wrong":

1. **Scientific management became mathematical management** — it reduced the manufacturing problem to analytically tractable subproblems using unrealistic assumptions, providing little useful overall guidance (though the mathematics and original insights remain individually useful within a better framework).
2. **Information technology without a suitable flow-process model is fundamentally flawed** — MRP is not flawed in its details but in its basics (infinite-capacity, fixed-lead-time), a flaw inherited unchanged by MRP II, ERP, and SCM (see [[mrp-erp-empirical-failure-and-other-scientific-approaches]]).
3. **Other "scientific" approaches (e.g., BPR) exhorted rethinking without providing a framework for doing so**, becoming too closely identified with purely radical solutions and downsizing to offer a balanced alternative.
4. **Lean manufacturing provides many useful tools, but its methodology is fundamentally imitation-based** — it offers no general improvement approach and no comprehensive systems-analysis paradigm; VSM is a good start but doesn't go far enough (e.g., it offers no help with practical lot sizing or stock-setting decisions).
5. **Six Sigma is genuinely rooted in the scientific method's experimentation step, but provides no paradigm for organizing and retaining the knowledge experiments generate** — DMAIC is useful for cause-finding and variability control, but is not a comprehensive tool set.

The book draws a deliberate parallel between Lord Kelvin's 1900 overconfidence that physics was essentially finished ("nothing new to be discovered... all that remains is more and more precise measurement") and economist John Kenneth Galbraith's 1958 claim that society had "solved the problem of production." **Each successive manufacturing "solution" — scientific management, operations research, MRP, JIT, TQM, BPR, ERP, SCM, lean, Six Sigma — has been sold as *the* answer, and each has disappointed**, yet faith in an eventual "technological silver bullet" persists undiminished (the 2002 coinage of "lean Six Sigma" / "lean sigma" — concatenating two existing buzzwords rather than generating a genuinely new idea — is offered as a symptom of this fatigue). **The book's central wager**: manufacturing is too complex, large-scale, multiobjective, rapidly changing, and competitive for any simple, uniform solution to work across the full spectrum of environments — so each firm must develop its own effective strategy, grounded in real understanding of core processes and the relationships between performance measures, and continue improving it indefinitely. **"Factory Physics" is the book's name for the framework it believes can finally deliver this** — scientific management based on actual science.

## Key Takeaways

- The book's central diagnostic move: all three historical trends (efficiency, quality, integration) contain real value, but all three are missing the same thing — a working scientific model of how manufacturing systems actually behave, connecting policies (lot size, WIP levels, capacity buffers) to performance (cycle time, service, cost).
- Six Sigma's central weakness, in the book's own framing: it trains people in statistics, not in manufacturing-system behavior — so practitioners must rediscover, case by case and at great cost in time, causal relationships (e.g., WIP↔service) that are already known general principles.
- Lean's central weakness: its methodology is imitation-based (pattern-match to a prior success), which works well for familiar problems but cannot reliably generate solutions to genuinely new ones.
- The IT/SCM trend's central weakness: software always implicitly encodes a model, and the model inherited from 1960s MRP has been wrong since the start — more IT sophistication without fixing the underlying model just automates the same flaw faster.
- The Kelvin/Galbraith parallel is a sharp, reusable rhetorical device for any conversation where a client (or a vendor) claims a "final," "complete," or "silver bullet" solution to an operational problem.

## Connects to

- [[mrp-erp-empirical-failure-and-other-scientific-approaches]] — the specific empirical evidence (inventory-turns data, adoption surveys, the BPR/VSM/DMAIC case-by-case critiques) supporting this page's diagnostic claims.
- [[mrp-history-and-push-pull-paradigm]] and [[erp-and-scm-history-and-tradeoffs]] — the integration-trend lineage this page argues never fixed its foundational flaw.
- [[jit-origins-goals-and-environment-as-control]] and [[goodbye-jit-hello-lean]] — the efficiency-trend lineage; this page's lean critique builds directly on the "imitation, not innovation" framing introduced there.
- [[manufacturing-peak-decline-resurgence]] — the original three-trend framing (efficiency/quality/integration) this chapter explicitly revisits and critiques.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | This is the book's thesis statement — directly informs how Chris should evaluate any client's existing "lean," "Six Sigma," or ERP/SCM initiative |
| Current usefulness | 5 | The "three trends, one missing piece" framework is immediately usable in any audit or client-advisory conversation |
| KSU support | 5 | Canonical operations-management historiography and the explicit setup for the book's entire Part II framework |
| Tech-stack relevance | 2 | Conceptual; informs how to evaluate `stack/industry-platforms` (ERP/SCM) critically rather than directly building anything |
| Business audit value | 5 | The Kelvin/Galbraith "silver bullet" parallel and the three-fallback-options framing (statistics/imitation/IT) are both sharp, ready-to-use audit talking points |
| Data/workflow value | 2 | Conceptual/diagnostic, not a data technique |
| Reading urgency | 5 | This is the hinge chapter the entire book has been building toward since Chapter 1 |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit framing / client advisory — diagnosing whether a client's existing improvement initiative (lean program, Six Sigma black belt, new ERP/SCM rollout) has a real underlying model of their operations, or is relying on imitation, ungrounded statistics, or software alone

**Use when**:
A client describes an existing lean, Six Sigma, or ERP/SCM initiative as "the" solution to their operational problems, or when Chris needs a framework for explaining why a sophisticated-sounding methodology hasn't actually fixed an underlying operational issue.

**Do not use when**:
The client genuinely just needs one of the three components (a kaizen event, a statistical root-cause investigation, better data visibility) rather than a full diagnostic reframe — not every engagement needs this chapter's full critique.

**Fast retrieval query**:
`subject/manufacturing-history` + `priority/now` — or search "Newton's law of consultants" / "three trends" / "Kelvin Galbraith silver bullet" / "scientific management based on science"

## North Star Connection

- How this applies to the audit business: this is arguably the single most important page in the entire Factory Physics ingest for the audit business specifically — it gives Chris a direct, source-backed answer to "why hasn't [lean / Six Sigma / our new ERP] already fixed this?" The three-fallback-options framing (statistics, imitation, or software, absent a real model) is a fast diagnostic for categorizing what kind of "solution" a client has actually been sold, and the explicit call for a framework connecting policy to performance is exactly the audit value proposition Chris is building toward.
- Track relevance: Business / Systems / KSU — the highest-leverage page so far in this ingest across all three.
- Possible future Second Brain use: Yes — strong candidate for a core audit-philosophy document once Chris formalizes his own audit methodology, since it's effectively the intellectual foundation for "find the model, not just the symptom."
