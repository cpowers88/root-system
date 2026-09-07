---
type: research
timeline: reference
tags: [ai-automation, agentic-ai, adoption, verification]
source: raw/2605.14675v1.pdf
---

# Agentic AI in Industry: Adoption Level and Deployment Barriers

**Apostolou, Bosch & Holmström Olsson (Chalmers / Eindhoven / Malmö), arXiv:2605.14675, May 2026.**
Qualitative interview study — 16 practitioners, 12 companies (small to large,
fintech to automotive safety to pharma).

## One-paragraph summary

Companies were placed on a six-level agentic-AI maturity ladder (L0 individual
use → L5 self-optimizing systems). Seven of twelve sit at Level 1 (AI
assistants), four at Level 2 (task-specific agents), one at Level 3
(multi-agent orchestration). The headline finding: a **capability-deployment
verification gap** — four companies have working agentic capabilities *beyond*
their production maturity level but cannot deploy them, because no verification
mechanism other than human review is trusted, and human review doesn't scale
with generated output volume.

## The maturity ladder (useful reference)

| Lvl | Name | Description |
|---|---|---|
| 0 | Individual Use | Personal AI use, no organizational backing |
| 1 | AI Assistants | LLM tools enhancing productivity (Copilot etc.) |
| 2 | Task Agents | Agents own specific tasks (code review, docs, log analysis) |
| 3 | Collaborative AI | Human-managed multi-agent workflows across phases |
| 4 | System Builders | Autonomous generation of systems from high-level intent |
| 5 | Self-Optimizing AI | Self-healing systems without human input |

Notable: the most advanced adopters are *large or safety-regulated*
organizations, not small unregulated ones — organizational investment
outweighs regulatory drag. The one Level 3 company is the exception that
proves the rule: a small analytics shop in a low-risk domain with no
qualification requirements, built AI-native from the start.

## The four recurring barriers

1. **Context management in large industrial input** — codebases + docs exceed
   model capacity; RAG helps for well-structured docs and simple questions but
   fails on complex cross-cutting queries (11 of 12 companies).
2. **Underperformance on proprietary content** — proprietary languages,
   toolchains, protocols; RAG/LoRA/prompt-injection of docs mitigate but don't
   meet quality bars (all 5 companies with proprietary stacks).
3. **Non-determinism vs. qualification standards** — same prompt, different
   output across model versions; silent version changes; incompatible with
   safety-qualification requirements that a tool's behavior boundaries be
   documented. Static-analysis guardrails (SonarQube etc.) check code quality
   but not semantic correctness or regulatory intent.
4. **Data confidentiality** — cloud LLMs distrusted with sensitive code;
   mitigated via sandboxed local models at capability cost.

## The two-dimensional gap

- **Information asymmetry**: agents lack the fragmented, heterogeneous
  organizational context (code, tickets, regulations, architecture docs) that
  a human developer accumulates — "an unfair comparison."
- **Qualification absence**: no method exists to bound or certify probabilistic
  outputs, so human-in-the-loop stays the only trusted verifier — and it
  doesn't scale.

## Why this matters for this wiki / `.ROOT`

- The maturity ladder is a usable self-assessment lens for `.ROOT` itself
  (currently roughly L1–L2: assistant use plus task-owned session protocols).
- The paper's core lesson transfers directly: **progress is gated by
  verification, not capability**. Any proposal to give AI sessions more
  autonomy over `.ROOT` files should lead with the verification mechanism
  (review cadence, castle oversight), not the capability. The existing
  eyes-not-hands split between this wiki and `00-BRAIN\CASTLE` is exactly the
  human-in-the-loop pattern the paper says is the only trusted mechanism —
  and its scaling limit is worth watching as session volume grows.

Related: [[shift-to-agentic-ai-codex]] (delegation/verification at frontier),
[[2025-ai-agent-index]] (safety/transparency gaps ecosystem-wide).
