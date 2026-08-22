---
domain: tech
type: concept
tags: [subject/serverless]
timeline: later
status: wiki-only
---

# Serverless Processing Systems

**Summary**: How serverless platforms (Google App Engine, AWS Lambda) eliminate manually-provisioned infrastructure for highly variable workloads, the cost/performance trade-offs hidden in their autoscaling configuration parameters, and a worked example of systematically tuning those parameters instead of guessing.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 8)

**Last updated**: 2026-06-17

---

## Why serverless

Some workloads are spiky in ways that are hard to provision for in advance — the book's example: an online ticket sale system might run at near-zero background load 99% of the time, then spike 10,000x for a few hours. Traditional IaaS (provisioned VMs, even with elastic load balancing from [[application-services]]) still means *some* resources are sitting idle most of the time, and you pay for them regardless of utilization. **Serverless platforms (AWS Lambda, Google App Engine) load and execute code only when a request arrives, scale automatically, and charge only for actual execution** — zero traffic, zero cost (source: Foundations of Scalable Systems.pdf).

This isn't free of architectural decisions, though — the book is blunt that cloud "sticker shock" is common (one survey found 69% of respondents routinely overspent cloud budgets by 25%+), usually from under-using autoscaling or simply not understanding a platform's cost model.

## Google App Engine vs. AWS Lambda

Both follow the same basic shape (upload code, platform manages scaling), but differ in mechanics worth knowing if choosing between them:

- **GAE standard environment**: can route *multiple concurrent requests to the same instance* up to a configured limit, and lets you set a minimum resident-instance count (paying to eliminate cold-start latency) and maximum (capping cost). Three interacting parameters control scaling: target CPU utilization, max concurrent requests per instance, and target throughput utilization (source: Foundations of Scalable Systems.pdf).
- **AWS Lambda**: one runtime instance handles exactly one request at a time — a burst of N simultaneous requests spins up N instances, each potentially paying a **cold start** cost (a few hundred ms for lightweight runtimes like Go/Node.js, a second or more for Java/.NET). Idle instances freeze (no cost) and eventually deactivate. **Provisioned concurrency** keeps a minimum warm pool to avoid cold starts, at a continuous cost. Memory allocation is the dominant tuning knob — CPU is allocated *proportionally* to memory, so more memory can mean both faster execution *and* lower total cost if the speedup outpaces the per-millisecond price increase (the book's worked example: doubling memory cut execution time 4x while only doubling the per-ms rate — net 50% cost reduction) (source: Foundations of Scalable Systems.pdf).
- Lambda's concurrency limit is shared across *all* functions in a region under one AWS account by default — one function's unexpected burst can starve another's capacity unless you set **reserved concurrency** per function.

## Case study: parameter tuning as a discipline, not guesswork

With even 3 interacting autoscaling parameters at coarse granularity, the combinatorial space is large (the book counts ~648 plausible GAE configurations from just 3 parameters at reasonable increments) — too many to explore by intuition. The book's prescribed method is a **parameter study**: pick the parameters that matter, choose a small number of values to test for each, run load tests across the resulting grid, then compare throughput *and* cost side by side (source: Foundations of Scalable Systems.pdf).

The result from their actual GAE experiment is the real lesson: **the platform's default configuration was neither the highest-throughput nor the lowest-cost option** — one alternate setting matched default performance at 55% of the cost; another beat default throughput at the same cost. Defaults exist to be reasonable for the platform vendor's general case, not to be optimal for any specific workload — a small, cheap experiment found double-digit-percent savings that intuition alone wouldn't have found.

## Connects to

- [[application-services]] — serverless autoscaling is the same elasticity concept from horizontal scaling, taken to its logical extreme (scale to zero).
- [[scalability-fundamentals]] — this chapter's parameter study is a direct, practical instance of "measure, don't assume" — the same lesson as the database hardware-upgrade benchmark in Chapter 2.
- [[microservices]] — serverless is one of the most common deployment targets for individual microservices, picked up again in the next chapter.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
