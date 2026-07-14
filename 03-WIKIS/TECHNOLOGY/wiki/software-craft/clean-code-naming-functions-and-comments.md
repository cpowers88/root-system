---
domain: technology
type: reference
tags: [priority/later, status/wiki-only, domain/technology, source-role/reference, use-case/tech-stack, subject/software-craft, subject/clean-code]
---

# Clean Code: Naming, Functions, and Comments

**Summary**: The core, language-agnostic writing discipline from Robert C.
Martin's *Clean Code* (Ch. 1-4) — why bad code accumulates into an
unmanageable mess (the "Total Cost of Owning a Mess"), and the three most
directly actionable rule sets for keeping code readable as a solo builder:
naming, function design, and when comments help vs. hurt.

**Sources**: Clean-Code-Collection.pdf (Robert C. Martin, *Clean Code: A
Handbook of Agile Software Craftsmanship*, Prentice Hall, 2008 — bundled
in this PDF with *The Clean Coder*, see [[the-clean-coder-professionalism-and-saying-no]]), Ch. 1 ("Clean Code"), Ch. 2 ("Meaningful Names"), Ch. 3 ("Functions"), Ch. 4 ("Comments")

**Last updated**: 2026-07-13

---

## Why This Matters Before the Rules

Martin's core argument in Ch. 1: messy code isn't a shortcut, it's debt
that compounds. Teams that write fast and messy see productivity approach
zero asymptotically as every change requires "understanding" tangled
code before adding to it — and "later" (the promise to clean it up)
"equals never" (LeBlanc's Law). The fix isn't a redesign — it's the Boy
Scout Rule: leave the code cleaner than you found it, one small
improvement at a time, every time you touch a file.

## Meaningful Names (Ch. 2)

A compact rule set, most useful as a checklist during a self-review pass:

- **Intention-revealing names** — a variable/function name should answer
  why it exists, what it does, how it's used, without needing a comment.
- **Avoid disinformation** — don't call a group of accounts `accountList`
  unless it's actually a `List`.
- **Make meaningful distinctions** — `data` vs. `theData` isn't a real
  distinction; it's noise to satisfy a compiler.
- **Use pronounceable, searchable names** — `genymdhms` fails both; a
  single-letter name like `e` is fine as a loop counter, useless as a
  search target across a large codebase.
- **Avoid encodings** (Hungarian notation, member prefixes) — modern
  editors make type information visible; encoding it in the name is a
  translation tax on every reader.
- **Class names are nouns, method names are verbs** — `Customer`,
  `AccountVisitor`, not `Manager`/`Processor`/`Data` (too vague to
  distinguish anything).
- **Pick one word per concept, and don't pun** — don't use `fetch`,
  `retrieve`, and `get` for the same kind of operation across classes; and
  don't reuse `add` for both "sum two values" and "append to a
  collection" in the same codebase.

## Functions (Ch. 3)

- **Small, and then smaller than that.** Blocks inside `if`/`else`/`while`
  should usually be one line — a function call with a well-chosen name.
- **Do one thing.** A function does one thing if you can't meaningfully
  extract another function from it with a name that isn't just a
  restatement.
- **One level of abstraction per function** — mixing high-level policy
  ("process the order") with low-level detail ("increment `i`") in the
  same function is a readability smell.
- **Function arguments**: 0 (niladic) is ideal, 1 (monadic) is fine, 2
  (dyadic) is acceptable with care, 3 (triadic) needs strong
  justification, more than 3 needs restructuring (often into an argument
  object). **Flag arguments are a code smell** — a boolean parameter means
  the function does two things depending on its value; split it into two
  functions instead.
- **No side effects** — a function named `checkPassword` that also
  initializes a session as a side effect will surprise every caller who
  only wanted the check.
- **Prefer exceptions to error codes**, and extract the `try`/`catch`
  body into its own function — error handling is one thing, so it
  shouldn't be mixed with the logic that generates the error.

## Comments (Ch. 4)

The central claim: **comments do not make up for bad code.** A comment
explaining what a poorly-named function does is a sign the function
should be renamed instead, not documented.

**Good comments**: legal notices, explanation of intent that genuinely
can't be captured in code, warnings of consequences ("don't run this on
prod, it's slow"), Javadoc-style public API documentation.

**Bad comments** (the more common failure mode): comments that merely
restate what the code already says (redundant), comments that go stale
because nobody updates them when the code changes (misleading — worse
than no comment, since it's actively wrong), commented-out code (delete
it — version control remembers), and "noise" comments that exist because
a style guide mandates a comment on every function regardless of whether
it adds anything.

## Use / Retrieval Notes

**Best use**: Self-review checklist before committing — run new
functions/variable names against the Meaningful Names list; run new
functions against the Functions size/argument-count/side-effect list.

**Use when**: Writing or reviewing any Flask/Python code for a client
tool — these rules are language-agnostic and apply directly to the
[[../web-frameworks/flask-web-development|Flask toolkit]] already ingested
in this wiki.

**Do not use when**: Treating this as a rigid style guide to enforce
mechanically — Martin's own later chapters (Smells and Heuristics, see
[[clean-code-error-handling-testing-and-smells-checklist]]) frame these as
heuristics to apply with judgment, not laws.

## Connects to

[[../web-frameworks/flask-web-development]] — the client-tool codebase
these naming/function rules apply to directly.
[[clean-code-error-handling-testing-and-smells-checklist]] — the
companion page (error handling, testing, and the full smells checklist).
[[pragmatic-programmer-core-principles]] — DRY and orthogonality are the
system-level complement to this page's function/naming-level discipline.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | Improves the quality of any client-facing tool built, not a new capability itself |
| Current usefulness | 3 | Directly applicable to any Python/Flask code written today |
| Tech-stack relevance | 3 | Language-agnostic discipline, not a specific tool |
| Reading urgency | 1 | Reference material — consult during review, not a linear read |

**Overall priority**: LATER — reference, not a study sequence item.

## North Star Connection

Code quality discipline for the audit-tool-building work this wiki's
`web-frameworks/` toolkit exists to support — directly relevant once a
client engagement produces real Flask code that needs to stay
maintainable on retainer, not thrown away after one demo.
