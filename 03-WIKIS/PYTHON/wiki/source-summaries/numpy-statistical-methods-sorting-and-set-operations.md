---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# NumPy Statistical Methods, Sorting, Set Operations, and File I/O

**Summary**: Array-wide and per-axis aggregation methods (sum/mean/std), Boolean-array counting tricks, in-place vs. copying sort, NumPy's 1D set operations, and saving/loading arrays to disk in NumPy's native binary format.

**Sources**: PythonforDataAnalysis.pdf, Chapter 4 ("NumPy Basics: Arrays and Vectorized Computation"), sections 4.3-4.5

**Last updated**: 2026-06-23

---

## Mathematical and statistical methods

Aggregations (also called *reductions*) like `sum`, `mean`, and `std` are available both as array methods (`arr.mean()`) and as top-level NumPy functions (`np.mean(arr)`, which takes the array as its first argument). They accept an optional **`axis`** argument that computes the statistic along one dimension, returning a result with one fewer dimension: `arr.mean(axis=1)` means "compute the mean across the columns" (i.e., one result per row); `arr.sum(axis=0)` means "compute the sum down the rows" (one result per column) — this axis-direction phrasing is easy to get backwards and worth re-checking each time. `cumsum` and `cumprod` don't reduce to a single value — they return an array of running totals/products, optionally per-axis in a multidimensional array.

**A genuinely useful trick**: Booleans coerce to `1`/`0` in these methods, so `(arr > 0).sum()` counts how many elements satisfy a condition — the parentheses are required so `.sum()` applies to the comparison's result, not to `arr` directly. `.any()` (true if at least one element is `True`) and `.all()` (true only if every element is `True`) are the other two Boolean-array-specific reductions, and they also work on non-Boolean arrays by treating any nonzero value as `True`.

## Sorting

`arr.sort()` sorts **in place** (like Python's `list.sort()`), optionally along a given `axis` in a multidimensional array (`axis=0` sorts within each column independently, `axis=1` within each row). **`numpy.sort(arr)`** (the top-level function, contrast with the instance method) returns a **new sorted copy** instead — the same in-place-vs-copy split as Python's `list.sort()` vs. `sorted()`.

## Unique values and set logic

`numpy.unique(arr)` returns the **sorted** unique values in a 1D array — faster than, and returning an actual NumPy array rather than a Python list compared to, the pure-Python equivalent `sorted(set(arr))`. `numpy.in1d(values, [list_of_candidates])` tests membership of each element of `values` against a list, returning a Boolean array — useful for flagging which rows match a set of target values without writing a loop. Other 1D set operations follow the same naming pattern as Python's native `set` methods: `intersect1d`, `union1d`, `setdiff1d`, `setxor1d`.

## File I/O with arrays

`numpy.save(path, arr)` / `numpy.load(path)` save and load a single array in NumPy's native uncompressed binary `.npy` format (the `.npy` extension is appended automatically if missing). `numpy.savez(path, name1=arr1, name2=arr2)` bundles multiple arrays into one `.npz` archive, keyed by the names you give as keyword arguments; loading it back (`np.load(path)`) returns a dict-like object that loads each named array lazily on access. `numpy.savez_compressed` is the same idea with compression, useful when the data compresses well. The book's explicit framing: **most real tabular/text data loading should go through pandas, not these binary array functions** — `.npy`/`.npz` are for NumPy-native array data specifically (e.g., caching an intermediate numeric result), not for client CSV exports.

## Key Ideas

- `axis=0` vs `axis=1` direction is genuinely confusing on first encounter — `axis=1` means "collapse across columns, leaving one result per row," the opposite of what the number might intuitively suggest. Worth deliberately re-verifying rather than assuming.
- `(condition).sum()` for counting matches is a small but extremely common idiom worth internalizing — much more common in real code than `np.count_nonzero` or a manual loop.
- `.npy`/`.npz` are for caching NumPy-native numeric arrays, not a substitute for `pandas.read_csv`/`to_csv` on tabular client data.

## Operational Use

`(condition).sum()` is the fast way to answer "how many records fail this validation rule" during a data-quality check — a near-universal first step in any audit data review. `np.unique` and the set-operation family are the array-native equivalent of the pandas/Python set-difference reconciliation pattern (comparing two client exports) when working at the raw-array level rather than a full DataFrame.

## Connects to

- [[numpy-ufuncs-pseudorandom-and-vectorized-logic]] — these statistical methods are themselves implemented as reductions over the same ufunc machinery.
- [[stages/stage-05-data-shapes]] — `numpy.unique`/`in1d`/`intersect1d` are the array-native counterparts to plain Python's `set` operations covered there.
- [[pandas-summary-stats-and-value-counts]] — pandas' `.describe()` and reduction methods are the DataFrame-level extension of exactly these array statistical methods.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** — the NumPy layer underneath pandas (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, indexing, slicing) and [[stages/stage-04-functions-parameters-return]].
- **Status**: parked per [[parking-lot]] (NumPy row). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
