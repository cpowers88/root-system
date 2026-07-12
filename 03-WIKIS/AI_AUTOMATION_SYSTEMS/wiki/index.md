---
type: map
tags: [now, ai-automation]
---

# AI_AUTOMATION_SYSTEMS Wiki — Index

### Scope: AI tooling, agent patterns, and automation research generally — plus self-evolution research on `.ROOT` itself. Researches and proposes; `00-BRAIN\CASTLE` reviews and maintains.

## Status

Operational as of July 8, 2026. Seven research batches ingested (agentic-AI
papers; AI Agent Index detail data; MCP docs + NIST AI RMF; WTI series +
OECD AIM; LLM-wiki pattern batch; Pereira O'Reilly book; Claude Code official
docs pack), two self-evolution proposals approved and promoted. **raw/ fully
processed as of July 12, 2026 (session 13)** — the July 9 processed state
plus the `CLAUDE_FILES/` pack (moved here from `00-BRAIN\CASTLE\raw\books\`
July 12, correctly relocated to this wiki's intake lane) now read in full
and routed into five pages. See `log.md`.

## Pages

- [Agentic AI in Industry: Adoption Level and Deployment Barriers](agentic-ai-industry-adoption-barriers.md)
  — interview study; the capability-deployment **verification gap**; six-level
  maturity ladder; four recurring barriers (context, proprietary content,
  non-determinism, confidentiality).
- [The Shift to Agentic AI: Evidence from Codex](shift-to-agentic-ai-codex.md)
  — OpenAI usage data; delegation vs. consultation; skills/**systematization**
  as the frontier lever; concurrency and long-running agents; empirical
  validation of the `.ROOT`-style persistent-procedural-context pattern.
- [The 2025 AI Agent Index](2025-ai-agent-index.md)
  — census of 30 deployed agents; three form factors (chat / browser /
  enterprise); MCP dominance; safety-transparency gaps; tool-vetting
  heuristics.
- [`.ROOT` Maturity Self-Assessment](root-maturity-self-assessment.md)
  — first self-evolution rep: `.ROOT` sits at L1 solid / L2 emerging on the
  agentic maturity ladder; verification capacity (not capability) is the
  gate to watch; baseline for future drift checks.
- [Agent-Tool Vetting — Worked Examples](agent-vetting-worked-examples.md)
  — 8 agents scored against the promoted vetting screen using per-agent
  Index data: CLI agents (Claude Code, Codex) are the only clean passes;
  builders fail evals/sandboxing; n8n and HubSpot Breeze can't stop a
  running agent; Comet is the failing-grade contrast row.
- [MCP Landscape — Architecture, Primitives, and Scaling Patterns](mcp-landscape-architecture-and-patterns.md)
  — the long-open MCP rep: host/client/server model, six primitives,
  transports, deployment paths; **progressive tool discovery** and **code
  mode** as the context-economy patterns — the `.ROOT` router pattern,
  formalized by the official docs.
- [MCP Security and Authorization — Threat Catalog](mcp-security-and-authorization.md)
  — eight named attack classes (confused deputy, token passthrough, SSRF,
  session hijacking, local server compromise, OAuth URL injection, stdio
  proxy escalation, scope inflation); OAuth 2.1 essentials; the depth
  layer under the Category 10 vetting screen.
- [NIST AI Risk Management Framework (AI RMF 1.0)](nist-ai-rmf.md)
  — GOVERN/MAP/MEASURE/MANAGE, seven trustworthiness characteristics;
  formalizes the verification-gap finding and supplies citable audit
  vocabulary for client work; `.ROOT` mapped onto the four functions.
- [MCP Client Primitives in Depth + Build Notes](mcp-client-primitives-and-build-notes.md)
  — second-pass extraction: trust semantics of elicitation/roots/sampling
  (**roots are advisory, not security**), the stdio never-log-to-stdout
  rule, and an operational debug quick-reference for MCP servers on this
  machine.
- [Microsoft Work Trend Index 2024 → 2026 — The Adoption Arc](work-trend-index-2024-2026.md)
  — three-report series: BYOAI baseline (78%) → infinite-workday waste
  telemetry (interruptions every 2 min) → the **Transformation Paradox**
  (org factors drive 2× the AI impact of individual skill; only 19% of AI
  users sit in orgs ready for them). Independent confirmation of the
  verification-capacity finding + Tier 1–2 audit ammunition.
- [OECD AI Incidents Monitor (AIM)](oecd-ai-incidents-monitor.md)
  — live catalog of ~16,300 AI incidents/hazards, filterable by harm type,
  business function, and autonomy level; the incident-history lookup for
  the vetting screen and the failure-evidence counterweight to the
  capability sources.
- [The LLM-Wiki Pattern and Its Second-Brain Implementations](llm-wiki-pattern-and-second-brain-tools.md)
  — Karpathy's pattern + three implementations compared against `.ROOT`
  practice; what was adopted into the Wiki Shared Layer (lint,
  update-over-create, contradiction flags, recency markers) and what was
  rejected (hot cache, self-rewriting scheduled agents).
- [Workflow Automation Tools — 2026 Landscape Snapshot](workflow-automation-tools-landscape.md)
  — Zapier-blog category map (10 tools, pricing as of 2026-06) with a
  provenance warning (Make.com omitted by its rival); the
  automation-first vs. built-in-automation split as an audit lever
  ("turn on what the client already pays for"); cross-checked against
  the vetting page's harder findings on Zapier/n8n/HubSpot.
- [Generative AI for Software Development (Pereira, O'Reilly 2025)](generative-ai-for-software-development-pereira.md)
  — 171-pp. book distilled: SDLC-wide tool map with a reusable two-stage
  evaluation method; the Levels-vs-Shopify adoption contrast (the three
  blockers solo builders don't have); Shopify's prompting + doubled code
  review = **third independent confirmation of the verification-capacity
  verdict**; the ATM/elevator/Excel jobs thesis ending in "AI integration
  specialist." Ratings are a 2025-04 snapshot — trust the method, verify
  the tools.
- [Stanford AI Index 2026 — The Measurement-Gap Edition](ai-index-2026.md)
  — the neutral annual dataset: frontier convergence (4 labs within 25
  Elo), benchmarks saturating while labs disclose less, incidents 362
  (+55%), org adoption 88% with single-digit agents, GenAI at 53%
  population adoption in 3 years (US 24th), entry-level dev employment
  −20%. **Fourth independent confirmation of the verification-capacity
  verdict**, at ecosystem scale. Raw PDF lives in TECHNOLOGY raw/;
  economy data routed to BUSINESS market-map, education data to
  EDUCATION.
- [Claude Code — Context, Memory, and Instruction-File Economics](claude-code-context-and-instruction-economics.md)
  — the two memory channels (CLAUDE.md vs. auto memory); CLAUDE.md load
  mechanics (HTML-comment stripping, root-to-leaf concatenation, `@path`
  imports, path-scoped rules); full prompt-caching mechanics including the
  confirmed **mid-session CLAUDE.md edit doesn't take effect until
  `/clear`/`/compact`/restart** gotcha, directly relevant to `.ROOT`'s
  self-editing governance pattern.
- [Claude Code — Workflow Recipes, Session Mechanics, and the Extension Ladder](claude-code-workflows-and-sessions.md)
  — session naming/resume/branch mechanics; the four scheduling options
  (confirms `.ROOT`'s `schedule`/`loop` skills already cover both relevant
  ones); the **extension trigger table** (symptom → CLAUDE.md/skill/MCP/
  subagent/hook/plugin) as a reusable self-evolution screening heuristic.
- [Claude Code — Permission Modes, Security Guidance, and Code Review](claude-code-permissions-security-and-review.md)
  — validates `.ROOT`'s Manual-mode + deny-rule hardening against the
  vendor's own "hard guarantee" guidance; the protected-path backstop
  (never auto-approved except in `bypassPermissions`, independent of allow
  rules); the `security-guidance` plugin (automatic 3-layer review, not
  yet evaluated) and `REVIEW.md` PR-tuning mechanic, both newly read.
- [Claude Code Prompt Library — Reusable Prompt Patterns](claude-code-prompt-library-patterns.md)
  — 52 slotted prompt cards across 5 SDLC stages; six named patterns for
  what makes a prompt reusable (outcome not steps, self-check, reference
  pointer, measurable target, artifact not description, output format);
  three candidate `.ROOT` task mappings (session-close capture, review
  routing, MCP-as-standing-connection).
- [Claude Code Integration Surface — CI/CD, IDE, Slack, and Platform Landscape](claude-code-integration-surface-and-platform.md)
  — inventory of surfaces (CLI/Desktop/VS Code/JetBrains/web/mobile) and
  integrations (GitHub Actions, GHES, GitLab CI/CD, Slack→Claude Tag,
  computer use) with **no current `.ROOT` use case**, honestly recorded as
  such; plus the Thomson Reuters case study (fifth independent
  confirmation of the verification-capacity finding) and the still-unparsed
  enterprise ebook PDF (hard technical block, poppler unavailable).

## Proposals

- [Agentic-Tool Vetting Checklist](proposals/2026-07-08_agentic-tool-vetting-checklist.md)
  — **APPROVED & APPLIED July 8, 2026.** Chris approved with one revision
  (compressed to a single bullet); promoted into Category 10 of
  `TECHNOLOGY_LIBRARY_STRATEGY.md`. First proposal to complete the full
  research → proposal → review → promotion loop.
- [Wiki Shared Layer + AI-Lane Cleanup](proposals/2026-07-09_wiki-shared-layer-and-lane-cleanup.md)
  — **APPROVED & APPLIED July 9, 2026.** Deduplicated the seven wiki
  CLAUDE.mds into AI_Agent.md's new Wiki Shared Layer (that OS is now AGENT.md — July 10, 2026) (with lint and
  ingest-discipline rules from the LLM-wiki batch), closed the TECHNOLOGY
  `ai-and-llm/` intake lane, slim-rewrote BUSINESS CLAUDE.md. Second
  completed research → proposal → promotion loop.

---
*Last updated: July 12, 2026 (session 13 — Claude Code docs pack ingest, moved from CASTLE)*

