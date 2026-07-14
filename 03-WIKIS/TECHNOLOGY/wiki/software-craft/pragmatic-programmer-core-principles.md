---
domain: technology
type: reference
tags: [priority/later, status/wiki-only, domain/technology, source-role/reference, use-case/tech-stack, subject/software-craft]
---

# The Pragmatic Programmer: DRY, Orthogonality, Broken Windows, and Tracer Bullets

**Summary**: The highest-signal, most-cited principles from Hunt &
Thomas's *The Pragmatic Programmer* (20th Anniversary Edition) — four
ideas that show up repeatedly across the software industry's vocabulary
regardless of language or stack: DRY, orthogonality, the Broken Window
Theory applied to code, and tracer-bullet development.

**Sources**: The-Pragmatic-Programmer;Journeyman-Master.pdf (David Thomas
& Andrew Hunt, *The Pragmatic Programmer*, 20th Anniversary Ed.,
Addison-Wesley), Topic 2 ("The Cat Ate My Source Code" — broken windows),
Topic 4 ("Good-Enough Software"), Topic 7 ("The Evils of Duplication" —
DRY), Topic 8 ("Orthogonality"), Topic 10 ("Tracer Bullets")

**Last updated**: 2026-07-13

---

## DRY — Don't Repeat Yourself

The formal statement, more precise than the popular shorthand: **"Every
piece of knowledge must have a single, unambiguous, authoritative
representation within a system."** This is broader than "don't
copy-paste code" — it covers duplicated knowledge in documentation,
database schemas, and comments that restate what the code already says.
The book names four ways duplication actually arises in practice:

- **Imposed duplication** — the environment seems to force it (e.g., the
  same constant needed in both frontend and backend config).
- **Inadvertent duplication** — developers don't realize two pieces of
  code encode the same knowledge until a bug in one doesn't get fixed in
  the other.
- **Impatient duplication** — copy-pasting because it's faster in the
  moment.
- **Interdeveloper duplication** — two people (or two AI sessions) solve
  the same problem separately without knowing the other did.

The risk DRY names precisely: "it isn't a question of whether you'll
forget to update the duplicate — it's a question of when."

## Don't Live with Broken Windows

Borrowed directly from the criminology "Broken Window Theory" (unrepaired
small damage signals nobody cares, inviting more damage) and applied to
codebases: **one badly-designed piece of code, left unrepaired, changes
the team's own standard for what's acceptable** — the next shortcut feels
justified because the codebase "already looks like this." The
prescription isn't "fix everything now" — it's fix each one as soon as
it's discovered, or explicitly mark it (a comment, a "Not Implemented"
stub) so it reads as a known, contained gap rather than an invitation.

## Good-Enough Software

A deliberately uncomfortable idea for craftsmanship-minded readers:
software doesn't need to be perfect to ship — it needs to be good enough
for its users, its future maintainers, and its own timeline. Gold-plating
a feature nobody asked for is its own form of waste, not a virtue. This
is the same trade-off logic
[[../../SYSTEMS/wiki/goodbye-jit-hello-lean|Lean's own "waste"
framing]] applies elsewhere in this vault — polish beyond what the
customer values is a cost, not a quality signal.

## Orthogonality

Borrowed from geometry: two things are orthogonal if a change to one
doesn't affect the other — in software, decoupling. The book's own
illustration: a helicopter with orthogonal controls lets you adjust
altitude without also having to compensate for a resulting spin (real
helicopters aren't orthogonal — every control input has secondary
effects, which is why they're hard to fly). **In a well-designed system,
the database layer is orthogonal to the UI layer** — you can swap either
without touching the other. This is the direct architectural argument for
why [[../web-frameworks/flask-large-application-structure|Flask's
application-factory/blueprint pattern]] (already ingested in this wiki)
matters: it's what makes routes, models, and templates independently
changeable.

## Tracer Bullets

A development strategy distinct from a disposable prototype: build a
thin, working, end-to-end slice of the whole system first (like a tracer
round showing where the gun is actually aiming), then flesh it out
incrementally. Unlike a prototype, **tracer code is not thrown away — you
write it for keeps.** The payoff: it proves the whole architecture
connects (database → backend → frontend) early, when a wrong assumption
is cheap to fix, instead of discovering an integration problem after
every layer is separately "done."

## Use / Retrieval Notes

**Use when**: Starting a new client tool build — Tracer Bullets is the
direct argument for building a thin working slice first (e.g., one Flask
route that touches the real database and renders a real template) before
building out every feature in isolation.

**Use when**: Reviewing whether a codebase is getting harder to change —
Orthogonality names *why* ("the database layer isn't actually independent
of the UI layer anymore") in a way that's more specific than "this code
is messy."

**Do not use when**: DRY is being cited to justify a premature
abstraction — the book's own caveat (not fully excerpted here) is that
DRY is about knowledge duplication, not necessarily code-line
duplication; two pieces of code that look similar but represent different
business rules aren't a DRY violation.

## Connects to

[[clean-code-naming-functions-and-comments]],
[[clean-code-error-handling-testing-and-smells-checklist]] — Clean Code's
"General: Duplication" smell is the same DRY principle at function scope.
[[../web-frameworks/flask-large-application-structure]] — the concrete
Flask pattern that implements orthogonality in this wiki's own toolkit.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | System-design discipline for any client tool build |
| Current usefulness | 3 | Tracer Bullets directly informs how to start a new build |
| Tech-stack relevance | 3 | Language-agnostic, but ties directly to the Flask toolkit already ingested |
| Reading urgency | 1 | Reference — apply at project-start and design-review moments |

**Overall priority**: LATER — reference, apply at specific decision points.

## North Star Connection

Tracer Bullets specifically is the most actionable idea here for the
audit-tool-building work: build one real end-to-end path first (a single
Flask route hitting the real database and rendering a real page) before
building out the rest of a client tool — proves the architecture works
before investing further, same logic the Recommendation Ladder already
applies to tool choice.
