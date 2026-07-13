---
type: map
tags: [now, ai-automation]
---

# AI_AUTOMATION_SYSTEMS Wiki — Index

### Scope: AI tooling, agent patterns, and automation research generally — plus self-evolution research on `.ROOT` itself. Researches and proposes; `00-BRAIN\CASTLE` reviews and maintains.

## Status

Operational as of July 8, 2026. Eight research batches ingested (agentic-AI
papers; AI Agent Index detail data; MCP docs + NIST AI RMF; WTI series +
OECD AIM; LLM-wiki pattern batch; Pereira O'Reilly book; Claude Code official
docs pack; OpenAI Platform/ChatGPT/Codex docs pack), two self-evolution
proposals approved and promoted. **raw/ fully processed as of July 12, 2026
(session 14)** — both `CLAUDE_FILES/` and `OPEN_AI-CHATGPT_CODEX_FILES/`
(moved here from `00-BRAIN\CASTLE\raw\books\`, correctly relocated to this
wiki's intake lane) now read in full and routed into eighteen pages total.
**One later same-day addition (session 15):** *Building a Second Brain*
promoted from `77-INBOX` as a self-evolution source — nineteen pages total.
See `log.md`.

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
- [OpenAI Responses API — State, Streaming, and Context Mechanics](openai-responses-api-state-and-streaming.md)
  — three state-management approaches, two extra transports (SSE, WebSocket
  for tool-heavy loops), background mode, structured-outputs constraints,
  and a direct OpenAI-vs-Claude prompt-caching comparison. Also Codex's own
  underlying API surface — not pure landscape research.
- [OpenAI Developer Tooling — SDKs, the `openai` CLI, and Agent Builder](openai-sdks-cli-and-agent-builder.md)
  — the CLI-for-repeatable-work vs. subagents-for-judgment split (stated
  explicitly for Codex's own operating model); the reusable
  `--transform`/`--format` batch pattern; Agent Builder inventoried as
  deprecated (shutdown Nov 30, 2026). Flags `Node reference  OpenAI API.md`
  as mislabeled (actual content: Agent Builder node catalog).
- [OpenAI Model Lineup, Selection, and Optimization Workflow](openai-model-lineup-and-selection.md)
  — GPT-5.6 tiers/pricing, the five-step optimization flywheel, and a
  second independent vendor confirmation (10–15% quality gain, 33–67% cost
  cut from leaner prompts) of `.ROOT`'s own instruction-file discipline.
- [OpenAI Multimodal Generation — Vision, Image, Audio, and Voice Agents](openai-multimodal-generation.md)
  — vision/image/audio/voice-agent mechanics, honestly recorded as no
  current `.ROOT` use case (text-only, Windows-based system).
- [OpenAI Tools and Function Calling — Mechanics and Claude Code Contrasts](openai-tools-and-function-calling.md)
  — hosted/custom/orchestration tool mechanics; `tool_search` and
  Programmatic Tool Calling confirmed as independent re-inventions of MCP's
  progressive discovery and "code mode" — cross-vendor validation of a
  pattern this wiki already documented. Also covers Agent Skills, the Shell
  tool, and Retrieval/vector stores.
- [OpenAI Agents SDK — Orchestration, Guardrails, and the Claude Code Contrast](openai-agents-sdk-and-orchestration.md)
  — handoffs and agents-as-tools, both genuinely absent from Claude Code's
  subagent model (not just differently named); a resumable-approval state
  machine more developed than Claude Code's per-action permission prompts.
- [OpenAI MCP Integration, ChatGPT Apps, and Agent Builder](openai-mcp-and-chatgpt-apps.md)
  — OpenAI's MCP product surface (connectors, remote servers, Secure MCP
  Tunnel — no documented Anthropic equivalent), ChatGPT Apps philosophy,
  ChatKit; Agent Builder and Prompt objects both shutting down Nov 30, 2026.
- [OpenAI GPT Actions — Custom GPT API Integration Surface](openai-gpt-actions.md)
  — the older, schema-driven Custom-GPT integration path; three retrieval
  patterns (REST/relational/vector, each needing middleware); a third
  independent confirmation of "gate writes, free reads"
  (`x-openai-isConsequential`).
- [OpenAI Prompting Craft and Reasoning-Model Mechanics](openai-prompting-and-reasoning-models.md)
  — the GPT-vs-reasoning-model prompting split; `reasoning.effort` scale
  (none→xhigh); the counterintuitive finding that reasoning models perform
  *worse* with "think step by step" prompting.
- [OpenAI Evals and Red Teaming — The Mechanics Behind "Verify Before Scaling"](openai-evals-and-red-teaming.md)
  — the actual mechanism behind CASTLE's applied "traces/evals before
  multi-agent scale" claim: each architecture-complexity step adds its own
  nondeterminism category needing new evals. **Major recency flag**:
  OpenAI's Evals platform shuts down Nov 30, 2026 (read-only Oct 31).
- [OpenAI Fine-Tuning Methods and Legacy Assistants API](openai-fine-tuning-and-legacy-assistants.md)
  — confirms and sharpens CASTLE's "park fine-tuning" verdict with hard
  dates: fine-tuning platform closed to new users; Assistants API shuts
  down **August 26, 2026**.
- [OpenAI Responses API Multi-agent — A Third Orchestration Primitive](openai-responses-multi-agent.md)
  — a model-initiated, built-in multi-agent primitive (`spawn_agent`,
  `send_message`, etc.), distinct from the Agents SDK. Directly relevant
  landscape research given `.ROOT`'s own heavy use of parallel research
  forks.
- [OpenAI Webhooks and Context Compaction](openai-webhooks-and-compaction.md)
  — webhooks (no current `.ROOT` use case) plus compaction, contrasted
  directly against Claude Code's `/compact`: OpenAI's compaction is an
  opaque encrypted item, Claude's is a human-readable re-injected summary.
- [Building a Second Brain — Applied to `.ROOT`](building-a-second-brain-root-application.md)
  — full-book self-evolution audit (Tiago Forte, CODE/PARA); verdict:
  validates the architecture, no PARA rebuild; four narrow operating
  upgrades adopted (capture filter, Hemingway Bridge merged into the
  Handoff Ritual, kickoff/completion checklist, 3-page At a Glance pilot).

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
- [Governance Drift Detection — A Standing Staleness Check](proposals/2026-07-12_governance-drift-detection.md)
  — **PENDING REVIEW.** Proposes a standing check (script, weekly-sweep
  item, or one-time red-team exercise — options, not a mandate) so a stale
  governance claim is caught before it propagates, not just when an audit
  happens to catch it. Direct response to the same-day Codex validation
  incident, plus a REVIEW.md mechanic and an OpenAI evals anti-pattern
  independently naming the same failure class.
- [Mid-Session Governance-Edit Discipline](proposals/2026-07-12_mid-session-governance-edit-discipline.md)
  — **APPROVED & APPLIED July 12, 2026.** Added to `AGENT.md` § File
  Safety: editing a system file mid-session doesn't take effect until
  `/clear`/`/compact`/restart.
- [Session-Close Capture Prompt](proposals/2026-07-12_session-close-capture-prompt.md)
  — **APPROVED & APPLIED July 12, 2026.** Added to both skill-file copies:
  an explicit "what would otherwise be silently lost" question, distinct
  from the existing "what was done" activity log.
- [MCP Vetting Screen — Secure Tunnel Gap](proposals/2026-07-12_mcp-vetting-screen-secure-tunnel-gap.md)
  — **APPROVED & APPLIED July 12, 2026.** Category 10's vetting screen now
  checks for a no-inbound-port private-network bridge, genericized (not
  pinned to a single vendor product name) and folded into the existing
  "Check for:" list. Third promoted proposal from this wiki.
- [Extension Trigger Table for AGENT.md / CLAUDE.md](proposals/2026-07-12_extension-trigger-table.md)
  — **APPROVED & APPLIED July 12, 2026.** Added to `AGENT.md` as a new
  section (single source of truth); `CLAUDE.md` points to it rather than
  duplicating. Also prompted demoting `AGENT.md`'s own Graph Color
  Maintenance section into a new `graph-colors` skill.
- [Scale the Agent Evaluation Gate with Architecture Complexity](proposals/2026-07-12_eval-gate-complexity-scaling.md)
  — **APPROVED & APPLIED July 12, 2026.** `AGENT.md`'s Agent Evaluation
  Gate rule 2 now scales test cases to what a workflow actually introduces
  (tools, multiple agents, sensitive actions) instead of demanding a fixed
  five uniformly. Kept to one sentence, rule count unchanged.
- [Enforce CASTLE's Research Boundary + Add a `raw/` Placement Rule](proposals/2026-07-12_castle-research-boundary-and-raw-placement.md)
  — **APPROVED & APPLIED July 12, 2026.** Resolved by the `WHERE_IT_GOES.md`
  raw-intake rule alone, kept at its original stricter wording (a proposed
  loosening was considered and declined). No `OPERATIONS.md` change needed.
  Raw-file retirement established as a flag-when-noticed judgment call, not
  a rule — except the Claude Code/OpenAI docs, which never retire.
- [Make the HIGH-Flag-Before-Close Rule a Hook, Not Just Prose](proposals/2026-07-12_session-close-high-flag-hook.md)
  — **PENDING REVIEW.** The session-close skill's HIGH-flag rule is
  advisory prose, not an enforced hook — proposes converting it per the
  now-confirmed "guardrails belong in hooks" principle.

---
*Last updated: July 13, 2026 (local-root path sweep; C: canonical, Google Drive backup only)*
