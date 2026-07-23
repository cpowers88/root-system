---
type: log
tags: [business]
timeline: log
---

# Wiki Log

## 2026-07-23 — Raw source map built (Codex plan, Claude Chat-scoped, Claude Code-executed)

Executed `ExecutionBrief_Buisness-WIKI.md` (Claude Chat-authored, reduced from Codex's
original "Business Learning and Evidence Engine" proposal): a single source-accounting
page for the 69-file `raw/` corpus, explicitly not a curriculum and not a second ranking
model (those guardrails held — `most-profitable-pathways.md` and `market-map.md` remain
the only ranking authorities).

### What Changed
- Created `raw-source-map.md`: a classification table (Type / Category / Authority /
  Pub date / Industries / Company size / Concepts / Evidence value / Implementation
  value / Wiki destination / Processing / Reopen trigger) for all 69 sources, a blank
  CSV-compatible evidence-row schema for future research capture, and a curated reading
  sequence (question-per-source, explicitly framed as a starting point, not a
  curriculum).
- Added one link row to `index.md` §5 (Capability Building) pointing to the new page —
  the only edit to an existing file, additive only.

### What Was Added
- `raw-source-map.md` (new page, `wiki/ai-integration-company/`).

### What Was Updated
- `wiki/ai-integration-company/index.md` (1 row added under Capability Building).

### Correction made mid-build
- The table was first drafted from a fresh read of each source's title/opening pages,
  without cross-referencing this log. Cross-checked against the July 8/9/12/16 intake
  entries below before finalizing and corrected several rows that fresh reading got
  wrong relative to what's already been decided: `state-of-ai-2026.pdf` is a confirmed
  duplicate of the Deloitte "State of AI in the Enterprise" survey already cited in
  `market-map.md` (not an unconfirmed-publisher source needing verification);
  `NewCodeofEstimating.pdf` is UK commercial/PFI tendering content for large
  contractors, wrong market segment for the current US residential/light-commercial
  hypothesis (not a usable estimating reference); `HowAIcanbenefitabusinessatbanksandinsurace.pdf`
  is ~2020-vintage pre-GenAI vendor material for enterprise carriers, wrong vintage and
  audience. Also corrected several `Processing` values from forward-looking
  recommendations ("read-selectively") to reflect sources already read-fully and
  absorbed into named pages in the July 16 batch (Mom Test, Good Strategy/Bad Strategy,
  Prediction Machines, The AI Dossier, All-In on AI, Inspired, Transformed, Psychology
  of Human Misjudgement), so the map doesn't send anyone back to re-read what's done.

### What Was Parked
None newly parked — the map documents prior park/exclude decisions (Seneca, book list,
Mastery, Undercover Economist, AI and ML Red/pptx, howtobuildyourcareerinAI,
HowAIcanbenefit..., NewCodeofEstimating, 2606.12428v1) rather than making new ones.

### Missing Data Needed From Chris
None for this build. Two sources remain flagged from prior sessions as JS-blocked
scrapes with only frontmatter descriptions usable (`Census Bureau's 2023 Annual
Business Survey...md`, `Large Firms With at Least 20 Employees Biggest AI Users.md`) —
carried into the new map's Reopen triggers, not resolved here.

### Recommended Next Action
None urgent. The map is a lookup tool, not a task — next raw-file drop gets a row here
per the Raw Intake Protocol before any extraction happens.

## 2026-07-13 — Template-library navigation repair

### What Changed
- Repaired six links that treated `template-library.md` as a sibling of the
  company pages even though it lives in `ai-integration-company/templates/`.

### What Was Added
None.

### What Was Updated
- `wiki/ai-integration-company/index.md` (2 links)
- `wiki/ai-integration-company/smb-ai-audit-method.md` (1 link)
- `wiki/ai-integration-company/start-here.md` (3 links)

### What Was Parked
None.

### Missing Data Needed From Chris
None.

### Recommended Next Action
None. The BUSINESS page catalog now resolves its template-library navigation.

## 2026-07-12 — Full `raw/` intake: 24 unprocessed sources (7 background research forks + direct data pulls)

Chris asked for the "chunk raw intake of the new files in raw." Cross-referenced all 39 files in `raw/` against this log; ~13 were already absorbed in prior sessions (McKinsey survey, BTOS clipping + AI supplement, EDGAR clips, Procore clips, WTI report, Entrepreneurship textbook → `venture-fundamentals.md`). Confirmed scope with Chris on how to handle three full-length textbooks (marketing, 2 estimating) plus the 18.6MB WEF report before starting — Chris chose full intake on everything. Processed the remaining 24 sources: small clippings and xlsx data pulled directly; the five large-PDF sources delegated to parallel research forks (read-only, no file writes) to keep raw PDF content out of the main session's context — synthesis and all page edits done directly afterward so parallel forks never collided on the same file.

### What Was Added
No new pages — every source strengthened an existing page (§7A step 2: update over create held for all 24 sources).

### What Was Updated (9 pages)
- **`market-map.md`** — heaviest update: (1) small-firm AI-adoption-curve nuance and a job-loss objection line from two Census Research Matters clippings; (2) BTOS methodology credibility detail (1.2M businesses, 6 panels, MSA-level sort, Oct–Nov 2025 shutdown data gap) from `BTOS - About/Methodology.md`; (3) a new "Current Business-Conditions Snapshot" table — live BTOS core (non-AI) index pull via a Python/openpyxl script against the 9 xlsx workbooks, showing Georgia/Atlanta running softer than national/construction on performance, revenue, and demand as of period 202613 (ref. 2026-06-01–14); (4) a measurement-caveat on the 1.4%→9.2% construction AI-adoption figure (CES-WP-24-16 vs. CES-WP-26-25: the Nov 2025 core-question wording changed, so it's a level-shift, not a clean multiplier); (5) the "AI not applicable" objection dropping from 80.9% (2024) to 65% (2026) — the education-led sale window is closing, not permanent; (6) the objection-handling section rewritten around CES-WP-26-25's hard employment-impact numbers (66% augmentation-only, employment change hits only 5% of firms, capital substitution 3x more common) replacing a thin/JS-blocked source citation.
- **`smb-ai-audit-method.md`** — new "Who You're Actually Auditing" subsection (CES-WP-26-25's five-archetype latent-class analysis: 57% of AI-using firms touch ≤3 of 15 functions; most prospects are "Minimalist Adopters," not non-users); new "bid-closing interview" subsection in Step 2 (from the residential estimating textbook — phone/fax-era manual bid-transcription workflow as a concrete discovery-question template for GC/builder clients).
- **`quality-control-and-risk-gates.md`** — shadow-AI finding (CES-WP-26-25: 36% of firms with real employee AI use have no formal adoption policy — ungoverned use is the most common day-one audit finding, not a hypothetical); new "Gap Model" subsection (*Principles of Marketing* Ch.12 — five named failure gaps: discovery/scoping/delivery/promise/perception — for diagnosing a soured engagement).
- **`progressive-operating-thesis.md`** — the redesign *mechanism*, not just correlation (CES-WP-26-25 regressions: functional breadth and investment predict performance; narrow worker-task-only use does not).
- **`agent-manager-job-design.md`** — WEF Future of Jobs 2025's task-shift data (82% of the 2025→2030 shift is pure automation, 19% augmentation) with industry variance (Insurance/Telecom automation-heavy vs. Healthcare/Government augmentation-heavy) for calibrating which of the five roles to emphasize per client industry.
- **`human-role-redesign.md`** — WEF's named fastest-declining roles (Administrative Assistants/Executive Secretaries the largest absolute decline; also Data Entry Clerks, Bank Tellers) as concrete, citable third-party evidence for the Producer→Reviewer→Improver case study.
- **`skill-roadmap.md`** — WEF Core Skills 2025 ranking corroborating the existing Layer 1/2 priority order (systems thinking, resource management, quality control all named core skills; AI & big data ranks only 11th in current importance despite being the fastest-*growing* skill) plus the reskilling-participation trend (50% vs. 41% in 2023).
- **`risks-and-failure-modes.md`** — one-line corroboration on risk #10 (Adoption failure): WEF names organizational resistance to change as employers' #2 transformation barrier globally (46%).
- **`sales-system.md`** — new "Who You're Actually Selling To" subsection (*Principles of Marketing* Ch.7's B2B buying-center roles — initiator/influencer/gatekeeper/decider — for prospects toward the upper end of the target range where an office/ops manager sits between Chris and the owner); one-line addition on consulting as a "credence" purchase (Ch.12) explaining why proof content and referrals carry outsized weight for this business model.

### What Was Parked
- **`HowAIcanbenefitabusinessatbanksandinsurace.pdf`** — 2020-vintage RPA/ML vendor brochure (Danske Bank, BNP Paribas, ING, etc.), pre-GenAI and enterprise-carrier-scale — wrong vintage and wrong audience (carriers, not the small local insurance *agencies* on the expansion map).
- **`state-of-ai-2026.pdf`** — confirmed duplicate: this is Deloitte's "State of AI in the Enterprise" (Jan 2026, n=3,235), already processed in the July 8 batch and cited in `market-map.md`. No action.
- **`howtobuildyourcareerinAI.pdf`** (Andrew Ng) — a personal ML-engineer job-search guide; actively conflicts with `skill-roadmap.md`'s deliberate layer-2 de-prioritization of deep ML/math. Parked.
- **`NewCodeofEstimating.pdf`** — UK commercial/PFI tendering code (bills of quantities, CDM regs, bid-rigging) for large contractors — wrong market segment for the current $2M–$15M US residential/light-commercial entry hypothesis. Revisit only if Chris moves into larger commercial contracting.
- **`Census Bureau's 2023 Annual Business Survey...md`** and **`Large Firms With at Least 20 Employees Biggest AI Users.md`** — both are JS-blocked scrapes (cookie-banner shell only, no body content). Their frontmatter `description` fields were usable and got cited (job-impact headline in `market-map.md`; the "AI use growing Dec 2025–May 2026" line was already cited pre-session). Full body content unavailable until re-captured.
- **`BTOS - Data.md`** and **`URR.xlsx`/`AI26_URR.xlsx`** — not narrative content (a 275K-token scraped HTML dashboard dump, and data-quality/response-rate meta-files respectively). Noted as available data sources, not mined further — low marginal value relative to the Index Estimates pull already done.

### Missing Data Needed From Chris
- Re-capture the two JS-blocked Census clippings (2023 ABS tech-adoption story, May 2026 "Large Firms" story) with a scraper that renders JS, if the full body detail (which industries, what magnitude) is needed for a specific proposal.
- Sanity-check the bid-closing interview questions (`smb-ai-audit-method.md` Step 2) with an actual contractor — the source textbook is from 2011 and assumes phone/fax bid intake; confirm the channel specifics still match 2026 shop practice even though the underlying manual-transcription pattern is still credible per the BTOS near-zero-adoption evidence.
- Decide whether `NewCodeofEstimating.pdf` and the banks/insurance PDF should be archived out of `raw/` or left in place as-is (raw/ is immutable by default — no action taken without Chris's instruction).

### Recommended Next Action
None urgent — this batch is evidence/credibility layering onto an already-built page set, not a new capability. The CES-WP-26-25 findings (customer archetypes, shadow AI, redesign mechanism) are the strongest single addition in this batch and are worth a specific read-through before the next audit engagement or proposal, since they replace softer claims with hard Census microdata across four pages.

## 2026-07-09 (late) — AI Index 2026 evidence folded into market-map

- Part of the flag-55(c) multi-hub ingest (Chris-directed): the Stanford
  AI Index 2026's Economy-chapter evidence was added to `market-map.md`'s
  Market Timing section as a corroboration block under the McKinsey/
  Deloitte findings — 88% org adoption vs single-digit agent deployment,
  productivity gains concentrated in structured work (14/26/50%), US 24th
  in consumer adoption, ISO 42001 (36%) and NIST AI RMF (33%) as rising
  named standards, documented incidents +55% YoY. Neutral,
  university-sourced numbers for outreach and proposals (§7A
  update-over-create: no new page).
- Source PDF: `03-WIKIS\TECHNOLOGY\raw\`; full distillation:
  `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\ai-index-2026.md`; coverage record
  in that wiki's log (session 12).
- Next: none new — the evidence activates in outreach material on the
  Business Arc clock (first conversations ~Sep 2026).

## 2026-07-09 — Citation/sort audit (Chris-directed, all-wikis sweep) + second raw/ intake

Second hub in the hub-by-hub sweep. Structure checks passed: all 51 content
pages reachable from `ai-integration-company/index.md` (root index is the
doorway by design); all 10 templates linked from `template-library.md`; the
"vanished" BTOS clipping is back in `raw/` (restored — content was already
absorbed July 8). Then processed the raw/ files no prior session had touched:

### What Changed
- `smb-ai-audit-method.md` — Procore block gained a fourth audit use: the
  App Marketplace integration check (double-entry checklist from the
  marketplace category list). Source: December & January Integration Roundup
  clipping.
- `market-map.md` — EDGAR data-sources bullet extended: the official API
  overview PDF (22 pp., Dec 2025), Development Toolkit, token-management,
  and versioning clips are implementation reference in `raw/`.
- Cross-hub: the **WTI 2025 annual full report PDF** (15 pp.) sitting in this
  wiki's `raw/` was ingested into AI_AUTOMATION_SYSTEMS's
  `work-trend-index-2024-2026.md` (its series page; completion pass, all
  15 pp. read). It closes that page's flagged gap; citation there points
  here. Lane note: WTI research lives in AI_AUTOMATION_SYSTEMS; the raw file
  stays here untouched (raw/ immutable).

### What Was Parked
- `2606.12428v1.pdf` ("Mapping AI Programs in the U.S.," Muzny et al., 9 pp.,
  early 2026) — a census of US university AI majors/minors. Fails the
  Business Design Rule (no client throughput connection). Possible EDUCATION
  wiki relevance (degree-landscape context for KSU planning) — Chris's call.

### Missing Data Needed From Chris
- `EDGAR Application Programming Interfaces (APIs).md` and
  `... (APIs) 1.md` are byte-identical duplicate downloads (6,905 bytes
  each); one could be removed on instruction (raw/ immutable, not acted on).
- Decide the parked AI-programs paper's disposition.

### Recommended Next Action
None urgent. The EDGAR implementation reference activates when the first
demo dashboard gets built (per the roadmap clock, not before).

## 2026-07-09 — Go-live audit: root index restored

- Created `wiki/index.md` as the standard Business wiki doorway expected by
  the shared `03-WIKIS` session rules.
- No business content changed. The full page catalog remains
  `wiki/ai-integration-company/index.md`; the new root index points there and
  clarifies boundaries.
- Next action: first monthly wiki lint should verify root index links and
  index-vs-live-tree match.

## 2026-07-09 — CLAUDE.md slim rewrite (Chris-approved, go-live eve)

- This wiki's CLAUDE.md rewritten from the ~920-line original build prompt to a
  ~180-line operating file: mission is now a NORTH_STAR.md pointer (the embedded
  quote had drifted — flag-38 pattern), §7A intake / §9 page template / §23 phase
  tags retained, shared blocks now point to `00-BRAIN\AI_Agent.md § Wiki Shared
  Layer`. Old version archived:
  `99-ARCHIVE\ARCHIVED_2026-07-09_CLAUDE_BUSINESS_WIKI.md`. No wiki pages changed.
  Full record: `00-BRAIN\Session_Logs\DAILY_2026-07-09.md` + AI_AUTOMATION_SYSTEMS
  `proposals/2026-07-09_wiki-shared-layer-and-lane-cleanup.md`.

## 2026-07-08 (later same day) — Follow-up data pulls from the intake batch (2 pages updated)

Chris approved both follow-ups from the intake gap report; both executed with live data:

- **BTOS construction pull** — downloaded the Census BTOS 2026 AI Supplement
  (`census.gov/hfp/btos/downloads/AI_Supplement_Table_2026.xlsx`) and extracted the
  sector (NAICS 23), state (GA), and national sheets directly. Added "The
  Construction AI Gap, Quantified" section to `market-map.md` under the Entry
  Hypothesis: construction AI use 9.2% vs 17.9% national (last two weeks); 69% of
  construction non-planners say AI "not applicable" (perception gap → education-led
  sale); 75% of construction AI adopters made no operational changes and only 2.2%
  used a vendor/consultant to integrate (near-virgin integration market); quality
  mgmt 1.6% / supply chain 2.3% AI use (field-ops layer untouched); Georgia tracks
  the national average (17.3%), so the gap is sectoral, not regional. Noted refresh
  cadence (core biweekly, supplement annual).
- **Procore data landscape** — researched the platform's data model (product pages +
  API ecosystem: 90+ endpoints; RFIs, submittals, change orders, daily logs,
  budgets/commitments, timecards, inspections, punch lists). Added a
  construction-specific block to `smb-ai-audit-method.md` Step 2: mine the client's
  Procore instance for real volumes/timestamps for waste math, the double-entry
  finding (Procore + QuickBooks + spreadsheet), and the unused-data → dashboard
  finding. Cross-linked market-map's BTOS section and skill-roadmap's Procore
  training bullet.

Note: the BTOS raw clipping vanished from `raw/` between the morning intake and this
pass (not deleted by the agent — raw/ treated as immutable throughout). Its content
was already absorbed into market-map; flagged to Chris to check Drive trash.

## 2026-07-08 — First `raw/` intake batch (6 sources → 5 existing pages updated, 0 new pages)

First intake under §7A from `raw/` (which stays immutable — sources left in place).
Classification and disposition:

- **McKinsey "The State of AI in 2025" (Nov 2025 survey, n=1,993)** + **Deloitte
  "State of AI in the Enterprise" (Jan 2026, n=3,235 PDF)** — classified market
  research + human-agent operating model + risk/QC evidence. The two surveys
  independently confirm the wiki's core thesis with citable numbers, so they were
  distributed as evidence sections rather than summarized standalone:
  - `progressive-operating-thesis.md` — new "External Evidence" section: high
    performers ~3× more likely to have fundamentally redesigned workflows (McKinsey's
    strongest tested factor); 84% of companies haven't redesigned jobs around AI
    (Deloitte); the activation gap.
  - `market-map.md` — new "Market Timing" section: AI scaling falls off with company
    size (29% under $100M vs ~half of $5B+), the proof-of-concept trap / pilot
    fatigue, and the agent-governance gap (74% deploying within 2 years, 21% mature
    governance) as third-party proof points for outreach.
  - `agent-manager-job-design.md` — Deloitte names the same emerging roles ("AI
    operations managers, human-AI interaction specialists, quality stewards") that
    this page's five roles specify; added as lead Why-It-Matters bullet with the
    telecom-exec force-multiplier quote.
  - `quality-control-and-risk-gates.md` — McKinsey: defined human-validation
    processes are a top high-performer differentiator; inaccuracy the #1 experienced
    AI risk; Deloitte's "agents scaling faster than the guardrails." Added as lead
    Why-It-Matters bullet, framed for use in proposals.
- **Census BTOS clipping** — classified market research (data source, not findings).
  Filed into `market-map.md`'s new "Free Market-Research Data Sources" section:
  biweekly, NAICS-sector × state × size-class data including AI-use rates over time —
  quantifies vertical AI adoption for pitches and audit reports.
- **SEC EDGAR APIs clipping** — classified market research / tool stack (weak but
  real fit): free JSON APIs for public-company XBRL financials. Same market-map
  data-sources section — industry benchmark economics for audit context and free
  real data for demo dashboards. Not parked, but deliberately kept to two sentences.
- **Procore "Tool Training" + "Data in Construction" clippings** — thin course-catalog
  captures from learn.procore.com, classified tool stack / skill roadmap for the
  construction-first entry hypothesis. Added one bullet to `skill-roadmap.md` Layer 1:
  free Procore training (Construction 101/Bootcamp, Data in Construction series, AI
  in Construction program, Estimating) as pre-gate domain-fluency prep — Procore
  vocabulary = credibility with $2M–$15M contractors.

Nothing parked outright; no new pages created (everything strengthened existing
pages per §7A step 2); `index.md` unchanged (no page-set changes). Gap noted for
Chris: the Deloitte PDF's exhibit data is enterprise-skewed — a true SMB-adoption
number for construction specifically would need a BTOS pull (the source is now
filed for exactly that).

## 2026-07-07 (later same day) — North Star realignment pass

Chris asked for a review of the wiki against `.ROOT\01-NORTH_STAR\NORTH_STAR.md`'s July 6,
2026 full rewrite (identity, the Ratchet, the Engine, four-track order, construction-first
entry hypothesis, March 2027 first-client date). Grepped the wiki for that rewrite's
specific language (`March 2027`, `construction`, `Ratchet`, `top 1%`, `Chris + AI`,
`October 8, 2031`, `Engine Question`, `entry hypothesis`) — only one incidental hit found.
The wiki was structurally complete (all 29 required pages + 15 FORGE-migration pages
present) but had not been updated for the identity/timeline rewrite; several roadmap pages
read as an immediate go-to-market plan, which directly contradicts NORTH_STAR.md's
"Foundation: Now–Aug 2026, no clients" and "First client: March 2027."

**Updated (8 files):**
- `north-star-alignment.md` — added the verbatim top-1% identity line, the four-track
  order (school non-negotiable, this wiki is Track 3), a Business Arc timeline table, the
  construction-first entry hypothesis with NORTH_STAR.md's actual reasoning, the Engine's
  four compounding-asset classes, and the Ratchet (floors not ceilings, quarterly-only).
- `index.md` — corrected the North Star summary to the canonical wording, added the
  timeline-gate and entry-hypothesis note to the top-level preamble.
- `market-map.md` — added an explicit "Entry Hypothesis: Construction First" section;
  reframed the vertical list so construction/trades is the decided entry, others are
  post-2028 expansion, not equal first choices.
- `start-here.md`, `first-30-days.md`, `first-90-days.md` — added timeline-gate banners:
  these pages describe Track 3 execution once the First Contact phase opens (~Sep 2026),
  targeting first client March 2027 — not literal day-1-from-reading. Pointed to what's
  actually correct work before the gate (school, Python/SQL, Tracker/POL, audit-method
  prep) instead of outreach/LLC filing.
- `service-offer-ladder.md` — added a callout distinguishing NORTH_STAR.md's literal first
  engagement (observation + written report only, no software, no retainer pitch, no
  bundled Rung-2 proposal) from Rung 1 as the audit product matures into after repeat
  delivery.
- `skill-roadmap.md` — added the ISYE-course-to-audit-capability mapping (Track 1 feeds
  Track 3) and a note that application development (Tracker → POL → client tools →
  products) is part of the identity, not a side quest.
- `one-year-plan.md`, `three-year-plan.md`, `ten-year-scale-plan.md`, `business-setup.md`
  — added one-line date anchors tying each plan's relative years to the actual Business
  Arc calendar (Year 1 ≈ Mar 2027–Feb 2028, Years 2–3 ≈ 2028–2029 overlapping graduation,
  Years 4–10 ≈ 2030–2036 past the North Star date).

No pages deleted, no structural changes to the required page set. This was a content
realignment, not an intake batch — no new pages created.

## 2026-07-07

- First `log.md` for this wiki — didn't exist before (CLAUDE.md §7A step 5 requires
  one; created now as part of the first FORGE intake batch).
- Started intake-migrating FORGE's `wiki\business\` (136 pages) per the FORGE
  retirement brief (`03-WIKIS\CLAUDE.md`). Real intake, not a file copy — each source
  page classified per §7A, checked against the existing 44 pages in
  `wiki\ai-integration-company\` before creating anything new.
- **Batch 1 — Theory of Constraints cluster (7 source pages → 1 new page + 1 existing
  page strengthened):**
  - Consolidated `theory-of-constraints.md` + `the-goal-goldratt.md` (source tracker)
    into one new page, `theory-of-constraints.md`, following the §9 template. Kept as
    a standalone page (not folded entirely into the audit method) because it's cited
    as reusable theory beyond just the audit — e.g. the retainer-model rationale.
  - Folded the five TOC-step pages (`toc-step-1-identify` through `toc-step-5-repeat`)
    into `smb-ai-audit-method.md` as a new "Applying the Five Focusing Steps to a
    Client Engagement" section, plus a constraint-first framing added to Step 4
    (Waste Diagnosis) and a bottleneck-first ranking rule added to Step 6 (Priority
    Scoring). This is where the theory earns its keep — condensed and applied, not a
    1:1 page-for-page port.
  - Updated `wiki/ai-integration-company/index.md` with the new page.
  - Deleted all 7 source pages from FORGE once absorbed.
- **Also found while auditing this folder (not part of the BUSINESS intake):** ~30
  pages in FORGE's `wiki\business\` were actually Sterman *Business Dynamics* case
  studies and Factory Physics/JIT/lean/MRP/ERP history — filed under `business/` but
  tagged `subject/factory-physics` / `subject/system-dynamics`. Moved those to the new
  `03-WIKIS\SYSTEMS\` hub instead (see that wiki's log for detail), not into BUSINESS.
- **Batch 2 — Negotiation cluster (12 source pages → 1 new page, 2 existing pages
  linked):**
  - Consolidated all 12 *Never Split the Difference* pages (10 chapters + Appendix +
    book-level hub) into one new page, `negotiation-toolkit.md`, following the §9
    template. This was a genuine condensation, not a port — the source pages are
    extremely detailed (full hostage-negotiation case narratives per chapter); the new
    page keeps only the reusable tools (Mirroring, Labeling, Accusation Audit,
    Calibrated Questions, the "That's Right" test, negotiator types, the Ackerman
    Model, Black Swan triage, the Negotiation One Sheet) tied directly to audit/sales
    use, per the intake protocol's "don't duplicate full source content" rule.
  - Linked the new page from `sales-system.md` (the close, objection handling, fee
    negotiation) and `smb-ai-audit-method.md` (Step 2 discovery interviews, Step 6
    findings presentations) — both got a sentence added pointing to the toolkit rather
    than a full rewrite, since the negotiation technique is genuinely a separate
    concern from what those pages already cover well.
  - Updated `index.md` with the new page under Commercial Engine.
  - Deleted all 12 source pages from FORGE once absorbed.
- **Batch 3 — Checklist Manifesto cluster (5 source pages → 0 new pages, 3 existing
  pages strengthened):**
  - No new page created — this cluster's ideas distributed cleanly into three existing
    pages rather than needing a standalone home:
    - `quality-control-and-risk-gates.md` gained a "Checklist Design Discipline"
      section (pause points, DO-CONFIRM vs. READ-DO, killer-items-only, real-world
      testing before trusting a gate checklist — WHO trial results as evidence) plus
      the ignorance-vs-ineptitude diagnostic for *why* a gate is failing.
    - `smb-ai-audit-method.md` gained the ignorance-vs-ineptitude diagnostic in Step 4
      (train vs. enforce discipline — two different fixes for the same symptom) and a
      group-interview note in Step 2 (communication checklists / shared power — no
      single role has full visibility, so interview the team together when possible).
    - `risks-and-failure-modes.md` risk #6 (Bad-fit clients) gained the "cocaine
      brain" motivated-skipping mechanism and a Pabrai-style pre-engagement
      due-diligence checklist as the countermeasure.
  - Deleted all 5 source pages from FORGE once absorbed.
- **Batch 4 — Profit First cluster (14 source pages → 1 new page, 2 existing pages
  linked):**
  - Consolidated all 14 pages (the full *Profit First* book — formula, four-account
    system, Instant Assessment, Day One rollout, 10/25 rhythm, debt handling,
    efficiency-before-sales, accountability groups, advanced accounts/RIFA, personal
    application, failure-mode catalog) into one new page, `cash-flow-audit-method.md`.
    Structured as a full second sellable service — parallel to
    `smb-ai-audit-method.md` — since the source material itself frames this as a
    standalone "Cash Flow Audit" service offering, not just reference material.
    Personal-lifestyle-application content (Lifestyle Lock, Wedge Theory, Profit First
    Kids) was deliberately left out of the condensed page — secondary/situational per
    the source's own ranking, not core to the sellable service.
  - Linked from `pricing-models.md` (as a second diagnostic offering) and
    `financial-model.md` (the same discipline applied to the business's own cash).
  - Updated `index.md` with the new page under Service Pathways.
  - Deleted all 14 source pages from FORGE once absorbed.
- **Batch 5 — Lean/VSM cluster (10 source pages → 1 new page, 1 existing page
  strengthened):**
  - Created `lean-methodology.md`: VSM field method (walk twice, pencil/paper,
    lead-time-vs-processing-time), the seven-wastes-plus-one taxonomy, the "monument"
    diagnostic (automating a batch process makes its waste worse, not better), takt
    time/pull, and — the standout artifact — the five-year, four-phase Action Plan as a
    directly adaptable multi-year retainer engagement template.
  - Strengthened `smb-ai-audit-method.md`: Step 2 gained the VSM walk-twice field
    method explicitly; Step 4 gained the seven-wastes naming checklist and the
    monument diagnostic (don't recommend automation on top of a monument).
  - Linked from `retainer-model.md` (the five-year Action Plan as the highest-tier
    retainer template).
  - Updated `index.md`. Deleted all 10 source pages from FORGE once absorbed.
- **Batch 6 — E-Myth cluster (17 source pages → 1 new page, 3 existing pages linked):**
  - Consolidated all 17 pages (Fatal Assumption, Entrepreneur/Manager/Technician,
    business lifecycle stages, Management by Abdication, the Franchise Prototype six
    rules, the five self-audit questions, Innovation/Quantification/Orchestration, the
    full seven-step Business Development Program, the Gap Method/Comfort Zone, and
    `survival-trap.md` — a Profit First page missed in Batch 4, folded in here since it
    shares this cluster's crisis-diagnosis theme) into one new page,
    `owner-dependency-diagnostic.md`. Framed explicitly as the *why is this business
    stuck* complement to `smb-ai-audit-method.md`'s *what to automate* — nearly every
    question in the source material is verbatim-usable in a real discovery interview,
    so the condensation kept the interview questions and diagnostic tests intact
    rather than summarizing them into prose.
  - Linked from `smb-ai-audit-method.md` (Related Pages) and `cash-flow-audit-method.md`
    (Survival Trap cross-reference, replacing the now-resolved `[[e-myth-revisited]]`
    link from Batch 4).
  - Updated `index.md`. Deleted all 17 source pages from FORGE once absorbed.
- **Batch 7 — Flawless Consulting cluster (22 source pages → 1 new page, 2 existing
  pages linked):** the richest single source in this migration.
  - Consolidated all 22 pages (the consultant/manager distinction and five-phase model,
    the nine-element contract, the eight-step contracting meeting + stuck-recovery
    sequence, the full resistance taxonomy and three-step naming method, the
    three-layer discovery interview, the ten-step timed feedback meeting agenda, the
    installation-vs-engagement implementation model, and the closing ethics/mindset
    chapters) into one new page, `consulting-methodology.md`. Framed as the
    engagement-mechanics layer underneath `fulfillment-system.md` and
    `smb-ai-audit-method.md` — not what to deliver, but how to run every client
    conversation that gets you there. Heavy condensation was required (22 source pages
    of very detailed material, including full worked case studies) down to the
    reusable scripts, checklists, and decision rules; case-study narrative detail was
    dropped per the intake protocol's "extract with a use test" rule.
  - Linked from `fulfillment-system.md` and `smb-ai-audit-method.md`.
  - Updated `index.md`. Deleted all 22 source pages from FORGE once absorbed.
- **Batch 8 — Barringer & Ireland entrepreneurship cluster (17 source pages → 1 new
  page, 2 existing pages linked):**
  - Consolidated all 17 pages (First Screen feasibility analysis, the Business Model
    Template, Porter's Five Forces, the business plan outline, legal entity choice,
    financing sources, IP basics, the managerial-capacity growth constraint, and
    internal/external growth strategy) into one new page, `venture-fundamentals.md`.
    Framed explicitly as reference for building **Chris's own company**, distinct from
    the client-facing audit/diagnostic pages — this cluster is general venture-building
    textbook content, not audit methodology, so it didn't distribute into the existing
    AI-integration-company pathway pages the way earlier clusters did.
  - Linked from `business-setup.md` (the underlying frameworks behind its tiered
    checklist) and referenced `financial-model.md` and `theory-of-constraints.md`.
  - Updated `index.md`. Deleted all 17 source pages from FORGE once absorbed.

## FORGE `wiki\business\` intake — COMPLETE

All 135 original pages processed across 8 batches (105 pages absorbed into 8 new
BUSINESS pages + numerous existing-page strengthenings; 30 pages redirected to the new
SYSTEMS hub as misfiled system-dynamics content). `FORGE\wiki\business\` now contains
only `desktop.ini` — confirmed empty. New pages created this session:
`theory-of-constraints.md`, `negotiation-toolkit.md`, `cash-flow-audit-method.md`,
`lean-methodology.md`, `owner-dependency-diagnostic.md`, `consulting-methodology.md`,
`venture-fundamentals.md` (7 new pages; the Checklist Manifesto batch added no new page,
distributing entirely into existing pages instead). BUSINESS wiki's
`wiki/ai-integration-company/` went from 44 pages to 52.

Next action for Task 1: FORGE's `wiki\technology\` (135 pages) still needs the
split-migration into PYTHON (~50 pages) and TECHNOLOGY (~85 pages) per the user's
"split by subject" decision — this is Task 4/5 in the migration tracker, a separate
body of work from the business/ intake this log has covered.

## 2026-07-10 — Three-track alignment + color-language cleanup (system-directed)
Post-split review execution touched four files here: `north-star-alignment.md`
(four-track order → three-track order per NORTH_STAR.md's July 10 ruling;
Heather/JV retirement annotated in place), `start-here.md` (link text
updated to three-track order), `CLAUDE.md` (retired phase color-ramp
parenthetical removed — tag filters are the progression view), `README.md`
(phase table's Color column removed; it contradicted the tag-filter doctrine
four lines above it). No content pages added or removed.

## 2026-07-14 — Unified-team terminology and high-load policy reconciled

- Updated `first-90-days.md` to name March 2027 as the first consulting-client
  target and replace the school-only danger-week rule with fixed-commitment
  protection plus Chris's final direction.
- Updated the capability-library first-run wording to match the consulting
  milestone. No offer, client, or business phase was opened.
- Next action: normal business cadence; continuity-income tests remain in
  REVENUE_LAB and consulting assets remain here.

## 2026-07-14 — Client-workspace privacy boundary reconciled

- Updated the Business hub OS, human guide, and index to match the approved
  privacy boundary: active client-specific/private work lives in a separate
  authorized client workspace or repository outside `.ROOT`.
- `.ROOT` keeps blank masters, sanitized lessons, reusable methods/assets,
  approved case studies, and non-sensitive metadata only.
- Next: before the First Contact phase opens, create no client workspace. When
  real client work begins, define that external boundary in the engagement's
  own instructions and agreement.

## 2026-07-14 — Business wiki separated from durable identity

- Replaced the copied North Star constitution with a routing bridge: NORTH_STAR owns
  durable direction, CURRENT_STRATEGY owns the active vehicle, this wiki owns methods
  and evidence, and CASTLE/NOW owns sequencing.
- Reconciled index/start pages, current wedges/first offer pointers, skill roadmap,
  and time-horizon pages so old June business-arc wording no longer overrides live
  strategy or school frontiers.
- Added the Watchtower boundary: external market change may route outward; our own
  field results return directly through CASTLE to a strategy assumption/milestone.
- Next: practice the observation method when real access exists; do not activate a
  sales checklist merely by opening a roadmap page.

## 2026-07-14 — User router and live-path audit

- Replaced the stale copied README architecture with a short router to the current
  strategy, HOW_TO, index, and North Star alignment bridge. Clarified that roadmap
  pages are scenarios until CASTLE activates a bounded test.
- Corrected the CASTLE decision-rule path in HOW_TO. Strict wiki lint reports no
  unresolved dead links.

## 2026-07-16 — Book and source intake routed from `77-INBOX`

- Added 19 unique raw sources covering enterprise AI adoption/use cases, product
  discovery and management, strategy, leadership, economics, and judgment.
- Highest-value intake queue for the active Advisor-Builder strategy: *The Mom
  Test* -> *The AI Dossier* -> *All-In on AI* -> *Good Strategy/Bad Strategy* ->
  *Inspired* / *Transformed*. The entrepreneur book list and Silver Space AI/ML
  PDF/PPTX package are low-priority discovery/marketing sources and may be parked.
- This is source placement only. No book is marked covered or ingested.

## 2026-07-16 — New BUSINESS book batch chunk-ingested and fully dispositioned

### What changed

- Processed all 19 July 16 source files. Thirteen useful sources were ingested
  through complete named PDF ranges into six reusable method pages; six sources
  were explicitly parked or excluded. Large books were never treated as one-pass
  summaries, and each new page carries its own chunk ledger.
- Created `customer-discovery-and-evidence.md` from *The Mom Test* and wired its
  behavior/commitment standard into the sales system and audit interview guide.
- Created `enterprise-ai-opportunity-and-adoption.md` from all six industry
  sections/86 use cases in *The AI Dossier* plus all seven chapters of *All-In on
  AI*. Enterprise examples were normalized into durable workflow patterns and an
  adoption-readiness diagnostic rather than copied as a catalog.
- Created `strategic-diagnosis-and-coherent-action.md` from all three parts of
  *Good Strategy/Bad Strategy*.
- Created `product-discovery-and-operating-model.md` from all five parts of
  *Inspired* and all eleven parts of *Transformed*, then extended it with bounded
  dispositions for *The Innovator's Dilemma* and the 854-page *Cracking the PM
  Career*. Career/job-search chapters were excluded from the company method.
- Created `ai-economics-and-decision-workflows.md` from *Prediction Machines*.
  The audit can now separate prediction from judgment, action, outcome, and
  feedback before recommending AI.
- Created `company-operating-system-and-founder-judgment.md` from *The Great CEO
  Within*, *The Hard Thing About Hard Things*, the business-relevant portions of
  *The 80/20 Principle*, and the complete *Psychology of Human Misjudgment*
  speech. The page is phase-3 reference, not permission to install bureaucracy.

### What was parked or excluded

- `book list.pdf`: source-discovery list with hype-heavy rankings; no independent
  evidence or operating method. Parked as a catalog only.
- `AI and ML Red.pdf` + `AI and ML text.pptx`: the same Silver Space marketing
  package in rendered/editable formats. It makes unsupported absolute-accuracy
  and near-total-autonomy claims that conflict with the wiki's gate discipline;
  parked, not promoted.
- `Matery byRobertGreene.pdf`: personal mastery/apprenticeship narrative; useful
  general reading but no current BUSINESS page gap. Parked.
- `SenecaLettersfromaStoic-SelectedLetters.pdf`: philosophy/personal resilience,
  not a business operating source. Excluded from wiki ingestion.
- `theundercovereconomist.pdf`: broad economics examples; no direct gap beyond
  the stronger AI economics, pricing, and market pages already present. Parked.

### Missing data needed from Chris

- None for source ingestion. Field evidence is still missing: real workflow
  conversations, observed process costs, advancement commitments, and a used
  audit artifact. Reading does not satisfy strategy assumptions S-01 through S-03.

### Recommended next action

- Use `customer-discovery-and-evidence.md` to prepare one warm-network workflow
  conversation. Capture the last concrete problem event, current workaround,
  quantified consequence, decision owner, and one advancement commitment; let
  the result update the active strategy through CASTLE.

## 2026-07-16 — First workflow observation converted into a field protocol

### What changed

- Added `first-workflow-observation-field-plan.md`, a field-ready protocol for
  selecting one bounded workflow, requesting access, conducting a 45-60 minute
  observation, labeling evidence, quantifying friction conservatively, writing
  a 2-4 page report, and securing one advancement commitment.
- Compared the three available access paths without storing candidate identities
  or private operational details. Recommended a local real-estate workflow as
  the first method rehearsal, a small Boston-area construction business as the
  first serious commercial-discovery test, and the harder-to-schedule medium
  construction company as later validation.
- Added explicit privacy boundaries, calculation rules, quality gates, stop
  conditions, and strategy evidence routing for S-01 through S-03.

### Missing evidence

- The actual workflow has not yet been selected or observed. Candidate scores
  are provisional until participant role, artifact access, recency, volume, and
  scheduling are confirmed.

### Recommended next action

- Ask the local real-estate participant to identify one recurring workflow with
  a safe, completed example from the last 30 days. Schedule a 45-60 minute live
  observation and use the new field plan without pitching a solution.

## 2026-07-16 — Workflow observation question sequence added

### What changed

- Added `templates/workflow-observation-question-sequence.md`, a fill-in live
  worksheet ordered by evidence value: recent event, observed workflow, repeated
  friction, magnitude, consequence, motivation, authority, disconfirmation, and
  advancement.
- Added explicit gates for when to narrow, measure, park, or reject a workflow,
  plus optional real-estate and construction question branches.
- Linked the worksheet from the template library and first-observation field plan.

### Recommended next action

- Complete the short pre-session test block, then use Steps 1-11 during the local
  real-estate observation. Do not read every optional branch unless the observed
  workflow makes it relevant.

## 2026-07-16 — AGC construction outlook routed through Watchtower

### What changed

- Preserved the official five-page AGC 2026 Construction Hiring and Business
  Outlook remarks in `raw/` and reviewed the complete source, including rendered
  verification of the workforce and AI-adoption pages.
- Updated `enterprise-ai-opportunity-and-adoption.md` with current construction
  evidence: 61% of respondents use AI or plan more investment, with reported use
  concentrated in office/admin, estimating, preconstruction/design, and HR.
- Converted the source into a bounded field-test question for the already-planned
  construction observation. It does not prove willingness to pay or authorize a
  new offer, tool, outreach campaign, or project.
- Routed the material external change to `...projectSuccess/radar.md` as WATCHING;
  the source and analysis remain in this owning evidence home.

### Recommended next action

- During the first approved construction observation, test one actual office/admin,
  estimating, or preconstruction workflow and record whether AI use created value,
  integration friction, new review work, or no meaningful change.

## 2026-07-16 — Real-estate ecosystem entry ideas ranked

### What changed

- Researched the operating boundaries around a Mark Spain-affiliated agent,
  independent brokers, Georgia closing attorneys, and residential flippers.
- Updated `market-map.md` with a four-candidate entry ranking. Rejected generic
  agent CRM and broker-compliance software as first builds because brokerage
  control and established transaction platforms make them poor individual-agent
  wedges.
- Passed a **Flip Margin Leak Audit + Cost-to-Complete Cockpit** into a bounded
  Phase 2 test: one completed flip, one margin-variance analysis, and one Sheet;
  no platform or automation unless the investor asks to repeat it on a live deal.
- Held the broader **Closing Exception Autopsy / Deal Friction Radar** until one
  safe, redacted delayed transaction proves repeated missing-item chasing,
  measurable consequence, and a reachable process/budget owner.
- Preserved Mark Spain, NAR, ATTOM, Georgia regulatory, and Clio source roles in
  the CASTLE source map before allowing the research to affect the opportunity
  queue.

### Recommended next action

- With Chris's explicit approval, Heather asks one residential flip investor for
  a 60-minute replay of a completed project. Ask for the original underwriting
  and actual cost categories, not live credentials or documents for `.ROOT`.

## 2026-07-16 — Creative problem-solving handbook routed from `77-INBOX`

- Moved and clearly named James M. Higgins's 1994 *101 Creative Problem Solving
  Techniques: The Handbook of New Ideas for Business* in this hub's immutable
  `raw/`.
- Visually verified the title, copyright page, contents, and source purpose. It is
  a facilitation toolbox spanning problem recognition, assumption testing,
  individual and group ideation, alternative selection, implementation, and
  control.
- Source placement only. Reopen selectively when a real audit workshop,
  facilitation session, or stuck problem needs additional techniques; do not
  chunk-ingest 101 methods merely because the catalog exists.

## 2026-07-16 — Creative problem-solving handbook selectively chunk-ingested

### What changed

- Reconciled the 68-file `raw/` inventory against prior intake records. The AGC
  outlook and the 19-source July book batch were already covered; Higgins's
  *101 Creative Problem Solving Techniques* was the only outstanding source.
- Reviewed and dispositioned all 241 physical PDF pages in 11 named chunks,
  including visual checks at the major method boundaries.
- Added `creative-problem-solving-and-facilitation-toolkit.md`: an evidence-gated
  eight-step problem-solving loop, compact technique chooser, bounded workshop
  protocol, human-agent boundary, and complete source ledger.
- Linked the method into consulting, the SMB AI audit, strategic diagnosis,
  product discovery, and the Business operating index.

### What was parked

- The 101 exercise instructions, repeated historical company anecdotes, and
  technique-by-technique catalog remain immutable in `raw/` for triggered
  retrieval. They were not reproduced as wiki pages.
- The book's 1994 cases do not count as current market evidence or proof that a
  technique works in a present client setting.

### Missing data needed from Chris

- None for source intake. The method has not yet been used in a real workshop;
  effectiveness and fit remain unproven until a named, observed problem actually
  requires facilitated option generation or selection.

### Recommended next action

- Keep the toolkit dormant until an audit or workflow observation reaches a
  specific stuck decision. Then use the smallest applicable technique and ship
  a decision record plus a bounded test, not a brainstorming transcript.
