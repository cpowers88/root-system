---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# NumPy ndarray Basics and Data Types

**Summary**: NumPy's core `ndarray` object — creation, shape/dtype metadata, casting between types, and vectorized arithmetic — the foundation pandas itself is built on.

**Sources**: PythonforDataAnalysis.pdf, Chapter 4 ("NumPy Basics: Arrays and Vectorized Computation"), sections 4.1

**Last updated**: 2026-06-23

---

## Why NumPy is fast

NumPy stores array data in a single contiguous block of memory, separate from regular Python objects, and its C-level algorithms operate on that block without per-element type-checking overhead. The practical result, demonstrated directly in the source with `%timeit`: multiplying a million-element NumPy array by 2 took 715 microseconds; the equivalent pure-Python list comprehension took 48.8 milliseconds — **roughly 70x slower**. NumPy-based code is generally 10-100x faster than the pure-Python equivalent and uses substantially less memory. This performance gap is *why* pandas exists on top of NumPy rather than on top of plain Python lists.

`import numpy as np` is the universal convention — avoid `from numpy import *`, since the NumPy namespace is large and contains names that collide with Python builtins (`min`, `max`).

## Creating arrays

- **`np.array(data)`** — converts any sequence-like object (list, tuple, another array) into an ndarray, inferring a dtype unless one is given. Nested sequences (a list of equal-length lists) become a multidimensional array automatically.
- **`np.zeros(shape)`** / **`np.ones(shape)`** — arrays of all 0s/1s. Pass a tuple for higher-dimensional shapes: `np.zeros((3, 6))`.
- **`np.empty(shape)`** — allocates memory but does **not** initialize values. **Caution from the source: it's not safe to assume `np.empty` returns zeros — it can contain arbitrary garbage values.** Only use it when you're about to overwrite every element anyway.
- **`np.arange(n)`** — the array-valued version of the built-in `range`.
- **`np.full(shape, fill_value)`** and **`np.eye(n)`** (identity matrix) round out the standard creation functions.

Every array has a **`shape`** (a tuple giving the size of each dimension) and a **`dtype`** (the data type metadata).

## Data types (dtype)

NumPy's numeric dtypes are named `type` + `bits`: `float64` is the standard double-precision type Python's own `float` uses under the hood (8 bytes / 64 bits); `int32`, `int64`, `float32`, etc. follow the same pattern. The source's explicit advice for beginners: **don't worry about memorizing every dtype** — usually only the general *kind* (floating point, integer, boolean, string, object) matters day to day; precise control over storage type matters mainly for large datasets or interop with disk/C/FORTRAN code.

**Casting** between types uses `.astype()`:

```python
arr.astype(np.float64)   # int -> float
arr.astype(np.int32)     # float -> int, truncates the decimal part (doesn't round)
numeric_strings.astype(float)  # string array -> numeric, if every value parses
```

**`astype` always creates a new array — a real copy — even if the target dtype is identical to the source.** Casting a string array to numbers will raise `ValueError` if any value can't be parsed. **Caution: NumPy's fixed-size `numpy.string_` type can silently truncate input without warning — pandas handles non-numeric/string data more safely than raw NumPy.**

## Vectorized arithmetic and broadcasting (intro)

Arithmetic between two equal-size arrays applies **element-wise**: `arr * arr`, `arr - arr`. Arithmetic between an array and a scalar **broadcasts** the scalar to every element: `1 / arr`, `arr ** 2`. Comparisons between equal-size arrays (`arr2 > arr`) produce a Boolean array of the same shape, not a single `True`/`False` — this is the array-level extension of Python's scalar comparison operators. Operations between *differently sized* arrays (full broadcasting) are covered in the book's Appendix A and aren't needed for most everyday use.

## Key Ideas

- The performance gap between NumPy and pure Python isn't marginal — it's the entire reason pandas (built on NumPy) is the standard tool rather than manual Python loops over lists of dicts.
- `np.empty` is a sharp edge for beginners — it looks like it should give zeros, but doesn't. Use `np.zeros` unless you specifically intend to overwrite every value immediately.
- `astype` always copies, even when "casting" to the same dtype — useful to know when reasoning about memory usage on large arrays.

## Operational Use

This is the layer underneath every pandas DataFrame column — a DataFrame's numeric columns are, internally, NumPy arrays with a dtype. Understanding `dtype` and `.astype()` here directly explains why a pandas column sometimes silently behaves unexpectedly (e.g., an `int` column that should hold `NaN` gets upcast to `float64`, since `NaN` doesn't exist as an integer).

## Connects to

- [[stages/stage-01-python-atoms]] — NumPy's dtype system is the array-level analogue of Python's own scalar type model (int/float/str), just with explicit bit-width control.
- [[pandas-series-dataframe-fundamentals]] — every pandas Series/DataFrame column is backed by exactly this kind of NumPy array.
- [[numpy-indexing-and-slicing]] — the array creation and dtype concepts here are the prerequisite for everything in that page.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** — the NumPy layer underneath pandas (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, indexing, slicing) and [[stages/stage-04-functions-parameters-return]].
- **Status**: parked per [[parking-lot]] (NumPy row). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
