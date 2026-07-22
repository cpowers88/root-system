---
domain: technology
type: reference
tags: [subject/api-security, subject/client-engagement]
timeline: next
status: wiki-only
source_role: primary
use_cases: [audit]
---

# API Security Testing: Engagement Scoping and a Consolidated Checklist

**Summary**: How a legitimate security-testing engagement gets scoped
(authorization, statement of work, testing depth) before any technical
work starts, plus the book's own consolidated checklist adapted into an
audit-ready review structure. The scoping material matters as much as the
technical checklist for Chris's audit business specifically — it's the
difference between a defensible client engagement and something that
looks like unauthorized access.

**Sources**: Hacking APIs.pdf (Corey Ball, No Starch Press, 2022), Chapter
0 ("Preparing for Your Security Tests"), pp. 3-9; Appendix A ("API
Hacking Checklist"), pp. 321-322.

**Last updated**: 2026-07-13

---

## Before Any Technical Work: Authorization

The book's own rule, stated bluntly: **never test an API's security
without a signed contract that explicitly grants authorization**, naming
the scope (which targets, which features, any exclusions) and the time
window. Two verification steps the book calls out as easy to skip and
important not to: confirm the person signing is actually authorized to
grant that permission, and confirm the client actually owns the assets
being tested (not a third-party host/vendor who'd need to separately
authorize it). This is the audit-business equivalent of "get it in writing
before you touch anything" — directly relevant if a security-review
service ever gets offered alongside build work.

## Testing Depth: Black Box, Gray Box, White Box

Three levels of information disclosed to the tester going in, chosen based
on what threat the engagement is actually modeling:

- **Black box** — the tester gets nothing but the company name; models an
  opportunistic outside attacker. Most of the effort goes into
  reconnaissance before any actual testing starts.
- **Gray box** — the tester gets scope boundaries, API docs, and often a
  basic user account; models a better-informed attacker (or is the
  realistic level for most paid engagements, since black-box recon burns
  billable time without adding much signal for a small client).
- **White box** — the tester gets source code, design docs, and internals
  access; models an insider threat and produces the most thorough result.

**Audit-usable rule**: match testing depth to a realistic threat model for
the client's actual size and risk profile — the book's own explicit
caution against over-scoping a small business as if it faced a
nation-state adversary applies directly to SMB client work generally, not
just security testing.

## The Consolidated Checklist (Adapted for an Audit Review, Not an Attack)

The book's Appendix A is written as an attack checklist; this is the same
structure reframed as a review checklist — confirm each item is *handled
correctly*, not attempt to break it.

**Scoping**
- [ ] Signed authorization/SOW in place, confirmed against the actual
  asset owner, before any testing begins.
- [ ] Testing depth (black/gray/white box) matches a realistic threat
  model for this client.

**Reconnaissance / Attack Surface**
- [ ] No secrets (API keys, tokens, credentials) exposed in client-side
  code, public repos, or documentation.
- [ ] API endpoint inventory is complete and matches what's actually
  documented and deployed (see Improper Assets Management, below).

**Endpoint & Documentation Review**
- [ ] API documentation matches the live API — no references to
  retired/undocumented endpoints still reachable.
- [ ] Responses reviewed for information disclosure, excessive data
  exposure, and business-logic assumptions that don't hold — see
  [[api-vulnerability-classes-owasp-top-10]] for the full ten-class
  breakdown.

**Authentication**
- [ ] Token generation has real entropy; no hardcoded tokens anywhere in
  client-reachable code.
- [ ] Rate limits specifically on login, password-reset, and MFA
  endpoints — not just general API rate limiting.

**Authorization**
- [ ] BOLA check: every object-ID-taking endpoint verifies the requester
  owns that object.
- [ ] BFLA check: every privileged endpoint verifies the caller's role,
  not just that they're authenticated.

**Input Handling**
- [ ] Mass assignment: incoming fields bound via an explicit allowlist,
  never blind pass-through to internal objects.
- [ ] Injection: all input sanitized/parameterized before reaching a
  database, shell, or interpreter (same baseline as
  [[../devops/web-application-security-basics]], extended to every input
  surface, not just SQL).

**Configuration**
- [ ] TLS enforced everywhere sensitive data moves.
- [ ] Default credentials rotated or disabled.
- [ ] Response headers reviewed for unnecessary version/framework
  disclosure.
- [ ] Retired API versions actually decommissioned, not just
  undocumented.

## Connects to

[[hacking-apis-source-summary]] (navigation hub),
[[api-vulnerability-classes-owasp-top-10]] (the ten vulnerability classes
this checklist's Input Handling/Authorization/Configuration sections
check against), [[../devops/web-application-security-basics]] (the
existing baseline this checklist extends for API-specific concerns).

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | A defensible, citable process for any future client API review or engagement scoping. |
| Current usefulness | 2 | No client API review is currently in progress. |
| KSU support | 1 | Not coursework-related. |
| Tech-stack relevance | 3 | Applies to any Flask/REST API work, not stack-specific otherwise. |
| Business audit value | 4 | The scoping/authorization section directly protects Chris if a security-review service is ever offered — legal/ethical grounding, not just technique. |
| Data/workflow value | 2 | Process checklist, not a data-workflow tool. |
| Reading urgency | 2 | Low until a client API review is actually being scoped. |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**: Pre-engagement scoping document if a client ever asks for
(or a build project ever warrants) an API security review — read the
Authorization section first, every time, before any technical checklist
item.

**Use when**: Scoping any engagement that involves testing or reviewing a
client's (or Chris's own) API for security issues.

**Do not use when**: No authorization/contract is in place — the book's
own rule is explicit that this checklist should never be run against a
system without signed permission first.

**Fast retrieval query**: `subject/api-security` + `subject/client-engagement`

## North Star Connection

- How this applies to the audit business: the authorization/scoping
  section is the legal and ethical guardrail for ever offering a
  security-review service — as important as the technical checklist, and
  the part most likely to be skipped without a source calling it out
  explicitly.
- Track relevance: Tech — process discipline for any future security-
  adjacent client offering.
- Possible future Second Brain use: Yes — this checklist is ready to use
  as-is the first time a client API review is actually scoped.
