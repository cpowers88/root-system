---
type: research
tags: [technology, landscape, category-5, data-science-ml, vs-code]
source: raw/Data Wrangler - Visual Studio Marketplace.md (Microsoft, captured 2026-06-13); raw/co.md (Edit CSV extension, VS Marketplace, captured 2026-06-13, misnamed by the clipper — actual title "Edit CSV - Visual Studio Marketplace"); raw/Data Science in VS Code tutorial.md (Microsoft Learn, captured 2026-06-14)
---

# VS Code Data Tooling: Data Wrangler, Edit CSV, and the Titanic Tutorial

**Summary**: Two free VS Code extensions plus Microsoft's own worked
tutorial, together forming a complete free-tier data-cleaning-to-model
pipeline inside the editor Chris already uses for Python work. Directly
supports the applied-reference `data-science-ml/` folder already in this
wiki (CRISP-DM, tree induction, cross-validation) by giving it a concrete
tool layer — those pages teach the concepts; this page is where to
practice them.

## Data Wrangler (Microsoft, free, 2.1M+ installs)

A data viewing/cleaning UI built into VS Code and Jupyter notebooks.
Launches from a CSV/Parquet/Excel/Jsonl file or directly from a pandas
DataFrame in a notebook cell. Two modes: **Viewing** (filter/sort/column
statistics — fast initial exploration) and **Editing** (apply
transformations through a UI; every click generates the equivalent pandas
code, shown live and exportable back into the notebook). Concretely: pick
"Fill Missing Values" from the Operations panel, preview the diff, and
Data Wrangler writes the `df.fillna(...)` line for you — a genuinely
useful bridge from "I don't remember the exact pandas syntax" to a
correct, inspectable line of code, not just a black-box UI action.

## Edit CSV (janisdd, free, 2.4M+ installs)

Lighter-weight: an Excel-like table editor for `.csv`/`.tsv` files
directly in VS Code, one-way (editor → source file). No code generation —
this is for quick manual edits to a data file, not a pandas-learning tool.
Complementary to Data Wrangler, not competing: reach for this when the
task is "fix three bad rows by hand," reach for Data Wrangler when the
task is "write the transformation logic."

## Data Science in VS Code Tutorial (Microsoft Learn)

A complete worked example using the classic Titanic dataset: environment
setup (Anaconda/pip) → load data with pandas → clean it (replace `?`
placeholders with `NaN`, fix dtypes) → visualize with seaborn/matplotlib →
compute correlations → engineer a feature (`relatives` from `sibsp` +
`parch`) → train/test split with scikit-learn → Naive Bayes classifier
(~75% accuracy) → optional Keras/TensorFlow neural network (~79%
accuracy). This is the same CRISP-DM shape (business understanding → data
prep → modeling → evaluation) already documented conceptually in
[[data-science-ml/crisp-dm-process-and-data-leakage]] — this tutorial is a
literal runnable instance of that process, useful as a first hands-on rep
once Python fundamentals are further along.

## Use / Retrieval Notes

**Use when**: A client engagement or personal project needs a quick data
clean-up or a first predictive-model prototype, and the data already fits
in a CSV/pandas DataFrame — no need to reach for a heavier ML platform.

**Do not use when**: Coursework is still Python Stage 0-4 (per
`03-WIKIS\PYTHON\wiki\current-position.md`) — this tutorial assumes
working pandas/scikit-learn fluency; premature relative to current stage,
same caution [[data-science-ml/]] itself already carries in this wiki's
July 7 alignment pass.

## Connects to

[[data-science-ml/crisp-dm-process-and-data-leakage]],
[[data-science-ml/holdout-cross-validation-and-learning-curves]],
[[data-science-ml/generalization-overfitting-and-fitting-graphs]] — the
tutorial is a concrete instance of concepts those pages cover abstractly.

## North Star Connection

`TECHNOLOGY_LIBRARY_STRATEGY.md` Category 5 (Data Storage & Retrieval) —
"the spreadsheet became the database" — Data Wrangler/Edit CSV are the
free-tier tools for exactly that failure mode before anything heavier
(Airtable, SQLite, Postgres) gets recommended. Also feeds the Python
track's eventual Stage 9-10 (automation bridge / application thinking)
once Chris reaches CSV/spreadsheet-processing material.
