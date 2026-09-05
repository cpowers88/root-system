---
domain: technology
type: concept
timeline: reference
status: wiki-only
tags: [subject/ux, subject/product-design]
source_role: primary
use_cases: [tech-stack]
---

# User Experience Five-Plane Decision Model

## Core Model

User experience is the result of decisions that depend on one another from
abstract intent to concrete presentation.

| Plane | Decision question | Typical output |
|---|---|---|
| Strategy | What should the product accomplish for the organization and users? | Product objectives, user needs, success measures |
| Scope | Which functions and content will satisfy that strategy? | Prioritized requirements and exclusions |
| Structure | How will the system behave and how will information be organized? | Interaction flows, conceptual model, information architecture |
| Skeleton | Where are controls, information, and navigation placed? | Interface/navigation/information design and wireframes |
| Surface | How does the product communicate through visual and sensory treatment? | Visual hierarchy, typography, color, imagery, style guide |

Each higher plane is constrained by decisions below it. Work may overlap, but a
lower-plane change can invalidate higher-plane work. The model prevents teams
from treating a visible interface defect as automatically a color or layout
problem when its real cause is navigation, requirements, or strategy.

## Dual Nature of Products

Products often combine:

- **functionality:** users perform tasks through interaction design and interface controls;
- **information:** users find and understand content through information architecture and navigation.

The two tracks converge at the skeleton and surface. A dashboard, for example,
is simultaneously a tool for filtering/acting and an information product for
understanding status.

## Review Sequence

Ask from bottom to top:

1. Which business outcome and user need does this serve?
2. Which requirement authorizes this feature or content?
3. Does the interaction/information structure make the task understandable?
4. Can users find the action and recognize their location/state?
5. Does the visual treatment express priority and consistency?

If an answer fails, fix that plane before polishing above it.

## Advisor-Builder Application

Apply this to lightweight internal tools as a pre-build gate:

```text
Strategy: measurable business outcome + named user need
Scope: minimum functions/content + explicit exclusions
Structure: start-to-finish user path + error/exception paths
Skeleton: wireframe showing actions, navigation, status, and feedback
Surface: visual hierarchy and accessible styling after the above are sound
```

This fits the Technology Recommendation Ladder: first ensure the right process
and requirement exist, then decide whether configuration, integration, or a
light build is justified.

## Source Coverage

Primary source: `raw/UserExperience.pdf`, PDF pages 21-52 (Chapters 1-2),
with application guidance at 171-191. See
[[elements-of-user-experience|source hub]] for complete disposition.

## Related Pages

- [[user-experience-strategy-scope-and-requirements|Strategy, Scope, and Requirements]]
- [[user-experience-structure-skeleton-surface-and-validation|Structure, Skeleton, Surface, and Validation]]
