---
domain: tech
type: concept
tags: [priority/later, status/wiki-only, subject/caching]
---

# Distributed Caching

**Summary**: How application-level caches (Redis/Memcached) and the internet's own multilevel web-caching infrastructure (HTTP cache headers, CDNs) reduce load on databases and origin servers — the caching patterns available, and how to control freshness vs. staleness.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 6)

**Last updated**: 2026-06-17

---

## Application caching

A distributed cache (Redis, Memcached — both essentially distributed in-memory hash tables) sits between a service and its database. Basic flow: check cache → **hit** → return cached value; **miss** → query the database, write the result to cache, return it (source: Foundations of Scalable Systems.pdf). Each cached entry gets a **TTL (time to live)** — after which it's evicted as stale, forcing the next request to recompute and refresh it.

The economics are stark: caching is cheap relative to scaling the database itself — the book cites ~3% of Twitter's infrastructure being dedicated to caching, which is a small price for taking massive read load off the database. The design goal is **maximizing cache hit rate**, which depends on the read:write ratio of the underlying data — frequently-updated data invalidates its own cache entries constantly, eroding the benefit. Monitoring hit/miss counts in production (most cache technologies expose this natively) is essential to confirm a caching scheme is actually paying for itself.

Four named caching patterns, differing in who's responsible for keeping cache and database in sync:

- **Cache-aside** — application code explicitly checks the cache, and on a miss queries the database and populates the cache itself. Most common in massively scalable systems because it degrades gracefully: if the cache is unavailable, every request just becomes a (slower) miss — the system stays up, just slower (source: Foundations of Scalable Systems.pdf).
- **Read-through** — the cache itself has a "loader" that transparently fetches from the database on a miss; application code only ever talks to the cache.
- **Write-through** — writes go to the cache first, which synchronously propagates to the database before the request completes.
- **Write-behind (write-back)** — like write-through, but the database write happens asynchronously after the cache write — faster responses, at the risk of losing the update if the cache crashes before the DB write completes.

## Web caching: the internet's built-in cache layers

Beyond application caching, HTTP itself has a multilevel caching infrastructure: browser caches (private, single-user) → ISP/organizational proxy caches (shared) → **CDN/edge caches** (geographically distributed — Akamai alone serves up to 30% of global internet traffic from 2,000+ locations) (source: Foundations of Scalable Systems.pdf). These only cache `GET` responses, keyed by URI, and are controlled entirely through HTTP response headers — no application code changes required:

- **`Cache-Control`** — `no-store` (never cache, for sensitive data), `no-cache` (must revalidate before use), `private` (browser-only), `public` (any proxy can cache), `max-age=N` (freshness window in seconds).
- **`Expires`** / **`Last-Modified`** — fallback freshness signals if `max-age` isn't set.
- **`Etag`** — an opaque version identifier for a resource. When a cached copy goes stale, the cache sends a conditional request (`If-None-Match`) back to the origin; the origin replies `304 Not Modified` (no body, just confirms the cached copy is still valid) if the Etag still matches, or `200` with a fresh body and new Etag if it's changed (source: Foundations of Scalable Systems.pdf). This **revalidation** pattern avoids re-sending large unchanged payloads while still guaranteeing correctness.

Web caching is most valuable for static or slowly-changing data (images, video, infrequently-updated reports) — exactly the same "skewed toward reads, rarely updated" profile that makes application caching effective.

## Connects to

- [[application-services]] — caching is the standard mechanism for externalizing state once a service goes stateless, and for protecting the database tier as services scale out.
- [[distributed-systems-architecture-patterns]] — this chapter is the detailed version of the caching layer introduced briefly when scaling the database tier.
- [[theory-of-constraints#The Five Focusing Steps|TOC Step 2 — Exploit the constraint]] — a cache is a literal "exploit the constraint" move: rather than adding database capacity (an elevate-tier spend), you squeeze more usable throughput out of the existing database by routing most reads around it entirely.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
- think-python-lists-dicts-tuples — memoization (caching a function's computed results in a dictionary to skip recomputation) is this same cache-aside logic running inside a single process, on a much smaller scale.
