---
type: log
tags: [log]
---

# AI_AUTOMATION_SYSTEMS Wiki — Log

## 2026-07-09 (session 12) — Stanford AI Index 2026 ingested multi-hub (flag 55c closed)

### Work completed
Chris directed the flag-55(c) ingest with a multi-hub routing decision:
read the report and place each part where it belongs. Source: AI Index
2026 (Stanford HAI, 9th ed., April 2026, 425 pp., arXiv:2606.15708) —
sits in `03-WIKIS\TECHNOLOGY\raw\` (dropped July 8, pre-lane-closure);
raw stays there, research routed per lane.

**Coverage record (chunking rule):** ingested at the report's own
designed summary layer — Introduction + all 15 Top Takeaways (pp. 5–12)
and all nine Chapter Highlights sections read in full (R&D pp. 14–16,
Technical Performance 70–72, Responsible AI 127–130 incl. the RAI
dimensions framework, Economy 172–175, Science 232–234, Medicine
256–258, Education 289–292, Policy 324–327, Public Opinion 361–363).
Chapter bodies (~340 pp. of per-benchmark charts and country tables)
classified for lookup — the public raw data/chart files Stanford
publishes make deep chart-level extraction redundant.

**Routing (three hubs written, one page each way):**
- HERE (primary, per AI-lane closure): `ai-index-2026.md` — capability/
  measurement, responsible AI, adoption arc, sovereignty; ties to the
  WTI series, NIST RMF (now a market-cited standard at 33%), OECD AIM
  (incidents 362), and the Pereira book's convergence finding.
- BUSINESS: `market-map.md` Market Timing section extended with the
  Index's corroboration block (88% org adoption vs single-digit agents,
  productivity gains 14/26/50%, US 24th in adoption, ISO 42001 + NIST
  RMF as named standards, incidents +55%).
- EDUCATION: `ai-programs-us-2026.md` extended with the Education
  chapter (CS enrollment −11%, AI master's +17%, PhDs to academia,
  80% student AI use vs 6% clear policies).
- TECHNOLOGY: disposition logged in its log (raw home; no content
  change — its AI lane is closed).

### Pages created/updated
Created: `ai-index-2026.md`. Updated: `index.md`, this log; cross-hub:
BUSINESS `market-map.md`, EDUCATION `ai-programs-us-2026.md`, TECHNOLOGY
`log.md`, SYSTEM_FLAGS #55 (c closed — flag 55 fully resolved).

### Next action
Flag 55 is fully closed; every hub's raw/ is processed or
classified-with-record. Carry-over rep unchanged: MCP threat-catalog →
audit-facing vetting proposal — now with AI Index incident/RAI data as
supporting evidence.

## 2026-07-09 (session 11) — Pereira O'Reilly book chunk-ingested (flag 55a closed)

### Work completed
Chris directed the flag-55(a) ingest: `raw/GenerativeAIforSoftwareDev.pdf`
(Pereira, "Generative AI for Software Development," O'Reilly, July 2025,
171 pp.) — the source session 10's sweep found unlogged and unprocessed.

**Coverage record (chunking rule):** read in 10 chunks on chapter
boundaries — pp. 9–27 (preface + Ch1 tools), 28–40 (Ch1 tests/conclusion),
41–58 (Ch2 UI/UX), 59–78 (Ch3 code review), 79–94 (Ch4 testing), 95–118
(Ch5 analytics), 119–134 (Ch6 documentation), 135–152 (Ch7 chatbots),
153–164 (Ch8 case studies + conclusion), 165–171 (index/colophon — no
content). Pp. 1–8 are cover/copyright/TOC (inspected via the PDF outline).
**Coverage total: complete.**

Synthesized as ONE new page (update-over-create: no existing page covers
the SDLC-wide tool landscape):
`generative-ai-for-software-development-pereira.md` — the reusable
two-stage evaluation method, the seven-category tool map (ratings marked
as a 2025-04 snapshot with a staleness warning), the Levels/Shopify
adoption contrast (three-blockers analysis), the jobs thesis
(ATM/elevator/Excel → "AI integration specialist"), and the tie-backs:
Shopify's doubled code review = third independent confirmation of the
July 8 verification-capacity verdict; the analytics chapter's universal
forecast hallucinations = standing caution for the data-and-dashboard
pathway.

### Pages created/updated
Created: `generative-ai-for-software-development-pereira.md`. Updated:
`index.md` (page entry + Status: raw/ fully processed as of session 11),
this log. Outside the wiki: SYSTEM_FLAGS #55 status (item a closed).

### Next action
Flag 55 remainder is other hubs' work on Chris's schedule: (b) BPMN spec
chunked ingest (SYSTEMS), (c) AI Index 2026 lane decision + ingest
(TECHNOLOGY raw/ → this wiki per lane closure). Carry-over rep unchanged:
MCP threat-catalog → audit-facing vetting proposal.

## 2026-07-09 (session 10) — Citation/sort audit (Chris-directed, all-wikis sweep)

### Work completed
First hub in Chris's hub-by-hub citation-and-sorting sweep. Full check of
raw/ vs. log claims, index vs. live tree, page frontmatter, and cited
source paths. Findings and fixes:

1. **Two unprocessed raw sources found** — the log's "raw/ fully
   processed" claims (sessions 8–9) were wrong:
   - `raw/The best workflow automation tools in 2026.md` (Zapier blog
     roundup, dropped 2026-07-09 15:29, after session 9's last ingest) —
     **ingested this session** as `workflow-automation-tools-landscape.md`
     (new page justified per update-over-create: no existing page covers
     the workflow-tool category landscape; read in full, one pass —
     35KB article, holdable whole).
   - `raw/GenerativeAIforSoftwareDev.pdf` — a **171-page O'Reilly book**
     (Sergio Pereira, "Generative AI for Software Development", July 2025)
     never mentioned in any log entry. NOT ingested this session: the
     chunking rule makes it a multi-session job (~12–15 chunks). Logged
     here as the known backlog item; needs Chris's call on priority
     (it may also belong in TECHNOLOGY/PYTHON's applied-technique lane —
     lane check before ingest).
2. **Citation fixes:** `2025-ai-agent-index.md` source line updated (the
   flagged duplicate PDF was since removed; ACM version noted);
   `llm-wiki-pattern-and-second-brain-tools.md` given the `source:`
   frontmatter line its siblings carry (sources were body-only).
3. **Sort/lint checks passed:** all 13 content pages listed in index (now
   incl. the new page); both proposals listed; all cited raw/ paths
   resolve; all inter-page wikilinks resolve; frontmatter present on every
   page; `root-maturity-self-assessment.md` correctly has no `source:`
   (internal assessment, sources are wiki pages cited inline). Index
   Status block refreshed (was stale at "two research batches").

### Pages created/updated
Created: `workflow-automation-tools-landscape.md`. Updated: `index.md`
(new page entry + Status refresh), `2025-ai-agent-index.md` (source line),
`llm-wiki-pattern-and-second-brain-tools.md` (source frontmatter), this log.

**Addendum (same sweep, BUSINESS hub):** the sweep's BUSINESS pass found
the **WTI 2025 annual full report PDF** (15 pp.) in `03-WIKIS\BUSINESS\raw\`
— the exact source session 8 flagged as missing. Completion pass done: all
15 pp. read (report body pp. 1–11, methodology p. 12, by-market appendix
pp. 12–14), `work-trend-index-2024-2026.md` extended (Frontier Firm
definition bar, three-phase journey, six named case studies, workforce
strategy rankings + top-10 AI roles, why-AI-over-colleague data,
US-vs-global deployment gap, leader playbook) and its source line now
cites the BUSINESS raw/ location. All five WTI-series sources at full
coverage — for real this time.

### Next action
Chris decides on the O'Reilly book: chunked ingest here, route to another
hub, or archive. Carry-over rep unchanged: MCP threat-catalog →
audit-facing vetting proposal. Sweep continues to the next wiki hub.

## 2026-07-09 (session 9) — LLM-wiki batch ingested → shared-layer proposal approved & applied

### Work completed
Chris directed a go-live-eve optimization review of all seven wiki
CLAUDE.mds. Read the four-source LLM-wiki batch in raw/ in full (Karpathy
pattern gist, Rezvani llm-wiki skill, claude-obsidian article,
obsidian-second-brain README — each in one complete pass; all four small
enough to hold whole, coverage complete). Compared the pattern against
`.ROOT` practice, then drafted and applied the Chris-approved proposal:
Wiki Shared Layer added to AI_Agent.md (9 rules, including the new lint /
update-over-create / contradiction-flag / recency-marker rules drawn from
this batch); all 7 wiki CLAUDE.mds deduplicated to pointers + unique
rules; BUSINESS CLAUDE.md slim-rewritten (920-line build prompt archived,
drifted mission quote replaced with a NORTH_STAR pointer); AI-lane
closure (new AI/LLM/agent research routes HERE; TECHNOLOGY's `ai-and-llm/`
closed inherited reference; `02-LIBRARY\08-AI-AUTOMATION` declared
artifact home, not intake lane — also recorded in WHERE_IT_GOES.md).

### Pages created/updated
Created: `llm-wiki-pattern-and-second-brain-tools.md`,
`proposals/2026-07-09_wiki-shared-layer-and-lane-cleanup.md` (APPROVED &
APPLIED — second proposal to complete the full loop). Updated: `index.md`,
this log, this wiki's `CLAUDE.md` (as part of the 7-file dedup).

### Next action
Carry-over rep remains: MCP threat-catalog → audit-facing vetting proposal
(via castle/Chris review path). raw/ remains fully processed.

## 2026-07-09 (session 8) — Work Trend Index series + OECD AIM ingested

### Work completed
Chris dropped four new sources in raw/ the morning of July 9: the Microsoft
Work Trend Index 2024 and 2026 annual-report PDFs, the June 2025 WTI special
report clipping ("Breaking down the infinite workday"), and an OECD AI
Incidents Monitor capture. Ingested as two synthesis pages (series page +
reference page), not four clip pages, per this wiki's established pattern:

- **`work-trend-index-2024-2026.md`** — the adoption arc read as a series:
  2024 unmanaged adoption (75% use, 78% BYOAI, hiring flips to AI aptitude,
  power-user profile), 2025 infinite-workday telemetry (2-min interruptions,
  117 emails/153 messages, 57–60% ad hoc meetings — quotable waste evidence),
  2026 Transformation Paradox (org factors 2× individual, five readiness
  zones, Frontier Professionals, Learning System / Owned Intelligence,
  agents 15× YoY). Key tie-back: Microsoft's "evaluation infrastructure"
  finding independently confirms the July 8 verification-capacity verdict.
- **`oecd-ai-incidents-monitor.md`** — ~16,300-entry incident/hazard catalog,
  incident-vs-hazard taxonomy, seven named failure classes with audit
  lessons; positioned as the vetting screen's incident-history lookup and
  the failure-evidence counterweight to capability sources. Watchtower
  boundary respected (lookup resource here, horizon-scanning stays there).

**Gap closed same session:** Chris added the 2025 annual announcement
("The Frontier Firm Is Born," Spataro blog clipping) to raw/ — series page
extended with its own section (Capacity Gap, human-agent ratio, agent boss,
Frontier Firm thriving numbers) and the arc table now runs four releases.

**Completion pass (Chris's new chunking rule, applied same session):** both
PDFs re-checked chunk by chunk to full coverage — 2026 report pp. 1–35 of 35
(pp. 24–35 = methodology + 28-market appendix; yielded the by-market Frontier
Professional spread, France 8% → Vietnam 39%, US 17%) and 2024 report
pp. 1–39 of 39 (pp. 25–39 = leader takeaways + methodology + 31-market
appendix; yielded the US baseline row and the "identify a business problem,
then apply AI" leader playbook). Coverage is now total on all five WTI-series
sources. Same rule written into all seven wiki CLAUDE.mds this session
(system-wide, Chris's call).

### Pages created/updated
Created: `work-trend-index-2024-2026.md`, `oecd-ai-incidents-monitor.md`.
Updated: `index.md`, this wiki's `CLAUDE.md` (chunking rule),
`work-trend-index-2024-2026.md` (2025 section + completion-pass additions).

### Next action
Unchanged carry-over from session 7: draft the proposal folding the MCP
threat-catalog/local-server questions into audit-facing vetting material —
now strengthened by the WTI org-readiness data and AIM failure classes.

## 2026-07-08 (session 7) — Vetting table spot-checked against live index

### Work completed
Executed the open verification rep: checked all 8 rows of
`agent-vetting-worked-examples.md` against the live per-agent pages at
aiagentindex.mit.edu (`/2025/<agent>`). Result: **every scored cell
confirmed**, most verbatim — both no-stop findings (n8n, Breeze), the
Breeze auto-trigger approval loophole and unremediated prompt injection,
Zapier's agents.zapier.com bounty exclusion, the Comet incident record,
and the full Claude Code / Codex clean-pass rows (system cards, default
sandboxes, read-only defaults, stop-anytime).

One correction applied: the Comet disclosure cell claimed "robots.txt
ignored by design for user-driven fetches" — the live index records no
robots.txt behavior for Comet; that characterization traces to
third-party reporting (Cloudflare/Perplexity dispute), not the index.
Cell annotated to cite accordingly; the ❌ verdict stands on Chrome UA +
residential IPs alone. Table marked quotable in client deliverables as of
July 8, 2026.

### Pages created/updated
Updated: `agent-vetting-worked-examples.md` (Comet cell correction +
verification provenance note).

### Next action
The remaining candidate rep: draft the proposal folding the MCP
threat-catalog/local-server questions into audit-facing vetting material
(via the castle/Chris review path).

## 2026-07-08 (session 6) — raw/ extraction completed

### Work completed
Chris removed the duplicate clip flagged in session 5
(`Understanding_MCP_Servers_(MCP).md.txt`) and asked for any remaining
raw/ value to be brought into the wiki. Second-pass extraction of the
material session 5 had shelved:

Created **`mcp-client-primitives-and-build-notes.md`** from
`Understanding MCP clients.md` (roots/sampling/elicitation read in full
this time) plus the language-agnostic core of the two "Build an MCP…"
tutorials. Key catches that justified the pass: **roots are coordination,
not security** (spec says servers "SHOULD respect," not "MUST enforce" —
feeds the vetting screen's sandboxing rationale); elicitation's
never-request-credentials rule; sampling's human-in-the-loop design with
cost/speed/intelligence model preferences; the stdio
never-write-to-stdout rule; and an operational debug quick-reference
(Claude Desktop MCP log locations, full-quit-to-reload-config, absolute
paths).

Cross-linked from the landscape page. With this, every source in `raw/`
is processed; the per-language tutorial bodies remain as code reference
only.

### Pages created/updated
Created: `mcp-client-primitives-and-build-notes.md`.
Updated: `mcp-landscape-architecture-and-patterns.md` (cross-link),
`index.md`.

### Next action
Unchanged from session 5: next rep is either the proposal seed (fold the
MCP local-server/threat-catalog questions into audit-facing vetting
material via the review path) or spot-checking the session-4
worked-examples table against the live index site.

## 2026-07-08 (session 5) — MCP docs batch + NIST AI RMF ingested

### Work completed
Chris dropped a second raw batch the evening of July 8 (14 modelcontextprotocol.io
clips covering architecture, server/client concepts, client best practices,
security, authorization, agent skills, Inspector, SDKs, connect guides,
plus `NIST.AI.100-1.pdf`). Intaken as three synthesis pages rather than
one page per clip:

1. **`mcp-landscape-architecture-and-patterns.md`** — closes the
   MCP-landscape rep open since session 3. Architecture, six primitives,
   transports, deployment paths; highest-value material is the client
   scaling patterns (progressive tool discovery, code mode, prompt-caching
   interaction). Key resonance: progressive discovery is the `.ROOT`
   router pattern formalized by the official docs.
2. **`mcp-security-and-authorization.md`** — eight-attack-class threat
   catalog + OAuth 2.1 essentials; the MCP-specific depth layer under the
   approved Category 10 vetting screen. Practical takeaway: a local MCP
   server install is code execution with the client's privileges.
3. **`nist-ai-rmf.md`** — GOVERN/MAP/MEASURE/MANAGE + seven
   trustworthiness characteristics; formalizes the verification-gap
   finding and maps `.ROOT` onto the four functions (GOVERN/MAP strong,
   MEASURE thin). Citable audit vocabulary for future client work.

The two "Build an MCP server/client" clips are per-language tutorials —
kept as implementation reference, not separately summarized. Large files
were read via text extraction to scratchpad; `raw/` untouched.

**Housekeeping flags for Chris (raw/ immutable, not acted on):**
`Understanding_MCP_Servers_(MCP).md.txt` is a duplicate clip of
`Understanding MCP servers.md` (same page, earlier grab) and could be
removed on instruction. NIST AI RMF 1.0 predates the agentic wave; the
generative-AI companion profile (NIST AI 600-1) would be the natural
follow-up source if this thread continues.

### Pages created/updated
Created: `mcp-landscape-architecture-and-patterns.md`,
`mcp-security-and-authorization.md`, `nist-ai-rmf.md`.
Updated: `index.md`.

### Next action
No unprocessed sources remain in `raw/`. Candidate next reps: (a) a
proposal seed — fold the MCP threat catalog's local-server questions into
the audit-facing vetting material (needs Chris/castle review path), or
(b) spot-check the session-4 worked-examples table against the live index
site before first client use.

## 2026-07-08 (session 4) — Vetting screen operationalized with Index data

### Work completed
Chris clipped the aiagentindex.mit.edu detail data into `raw/` (8 new files:
`Further Details — 2025 AI Agent Index.md` + `2025 Index.md` through
`2025 Index 6.md` — category-per-file exports covering ~22 of 30 agents,
entries unlabeled but matchable by cited vendor URLs). Processed them into
`agent-vetting-worked-examples.md`: 8 priority agents (Claude Code, Codex,
Gemini CLI, Zapier, n8n, Copilot Studio, HubSpot Breeze, Comet) scored
against the vetting screen's five checks, with an audit-usable readout.

Standout findings: only the CLI agents pass all five checks; no enterprise
builder publishes agent-specific safety evals or sandboxes the deployed
agent; n8n and HubSpot Breeze cannot stop an individual running agent;
HubSpot's approval default silently stops applying to auto-triggered runs;
Zapier's bug bounty excludes its agents product; Comet pairs the highest
autonomy with a real incident record (hidden MCP API, indirect prompt
injection).

### Pages created/updated
Created: `agent-vetting-worked-examples.md`. Updated: `index.md`.

### Next action
Unchanged from session 3: next open research rep is the MCP-landscape page;
alternatively the worked-examples table's key rows could be spot-checked
against the live index site before first client use.

## 2026-07-08 (session 3) — First proposal approved and promoted

### Work completed
Chris reviewed the agentic-tool vetting proposal, approved it with one
revision (he compressed the draft checklist into a single audit-style
bullet, "Agent-tool vetting screen"), and ordered promotion. Applied his
final text verbatim into
`02-LIBRARY\08-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md` Category 10
(after the "AI is a layer" rule) and updated that file's footer.
SYSTEM_FLAGS.md checked before the write — no open HIGH flags.

This completes the wiki's first full self-evolution loop:
raw source → research page → proposal → Chris review → promotion into a
core file. The division of labor held: the wiki drafted, Chris decided,
and the target file changed only on his approval.

### Pages created/updated
Updated: `proposals/2026-07-08_agentic-tool-vetting-checklist.md` (status →
APPROVED & APPLIED), `index.md`.
Outside the wiki (Chris-approved): `TECHNOLOGY_LIBRARY_STRATEGY.md`.

### Next action
Nothing pending review; next research rep is open — leading candidate is an
MCP-landscape page (MCP surfaced as the dominant interop standard in the
Agent Index and is a named rung in Chris's integration-layer build
territory).

## 2026-07-08 (session 2) — Wiki operational: self-assessment + first proposal

### Work completed
Executed the next actions from the morning session, getting the wiki fully
off the ground:
1. **First self-evolution rep:** applied the six-level agentic maturity
   ladder (Apostolou et al.) to `.ROOT` itself. Verdict: L1 solid, L2
   emerging, L3 not warranted. `.ROOT` already mitigates three of the four
   adoption barriers; verification capacity (Chris's review time) is the
   scaling limit to re-check at quarterlies. No governance change proposed —
   the page is the drift baseline.
2. **First proposal drafted** (`wiki/proposals/`): agentic-tool vetting
   checklist for Category 10 of
   `02-LIBRARY\08-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md`. Friction:
   that file calls agent workflows "newest, highest risk/reward" with no
   risk criteria; the 2025 AI Agent Index supplies them. One file, additive,
   ≤15 lines, reversible. Pending castle/Chris review per the division of
   labor — this wiki does not touch the target file.

Grounding reads this session: `00-BRAIN\AI_Agent.md` (verify the proposal
duplicates no existing rule) and `TECHNOLOGY_LIBRARY_STRATEGY.md` (confirm
the gap is real).

### Pages created/updated
Created: `root-maturity-self-assessment.md`,
`proposals/2026-07-08_agentic-tool-vetting-checklist.md`.
Updated: `index.md`.

### Next action
Chris reviews the vetting-checklist proposal (approve into
TECHNOLOGY_LIBRARY_STRATEGY.md, revise, or reject); the wiki's next research
rep is otherwise open — candidates: MCP landscape depth, or the parked
verification-first question if session volume grows.

## 2026-07-08 — First raw-source processing: three agentic-AI papers

### Work completed
Processed the first batch of raw sources (5 PDFs dropped in `raw/`, resolving
to 3 unique papers) into wiki pages:
1. **Agentic AI in Industry** (Apostolou et al., arXiv:2605.14675) — the
   capability-deployment verification gap; adoption is gated by verification,
   not capability.
2. **The Shift to Agentic AI: Evidence from Codex** (Johnston et al.,
   arXiv:2606.26959) — delegation replaces consultation at the frontier;
   skills/systematization (the `.ROOT` pattern) is where value concentrates.
3. **The 2025 AI Agent Index** (Staufer et al., FAccT '26,
   arXiv:2602.17753) — ecosystem census; safety-transparency gaps; MCP
   dominance; tool-vetting heuristics.

Each page includes a "Why this matters for this wiki / `.ROOT`" section tying
findings back to the self-evolution charter.

**Housekeeping flag for Chris (raw/ is immutable, so not acted on):** three of
the five PDFs are the same paper — `2602.17753v2.pdf`, `2602.17753v2 (1).pdf`
(duplicate download), and `3805689.3806728.pdf` (the ACM FAccT version).
The two redundant copies could be removed on Chris's instruction.

### Pages created/updated
Created: `agentic-ai-industry-adoption-barriers.md`,
`shift-to-agentic-ai-codex.md`, `2025-ai-agent-index.md`.
Updated: `index.md`.

### Next action
Candidate proposal seeds surfaced by this batch — draft one in
`wiki/proposals/` next session: (a) a `.ROOT` self-assessment against the
six-level agentic maturity ladder, or (b) a verification-first rule for any
future increase in AI-session autonomy over `.ROOT` files.

## 2026-07-07 — Wiki created

### Work completed
Created as part of the `.ROOT` wiki unification. New hub for AI tooling/agent
pattern research and `.ROOT` self-evolution proposals. Division of labor with
`00-BRAIN\CASTLE` established: this wiki researches and proposes, the castle
reviews and promotes through the existing review cadence.

### Pages created/updated
CLAUDE.md, index.md, log.md, raw/README.md, HOW_TO_USE.md

### Next action
First research rep — pick one AI/automation pattern or one piece of `.ROOT`
friction worth studying, and file the first real page or proposal.

## 2026-07-07 — Structural fix: index.md/log.md moved into wiki/

### Work completed
Found during a TECHNOLOGY wiki alignment session: this wiki's own `CLAUDE.md`
specifies `index.md` and `log.md` living under a `wiki/` subfolder, but both
files had been sitting at the hub root since the July 7 wiki-unification pass
— the same inconsistency TECHNOLOGY caught and fixed in itself the same day.
Moved both files into a new `wiki/` subfolder. No content changes; empty
scaffold, so no other files were affected.

### Pages created/updated
Moved: `index.md` → `wiki/index.md`, `log.md` → `wiki/log.md`.

### Next action
First research/proposal entry per this wiki's stated purpose — still an empty
scaffold otherwise.

## 2026-07-12 (Codex validation correction pass, Claude Code)

### Work completed
Corrected `HOW_TO_USE.md`'s Start Here and Current State sections, which falsely
claimed the hub had no research or proposals filed as of July 12, 2026. The hub is
actually operational: 14 research pages and 2 approved/promoted proposals live in
`wiki/`. Flagged by Codex's `ROOT_OPERATING_INSTRUCTIONS_VALIDATION_2026-07-12.md`
(P1 finding) as the exact class of current-state drift the human instruction system
is meant to prevent.

### Pages created/updated
HOW_TO_USE.md (Start Here now points to the live index/log instead of "once research
accumulates"; Current State rewritten to durable non-exact-count wording)

### Next action
None — hub description now matches live index.md/log.md.

## 2026-07-12 (session 13) — Claude Code docs pack ingested in chunk format (moved from CASTLE)

### Work completed
Chris relocated the Claude Code official docs pack from `00-BRAIN\CASTLEawooks\CLAUDE_FILES\`
to its correct home, `raw\CLAUDE_FILES\` in this wiki, and directed a proper chunked ingest so
nothing from the earlier partial CASTLE-era pass (which only fully read 5 of 20 files) got missed.
Ran three parallel research forks, each reading its assigned files in full and writing new wiki
pages against the CASTLE-era summary (`00-BRAIN\CASTLE\wiki\source-summaries\claude-code-docs-pack-2026-07.md`)
so nothing already captured was duplicated:

- Chunk 1 (highest value): Best_Practices, STORE_INSTRUCTIONS_AND_MEMORIES, EXPLORE_CLAUDE_CONTEXT_WINDOW,
  HOW_CLAUDE_CODE_WORKS, PROMPT_CACHING, COMMON_WORKFLOWS, MANAGE_SESSIONS, Extend_Claude_Code -> two pages.
- Chunk 2: PERMISSION_MODES, SECURITY_GUIDANCE_PLUGIN, CODE_REVIEW, PROMPT_LIBRARY -> two pages.
- Chunk 3: CLI_USE (mislabeled — actual content is computer use), VSCODE_CLAUDE, JETBRAIN,
  GITHUB_ACTIONS, GITHUB_ENTERPRISE_SERVER, GITLAB_CI-CD, CLAUDE_CODE_IN_SLACK,
  OVERVIEW-Platform-and-Intergrations, the Thomson Reuters case study, and an attempt at the
  unparsed enterprise ebook PDF (still unparsed — poppler/pdftoppm unavailable in this
  environment, a hard technical block, not a judgment call) -> one page.

### Pages created/updated
claude-code-context-and-instruction-economics.md, claude-code-workflows-and-sessions.md,
claude-code-permissions-security-and-review.md, claude-code-prompt-library-patterns.md,
claude-code-integration-surface-and-platform.md (all new); index.md (7th research batch, 5 new
page entries, raw/ status updated to July 12); raw/README.md (corrected — falsely said "Nothing
here yet" while raw/ already held 6+ processed source packs plus this new one).

### Findings flagged for Chris (none drafted as proposals — this wiki proposes, doesn't self-promote)
- **Confirmed mechanic**: editing a CLAUDE.md/AGENT.md file mid-session does not take effect
  until `/clear`, `/compact`, or a session restart — the editing session itself keeps running on
  the pre-edit version. Real and current (today's own Codex-correction pass did exactly this).
  Candidate: a governance note in `AGENT.md`, not urgent enough alone for a formal proposal.
- **`security-guidance` plugin** (automatic 3-layer code review via hooks) — genuinely new
  capability, not yet evaluated. Only relevant once Claude Code writes real code in a git-backed
  `02-LIBRARY\.PROJECTS` build — not before.
- **`REVIEW.md`'s CLAUDE.md-staleness-as-finding pattern** — Anthropic's own PR-review product
  treats "code changed, docs didn't" as a standing check. Same failure class as today's Codex
  validation pass. Candidate: could wiki-lint or session-close do a lighter version of this check?
- **Auto memory vs. `.ROOT`'s hand-built memory/ system** — structurally near-identical (index +
  topic files). Open architecture question for a future self-evolution rep, not resolved here.
- **`capture-what-to-remember` prompt card** — could sharpen the `session-close` skill's
  end-of-session capture step.

### Next action
Chris decides whether any of the five flagged items becomes a real `wiki/proposals/` entry.
