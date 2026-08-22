---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [programming, sql-strand]
---

# Practical SQL: Basic Math and Stats with SQL

**Summary**: SQL's arithmetic operators and their type-coercion rules, row-by-row column math (with a self-checking pattern for validating an import), percentage-of-whole and percent-change formulas, and the core aggregate functions (`sum()`, `avg()`, `percentile_cont()`/`percentile_disc()` for median/quartiles, `mode()`) — applied throughout to the Census county population data imported in Chapter 5.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 6 ("Basic Math and Stats with SQL")

**Last updated**: 2026-06-20

---

## Operators and Type Coercion

Nine operators: `+ - * /` (ANSI standard), `%` modulo, `^` exponentiation, `|/` square root, `||/` cube root, `!` factorial (PostgreSQL-specific; `!` removed in PostgreSQL 14+, use `factorial(n)`). Result type follows fixed rules: **two integers return an integer** (division truncates — `11 / 6` returns `1`, dropping the remainder, not `1.833`); **a `numeric` on either side returns `numeric`**; **any floating-point operand returns `double precision`**. To force true decimal division between integers, cast one operand: `CAST(11 AS numeric(3,1)) / 6` or `11.0 / 6`. `%` (modulo) returns just the remainder and doubles as a parity test (`value % 2 = 0` means even). **Operator precedence follows standard math convention**: exponents/roots first, then multiplication/division/modulo, then addition/subtraction — parenthesize explicitly whenever the intended order differs.

## Row-Wise Math and a Self-Check Pattern

`SELECT births_2019 - deaths_2019 AS natural_increase FROM ...` performs the calculation independently on every row. **Aliasing computed columns with `AS` is necessary** — an unlabeled expression displays as the unhelpful `?column?` header.

A reusable **data-validation pattern**: when a dataset's components should sum to a known total (e.g., 2019 population estimate = 2018 estimate + births − deaths + migration + residual), compute both the official total and your own recomputed total in the same query, then subtract one from the other into a `difference` column, sorted descending. **Any nonzero value in that column flags either an import error or a misunderstood column definition** — a fast, automatable way to confirm a large import is intact without manually re-checking thousands of rows.

## Percentages and Percent Change

**Percentage of whole**: `part / total * 100`. Demonstrated finding what fraction of each county's land area is water (`area_water::numeric / (area_land + area_water) * 100`) — **casting at least one operand to `numeric` is required**, since dividing two raw integers truncates to `0` before the multiplication ever happens. Sorting this metric surfaced a real anomaly worth knowing as a sanity-check habit: Michigan's Keweenaw County is "90% water" because the Census includes the surrounding Great Lake surface in county area — an apparent data oddity that turned out to be a legitimate, explainable fact, not an error.

**Percent change**: `(new_number - old_number) / old_number`, multiplied by 100 for a percentage. `round(expression, decimal_places)` cleans up display precision — both arguments combine to determine the type and rounding of the output.

## Aggregate Functions: Sum, Average, Median, Mode

`sum()` and `avg()` collapse an entire column into a single value (e.g., total and average county population across all 3,142 rows). **Average is misleading whenever outliers exist** — illustrated by a field-trip-ages example where one 46-year-old chaperone pulls the average age from 10.8 to 15.9, while the **median** (the literal middle value in sorted order, or the average of the two middle values for an even count) stays representative at 11. **The rule of thumb: compute both average and median — if they're close, the data is roughly normally distributed and the average is trustworthy; if they're far apart, prefer the median.** Applied to the full Census dataset: average county population was 104,468 but the median was only 25,726 — meaning more than half of US counties have fewer than 26,000 people, a fact the average alone completely obscures (driven by 40+ counties over a million and LA County over 10 million).

PostgreSQL has no built-in `median()` function (and the SQL standard doesn't define one either) — instead, **`percentile_cont(.5) WITHIN GROUP (ORDER BY column)`** computes the 50th percentile as a continuous (interpolated) value, exactly equivalent to a median. `percentile_disc(n)` is the discrete counterpart, rounding to an actual value present in the dataset rather than interpolating — **`percentile_cont` is the correct choice whenever an actual median is wanted.** Passing an array of cut points (`percentile_cont(ARRAY[.25,.5,.75])`) computes quartiles in one call, returned as a PostgreSQL array (`{...}`); `unnest()` converts that array into separate rows for easier reading. `mode() WITHIN GROUP (ORDER BY column)` (PostgreSQL-specific) finds the single most frequently occurring value.

## Key Takeaways

- Integer division truncates the remainder; cast to numeric or use a decimal literal to force a true fractional result.
- Build a "recompute the known total, subtract, sort descending" self-check into any nontrivial import — it surfaces data-quality problems automatically rather than requiring manual spot-checks.
- Average and median answer different questions — always compute both for skewed data (population, income, salaries, real estate) and prefer the median whenever they diverge meaningfully.
- percentile_cont(.5) is PostgreSQL's median function; there's no dedicated median() built-in.

## Connects to

- [[sql-import-export-data]] — the self-check validation pattern is the natural next step after any COPY import, directly using the Census table loaded there.
- [[sql-data-types]] — the integer-truncation and casting behavior here is a direct consequence of the type-coercion rules covered in Chapter 4.
- Profit First's "instant assessment" idea (business material that stayed with the FORGE split — route via `03-WIKIS\BUSINESS`) — the average-vs-median distinction parallels its caution about a single aggregate metric (Top Line Revenue) misrepresenting a business's real financial picture; both argue for a second, outlier-resistant metric before drawing conclusions.

## Pathway Placement

- **Role**: reference for the parked **SQL-fundamentals strand** (candidate Stage 10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s databases intro ([[concepts/databases-and-sqlite]]).
- **Caution**: this book's examples are PostgreSQL; the vault's Stage 10 path uses SQLite. Core syntax overlaps, but PostgreSQL-specific pieces (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, pgAdmin workflow) do not transfer 1:1.
- **Status**: parked per [[parking-lot]]. Not part of the active Stage 0-10 path — wait for Chris's go-ahead to build the strand.
