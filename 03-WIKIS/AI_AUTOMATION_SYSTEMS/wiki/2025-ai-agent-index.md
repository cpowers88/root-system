---
type: research
tags: [ai-automation, agentic-ai, ecosystem, safety, transparency]
source: raw/2602.17753v2.pdf (arXiv; same paper as raw/3805689.3806728.pdf, the ACM FAccT version — the third duplicate copy was removed from raw/ after the 2026-07-08 log flag)
---

# The 2025 AI Agent Index

**Staufer, Feng, Wei, Bailey, Duan, Yang, Ozisik, Casper & Kolt (Cambridge /
UW / Harvard / Stanford / MIT et al.), FAccT '26, arXiv:2602.17753.**
Systematic documentation of 30 deployed, general-purpose, high-impact agentic
AI systems across 45 fields each (1,350 total). Live index:
https://aiagentindex.mit.edu.

## One-paragraph summary

A census of the deployed agent ecosystem as of Dec 31, 2025, across six
categories: product, company/accountability, technical capabilities,
autonomy & control, ecosystem interaction, and safety/evaluation. Headline:
**transparency is poor exactly where it matters most** — 135 of 240
safety-related fields had no public information, only 4 of 30 agents have
agent-specific safety evaluations (ChatGPT Agent, OpenAI Codex, Claude Code,
Gemini 2.5 Computer Use), and most agents don't disclose their AI nature to
end users or third parties by default.

## The three agent form factors

1. **Chat applications with agentic tools** (12/30) — chat interfaces with
   extensive tool access; includes Claude Code, ChatGPT Agent, Manus. Lower
   autonomy (L1–L3), turn-based; but a single interface can span passive Q&A
   to autonomous web actions, so users may not anticipate when a request
   triggers real-world consequences.
2. **Browser-based agents** (5/30) — Comet, ChatGPT Atlas, Agent TARS.
   *Highest* autonomy (L4–L5), often no mid-execution intervention, and the
   concentration point for documented incidents (prompt injection via
   untrusted web content).
3. **Enterprise workflow agents** (13/30) — Copilot Studio, Agentforce, n8n.
   Split autonomy: L1–L2 during visual design, L3–L5 once deployed on event
   triggers. Safety framed as compliance (SOC 2 etc.), with agent-specific
   guardrails delegated to the deploying customer.

## Key ecosystem findings

- **Foundation-model concentration**: nearly all 30 agents run on GPT, Claude,
  or Gemini families — shared single points of failure (pricing, outages,
  safety regressions), but also a simplification for evaluators.
- **MCP is the dominant interoperability standard** (20/30 agents); A2A trails
  at 6/30, all enterprise.
- **Accountability fragmentation**: control is split across model provider,
  scaffolding/orchestration layer, agent builder, and deploying customer — no
  single entity bears clear responsibility, and model-level evaluations give
  false assurance about deployed agentic behavior.
- **Web conduct is unsettled**: agents acting "on behalf of users" routinely
  ignore robots.txt; some mimic human traffic. Only ChatGPT Agent
  cryptographically signs its requests (RFC 9421). Litigation is active.
- **Selective transparency ("safety-washing" risk)**: capability benchmarks
  get published; safety evaluations don't. Chinese-incorporated developers
  (5/30) mostly publish neither safety frameworks nor compliance standards.
- Claude Code was the only system with information available on all 8 safety
  fields.

## Why this matters for this wiki / `.ROOT`

- Best available **map of the deployed agent landscape** and its vocabulary
  (form factors, autonomy levels L1–L5 per Feng et al., MCP dominance) — a
  reference frame for evaluating any new agent tool before it touches
  `.ROOT` workflows.
- Practical tool-vetting heuristic from the findings: prefer tools with
  agent-specific system cards and documented sandboxing/stop controls;
  treat browser agents as the highest-risk category (autonomy high,
  disclosure lowest, prompt-injection incidents concentrated there).
- The "evaluations must target the deployed configuration, not the base
  model" argument mirrors `.ROOT`'s own logic: what matters is the system
  (files + protocols + tools), not the model in isolation.

Related: [[agentic-ai-industry-adoption-barriers]] (adoption-side view of the
same trust problem), [[shift-to-agentic-ai-codex]] (usage-side view of the
same ecosystem).
