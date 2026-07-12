---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# NumPy Universal Functions, Pseudorandom Generation, and Vectorized Conditional Logic

**Summary**: Universal functions (ufuncs) for fast element-wise array math, the `numpy.random` module for generating array-shaped random data, and `numpy.where` as the vectorized replacement for an if/else loop over array elements.

**Sources**: PythonforDataAnalysis.pdf, Chapter 4 ("NumPy Basics: Arrays and Vectorized Computation"), sections 4.2-4.4

**Last updated**: 2026-06-23

---

## Universal functions (ufuncs)

A **ufunc** performs a fast, vectorized, element-wise operation on an ndarray — conceptually a wrapper around a simple scalar-in/scalar-out function, applied to every element at once instead of via an explicit loop.

- **Unary ufuncs** (one array in): `np.sqrt(arr)`, `np.exp(arr)`, plus `abs`, `square`, `log`/`log10`/`log2`, `sign`, `ceil`/`floor`/`rint`, `isnan`, `isfinite`/`isinf`, the trig functions, and `logical_not`.
- **Binary ufuncs** (two arrays in): `np.add`, `np.maximum` (element-wise max between two arrays — not the same as `arr.max()`, which reduces to a single value), `subtract`, `multiply`, `divide`/`floor_divide`, `power`, `mod`, and the comparison ufuncs (`greater`, `equal`, etc. — equivalent to `>`, `==`, and so on).
- A few ufuncs return **multiple arrays**: `np.modf(arr)` is the vectorized version of `math.modf`, splitting a float array into its fractional and integer parts as two separate output arrays.
- Ufuncs accept an optional **`out=`** argument to write results into an existing array instead of allocating a new one — a memory-efficiency option for large arrays (`np.add(arr, 1, out=existing_array)`).

## Pseudorandom number generation

`numpy.random` supplements the built-in `random` module with functions that generate a whole **array** of samples in one call, rather than one value at a time — and it's dramatically faster for this: the source's own benchmark shows it roughly 50x faster than the equivalent loop over `random.normalvariate`. `np.random.standard_normal(size=(4, 4))` draws a 4x4 array from the standard normal distribution.

These are **pseudorandom**, not truly random — a deterministic generator seeded with an initial state. The recommended modern pattern is an explicit, isolated generator object: `rng = np.random.default_rng(seed=12345)`, then `rng.standard_normal(...)`. This isolates your random draws from any other code that might also be using the shared global `numpy.random` state, and makes results reproducible given the same seed. Other generator methods include `permutation`, `shuffle`, `uniform`, `integers` (random integers in a range), `binomial`, `normal`, `beta`, `chisquare`, and `gamma`.

## Array-oriented (vectorized) conditional logic

`numpy.where(condition, x, y)` is the vectorized form of the ternary expression `x if condition else y`, applied element-wise across whole arrays:

```python
result = np.where(cond, xarr, yarr)
```

The equivalent written as a list comprehension (`[(x if c else y) for x, y, c in zip(xarr, yarr, cond)]`) has two real problems the source calls out explicitly: it's slow on large arrays (all the work happens in interpreted Python), and it doesn't generalize to multidimensional arrays at all. `np.where` solves both. Either or both of the `x`/`y` arguments can be a scalar instead of an array — a common real pattern is replacing all values matching a condition with a constant while leaving the rest untouched: `np.where(arr > 0, 2, arr)` sets every positive value to 2 and leaves negatives as they were.

## Key Ideas

- Reach for a ufunc instead of a Python loop any time the same scalar operation needs to apply to every element of an array — this is the literal definition of "vectorize this."
- `np.random.default_rng(seed=...)` (an explicit, seeded generator object) is the modern recommended pattern over calling functions on the bare `numpy.random` module directly — it's both reproducible and isolated from other code's random state.
- `np.where` is the go-to tool the moment a per-element if/else inside a Python loop starts feeling slow or won't generalize past one dimension.

## Operational Use

`np.where` is the standard, fast pattern for any "replace value X with Y based on a condition, otherwise leave it" cleaning rule on a numeric column or array — a near-universal client-data cleaning need (e.g., capping outliers, recoding a sentinel value). A seeded `default_rng` generator is the right tool any time an audit deliverable needs reproducible sample data for a demo, a Monte Carlo estimate, or a synthetic dataset to illustrate a methodology to a client without using their real (possibly sensitive) numbers.

## Connects to

- [[numpy-ndarray-basics-and-dtypes]] — ufuncs operate on the dtype'd arrays introduced there.
- [[numpy-indexing-and-slicing]] — `np.where`'s condition argument is itself a Boolean array, built the same way as in Boolean indexing.
- [[numpy-statistical-methods-sorting-and-set-operations]] — the aggregation methods (`sum`, `mean`) covered there are themselves implemented as reductions over ufuncs.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** — the NumPy layer underneath pandas (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, indexing, slicing) and [[stages/stage-04-functions-parameters-return]].
- **Status**: parked per [[parking-lot]] (NumPy row). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
