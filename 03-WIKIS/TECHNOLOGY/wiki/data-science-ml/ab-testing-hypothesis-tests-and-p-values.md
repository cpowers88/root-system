---
domain: technology
type: concept
tags: [subject/data-science, subject/statistics]
timeline: now
status: wiki-only
source_role: primary
use_cases: [data-workflow, business-model, audit]
stack: [python]
---

# A/B Testing, Hypothesis Tests, and p-Values

**Summary**: How to actually run and correctly interpret an experiment
comparing two options (two prices, two ad creatives, two process changes)
— including the single most common misreading of a p-value, which the
American Statistical Association issued a formal caution about in 2016.
Directly practical for an audit business measuring whether a recommended
change actually worked.

**Sources**: PracticalStatisticsforDataScientists.pdf (Bruce, Bruce &
Gedeck, 2nd ed., O'Reilly, 2020), Chapter 3 ("Statistical Experiments and
Significance Testing") — A/B Testing, Hypothesis Tests, and Statistical
Significance/p-Values sections.

**Last updated**: 2026-07-13

---

## A/B Testing — the Structure

Two groups, one **treatment** (the new price, the new ad, the new
process), one **control** (the existing standard, or nothing). Subjects
(customers, web visitors, transactions) get **randomized** — assigned to
one group or the other by chance, not by choice — so any observed
difference in outcome is attributable to the treatment rather than to some
pre-existing difference between the groups. Classic uses: two prices to
see which yields more net profit, two web headlines to see which gets more
clicks, two process changes to see which actually reduces the metric it's
meant to fix.

**Why have a control group at all?** Because without one, you can't tell
whether a result reflects the treatment or just normal variation over
time. A "before vs. after" comparison with no control confounds the
treatment with everything else that changed in the interim (season, market
conditions, a different set of customers).

## Hypothesis Tests — the Formal Version

The **null hypothesis** is the default assumption: no real difference
between treatment and control — any observed gap is just chance/random
variation. The **alternative hypothesis** is what you're actually trying
to show (the new price does better). A hypothesis test asks: is the
observed difference bigger than what random chance alone would plausibly
produce?

## The p-Value — What It Actually Means (and What It Doesn't)

**Correct definition**: the probability that, *given the null hypothesis
is true*, you'd see a result at least this extreme purely by chance.

**The near-universal misreading** (the book quotes this directly as the
wrong interpretation many people — including journal editors — actually
use): "the probability that the result is due to chance." That is **not**
what a p-value measures. The difference is subtle but real: a p-value
doesn't tell you the probability your hypothesis is true; it tells you how
surprising your data would be *if* the null hypothesis were true.

**Alpha**: the threshold set *in advance* (commonly 5% or 1%) below which
a result is called "statistically significant." Choosing 5% is an
arbitrary convention, not a guarantee of being right 95% of the time.

**The ASA's 2016 formal caution** (worth citing directly in any client-
facing analysis that leans on p-values) — six principles:
1. P-values indicate how incompatible data are with a specified model.
2. They do **not** measure the probability a hypothesis is true, or that
   results are due to random chance alone.
3. Decisions shouldn't rest on a p-value threshold alone.
4. Proper inference requires full reporting and transparency.
5. A p-value doesn't measure effect size or practical importance.
6. By itself, a p-value is not a good measure of evidence for or against a
   model.

**Why this matters for audit/consulting work specifically**: a client (or
their accountant) citing "statistically significant, p<0.05" as proof a
change worked is exactly the overclaim the ASA is warning against — a
small, practically meaningless improvement can still hit p<0.05 with
enough data, and a real, valuable improvement can fail to hit significance
with too little data. Report the actual effect size and confidence
interval alongside the p-value, not the p-value alone.

## Key Ideas

- Randomization into treatment/control is what makes an A/B test's result
  attributable to the treatment — without it, you have a before/after
  comparison confounded by everything else that changed.
- A p-value answers "how surprising is this result if nothing real is
  happening" — not "what's the probability something real is happening."
  Getting this backward is the single most common statistical
  misinterpretation in business reporting.
- Statistical significance (p < alpha) is not the same question as
  practical significance (is the effect big enough to matter) — always
  report both.

## Connects to

[[estimates-of-location-and-variability]],
[[statistical-distributions-normal-long-tailed-t-and-binomial]] — same
source; standard deviation and the binomial/t-distributions are the
mechanics a p-value calculation runs on.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Directly usable for validating whether an audit recommendation actually worked |
| Current usefulness | 3 | Ready to use whenever a client engagement needs to measure a before/after change |
| KSU support | 1 | Not coursework-related |
| Tech-stack relevance | 3 | Supports `scipy.stats` A/B-test and significance-testing code |
| Business audit value | 5 | The exact statistical rigor that separates a credible "this recommendation worked" claim from an anecdote |
| Data/workflow value | 4 | Directly reusable for any client process-change or pricing-test measurement |
| Reading urgency | 2 | Reference — read when a real A/B/experiment question comes up |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Use when**: A client wants to know whether a change (price, process,
marketing) actually worked, or when reporting the result of any test/
experiment to a client — cite effect size and confidence interval, not
just "it was significant."

**Do not use when**: There's no control/comparison group at all — that's
not an A/B test, and a p-value computed without one doesn't mean what it
would in a proper experiment.

**Fast retrieval query**: `subject/statistics` + `use-case/audit`

## North Star Connection

How this applies to the audit business: this is the rigor layer behind any
"we recommended X and it improved Y" claim — the exact kind of statistical
literacy that turns an audit finding from an anecdote into a defensible,
citable result. Track relevance: Tech + Business audit credibility.
Possible future Second Brain use: yes — a reusable "how to measure whether
a recommendation worked" checklist for client engagements.
