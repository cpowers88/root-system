---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [reference, programming, parked, sql-strand]
---

# Practical SQL: Statistical Functions in SQL

**Summary**: SQL's built-in statistical toolkit — correlation (`corr(Y, X)`), linear regression (`regr_slope`/`regr_intercept`/`regr_r2`), variance/standard deviation, window functions for ranking (`rank()`/`dense_rank()`/`PARTITION BY`), rate calculations for fair comparisons, and rolling averages/sums for smoothing time-series data — all demonstrated on US Census ACS education/income data and federal export data.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 11 ("Statistical Functions in SQL")

**Last updated**: 2026-06-20

---

## Correlation with corr(Y, X)

The **Pearson correlation coefficient** (`r`) measures the strength and direction of a *linear* relationship between two variables, ranging from -1 (perfect inverse) to 1 (perfect direct), with values near 0 indicating little to no linear relationship. A rough interpretation scale: 0 = none, .01–.29 = weak, .3–.59 = moderate, .6–.99 = strong, 1 = perfect. SQL's `corr(Y, X)` (a *binary aggregate function*, taking two column inputs) computes it directly — demonstrated finding `r = 0.70` between a county's percentage with a bachelor's degree and median household income (a fairly strong direct relationship), versus near-zero correlations between income and long commute times. **Two critical caveats apply to any correlation finding: correlation does not imply causation, and results should be checked for statistical significance before being treated as conclusive** — both beyond this chapter's scope but essential before using a correlation in a report.

## Predicting Values with Linear Regression

Linear regression finds the "best fit" straight line (`Y = bX + a`) describing the relationship between an independent variable `X` and dependent variable `Y`, letting you predict a `Y` value for an `X` you haven't observed. `regr_slope(Y, X)` returns the line's slope (`b`); `regr_intercept(Y, X)` returns where the line crosses the y-axis (`a`). Applied to the education/income data: slope = 1016.55, intercept = 29651.42 — meaning each one-point increase in bachelor's-degree percentage predicts roughly a $1,017 increase in median household income, and a county with 0% bachelor's degree would be predicted at ~$29,651. Plugging X=30 into the formula predicts ~$60,148 median income for a county where 30% of the population holds a bachelor's degree or higher.

`regr_r2(Y, X)` computes the **coefficient of determination (r-squared)** — the square of `r`, expressing the percentage of variation in the dependent variable explained by the independent variable. The education/income r-squared was 0.490: **about 49% of the variation in county median income is explained by bachelor's-degree attainment alone; the remaining 51% comes from other factors** (e.g., local job mix) not captured by this one variable.

## Variance and Standard Deviation

**Variance** is the average squared distance of each value from the mean — larger variance means more dispersion/volatility (a finance use case: measuring a stock's daily price volatility). **Standard deviation** is variance's square root, and is most interpretable for normally distributed ("bell curve") data: roughly two-thirds of values fall within one standard deviation of the mean, ~95% within two. Standard deviation is expressed in the data's own units; variance is not (it's on its own larger scale). Four functions: `var_pop()`/`var_samp()` (variance for a complete population vs. a sampled subset) and `stddev_pop()`/`stddev_samp()` (the corresponding standard deviations) — choosing population vs. sample depends on whether the dataset contains every possible value or only a survey sample of them.

## Ranking with Window Functions

`rank()` and `dense_rank()` are **window functions** — unlike aggregate functions (which collapse multiple rows into one), a window function first generates the full result set, then computes a value relative to each row without collapsing anything. Syntax: `rank() OVER (ORDER BY column DESC)`. **The difference is how ties are handled**: `rank()` leaves a gap in the numbering after a tie (if two rows tie for 3rd, the next row is 5th), while `dense_rank()` does not (the next row is 4th). The author recommends `rank()` as the default, since it accurately reflects how many rows actually outrank the current one.

`PARTITION BY column` added inside the `OVER` clause divides the ranking into independent subgroups — e.g., `rank() OVER (PARTITION BY category ORDER BY unit_sales DESC)` ranks each store's sales *within* its own product category rather than across all categories combined. This is the general pattern for "rank X within each Y" questions (top vehicle complaints per manufacturer, top scorer per team, etc.).

## Calculating Rates for Meaningful Comparisons

**Raw counts mislead whenever the underlying populations differ in size** — Texas had far more births than Utah in 2019, but Utah's per-capita *fertility rate* (births per 1,000 women aged 15-44) was actually higher. The standard fix: convert a count to a rate per a fixed base (per 1,000, per 100,000, etc.) — `(count / population) * 1000`. Demonstrated joining Census population estimates with County Business Patterns "Accommodation and Food Services" establishment counts to compute tourism-business density per 1,000 residents (`(establishments::numeric / population) * 1000`), filtered to counties with 50,000+ population for a fair comparison — the top results (Cape May NJ, Worcester MD, Monroe FL) were all recognizable beach/tourism destinations, confirming the metric captured something real.

## Smoothing Uneven Data with Rolling Averages and Sums

A **rolling (moving) average** computes the average over a sliding window of the most recent N periods, recalculated for every row — useful for revealing a trend obscured by day-to-day or month-to-month noise. Syntax: `avg(column) OVER (ORDER BY date_columns ROWS BETWEEN n-1 PRECEDING AND CURRENT ROW)` — `ROWS BETWEEN 11 PRECEDING AND CURRENT ROW` produces a 12-period (e.g., 12-month) window including the current row. Demonstrated on US monthly citrus export values, which spike sharply every winter and crash every summer: the raw monthly series is too spiky to read a multi-year trend from, but the 12-month rolling average revealed a clear pattern — exports were steady through 2018, declined through 2019, then partially recovered in 2020. **`sum()` can substitute for `avg()` in the same window-function pattern to get a rolling total instead** (e.g., a trailing 7-day or 12-month total). **A critical caveat: rolling calculations operate on row count, not actual calendar gaps** — a missing month in the data will silently turn a "12-month" window into an 11-month window covering 13 calendar months, distorting the result.

## Key Takeaways

- `corr(Y, X)` and `regr_r2(Y, X)` together answer "is there a relationship, and how much does it explain" — but neither proves causation, and both should be paired with the underlying scatterplot before trusting the number.
- Window functions (`rank()`, `dense_rank()`, and aggregate functions used with `OVER`) compute a per-row result without collapsing the result set — the tool for "rank within a group" and "rolling average/sum" problems that a plain `GROUP BY` can't express.
- Always convert raw counts to a rate (per 1,000, per capita, etc.) before comparing across groups of different sizes — a raw-count ranking can be actively misleading.
- Rolling averages/sums assume no gaps in the underlying time series — verify there are no missing periods before trusting a "12-month" or "7-day" window's stated coverage.

## Connects to

- [[sql-basic-math-and-stats]] — corr/regression/variance extend Chapter 6's average/median/percentile toolkit into genuinely statistical territory; the average-vs-median caution there parallels the "correlation isn't causation" caution here.
- [[sql-grouping-and-aggregate-functions]] — PARTITION BY-based ranking is the window-function counterpart to Chapter 9's GROUP BY-based per-category aggregation; both answer "how does X break down by category," but ranking preserves row-level detail that GROUP BY collapses.
- [[sql-joining-tables-and-relationships]] — the tourism-business-rate calculation reuses the multi-table JOIN pattern (Census population + County Business Patterns establishment counts) directly from Chapter 7.

## Pathway Placement

- **Role**: reference for the parked **SQL-fundamentals strand** (candidate Stage 10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s databases intro ([[concepts/databases-and-sqlite]]).
- **Caution**: this book's examples are PostgreSQL; the vault's Stage 10 path uses SQLite. Core syntax overlaps, but PostgreSQL-specific pieces (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, pgAdmin workflow) do not transfer 1:1.
- **Status**: parked per [[parking-lot]]. Not part of the active Stage 0-10 path — wait for Chris's go-ahead to build the strand.
