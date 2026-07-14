---
domain: technology
type: concept
tags: [priority/later, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, subject/data-science, subject/statistics, stack/python]
---

# Estimates of Location and Variability

**Summary**: The vocabulary and formulas for summarizing a single variable —
where its "typical value" sits (location) and how spread out it is
(variability) — with the specific reasons each robust alternative to the
plain mean/standard deviation exists. This is inferential-statistics ground
truth underneath the ML-focused `data-science-ml/` pages already in this
wiki (which lean CRISP-DM/tree-induction/regression-mechanics from *Data
Science for Business*); this source fills the classical-statistics gap those
pages don't cover.

**Sources**: PracticalStatisticsforDataScientists.pdf (Bruce, Bruce & Gedeck,
2nd ed., O'Reilly, 2020), Chapter 1 ("Exploratory Data Analysis") —
"Estimates of Location" and "Estimates of Variability" sections.

**Last updated**: 2026-07-13

---

## Location: Where's the Center?

- **Mean** — sum divided by count. Easy, but sensitive to outliers.
- **Trimmed mean** — drop a fixed number/percent of extreme values at each
  end (commonly 10%), then average what's left. A genuine compromise: more
  robust than the mean, uses more data than the median. (Olympic diving
  drops the highest and lowest judge scores for the same reason — it makes
  the score harder for one biased judge to manipulate.)
- **Weighted mean** — used when some observations are intrinsically more
  reliable (downweight a noisy sensor) or when the sample doesn't
  proportionally represent the groups you care about (upweight an
  underrepresented group).
- **Median** — the middle sorted value. Depends only on the center of the
  sorted data, so it's untouched by how extreme the outliers are — the
  book's example: comparing average income in two Seattle neighborhoods,
  the mean gets wrecked by Bill Gates living in one of them; the median
  doesn't move.

**The core judgment call**: use the mean when you trust the data and want
every point to count; reach for median/trimmed mean the moment outliers or
data-entry errors are plausible — which, in an audit/consulting context
pulling numbers from a client's real books, is close to always.

## Variability: How Spread Out?

- **Variance / standard deviation** — average of squared deviations from
  the mean, then square-rooted back to the original units. Standard because
  the math is convenient (squared terms are easier to work with
  analytically than absolute values), not because it's the most intuitive
  measure.
- **Mean absolute deviation** — average of the *absolute* deviations from
  the mean. More intuitive, less mathematically convenient — rarely the
  default, but useful to know it exists.
- **Median absolute deviation (MAD)** — median of the absolute deviations
  *from the median*. The robust counterpart to standard deviation: not
  influenced by extreme values, the same way the median isn't.
- **Percentile-based estimates** — range (max − min, extremely sensitive to
  outliers) and interquartile range / IQR (75th percentile − 25th
  percentile, the standard robust spread measure — this is the box in a
  box plot).

**The n vs. n−1 aside** (degrees of freedom): dividing by n underestimates
the true population variance (a biased estimate); dividing by n−1 corrects
it. Doesn't matter in practice once n is reasonably large — worth knowing
why the formula looks that way, not worth losing sleep over.

## Key Ideas

- Every "typical value" or "spread" metric is a *choice*, not a fact about
  the data — mean vs. median, standard deviation vs. MAD each trade off
  sensitivity-to-real-signal against sensitivity-to-outliers/errors.
- Robust metrics (median, trimmed mean, MAD, IQR) exist specifically to
  survive small data sets, extreme values, and dirty real-world data — the
  default condition of client data in an audit engagement, not the
  exception.
- The vocabulary here (deviation, variance, standard deviation, percentile,
  IQR) is the shared language every downstream statistical/ML technique in
  this wiki builds on — worth being fluent in before touching hypothesis
  testing or regression diagnostics.

## Connects to

[[tree-induction-and-decision-boundaries]],
[[linear-regression-least-squares-and-logistic-regression]],
[[generalization-overfitting-and-fitting-graphs]] — those pages assume this
vocabulary; this page is the prerequisite layer, not a replacement.
[[ab-testing-hypothesis-tests-and-p-values]] — the next page in this same
ingest, which uses standard deviation and the normal/t-distributions built
on these estimates directly.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | Foundational vocabulary, not a client-facing deliverable itself |
| Current usefulness | 3 | Directly usable any time real client data needs summarizing honestly |
| KSU support | 1 | Not coursework-related |
| Tech-stack relevance | 3 | Underlies every pandas `.describe()` / `.median()` call already in daily use |
| Business audit value | 4 | Robust-vs-mean judgment calls are exactly what separates a credible audit finding from a skewed one |
| Data/workflow value | 4 | Prerequisite fluency for any client data-cleaning or reporting work |
| Reading urgency | 2 | Reference material — read on demand, not sequentially |

**Overall priority**: LATER (reference)

## Use / Retrieval Notes

**Use when**: Summarizing a client's numbers for a report and deciding
whether "average" should mean mean, median, or trimmed mean — especially
when the data plausibly contains outliers (one huge invoice, a data-entry
typo, a one-off bad month).

**Do not use when**: The task is building a predictive model — that's
[[tree-induction-and-decision-boundaries]] and the linear/logistic
regression pages, not this one.

**Fast retrieval query**: `subject/statistics` + `use-case/data-workflow`

## North Star Connection

Direct audit-credibility lever: choosing the right location/variability
estimate for a client's real (often dirty) numbers is the difference between
a defensible finding and one that collapses under one outlier data point.
Track relevance: Tech — statistical literacy underneath every data-driven
audit claim.
