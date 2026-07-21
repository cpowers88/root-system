---
type: research
timeline: reference
status: wiki-only
tags: [domain/technology, landscape, capability-gap, production-operations]
source: local capability and artifact audit plus current primary documentation, 2026-07-16
---

# Goal-Aligned Technology Gap Audit — July 16, 2026

**July 21 status note:** the integrated-operating-proof diagnosis remains useful,
but the scanner-first sequence and July 25 tracker assumption were superseded by the
live MCP Bootcamp, `NOW.md`, and `SYSTEM_FLAGS.md` #57. Current action belongs to
those owners. Retain this audit as the August 1 comparison baseline, not a second
technology frontier.

## Executive Verdict

Chris is not blocked by a shortage of advanced technology information. The vault
already explains SQL, Flask, APIs, distributed systems, DevOps, security,
observability, AI evaluation, human oversight, and industrial methods. The material
gap is **integrated operating proof**: no small application has yet been migrated,
tested in CI, served with a production server, observed, backed up, restored, and
rolled back as one system.

The correct three-horizon response is:

1. **Now:** deepen Python and SQL through the existing scanner and tracker; turn the
   scanner's brittle API boundary into a tested reliability lab.
2. **Near future:** wrap one justified workflow in a small Flask application and
   operate it to a minimum production standard.
3. **Future:** add governed AI or industrial methods only after a measured workflow,
   suitable data, and a simpler baseline justify them.

This preserves the North Star's Advisor-Builder sequence: observe and diagnose
first, then engineer and deploy the smallest response the evidence supports.

## Audit Method

The audit compared four kinds of evidence:

- the permanent goal and current Advisor-Builder strategy;
- July's live weak links and the eight-rung Advanced Application Capability Trace;
- retrieval coverage in TECHNOLOGY, PYTHON, and AI_AUTOMATION_SYSTEMS;
- working artifacts, especially the YouTube scanner and Academic Tracker.

Each capability is separated into **knowledge coverage** and **demonstrated proof**.
Having a page, book, tutorial, or AI-generated implementation is not evidence that
Chris can independently operate the capability.

## Eight-Rung Coverage Audit

| Rung | Knowledge coverage | Demonstrated proof | Real gap / next evidence |
|---:|---|---|---|
| 1. Python foundation | Strong staged curriculum and references | Stages 1-2 closed; Stage 3 active | Finish Stages 3-8 through independent build, explain, and debug gates |
| 2. Data and automation | Strong SQLite and SQL retrieval coverage | Tracker and scanner use real SQLite schemas | Reliable SQL with verified data: joins, aggregation, transactions, constraints, indexing, query explanation, and recovery |
| 3. Decision interface | Data Studio and visualization references exist | First private scanner dashboard verified | Show a named decision, calculation provenance, uncertainty, and an action another person can take |
| 4. Integration | Current API/integration landscape and webhook rules exist | Scanner consumes one public API; Make.com landscape rep complete | Retry/backoff, error classification, idempotency/run ledger, safe secret handling, and human-visible failure recovery in one flow |
| 5. Production application | Flask, SQLAlchemy, REST, authentication, UX, and testing references exist | No complete production-style app | One small application with a current architecture, migrations, permissions, validation, integration tests, and operator handoff |
| 6. Deployment and operations | Deep conceptual DevOps, security, telemetry, and resilience coverage | No deployed/recovered application proof | CI, production server, configuration, logs/metrics, backup, restore, rollback, defensive review, and an induced-failure drill |
| 7. Governed AI | Deep official-source coverage of Responses, evals, red teaming, privacy, HITL, and rollback logic | AI assists work, but no evaluated in-product feature | A bounded feature with task-specific evals, representative/edge/adversarial cases, human approval, privacy boundary, cost/latency log, monitoring, and disable path |
| 8. Industrial advanced application | Growing optimization, IoT, simulation, and manufacturing shelf | No justified industrial implementation | Wait for a measured industrial problem and suitable data; compare with a simpler baseline before adopting advanced methods |

## What Is Missing Now — 0 to 90 Days

### 1. Reliable SQL behavior, not more SQL reading

The immediate weak link remains SQL. The missing proof is a compact evidence pack
against live data:

- design or explain the schema, keys, constraints, and relationships;
- write joins and grouped calculations that answer named questions;
- make one multi-step write atomic with a transaction and verify rollback;
- inspect one query plan and justify an index;
- back up the database, restore to a separate file, and verify the restored result.

Use the scanner now. Switch the primary practice vehicle to verified Academic
Tracker data around July 25. Do not expand the tracker spec before real use reveals
the need.

### 2. API reliability at the failure boundary

The scanner's current `api_get()` exits immediately on HTTP or network errors. It
has quota accounting and an offline self-test, but no bounded retries, retry-after
handling, structured error classes, durable run ledger, or resume path. That makes
it the best existing artifact for the next integration proof.

The next proof should distinguish:

- retryable timeouts, connection failures, and rate limits;
- permanent authentication, permission, validation, and quota failures;
- safe retries for read operations with capped exponential backoff and jitter;
- a durable record of run start, outcome, error, and recovery action;
- a clear operator message that says what failed and what to do next.

### 3. Test extraction and continuous integration

The scanner has a useful monolithic `selftest`, but the system lacks a normal test
suite that runs on every change. Extract deterministic database, ranking, export,
and failure-path tests into pytest fixtures, then run them in GitHub Actions with an
explicit Python version and dependency definition. CI should be introduced before
deployment, not after the first production failure.

### 4. Restore confidence

Backups are described in the library but have not been proved on a live application.
For SQLite, use a consistent snapshot method such as its Online Backup API or
`VACUUM INTO`; do not treat an uncoordinated file copy of a live database as a
recovery plan. A backup does not count until a separate restore is opened and
checked.

## What Is Missing in the Near Future — 3 to 12 Months

### Minimum production application standard

The first real application should meet this standard without becoming a platform:

1. **Bounded workflow:** named user, decision, input, output, and non-goals.
2. **Application shape:** Flask application factory, modular routes, environment-
   specific configuration, and secrets outside source control.
3. **Data discipline:** SQLAlchemy 2.x transaction patterns, explicit constraints,
   and Alembic versioned migrations. Schema creation hidden inside startup code is
   not a migration strategy.
4. **Access and validation:** least-privilege roles, server-side validation, secure
   session settings, CSRF protection where needed, and a short threat review.
5. **Tests:** unit tests for business rules, database/integration tests, route tests,
   and at least one authorization and failure-path test.
6. **CI:** repeatable dependency install, explicit Python version, automated tests,
   and no plaintext secrets in workflows or logs.
7. **Serving:** a production WSGI server or managed hosting platform; never Flask's
   development server for non-development use.
8. **Observation:** structured logs first; then a small set of request, error,
   latency, and workflow-outcome metrics. Add distributed tracing only when the
   application has boundaries worth tracing.
9. **Recovery:** documented backup, verified restore, migration rollback or forward-
   fix plan, and one induced-failure drill.
10. **Operator handoff:** how to start, stop, inspect, recover, rotate a secret, and
    decide when to escalate.
11. **Economics:** build hours, monthly run cost, failure/rework avoided, adoption,
    and the condition under which the tool should be retired.

### Hosting decision remains intentionally open

Do not choose a cloud vendor before the application exists. The first deployment
decision should compare a managed Python platform against a small container-based
service on simplicity, private access, database needs, backup support, logs, cost,
and exit path. Docker is useful when reproducibility or the host requires it; it is
not a prerequisite for learning Flask or SQL.

### Security proof must match the actual threat model

The existing security library is sufficient to begin. The missing proof is using it
on a real app: identify protected data and actors, test authorization boundaries,
review dependency and secret exposure, set secure cookies/headers, constrain input,
and document incident/recovery actions. Compliance claims and legal conclusions
remain specialist territory.

## What Is Missing in the Future — 12 Months and Beyond, or Triggered Earlier

### Governed AI inside an operated workflow

The AI knowledge base is already ahead of present implementation needs. The future
gap is not another agent framework; it is a measured feature inside a stable
workflow. A valid proof requires:

- a narrow task and structured output contract;
- a task-specific evaluation objective and held-out set;
- normal, edge, and adversarial cases drawn from representative use;
- human review with easy access to the source evidence;
- privacy/data-retention and permission boundaries;
- model/version, prompt, latency, cost, failure, and override records;
- continuous evaluation after changes and a one-step disable or rollback path.

Start with a deterministic workflow plus one model call. Do not begin with a
multi-agent architecture.

### Data and platform scale

PostgreSQL, background queues, caching, containers, infrastructure-as-code, service
level objectives, and deeper OpenTelemetry become useful only when load, concurrency,
deployment frequency, or recovery needs exceed the simple system. The trigger is a
measured operating constraint, not professional appearance.

### Industrial and optimization methods

Simulation, optimization, digital twins, predictive maintenance, IoT, and swarm
methods are future option value. They become active when a real observation supplies
a decision, trustworthy measurements, an objective function, constraints, and a
baseline. Until then, maintain retrieval coverage and do not open a parallel study
lane.

## Ranked Practice Applications

| Rank | Application | Why it fits | Capability reach | Boundary |
|---:|---|---|---|---|
| 1 | **Scanner Reliability and Operations Console** | Existing real API, SQLite data, reporting code, dashboard, and known brittle failure boundary | Rungs 2-4 immediately; can prepare 5-6 | Internal only; do not turn it into a public content business or invent multi-user demand |
| 2 | **Academic Tracker Operating Proof** | Real personal workflow and verified data arrive around July 25 | Strong Rung 2; later decision-interface and recovery proof | Use V1 first; no speculative V2, scraping, or school-integrity shortcuts |
| 3 | **Observation-Derived Cost-to-Complete Cockpit** | Directly supports the Advisor-Builder offer and real-estate/construction access wedges | Rungs 3-7 if a real observation earns the build | No outreach or client-data intake without approval; Sheet/report before custom software |

### Selected first build

Select **Scanner Reliability and Operations Console**, but execute it as one gated
chain rather than a new broad project:

1. finish Python Stage 3 and run the bounded scanner SQL evidence pack;
2. extract pytest tests from the self-test;
3. add retry/error policy plus a durable run ledger and resume instructions;
4. add CI;
5. only then build a small read-only Flask operations view if it improves actual
   review or recovery;
6. deploy and perform a restore/failure drill only after the local version earns it.

The console may prepare Rung 5, but it does **not** close the multi-user application
proof unless a real second-user role and permission boundary exist. Do not manufacture
requirements merely to check a box.

## Explicitly Not Needed Now

- another broad batch of technology books;
- Kubernetes, microservices, service meshes, or event-streaming infrastructure;
- a vector database or RAG layer without a retrieval problem and evaluation set;
- multi-agent orchestration before one bounded model call is measurable;
- a custom CRM, intake platform, or client portal before workflow observation;
- paid hosting, automation subscriptions, or cloud accounts before a bounded proof;
- deeper swarm, digital-twin, quantum, or predictive-maintenance study.

These are not rejected forever. They are parked behind evidence triggers.

## Primary-Source Verification Set

- [Flask application factories](https://flask.palletsprojects.com/en/stable/patterns/appfactories/)
- [Flask testing](https://flask.palletsprojects.com/en/stable/testing/)
- [Flask production deployment](https://flask.palletsprojects.com/en/stable/deploying/)
- [Flask security considerations](https://flask.palletsprojects.com/en/stable/web-security/)
- [SQLAlchemy 2.0 unified tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- [SQLAlchemy transaction management](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html)
- [Alembic migration documentation](https://alembic.sqlalchemy.org/en/latest/)
- [GitHub Actions: build and test Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)
- [GitHub Actions secure-use reference](https://docs.github.com/en/actions/reference/security/secure-use)
- [SQLite Online Backup API](https://sqlite.org/backup.html)
- [Docker's Python guide](https://docs.docker.com/guides/python/)
- [OpenTelemetry Python getting started](https://opentelemetry.io/docs/languages/python/getting-started/)
- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [OpenAI safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices)

## Review Triggers

- **After Python Stage 3:** authorize the bounded scanner SQL/reliability proof.
- **Around July 25:** re-evaluate whether verified tracker data is the better SQL
  vehicle.
- **After one live workflow observation:** decide whether a Sheet/report is enough or
  a Flask application has earned development.
- **Before any deployment:** choose hosting from the actual app's requirements and
  complete the minimum operating checklist.
- **Before any AI feature:** define the task, eval set, human gate, privacy boundary,
  and rollback path first.
- **Monthly:** revisit this audit with `SKILL_GAP_ANALYSIS.md`; change the sequence
  only when live evidence changes the bottleneck.

---

*Audit date: July 16, 2026 | Next scheduled review: August 1, 2026, or earlier on a listed trigger.*
