---
type: log
tags: [log]
---

# AI_AUTOMATION_SYSTEMS Wiki — Log

## 2026-07-13 (session 16) — CASTLE review of `Clippings\`: GBrain + loopany routed, belief/proposal-split proposal drafted

Chris pointed at a root-level `C:\Users\chris\.ROOT\Clippings\` folder (8
web clips on GBrain, loopany, and a related "self-improving companies"
video transcript) and asked for a CASTLE-lens review: is anyone else
building something like `.ROOT`, and is there anything worth adopting.
Checked for duplicate research first — `llm-wiki-pattern-and-second-brain-tools.md`
already covered this exact question on 2026-07-09 for three sibling tools,
including an explicit rejection of autonomous nightly rewrite loops. Did
not re-litigate; updated that page instead of creating a new one.

**Findings:** GBrain (Garry Tan/YC) is a database-backed, more elaborate
descendant of the same raw/wiki/schema pattern, but its headline feature —
a cron-driven "dream cycle" that autonomously rewrites the knowledge base
overnight — is the same feature class already evaluated and rejected on
2026-07-09 (violates eyes-not-hands; see
[[root-maturity-self-assessment]]). Not re-opened. loopany is a different
shape (action/outcome ledger, not a knowledge wiki) with one genuinely new
piece: a `reflect` skill that splits self-evolution into a `learning`
artifact (a belief, with evidence) and a separate `skill-proposal` artifact
(the matching behavior change) — human accepts/rejects, rejected reasons
logged so they don't resurface, accepted ones get a `check_at` follow-up.
This stays inside the eyes-not-hands boundary rather than violating it.

**Action taken, per Chris's choice ("Route to AI_AUTOMATION_SYSTEMS raw/,
draft a proposal"):**
1. Moved all 8 clippings into this wiki's `raw/` (renamed for clarity;
   `Clippings\` now empty).
2. Updated `llm-wiki-pattern-and-second-brain-tools.md` with a new
   "2026-07-13 Update" section covering both tools and the verdict above.
3. Drafted `proposals/2026-07-13_belief-proposal-split-for-system-flags.md`
   — adapts loopany's belief/proposal split as an *optional* addition to
   `SYSTEM_FLAGS.md` for flags that generalize into a reusable lesson,
   scoped as a lightweight convention (no new tooling/database), not a
   port of loopany's full artifact machinery. Pending Chris/CASTLE review.

**Noted, not yet actioned:** the root-level `Clippings\` folder is likely a
misconfigured Obsidian-clipper intake target — `WHERE_IT_GOES.md` names
`77-INBOX\Clippings\` as the correct landing zone. Flagging for Chris to
either fix the clipper's save path or confirm the root-level folder is
intentional; not fixed unilaterally since it may be a deliberate setting.

Files changed: `raw/` (8 new files), `wiki/llm-wiki-pattern-and-second-brain-tools.md`,
`wiki/proposals/2026-07-13_belief-proposal-split-for-system-flags.md` (new),
`index.md`, this log.

Next: Chris/CASTLE review of the belief/proposal-split proposal; separately,
resolve the `Clippings\` vs `77-INBOX\Clippings\` intake-path question.

## 2026-07-13 (session 16, continued) — Full ingest pass on the 8 raw/ clippings, chunked, with one live web fetch

Chris asked for the formal ingest process to run on today's raw/ intake
specifically (not just the lighter comparison-page update above), chunked
where needed, with explicit permission to visit linked websites if the
clippings themselves were incomplete. Read all 8 sources in full (5 not yet
fully read in the prior pass: the GBrain README, the AI Jason video
transcript, loopany's `CLAUDE.md`, `INSTALL_FOR_AGENTS.md`, and root
`README.md`; `loopany part 3/4` — ONBOARDING.md and the resolver SKILL.md —
were already read in full in the prior pass). Found the raw/ material,
while thorough, didn't include the actual `loopany-reflect/SKILL.md` — the
resolver in raw/ points to it, but only its README-level CLAUDE.md summary
was captured, not the skill file itself, and that skill is the direct
source basis for the drafted proposal. Fetched it live via `gh api
repos/superdesigndev/loopany/contents/skills/loopany-reflect/SKILL.md`
rather than working from the summary alone — confirmed concrete mechanics
not visible in the clippings: pattern thresholds (≥3 tasks same class, ≥2
contradicting an existing belief, ≥3 dismissals over ≥2 weeks before a
belief is written), an evidence-chain verify step (`loopany trace
--direction backward`) before a proposal is actionable, and the accept flow
committing the target file and the proposal artifact together in one git
commit.

Synthesized a new dedicated page rather than further expanding the
comparison page — the GBrain/loopany material is substantial enough
(schema packs, hybrid search, Minions job queue, eval framework, the full
artifact/kind/domain model) to warrant its own file per this wiki's own
per-source-cluster convention, keeping `llm-wiki-pattern-and-second-brain-tools.md`
as the pattern-history/verdict hub rather than letting it absorb full
architectural depth. Also folded in the AI Jason video's closed-loop-
operations framing (open-loop vs. closed-loop, the five-component loop,
factual-vs-procedural memory split, the Airbnb SEO and ads-optimization
case studies) as the third source in the same page, since it's the general
pattern both tools implement rather than a fourth standalone concept.
Strengthened the drafted proposal with the now-confirmed threshold/
verify-step mechanics (not available when it was first drafted from the
README-level summary).

Files changed: `wiki/self-improving-agent-architectures-gbrain-loopany-closed-loop.md`
(new); `wiki/llm-wiki-pattern-and-second-brain-tools.md` (2026-07-13 update
section trimmed to a pointer, frontmatter `source:` line updated with the
live-fetch citation); `wiki/proposals/2026-07-13_belief-proposal-split-for-system-flags.md`
(Proposed Change and Source Basis strengthened with confirmed mechanics);
`index.md` (new page listed, Status line updated to twenty pages); this log.

Next: Chris/CASTLE review of the proposal, now grounded in confirmed
(not summarized) loopany mechanics.

## 2026-07-12 (session 15) — Building a Second Brain promoted from 77-INBOX + report recommendations implemented

Chris asked for the `BUILDING_A_SECOND_BRAIN_ROOT_STRUCTURE_REPORT_2026-07-12.md` findings turned into an approvable plan, then approved it. Verdict: the book validates `.ROOT`'s existing CODE/PARA-equivalent architecture — no structural rebuild. Implemented, in order:

- **Pass 0 (prerequisite):** verified all four corrections from `ROOT_OPERATING_INSTRUCTIONS_VALIDATION_2026-07-12.md` were already resolved by an earlier same-day session; re-ran `validate_boot_chain.py` (PASS), `wiki_lint.py` (0 blockers), `frontmatter_audit.py` (baseline-consistent) to confirm the fix actually holds rather than trusting the log entry alone.
- **Pass 1:** capture-quality filter added to `CASTLE\OPERATIONS.md`'s Weekly Inbox Routing Checklist; the Hemingway Bridge merged into the existing Handoff Ritual (canonical definition now in `AGENT.md`, `CLAUDE.md` trimmed to a pointer — avoided creating a second overlapping handoff structure); a `SKILL: Project Kickoff` added to `HAT_OPERATOR_PLAYBOOKS.md` paired with the existing `SKILL: Asset Harvest`, expanded to `SKILL: Project Completion & Asset Harvest`.
- **Pass 2:** piloted "At a Glance" blocks on exactly 3 high-use pages (not vault-wide): PYTHON `stage-01-python-atoms.md`, PHYSICS `stage-3-vectors.md`, BUSINESS `smb-ai-audit-method.md`.
- **Pass 3 (this wiki):** moved `77-INBOX\buildingasecondbrain.pdf` → `raw\Building-a-Second-Brain-Tiago-Forte-2022.pdf` (raw, now immutable); wrote `wiki\building-a-second-brain-root-application.md` summarizing the verdict and pointing to the full report rather than duplicating it; updated `index.md` (Status line + Pages list).

Declined per the report's own §7: PARA rename, new tag scheme, vault-wide Progressive Summarization, "Mode: DIVERGE/CONVERGE," a "favorite problems" list.

One unrelated drift noticed during Pass 0 verification, out of scope here: `03-WIKIS\EDUCATION\wiki\learning-how-to-learn-principles.md` is missing from that hub's index (orphan page) — flagged for the EDUCATION hub's own next touch or the monthly lint pass, not fixed opportunistically.

Files changed: `AGENT.md`, `CLAUDE.md`, `CASTLE\OPERATIONS.md`, `HAT_OPERATOR_PLAYBOOKS.md`, `ROOT_OPERATING_MANUAL.md`; the 3 pilot pages; this wiki's `raw\` (new file) and `index.md`; this log; today's DAILY.

Next: evaluate the 3-page At a Glance pilot's retrieval/maintenance cost at the next weekly review before expanding further.

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

## 2026-07-12 (session 14) — OpenAI Platform/ChatGPT/Codex docs pack ingested in chunk format (moved from CASTLE)

### Work completed
Chris relocated the OpenAI Platform/ChatGPT/Codex docs pack (95 files) from `00-BRAIN\CASTLEawooks\OPEN_AI-CHATGPT_CODEX_FILES\`
to its correct home, `raw\OPEN_AI-CHATGPT_CODEX_FILES\` in this wiki, and directed the same chunked full-read ingest
as the same-day Claude Code pack. CASTLE's prior pass (`00-BRAIN\CASTLE\wiki\source-summaries\openai-platform-docs-pack-2026-07.md`)
had only deep-read Chunks 01-04 and 08 of its own 10-chunk routing (~60 of 95 files at real depth); the
remaining ~35 were inventory-only. Ran six parallel research forks against a fresh thematic grouping, then
a seventh closing fork to route a coverage gap the fifth fork surfaced mid-ingest.

### Pages created/updated (13 new, 4 edited)
New: openai-responses-api-state-and-streaming.md, openai-sdks-cli-and-agent-builder.md,
openai-model-lineup-and-selection.md, openai-multimodal-generation.md, openai-tools-and-function-calling.md,
openai-agents-sdk-and-orchestration.md, openai-mcp-and-chatgpt-apps.md, openai-gpt-actions.md,
openai-prompting-and-reasoning-models.md, openai-evals-and-red-teaming.md,
openai-fine-tuning-and-legacy-assistants.md, openai-responses-multi-agent.md, openai-webhooks-and-compaction.md.
Edited (fold-ins from the closing fork's gap-fill): openai-tools-and-function-calling.md (Agent Skills, Shell
tool, Retrieval/vector stores), openai-evals-and-red-teaming.md (grader mechanics in depth),
openai-mcp-and-chatgpt-apps.md (ChatKit session-security addendum), openai-agents-sdk-and-orchestration.md
(cross-link to the new Multi-agent page). index.md (8th research batch, 13 new page entries, raw/ status
updated). raw/README.md blocked by the hard `raw/**` deny rule, same as the Claude Code ingest — cannot be
corrected by any session, only Chris directly.

### Two raw-file defects found (flag only, not fixed — raw/ immutable)
- **Title-collision defect (new class)**: 12 files (`OpenAI API.md` through `OpenAI API 9.md`,
  `OpenAI AP15I (1)/(2).md`) all inherited the literal page `<title>` "OpenAI API" from the doc site during
  capture — real topic identity only recoverable by opening each file and reading its source URL. Triaged by
  SHA-256: none are duplicates, all 12 are genuinely distinct content. All 12 now routed (2 via the models
  page, 10 via the closing fork). Different failure mode than the already-flagged byte-identical
  Agents-SDK-duplicate (SYSTEM_FLAGS #63-adjacent) — worth its own flag if Chris wants a SYSTEM_FLAGS entry.
- **Second mislabeled file**: `Node reference  OpenAI API.md` actual content is the Agent Builder node
  catalog, not a Node.js SDK reference — same defect class as `CLI_USE.md` in the Claude Code pack.
- Confirmed (not just repeated from CASTLE's note): `Agents SDK  OpenAI API 1.md` is byte-identical to
  `Agents SDK  OpenAI API.md` (SHA-256 0ddb73d5...92db1), independently re-hashed.

### Two hard dates surfaced that CASTLE's inventory-level pass missed
- OpenAI Evals platform: read-only October 31, 2026; fully shut down November 30, 2026 (same date as Agent
  Builder and Prompt objects deprecation).
- Assistants API: hard shutdown **August 26, 2026**. Fine-tuning platform already closed to new users.

### Findings flagged for Chris (none drafted as proposals)
- Cross-vendor pattern convergence (now recurring across both packs): `tool_search`/Programmatic Tool Calling
  = independent reinventions of MCP progressive discovery/code mode; consequential-action gating confirmed
  three times (Claude permission modes, MCP `require_approval`, GPT Actions `x-openai-isConsequential`);
  prompts-as-versioned-files validated a second time (Prompt objects deprecation); the index+detail-file
  memory shape now confirmed a third time (Claude auto memory, `.ROOT` memory/, OpenAI Sandbox Agents).
- OpenAI Agents SDK has genuine orchestration primitives (handoffs, resumable-approval state machine) that
  Claude Code's subagent model lacks — confirmed real, also confirmed not needed by `.ROOT`'s own fork
  pattern (which only ever needs agents-as-tools, never full handoff).
- Responses API Multi-agent (model-initiated, built-in) is directly relevant landscape research given
  `.ROOT`'s own heavy parallel-fork usage — this very ingest used 7 forks.
- Compaction: OpenAI's mechanism is an opaque encrypted item; Claude Code's `/compact` is a human-readable
  re-injected summary — worth knowing which engine a session is running on before relying on mid-session
  context recovery.
- Secure MCP Tunnel has no documented Anthropic equivalent — a real ecosystem-maturity gap worth the
  Category 10 agent-vetting screen knowing.
- `.ROOT` already runs two of OpenAI's three evaluator types unnamed (wiki_lint/frontmatter_audit as metric
  graders, Codex validation passes as LLM-as-judge) but has no persistent regression dataset of known-good/bad
  governance states — structural gap, not urgent.
- Red-teaming `.ROOT`'s own permission hardening (deliberately probing the 88-JOURNAL/raw/ deny rules) is a
  concrete, cheap exercise nobody's run yet.

### Next action
Chris decides whether any flagged item (from this session or the same-day Claude Code ingest) becomes a real
`wiki/proposals/` entry, and whether the title-collision defect warrants a SYSTEM_FLAGS entry.

## 2026-07-12 (session 15) — Four proposals drafted from the docs-pack ingest findings + two SYSTEM_FLAGS raised

### Work completed
Chris directed writing up the flagged-but-parked findings from sessions 13-14 (the Claude Code and OpenAI
docs pack ingests). Sorted the ~20 flagged items into three buckets: genuine governance-change candidates
(drafted as formal proposals below), informational raw-file defects (raised as SYSTEM_FLAGS, not proposals —
they are not governance changes, just tracked findings), and open questions not yet proposal-shaped (auto
memory vs. `.ROOT`'s memory/ system, the security-guidance plugin — both explicitly left parked per the
ingesting forks' own judgment, no action taken).

### Proposals drafted (all PENDING CHRIS / CASTLE REVIEW — none applied)
1. `proposals/2026-07-12_governance-drift-detection.md` — standing staleness check (script/weekly-sweep/
   red-team options), direct response to the same-day Codex validation incident plus REVIEW.md and OpenAI
   evals cross-vendor confirmation of the same failure class.
2. `proposals/2026-07-12_mid-session-governance-edit-discipline.md` — one-paragraph AGENT.md addition on the
   confirmed mid-session CLAUDE.md-edit-doesn't-apply-until-/clear mechanic.
3. `proposals/2026-07-12_session-close-capture-prompt.md` — small session-close skill addition, modeled on
   Claude Code's own `capture-what-to-remember` prompt-library card.
4. `proposals/2026-07-12_mcp-vetting-screen-secure-tunnel-gap.md` — one bullet added to the already-approved
   Category 10 vetting screen for the Secure MCP Tunnel / private-network-MCP gap.

### SYSTEM_FLAGS raised (informational, LOW priority — not proposals)
- Flag 68: raw-file naming defects (12-file title collision in the OpenAI pack + two mislabeled files —
  `CLI_USE.md` and `Node reference  OpenAI API.md`). All four already correctly routed in wiki pages.
- Flag 69: `Agents SDK  OpenAI API 1.md` confirmed byte-identical to `Agents SDK  OpenAI API.md` — same
  defect class as closed flag #63.

### Files changed
Four new proposal files (above); `index.md` (Proposals section, four new PENDING entries);
`00-BRAIN\SYSTEM_FLAGS.md` (flags 68-69 added to OPEN FLAGS, header timestamp updated) — this is the flag
tracker's own designed intake mechanism, not a governance rewrite; this log.

### Next action
Chris/CASTLE review the four proposals; promotion into their target files (`AGENT.md`,
`session-close/SKILL.md`, `TECHNOLOGY_LIBRARY_STRATEGY.md`, or a wiki_lint.py change) happens only after
approval, same lane sequence as the two already-promoted proposals in this wiki.

## 2026-07-12 (session 16) — Full-system instruction-file audit against the docs-pack ingest

### Work completed
Chris directed a full audit of every human/AI instruction file across `.ROOT` (46 files: AGENT.md, all
lane files, CASTLE governance, all 9 HATS, all 7 wiki CLAUDE.md/HOW_TO_USE.md pairs, all skill files) against
two baselines: the deep knowledge from today's 18-page Claude Code + OpenAI docs-pack ingest, and what CASTLE
itself concluded from the same raw material this morning (its two source-summaries + what it applied into
`FINAL_ROOT_LAUNCH_OPTIMIZATION_REPORT_2026-07-12.md`). Ran five parallel audit forks by cluster.

### Result: most of the system holds up clean
All 9 HATS, 5 of 6 remaining wiki hubs, all CASTLE pointer files, two of three skill files, and the majority
of the universal-OS files (ATLAS.md, CHRIS_CORE.md, CHRIS.md, root pointers, START_HERE.md) showed no
contradictions. `ROOT_OPERATING_MANUAL.md` (built this morning from CASTLE's synthesis) independently
converges with the new prompt-library six-pattern checklist — good validation, no change needed.

### Direct fix applied (same failure class already fixed twice today)
EDUCATION `HOW_TO_USE.md` + `CLAUDE.md` — Start Here and Current State falsely said no course had
activated, contradicting the hub's own `current-position.md` (three live courses: TCOM 2010, ECON 1000,
ENGR 1000) and `index.md` (2 real pages). Third instance of the identical stale-current-state pattern found
today (after AI_AUTOMATION_SYSTEMS and Capability Library) — corrected directly, same as those two.

### Four new proposals drafted (PENDING REVIEW, none applied)
1. `2026-07-12_extension-trigger-table.md` — adds the Claude Code docs' symptom-to-tool-type decision table
   to AGENT.md/CLAUDE.md, replacing judgment-only guidance for when a pattern earns a skill/hook/subagent/etc.
2. `2026-07-12_eval-gate-complexity-scaling.md` — AGENT.md's fixed five-test-case Agent Evaluation Gate (from
   CASTLE's shallow morning read) doesn't match the deeper finding that verification needs grow with
   architecture complexity; proposes scaling test cases to what's actually being changed.
3. `2026-07-12_castle-research-boundary-and-raw-placement.md` — **the audit's headline finding.** CASTLE's own
   OPERATIONS.md says it is not the landscape-research/self-evolution layer, but it did exactly that research
   in place this morning (both docs packs ingested directly in `CASTLEawooks\`, source-summaries
   written, claims applied into the launch report) — AI_AUTOMATION_SYSTEMS's exact charter. This is also the
   root cause of why both packs needed same-day relocation. Proposes a `WHERE_IT_GOES.md` raw-intake rule.
4. `2026-07-12_session-close-high-flag-hook.md` — the session-close skill's "HIGH flag must be fixed before
   closing" rule is prose, not an enforced hook, per the now-confirmed "guardrails belong in hooks" principle.

### Minor item flagged, not proposed
`atlas-brief` skill: the `.claude` copy says "Claude" generates the brief, the `.agents` copy says "Codex" —
everything else identical. Likely intentional per-engine parameterization, but fragile (a human has to
remember to hand-edit one word in two places). Needs a yes/no from Chris, not a full proposal.

### Files changed
`03-WIKISDUCATION\HOW_TO_USE.md`, `CLAUDE.md`; four new proposal files; `index.md` (8 proposals now
listed, all PENDING); this log.

### Next action
Chris reviews the 8 pending proposals (4 from the docs-pack findings, 4 from this audit) and confirms the
atlas-brief parameterization question.

## 2026-07-12 (session 17) — MCP vetting-screen proposal approved and applied

### Work completed
Chris approved `proposals/2026-07-12_mcp-vetting-screen-secure-tunnel-gap.md` with a wording revision pass:
folded into `TECHNOLOGY_LIBRARY_STRATEGY.md` Category 10's existing "Check for:" list (matching the
document's actual flowing-prose style, not the bold-header format the draft used) and genericized away from
naming a single vendor product — the same ingest that found Secure MCP Tunnel also found Agent Builder and
Prompt objects both sunsetting November 30, 2026, so a durable checklist shouldn't hard-pin a product name
that may not exist next quarter. Applied clause: check whether the vendor has any no-inbound-port
private-network bridge at all when the target system isn't internet-reachable; reverify specific offerings
against current docs rather than assuming from memory.

### Files changed
`02-LIBRARY 8-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md` (Category 10 + Last Updated footer);
`proposals/2026-07-12_mcp-vetting-screen-secure-tunnel-gap.md` (status APPROVED & APPLIED); `index.md`; this log.

### Result
Shipped. Third proposal from this wiki to complete the full research -> proposal -> review -> promotion loop
(after the July 8 vetting screen itself and the July 9 wiki-shared-layer cleanup).

### Next action
Seven proposals remain PENDING REVIEW (governance-drift-detection, mid-session-governance-edit-discipline,
session-close-capture-prompt, extension-trigger-table, eval-gate-complexity-scaling,
castle-research-boundary-and-raw-placement, session-close-high-flag-hook).

## 2026-07-12 (session 18) — CASTLE review pass: 4 of 7 proposals applied, 1 partial

### Work completed
Chris asked CASTLE to put its hat on and review the 7 pending proposals from sessions 16-17. Ran the
standard five-point castle discipline (why now / proof required / realm / next action / return path)
against each. Verdict: 3 approved as-drafted, 1 approved with a dedup fix, 1 partially applied (touches
CASTLE's own OPERATIONS.md, which CASTLE cannot self-approve), 1 needs a compact-rewrite pass before it
can ship, 1 deferred to Codex (would be the first hook in the system, undesigned).

Mid-review, Chris asked a design question: should HATS content move into real Claude Code Skills instead
of plain `.md` files, given skills load on-demand? Verified live: Claude Code and claude.ai do NOT share
skills (confirmed via platform.claude.com docs — "Custom Skills do not sync across surfaces"); Codex CLI
and ChatGPT don't either (ChatGPT only gets skills via plugins, doesn't scan `.agents/skills/`). This
settled the question: cross-engine content (HATS, AGENT.md) correctly stays plain-file since Claude Chat
and ATLAS can't read either skills folder at all; the three (now four) existing skills are correctly
scoped to Claude-Code/Codex-CLI-only rituals.

### Applied
1. **Mid-session governance-edit discipline** — one paragraph added to `AGENT.md` § File Safety.
2. **Session-close capture prompt** — added to both `.claude` and `.agents` copies of `session-close/SKILL.md`
   (confirmed byte-identical mirror is correct here, unlike `atlas-brief`'s deliberate per-engine split).
3. **Extension trigger table** — added to `AGENT.md` as its own section; `CLAUDE.md` points to it instead of
   duplicating. Applying this surfaced a related trim: `AGENT.md`'s Graph Color Maintenance section (2
   lines, rarely-needed procedure) demoted into a new `graph-colors` skill, mirrored in both skills folders
   — a live example of the table's own logic applied to `AGENT.md` itself. Chris confirmed via a quick
   question before this specific trim.
4. **CASTLE research-boundary + raw placement (half)** — the `WHERE_IT_GOES.md` raw-intake rule is live:
   source material landing in `CASTLEaw\` matching a wiki's charter must be relocated before processing,
   not ingested in place. The `OPERATIONS.md` boundary-reinforcement half stays PENDING — CASTLE's own rule
   says `OPERATIONS.md` edits need Chris directly, even under CASTLE's own review.

### Still open
- **Eval-gate complexity scaling** — approved in principle, needs a compact-rewrite pass (the whole point of
  the existing Agent Evaluation Gate was staying short) before the exact text ships.
- **CASTLE OPERATIONS.md boundary language** — needs Chris's explicit call on how much raw-triage latitude
  CASTLE keeps.
- **Session-close HIGH-flag hook** — deferred to Codex; would be the first hook in `.ROOT`, undesigned.

### Files changed
`00-BRAIN\AGENT.md` (3 edits); `00-BRAIN\CLAUDE.md` (1 pointer edit); `00-BRAIN\WHERE_IT_GOES.md`;
`.claude\skills\session-close\SKILL.md`, `.agents\skills\session-close\SKILL.md`;
`.claude\skills\graph-colors\SKILL.md` (new), `.agents\skills\graph-colors\SKILL.md` (new); four proposal
files (status updates); `index.md`; this log.

### Next action
Draft the compact eval-gate rewrite for Chris's review; get Chris's call on OPERATIONS.md triage latitude;
hand the session-close hook to Codex's next audit pass.

## 2026-07-12 (session 19) — CASTLE research-boundary proposal fully resolved

### Work completed
Closed out the last open half of `2026-07-12_castle-research-boundary-and-raw-placement.md`. Chris considered
a loosening of the `WHERE_IT_GOES.md` raw-intake rule (let CASTLE read/reference raw material in place,
only relocate once fully absorbed) and explicitly declined it — the stricter original wording (relocate
before processing, no in-place ingest) stays exactly as applied earlier today. No `OPERATIONS.md` edit was
made; the `WHERE_IT_GOES.md` rule alone fully closes the gap.

Established a standing practice alongside this: raw-file retirement (removing a source once its derived
`.md` content has fully absorbed it) is a judgment call Claude flags when noticed, not an automated rule —
except the Claude Code and OpenAI/Codex documentation packs, a standing exception that never retires
regardless of derived-page completeness (re-consulted directly, not just summarized once).

Checked `00-BRAIN\CASTLEaw\` as of this session: empty of content (both docs packs already relocated
to `AI_AUTOMATION_SYSTEMSaw\` earlier today, folder skeleton + README.md only) — nothing currently
retirement-eligible.

### Files changed
`2026-07-12_castle-research-boundary-and-raw-placement.md` (status -> APPROVED & APPLIED, both halves);
`index.md`; this log.

### Result
All 8 proposals from sessions 13-18 now resolved: 6 fully applied, 1 (eval-gate complexity scaling) has
drafted compact wording awaiting Chris's go-ahead, 1 (session-close HIGH-flag hook) deferred to Codex as
undesigned.

## 2026-07-12 (session 20) — Eval-gate complexity-scaling proposal applied

### Work completed
Chris approved the drafted compact rewrite. Applied to `AGENT.md` § Agent Evaluation Gate, rule 2: replaced
the fixed fifteen-word "at least five cases" list with a scaled version — typical/edge/failure-recovery stay
the floor for any workflow, and tool-selection/data-precision, handoff-accuracy, and
adversarial/permission-boundary cases now trigger on what the workflow actually introduces (tools, multiple
agents, sensitive actions) rather than being demanded uniformly regardless of complexity. Rule count and
section structure unchanged; kept to one sentence, matching the original's compactness.

This closes out the eval-gate proposal, the last of the 8 proposals from today with an open action. Final
tally: 7 fully applied (MCP vetting screen, mid-session governance-edit discipline, session-close capture
prompt, extension trigger table + graph-colors demotion, CASTLE research-boundary/raw-placement,
eval-gate complexity scaling), 1 deferred to Codex (session-close HIGH-flag hook, undesigned).

### Files changed
`AGENT.md`; the proposal file (status -> APPROVED & APPLIED); `AI_AUTOMATION_SYSTEMS\wiki\index.md`; this log.

### Next action
Session-close HIGH-flag hook remains parked for a future Codex audit pass — would be the first hook in
`.ROOT`. Nothing else currently open from today's proposal batch.

## 2026-07-13 — Local-root path sweep

### Work completed
Corrected the live infrastructure claim in `openai-webhooks-and-compaction.md`:
`.ROOT` is now a local C: vault cloud-backed by Google Drive, not a local Google
Drive working tree. This was part of the full local-root path sweep after Chris
made `C:\Users\chris\.ROOT` canonical.

### Files changed
`openai-webhooks-and-compaction.md`; `index.md`; this log.

### Next action
Continue the normal research cadence; path governance is now owned by the C:
canonical-workspace rule in `00-BRAIN`.

## 2026-07-13 — CASTLE review: two bounded self-evolution proposals promoted

- Chris approved the belief/proposal split as a lightweight pilot: no
  `SYSTEM_FLAGS.md` rewrite and no retrofits. A generalized lesson now needs
  two unrelated supporting flags/incidents, evidence citations, a `check_at`,
  and any behavior change remains proposal-gated in
  `00-BRAIN\SYSTEM_LEARNINGS.md`.
- Chris approved governance-drift detection **Option B only**: CASTLE's
  weekly sweep rotates one stated-current-state check against its live source.
  Script expansion and red-team work remain deferred because the evidence is
  not yet strong enough to justify more infrastructure.
- Updated this index and both proposal outcomes.
- Next: run the new practices in normal review cadence; do not add automation
  unless repeated evidence demonstrates the manual checks are insufficient.

## 2026-07-14 — Unified-team and Second Brain follow-up applied

- Re-read the complete *Building a Second Brain* extraction and successfully
  inspected all eight supplied visuals, closing the July 12 viewer limitation.
- Updated the application page: DIVERGE/CONVERGE is now a lightweight AI work
  mode after Chris directly removed hard drift control over himself. It does
  not constrain Chris or justify a PARA rebuild.
- Applied the approved system-evolution distinction: Chris-directed change may
  proceed after impact review and approval; AI-initiated proposals still need
  repeated evidence.
- Next: validate the unified operating model in normal use and review friction
  at the next weekly/monthly cadence.

## 2026-07-14 — Clippings triaged; two bounded knowledge-maintenance deltas applied

- Reviewed the July 14 Second Brain/AI-OS clipping batch. Promoted only source
  prioritization and the temporal-update/context-variant/true-contradiction
  distinction; the larger raw/wiki/index/log architecture was already live.
- Preserved the two useful source articles in this hub's immutable `raw/` and
  archived the promotional duplicates/search capture as reference/noise.
- Added a primary-source research queue and corrected “wiki replaces RAG” into
  an evidence-based tradeoff using three 2026 research papers. Nightly
  heartbeats, autonomous repair, and marketing/revenue claims remain rejected.
- Applied Chris-authorized governance reconciliation in the universal OS and
  human maps; expanded `validate_boot_chain.py` with semantic contract checks.
- Next: normal use first. Inspect one queued primary mechanism only when a
  concrete failure or review question gives it a job.

## 2026-07-14 — North Star system-capability return contract installed

- Added the cross-model `.ROOT` capability contract under
  `01-NORTH_STAR\System Contracts\`, covering teaching, research, engineering,
  maintenance, business partnership, strategy, self-evolution, proof, and return.
- Updated this hub's guide/operating contract so external AI change may feed
  Watchtower only after evidence and materiality; internal friction remains a
  proposal/SYSTEM_FLAGS path.
- Next: use the contract in normal sessions and repair only observed failures.

## 2026-07-14 — Human guide path audit

- Rechecked the hub's user guide against the live boot and capability-contract
  paths. Added the exact conditional route to `ROOT_CAPABILITY_CONTRACT.md` and
  retained AGENT.md as the universal authority.
- Strict wiki lint and boot validation pass; no active dead link remains.
