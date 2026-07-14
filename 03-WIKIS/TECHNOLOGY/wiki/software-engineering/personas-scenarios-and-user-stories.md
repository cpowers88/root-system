---
domain: technology
type: concept
tags: [priority/later, status/wiki-only, domain/technology, source-role/primary, use-case/tech-stack, subject/requirements, subject/agile, subject/software-engineering]
---

# Personas, Scenarios, and User Stories — Three Levels of Requirements Narrative

**Summary**: A genuinely new topic for this wiki — nothing in the existing
68 FORGE-inherited pages covers requirements-gathering technique. Three
narrative tools, each at a different grain, for figuring out what a
software product should actually do: **personas** (who the users are),
**scenarios** (a high-level story of a user trying to do something), and
**user stories** (a specific, structured statement of one thing a user
needs).

**Sources**: EngineeringSoftwareProducts.pdf (Ian Sommerville, *Engineering
Software Products*, Pearson, 2020), Chapter 3

**Last updated**: 2026-07-13

---

## Personas — "Who Are the Target Users?"

An imagined, concrete character portrait of a type of user — not a real
person, but specific enough to reason about (name, age, role, habits,
technical comfort level, motivations). The point isn't biographical detail
for its own sake; it's forcing a shared team picture of the user instead
of each developer privately assuming a different one, which otherwise
produces an inconsistent product as those different assumptions leak into
different parts of the implementation. Different personas for the same
product surface different, sometimes conflicting needs (e.g., a
non-technical end user persona vs. a technical administrator persona for
the same system) — deliberately, since real user bases are diverse.

## Scenarios — High-Level Stories of Use

A narrative describing a sequence of interactions a persona has with the
system, written from the user's perspective, without implementation
detail. Not a specification — a communication and design tool. Scenarios
read more naturally than dry requirement lists precisely because they
describe *what a user does*, not what the system must implement — which
is also their limit: they're for understanding intent, not for defining
exact behavior.

## User Stories — Finer-Grained, Structured

Standard format: **"As a `<role>`, I `<want/need>` to `<do something>`."**
Optional justification variant: **"...so that `<reason>`."** User stories
are the standard unit for a Scrum product backlog — each should be small
enough to implement within a single sprint. A story too large for one
sprint is called an **epic** and needs breaking down into smaller stories
before it's plannable. Stories aren't meant to be a complete
specification either — Sommerville is explicit that when using stories
for *feature identification* (rather than sprint planning), don't worry
about story-vs-epic size; use whichever narrative form helps surface the
feature.

## How the Three Compose

A scenario can be refined into several user stories (each capturing one
concrete action within the broader scenario) — going from "a teacher logs
into the system from home and does her admin" (scenario) to three
specific stories: log in with existing Google credentials, access
class-management apps, disambiguate between two linked accounts. This is
the practical link between the high-level story and what actually lands
on a backlog as buildable work.

## Connects to

[[agile-software-engineering-and-scrum]] — the Scrum process this
technique feeds.

## North Star Connection

Directly applicable to any future client-facing tool build
(`TECHNOLOGY_LIBRARY_STRATEGY.md` Category 9/12): before building a
data-entry form or dashboard, write the persona (who's using this — the
shop owner? the office admin?) and 2–3 user stories. Cheap, fast, and
catches "wait, who is this actually for" before code gets written — a
much lower-cost mistake to catch at the story stage than after a client
demo goes wrong.
