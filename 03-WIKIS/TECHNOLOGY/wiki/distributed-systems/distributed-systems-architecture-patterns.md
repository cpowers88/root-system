---
domain: tech
type: concept
tags: [subject/distributed-systems]
timeline: later
status: wiki-only
---

# Distributed Systems Architecture Patterns

**Summary**: A "30,000-foot tour" of the concrete architectural moves used to scale a basic web app — scaling up vs. scaling out, load balancers and stateless services, distributed caching, distributing the database, multi-tier/BFF designs, async queueing for responsiveness, and the hardware-level limits of throwing more cores at a problem.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 2)

**Last updated**: 2026-06-17

---

## The starting point: basic multitier architecture

Virtually every system that eventually needs to scale starts the same way: a client tier, an application service tier (often a rapid-development framework — the book explicitly names Django alongside Rails), and a database tier (source: Foundations of Scalable Systems.pdf). This is exactly the shape built in [[django-fundamentals]]. This pattern is called a **monolithic architecture** — fine under light load, but as load grows, the single service becomes a bottleneck and latencies climb.

## Scaling up vs. scaling out

- **Scaling up**: give the existing server more CPU/memory (e.g., a bigger AWS instance). Simple, no code changes, but has a ceiling — eventually no single machine is big enough.
- **Scaling out (horizontal scaling)**: run multiple replicas of the service across multiple machines, splitting requests between them. Requires two things to actually work:
  1. **A load balancer** — a reverse proxy that distributes incoming requests across replicas, trying to keep each equally busy, and must itself be extremely low-latency since it sits in front of every request (source: Foundations of Scalable Systems.pdf).
  2. **Stateless services** — replicas must not hold any per-client session state locally, because the load balancer needs the freedom to route any client's next request to *any* replica. Session state (e.g., a shopping cart) instead has to live in a shared session store.

Scaling out is attractive for a second reason beyond capacity: it gives you availability for free. If a stateless replica crashes mid-request, the client just retries and another replica picks it up — no session state was lost because none was held locally.

## Scaling the database: caching, then distributing it

Scaling out the service tier eventually exposes the database as the new bottleneck. Two escalating responses:

1. **Distributed caching** — store frequently-read, rarely-changing results (the book's example: a weather forecast) in a fast in-memory store (Redis, Memcached) in front of the database. If 80%+ of reads can be served from cache, the database effectively gets that much spare capacity back "for free." Requires deciding an invalidation/expiry policy matched to how stale your data can tolerably be (source: Foundations of Scalable Systems.pdf).
2. **Distributing the database itself** — once a single database (even cached) can't hold/serve the data volume, split it across multiple nodes. Two broad families: distributed SQL (including "NewSQL" — born-distributed relational stores) and NoSQL (Cassandra, MongoDB, Neo4j-style), each handling data placement and rebalancing differently. (Deferred in depth to Part III of the book.)

## Multiple processing tiers and the BFF pattern

Real systems aren't one service calling one database — fulfilling a single Amazon.com page view can invoke 100+ internal services (source: Foundations of Scalable Systems.pdf). The same stateless/load-balanced/cached pattern composes: a service can call other (also replicated, load-balanced) services. A specific recurring shape is the **Backend for Frontend (BFF)** pattern — separate services tailored to web vs. mobile clients sitting in front of a shared core service, each scaled independently based on its own demand pattern.

## Increasing responsiveness with async queueing

Not every write needs to be confirmed-persisted before responding to the user. The book's example: a ski lift scanner doesn't need the rider to wait for a database write — the read event is acknowledged instantly and pushed onto a queue, with a separate consumer writing it to the database "eventually" (typically seconds later) (source: Foundations of Scalable Systems.pdf). This pattern — producer writes to a queue fast, consumer persists asynchronously — improves perceived responsiveness whenever the result of a write isn't immediately needed by the requester. (Queueing technologies covered in depth later in the book.)

## The limits of hardware scaling: Amdahl's law

Adding more CPU cores doesn't help if the code can't actually use them in parallel. **Amdahl's law** quantifies this: if 5% of code must run serially, adding more than ~2,048 cores has essentially no effect; if 50% must run serially, more than 8 cores stops helping (source: Foundations of Scalable Systems.pdf). This is the direct justification for why concurrent/multithreaded code design (see [[concurrency-fundamentals]]) is foundational, not optional, for scalability — money spent on bigger hardware is wasted past the point your code's serial sections cap the benefit. A cited real benchmark also shows upgrading database hardware can plateau in throughput gains well before the theoretical maximum, if the bottleneck has actually moved elsewhere (e.g., the service tier) — a direct illustration of "you must know where your constraint actually is before spending money," same lesson as [[theory-of-constraints#The Five Focusing Steps|TOC Step 1 — Identify the constraint]].

## Connects to

- [[scalability-fundamentals]] — the replication/optimization principles this chapter makes concrete.
- [[concurrency-fundamentals]] — Amdahl's law and why serial code caps the benefit of horizontal scaling.
- [[django-fundamentals]] — the exact starting monolithic architecture this chapter scales away from.
- [[theory-of-constraints]] / [[theory-of-constraints#The Five Focusing Steps|TOC Step 1 — Identify the constraint]] / [[theory-of-constraints#The Five Focusing Steps|TOC Step 4 — Elevate the constraint]] — load balancing is literally "balance flow, not capacity" applied to request routing; the bottleneck moving from app tier to database tier to wherever next is the same constraint-relocation cycle as [[theory-of-constraints#The Five Focusing Steps|TOC Step 5 — Repeat, beware inertia]].
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
