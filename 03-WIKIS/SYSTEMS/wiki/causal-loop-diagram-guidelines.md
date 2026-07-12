---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/client-interview, use-case/audit, subject/system-dynamics, subject/causal-loop-diagrams, subject/feedback-loops]
---

# Causal Loop Diagram Guidelines: Eleven Rules for Building Diagrams People Can Actually Read

**Summary**: Sterman's full set of CLD construction rules — causation vs. correlation, the two methods for determining loop polarity, resolving "ambiguous" links by exposing hidden multiple pathways, naming loops, showing delays, variable-naming conventions, layout, aggregation level, why one giant diagram fails, making negative-loop goals explicit, and separating actual from perceived state. Includes the schedule-pressure/burnout engineering case and the ice-cream/murder-rate correlation warning.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 5 ("Causal Loop Diagrams"), section 5.2

**Last updated**: 2026-06-22

---

## 5.2.1 Causation vs. Correlation: Never Diagram a Mere Correlation

Every link must represent a believed *causal* relationship — never a bare correlation. **The canonical illustration**: ice cream sales and the murder rate are positively correlated, but neither causes the other; both rise and fall with average temperature (summer vs. winter). A model linking ice cream sales directly to murder would "explain" that cutting ice cream consumption reduces murder — an absurd but structurally real risk whenever correlation gets mistaken for causal structure.

**Why this matters more than it might seem**: correlations reflect *past* behavior of a system, not its underlying structure. If conditions change — a previously dormant loop becomes dominant, a new policy is tried — a correlation built only on historical co-movement can break down entirely, while genuine causal structure persists across the regime change. Sterman quotes economist Phelps-Brown's blunt warning: **"Running regressions between time series is only likely to deceive"** when many series simply share a common driver (the business cycle, a seasonal pattern) without any direct causal link between them. The discipline required: scrutinize every candidate link for *whether you actually believe it's causal*, independent of how strong the correlation or statistical significance happens to be.

## 5.2.2-5.2.3 Labeling Polarity, and the Two Ways to Determine Loop Polarity

Every link and every important loop must be explicitly labeled (+ /- for links; R or B, with a circulating arrow matching the loop's own direction, for loops). Two methods exist for determining a loop's overall polarity:

- **The fast way**: count the negative links in the loop. Even count → positive loop; odd count → negative loop. (Formally: loop polarity is the sign of the *open loop gain*, the product of the individual link gains around the loop — and since the product of two negatives is a positive, an odd number of sign-reversals is required for net negative/self-correcting polarity.)
- **The right way**: trace the actual effect of a small disturbance all the way around the loop, starting from any variable. If the returning effect *reinforces* the original disturbance, the loop is positive; if it *opposes* it, negative.

**Sterman's explicit recommendation is the slower method, not the faster one** — "the right method... will often reveal a wrongly labeled polarity and will help you and your audience to grasp the meaning and mechanism of the loop. Assigning loop polarity the right way rather than the fast way saves time in the long run." The fast method is mechanically reliable but doesn't catch upstream labeling errors and doesn't build the audience's intuitive understanding of *why* the loop behaves the way it does — both of which matter more in a client workshop than counting speed.

## Resolving "Ambiguous" Polarity: It Usually Means a Hidden Second Pathway

When a link seems to have no single consistent polarity (the chapter's example: does Price → Revenue have positive or negative polarity, given that it depends on the price elasticity of demand?), **the right response is not to declare the link "conditionally signed" — it's to recognize that there are actually two separate causal pathways bundled into one link**, and to separate them explicitly. Revenue = Price × Sales, and Sales depends (negatively) on Price — so the single ambiguous "Price → Revenue" link should become two unambiguous links: Price → Revenue (positive, the per-unit-revenue effect) and Price → Sales → Revenue (negative overall, the volume effect). **Which pathway dominates is then a question of magnitude (the elasticity of demand) and delay (the volume effect is typically much more delayed than the per-unit effect) — exactly the kind of structural detail that gets lost if the ambiguity is left unresolved.** This is a generally reusable diagnostic: **whenever you can't assign a clean polarity, that discomfort is telling you a variable is bundling two distinct causal mechanisms that need to be pulled apart.**

## 5.2.4 Name Your Loops: The Schedule-Pressure/Burnout Engineering Case

Numbering loops (R1, R2, B1...) and **naming** them gives an audience a durable shorthand for a whole chunk of causal structure — and naming is most powerful when the client group itself supplies the name. **The chapter's worked case**: engineers and managers mapping the causes of chronically late design-project delivery identified a workweek/schedule-pressure structure with two intended fixes (work overtime — "Midnight Oil," loop B1; or cut corners on quality — loop B2) and two undercutting side effects: sustained overtime causes fatigue, which drops productivity, which raises schedule pressure further (the reinforcing **Burnout loop**, R1); and corner-cutting raises the error rate, which creates rework and lowers long-run productivity, raising pressure further still (the reinforcing **Haste Makes Waste loop**, R2 — the engineers' own name for it, after the manager group had initially wanted to call corner-cutting "gold-plating waste removal").

**Why the naming itself mattered, beyond clarity**: prior to the modeling intervention, the organization's standard mode of discourse was managers saying engineers "need to have their butts kicked" and engineers saying promotion to management "turns your brain to [fertilizer]" — pure mutual blame. Once the loops had names, **participants began discussing "the Burnout Loop kicking in"** instead of attacking each other — the names converted a person-blaming argument into a structure-discussing one. This is the same mechanism Ingalls/Navy achieved with their rework-cycle model (see [[ingalls-shipbuilding-project-dynamics-case]]) — a named, shared structural account replacing finger-pointing.

## 5.2.5 Indicate Important Delays: The Gasoline Demand Case

Delays should be shown explicitly in a CLD whenever they're important to the dynamic hypothesis or significant relative to the time horizon. **The chapter's central worked example**: gasoline demand's response to a price increase involves *radically different* delays stacked on top of each other — discretionary-trip cutbacks (near-immediate), carpooling/transit-switching (months), the decision to buy a more efficient car (~1 year perceptual/decision delay before committing), designing and building more efficient vehicles (several years), the existing inefficient car stock turning over only as it wears out (~10 years), and settlement-pattern changes (decades). **Total delay in the price-to-demand link: well over a decade.**

**The direct policy consequence**: because expenditures respond on the *short* delay (near-inelastic demand) while consumption only falls on the *long* delay (the vehicle stock turning over, efficiency improving), a permanent gas-price increase produces a textbook **worse-before-better** trade-off for consumers — expenditures rise immediately and only fall below the original level years later, once demand has fully adjusted. **This directly explains a persistent political puzzle**: raising gasoline taxes is hard in the US even when the long-run, NPV-positive benefit is well-established, because the short-run cost lands immediately and visibly while the benefit only accrues years after the policy — and elected officials, focused on the next reelection cycle, judge the short-run political cost as unacceptable, a judgment that itself reflects public unwillingness to accept near-term pain for distant gain.

## 5.2.6 Variable Naming Conventions

Three rules, each preventing a specific, common confusion:

1. **Variable names should be nouns or noun phrases, not verbs.** "Costs Rise" presumes costs only ever rise (biasing the discussion toward one behavior pattern) and makes it nonsensical to describe a *decrease* in costs ("costs rise" falling?). Use "Costs," with the direction of change captured by the link polarity, not baked into the name.
2. **Variable names must have a clear, unambiguous sense of direction.** "Feedback from the Boss" doesn't indicate whether *more* feedback is good or bad, or what an increase even means. "Praise from the Boss" does — it has an obvious positive-to-negative axis.
3. **Choose variables whose normal sense of direction is positive; avoid negation prefixes** (non-, un-, etc.). Use "Profit" (Revenue − Costs) rather than "Losses," and "Happiness" rather than "Unhappiness" — so that an increase in the variable name reads naturally as "more of a good thing," matching the audience's intuitive reading of "+" links.

## 5.2.7 Layout Tips

Use curved lines for feedback links (helps the eye trace the loop visually); route important loops along circular/oval paths; minimize crossed lines; **avoid decorative boxes/circles/hexagons around plain variables** ("chart junk" that clutters without adding meaning) — the explicit exception being stock-and-flow notation (rectangles for stocks, valve symbols for flows), where the shape itself conveys real structural information (covered in Chapter 6). Expect to redraw a diagram many times as you discover its content — iteration is normal, not a sign of poor initial work.

## 5.2.8 Choose the Right Aggregation Level

Too much detail obscures the overall loop structure; too little leaves the audience unable to judge plausibility. **The fix when an audience is confused by a compressed link** ("Market Share → Unit Costs"): disaggregate to show the intermediate reasoning explicitly (Market Share → Production → Cumulative Production Experience → Unit Costs, i.e., the learning-curve mechanism). Once the detailed version has been validated with the audience, it can be **"chunked" back into the simpler, aggregate link**, which then serves as a known shorthand for the richer structure underneath — a two-step process (disaggregate to build understanding, then re-aggregate for communication) rather than a one-time choice.

## 5.2.9 Don't Put All the Loops in One Diagram

Working memory holds roughly **7±2 chunks of information** — a hard practical ceiling on how much causal structure a single diagram can communicate, regardless of how comprehensive it is. A wall-filling, all-loops-included diagram "may be perfectly comprehensible to the person who drew it" but reads to everyone else as noise — "indistinguishable from a Jackson Pollock and considerably less valuable." **The fix**: build the model in stages, with a separate, focused diagram for each major loop or part of the dynamic story, then "chunk" those into a simpler high-level overview showing how the pieces interact — and in live presentations, build the full diagram up piece by piece rather than revealing it all at once.

## 5.2.10 Make the Goals of Negative Loops Explicit

Every negative loop compares an actual state to a goal and corrects the gap — and that goal should be shown explicitly in the diagram, **even when the goal isn't set by a person** (a cooling cup of coffee's implicit "goal" is room temperature, set by thermodynamics, not a decision-maker). Making the goal explicit invites the next, often more important question: **where does the goal itself come from?** Is product-quality target set by CEO edict, competitor benchmarking, customer input, or the company's own past performance? **Goals are frequently not exogenous but part of the feedback structure themselves** — capable of drifting over time in response to environmental pressure (directly previewed by [[gm-auto-leasing-case-study]]'s residual-value assumptions and fully developed in the student-workload case's "Goal Erosion" loop, where aspirations adjust downward after repeated disappointment). **The explicit exception**: don't bother showing the goal for pure decay processes whose implicit goal is simply zero (a death rate, equipment depreciation) — making that goal explicit adds no insight.

## 5.2.11 Distinguish Actual from Perceived Conditions

Real systems have a gap between the *true* state and what decision-makers *perceive* — caused by reporting delays, measurement noise, and systematic bias. **The chapter's quality-management example**: senior auto executives are typically given personally-selected, company-mechanic-serviced vehicles — meaning their personal experience of "our product quality" is systematically biased upward relative to a customer who buys off the lot and keeps the car for a decade. **Separating "Product Quality" (actual) from "Management Perception of Product Quality"** in the diagram — with an explicit delay and an explicit bias term between them — makes visible exactly how well-intentioned management can come to hold a "grossly exaggerated view" of their own product's quality, and immediately suggests the practical fix (shorten the delay, eliminate the bias) rather than leaving the gap as an unexamined assumption.

## Connects to

- [[causal-loop-diagram-notation-and-polarity]] — the companion page on CLD notation and the polarity-vs-behavior caveat that underlies the "determining loop polarity" methods on this page.
- [[ingalls-shipbuilding-project-dynamics-case]] — the schedule-pressure/burnout case's "loops replace blame" mechanism is the same dynamic the Ingalls/Navy rework-cycle model achieved at much larger scale.
- [[time-horizon-and-endogenous-explanation]] — the gasoline-demand delay-stacking example is a direct, granular illustration of that page's "set the time horizon several times longer than the longest delay" rule.
- [[barriers-to-learning-and-virtual-worlds]] — the actual-vs-perceived-conditions guideline is the diagrammatic tool for representing exactly the measurement-bias barrier (1.3.2) discussed there (the NASA ozone case is a real-world instance of an unmodeled actual/perceived gap).
- [[gm-auto-leasing-case-study]] — the "make goals explicit, and ask where they come from" guideline directly explains why GM's residual-value assumptions (an implicit, drifting goal) deserved scrutiny rather than being treated as fixed.

## North Star Connection

- How this applies to the audit business: the loop-naming technique (letting the client group name their own loops) is a directly reusable facilitation tool for de-escalating blame-based client conversations into structure-based ones. The actual-vs-perceived-state distinction is a sharp diagnostic question for any client whose self-reported metrics (quality, customer satisfaction, on-time delivery) may not match field reality.
- Track relevance: Business / Systems — directly applicable facilitation and diagramming technique for any audit discovery workshop.
- Possible future Second Brain use: an "eleven rules" CLD-drafting checklist, and a "name your own loop" facilitation script, are both strong candidates for a standalone audit-workshop toolkit.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Directly reusable facilitation and diagramming technique for client discovery workshops |
| Current usefulness | 5 | The loop-naming and actual-vs-perceived guidelines are immediately actionable in any client conversation |
| KSU support | 4 | Strong applied methodology, somewhat less formula-driven than the queueing-theory chapters |
| Tech-stack relevance | 1 | Conceptual diagramming guidance, no direct tool dependency |
| Business audit value | 5 | The blame-to-structure reframe (loop naming) is one of the sharpest consulting techniques in the whole ingest so far |
| Data/workflow value | 2 | Guides diagram construction rather than data collection itself |
| Reading urgency | 4 | High-value, broadly applicable guidance for any future client-facing diagramming work |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Facilitation toolkit for client discovery workshops — use the loop-naming technique to convert blame-based discussion into structure-based discussion, and the actual-vs-perceived-conditions guideline to probe whether a client's self-reported metrics match field reality.

**Use when**:
Running a discovery session where a client team is in active disagreement about whose fault a recurring problem is, or when a client's own reported numbers (quality, satisfaction, delivery) seem inconsistent with what's observed in the field.

**Do not use when**:
The diagramming exercise itself isn't warranted — a simple, well-understood problem doesn't need the full eleven-rule treatment.

**Fast retrieval query**:
`subject/causal-loop-diagrams` — or search "ice cream sales murder rate correlation" / "name your loops Burnout Haste Makes Waste" / "ambiguous link polarity multiple pathways" / "actual vs perceived product quality" / "seven plus or minus two chunks"
