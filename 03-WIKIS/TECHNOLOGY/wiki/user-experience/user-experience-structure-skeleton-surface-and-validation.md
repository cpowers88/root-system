---
domain: technology
type: concept
timeline: reference
status: wiki-only
tags: [subject/ux, subject/interface-design]
source_role: primary
use_cases: [tech-stack]
---

# User Experience Structure, Skeleton, Surface, and Validation

## Structure Plane

Structure turns requirements into behavior and organization.

**Interaction design** defines how the system responds to user actions, including
conceptual models, state, feedback, constraints, defaults, recovery, and errors.
Match the user's mental model where possible; when the system behaves differently,
make that difference visible and learnable.

**Information architecture** organizes information so users can find and
understand it. Choose structures and labels based on user tasks and language.
Common structures include hierarchical, sequential, matrix/faceted, and organic
networks. Metadata and controlled terminology make multiple routes possible.

Design error handling as part of the normal interaction, not an afterthought:
prevent predictable errors, explain what happened, preserve entered work, and
show a recovery path.

## Skeleton Plane

Three disciplines work together:

- **interface design:** controls and arrangements that make actions apparent;
- **navigation design:** movement, location, available destinations, and route back;
- **information design:** presentation that makes meaning and priority clear.

Wireframes combine these without prematurely committing to visual polish. A
wireframe should expose hierarchy, actions, navigation, information placement,
system feedback, and important states. Include empty, loading, error, permission,
and exception states, not only the happy path.

Wayfinding checks:

- Where am I?
- How did I get here?
- What can I do here?
- Where can I go next?
- How do I return or recover?

## Surface Plane

Visual design communicates relationships and priority through contrast,
uniformity, grouping, typography, color, imagery, and whitespace. Consistency is
both internal (the product behaves/looks coherently) and external (it respects
useful platform and organizational conventions).

Consistency is not sameness. Repeated elements should behave consistently;
differences should communicate a real difference in meaning or priority. A style
guide records recurring decisions so the system remains coherent as it grows.

## Validation

For every design decision ask: **Why did you do it that way?** The answer should
trace downward to a requirement, user need, and product objective, not taste.

Validation can be scaled to available resources:

1. walk a realistic scenario through all five planes;
2. test a wireframe or prototype with representative users;
3. observe confusion, errors, hesitation, recovery, and completion;
4. compare outcomes with the strategy-plane success measure;
5. correct the lowest plane causing the failure;
6. retest after the change.

UX work is a continuing discipline, not a cosmetic sprint at the end. Persistent
emergency delivery usually means upstream decisions were deferred until they
became expensive.

## Three-Layer Worth Test

Do not collapse "it works" into "it is valuable." Assess three different
properties:

| Property | Question | Example evidence |
|---|---|---|
| **Functionality** | Does the system perform the required actions correctly? | acceptance tests, output accuracy, error handling |
| **Usability** | Can the intended stakeholder use it effectively in the real task? | observed completion, errors, hesitation, recovery, satisfaction |
| **Utility** | Does its use improve the activity system or decision it exists to serve? | less delay/rework, better service, safer work, improved outcome |

The evidence chain is therefore:

```text
system and information quality
  -> stakeholder use and satisfaction
  -> individual/group impact
  -> organizational net benefit
```

Use is a precondition for impact, not proof of impact. A frequently used system
may be mandatory, burdensome, or merely shift work between stakeholders. Measure
both first-order effects (adoption and use) and second-order effects (changes to
work, coordination, control, service, cost, risk, or organizational performance).

Before recommending or validating a system:

1. identify internal and external stakeholder groups rather than one generic
   "user";
2. record each group's assumptions, expectations, knowledge, and definition of
   success;
3. test representatives in the real context of use;
4. separate interface satisfaction from system functionality and workflow
   utility; and
5. check whether the design changes autonomy, skill, task variety, monitoring,
   power, access, or switching cost for any stakeholder.

This extends the field-facing
[[user-centered-system-design-principles-and-tradeoffs|user-centered system
design review]] and supplies the post-observation technology gate used by
[[workflow-observation-method|the Workflow Observation Method]].

## Source Coverage

Primary source: `raw/UserExperience.pdf`, PDF pages 97-191 (Chapters 5-8 and
index). Index material was used only for retrieval confirmation. See
[[elements-of-user-experience|source hub]].

Supplemental source: Beynon-Davies, *Business Information Systems*, 2nd ed.
(2013), physical PDF pp. 313-327 (book pp. 274-288), selectively reviewed
2026-07-27 from `03-WIKIS/TECHNOLOGY/raw/Business Information Systems 2nd Ed.
Textbook.pdf`. Durable evaluation logic retained; period-specific ICT examples
remain historical.

## Related Pages

- [[user-experience-five-plane-decision-model|Five-Plane Decision Model]]
- [[user-experience-strategy-scope-and-requirements|Strategy, Scope, and Requirements]]
- [[../software-engineering/software-testing-levels-and-techniques|Software Testing Levels and Techniques]]
- [[../software-engineering/information-system-evaluation-lifecycle-and-failure-levels|Information-System Evaluation Lifecycle and Failure Levels]]
- [[user-centered-system-design-principles-and-tradeoffs|User-Centered System Design]]
- [[workflow-observation-method|Workflow Observation Method]]
