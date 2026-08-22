---
domain: systems
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, process-mining, fairness, data-quality, privacy, transparency, audit]
---

# Responsible Process Mining - FACT Gate

**Summary**: Process mining can expose employees, customers, controls, and detailed
operational behavior even when its nominal target is a process. Before using a log,
model, prediction, or automation recommendation, test Fairness, Accuracy,
Confidentiality, and Transparency. A white-box diagram is not automatically fair,
accurate, private, or understandable.

**Source**: `Process Mining Handbook.pdf`, Chapter 12, "Responsible Process
Mining" (printed pp. 373-401; physical pp. 377-405), read in full.

**Last updated**: 2026-07-18

## The FACT Review

### Fairness

Process redesign affects people indirectly: which customers receive extra checks,
which workers appear slow, which exceptional cases disappear from the dominant
variant, and which tasks are automated or removed.

Ask:

- Are protected or vulnerable groups represented in the log and in infrequent paths?
- Could apparently slow workers be handling more difficult cases or receiving less
  support?
- Are proxy variables reproducing a sensitive attribute after the attribute itself was
  removed?
- Does optimizing the majority path degrade service for a minority with different
  needs?
- If a prediction triggers different treatment, which fairness definition fits the actual
  consequence, and what tradeoff does it impose?

Fairness through unawareness is insufficient. Sensitive effects can persist through
correlated attributes and system structure.

### Accuracy

Process-mining accuracy depends on both event data and model quality.

Ask:

- Do timestamps have enough precision to distinguish order from concurrency?
- Are case identifiers stable, complete, and appropriate for the analytical question?
- Do event labels carry consistent business semantics across systems and time?
- Is missing or inferred data explicitly marked rather than blended into observed data?
- Are fitness, precision, generalization, and simplicity interpreted for this purpose,
  rather than treated as universal scores?
- Does more or fresher data materially change the discovered behavior?

A perfectly fitted model of a poor log is still wrong. A simple model may hide
important rare behavior; a detailed model may be impossible for stakeholders to
interpret.

### Confidentiality

Event sequences are highly identifying. Replacing names with pseudonyms is often
insufficient because unique traces, timestamps, roles, and background knowledge can
reidentify a person or expose sensitive operational facts.

Ask:

- Which information is sensitive: identity, behavior, performance, health, customer
  attributes, controls, capacity, volume, or commercial procedure?
- What background knowledge could an insider, partner, or external party combine
  with the released data/model?
- Does the analysis need the full event log, a protected abstraction, or only an
  aggregated result?
- Who can access raw events, derived tables, models, screenshots, and exports?
- Can consent, access, correction, retention, and deletion obligations be traced across
  all source and derived data?

Protection methods trade utility for disclosure risk. Choose the smallest release that
still supports the decision, and document the remaining risk in language a non-expert
can understand.

### Transparency

Process models are often called white-box, but loops, silent transitions, filtering,
generalized paths, and hidden preprocessing can make them easy to misread.

Ask:

- Which behavior was filtered as infrequent, and could it contain important exceptions?
- Which paths are observed, inferred, allowed by the model, or impossible to determine?
- Can the intended stakeholder correctly interpret loops, optionality, concurrency,
  percentages, and missing data?
- Are the data lineage, transformation rules, parameters, and model version visible?
- Can a person challenge or override a prediction/recommendation and see why it was
  produced?

Judge the representation by the analyst's task and the affected stakeholder's ability
to understand it, not merely by whether the underlying notation has formal semantics.

## Decision Gate

| Result | Action |
|---|---|
| All four dimensions bounded and documented | Proceed with the named purpose and review trigger. |
| Material uncertainty but reversible/low-stakes use | Pilot with human review, restricted access, and explicit abstention conditions. |
| Unresolved privacy, fairness, or evidence-lineage risk | Stop deployment; redesign the data, representation, or decision boundary. |
| High-stakes automated action without traceable evidence and override | Do not automate. |

## Minimum Evidence Record

Every consequential analysis should preserve:

1. purpose, decision, users, and affected stakeholders;
2. source systems, extraction scope, case notion, event definitions, and exclusions;
3. data-quality tests, uncertainty, and inferred/repaired fields;
4. protected attributes or plausible proxies reviewed;
5. access, retention, disclosure, and release controls;
6. model/filter parameters and observed-versus-inferred behavior;
7. human interpretation, challenge, override, and escalation path;
8. post-deployment outcome and harm monitoring.

## Connects to

[[process-mining-engagement-and-value-realization]],
[[conformance-checking-and-kpi-driven-process-improvement]],
[[designing-for-human-error-and-recovery]], and
`03-WIKIS/AI_AUTOMATION_SYSTEMS/wiki/alignment-safety/algorithmic-fairness-metrics-ground-truth-and-intervention.md`.

## Use / Retrieval Notes

**Use when**: Event logs contain employee/customer/resource data, findings affect
work allocation or service, models are shared outside the analysis team, or process
mining drives predictions or automated actions.

**Proof**: An independent reviewer can trace the result to source evidence, explain
who could be harmed or exposed, identify uncertainty, and state the conditions that
would stop or reverse the use.

