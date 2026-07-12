---
domain: tech
type: framework
tags: [priority/later, status/wiki-only, subject/devops, subject/theory-of-constraints]
---

# The Three Ways (DevOps)

**Summary**: Erik Reid's formal framework for IT Operations improvement — three guiding principles, explicitly built on Goldratt's Theory of Constraints, that define what to optimize for: fast flow of work, fast feedback, and a culture of continual experimentation/learning.

**Sources**: The Phoenix Project, thePhoenixProject.pdf (Ch. 15, 20, 22-23, 25-35; pp. 160-165, 207-214, 224-238, 246-339; Resource Guide "The Three Ways Explained", pp. 356-357)

**Last updated**: 2026-06-18

---

## How Bill earns the explanation

Erik doesn't explain the Three Ways until Bill has independently named all Four Types of Work (see [[four-types-of-work]]) and reported back on his own initiative — Erik treats this as confirmation Bill is "ready" (p. 161). Erik also validates that Bill, mostly by instinct, has already been practicing the *mechanics* of the First and Second Ways without having the vocabulary for them: the change-card whiteboard is effectively a **kanban board** providing visual management of WIP, which is "a critical part of the First Way" (p. 161), and the Brent-containment policy is the start of protecting the organization's constraint.

## The Three Ways, as named

1. **The First Way** — create fast and smooth flow of work as it moves from Development into IT Operations (and on to the customer). This is "what's between the business and the customer" (paraphrased from earlier naming, p. 91, and reaffirmed p. 161).
2. **The Second Way** — shorten and amplify feedback loops, so quality problems get fixed at the source instead of being discovered (and re-discovered) downstream. Erik frames the homework directly: "now you must continually eradicate your largest sources of unplanned work, per the Second Way" (p. 161) — i.e., the Second Way is partly *about* killing the antimatter described in [[four-types-of-work]].
3. **The Third Way** — create a culture that simultaneously fosters experimentation, learning from failure, and understanding that repetition and practice are the prerequisites of mastery (source: thePhoenixProject.pdf, p. 91).

## Resource Guide formalization

The Resource Guide makes the Three Ways less story-dependent and more operational:

- **First Way**: optimize the left-to-right flow from Development to IT Operations to the customer. The practices are small batches, short work intervals, not passing known defects downstream, optimizing for global goals instead of silo metrics, continuous build/integration/deployment, on-demand environments, WIP limits, and systems that are safe to change (source: thePhoenixProject.pdf, pp. 356-357).
- **Second Way**: create fast right-to-left feedback at every stage of the value stream so problems are prevented, detected, recovered from, and learned from quickly. The practices include stopping the line when builds or tests fail, making feedback visible, and embedding knowledge where the work actually happens so quality is created at the source (source: thePhoenixProject.pdf, pp. 356-357).
- **Third Way**: build a high-trust culture of continual experimentation and daily practice. The practices include automated test suites that keep code potentially deployable, shared goals and shared pain across Development and IT Operations, production telemetry visible to everyone, at least 20% of Dev/Ops cycles for nonfunctional requirements, and explicit reinforcement that improvement work is valued (source: thePhoenixProject.pdf, pp. 357-358).

## The First Way, unpacked via Theory of Constraints

Erik walks Bill through Goldratt's Five Focusing Steps (see [[theory-of-constraints#The Five Focusing Steps|TOC Step 1 — Identify the constraint]] through [[theory-of-constraints#The Five Focusing Steps|TOC Step 5 — Repeat, beware inertia]]), mapped directly onto IT Operations:

- **Step 1 — Identify the constraint.** Erik confirms Brent is Bill's constraint, but warns him to keep re-verifying this — "if you're wrong, nothing you do will matter" (p. 162).
- **Step 2 — Exploit the constraint.** Make sure the constraint never wastes time waiting on anything else, and that it's always working the highest-priority commitment IT Operations has made. Erik credits Bill with having already started this (reducing Brent's exposure to unplanned work and to the other three types of work) (p. 163).
- **Step 3 — Subordinate everything else to the constraint.** In TOC this is implemented via **Drum-Buffer-Rope**: in *The Goal*, Alex moves the slowest Boy Scout (Herbie) to the front of the hiking line so the whole troop's pace matches its actual constraint, then later releases plant work at the rate the bottleneck (the heat-treat oven) can consume it. Erik's explicit homework for Bill: figure out how to set the tempo of work released into IT Operations *according to Brent* — i.e., build IT's version of the job-release desk, now informed by where the real constraint sits (pp. 163-164). He also name-drops David J. Anderson's kanban techniques (developed ~20 years after *The Goal*) as the modern Dev/Ops implementation of this same idea, and notes Bill's change board is already close to one.
- Erik later sharpens the diagnosis: Brent is not literally the work center; he is a worker required by too many work centers. The practical First Way task becomes building the IT equivalent of a bill of materials/routing - a "bill of resources" that identifies prerequisites, work centers, routing, and capacity before new work is accepted (source: thePhoenixProject.pdf, pp. 208-213; see [[it-work-centers-and-kanban]]).

- Steps 4 and 5 arrive through the monitoring project. Because monitoring reduces outages, shortens troubleshooting, and prevents escalations to Brent, Erik treats it as constraint elevation, not optional tooling (source: thePhoenixProject.pdf, pp. 213-214). Bill later uses the same rule for internal IT projects: prioritize work that increases Brent's throughput or reduces unplanned work hitting him; safely release work that does not require Brent (source: thePhoenixProject.pdf, p. 231).

## The harder, second half of the First Way: knowing what NOT to do

Erik adds a point Bill almost misses: reducing WIP is only half the problem. The other half is knowing what work *shouldn't enter the system at all* — distinguishing work that serves real business objectives (projects, operations, strategy, compliance, security) from work that doesn't, regardless of who's demanding it. He uses the CISO (John, called "Jimmy" in Erik's mangled-names habit) as the negative example: John can't tell which audit findings actually matter to the business, so he treats all of them as equally urgent, which is the same undifferentiated-demand problem at the front door that unplanned work is at the back door (p. 164). Erik's framing: *"outcomes are what matter — not the process, not controls, or, for that matter, what work you complete."*

The audit thread makes this operational: compliance and security work must still be tested against business risk, flow, operational stability, recovery speed, Brent capacity, and WIP. Erik's rule for John is that security wins when it protects the organization without adding meaningless work to the IT system, and wins even more when it removes meaningless work from the system (source: thePhoenixProject.pdf, pp. 214-216, 222; see [[security-work-and-business-outcomes]]).

Part 2 expands the First Way beyond IT Operations itself. Erik says IT must gain an appreciation for the business system it operates inside: where business outcomes depend on IT, where IT risks jeopardize those outcomes, and where compliance controls are over-scoped because the business already mitigates the risk elsewhere (source: thePhoenixProject.pdf, pp. 253-255; see [[it-risk-and-business-value-chains]]).

## The Second Way becomes visible queues and handoffs

The first concrete Second Way lesson is not automated testing yet; it is queue visibility. Erik tells Bill that wait time grows rapidly as utilization rises: a resource at 90% utilization has about nine times the queue wait of a 50% utilized resource, and at 99% utilization the wait explodes to ninety-nine units (source: thePhoenixProject.pdf, p. 214). The practical lesson is that a system with no slack creates long hidden waits between steps.

Chapter 23 applies this to Phoenix environment work. A supposedly small Brent task turns out to be more than twenty steps across at least six teams, with much of the delay caused by queues and handoffs rather than touch time (source: thePhoenixProject.pdf, pp. 234-236). Patty's answer - kanban lanes, handoff control, and a "water spider" style expediter for critical work - is fast feedback about where work is stuck (source: thePhoenixProject.pdf, pp. 236-238).

At the end of Part 2, Erik names the next Second Way obstacle: batch size. The team has improved project flow, but Phoenix releases are still too large and too infrequent, so each deployment creates downstream recovery work and feedback arrives far too late (source: thePhoenixProject.pdf, pp. 286-287). His prescription is to continually reduce batch sizes toward single-piece flow and create faster feedback from IT Operations back into Development, designing quality into the product earlier instead of discovering failure at release time (source: thePhoenixProject.pdf, pp. 286-289).

Part 3 turns that prescription into Continuous Delivery. The team value-stream maps the deployment pipeline, marks prior failure points, standardizes environment creation, moves package creation upstream, automates deployment, and integrates tests into the build process (source: thePhoenixProject.pdf, pp. 300-307, 309-321; see [[deployment-pipeline-and-continuous-delivery]]). The result is a radically shorter feedback loop: Unicorn can deploy fixes within hours or days, and security tests run every time a developer commits code (source: thePhoenixProject.pdf, pp. 320-321).

## The Third Way becomes repeated improvement

The Third Way gets its first concrete narrative treatment through preventive work and the Improvement Kata. Erik connects Total Productive Maintenance, resilience engineering, fault injection, and Mike Rother's Improvement Kata around one idea: improving daily work is more important than merely doing daily work, because repetition creates the habits required for mastery (source: thePhoenixProject.pdf, pp. 213-214).

Patty then turns that idea into practice. Her service-request kanban includes measured steps, work instructions, checklist-driven handoffs, error-rate tracking, and two-week Plan-Do-Check-Act improvement cycles adopted from MRP-8 (source: thePhoenixProject.pdf, pp. 227-229). This is the Third Way as a management system: small repeated experiments that make the work safer, faster, and more learnable.

The narrative closes with Third Way fault injection. Project Narwhal/Chaos Monkey deliberately kills processes and servers, forcing Development and Operations to make services resilient; John's Evil Chaos Monkey applies the same idea to security by constantly attacking test and production environments (source: thePhoenixProject.pdf, pp. 328-330; see [[resilience-engineering-and-chaos-testing]]). Bill's final lesson is that quality and security should show up in daily work, not posters or occasional reviews.

## Connects to

- [[the-phoenix-project]] — tracker page.
- [[theory-of-constraints]] and [[theory-of-constraints#The Five Focusing Steps|TOC Step 1 — Identify the constraint]] through [[theory-of-constraints#The Five Focusing Steps|TOC Step 5 — Repeat, beware inertia]] — the Five Focusing Steps this framework is explicitly built on; Erik cites Goldratt and *The Goal* by name and walks through the steps in the same order.
- [[theory-of-constraints|The Goal (Goldratt) — Theory of Constraints]] — the Drum-Buffer-Rope/Herbie story Erik retells directly from this source.
- [[it-operations-bottleneck-management]] — Brent as the confirmed constraint; this page is the deeper TOC mechanics behind that diagnosis.
- [[four-types-of-work]] — the Second Way's goal (eliminate unplanned work) and the First Way's "know what not to do" point are both about controlling demand, just from different ends of the pipeline.
- [[change-management-failure-modes]] — the change-card whiteboard is reframed here as a kanban board, a recognized First Way mechanism rather than an ad hoc fix.
- [[it-work-centers-and-kanban]] - concrete implementation of flow, WIP visibility, queue-time feedback, standard work, and recurring improvement cycles.
- [[security-work-and-business-outcomes]] - the "know what not to do" lesson applied to compliance and security work.
- [[it-risk-and-business-value-chains]] - the First Way expanded into appreciation for the business system IT serves and the value chains it protects.
- [[deployment-pipeline-and-continuous-delivery]] - Part 3's concrete implementation of smaller batches, faster feedback, and deployable environments.
- [[business-experimentation-and-project-unicorn]] - the business payoff of applying the Three Ways to market experiments.
- [[resilience-engineering-and-chaos-testing]] - the Third Way rendered as continuous operational and security fault injection.
- [[devops-origins-and-myths]] - the Resource Guide's explanation of where DevOps came from and what it does not mean.
- [[devops-reading-map]] - the appendix's recommended reading list for the bodies of knowledge behind the Three Ways.
- think-python-interface-conditionals-recursion - the turtle case study's development plan (small working version → encapsulate → generalize → refactor only once the problem is understood) is the same small-batch, iterate-on-a-working-system discipline, applied to a single function instead of a release pipeline.
