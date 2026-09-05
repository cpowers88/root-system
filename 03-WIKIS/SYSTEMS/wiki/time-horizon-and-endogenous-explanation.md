---
domain: systems
type: method
tags: [subject/system-dynamics, subject/time-horizon, subject/endogenous-explanation, subject/model-boundary]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, audit, client-interview]
---

# Time Horizon, Endogenous Explanation, and Model Boundary: How to Scope a Diagnosis Correctly

**Summary**: Why "always model a problem, never model a system" is the single most important scoping discipline, how the choice of time horizon can completely reverse a diagnosis (the US oil production case), why exogenous explanations are not explanations at all, and the federal PIES energy model's costly real-world failure from treating the economy as exogenous when it should have been endogenous.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 3 ("The Modeling Process"), sections 3.5-3.6 (chapter complete)

**Last updated**: 2026-06-22

---

## "Always Model a Problem, Never Model a System"

The single most important scoping rule in the chapter. A model of *the business cycle* or *fossil-fuel policy* is a model of a problem — bounded by a specific question. A model that claims to represent "the entire economy" is a model of a *system* — and Sterman argues this is close to incoherent: a model detailed enough to answer every conceivable question would be as complex as the system itself, could never be completed, and even if completed, its assumptions could never be examined or its behavior understood — at which point client confidence would rest on the modeler's authority rather than anything testable. Quoting Mesarovic: **"No matter how many resources one has, one can envision a complex enough model to render resources insufficient to the task."**

**The practical payoff of a clear purpose**: it "acts as the logical knife" — it gives you a defensible basis to say "we don't need to include that" when a client pushes to add scope. Without a stated purpose, there's no principled way to refuse scope creep — every suggested addition seems equally justified, and the model becomes unbuildable, untestable, or both.

## The Time Horizon Test: The US Oil Production Case

A worked, visceral demonstration of how time-horizon choice alone can reverse a diagnosis, using the same underlying US petroleum data at three different scales:

- **10-year horizon (1986-1996)**: production trending slowly down, consumption slowly up, imports growing modestly, prices in a narrow $14-23/barrel band. **Conclusion supported: the energy system looks relatively stable — no urgent long-term problem.**
- **130-year horizon (from the 1859 start of the US oil industry)**: reveals two completely different regimes — exponential consumption growth (4.3%/year, 1920-1973) that production nearly matched, followed by a 1970 production *peak* that has fallen ever since (54% of peak by 1996 despite Alaska's Prudhoe Bay coming online), with imports reaching 61% of total consumption by 1996. **Conclusion supported: the problem was never solved in the 1980s — it has been steadily getting worse the entire time**, completely contradicting the 10-year read of the identical underlying system.
- **A too-long horizon (M. King Hubbert's 150,000-year graph)**: shows the entire fossil-fuel era as a brief, transitory spike in human history — true and sobering, but, in Sterman's own assessment, "too long to be useful to policy makers" making near-term capital, regulatory, or R&D decisions.

**The general lesson, stated as a rule of thumb**: "Most people dramatically underestimate the length of time delays and select time horizons that are far too short... A good rule of thumb is to set the time horizon several times as long as the longest time delays in the system, and then some." Modelers must actively resist a client's *initial* proposed time frame, which is usually set by an arbitrary milestone (fiscal year-end, next 5-year plan) rather than by the actual dynamics of the problem.

**A second worked example sharpens the stakes**: a 1970s Sahel-region foreign-aid model, run to the round-number year 2000, showed irrigation/bore-hole subsidies producing clear improvement (cattle stocks and herder wealth both rising). **Run further into the 2000s, the same model showed cattle stocks eventually overshooting the region's carrying capacity, triggering overgrazing, desertification, and a population crash** — i.e., the policies the short horizon recommended were actively counter to the region's long-term interest. The time-horizon choice alone flipped the policy recommendation from "fund this" to "this will cause a future collapse."

## Endogenous vs. Exogenous Explanation

**Endogenous** ("arising from within") explanations generate a system's dynamics from the interaction of variables and decision rules actually represented inside the model. **Exogenous** ("arising from without") variables are assumed inputs from outside the model boundary. Sterman's blunt verdict: **"Exogenous explanations are really no explanation at all; they simply beg the question, what caused the exogenous variables to change as they did?"** This isn't a purist preference — every candidate exogenous variable should be scrutinized specifically for whether there's an important feedback loop *from* the model's own endogenous elements back to it; if so, the boundary must expand to bring it inside.

## The PIES Model: A Real, Costly Failure of Boundary Choice

The Federal Energy Administration's Project Independence Evaluation System (PIES, 1970s) modeled US energy policy's impact on economic growth, inflation, and unemployment — but treated **the economy itself as exogenous**, completely unaffected by energy prices or policy. The internal contradiction this created: the model assumed high economic growth and low price elasticities, which implied huge energy-sector capital requirements — satisfied in the model **without reducing investment or consumption anywhere else in the economy and with no effect on interest rates or inflation**. As Sterman puts it: "the model let the economy have its pie and eat it too."

**The real-world consequence**: PIES projected the US would be near energy independence by 1985 — 3.3 million barrels/day of imports, 250,000 bbl/day of shale oil production, ~$22/barrel oil, alongside vigorous growth. **None of this happened**: imports were 5.5M bbl/day in the late 1980s and over half of consumption by the mid-1990s; shale oil and synfuels never materialized — despite the model not even anticipating the demand-crushing recession and $30+/barrel prices that actually occurred. **The sharpest line in the section**: the model provided detailed supply/demand/price breakdowns for dozens of fuels by region — "what purpose was served by the effort devoted to forecasting the demand for jet fuel... in the Pacific Northwest when the basic assumptions were so palpably inadequate?" **Granular detail inside a wrongly-drawn boundary doesn't rescue a model — it just produces more precisely wrong numbers.** This is a direct, real-stakes instance of [[policy-resistance-and-feedback-thinking]]'s "a broad model boundary matters more than detail" principle.

## How to Make the Boundary Inspectable: The Model Boundary Chart

A **model boundary chart** simply lists which key variables are endogenous, which are exogenous, and which are excluded entirely — and Sterman calls this tool "surprisingly useful and shockingly rare." His own DOE energy-economy model (1950-2050 horizon, deliberately built in reaction to PIES's failure) made *all* major macroeconomic variables endogenous (GNP, employment, interest rates, energy production/demand/imports) but explicitly listed remaining exogenous variables (population, technological-progress rate, world oil price) and excluded concepts (inventories/business cycles, nonenergy trade, environmental constraints, interfuel substitution, income distribution) — with an explicit caveat for each: e.g., excluding environmental constraints means conclusions about exotic energy sources (synfuels) will be *overoptimistic*, a direction-of-bias the model user needs to know before trusting an output number.

**Why modelers resist publishing this list, and why that resistance is exactly backwards**: "many feel uncomfortable listing what they've left out, see the omissions as flaws and prefer to stress the strengths of their model... this tendency... undercuts the utility of your model." A published boundary chart is a *credibility* tool, not an admission of weakness — it's what lets a model user judge for themselves whether a given conclusion can be trusted, rather than discovering the hidden assumption only after a bad decision has been made on it.

## Other Boundary/Architecture Mapping Tools (Briefly)

- **Subsystem diagrams**: show a model's major subsystems (e.g., "the firm" and "the market," or manufacturing/product-development/accounting/financial-stress for a more complex case) and the flows connecting them — communicating scope and aggregation level without yet showing internal causal detail. Forrester's own corporate-growth model took roughly two years of false starts to find the right subsystem boundary, but only eight weeks to build the full ~200-equation model once that boundary was right — a sharp illustration that **boundary-finding, not equation-writing, is where most of a real modeling project's time and difficulty actually lives.**
- **Causal loop diagrams** (full treatment in Chapter 5) and **stock-and-flow maps** (Chapters 6-7) — covered in depth elsewhere in the planned ingest scope.
- **Policy structure diagrams** — show the specific information inputs to one decision rule, rather than a whole system's feedback structure.

## Formulation, Testing, and Policy Design (Briefly)

**Formulating the simulation model** forces precision a conceptual diagram doesn't: "computers accept no hand-waving arguments" — writing actual equations routinely surfaces vague concepts and unnoticed contradictions even before any simulation runs. **Testing** goes well beyond fitting historical data — every variable must map to a real-world concept, every equation must be dimensionally consistent, and **extreme-conditions tests** are critical: a model of an economy must show GDP collapsing toward zero if energy supply is cut to zero; a model of an automaker must show demand collapsing to zero if price rises a billionfold. Sterman's pointed warning: **"you might imagine models would never fail such obvious tests... but you'd be wrong"** — many widely-used models in economics, psychology, and management violate basic physical/logical constraints while still fitting historical data well, because historical-fit testing alone never exercises the regions where the violation would show up. **Policy design** is not parameter-tweaking (changing a tax rate) but the design of genuinely new decision rules and structures — and because real systems are nonlinear, combined policies routinely produce effects that are not simply additive (sometimes interfering, sometimes strongly synergistic — directly echoing the synergy result in [[dupont-maintenance-game-and-twelve-principles]]'s Du Pont policy comparison).

## Connects to

- [[policy-resistance-and-feedback-thinking]] — "exogenous explanations are no explanation at all" is the formal modeling-methodology version of that chapter's "there are no side effects, only effects from a too-narrow model boundary."
- [[barriers-to-learning-and-virtual-worlds]] — the PIES case is a real, expensive instance of the confounding-variables and flawed-cognitive-map barriers operating at the scale of a national policy model rather than an individual's mental model.
- [[gm-auto-leasing-case-study]] — GM's leasing model succeeded specifically *because* it expanded the boundary to include the used-car market endogenously, exactly the move PIES failed to make with the broader economy.
- [[modeling-process-and-client-ethics]] — this page's model boundary chart is the concrete tool for the ethical transparency that page describes (showing clients exactly what's included/excluded rather than hiding assumptions).

## North Star Connection

- How this applies to the audit business: the time-horizon test (the 10-year vs. 130-year oil case) is a directly reusable audit technique — when a client's own data looks "stable" or "fine," check whether the time window itself is hiding a longer-term trend. The model boundary chart is a strong, lightweight, transparency-building deliverable: an explicit list of what an audit's recommendations do and don't account for, protecting both Chris and the client from over-trusting a scoped analysis.
- Track relevance: Business / Systems — core scoping discipline for every audit engagement, and a strong KSU/ISYE methodology reference.
- Possible future Second Brain use: a "time horizon check" question and a lightweight "boundary chart" template (endogenous / exogenous / excluded, one line each) are both strong candidates for a standalone audit-scoping checklist.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Core scoping discipline directly applicable to every audit engagement's framing and credibility |
| Current usefulness | 5 | The time-horizon test and the boundary-chart tool are both immediately usable, lightweight audit techniques |
| KSU support | 4 | Strong methodology content; the PIES case is a well-documented real policy-modeling failure useful for systems engineering coursework |
| Tech-stack relevance | 1 | Conceptual chapter, no direct tool dependency |
| Business audit value | 5 | The time-horizon test and the "always model a problem, never a system" rule are both sharp, directly reusable consulting disciplines |
| Data/workflow value | 2 | Conceptual scoping guidance rather than a specific data method |
| Reading urgency | 4 | Closes out Part I's foundational methodology before the book's technical tool chapters (5-8) begin |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Engagement-scoping and credibility tool — use the time-horizon test whenever a client's own data appears reassuringly stable, and use a lightweight model-boundary chart (endogenous/exogenous/excluded) to make explicit what any audit analysis does and doesn't account for.

**Use when**:
Scoping any new engagement (to set the right time horizon and explicit boundary up front) or reviewing a client's existing report/dashboard that looks stable over a short window.

**Do not use when**:
The problem genuinely has no meaningful longer-term trend to check (e.g., a one-time operational incident) — forcing a time-horizon reframe onto a genuinely short-horizon problem would overcomplicate it.

**Fast retrieval query**:
`subject/time-horizon` + `subject/endogenous-explanation` — or search "US oil production 130 year time horizon" / "PIES model exogenous economy" / "always model a problem never a system" / "model boundary chart"
