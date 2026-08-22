---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# String Manipulation and Regular Expressions in pandas

**Summary**: Cleaning messy text fields — inconsistent capitalization, extra whitespace, embedded contact info, free-text notes — is one of the most common real-world data cleaning tasks. This page covers Python's built-in string methods, the `re` module for pattern matching, and the vectorized `.str` accessor that applies both to an entire pandas column at once while correctly skipping missing values.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 7 ("Data Cleaning and Preparation"), section 7.4 ("String Manipulation")

**Last updated**: 2026-06-20

---

## Built-In String Methods (Plain Python, One String at a Time)

```python
val.split(",")                      # break into a list on a delimiter
[x.strip() for x in val.split(",")] # split + trim whitespace from each piece, a very common pair
"::".join(pieces)                   # opposite of split — join a list back into one string
"guido" in val                      # substring check (preferred over .find/.index for a simple yes/no)
val.replace(",", "")                # substring replace, also commonly used to delete a pattern
```

`find` returns `-1` if the substring isn't present; `index` raises a `ValueError` instead — `find`/`in` are safer defaults when a substring might legitimately be absent.

## Regular Expressions (Pattern Matching Beyond Simple Substrings)

```python
import re
re.split(r"\s+", text)              # split on variable-width whitespace (regex handles what split() can't)
regex = re.compile(r"\s+")          # compile once, reuse many times — faster for repeated use
regex.findall(text)                 # all matches, as a list
regex.search(text)                  # first match only, as a match object (has .start()/.end())
regex.match(text)                   # like search, but only matches at the very start of the string
regex.sub("REDACTED", text)         # replace every match with a fixed string
```

Use **capture groups** (parentheses) to pull a pattern apart into pieces in one pass — e.g., `r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"` segments an email into username/domain/suffix; `match.groups()` returns those pieces as a tuple, and `findall` on a grouped pattern returns a list of tuples instead of plain strings.

**Audit-usable pattern**: a regex like the email pattern above is the standard tool for pulling structured pieces (phone numbers, job IDs, dollar amounts) out of free-text notes fields that a client's software exports as one unstructured blob.

## The Vectorized .str Accessor — The pandas-Specific Piece

Plain Python string methods (or `.map(lambda x: ...)`) **fail outright** on a Series containing `NaN`. The `.str` accessor on a Series applies any string or regex method element-wise while automatically skipping missing values and returning `NaN` in their place:

```python
data.str.contains("gmail")          # Boolean mask, NA stays NA — no error
data.str.findall(pattern, flags=re.IGNORECASE)
data.str.extract(pattern, flags=re.IGNORECASE)   # captured groups -> a DataFrame, one column per group
data.str[:5]                        # vectorized slicing, same NA-safe behavior
data.str.get(1)                     # pull the i-th element out of each row's list/tuple result
```

**This is the rule to remember**: any time a string operation needs to run across a whole column that might contain missing values, reach for `series.str.<method>` rather than `.map()` with a raw Python string method — it is both safer (NA-aware) and the more idiomatic pandas pattern.

## Connects to

- [[pandas-missing-data-and-duplicates]] — the `.str` accessor's NA-aware behavior is the string-specific extension of the same missing-data handling philosophy.
- [[pandas-arithmetic-and-function-application]] — `.str.<method>` is functionally the string-specific sibling of `.map()`/`.apply()`.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
