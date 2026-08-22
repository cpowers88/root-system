---
domain: technology
type: concept
tags: [subject/agile, subject/scrum, subject/software-engineering]
timeline: later
status: wiki-only
source_role: primary
use_cases: [tech-stack]
---

# Product vs. Project Software Engineering, and the Agile/Scrum Method

**Summary**: Sommerville's foundational distinction between project-based
software engineering (a customer specifies requirements up front; a
developer builds to that spec) and product-based software engineering (a
team has an opportunity, builds increments, and learns from user
feedback) — the reason agile methods exist. Covers the Agile Manifesto's
practical core and the Scrum method's roles, ceremonies, and sprint cycle
in working detail.

**Sources**: EngineeringSoftwareProducts.pdf (Ian Sommerville, *Engineering
Software Products*, Pearson, 2020), Chapters 1–2

**Last updated**: 2026-07-13

---

## Product vs. Project Development

Project-based SE (dominant for ~25 years): a customer defines requirements
in a contract, a team builds to that specification, success is measured
against the spec. This assumes you can get the requirements "right" before
writing code. Product-based SE inverts this: a team has an opportunity (not
a pre-defined problem), builds a minimal version, releases it, and learns
from real usage what to build next. The two approaches need different
techniques — heavyweight upfront requirements docs don't fit a product
team that doesn't yet know what its users actually want.

## The Agile Manifesto, Practically

Individuals/interactions over processes/tools; working software over
comprehensive documentation; customer collaboration over contract
negotiation; responding to change over following a plan. The practical
consequence for product teams: no "grand plan" for the whole system —
incremental planning driven by user stories, discovered and refined
sprint by sprint, because a product team can't fully anticipate what
users will actually want.

## Scrum: Roles, Ceremonies, Cycle

**Two roles unique to Scrum** (deliberately not called "manager"):
- **Product Owner** — represents the customer/user interest, owns and
  prioritizes the backlog.
- **ScrumMaster** — a coach, not a conventional manager. Guides the
  team's use of Scrum; has no direct authority to assign work.

**The sprint cycle**: fixed-length iterations (commonly 2–4 weeks). Daily
**scrums** — short, stand-up status meetings (deliberately no chairs, to
keep them short) where each person shares progress, plans, and blockers;
the sprint backlog gets reviewed and re-planned in real time if problems
surface. Two practices Sommerville recommends as non-negotiable
regardless of which agile flavor a team uses: **test automation** (a
runnable test suite, not manual testing) and **continuous integration**
(every change gets immediately integrated and tested against the rest of
the system, to catch interaction problems early).

**Definition of Done**: a team-agreed checklist for what "complete" means
for a piece of work in a given sprint — e.g., reviewed, unit-tested,
integrated. Without this, "done" means different things to different team
members and slips silently.

## Connects to

[[personas-scenarios-and-user-stories]] — user stories are Scrum's
standard unit for the product backlog; this page covers the *process*
that consumes them, that page covers how to *write* them.
`03-WIKIS\TECHNOLOGY\wiki\devops\the-three-ways-devops.md` and
`the-phoenix-project.md` — Scrum's sprint cycle and continuous
integration/test-automation rules are a concrete, team-level instance of
DevOps's Three Ways (flow, feedback, learning) at a finer grain than the
Phoenix Project's IT-ops-wide narrative.

## North Star Connection

No current project runs Scrum formally, but the underlying discipline —
small increments, a real Definition of Done, a backlog instead of a fixed
spec — applies directly to any client-facing tool build under
`TECHNOLOGY_LIBRARY_STRATEGY.md` Category 9/12 (Chris's own build
territory): build a thin increment, get it in front of the client, refine
from real use rather than guessing the full spec up front.
