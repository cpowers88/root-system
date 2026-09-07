---
type: research
timeline: reference
tags: [ai-automation, agents, workflows, reliability, economic-evidence, systems-engineering]
source: raw/2311.10751v2.pdf (ProAgent, 14 pp.) + raw/2510.25423v2.pdf (developer challenges, 15 pp.) + raw/2606.26118v1.pdf (Open Source Economic Index, 37 pp.); each reviewed in page-range chunks, 2026-07-15
---

# Agentic Automation: Architecture, Reliability, and Economic Evidence

Three previously untracked papers form a useful sequence: one proposes an
agentic workflow architecture, one measures where real agent developers
struggle, and one tests whether agents can perform occupation-grounded work.
Together they argue for bounded, observable workflow automation with explicit
contracts and human oversight—not unconstrained autonomy.

## Chunk A — ProAgent and agentic process automation (14 pages)

Ye et al.'s 2023 ProAgent paper distinguishes robotic process automation from
agentic process automation. Traditional workflows encode deterministic data and
control flow but cannot construct themselves or make flexible decisions.
ProAgent adds agents at two specific seams:

- a DataAgent handles unstructured or judgment-heavy data transformations;
- a ControlAgent chooses branches when fixed rules are insufficient.

Its Agentic Workflow Description Language uses JSON-shaped data contracts and
Python control flow. That choice is important: the model does not replace the
workflow substrate; it generates and operates inside an explicit, inspectable
representation. Routine steps remain deterministic while agent judgment is
localized.

Evidence limit: this is a 2023 proof-of-concept with case demonstrations, not
production reliability evidence. The reusable contribution is the separation of
deterministic workflow, data contracts, and bounded agent decisions.

## Chunk B — What agent developers actually struggle with (15 pages)

Asgari et al. analyzed 3,191 accepted-answer Stack Overflow questions and
64,098 issues from 18 agent-framework repositories. Their seven Stack Overflow
topics and thirteen GitHub topics converge into five challenge families:

1. environment, platform, and dependency management;
2. retrieval, embeddings, and memory;
3. orchestration and execution control;
4. model/tool interaction contracts; and
5. runtime reliability and operational robustness.

Installation, configuration, and prompting are highly visible and often fixed
relatively quickly. Retrieval, persistent memory, orchestration semantics, and
long-running execution are less visible but harder and longer-lived. UI and
workflow platforms create high issue volume; infrastructure issues are fewer
but persist longer. The paper's central interpretation is that agent development
has moved from a model-centric problem to a systems-engineering problem.

The practical design implications are explicit: make interaction contracts
stable across providers, treat memory as a lifecycle-managed subsystem, preserve
execution traces, and test long-running behavior rather than only prompt/answer
quality.

## Chunk C — Adoption versus task capability (37 pages)

Somerstep et al. build an open-source adoption index by mapping public WildChat
conversations to O*NET tasks, then construct occupation-grounded agent scenarios
using MCP servers and an OpenAI Agents SDK harness. From 3.2 million chats, the
pipeline retained about 1.67 million unique English chats, classified 789,768 as
occupationally relevant, and mapped 668,380 to at least one task. Finance,
computer/mathematical, and arts-related occupations were among the most
represented relative to the economy.

The benchmark result matters more than any single occupation ranking:
high-level workflow completion can look strong while granular tool selection,
grounding, and interpretation still fail. Multi-turn user collaboration improved
workflow completion but did not eliminate tool-call and grounding errors. The
authors therefore find theoretical capability ahead of observed adoption and
augmentation stronger than fully autonomous execution in their tested setting.

Evidence limits: the adoption data comes from one public chat corpus; task
mapping is model-assisted; the capability benchmark covers nine occupations and
one tested agent stack. It is evidence for a pattern, not a labor-market forecast.

## Combined system design verdict

The three sources converge on a serviceable architecture:

```text
business outcome and constraints
        -> explicit workflow and data contracts
        -> deterministic steps by default
        -> bounded agent decisions where judgment is needed
        -> trace, evaluation, human escalation, and rollback
```

For `.ROOT`, the important distinction is between orchestration and autonomy.
Persistent instructions, routing, logs, and review gates provide orchestration;
they do not require an agent to control every branch. For a client offer, the
credible wedge is to audit one workflow, locate the judgment seams, automate the
stable portions, and measure the result before expanding scope.

## Related pages

- [[mcp-landscape-architecture-and-patterns]]
- [[mcp-client-primitives-and-build-notes]]
- [[agentic-ai-industry-adoption-barriers]]
- [[shift-to-agentic-ai-codex]]
- [[enterprise-ai-adoption-and-production-roadmap]]
