---
domain: technology
type: reference
tags: [priority/next, status/wiki-only, domain/technology, source-role/support, use-case/tech-stack, use-case/automation, subject/web-security, subject/flask, stack/flask]
---

# Web Application Security Basics: SQL Injection and CSRF

**Summary**: A minimal security checklist and definitions for the two vulnerability classes most likely to matter in a small Flask tool built for a client — SQL injection and Cross-Site Request Forgery (CSRF) — plus the general five-step approach to web app security the source recommends.

**Sources**: fullStackPython.pdf (Matthew Makai, 2020 Supporter's Edition), "Web Application Security" section (pp. 334–339)

**Last updated**: 2026-06-20

---

## Why This Narrow Slice Only

The source book is a 440-page survey of the entire Python web ecosystem (frameworks, ORMs, NoSQL, containers, serverless, CI/CD, enterprise monitoring) — almost all of it out of scope per the Source Filter, and the Flask/SQL portions are shallower surveys of ground already covered by dedicated sources (`FlaskWebDevelopment.pdf`, `PracticalSQL.pdf`). This page captures the one compact, non-redundant, directly useful section: basic web app security. Everything else in the book was deliberately left un-ingested.

## The Web Security Learning Checklist

A five-step approach to securing any web application, regardless of framework:

1. **Learn the major flaw categories** that attackers commonly exploit: CSRF, cross-site scripting (XSS), SQL injection, and session hijacking.
2. **Determine how your chosen framework already mitigates these** — most modern frameworks (including Flask, with extensions like Flask-WTF) have built-in protections that just need to be correctly enabled, not built from scratch.
3. **Verify your own code actually implements those mitigations** — a framework's built-in protection only helps if it's wired up (e.g., CSRF tokens included in every form).
4. **Think like an attacker** — actively try to break into your own application, or bring in someone with the experience to do so, before a client's data is at risk.
5. **Treat security as ongoing, not one-time** — popularity makes an application a more attractive target over time, so revisit security periodically rather than considering it solved after launch.

## SQL Injection

A category of vulnerability where unsanitized user input is concatenated directly into a database query, letting an attacker manipulate or extract data they shouldn't have access to. Affects both relational databases and NoSQL data stores. The standard defense is parameterized queries / using an ORM or query builder that escapes input automatically, rather than building SQL strings via string concatenation or formatting.

**Audit-usable rule**: any client-facing tool Chris builds that accepts user input and touches a database (a Flask form, an API endpoint) must use parameterized queries — this is a baseline, non-negotiable check before delivering any data-collecting tool.

## Cross-Site Request Forgery (CSRF)

A vulnerability that tricks an already-authenticated user's browser into submitting an unwanted action (e.g., a hidden form auto-submit) without the user's knowledge, because the browser automatically attaches the user's session credentials to any request to that site. The standard defense is a CSRF token: a unique, unguessable value embedded in each form that the server validates before processing the submission.

**Audit-usable rule**: any Flask form that performs a state-changing action (saving data, changing a setting) needs CSRF protection enabled — in Flask, this is typically handled by the Flask-WTF extension rather than something to build manually.

## Connects to

- [[sqlite-and-sql-with-pandas]] — the parameterized-query discipline described here applies directly to any raw SQL written when pulling data into pandas via sqlite3 or SQLAlchemy.

## North Star Connection

- How this applies to the audit business: a minimum-bar security checklist for any Flask tool built for a client — cheap insurance against shipping a client-facing tool with a basic, well-known vulnerability.
- Track relevance: Tech — baseline practice for any future Flask deliverable.
- Possible future Second Brain use: Not yet — this is a checklist to apply *while* building a tool, not itself a standalone deliverable; revisit once a Flask client tool is actually in progress.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | Baseline practice, not a differentiator, but non-negotiable hygiene for any client deliverable. |
| Current usefulness | 2 | No Flask client tool is in progress yet. |
| KSU support | 1 | Not coursework-related. |
| Tech-stack relevance | 4 | Directly tied to the Flask stack tag. |
| Business audit value | 2 | Protects deliverable quality rather than driving audit findings directly. |
| Data/workflow value | 2 | Security hygiene, not a data-workflow tool. |
| Reading urgency | 2 | Low until a Flask client tool is actually being built. |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Tech-stack decision / future reference

**Use when**:
Building any Flask form or API endpoint that accepts user input and touches a database.

**Do not use when**:
No client-facing Flask tool is currently in progress — this is a pre-build checklist, not standalone work.

**Fast retrieval query**:
`subject/web-security` + `stack/flask` — "SQL injection CSRF checklist"
