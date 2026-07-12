---
domain: tech
type: concept
tags: [priority/later, status/wiki-only, subject/microservices]
---

# Microservices

**Summary**: Why and how monoliths get decomposed into independently deployable microservices, the API gateway pattern that hides this decomposition from clients, the core design principles, and three essential resilience patterns (fail fast, circuit breaker, bulkhead) that stop a single overloaded dependency from cascading into a full outage.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 9)

**Last updated**: 2026-06-17

---

## From monolith to microservices

A **monolith** bundles all business logic, APIs, and data access into one deployed package — well understood, simple to test and deploy, and scales adequately via scale-up or scale-out (replicating the whole thing). It breaks down in two specific ways as a system grows: **code base complexity** (technical debt compounds, development cadence slows) and an **inability to scale selectively** — if one feature (e.g., a chat service) spikes in demand, you can only scale it by replicating the *entire* monolith, wasting resources on every other unrelated feature (source: Foundations of Scalable Systems.pdf).

**Microservices decompose the application into independent, self-contained services**, each with its own data storage where needed, each independently deployable and independently scalable. The named origin is Amazon's "two-pizza rule" — a team (and by extension, the service it owns) should be small enough to feed with two pizzas. The defining characteristic is **scope around a business capability**, not raw size (source: Foundations of Scalable Systems.pdf).

Decomposition isn't free, though — domain-driven design's "bounded contexts" are a starting point, but real systems have to balance domain purity against communication cost: two domains that need frequent, chatty cross-calls (e.g., "find funding by faculty") may be better merged, or have data deliberately duplicated across both services (accepting eventual-consistency cost) rather than paying constant network round trips.

## The API gateway pattern

Once an application is many independently-deployed services, clients can't reasonably track every service's location directly — that exposes backend refactoring to every client. An **API gateway** sits in front of all microservices as a single entry point, providing routing, authentication/authorization, per-API rate limiting, response caching, and centralized monitoring (source: Foundations of Scalable Systems.pdf) — essentially the façade pattern applied at the architecture level. Watch for the gateway itself becoming a new bottleneck under load (the same constraint-relocation lesson from [[application-services]] and [[theory-of-constraints#The Five Focusing Steps|TOC Step 5 — Repeat, beware inertia]]).

## Core principles (Sam Newman's list, with scalability commentary)

Modeled around a business domain; highly observable; hides implementation details; decentralizes workflow coordination (choreography — services talk peer-to-peer — vs. orchestration — one component owns the workflow logic, simpler to monitor but a potential bottleneck/SPoF); isolates failure; deploys independently; and requires a culture of automation (CI/CD) to actually realize the benefit of independent, frequent deployment (source: Foundations of Scalable Systems.pdf).

## Resilience: stopping cascading failures

This is the most operationally important material in the chapter. **Cascading failure**: service A calls B calls C. If C slows down (not crashes — slows), B's threads block waiting on C, B's thread pool fills up, B starts responding slowly to A, and the slowness propagates backward through the whole call chain (source: Foundations of Scalable Systems.pdf). This is more dangerous than an outright crash, because a crash fails fast and visibly — a slowdown just quietly consumes more and more resources until everything tips over at once. Naive client retries make it worse, not better, by adding load to an already-overwhelmed service.

Three concrete patterns guard against this:

- **Fail fast** — set an explicit timeout (e.g., the measured P99 response time) and return an error immediately rather than holding a thread indefinitely; combine with **throttling/rate limiting** at the load balancer or gateway so an overloaded service can reject excess requests outright rather than queueing them into oblivion. The book frames response-time targets in **percentiles, not averages** — a P50 of 200ms and P99 of 3000ms means 1% of 200M daily requests (2M requests) are 15x slower than typical, which matters enormously at scale even though the average looks fine.
- **Circuit breaker** — a client-side state machine wrapping calls to a dependency: CLOSED (normal) → trips to OPEN once an error-rate threshold is crossed (e.g., 25% of requests failing), during which all calls fail immediately with zero load sent to the struggling dependency → after a timeout, moves to HALF_OPEN to test with a trial request → CLOSED again if it succeeds, back to OPEN if it doesn't (source: Foundations of Scalable Systems.pdf). This is the single most important mechanism for letting an overloaded dependency actually recover instead of being continuously hammered by retries.
- **Bulkhead pattern** — named for ship hull partitioning: reserve a dedicated slice of a shared resource pool (e.g., threads) for a specific operation, so a surge in one endpoint's load can't starve every other endpoint sharing the same pool. A status-check endpoint and a heavyweight order-creation endpoint sharing one thread pool means an order-creation surge can starve status checks entirely — a bulkhead caps order-creation's thread usage so status checks always have capacity (source: Foundations of Scalable Systems.pdf).

## Connects to

- [[application-services]] — the API gateway, thread pools, and load-balancer concepts this chapter builds directly on.
- [[asynchronous-messaging]] — choreography between microservices is most often implemented via pub-sub messaging.
- [[serverless-processing]] — a common deployment target for individual microservices.
- [[theory-of-constraints]] / [[theory-of-constraints#The Five Focusing Steps|TOC Step 2 — Exploit the constraint]] / [[theory-of-constraints#The Five Focusing Steps|TOC Step 3 — Subordinate everything else]] — fail fast and bulkheads are exploit/subordinate moves at the request level: protect the constrained resource (threads, a downstream dependency) from being wasted on work that can't succeed or doesn't deserve priority.
- [[concurrency-fundamentals]] — thread pool exhaustion is the literal mechanism by which cascading failures propagate.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
