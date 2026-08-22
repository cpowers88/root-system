---
domain: technology
type: reference
tags: [subject/python]
timeline: next
status: wiki-only
source_role: reference
use_cases: [tech-stack]
stack: [flask]
---

# Task Queues for Background Jobs (Celery, RQ, Dramatiq)

**Summary**: Why a production Flask/Django app needs a task queue for slow
or scheduled work, and the landscape of Python task-queue libraries — the
natural next piece once [[flask-web-development]]'s toolkit needs to run
something outside the request-response cycle. Note on source style: this
book is a curated link directory more than a textbook — this page
synthesizes the conceptual framing, not a quoted narrative.

**Sources**: fullStackPython.pdf (Full Stack Python: 2020 Supporter's
Edition), §4.6 Task Queues (Celery, Redis Queue, Dramatiq).

**Last updated**: 2026-07-13

---

## Why Task Queues Exist

A web server (WSGI worker) should respond to an HTTP request as fast as
possible — each request ties up a worker process until the response
finishes. Any slow operation triggered by a request (an external API call,
a large database query, sending an email, processing an upload) should run
**outside** that cycle, asynchronously, so the worker frees up immediately.
A task queue is the mechanism for that: hand off the slow work to a
separate process (a "worker") that executes it in the background.

Concrete patterns this solves:
- **Precomputation as caching** — if a query is too slow to run during a
  request, run it on a fixed schedule in the background and store the
  result; the request just reads the precomputed value.
- **Spreading out bulk work** — large numbers of independent database
  writes, spread over time instead of all at once.
- **Scheduled/periodic jobs** — batch processes, recurring data pulls
  (e.g., polling an external API every 10 minutes).

## The Libraries

**Celery** — the de facto standard. The book's own explicit
recommendation: it has a real learning curve, but "put the effort in — it
is worth the time it takes to understand." Two distinct pieces worth
knowing by name: **Celeryd** (the worker daemon that actually executes
tasks) and **Celerybeat** (the scheduler that decides *when* — think of
Celerybeat as "the boss keeping track of when tasks should run," handing
jobs to Celeryd's pool of workers at the right time). Requires a message
broker (RabbitMQ or Redis) to pass jobs from the app to the workers.

**RQ (Redis Queue)** — the lighter alternative, explicitly positioned as
what to reach for when Celery feels like overkill for a simple use case.
Backed directly by Redis, low barrier to entry.

**Dramatiq** — a newer, "fast and reliable alternative to Celery,"
supporting both RabbitMQ and Redis as brokers.

**Other named options** (landscape-only, not evaluated further): Huey
(Redis-based, supports crontab-style scheduling), Kuyruk (built on
RabbitMQ), django-carrot (Django-specific lightweight option). Hosted
alternatives exist too — Amazon SQS, CloudAMQP (managed RabbitMQ) — worth
knowing as options when self-hosting a broker isn't wanted.

## Key Ideas

- The decision isn't "should I use a task queue" so much as "which slow
  function is currently running inside an HTTP request that shouldn't
  be" — the book's own suggested first step is auditing existing code for
  exactly that pattern.
- Celery is the default recommendation despite its learning curve because
  of ecosystem maturity; RQ/Dramatiq are the "simpler, lighter" answers
  when Celery's complexity isn't justified by the use case's actual scale.
- A task queue always needs a message broker (Redis or RabbitMQ) — this is
  additional infrastructure, not a pure code-level addition, and should be
  weighed against that operational cost for a small client-facing tool.

## Connects to

[[flask-web-development]] — this is the natural production-hardening
addition once a Flask app has any slow external call, scheduled job, or
bulk operation; the Flask page's own scoped ingest (Ch. 2-8, 14) didn't
cover deployment/production concerns, and this is one of them.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 2 | Relevant once a client tool needs background/scheduled work, not before |
| Current usefulness | 1 | No current client tool has this need yet |
| KSU support | 1 | Not coursework-related |
| Tech-stack relevance | 3 | A real, likely-eventual addition to the Flask-based stack |
| Business audit value | 2 | Relevant if a future client tool needs scheduled reports/data pulls |
| Data/workflow value | 2 | Same — scheduled data pulls are a task-queue-shaped problem |
| Reading urgency | 1 | Reference — no current trigger |

**Overall priority**: LATER (reference)

## Use / Retrieval Notes

**Use when**: A Flask (or any Python web) app needs to run something slow
or scheduled outside the request cycle — sending emails, calling a slow
external API, generating a report on a timer, precomputing a dashboard
value.

**Do not use when**: The "slow" operation is actually fast enough to run
synchronously, or when a simpler fix (caching, a faster query, an index)
solves the real problem — a task queue is real added infrastructure and
operational cost, not a free upgrade.

**Fast retrieval query**: `stack/flask` + `subject/python`

## North Star Connection

How this applies to the audit business: the natural next build once a
Flask client tool ([[flask-web-development]]) needs to do more than serve
requests — scheduled reports, background data syncs, slow third-party API
calls. Track relevance: Tech — production-readiness layer for the core
client-tool stack.
