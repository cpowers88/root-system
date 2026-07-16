---
type: map
timeline: reference
tags: [ai-automation, ingestion, provenance, coverage]
---

# AI_AUTOMATION_SYSTEMS Raw-Source Coverage

This is the hub's ingestion ledger. It separates **compiled** (source knowledge
is retrievable in wiki/report form), **lookup/reference** (accounted for but not
compiled), **duplicate**, and **misrouted**. A raw file existing on disk or
having been opened once is not, by itself, evidence of ingestion.

Coverage audit: **2026-07-16** — 180 raw files, approximately 184.6 MiB (live
recount after book intake).

## Large PDF and book sources

| Source | Coverage | Durable location / decision |
|---|---|---|
| `GenerativeAIforSoftwareDev.pdf` (171 pp.) | Compiled; full chunk read | [[generative-ai-for-software-development-pereira]] |
| `Building-a-Second-Brain-Tiago-Forte-2022.pdf` (237 pp.) | Compiled chapter-by-chapter; visuals later verified | [[building-a-second-brain-root-application]] plus `00-BRAIN/Session_Logs/Report Archive/BUILDING_A_SECOND_BRAIN_ROOT_STRUCTURE_REPORT_2026-07-12.md` |
| WTI 2024/2026 PDFs (39/35 pp.) | Compiled; full page coverage | [[work-trend-index-2024-2026]] |
| `NIST.AI.100-1.pdf` (48 pp.) | Compiled | [[nist-ai-rmf]] |
| Agent Index/Codex/industry papers | Compiled | [[2025-ai-agent-index]], [[shift-to-agentic-ai-codex]], [[agentic-ai-industry-adoption-barriers]] |
| `2311.10751v2.pdf`, `2510.25423v2.pdf`, `2606.26118v1.pdf` | Compiled in page-range chunks on 2026-07-15 | [[agentic-automation-architecture-reliability-and-economic-evidence]] |
| `2604.21412v3.pdf`, `2604.23183v2.pdf` | Compiled in page-range chunks on 2026-07-15 | [[oecd-ai-incidents-monitor]] |
| `CLAUDE_FILES/Anthropic-enterprise-ebook-digital.pdf` (35 pp.) | Compiled in five chunks on 2026-07-15; former parser block closed | [[enterprise-ai-adoption-and-production-roadmap]] |
| `empireofAIDreamsandNightmares.pdf` (575 pp.) | **Compiled; full argument-bearing text** | Author's Note, Prologue, Chapters 1-18, and Epilogue reviewed in complete physical-page chunks (pp. 8-398). Parts I-II retrieval: [[openai-governance-mission-capital-and-control]], [[ai-research-paradigm-concentration-and-commercial-selection]], [[scaling-doctrine-compute-data-and-hidden-labor]], [[frontier-lab-commercialization-safety-and-organizational-power]], [[corporate-ai-research-control-transparency-and-accountability]], and [[generative-ai-productization-content-safety-and-hidden-labor]]. Part III retrieval: [[ai-safety-ideologies-risk-language-and-release-gates]], [[chatgpt-launch-interface-risk-and-organizational-scaling]], [[ai-compute-infrastructure-energy-water-and-community-governance]], and [[ai-policy-agenda-setting-frontier-thresholds-and-oversight-information]]. Part IV retrieval: [[board-oversight-crisis-information-and-coalition-power]], [[ai-safety-capacity-whistleblowing-and-organizational-trust]], and [[mission-elasticity-centralization-and-ai-empire-pattern]]. Epilogue retrieval: [[community-governed-ai-data-sovereignty-and-power-redistribution]]. Acknowledgments begin p. 399 and notes p. 403; these and later bibliography/index material are reference back matter, not uncompiled argument. Investigative narrative, disputed claims, author framing, and historical case details require claim-level provenance/recency caution. |
| `ifAnyoneBuildsitEveryoneDies.pdf` (207 pp.) | **Chunk backlog; not compiled** | Advocacy argument for AI-extinction risk, not an empirical operating manual. Preserve as a challenge source; ingest by part/chapter only when the safety thesis has a concrete review job. |
| `ArchitectsofIntelligence.pdf` | Lookup/reference; not compiled | Historical expert-interview source. Use for dated viewpoints, not current capability claims. |
| `ArtificialIntelligenceAGuideforThinkingHumans.pdf` | Lookup/reference; not compiled | General conceptual challenge source; process only against a specific learning or strategy question. |
| `DeepLearningTextbook.pdf` (800 pp.) | Prerequisite reference; not compiled | Foundational 2016 technical text. Keep behind active math/ML prerequisites; not an active reading assignment. |
| `mastering claude.pdf` (401 pp.) | **Verification backlog; not compiled** | 2025 product-specific guide. Verify volatile Claude features against current official documentation before promoting claims. |
| `TheAlignmentProblem.pdf` (617 physical pp.; main text ends p. 403) | **Compiled; full main text** | Prologue (pp. 9-12), Introduction and Parts I-III (pp. 13-380), and Conclusion (pp. 381-403) reviewed in named chunks. Retrieval: [[training-data-representation-and-feedback-risk]], [[algorithmic-fairness-metrics-ground-truth-and-intervention]], [[interpretable-models-and-human-oversight]], [[reinforcement-learning-reward-prediction-and-credit]], [[reward-shaping-curiosity-and-safe-exploration]], [[imitation-learning-recovery-and-amplification]], [[preference-inference-feedback-and-human-ai-cooperation]], and [[uncertainty-corrigibility-and-impact-limits]]. Acknowledgments (from p. 404), notes (from p. 409), bibliography, and index are reference back matter, not uncompiled argument. |
| `Emerging Pedagogies - AI Territory and Situated Knowledges (2025).pdf` (157 pp.) | Lookup/reference; not compiled | Open-access ten-chapter collection on algorithmic literacy, epistemic inequality, ethical generative-AI teaching, design thinking, and critical thinking. Relevant to human/education consequences, but it does not fill the current production-application gap; retrieve for a specific AI-literacy, education, or governance question. |
| `TLS.pdf` (3 pp.) | **Misrouted; not an AIAS source** | APICS article on combining Theory of Constraints, Lean, and Six Sigma. Belongs in SYSTEMS if Chris authorizes a raw-source move/copy; raw remains untouched here. |

## Markdown source groups

| Group | Coverage |
|---|---|
| AI Agent Index detail clippings | Compiled into [[agent-vetting-worked-examples]]; numbered filenames are covered as a set. |
| MCP official-document clips | Compiled into the MCP landscape, security/authorization, and client-primitives pages. Per-language tutorial bodies remain implementation lookup. |
| LLM-wiki / GBrain / loopany / AI-OS clippings | Compiled into [[llm-wiki-pattern-and-second-brain-tools]] and [[self-improving-agent-architectures-gbrain-loopany-closed-loop]]. |
| OpenAI Platform/ChatGPT/Codex pack | Compiled thematically into thirteen pages; one byte-identical Agents SDK duplicate and title-collision defects remain documented, not double-counted. |
| Claude Code official-doc pack | Compiled thematically into five original pages plus the enterprise-roadmap page added in this audit. |
| Workflow-automation and OECD AIM clippings | Compiled into [[workflow-automation-tools-landscape]] and [[oecd-ai-incidents-monitor]]. |
| `Conversation.md` | Accounted reference, not research: a user/Gemini planning transcript whose durable decisions are superseded by `01-NORTH_STAR/NORTH_STAR.md` and `01-NORTH_STAR/System Contracts/ROOT_CAPABILITY_CONTRACT.md`. |
| `llm-wiki-karpathy-2026-07.md` | Duplicate capture of the Karpathy LLM-wiki pattern; read once, not double-summarized. |
| `README.md` | Intake instructions, not a research source. |

## Coverage rule going forward

Every intake must end in one of the statuses above and be recorded in this
ledger and `log.md`. Sources above roughly 40 pages, books, or large mixed-topic
document packs must be processed in named page/file chunks. A synthesis page may
remain the retrieval surface, but its `source:` line or log entry must preserve
the chunk ranges and coverage limit.

The hub is therefore **fully accounted as of 2026-07-16, not fully compiled**.
The named book/reference rows above are intentional queues or lookup sources;
`TLS.pdf` is a placement decision, not an ingestion omission.
