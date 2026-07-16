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

Coverage audit: **2026-07-15** — 176 raw files, approximately 111 MB.

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
| `empireofAIDreamsandNightmares.pdf` (575 pp.) | **Chunk backlog; not compiled** | Narrative investigative book. Relevant to AI power, labor, data, and supply-chain ethics, but lower current operating priority than primary/empirical sources. Requires a dedicated chapter-cluster ingest before any claim of coverage. |
| `ifAnyoneBuildsitEveryoneDies.pdf` (207 pp.) | **Chunk backlog; not compiled** | Advocacy argument for AI-extinction risk, not an empirical operating manual. Preserve as a challenge source; ingest by part/chapter only when the safety thesis has a concrete review job. |
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

The hub is therefore **fully accounted as of 2026-07-15, not fully compiled**.
The only intentional compilation backlog is the two named books; `TLS.pdf` is a
placement decision, not an ingestion omission.
