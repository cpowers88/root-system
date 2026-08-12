---
type: reference
timeline: later
tags: [school, econ-1000, macroeconomics, source-guide]
created: 2026-07-21
source_refs:
  - "raw/lesson--great-depression-introduction-essay-wheelock.pdf"
  - "raw/Consumer Price Index for All Urban Consumers All Items in U.S. City Average.md"
---

# ECON 1000 - Great Depression and CPI Reading Guide

## Purpose

This guide turns the two newly landed Federal Reserve sources into small,
just-in-time reading chunks for ECON 1000 Chapters 7-11. They are optional study
support, not confirmed assigned readings. The real Mathews and Patrono textbook,
professor guidance, and D2L modules remain authoritative.

## Source Authority and Limits

### CPIAUCSL clipping

- Primary data producer: U.S. Bureau of Labor Statistics.
- Distribution and graph interface: FRED, Federal Reserve Bank of St. Louis.
- Series: Consumer Price Index for All Urban Consumers, All Items, seasonally
  adjusted, monthly, reference base `1982-1984 = 100`.
- Population scope: the source says the measure represents roughly 88 percent of
  the U.S. population; it is not a cost-of-living measure for every household.
- The clipping's chart is transformed to percent change from a year ago. That view
  begins in 1948 because a year-over-year calculation needs twelve prior months.
  The local `CPIAUCSL.csv` stores index levels beginning in 1947.
- CPI includes volatile food and energy prices. The clipping names core CPI as a
  useful alternative for some inflation analysis; core CPI is not in the current
  local dataset set.

### Wheelock essay

- David C. Wheelock, Federal Reserve Bank of St. Louis, “The Great Depression: An
  Overview.” Four pages; visually checked after rendering on 2026-07-21.
- The essay is an introductory historical interpretation, not the course's assigned
  textbook. It emphasizes the monetary/banking explanation associated with Milton
  Friedman and Anna Schwartz while acknowledging that economists disagree.
- Several “present” comparisons were written years ago. Use the essay for causal
  structure and historical context, not for current federal-spending statistics.
- The local CPI series starts in 1947, so it cannot directly graph the Depression
  years discussed in the essay. Do not pretend the local CPI file proves the
  essay's 1929-1933 numerical claims.

## The Core Concept Skeleton

Read every chunk against this chain:

```text
shock or policy
    -> spending / lending / incentives change
    -> production and prices change
    -> employment and income change
    -> debt repayment and bank stability change
    -> government or central-bank response
    -> intended and unintended effects
```

For each arrow, ask whether the source is describing correlation, proposing a
causal mechanism, or presenting direct evidence. This is the critical-thinking
skill the course says its exams emphasize.

## Just-in-Time Reading Path

### Chunk 1 - CPI is a level; inflation is a rate

**Unlock:** Week 8, before Chapter 8 on inflation policy.

**Read:** the CPI clipping's chart description and Notes through the explanation of
seasonal adjustment.

**Anchor:** a price index is a measuring ruler. Inflation is how fast the reading on
that ruler changes; the index level itself is not “the inflation rate.”

**Know:**

- `CPIAUCSL` is an index level.
- Year-over-year inflation is approximately
  `(CPI this month / CPI 12 months earlier - 1) * 100`.
- A rising index normally means inflation; a falling index means deflation.
- Slower inflation means prices are still rising, just more slowly. It does not
  mean prices have fallen.

**Proof before moving on:** explain the difference among CPI level, inflation,
disinflation, and deflation without notes.

### Chunk 2 - Output, unemployment, and the scale of contraction

**Unlock:** Week 7, after the first Chapter 7 GDP lesson.

**Read:** Wheelock, page xi, opening through “What Caused the Great Depression?”

**Look for:** real output, unemployment, prices, bank failures, and the difference
between a dramatic event and a complete causal explanation.

**Do not memorize:** the grocery-price examples as isolated trivia. Use them to ask
why falling prices can coexist with severe hardship when income and employment are
also collapsing.

**Proof:** draw four boxes labeled output, employment, prices, and banks; state what
happened to each from 1929-1933 and why cheaper goods did not guarantee affordability.

### Chunk 3 - Money, banking, and deflation

**Unlock:** Week 8, after Chunk 1 and the Chapter 8 policy introduction.

**Read:** Wheelock, pages xii-xiii, “Money, Banking and Deflation” through the end of
the banking-panic explanation.

**Look for:** money stock, bank deposits, reserves, bank runs, loan contraction,
deflation, real debt burden, defaults, and the reinforcing feedback loop.

**Physical anchor:** a bank cannot keep every deposited dollar sitting idle and
also lend those dollars. Confidence normally prevents everyone from demanding cash
at once; a panic breaks that coordination.

**Proof:** reconstruct this loop from memory:

```text
withdrawals -> fewer reserves -> fewer loans/deposits -> smaller money stock
-> less spending -> lower output/prices/employment -> more defaults
-> weaker banks -> more withdrawals
```

Then identify where the loop can be interrupted.

### Chunk 4 - Recovery, institutions, and government action

**Unlock:** Week 10 or 11, alongside market failure and government failure.

**Read:** Wheelock, page xiii, “Recovery.”

**Sort every action into one of three columns:** restore confidence, provide relief,
or change market rules. Then record one intended effect and one possible unintended
effect.

**Interpretive caution:** the essay credits restored banking confidence while also
arguing that some New Deal policies may have slowed recovery. Treat this as a claim
to analyze, not a sentence to memorize as the only accepted explanation.

**Proof:** explain why “government acted” is not enough analysis. Name the policy,
mechanism, intended result, and possible tradeoff.

### Chunk 5 - Could it happen again?

**Unlock:** Week 14 final review, after Chapters 7-11 have been studied.

**Read:** Wheelock, pages xiii-xiv, “Could It Happen Again?”

**Look for:** lender-of-last-resort behavior, open-market purchases, deposit
insurance, price stability, debt deflation, and the distinction between preventing
all recessions and preventing an ordinary downturn from becoming a catastrophe.

**Proof:** give a two-minute explanation connecting GDP, unemployment, inflation or
deflation, banking stability, market failure, and government policy. Mark which
links come from the essay and which came from the course text or lecture.

## Data-Reading Path

Use the local files in `04-SCHOOL\04-ECON\datasets\` only for private
practice unless the instructor assigns them.

1. Open `CPIAUCSL.csv` and identify `date` and `value`.
2. State that `value` is an index level, not dollars and not an inflation percentage.
3. Compare a month with the same month one year earlier; predict whether the
   year-over-year inflation calculation is positive, negative, or near zero.
4. Calculate only after predicting.
5. Explain whether the result shows inflation, disinflation, or deflation.
6. Compare CPI movement with `UNRATE.csv` or `GDPC1.csv` only after stating that
   movement together does not by itself prove causation.

## Exam-Style Reading Frame

For any case-study question, use this skeleton before selecting an answer:

1. **Indicator:** What changed - output, prices, unemployment, lending, or income?
2. **Direction:** Did it rise, fall, accelerate, or decelerate?
3. **Mechanism:** What behavior or constraint connects cause to effect?
4. **Policy tool:** What institution can act, and how?
5. **Tradeoff:** What secondary effect or failure could result?
6. **Boundary:** What evidence would be needed before claiming causation?

## Connected Study Aids

- [[../glossary/macro-terms]]
- [[../flashcards/gdp-inflation-unemployment]]
- [[../drills/cpi-and-depression-reasoning]]
- [[../semester-map]]
- [[../../../course-briefs/fall-2026-course-briefs]]

## Sources

- `raw\lesson--great-depression-introduction-essay-wheelock.pdf`
- `raw\Consumer Price Index for All Urban Consumers All Items in U.S. City Average.md`
- `04-SCHOOL\04-ECON\datasets\README.md`
- `04-SCHOOL\04-ECON\datasets\CPIAUCSL.csv`
