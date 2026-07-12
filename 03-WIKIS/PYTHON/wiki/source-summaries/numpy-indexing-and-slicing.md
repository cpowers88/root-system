---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# NumPy Indexing, Slicing, Boolean Indexing, and Fancy Indexing

**Summary**: How to select subsets of an ndarray — basic integer/slice indexing (which returns *views*, not copies), Boolean indexing (which always copies), fancy indexing with integer arrays (which also always copies), and transposing/swapping axes.

**Sources**: PythonforDataAnalysis.pdf, Chapter 4 ("NumPy Basics: Arrays and Vectorized Computation"), section 4.1

**Last updated**: 2026-06-23

---

## Basic indexing and slicing — the critical view-vs-copy distinction

One-dimensional arrays act like Python lists on the surface (`arr[5]`, `arr[5:8]`). **The single most important fact on this page**: unlike a Python list slice, **a NumPy array slice is a *view* on the original array — the data is not copied, and writing to the slice writes through to the source array.**

```python
arr_slice = arr[5:8]
arr_slice[1] = 12345   # this also mutates the original arr
```

This is a deliberate design choice for performance on large arrays — copying on every slice would be prohibitively expensive at scale. **If you actually want a copy, you must say so explicitly**: `arr[5:8].copy()`. Pandas inherits this exact same view-by-default behavior, which is why `.copy()` shows up so often in pandas code that needs to guarantee it isn't mutating someone else's data.

A bare colon slice `[:]` assigns to every value in the (sub)array.

In a 2D array, `arr2d[2]` returns a 1D array (the third row) — indexing recursively. `arr2d[0][2]` and `arr2d[0, 2]` are equivalent, comma-separated indexing being the more idiomatic form. In a 3D array, omitting trailing indices returns a lower-dimensional sub-array of everything along the remaining axes (`arr3d[0]` is a 2x3 array; `arr3d[1, 0]` is a 1D array). **This multidimensional comma-indexing syntax is NumPy-specific — it does not work on a plain Python list of lists.**

**Slicing on multidimensional arrays** selects ranges along an axis: `arr2d[:2]` reads as "the first two rows." Multiple slices/indices can combine: `arr2d[:2, 1:]` (first two rows, all columns from index 1 on); mixing an integer index with a slice (`arr2d[1, :2]`) drops a dimension, returning a 1D result, while pure slicing (`arr2d[:2, 1:]`) always preserves the original number of dimensions. A bare `:` on one axis means "take that whole axis": `arr2d[:, :1]` selects every row's first column only.

## Boolean indexing

Comparing an array against a value or against another array of the same shape produces a Boolean array, which can itself be used to index: `data[names == "Bob"]` selects every row where the corresponding `names` entry equals `"Bob"`. The Boolean array must match the length of the axis being indexed; Boolean masks can be mixed with slices or integers on other axes. Negate a condition with `!=` or the `~` operator (`data[~(names == "Bob")]`); combine multiple conditions with `&` (and) / `|` (or) — **`and`/`or` (the Python keywords) do not work on Boolean arrays and will raise an error**.

**Boolean indexing always returns a copy**, even when the result happens to be unchanged — unlike basic slicing's view behavior. Boolean indexing is also the standard mechanism for **bulk conditional assignment**: `data[data < 0] = 0` zeroes out every negative value in one statement, no loop required.

## Fancy indexing

*Fancy indexing* means indexing with an integer array (or list of integers) rather than a single integer or slice: `arr[[4, 3, 0, 6]]` selects exactly those rows, in that order; negative integers select from the end. Passing **multiple** integer arrays (one per axis) is the part that surprises most people on first encounter — `arr[[1, 5, 7, 2], [0, 3, 1, 2]]` does **not** select a rectangular sub-block; it selects the individual elements at `(1,0)`, `(5,3)`, `(7,1)`, `(2,2)` — i.e., index *tuples*, producing a 1D result with as many elements as there are coordinate pairs. To get the "rectangular block of these rows and these columns" behavior people often expect instead, slice and fancy-index separately: `arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]`.

**Like Boolean indexing, fancy indexing always copies** — assigning to a fancy-indexed selection (`arr[[1,5,7,2],[0,3,1,2]] = 0`) modifies the original array's selected elements, but *reading* a fancy-indexed selection into a new variable gives you an independent copy, not a view.

## Transposing and swapping axes

`.T` (or the `.transpose()` method) returns a transposed **view** (no copy) of a 2D+ array — flipping rows and columns. This is most commonly used right before a matrix product: `np.dot(arr.T, arr)` or the equivalent `arr.T @ arr` (the `@` infix operator does matrix multiplication). `.swapaxes(axis1, axis2)` generalizes transposing to swap any two specified axes in a higher-dimensional array, also returning a view.

## Key Ideas

- **Memorize this distinction, it's load-bearing**: basic slicing → view (no copy, mutations propagate back); Boolean indexing → copy; fancy indexing → copy. Getting this wrong is a real, common source of "why did my original array/DataFrame change when I didn't mean it to" bugs.
- Multiple integer-array indexing selects coordinate *pairs*, not a rectangular block — this is genuinely unintuitive on first encounter (the source material admits as much) and worth double-checking when the result looks wrong.
- `&`/`|`, never `and`/`or`, for combining Boolean array conditions.

## Operational Use

Boolean indexing for bulk conditional cleaning (`data[data < 0] = 0`, flagging or zeroing out invalid values across an entire dataset in one line) is one of the most directly reusable NumPy patterns for client-data cleaning — it's the array-level version of the dict/defaultdict bucketing pattern, applied at scale. The view-vs-copy distinction is essential to understand before writing any pandas cleaning code that modifies a subset of a DataFrame in place.

## Connects to

- [[numpy-ndarray-basics-and-dtypes]] — the dtype/shape model this page's indexing operations all act on.
- [[stages/stage-05-data-shapes]] — the same `start:stop:step` slicing syntax, but NumPy's view-by-default behavior is a meaningful departure from plain Python lists, which always copy on slicing.
- [[pandas-series-dataframe-fundamentals]] — pandas' `.loc`/`.iloc` indexing inherits this exact view/copy distinction, which is the root cause of pandas' notorious `SettingWithCopyWarning`.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** — the NumPy layer underneath pandas (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, indexing, slicing) and [[stages/stage-04-functions-parameters-return]].
- **Status**: parked per [[parking-lot]] (NumPy row). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
