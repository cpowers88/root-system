---
domain: tech
type: framework
tags: [priority/later, status/wiki-only, subject/devops, subject/organizational-learning]
---

# Just Culture and Blameless Post-Mortems

**Summary**: The Handbook's Third Way technical/organizational practice —
why punishing engineers for mistakes guarantees the same failure recurs,
the concrete mechanics of running a blameless post-mortem (who attends,
what gets banned from the conversation, what gets produced), and how this
differs from the Phoenix Project's narrative Chaos-Monkey treatment of the
same Third Way.

**Sources**: DEvOpsHandbook.pdf (Kim, Humble, Debois, Willis, *The DevOps
Handbook*, 2016), Part V, "Enable and Inject Learning" chapters

**Last updated**: 2026-07-13

---

## The Core Argument

A "just culture" balances two needs that naively appear to conflict:
safety (people must feel safe disclosing what actually happened) and
accountability (mistakes still matter). John Allspaw (Etsy CTO), the
source of the term "blameless post-mortem": view mistakes "with a
perspective of learning." The mechanism is precise: if an engineer who
makes a mistake feels safe describing exactly what happened, they become
the organization's best resource for preventing a recurrence — they're
enthusiastic about helping, not defensive. Punish the same mistake, and
every future incident's true details get hidden or minimized, which
**guarantees** the failure mode recurs, because nobody with real
visibility into the mechanism will disclose it.

## Running the Meeting — the Concrete Mechanics

Scheduled as soon as possible after the incident is *resolved* (not
during — don't distract active responders), before memories fade.

**Who attends**: everyone involved in the contributing decisions, who
identified it, who responded, who diagnosed it, who was affected, and
anyone else interested.

**What the meeting produces**:
- A timeline reconstructed from multiple perspectives, preferring
  telemetry/chat-log evidence over subjective narrative (see
  [[production-telemetry-and-monitoring-architecture]] — this is exactly
  why that infrastructure matters beyond day-to-day monitoring).
- Explicit permission for the people who made the mistake to describe it
  in detail without punishment.
- Recorded countermeasures, each with a target date and an owner.

**What's explicitly banned**: the phrases "would have" or "could have."
These are counterfactual statements — they evaluate the incident against
an imagined system that doesn't exist, instead of the system that
actually does. The discipline is staying strictly in the system-as-it-was,
not the system-as-it-should-have-been.

**A specific human-factors caution**: engineers frequently blame
themselves in these meetings, disproportionately to their actual
contribution — "I suck and I have no idea what I'm doing" is a named,
expected reaction (Etsy's Ian Malpass), not a sign the process is working
correctly. First few post-mortems benefit from a trained facilitator who
wasn't involved in the incident, specifically to keep the conversation
on mechanism rather than self-blame.

## Why This Matters Beyond the Phoenix Project's Version

[[resilience-engineering-and-chaos-testing]] already covers this wiki's
existing Third Way material — but that page's source (the Phoenix
Project novel) renders the Third Way entirely through Chaos Monkey/Evil
Chaos Monkey fault injection. This page covers a *different*, arguably
more foundational Third Way practice: what happens *after* a real
(unplanned) failure, not how to manufacture practice failures. The two
are complementary, not overlapping — chaos engineering creates
controlled opportunities to practice; blameless post-mortems are how an
organization actually extracts the learning from failures (planned or
not) once they happen.

## Connects to

- [[resilience-engineering-and-chaos-testing]] — the existing Third Way
  page (planned fault injection); this page is the *unplanned*-failure
  learning mechanism, the other half of the same Way.
- [[production-telemetry-and-monitoring-architecture]] — post-mortems
  explicitly prefer telemetry evidence over recalled narrative; this is a
  direct, concrete use case for the telemetry infrastructure that page
  describes.
- [[the-three-ways-devops]] — Third Way's "culture that fosters
  experimentation, learning from failure" defined operationally.

## North Star Connection

Directly reusable for internal practice, not just client audits: any
mistake made in `.ROOT` session work (a bad file move, a broken link, a
misread scope) is a candidate for the same discipline in miniature — what
happened, why, what changes, no "should have known better" framing. Also
a credible, concrete audit-conversation tool: most SMB clients have no
formal incident-review practice at all; "what happens after something
breaks" is a diagnostic question with a specific, teachable answer here.
