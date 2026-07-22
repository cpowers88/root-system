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

Do not confuse a content format with the user need. "Add an FAQ" proposes a
format; the actual requirement may be fast access to recurring answers, which
could be solved in several ways.

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

## Source Coverage

Primary source: `raw/UserExperience.pdf`, PDF pages 53-96 (Chapters 3-4).
Front-matter context and the remaining chapters are closed in
[[elements-of-user-experience|the source hub]].

## Related Pages

- [[user-experience-five-plane-decision-model|Five-Plane Decision Model]]
- [[../software-engineering/personas-scenarios-and-user-stories|Personas, Scenarios, and User Stories]]
- [[../software-engineering/software-testing-levels-and-techniques|Software Testing Levels and Techniques]]
