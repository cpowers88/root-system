---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# pandas groupby: transform() — Group Results Broadcast Back to Row Shape

**Summary**: `transform` is a constrained sibling of `apply` ([[groupby-apply-and-quantile-bucket-analysis]]): instead of producing one summary row per group, it returns a result the **same shape** as the original data — each row gets its own group's computed value attached back to it. This is the tool for "add a column showing each row's group average next to the original row" rather than collapsing to a summary table.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 10 ("Data Aggregation and Group Operations"), section 10.4 ("Group Transforms and 'Unwrapped' GroupBys")

**Last updated**: 2026-06-20

---

## The Three Things transform() Is Allowed to Do

1. Produce a scalar value that gets broadcast to every row in the group.
2. Produce an object the same shape as the input group.
3. It must **not** mutate its input.

```python
g = df.groupby("key")["value"]
g.transform("mean")              # built-in by name — every row gets its OWN group's mean, not a 1-row-per-group summary
g.transform(lambda x: x.mean())  # equivalent custom version
g.transform(lambda x: x * 2)     # same-shape transform — each value doubled, group membership irrelevant to shape
```

**Key contrast with apply**: `g.apply(lambda x: x.mean())` returns one row per group (a summary); `g.transform("mean")` returns one row per *original row*, each filled with its group's mean — same length as the input.

## Group-Relative Normalization (z-score within group)

```python
def normalize(x):
    return (x - x.mean()) / x.std()

g.transform(normalize)   # or g.apply(normalize) — both give the same result here
```

**Audit-usable pattern**: this is the standard move for "how far above/below this site's own average is this particular job" — a normalized score relative to the *group*, not the whole dataset, which is usually the fairer comparison when sites or crews differ systematically in scale.

## The "Unwrapped" Pattern — Faster Than a Custom Function

Built-in aggregation names (`"mean"`, `"std"`, `"sum"`) have an optimized fast path through `transform`. Composing several of these directly is often faster than writing one combined custom function:

```python
normalized = (df["value"] - g.transform("mean")) / g.transform("std")
```

This produces the identical result to the `normalize` function above, just built from named built-ins applied separately and combined with plain arithmetic afterward — worth reaching for once a custom `apply`/`transform` function turns out slow on a large dataset.

## Connects to

- [[groupby-apply-and-quantile-bucket-analysis]] — `apply` is the general tool; `transform` is the narrower, faster tool for the specific case of "same-shape result broadcast back to every row."
- [[groupby-aggregation-with-agg]] — the named string aliases (`"mean"`, `"sum"`) work identically in `agg` and `transform`; the difference is purely in the output shape (one row per group vs. one row per original row).

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
