# EXECUTION BRIEF — Business Wiki `raw-source-map.md`

**For:** Claude Code (file executor lane)
**Authored by:** Claude Chat (operator) — approved scope, reduced from Codex's original "Business Learning and Evidence Engine" plan.
**Date:** 2026-07-23

---

## 1. What you are building

Create ONE new file:

```
C:\Users\chris\.ROOT\03-WIKIS\BUSINESS\wiki\ai-integration-company\raw-source-map.md
```

Its job: give the 70-file `03-WIKIS\BUSINESS\raw\` corpus a durable classification/source map, define a reusable evidence-row schema, and name a curated reading sequence. It is a **source-accounting page**, not a curriculum and not a command center.

## 2. Hard guardrails (do NOT do these)

This scope was deliberately trimmed. Do not reintroduce the cut pieces:

1. **No business-fundamentals curriculum / "education lane."** This hub is an application-decision engine (`HOW_TO_USE.md`: it "does not teach skills"; "re-reading plans is not progress"). Fundamentals education routes to the education system, not here.
2. **No new industry/business ranking model.** Ranking already lives in `most-profitable-pathways.md` (9-dimension matrix) and `market-map.md`. Do not build a competing model. If a gap exists, note it as a one-line pointer to update those pages — do not duplicate them here.
3. **Do not touch `raw/`.** Raw files are immutable. Read only. Classify, never move/rename/edit.
4. **Do not modify or replace** `CURRENT_STRATEGY.md`, `index.md`, `NORTH_STAR.md`, or any governance file. The Advisor-Builder vehicle stays the active hypothesis.
5. **Do not create additional files.** One file only. If you believe another is needed, stop and report instead.

## 3. Steps

1. `ls` `03-WIKIS\BUSINESS\raw\` and confirm the full file list (~70 files: PDFs, .md, .xlsx, .pptx).
2. For each source, classify it (schema in §4). For PDFs/large books you don't need to read fully — infer type/authority/date from title, opening pages, or the existing `book list.pdf`. Mark confidence where uncertain.
3. Write `raw-source-map.md` using the skeleton in §5.
4. Add one link line into `index.md` under section 5 (Capability Building) pointing to the new page — this is the ONLY edit to an existing file, and it is additive. If unsure, leave it out and report.
5. Report a short summary: count per category, any files you couldn't classify.

## 4. Classification schema (one row per source)

Columns for the source-classification table:

| Field | Notes |
|---|---|
| Source (filename) | exact name |
| Type | book / report / dataset / API-doc / article / challenge-source / reference |
| Category | one of: business-fundamentals, economy/industry-data, entrepreneurship/models, strategy/decision, marketing/sales, finance/cash-flow, operations/implementation, construction/real-estate, AI/technology-adoption, data/API/reference, challenge-source, duplicate/weak/outdated/park |
| Authority | primary-data / official / expert-book / vendor / opinion |
| Pub date | year (approx OK) |
| Industries covered | or "general" |
| Company size relevance | SMB / mid / enterprise / any |
| Concepts covered | 3–6 keywords |
| Evidence value | high / med / low |
| Implementation value | high / med / low |
| Wiki destination | which existing page(s) this feeds |
| Processing | read-fully / read-selectively / lookup-only / park |
| Reopen trigger | the specific question that would justify reopening it |

## 5. File skeleton (fill this exact structure)

```markdown
---
tags: [business, reference, source-map]
stage: phase-all
timeline: reference
---

# Raw Source Map — Business Wiki

> Classification and source-accounting for `03-WIKIS\BUSINESS\raw\`. What each source is, what it proves, where it feeds, and whether it's worth reopening. Raw files are immutable; this page is how we navigate them without re-reading everything.

## Purpose
[2–3 sentences: prevent "more books" from becoming the goal; sources earn deeper processing only by answering a named question.]

## How to Use
[Look up a source before reading it; check Processing + Reopen trigger; new raw files get a row here before extraction.]

## Source Classification Table
[The full ~70-row table using the §4 schema.]

## Evidence-Row Schema (reusable)
[The standard evidence-capture format for future Business/Technology/AIAS research. Fields:
Source | Date/geography | Industry/subsector | Company size | Business problem | Workflow location |
Current method | Technology layer | Adoption evidence | Implementation sequence | Measured outcome |
Barrier/failure mode | Evidence strength | Wiki destination | North-Star relevance | Next question.
Present as a Markdown table header that is CSV-compatible so it can later be analyzed in Python. Do NOT populate it with data yet — it is a blank master.]

## Curated Reading Sequence
[Grouped, from existing raw material. Each entry = filename + the ONE question it should answer.
- Business foundation: theE-MythRevisited, GoodStraatedgyBadStrategy, Entrepreneurship, TheGreatCEOWithin, theChecklisManifesto
- Operation/implementation: thePhoenixProject, profitFirst, MeasureWhatMatters, StrategicModelingandBusinessDynamics, NewCodeofEstimating, Estimatingforesidentailconstruction
- Customer/market/decision: theMomTest, PredictionMachines, MKTG13-Principlesofmarketing, StorytellingwithData, BTOS + Census datasets
- Technology/AI implementation: AllInOnAI, state-of-ai-2026, The AI Dossier, AI and ML Red, Data in Construction, Procore Tool Training, api-overview
State clearly: this is a starting sequence, not a permanent curriculum.]

## Weekly Review Hook
[Short: on the Sunday review, note which sources were used, which proved noise, and what gap (if any) justifies new intake. One paragraph — not a governance process.]

## Related Pages
- [[index|Wiki Index]]
- [[most-profitable-pathways|Most Profitable Pathways]] — ranking lives here, not in this file
- [[market-map|Market Map]] — industry attractiveness lives here
```

## 6. Acceptance criteria

The file is done when it:
- classifies every raw source with the §4 schema
- defines the evidence-row schema as a blank, CSV-compatible master (no fabricated data)
- names the curated reading sequence with a question per source
- preserves raw immutability (no raw files touched)
- creates no competing curriculum and no second ranking model
- does not alter `CURRENT_STRATEGY.md` or any governance file (index.md link line is the only additive edit)
- reads as a navigation/accounting page, not a command center
```