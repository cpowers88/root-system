---
domain: tech
type: concept
tags: [subject/devops, subject/theory-of-constraints]
timeline: later
status: wiki-only
---

# IT Operations as a Bottleneck-Management Problem

**Summary**: The Phoenix Project's reframe of IT Operations management as an application of Theory of Constraints — work should be released into IT Operations at the tempo the constrained resource can absorb, not whenever a requester wants it, and any improvement made anywhere except at the bottleneck is wasted effort.

**Sources**: The Phoenix Project, thePhoenixProject.pdf (Ch. 1-7, 10-11, 20, 22; pp. 1-92, 111-124, 207-214, 224-233)

**Last updated**: 2026-06-18

---

## The pattern, dramatized

At Parts Unlimited, one engineer — Brent — is the only person who understands enough of the stack to fix almost anything. Every outage, every audit-remediation task, every pre-launch question routes to him. This creates a self-reinforcing loop the protagonist (Bill, the newly-forced VP of IT Operations) names directly: Brent is needed at planning meetings to tell developers how production really works, but he can never attend, because he's always busy fixing what's already broken. Planned work that would prevent future breakage never gets done, which guarantees more breakage, which keeps Brent unavailable (source: thePhoenixProject.pdf, pp. 55-56).

When Bill and his managers try to inventory "all our commitments" (business projects, internal IT projects, audit remediation, and unplanned break-fix work), they find: 35+ official business projects, 70+ internal IT projects nobody centrally tracks, compliance remediation alone that would consume their key resources for a full year, and break-fix work eating an estimated 75% of staff time — all routed through the same handful of senior people, with no visibility into who's already overcommitted (pp. 70-77). Steve, the CEO, refuses to cut scope or add headcount when shown this data — "use what you've got" (p. 97).

## Erik's reframe: the plant-floor analogy

Erik Reid, a board candidate posing as a delivery driver, takes Bill to a manufacturing plant and tells the story of a job-release supervisor named Mark, who for twenty years released jobs to the floor in pure first-come-first-served order — "it's a job that requires this work center first, and we're open" — with no regard for the bottleneck twenty stations downstream (pp. 88-89). The result was permanent work-in-process (WIP) pileup and chronic late shipments, fixed only once Goldratt's Theory of Constraints was applied: stop releasing work faster than the bottleneck can consume it.

Erik states the principle directly, citing Eliyahu Goldratt by name: *"any improvement made anywhere besides the bottleneck is an illusion."* Improvements made after the bottleneck stay starved waiting for the bottleneck to feed them; improvements made before the bottleneck just pile up more inventory in front of it (p. 90). He then names the job for Bill: *"Your job as VP of IT Operations is to ensure the fast, predictable, and uninterrupted flow of planned work that delivers value to the business while minimizing the impact and disruption of unplanned work, so you can provide stable, predictable, and secure IT service"* (p. 91).

In other words: IT Operations' most senior, most overloaded people (Brent) are the constraint. Until Bill controls *what gets released to them and when* — the IT equivalent of the job-release desk on the plant floor — no amount of "rigor and discipline" elsewhere in the organization will fix the throughput problem.

## Containing the bottleneck, and the trap that follows

Bill and his managers act on this directly: Brent is taken off all non-Phoenix work, all incoming requests are redirected to Wes, and a "level 3" engineer pool is created specifically to absorb escalations without involving Brent — with documentation mandatory and a rule that Brent is never allowed to fix the same problem twice without someone else learning to do it (pp. 113-117). The explicit goal is to stop the organization from getting "a little dumber" every time it lets Brent fix something nobody else can replicate (p. 116).

The policy immediately produces an unexpected side effect: 60% of scheduled changes stop completing, because change after change turns out to silently depend on Brent's involvement, and he's now walled off (pp. 119-120). Bill's insight, arrived at independently of Erik but recognizing the same shape: this is the same WIP-pileup problem as the plant floor, just relocated — *"Work piling up in front of the heat treat oven, because of Mark sitting at the job release desk releasing work. Work piling up in front of Brent, because of... the CAB."* The fix isn't to reverse the Brent policy (that would mean treating blocked changes as more important than Phoenix), it's to make Brent-dependency visible *before* a change is scheduled, so it can be resolved or routed to the level-3 pool ahead of time rather than discovered mid-implementation (pp. 121-123).

## The refined diagnosis: Brent is attached to too many work centers

In Part 2, Erik corrects Bill's simplified diagnosis. Brent is not the work center; he is a worker attached to too many work centers, each of which also needs a machine/tool, method, and measure (source: thePhoenixProject.pdf, pp. 208-211). If the hidden method stays in Brent's head, adding more headcount does not solve the constraint, because new people cannot execute work they do not understand (source: thePhoenixProject.pdf, p. 211).

This turns bottleneck management into knowledge extraction and standard work. Bill's level-3 pool, documentation rule, and "Brent never solves the same problem twice without someone else learning it" policy are no longer just escalation hygiene; they are how IT reduces the number of work centers that require Brent and creates future automation candidates (source: thePhoenixProject.pdf, p. 211).

The project-freeze restart uses this rule explicitly. Work can be released if it does not require Brent, and internal IT work should be prioritized when it increases Brent's throughput, reduces his workload, or reduces unplanned work that would hit him later (source: thePhoenixProject.pdf, pp. 212-214, 230-231).

## Connects to

- [[theory-of-constraints]] — this is TOC's core claim (the goal, the five focusing steps, the bottleneck-first principle) applied directly to a knowledge-work/IT context rather than a physical plant.
- [[theory-of-constraints|The Goal (Goldratt) — Theory of Constraints]] — Erik's plant story is explicitly framed as a retelling of Goldratt's heat-treat-oven bottleneck.
- [[four-types-of-work]] — the four categories of demand competing for the same constrained resources; bottleneck management requires seeing all four at once, which Bill's organization initially cannot do.
- [[change-management-failure-modes]] — a related but distinct failure: even once Bill tries to control the *flow* of change requests, his organization has no working mechanism to do so.
- [[it-work-centers-and-kanban]] - the concrete Part 2 mechanism for making Brent-dependency, routings, recurring work, queues, and handoffs visible enough to manage.
