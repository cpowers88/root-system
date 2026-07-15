---
type: template
timeline: reference
status: active
template_for: decision-rule
tags: [decision-rule]
---

# Decision Rule: Name

> **Use:** copy and rename this file and title. Replace the copy's entire
> frontmatter with this block, choose one value from each `<...>` list and remove
> the brackets, add optional topics inside `tags`, then delete this instruction
> and example block.
> **Timeline:** `now` = apply now; `next` = on deck; `later` = deferred;
> `parked` = intentionally inactive; `reference` = use when needed.

```yaml
---
type: decision-rule
timeline: <now | next | later | parked | reference>
status: <active | retired>
tags: [decision-rule]
---
```

**Trigger**: The situation where this rule fires.
**Owner**: Chris decides; AI applies and flags.

## The Rule
Stated so a stranger could apply it. If/then, thresholds, no vibes.

## Why This Rule Exists
The failure mode it prevents (link the risk in [[north-star-roadmap]] or NORTH_STAR.md).

## Worked Example

## When to Break It
The named exception, if any. If none, say "none."
