---
domain: technology
type: concept
tags: [priority/later, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, subject/data-science, subject/statistics, stack/python]
---

# Statistical Distributions for Data Science: Normal, Long-Tailed, t, and Binomial

**Summary**: Which standard distribution actually fits a given real-world
variable, and the specific, common mistake of assuming "normal" when raw
data almost never is. Companion page to
[[estimates-of-location-and-variability]] from the same source and chapter.

**Sources**: PracticalStatisticsforDataScientists.pdf (Bruce, Bruce &
Gedeck, 2nd ed., O'Reilly, 2020), Chapter 2 ("Data and Sampling
Distributions") — Normal, Long-Tailed, Student's t, and Binomial
Distribution sections.

**Last updated**: 2026-07-13

---

## The Central Misconception

The normal distribution isn't called "normal" because most data follows it
— **most raw data does not**. Its outsized role in statistics comes from a
different fact: many *sample statistics* (means, sums, sample proportions)
turn out to be normally distributed even when the underlying raw data
isn't (the central limit theorem). Treat "assume normal" as a fallback for
when you lack an empirical or bootstrap distribution, not a default.

## Normal Distribution

68% of data within 1 standard deviation of the mean, 95% within 2 — the
familiar bell curve. **Z-score**: standardize a value by subtracting the
mean and dividing by the standard deviation. **QQ-plot**: the diagnostic
tool — plot a sample's sorted z-scores against the quantiles a true normal
distribution would produce; points falling on the diagonal line mean the
sample is close to normal, points curving away mean it isn't.

## Long-Tailed Distributions — the Actual Default

Most real data (stock returns, income, many business metrics) is **not**
normal — it has long tails, meaning extreme values occur far more often
than a normal-distribution assumption would predict. The book's Netflix
stock-return QQ-plot example: points close to the diagonal line near the
center ("normal in the middle") but curving sharply away at both ends —
exactly the "black swan" pattern Nassim Taleb's work is about. **Why this
matters practically**: assuming normality when the real distribution is
long-tailed systematically underestimates the frequency of extreme events
— a real risk in any forecast or risk estimate built on a normality
assumption without checking it first.

## Student's t-Distribution

A normal-shaped distribution with thicker, longer tails — used for the
distribution of *sample statistics* (especially sample means) rather than
raw data, particularly with smaller samples. The family of t-distributions
converges toward normal as sample size grows. Historical footnote worth
keeping: published in 1908 by a Guinness brewery statistician forced to
publish under the pseudonym "Student" because his employer didn't want
competitors to know it was using statistical methods. Practical takeaway
for a data scientist (the book's own verdict, not just historical color):
you don't need deep t-distribution theory — bootstrap resampling answers
most sampling-error questions directly — but t-statistics show up
constantly in software output (A/B tests, regression), so recognizing what
one means is necessary even if deriving one by hand isn't.

## Binomial Distribution

The distribution for yes/no outcomes: buy/don't buy, click/don't click,
convert/don't convert — exactly the shape of most business conversion
metrics. A binomial distribution answers "given probability *p* of success
per trial and *n* trials, what's the probability of exactly *x*
successes?" With large *n* and *p* not too close to 0 or 1, binomial
converges to normal — the practical reason normal-approximation shortcuts
work for large-sample conversion-rate questions.

## Key Ideas

- Check the actual shape of your data before assuming normal — long-tailed
  data is the norm, not the exception, in real business metrics.
- The t-distribution and normal distribution both matter mainly because
  *sample statistics* tend toward them even when raw data doesn't — not
  because raw data itself is well-modeled by either.
- Binomial is the distribution behind every conversion-rate / yes-no-metric
  question — directly relevant to the A/B testing content in
  [[ab-testing-hypothesis-tests-and-p-values]].

## Connects to

[[estimates-of-location-and-variability]] — same source, prerequisite
vocabulary (standard deviation feeds directly into z-scores here).
[[ab-testing-hypothesis-tests-and-p-values]] — binomial and t-distributions
are the mechanics underneath the hypothesis tests that page covers.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 2 | Background statistical literacy, not a direct deliverable |
| Current usefulness | 2 | Useful once real forecasting or risk-estimate work comes up |
| KSU support | 1 | Not coursework-related |
| Tech-stack relevance | 2 | Supports `scipy.stats` usage when it comes up |
| Business audit value | 3 | The long-tailed-data caution is a real, specific risk-estimate error to avoid making for a client |
| Data/workflow value | 2 | Reference-tier, not day-to-day |
| Reading urgency | 1 | No current project calls for this |

**Overall priority**: LATER (reference)

## Use / Retrieval Notes

**Use when**: Building any forecast, confidence interval, or risk estimate
and deciding whether a normality assumption is safe — check the actual
data's QQ-plot shape first, especially for anything financial (returns,
revenue swings) which is reliably long-tailed.

**Do not use when**: The question is really about summarizing a single
variable's center/spread — that's [[estimates-of-location-and-variability]].

**Fast retrieval query**: `subject/statistics` + `use-case/data-workflow`

## North Star Connection

Track relevance: Tech — the specific, nameable mistake ("assumed normal
when the data was long-tailed") is a credible-sounding but wrong forecast
or risk claim, exactly the kind of subtle error that damages audit
credibility if a client or their accountant catches it.
