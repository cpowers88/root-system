---
domain: tech
type: concept
tags: [subject/distributed-systems]
timeline: later
status: wiki-only
---

# Distributed Systems Essentials

**Summary**: The unavoidable realities of networked communication that every distributed system has to deal with — physical network characteristics, the IP/TCP/UDP stack, remote procedure calls, partial failures and idempotence, the impossibility of guaranteed consensus, and why clocks on different machines can't be trusted to agree.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 3)

**Last updated**: 2026-06-17

---

## Communications hardware: real numbers

Useful grounding data points: LANs run 10–100 Gbps at sub-millisecond latency; WANs are bounded by the speed of light through fiber (e.g., New York↔Sydney is a theoretical 53ms, ~80ms in practice) plus router hops; WiFi 6 tops out around 9.6 Gbps over tens of meters; 5G promises 1–2ms device-to-tower latency but only ~500m range, vs. 4G's 20–40ms latency and 10–15km range (source: Foundations of Scalable Systems.pdf). The practical point: physical distance and medium impose hard latency floors no software design can get around — minimizing the number of network hops a request takes matters.

## The IP stack, briefly

Four layers, lowest to highest: data link (device drivers/NICs) → internet (IP — addressing and routing) → transport (TCP/UDP) → application (HTTP, etc.). Key facts:

- **IP is best-effort** — no guarantee against corruption, loss, duplication, or out-of-order delivery (packet switching means different packets can take different paths).
- **TCP** is connection-oriented (three-way handshake), stream-oriented, and reliable via sequence numbers and cumulative acknowledgment — but this reliability is a deliberate trade-off against efficiency.
- **UDP** is connectionless and unreliable, but fast — appropriate where occasional loss is imperceptible (streaming, gaming, video calls) (source: Foundations of Scalable Systems.pdf).

## RPC/RMI: making remote calls look local

Sockets are the raw substrate (a bidirectional pipe identified by `<IP, port>` pairs) but are low-level and error-prone. RPC/RMI technologies (Java RMI, CORBA, gRPC, and ultimately REST-over-HTTP) exist to give remote calls the same syntax as local method calls, with a directory/registry providing **location transparency** — the server's network address can change without breaking client code (source: Foundations of Scalable Systems.pdf). Modern systems mostly settled on HTTP + JSON (REST-style) over older binary RPC mechanisms specifically because cross-language marshalling and stub/signature management became too costly to maintain at scale — directly relevant to why [[working-with-apis-python]]'s `requests`-over-HTTP pattern is the default today rather than something more exotic.

## Partial failures and idempotence

The central hard problem: when a client doesn't get a response, it **cannot distinguish** "the server crashed before processing," "the server processed it but the response was lost," and "the server is just slow" — these look identical from the client's side (source: Foundations of Scalable Systems.pdf). This uncertainty is called a partial/crash fault.

The standard fix is **retry-after-timeout**, but naive retries risk applying a mutating operation (e.g., a deposit) twice. The solution is making operations **idempotent**:

- Client attaches a unique idempotency key to every state-mutating request.
- Server checks a fast lookup store: if the key's already been seen, it's a retry — return the prior result without reapplying the operation; if not, apply the operation *and* record the key, as a single atomic unit (source: Foundations of Scalable Systems.pdf).
- Read-only requests are naturally idempotent and need no special handling.

This is directly actionable for any API design work — see [[working-with-apis-python]] and [[django-auth-and-forms]]'s form-handling pattern: any endpoint that mutates state (a `POST`/`PUT`) needs to consider what happens if the client's network call times out and retries.

## Consensus is provably impossible to guarantee — but works in practice

The **Two Generals' Problem** (two armies needing to agree on an attack time via messengers who might be killed) demonstrates that perfect consensus over an unreliable channel can never be guaranteed with certainty. The **FLP Impossibility Theorem** formalizes this: consensus on an asynchronous network with crash faults is impossible to guarantee within bounded time (source: Foundations of Scalable Systems.pdf). In practice this is a worst-case theoretical bound, not a practical blocker — real networks are fast and mostly reliable enough that timeout-and-retry algorithms achieve consensus routinely (covered concretely in the book's later distributed-database chapters). Worth distinguishing from **Byzantine faults** — malicious/lying nodes, not just crashed ones — which the book notes can mostly be excluded for systems running on trusted, secured infrastructure (the domain where they matter is things like blockchain consensus).

## Time can't be trusted across machines

Every node's clock drifts (commonly 10–20 seconds/day) due to temperature/voltage variation. NTP (Network Time Protocol) periodically corrects this via a global hierarchy of time servers, but correction can move a node's clock **forward or backward**, meaning a measured "end time" can appear earlier than a "start time" if NTP adjusted mid-measurement (source: Foundations of Scalable Systems.pdf). Two distinct clocks exist on every machine: a time-of-day clock (can jump due to NTP correction) and a monotonic clock (never goes backward, but can stall during VM suspension). **Practical takeaway: never compare timestamps across different nodes to determine event ordering** — this becomes critical later when reasoning about distributed database consistency.

## Connects to

- [[distributed-systems-architecture-patterns]] — the multi-tier, multi-service architectures whose communication this chapter explains the mechanics of.
- [[working-with-apis-python]] — the HTTP/JSON pattern this chapter explains the historical "why" behind, and idempotency as a concrete design requirement for any mutating API endpoint.
- [[django-auth-and-forms]] — form submission (POST) is exactly the kind of state-mutating request that needs idempotency handling if a client retries after a timeout.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
