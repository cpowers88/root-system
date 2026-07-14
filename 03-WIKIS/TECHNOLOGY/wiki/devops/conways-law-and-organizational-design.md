---
domain: tech
type: framework
tags: [priority/later, status/wiki-only, subject/devops, subject/organizational-design]
---

# Conway's Law and Organizational Design for DevOps

**Summary**: How team structure determines system architecture (and vice
versa) — Conway's Law, the three organizational archetypes (functional,
matrix, market), and Etsy's Sprouter case study showing how a
well-intentioned integration layer became a coordination bottleneck because
it mirrored a three-team split instead of enabling one team to own the
whole path.

**Sources**: DEvOpsHandbook.pdf (Kim, Humble, Debois, Willis, *The DevOps
Handbook*, 2016), Part II, "Conway's Law in Mind" chapter

**Last updated**: 2026-07-13

---

## Conway's Law, Stated Plainly

Melvin Conway's 1968 observation, from an eight-person team split 5/3 across
a COBOL and ALGOL compiler project: the COBOL compiler shipped in five
phases, the ALGOL compiler in three. Conway's Law: "organizations which
design systems...are constrained to produce designs which are copies of the
communication structures of these organizations." Eric S. Raymond's
compressed version: "if you have four groups working on a compiler, you'll
get a 4-pass compiler." The practical implication for DevOps: team topology
isn't a separate concern from system architecture — it's the same
decision, made twice.

## The Etsy Sprouter Case Study

Etsy (pre-2009) split into two teams by layer: developers (PHP application
logic) and DBAs (Postgres stored procedures). "Sprouter" (stored procedure
router) was built to let each team work in its own layer without stepping
on the other. Conway's Law predicted the failure mode exactly: any business
logic change now touched **three** layers (application, stored procedure,
Sprouter itself) instead of two, and required coordinating **three** teams
instead of two — increasing lead time and making nearly every deployment
risk a mini-outage, because the layers were tightly coupled to each other
regardless of the interface designed to decouple them.

The fix (2009-2011, under new CTO Chad Dickerson) wasn't a better Sprouter
— it was eliminating the three-way split. Business logic moved entirely
into the application layer via a PHP ORM, cutting the number of teams that
had to coordinate on a business-logic change from three down to one. Two
years to fully migrate off Sprouter; Sprouter itself stayed in production
the whole time (an incremental strangler-pattern migration, not a rewrite).

## Three Organizational Archetypes (Fernandez)

- **Functional-oriented** — organized by specialty (DBAs, network admins,
  server admins as separate groups). Optimizes for expertise and career
  development; the traditional IT Operations shape. Causes long lead times
  on anything that crosses specialties — a large deployment means opening
  tickets with multiple groups and coordinating handoffs.
- **Matrix-oriented** — attempts to blend functional and market; in
  practice often produces individual contributors reporting to 2+ managers
  and achieves neither orientation's goal cleanly.
- **Market-oriented** — flat, cross-functional teams organized around
  customer/product outcomes rather than technical specialty. Amazon and
  Netflix's extreme version: each service team owns both feature delivery
  *and* service support for that service — no handoff to a separate Ops
  team at all.

## Why This Matters Beyond the Book's Own Framing

This is a structural companion to [[the-three-ways-devops]]'s First Way
(fast flow) — the Handbook's argument is that flow bottlenecks are often
an organizational-design problem in disguise, not a tooling problem. A
team stuck in a functional silo can adopt every CI/CD tool in
[[deployment-pipeline-and-continuous-delivery]] and still have slow lead
times if every deployment still requires cross-team ticket handoffs.
Conway's Law is the diagnostic lens for *why* a specific coordination
bottleneck exists before reaching for a process fix.

## Connects to

- [[the-three-ways-devops]] — the First Way's flow goal; this page is the
  organizational-design layer underneath it that the Phoenix Project's
  narrative (Brent as a shared, over-subscribed resource) already
  dramatizes without naming Conway's Law explicitly.
- [[it-work-centers-and-kanban]] — work centers as currently organized are
  themselves an instance of Conway's Law; this page names the underlying
  principle.
- [[deployment-pipeline-and-continuous-delivery]] — a deployment pipeline
  built across a functionally-siloed org will reproduce that silo's
  handoffs regardless of automation quality.
- [[devops-reading-map]] — no prior entry names Conway's Law directly;
  this closes that gap in the existing reading map.

## North Star Connection

Direct audit lever: when a client's "why is everything so slow" complaint
traces back to an org chart rather than a missing tool, Conway's Law is
the vocabulary for explaining *why* — and the Sprouter case study is a
concrete, non-abstract example to use with a client who's skeptical that
team structure (not tooling) is the actual constraint.
