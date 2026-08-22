---
type: map
timeline: reference
status: active
tags: [programming, sources, retrieval]
created: 2026-07-25
---

# Source Page Map — Physical PDF Pages for Retrieval

Companion to [[source-map]]. `source-map.md` says *which book and chapter* serves a
stage; this page says *what physical PDF page to actually open*. Built 2026-07-25
because the spine was recorded as `ingested (TOC-level)` with no page numbers, so
every citation meant hunting a 291-page PDF by hand.

## How to use it

**Every page number below is a PHYSICAL PDF page** — the number your reader's page
box wants, not the number printed on the paper. Printed page numbers are what a
book's own table of contents and index use, and they are always lower because of
front matter. Both are given so either direction works.

```
printed page + offset = physical page
```

Open a book at a physical page directly:

```bash
# read one page as text
pdftotext -f 43 -l 43 -layout "raw/books/thinkpython.pdf" -

# extract a chunk to read or attach
pdftotext -f 43 -l 52 -layout "raw/books/thinkpython.pdf" stage04-functions.txt
```

## Verification status — read this before trusting a row

| Book | Chapters mapped | Offset | Verified how |
|---|---|---|---|
| Think Python 2e | **21 of 21** | printed **+22** | Chapter titles matched against the book's own TOC; physical p.43 opened and confirmed as Ch.3 "Functions" |
| Python Crash Course 3e | **19 of 20** (Ch.13 missed) | printed **+50** | Physical p.211 opened and confirmed as Ch.8 "FUNCTIONS" |
| Python Workout 2e | **12 of 12** | printed **+24** | Physical p.127 opened and confirmed as Ch.7 "Functions" running header |
| Invent Your Own Games 4e | **0** | — | **Not mapped.** Automated pass found no usable chapter pattern; needs a manual TOC pass |
| Grokking Algorithms 2e | **0** | — | **Not mapped.** Same reason |
| Common-Sense DS&A 2e | 20, unverified | unreliable | Chapter starts look plausible but the offset detection failed; **do not cite until spot-checked** |
| Think Like a Programmer | 8, unverified | unreliable | C++ source, strategy-reading only; low priority |
| Automate the Boring Stuff 3e | n/a | n/a | Already split into per-chapter `.md` files in `raw/books/automate-the-boring-stuff/` — cite the chapter file directly, no page math needed |

The unmapped and unverified books are all Stage 8+ support material (algorithms,
OOP depth, strategy reading). None of them is needed before November. They are
listed here as open work rather than quietly omitted.

## Think Python 2e (Downey) — SPINE, Stages 1–8

`raw/books/thinkpython.pdf` · 291 physical pages · **printed + 22 = physical**

| Ch. | Title | Printed | Physical | Vault stage |
|---:|---|---:|---:|---|
| 1 | The Way of the Program | 1 | **23** | Stage 0–1 |
| 2 | Variables, Expressions and Statements | 11 | **33** | Stage 1 |
| 3 | Functions | 21 | **43** | **Stage 4** |
| 4 | Case Study: Interface Design | 35 | **57** | Stage 7 |
| 5 | Conditionals and Recursion | 47 | **69** | Stage 2 (recursion → Stage 8) |
| 6 | Fruitful Functions | 61 | **83** | **Stage 4** |
| 7 | Iteration | 75 | **97** | **Stage 3** |
| 8 | Strings | 85 | **107** | Stage 3 (traversal) + Stage 5 |
| 9 | Case Study: Word Play | 99 | **121** | Stage 7 |
| 10 | Lists | 107 | **129** | Stage 5 |
| 11 | Dictionaries | 125 | **147** | Stage 5 |
| 12 | Tuples | 139 | **161** | Stage 5 |
| 13 | Case Study: Data Structure Selection | 151 | **173** | Stage 7 |
| 14 | Files | 165 | **187** | Stage 6 |
| 15 | Classes and Objects | 177 | **199** | Stage 8 |
| 16 | Classes and Functions | 187 | **209** | Stage 8 |
| 17 | Classes and Methods | 195 | **217** | Stage 8 |
| 18 | Inheritance | 207 | **229** | Stage 8 |
| 19 | The Goodies | 223 | **245** | Stage 10 |
| 20 | Debugging | 235 | **257** | Stage 6 |
| 21 | Analysis of Algorithms | 245 | **267** | Stage 8 |

### Section-level pages for the active stages

Verified individually by searching the extracted text, not interpolated.

**Stage 3 — Loops** (Ch.7 + the pulled-forward Ch.8 sections)

| Section | Physical page |
|---|---:|
| Reassignment | **97** |
| Updating Variables | **98** |
| The `while` Statement | **99** |
| `break` | **100–101** |
| Square Roots *(optional)* | **101** |
| Algorithms | **103** |
| A String Is a Sequence | **107** |
| `len` | **108** |
| Traversal with a `for` Loop | **108** |

**Stage 4 — Functions** (Ch.3 + Ch.6)

| Section | Physical page |
|---|---:|
| Function Calls | **43** |
| Math Functions | **44** |
| Composition | **45** |
| Adding New Functions | **45** |
| Definitions and Uses | **47** |
| Flow of Execution | **47** |
| Parameters and Arguments | **48** |
| Variables and Parameters Are Local | **49** |
| Stack Diagrams | **50** |
| Fruitful Functions and Void Functions | **51** |
| Why Functions? | **52** |
| Return Values | **83** |
| Incremental Development | **84–85** |
| Boolean Functions | **87** |
| *More Recursion — **skip**, Stage 8* | *88–89* |
| *Leap of Faith — **skip*** | *90* |
| *Checking Types — **skip*** | *91* |

So Stage 4's assigned spine reading is **physical pp. 43–52 and 83–87** — about
15 pages, not "two chapters."

## Python Crash Course 3e (Matthes) — support, Stages 1–7

`raw/books/PythonCrashCourse.pdf` · 761 physical pages · **printed + 50 = physical**

| Ch. | Title | Physical | Vault stage |
|---:|---|---:|---|
| 1 | Getting Started | **50** | Stage 0 |
| 2 | Variables and Simple Data Types | **65** | Stage 1 |
| 3 | Introducing Lists | **88** | Stage 5 |
| 4 | Working with Lists | **107** | Stage 3 (loop sections only) / Stage 5 |
| 5 | `if` Statements | **137** | Stage 2 |
| 6 | Dictionaries | **162** | Stage 5 |
| 7 | User Input and `while` Loops | **191** | **Stage 3** |
| 8 | Functions | **211** | **Stage 4** *(skip `*args`/`**kwargs`)* |
| 9 | Classes | **246** | Stage 8 |
| 10 | Files and Exceptions | **280** | Stage 6 |
| 11 | Testing Your Code | **313** | Stage 10 |
| 12 | A Ship That Fires Bullets | **337** | Stage 10 (parked) |
| 14 | Scoring | **405** | Stage 10 (parked) |
| 15 | Generating Data | **438** | Stage 10 (parked) |
| 16 | Downloading Data | **478** | Stage 10 (parked) |
| 17 | Working with APIs | **513** | Stage 10 (parked) |
| 18–20 | Django web app | **537 / 577 / 615** | parked — out of syllabus scope |

Ch.13 was missed by the automated pass; it falls between pp. 337 and 405 and is
parked Stage 10 project material either way.

## Python Workout 2e (Lerner) — drill bank

`raw/books/PythonWorkout.pdf` · 241 physical pages · **printed + 24 = physical**

| Ch. | Title | Physical | Vault stage |
|---:|---|---:|---|
| 1 | Improving your Python with practice | **25** | any |
| 2 | Numeric types | **31** | Stage 1 |
| 3 | Strings | **47** | Stage 1 / 5 |
| 4 | Lists and tuples | **58** | Stage 5 |
| 5 | Dictionaries and sets | **81** | Stage 5 |
| 6 | Files | **99** | Stage 6 |
| 7 | **Functions** | **127** | **Stage 4** |
| 8 | Functional programming with comprehensions | **143** | Stage 10 |
| 9 | Modules and packages | **169** | Stage 9 |
| 10 | Objects | **183** | Stage 8 |
| 11 | Iterators and generators | **219** | Stage 10 |
| 12 | Where to from here? | **235** | — |

## Rule for new source intake

Any book added to this hub gets a row here **at intake time**, with the offset
measured and at least one page opened to confirm it. A source that cannot be
page-mapped is recorded as unmapped rather than cited by chapter alone — a
chapter name is a search, a physical page is a retrieval.
