---
domain: tech
type: framework
tags: [priority/later, status/wiki-only, subject/devops, subject/kanban, subject/theory-of-constraints, start]
---

# IT Work Centers and Kanban

**Summary**: *The Phoenix Project* turns the factory-floor idea of work centers into a practical model for IT work: recurring work should have known prerequisites, routings, accountable resources, visible queues, and explicit WIP control instead of disappearing into e-mail, tickets, and informal escalation.

**Sources**: The Phoenix Project, thePhoenixProject.pdf (Ch. 20, 22-23; pp. 207-214, 224-233, 234-238)

**Last updated**: 2026-06-18

---

## Work centers, not heroes

Erik corrects Bill's first answer that "Brent" is the constraint: Brent is not a work center, he is a worker who has become required by too many work centers (source: thePhoenixProject.pdf, pp. 208-210). The useful unit of analysis is the work center, made of "machine, man, method, and measure" - the tool or system being worked on, the people who can execute the work, the defined steps, and the outcome measures (source: thePhoenixProject.pdf, pp. 210-211).

This reframes the Brent problem. The organization has allowed too much recurring IT work to depend on hidden steps that only Brent knows, so the answer is not simply "hire more Brents." Until the method is documented and executable by other people, new hires would stand around waiting for Brent's tacit knowledge (source: thePhoenixProject.pdf, p. 211).

## Bill of resources

Erik calls the next artifact a "bill of resources": a bill of materials plus the required work centers and routing for a unit of IT work (source: thePhoenixProject.pdf, pp. 212-213). In IT terms, that means the prerequisites required before work can finish: hardware model, user information, software, licenses, configuration, security, capacity, and continuity requirements (source: thePhoenixProject.pdf, pp. 212-213).

The business value is scheduling honesty. Once IT knows the work centers, routings, work orders, and resources involved, it can tell whether it has capacity to accept new work rather than accepting everything and discovering hidden dependencies halfway through (source: thePhoenixProject.pdf, p. 213).

## Safe release criteria

When the project freeze is about to lift, Erik gives Bill a simple release rule: projects that do not require Brent are safer to release; projects that reduce Brent's workload, reduce unplanned work, or increase Brent's effective capacity should be prioritized as constraint-elevation work (source: thePhoenixProject.pdf, pp. 212-213, 231). Bill turns this into three internal project lists: work requiring Brent, work that increases Brent's throughput, and everything else (source: thePhoenixProject.pdf, p. 231).

The monitoring project becomes the clearest example. It does not require Brent, and it prevents outages and speeds diagnosis when outages occur, so it directly protects and elevates the constraint (source: thePhoenixProject.pdf, pp. 205, 213-214, 224-226).

## Kanban makes demand and WIP visible

Patty tests the factory analogy on common service requests: office moves, account changes, laptop/desktop provisioning, and password resets. She builds a kanban board with Ready, Doing, and Done columns, requires all work to enter through the board instead of e-mail or chat, documents the steps, identifies who can execute them, and measures how long each operation takes (source: thePhoenixProject.pdf, pp. 226-228).

The first result is tangible: the laptop replacement queue gets a publishable schedule, early configuration errors are folded back into the work instructions, and the team moves from roughly fifteen customer turns to a target of three by adding checklists at handoffs (source: thePhoenixProject.pdf, pp. 227-228, 232-233).

Patty then generalizes the pattern to project and change work. Cards are color-coded so the team can see the balance of business-priority work, internal IT improvement work, blocked work, and work connected to the top business projects; the same cards are linked back to the change-tracking tool so the visual system and system of record do not diverge (source: thePhoenixProject.pdf, pp. 229-230).

## Queue time is the hidden delay

Erik states the queue-time rule as: wait time equals the percentage of time a resource is busy divided by the percentage it is idle. At 50% utilization, wait time is one unit; at 90%, it is nine units; at 99%, it is ninety-nine units (source: thePhoenixProject.pdf, p. 214). The point is not the formula itself but the management implication: without slack, work spends most of its life waiting between steps.

Chapter 23 applies this directly to Phoenix environment work. What Brent estimated as a short task turns out to be more than twenty steps across at least six teams, with days lost at handoffs; even a "thirty-second" firewall change can take weeks if it waits in queues (source: thePhoenixProject.pdf, pp. 234-236). Patty's conclusion is the Second Way in practice: make handoffs, queue time, rework, and blocked work visible so the system can be improved instead of blaming the person attached to the visible task (source: thePhoenixProject.pdf, pp. 236-238).

## Connects to

- [[the-three-ways-devops]] - this is the narrative's first concrete implementation of the First Way, Second Way, and Third Way together: flow through work centers, visible feedback through queues/handoffs, and repeated improvement cycles.
- [[it-operations-bottleneck-management]] - the page gives the mechanics for turning "Brent is the constraint" into a manageable system instead of a personality diagnosis.
- [[change-management-failure-modes]] - Bill's first whiteboard CAB was a visibility patch; Patty's kanban boards are the more general version for recurring work and project flow.
- [[four-types-of-work]] - the colored-card system helps distinguish business projects, internal IT work, changes, and blocked/unplanned work at a glance.
- [[theory-of-constraints#The Five Focusing Steps|TOC Step 3 — Subordinate everything else]] - safe project release and WIP limits are the IT version of subordinating work release to the constraint.
- [[theory-of-constraints#The Five Focusing Steps|TOC Step 4 — Elevate the constraint]] - monitoring, standard work, documentation, and checklists are elevation moves because they increase usable constraint capacity without simply adding headcount.
