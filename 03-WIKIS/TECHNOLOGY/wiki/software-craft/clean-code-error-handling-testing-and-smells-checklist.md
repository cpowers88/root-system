---
domain: technology
type: reference
tags: [priority/later, status/wiki-only, domain/technology, source-role/reference, use-case/tech-stack, subject/software-craft, subject/clean-code]
---

# Clean Code: Error Handling, Testing Discipline, and the Smells Checklist

**Summary**: The companion page to
[[clean-code-naming-functions-and-comments]] — three more chapters from
*Clean Code*: exception-handling rules (Ch. 7), the unit-testing
discipline (Ch. 9), and Ch. 17's full "Smells and Heuristics" list, which
is itself the book's own condensed checklist and the single most reusable
artifact in the source.

**Sources**: Clean-Code-Collection.pdf (Robert C. Martin, *Clean Code*),
Ch. 7 ("Error Handling"), Ch. 9 ("Unit Tests"), Ch. 17 ("Smells and
Heuristics")

**Last updated**: 2026-07-13

---

## Error Handling (Ch. 7)

- **Use exceptions, not return codes.** A return code forces the caller
  to check it immediately, cluttering the happy path; an exception
  separates error-handling logic from the main logic.
- **Write the `try`-`catch`-`finally` first**, before filling in the logic
  it wraps — it defines the transaction scope for the reader up front.
- **Provide context with exceptions** — an error message that says what
  operation failed and why, not just a stack trace.
- **Don't return `null`, and don't pass `null`.** A `null` return forces
  every caller to add a null-check or risk a crash; a special-case object
  or an exception is almost always cleaner.

## Unit Tests (Ch. 9)

- **The Three Laws of TDD**: write no production code until a failing
  test demands it; write no more of a test than is needed to fail; write
  no more production code than needed to pass the currently failing test.
  (Whether to follow strict TDD is a separate call — the point worth
  keeping regardless is that tests should exist *before* the code they
  verify gets complicated enough to be hard to test retroactively.)
- **Tests must stay as clean as production code** — messy tests rot
  faster than messy production code, and once they're unreliable, they
  get skipped, which defeats their purpose entirely.
- **F.I.R.S.T.**: tests should be **F**ast, **I**ndependent (no test
  depends on another's side effects), **R**epeatable (in any environment),
  **S**elf-validating (pass/fail, not "check the log"), **T**imely
  (written just before the production code, not after).

## Smells and Heuristics (Ch. 17) — the Condensed Checklist

Martin's own summary chapter, organized by category. Most useful entries
for a solo/small-team builder, verbatim from the source's own list:

**Comments**: obsolete comments left behind after the code changed;
redundant comments that just restate the code; commented-out code
(delete it, git remembers).

**Environment**: build requires more than one step; running the full
test suite requires more than one step. (Both should be a single
command.)

**Functions**: too many arguments; output arguments (a function that
mutates a parameter to return a value, instead of just returning a
value); flag arguments (see [[clean-code-naming-functions-and-comments]]);
dead functions (never called — delete them, don't comment them out).

**General** (selected, most broadly applicable):
- **Duplication** — the single most avoidable source of bugs; see
  [[pragmatic-programmer-core-principles]]'s DRY principle for the deeper
  treatment.
- **Dead code** — code that's never executed. Delete it; don't leave it
  "just in case."
- **Inconsistency** — if you call a variable `response` in one function,
  don't call the same concept `resp` in another.
- **Magic numbers** — replace `86400` with `SECONDS_PER_DAY`.
- **Feature envy** — a method that spends more time reaching into another
  class's data than using its own is a sign that method belongs on the
  other class.
- **Explanatory variables** — break a complex expression into named
  intermediate variables so the reader doesn't have to parse it in their
  head.

## Use / Retrieval Notes

**Best use**: The Smells section specifically is designed to be a
periodic self-review checklist, not a linear read — scan it before a
release or during a refactor pass.

**Use when**: Debugging a Flask app that's grown past its original scope
and started feeling hard to change — the "General" smells list is
usually where the actual problem is hiding.

**Do not use when**: Enforcing strict TDD (the Three Laws) on rapid
prototyping work — Martin's own *Clean Coder* half of this source
(see [[the-clean-coder-professionalism-and-saying-no]]) treats TDD as a
professional discipline to grow into, not a mandate for every line of
throwaway exploration code.

## Connects to

[[clean-code-naming-functions-and-comments]] — the companion naming/
functions/comments page from the same source.
[[pragmatic-programmer-core-principles]] — DRY (duplication) is the
system-level version of this page's "General: Duplication" smell.
[[the-clean-coder-professionalism-and-saying-no]] — TDD reappears there
as a professional-discipline argument, not just a technique.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | Debugging/refactor checklist for client-facing tools |
| Current usefulness | 3 | Directly usable during any code review pass |
| Tech-stack relevance | 3 | Language-agnostic |
| Reading urgency | 1 | Reference — consult, don't read linearly |

**Overall priority**: LATER — reference checklist.

## North Star Connection

The Smells checklist specifically is the fastest-payoff artifact in this
source for the audit-tool-building context: a 10-minute scan against this
list before shipping a client tool catches the failure modes Martin
argues actually sink projects over time (duplication, dead code,
inconsistency) — cheaper than discovering them after the tool is in a
client's hands.
