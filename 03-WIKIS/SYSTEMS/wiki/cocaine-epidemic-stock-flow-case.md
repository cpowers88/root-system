---
domain: systems
type: case-study
tags: [priority/now, status/wiki-only, domain/systems, source-role/example, use-case/systems-analysis, use-case/data-workflow, use-case/audit, subject/system-dynamics, subject/stocks-and-flows, subject/policy-resistance, subject/data-quality]
---

# The Cocaine Epidemic: How Stock-Flow Logic Proved the Government's Own Survey Data Was Mathematically Impossible

**Summary**: In the late 1980s, US government survey data showed cocaine use sharply declining — exactly while arrests, ER visits, deaths, and street purity all showed it exponentially increasing. A system dynamics model resolved the contradiction not through new data, but by applying a single, rigorous stock-flow constraint: the survey-reported decline was *physically impossible* given how a stock that can only be added to (or lost through death) actually has to behave. Closes Chapter 7 of Business Dynamics.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 7 ("Dynamics of Stocks and Flows"), section 7.3 (chapter complete)

**Last updated**: 2026-06-22

---

## The Paradox: Two Data Sets, Opposite Stories

By the late 1980s the US "War on Drugs" had spent billions on supply-side enforcement (interdiction, seizure, stiffened penalties), justified by survey data (National Household Survey, High School Senior Survey) showing past-month cocaine use falling sharply — from 3% of the population (1985) to under 1% (1990), coinciding neatly with rising seizure rates (above 75 metric tons/year). **The administration cited this as proof the strategy was working and asked for more funding.** But every other available indicator told the opposite story: arrests, cocaine-related ER visits, and cocaine-related deaths all rose **exponentially** over the same period, while street purity rose and street price fell — both classic signatures of *increasing*, not decreasing, supply and demand. Competing federal agencies (FBI, DEA, SAMHSA, NIJ, NIDA, ONDCP, CIA — each defending its own data and competing for a share of $10B+/year) argued past each other about which dataset was "right."

## The Stock-Flow Model That Resolved It (Homer 1993, 1997)

A National Institute of Justice-commissioned system dynamics model (several hundred equations) built an explicit stock-flow structure of the user population: **Never-Used → Active Casual Users → (escalation) → Active Compulsive Users**, with active users (both types) able to stop into **Transitional Users**, who either relapse back to active use or, after a year clean, become **Ex-Users** (who can themselves relapse) — plus death outflows from every stock. Critically, **the model's category boundaries were built to exactly match the survey's own definitions**: total active users = past-month use; active + transitional = past-year use; active + transitional + ex-users = lifetime ("ever used") prevalence — making the model and the survey data directly, rigorously comparable.

## The Proof of Impossibility

**The single inflow to the "ever-used" stock is the initiation rate (first-time users); the only outflow is death.** This stock-flow structure, by itself — with zero need for any feedback loop or further assumption — proves the survey data could not have been correct. The NHS reported the *fraction* of the population who'd ever used cocaine *falling* by 3.2 percentage points from 1982 to 1988. **For that to be true, the death rate of the ever-used population would have had to substantially exceed the death rate of the never-used population** (since the lifetime-prevalence *fraction*, not just the raw count, was reported as falling) — but excess mortality among the (mostly former) cocaine-user population is far too small to produce anything close to that decline, even under the most extreme, "every man, woman, and child just said no" assumption about the initiation rate dropping to zero. **The survey-reported decline was not merely unlikely — it was mathematically impossible given the basic stock-flow accounting of who can enter and leave that stock.**

**This single argument — not a new dataset, not a better survey, just rigorous stock-flow bookkeeping applied to data the government had already published — proved the headline "we're winning" claim false.** It is among the cleanest available illustrations in this entire ingest of [[stock-flow-fundamentals-and-notation]]'s point that "stocks change only through their rates": you cannot get a falling lifetime-prevalence *fraction* without either a death-rate or out-migration mechanism big enough to explain it, and none existed at anything like the required scale.

## Why the Survey Data Was Actually Wrong

Two compounding sources of systematic underestimation, both worsening specifically *because* the epidemic was getting worse: **(1) sampling bias** — heavy users (increasingly concentrated in populations the survey structurally undersamples: transients, the incarcerated, those without stable addresses) grew as a share of the true user population, and the survey's own stratification corrections didn't keep pace; **(2) increasing denial** — as legal and social risk grew, a rising fraction of both current and especially *former* users simply lied about ever having used cocaine when asked. **The second mechanism is the more important one, and it produces an especially insidious measurement artifact**: recent-use measures (past month, past year) **confound two genuinely different phenomena that move in the same direction in the data but mean opposite things** — people who *actually quit*, and people who *didn't quit but started lying.* Only by anchoring the analysis in lifetime-prevalence's strict stock-flow accounting (where the "ever used" stock's only legitimate outflow is death) could the model separate a real behavioral decline from a reporting artifact — a separation the raw survey data, taken at face value, could never make on its own.

**The administration's own preference for the recent-use measures over lifetime-use measures is itself diagnostically significant** — recent-use data showed the largest, most politically favorable decline, while lifetime-use data (the only category amenable to the stock-flow impossibility check) was comparatively ignored in the public debate. Sterman's pointed framing: whether this reflected genuine ignorance of basic stock-flow accounting, or cynical awareness that the more favorable (and less rigorously checkable) measure made the better political case, "the ability to understand basic stock and flow relationships is far too rare in our society today, even among many professional policy analysts."

## What Actually Ended the Epidemic — and Why Interdiction Gets the Wrong Credit

The model's later validation is itself a strong forecasting result: built on data available only through 1989, it correctly anticipated the epidemic's 1990s turning point (the shift from exponential growth to gradual decline) without being recalibrated, using only two genuinely exogenous inputs (the age-12+ population and marijuana prevalence as a social-tolerance proxy) — a meaningful, falsifiable predictive success, not just a backward-fit.

**The model's actual causal account directly contradicts the interdiction narrative**: the slowdown was driven by two negative feedback loops entirely on the *demand* side — rising recognition of cocaine's real **health risks** (no longer perceived as the benign, fashionable drug of the mid-1970s) and rising **fear of arrest/incarceration** — not by the supply-side Supply Disruption or Clean-Up-the-Streets loops the administration credited. **MacCoun and Reuter's blunt empirical summary, quoted directly**: "The probability of a cocaine or heroin seller being incarcerated has risen sharply since about 1985 but that has led neither to increased price nor reduced availability." **Both effective loops, however, operate on long, compounding delays**: harm has to actually accumulate in the compulsive-user population (itself growing on a lag behind casual use) before it's visible enough, personally or via high-profile cases (Richard Pryor's freebasing injury, Len Bias's death), to shift public perception — meaning the reinforcing Word-of-Mouth growth loop dominates early, and the corrective demand-side loops only catch up once substantial cumulative harm has already occurred. **The genuinely ironic mechanism, stated directly**: the epidemic was not curbed by making cocaine less available — availability, purity, and affordability all kept *rising* throughout the 1980s — it was curbed because abundance itself generated enough direct personal and secondhand experience of harm to erode the drug's social appeal. **"The cocaine epidemic was ultimately self-limiting"** — but only after the delay needed for harm-recognition to catch up with exponential growth had already let the epidemic run far longer and reach far higher than it otherwise would have.

## The General Pattern: Boom-and-Bust Is the Generic Signature of Any Harmful Novelty

Sterman explicitly generalizes this feedback structure (Word-of-Mouth positive loop vs. delayed Health-Risk/Fear-of-Arrest negative loops) to **any harmful substance or practice, legal or illegal** — and backs it with a second, independently-documented historical cycle: a near-identical late-1800s/early-1900s cocaine boom (beginning as a *medically endorsed* treatment — Freud's 1884 "On Coca" praised it for opium addiction, alcoholism, fatigue, and more; commercialized into Coca-Cola and cigarettes; eventually generating enough visible harm — "by 1914 the Atlanta police chief was blaming 70 percent of the crimes [in the city] on cocaine" — to trigger escalating legal restriction) followed by decades of low use, until institutional memory of the harm faded and the cycle restarted. **The closing, sobering generalization**: each new wave doesn't require a *new* drug — it just requires a population (or a drug) for which the hard-won knowledge of harm has faded from collective memory, which is exactly why the modest 1990s decline in cocaine use was immediately followed by rising use of other substances (marijuana, methamphetamine, and a heroin resurgence stimulated by 1990s "heroin chic" media glamorization) rather than any lasting reduction in overall demand for mind-altering substances.

## 7.4 Chapter Summary

Stocks integrate (accumulate) their net flow; differentiating a stock's trajectory recovers its net rate. These two operations — covered in [[graphical-integration-and-differentiation]] — require no formal calculus to apply intuitively, and the ability to reason this way "is essential for all modelers, even those with extensive mathematics training, because most realistic models have no analytical solutions." **Both case studies in this chapter (global warming, the cocaine epidemic) demonstrate that understanding stock-flow dynamics alone — even before considering the surrounding feedback structure — can resolve genuinely counterintuitive, high-stakes real-world puzzles** that intuition, or even competing expert data interpretation, gets wrong.

## Connects to

- [[stock-flow-fundamentals-and-notation]] — the "ever-used population can only fall via death" argument is the cleanest, highest-stakes available illustration of "stocks change only through their rates."
- [[barriers-to-learning-and-virtual-worlds]] — the systematic, worsening survey underreporting (sampling bias plus rising denial) is a real, consequential instance of the limited-information barrier (1.3.2), compounded by [[causal-loop-diagram-guidelines]]'s correlation-vs-causation warning (recent-use declines confounding real quitting with rising lying).
- [[global-warming-stock-flow-inertia-case]] — both cases share the same structural lesson: a politically convenient metric (recent-use surveys; near-term emission stabilization) can mask the true behavior of the underlying stock, which only rigorous stock-flow accounting reveals.
- [[traffic-congestion-and-compensating-feedback]] — the interdiction strategy receiving credit for a decline actually driven by unrelated demand-side feedback is structurally the same misattribution error as crediting road-building for congestion relief that's actually compensated away by induced demand.

## North Star Connection

- How this applies to the audit business: the "the stock can only change through its actual inflows/outflows, so check whether a reported trend is even mathematically possible" technique is a directly reusable due-diligence method for any client-reported metric that looks suspiciously favorable — before accepting a reported decline in a backlog, defect rate, or any cumulative count, check whether the implied flow rates are physically plausible given what's actually known about entries and exits. The demand-side-vs-supply-side misattribution (interdiction getting credit for a decline it didn't cause) is a sharp general caution against crediting whichever policy was most visible or most expensive, rather than the one a rigorous structural model actually supports.
- Track relevance: Business / Systems — a powerful, well-documented illustration of a generally applicable audit technique (testing whether a reported number is structurally possible), independent of the specific public-policy subject matter.
- Possible future Second Brain use: a "stock-flow plausibility check" (given the known inflows and outflows, could this reported change in the stock actually have happened?) is a strong, near-ready candidate for a standalone data-quality audit technique.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The stock-flow plausibility-check technique is a directly reusable, broadly applicable data-quality audit method |
| Current usefulness | 5 | Immediately applicable to vetting any client-reported cumulative metric before trusting it |
| KSU support | 5 | An exceptionally well-documented real case combining rigorous stock-flow theory with major public-policy stakes |
| Tech-stack relevance | 2 | The plausibility-check logic is directly implementable as a simple spreadsheet sanity-check formula |
| Business audit value | 5 | "Check whether the reported stock change is even mathematically possible given known flows" is one of the sharpest, most generally reusable audit techniques in this entire ingest |
| Data/workflow value | 5 | A concrete, rigorous data-validation method directly applicable to any client data review |
| Reading urgency | 4 | High standalone value as both a teaching case and an immediately practicable audit tool |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Data-quality due-diligence tool — before accepting any client-reported decline (or increase) in a cumulative stock metric (backlog, defect count, customer base, accumulated debt), check whether the implied change is actually possible given the known, plausible inflow and outflow rates for that stock.

**Use when**:
A client presents a favorable trend in a cumulative metric that seems inconsistent with other available indicators, or when a reported change seems too large or too fast relative to what the known flow rates could plausibly produce.

**Do not use when**:
The metric in question is a genuine flow (not a stock) or the reporting period is short enough that simple measurement noise is a sufficient explanation — not every discrepancy needs a full stock-flow impossibility analysis.

**Fast retrieval query**:
`subject/data-quality` + `subject/stocks-and-flows` — or search "ever used cocaine population physically impossible" / "lifetime prevalence stock death rate" / "cocaine epidemic self-limiting" / "recent use confounds quitting with lying"
