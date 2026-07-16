---
domain: technology
type: concept
timeline: reference
tags: [priority/later, status/wiki-only, domain/technology, source-role/primary, use-case/tech-stack, subject/ddd, subject/eventstorming, subject/microservices]
---

# Domain-Driven Evolution, EventStorming, and Distributed Boundaries

## Design Must Follow Business Change

Architecture is a current hypothesis about the business, not a permanent truth.
Watch for changes in subdomain type, terminology, ownership, coupling, and rate of
change. Boundaries and implementation patterns should evolve when those signals
change; otherwise the code preserves an obsolete business model.

Useful heuristics:

- optimize architecture effort around core subdomains;
- prefer simple business-logic patterns where rules are simple;
- protect models with boundaries and translation, not enterprise-wide objects;
- minimize coupling across components and teams;
- refactor incrementally from observed pain rather than rewrite by ideology.

## EventStorming

EventStorming is a collaborative, low-tech workshop for building shared domain
knowledge around events that happened in a business process. It is valuable for:

- creating a ubiquitous language;
- mapping an end-to-end business process;
- discovering edge cases, policies, commands, aggregates, and boundaries;
- recovering knowledge from a legacy system or fragmented team;
- exploring new requirements or improvement opportunities;
- onboarding people through the real process rather than a stale document.

### Practical sequence

1. Invite domain experts plus the people who design and operate the system.
2. Define the business-process boundary and timeline.
3. Place domain events in past-tense order.
4. Add commands/actions that cause events.
5. Add actors, policies/rules, external systems, and read models.
6. Mark questions, conflicts, pain points, and missing knowledge.
7. Group events around consistency/behavior and candidate aggregates.
8. Look for language and ownership changes that suggest bounded contexts.
9. Validate the map with scenarios and exceptions; do not treat sticky notes as code design automatically.

The workshop output is a learning model. It should inform requirements and
architecture but is not itself a final specification.

## Brownfield Adoption

Do not attempt a DDD rewrite. Start where change and pain are highest:

- recover terminology and rules with domain experts;
- identify the core subdomain and protect new work around it;
- add an anticorruption layer around a harmful legacy model;
- extract or remodel one boundary only when economics and ownership support it;
- allow old and improved models to coexist during migration.

## Microservices Boundary Test

DDD can help discover service boundaries, but a bounded context is not required
to be a microservice. A service should be deep enough to hide meaningful
complexity, owned by one team, and cohesive in its business purpose. Splitting
below those boundaries increases network, coordination, consistency, deployment,
and observability costs without creating autonomy.

Use a modular monolith until independent deployment, scaling, ownership, or
failure isolation has demonstrated value. Do not use microservices to compensate
for unclear domains or team structure.

## Event-Driven and Data Boundaries

Event-driven systems require explicit public contracts and failure design; see
[[domain-driven-integration-and-reliable-messaging|Integration and Reliable
Messaging]]. Event sourcing inside a context is different from publishing events
between contexts.

Data mesh applies similar boundary thinking to analytical data: organize data
around domains, treat data as a product, give domain teams ownership, and provide
shared platform/governance capabilities. This is an organizational architecture,
not permission to fragment a small company's reporting stack. Centralized tables
and simple dashboards remain correct until scale and ownership justify a mesh.

## Source Coverage

Primary source: `raw/LearningDomainDrivenDesign.pdf`, PDF pages 204-380
(Parts III-IV, Chapters 10-16, conclusion, and applied case study). References and
index at 381-446 were reviewed and closed in
[[learning-domain-driven-design|the source hub]].

## Related Pages

- [[domain-driven-strategic-design-and-bounded-contexts|Strategic Design and Bounded Contexts]]
- [[domain-driven-integration-and-reliable-messaging|Integration and Reliable Messaging]]
- [[../distributed-systems/microservices|Microservices]]
- [[../devops/conways-law-and-organizational-design|Conway's Law and Organizational Design]]

