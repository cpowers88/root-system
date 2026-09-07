---
domain: technology
type: concept
timeline: reference
status: wiki-only
tags: [subject/ux, subject/requirements]
source_role: primary
use_cases: [tech-stack]
---

# User Experience Strategy, Scope, and Requirements

## Strategy Plane

Make both sides explicit:

- **product objectives:** what the organization expects the product to accomplish;
- **user needs:** what the targeted users need to accomplish and under what conditions;
- **success measures:** observable signals that show whether both were served.

Broad goals such as "improve efficiency" are not enough. Specify which user,
behavior, workflow result, or business measure should change. Conflicting
unstated objectives cause later design arguments that appear to be about screens
but are actually about strategy.

## User Evidence

Segment users by needs and behavior relevant to the product, not convenient
demographics alone. Use interviews, observation, usage records, support issues,
and usability tests. Personas can keep research visible, but should synthesize
real evidence rather than decorate assumptions. Existing detail lives in
[[../software-engineering/personas-scenarios-and-user-stories|Personas,
Scenarios, and User Stories]].

Minimum strategy record:

```text
Primary user:
Situation and task:
Current workaround:
User need:
Product objective:
Success metric and baseline:
Evidence source:
```

## Scope Plane

Strategy becomes scope when objectives and needs are translated into specific
functionality and content. Scope exists to state both what will be built and what
will not.

Separate:

- **functional requirements:** actions, system behavior, inputs, outputs, rules, and error responses;
- **content requirements:** information needed, its purpose, format, owner, volume, update cadence, and lifecycle.
- **technical requirements:** the required shape and behavior of the tool,
  interface, data, integration, performance, security, and recovery;
- **work-system requirements:** the roles, authority, skills, procedures,
  handoffs, controls, support, and working conditions needed for successful use.

Do not confuse a content format with the user need. "Add an FAQ" proposes a
format; the actual requirement may be fast access to recurring answers, which
could be solved in several ways.

A technically correct feature can still fail when the surrounding role,
procedure, authority, training, or support model is missing. Model the intended
technical change and intended work change in parallel, then test that the two
fit.

## Requirement Quality

A useful requirement is specific, testable, and free of implementation detail
unless the implementation is itself a constraint. Describe what should happen
and under what conditions. Record source, priority, dependencies, and acceptance
evidence.

Prioritize by:

1. contribution to product objective and user need;
2. consequence of omission;
3. frequency and reach;
4. dependency for later requirements;
5. implementation and maintenance cost;
6. risk and uncertainty.

When time is fixed, cut lower-value scope rather than quietly reducing usability
or reliability across every feature.

## Requirements Are Negotiated Evidence

Requirements are not objective facts waiting to be collected. Clients, users,
operators, maintainers, security owners, and developers can have legitimate but
conflicting views. Elicitation surfaces those views; specification records the
agreement reached and the disagreement or uncertainty that remains.

For every consequential requirement, record:

```text
Requirement:
Source stakeholder and observed evidence:
Affected work and technical component:
Conflict or constraint:
Priority and decision owner:
Acceptance scenario:
Change/version history:
```

Use a scenario or use case to bridge ordinary workflow language and formal
specification: name the actor, trigger, normal interaction, exceptions, system
response, and observable completion condition. Participation must happen while
requirements and designs can still change—not only when users are asked to
accept a finished system.

## Source Coverage

Primary source: `raw/UserExperience.pdf`, PDF pages 53-96 (Chapters 3-4).
Front-matter context and the remaining chapters are closed in
[[elements-of-user-experience|the source hub]].

Additional source: Paul Beynon-Davies, *Business Information Systems*, 2nd ed.
(2013), Chapter 12 physical PDF pp. 421-435 (book pp. 382-396), reviewed
2026-07-27 from
`03-WIKIS/TECHNOLOGY/raw/Business Information Systems 2nd Ed. Textbook.pdf`.
Retained stakeholder agreement, scenario/use-case bridging, and parallel
technical/work-system requirements; period-specific methods and examples remain
historical.

## Related Pages

- [[user-experience-five-plane-decision-model|Five-Plane Decision Model]]
- [[../software-engineering/personas-scenarios-and-user-stories|Personas, Scenarios, and User Stories]]
- [[../software-engineering/software-testing-levels-and-techniques|Software Testing Levels and Techniques]]
