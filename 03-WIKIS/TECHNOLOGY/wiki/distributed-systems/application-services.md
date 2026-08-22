---
domain: tech
type: concept
tags: [subject/scalability]
timeline: later
status: wiki-only
---

# Application Services: API Design, State, and Horizontal Scaling

**Summary**: How services expose business logic over HTTP (CRUD/REST APIs), why state management is the central design decision for scalability, how application servers process concurrent requests, and the mechanics of horizontal scaling via load balancers.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 5)

**Last updated**: 2026-06-17

---

## API design basics

Most modern services expose an HTTP CRUD API: `POST` (create), `GET` (read), `PUT` (update), `DELETE` (delete) against resources identified by URIs — not "pure" REST per Fielding's definition, but the dominant pattern in practice (source: Foundations of Scalable Systems.pdf). Two scalability-relevant design traps:

- **Chatty APIs** — designing an API around object-oriented `get()`/`set()`-per-property thinking forces multiple round trips to assemble one logical operation. Fix: `GET`/`PUT` the whole resource, or use `PATCH` for partial updates — minimize round trips, since each one costs real network latency (see [[distributed-systems-essentials]]).
- **Payload compression** (`gzip` via `Accept-Encoding`/`Content-Encoding`) can cut network latency 50%+ for large payloads, at a small CPU cost for compress/decompress — almost always a worthwhile trade.

## State management: the central design decision

**HTTP is nominally stateless, but most real services need to remember something between a client's requests** (a logged-in session, a shopping cart) — this is called **conversational state**. The design choice between stateful and stateless services is the single biggest scalability lever in this chapter:

- **Stateful services** keep session state in service memory. Simple to build, but two problems emerge at scale: memory grows proportionally with concurrent sessions (an unanticipated spike can exhaust it), and session timeout tuning is a no-win trade-off (too short = surprising data loss; too long = wasted memory) (source: Foundations of Scalable Systems.pdf).
- **Stateless services** require the client to supply everything needed to process each request independently, with conversational state pushed out to an external store (a distributed cache — see [[distributed-caching]]).

**Statelessness is the precondition for horizontal scaling** (see below) — a load balancer can only freely route a client's next request to *any* replica if no replica is privately holding state that request depends on.

## Application servers

An application server (Tomcat, JEE, Express.js, Flask, Spring) accepts requests, queues them if no thread is free, processes them on a pooled thread (see [[concurrency-fundamentals]]), and replies. Two resource pools bound capacity: the **thread pool** (e.g., Tomcat defaults to 25–200 threads) and the **database connection pool** (typically smaller, since DB connections are expensive). When the thread pool is bigger than the connection pool — common — threads queue for a connection, and **response time becomes "processing time + time spent waiting in queues,"** not just processing time (source: Foundations of Scalable Systems.pdf). A key operational lesson: **systems degrade well before 100% resource utilization** — contention (context switching, garbage collection) eats into useful work as any resource approaches saturation, so a sane utilization target (not "max it out") is a real design parameter, not an afterthought.

## Horizontal scaling and load balancing

**Horizontal scaling = stateless replicas + a load balancer.** Add replicas, and capacity grows roughly linearly; a load balancer decides which replica handles each request and is itself a critical-path component that must be extremely low-latency (source: Foundations of Scalable Systems.pdf).

- **Network (layer 4) load balancers** route on raw TCP/UDP packets and IP — fast, minimal features (NAT-based redirection).
- **Application (layer 7) load balancers** reassemble full HTTP requests and can route on headers/content (e.g., all `POST`s to a specific subset of replicas) — slower per-request, but far more capable. The book's own benchmark shows network LBs ~20% faster at moderate load, but the gap disappears once the backend replicas themselves saturate — **the load balancer type stops mattering once the real bottleneck is downstream of it** (a direct instance of [[theory-of-constraints#The Five Focusing Steps|TOC Step 1 — Identify the constraint]]: know where the actual constraint is before optimizing the wrong layer).
- **Load distribution policies**: round robin, least connections, header-based routing, HTTP-verb-based routing, plus per-replica weighting for heterogeneous hardware.
- **Health monitoring**: periodic pings pull unresponsive replicas out of rotation and reinstate them once healthy.
- **Elasticity**: replicas are added/removed automatically based on metrics (e.g., scale up above 70% average CPU, down below 40%) — either schedule-based (predictable load, like weekend event listings) or policy-based (reactive to live metrics). This is the cloud-era version of [[theory-of-constraints#The Five Focusing Steps|TOC Step 4 — Elevate the constraint]] — temporarily or permanently adding capacity at the actual constraint, automatically.
- **Session affinity / sticky sessions**: a load balancer feature that routes a given client's requests to the *same* replica, to support stateful services. The book is explicit that this should be a last resort — sticky sessions cause load imbalance over time as sessions of varying duration pile up unevenly across replicas, and complicate failure handling (a failed replica strands that replica's sessions). **Stateless design avoids this entire class of problem.**

A final point worth carrying forward: scaling one tier can simply relocate the bottleneck downstream — "adding eight traffic lanes for 50 miles will just cause bigger traffic chaos if the highway ends at a one-lane road." This is [[theory-of-constraints#The Five Focusing Steps|TOC Step 5 — Repeat, beware inertia]] in software form: solving today's constraint reveals tomorrow's.

## Connects to

- [[distributed-systems-architecture-patterns]] — the scale-up/scale-out and caching concepts this chapter makes concrete at the service-design level.
- [[concurrency-fundamentals]] — thread pools, queuing, and resource contention underpin everything in "Applications Servers" above.
- [[distributed-caching]] — the standard place to externalize state once a service goes stateless.
- [[theory-of-constraints]] / [[theory-of-constraints#The Five Focusing Steps|TOC Step 1 — Identify the constraint]] / [[theory-of-constraints#The Five Focusing Steps|TOC Step 4 — Elevate the constraint]] / [[theory-of-constraints#The Five Focusing Steps|TOC Step 5 — Repeat, beware inertia]] — load balancing, elasticity, and the "scaling one tier exposes the next bottleneck" lesson are direct software analogues of the Five Focusing Steps.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
