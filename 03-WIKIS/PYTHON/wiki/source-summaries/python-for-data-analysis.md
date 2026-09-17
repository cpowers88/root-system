---
type: source-summary
timeline: reference
status: parked
source_role: spine (candidate — parked data-analysis strand)
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand, hub]
---

# Python for Data Analysis (Wes McKinney, 3rd ed.) — Source Summary

**Summary**: The core pandas reference for audit-tool-building work, now spanning the complete beginner-to-pandas on-ramp. Scoped ingest covering Chapter 5 (pandas fundamentals) through Chapter 10 (group operations), plus Chapters 2–4 (Python language basics/IPython/Jupyter, built-in data structures/functions/files, NumPy basics) added later as the beginner-programming on-ramp Chris requested — still deliberately excluding only Ch. 1 (motivational front matter), Ch. 11 (time series), Ch. 12 (modeling library intros), and the NumPy appendix.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed., O'Reilly)

**Last updated**: 2026-06-23

---

This page maps the pandas/matplotlib/seaborn pages (Ch. 5–10) plus the beginner Python fundamentals pages (Ch. 2) created from this book, organized by what problem each one solves rather than by chapter order.

## Beginner Python Fundamentals (Chapters 2–4)

- [[ipython-and-jupyter-basics]] — running Python via the interpreter, IPython shell, and Jupyter notebook; tab completion and `?` introspection
- The book's Ch. 2–3 beginner-Python pages (language semantics/scalar types, control flow, tuples/lists/slicing, dictionaries/sets, sequence functions/comprehensions, functions/namespaces/lambdas, generators/itertools/exceptions, file I/O) were **archived 2026-07-07** as duplicates of this vault's own curriculum. Equivalent coverage: [[stages/stage-01-python-atoms]], [[stages/stage-02-decisions-and-boolean-logic]], [[stages/stage-03-loops-and-repetition]], [[stages/stage-04-functions-parameters-return]], [[stages/stage-05-data-shapes]], [[stages/stage-06-files-errors-debugging]]. Archived originals: `99-ARCHIVE\ARCHIVED_2026-07-07_FORGE_technology_python_duplicates\`.
- [[numpy-ndarray-basics-and-dtypes]] — array creation, dtype/casting, vectorized arithmetic
- [[numpy-indexing-and-slicing]] — basic/Boolean/fancy indexing and the view-vs-copy distinction
- [[numpy-ufuncs-pseudorandom-and-vectorized-logic]] — universal functions, numpy.random, np.where
- [[numpy-statistical-methods-sorting-and-set-operations]] — aggregations with axis, sorting, set logic, npy/npz I/O
- [[numpy-linear-algebra-and-random-walk-case-study]] — matrix math and the full vectorization worked example

## Core Data Structures and Indexing

- [[pandas-series-dataframe-fundamentals]] — Series/DataFrame construction, Index objects, reindexing, the loc/iloc habit
- [[pandas-arithmetic-and-function-application]] — index-alignment in arithmetic, apply/applymap/map, sorting
- [[pandas-summary-stats-and-value-counts]] — describe(), reductions, correlation/covariance, value_counts(), isin()
- [[pandas-hierarchical-indexing]] — MultiIndex construction, partial indexing, stack/unstack, set_index/reset_index
- [[pandas-categorical-data-type]] — the Categorical dtype for memory/performance (lower priority)

## Loading and Storing Data

- [[reading-writing-csv-with-pandas]] — read_csv mechanics, chunked reading, to_csv, the csv module
- [[reading-excel-html-and-web-apis]] — Excel, HTML scraping, requests + JSON web APIs
- [[sqlite-and-sql-with-pandas]] — raw sqlite3 vs. SQLAlchemy + read_sql

## Cleaning and Transforming

- [[pandas-missing-data-and-duplicates]] — dropna/fillna strategies, duplicated/drop_duplicates
- [[pandas-transformation-binning-and-dummies]] — map/replace/rename, cut/qcut binning, outlier capping, get_dummies
- [[string-manipulation-and-regex-in-pandas]] — built-in string methods, regex, the NA-safe .str accessor

## Combining and Reshaping

- [[merging-datasets-with-merge-and-join]] — pandas.merge join types, merging on index, DataFrame.join
- [[pandas-concat-and-combine-first]] — stacking with concat, source-tagging via keys, combine_first
- [[reshaping-stack-unstack-pivot-melt]] — long-to-wide (pivot) and wide-to-long (melt)

## Visualization

- [[matplotlib-figures-axes-and-styling]] — Figure/Axes basics, styling, ticks/labels/legends, annotations, saving to file
- [[pandas-plotting-shortcuts-and-crosstab]] — the .plot accessor, bar/barh, pandas.crosstab
- [[seaborn-statistical-plots]] — barplot/histplot/regplot/pairplot/catplot — aggregation-aware charting

## Aggregation and Group Operations

- [[groupby-split-apply-combine-basics]] — the split-apply-combine model, grouping key types, iteration
- [[groupby-aggregation-with-agg]] — agg() for single/multiple/per-column aggregations
- [[groupby-apply-and-quantile-bucket-analysis]] — apply() for top-N-per-group, cut/qcut bucket analysis, group-specific fillna
- [[groupby-transform]] — transform() for same-shape group-relative results
- [[pivot-tables-and-cross-tabulation]] — pivot_table and crosstab — the report-ready summary table tools

## What Was Deliberately Skipped

- The "Extension Data Types" subsection (7.3) — too advanced/niche for current audit-tool needs.
- Group-wise linear regression and weighted-average/correlation worked examples (10.3, late) — illustrative statsmodels-dependent material, not core mechanics; the underlying `apply` pattern they demonstrate is already covered in [[groupby-apply-and-quantile-bucket-analysis]].
- Chapter 1 ("Preliminaries") — pure motivation/positioning (why Python, why not Python, installation), no actual beginner-programming content; skipped per Chris's explicit call. This is now the only chapter before Chapter 5 left uningested.
- Chapter 11 (time series — a `groupby` special case the book itself flags for separate treatment), Chapter 12 (scikit-learn/statsmodels modeling intro), and the NumPy-internals appendix — out of scope per Chris's chosen ingest boundary.

## Connects to

- [[reading-writing-csv-with-pandas]] / [[sqlite-and-sql-with-pandas]] — the data-loading layer that feeds everything else in this map.
- [[pivot-tables-and-cross-tabulation]] — the natural endpoint of most audit data pipelines built from this material: raw client export in, formatted summary table out.

## Source Identity

- Title: Python for Data Analysis, 3rd Ed.
- Author: Wes McKinney
- File: `raw/books/PythonforDataAnalysis.pdf`
- Type: book (data-analysis teaching/reference hybrid, O'Reilly)
- Ingest: FORGE pre-ingested Ch. 2-10 (2026-06-20/23). The Ch. 2-3 beginner-Python pages were archived 2026-07-07 as curriculum duplicates, leaving Ch. 2 (IPython/Jupyter) + Ch. 4-10 in this vault. Ch. 1, 11-12, and the NumPy appendix were never ingested.

## Best Use In This Vault

Candidate **spine** for a future "data analysis" strand extending Stages 9-10 (pandas/NumPy data manipulation, cleaning, merging, groupby aggregation, visualization) — the gap Automate the Boring Stuff leaves open. Until Chris approves that strand, this hub and its topic pages are lookup reference only.

## Difficulty Assessment

Post-Stage-9. Assumes fluency with data shapes ([[stages/stage-05-data-shapes]]), files ([[stages/stage-06-files-errors-debugging]]), and CSV/JSON handling (Stage 9). Not beginner material — the book's own beginner-Python chapters were archived 2026-07-07 as duplicates of this vault's Stages 1-6.

## Advanced Material To Park

Ch. 11 (time series), Ch. 12 (modeling/scikit-learn intro), the NumPy-internals appendix, and extension dtypes (section 7.3) — all already excluded from the ingest. Keep them out unless a concrete need appears.

## Recommended Placement In Learning Path

After Stage 9 mastery, as the spine of a Chris-approved data-analysis strand — see `wiki/source-map.md` ("Required Next Update") and [[parking-lot]] (pandas/NumPy rows). Do not fold into the active Stage 0-10 path.

## Notes For Future Claude

The topic pages under `wiki/source-summaries/` from this book are inventory, not curriculum. Building them into concept/glossary/drill/flashcard pages requires Chris's explicit go-ahead per the closed-intake rule in `wiki/source-map.md`.
