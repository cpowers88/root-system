---
type: ops
register: ai-directive
timeline: now
status: ready
tags: [ai-automation, technology, systems, castle, governance]
created: 2026-07-24
---

# INGEST PROTOCOL — 2026-07-24 Vault-Redesign Source Review
### First real use of `register: ai-directive` (proposed in `vault-skeleton-design.md` §7.1). Six-part structure per §7.2. Sandwich technique per §7.5 — the one-line mandate below is restated at the end, unchanged.

**Mandate: read these 8 sources for what they say about implementing `vault-skeleton-design.md` — not for general domain knowledge.** Everything below exists to make that one read precise and repeatable across sessions/models.

---

## Role

You are the wiki-ingest agent for `03-WIKIS\AI_AUTOMATION_SYSTEMS` and `03-WIKIS\TECHNOLOGY`, running a Chris-directed special-lens pass. You are not executing either hub's default generic-research charter this pass.

## Context

- 8 books landed in `77-INBOX` 2026-07-24, identified, deduped (1 confirmed duplicate archived), and placed:
  - `AI_AUTOMATION_SYSTEMS\raw\`: `AI_engineering.pdf` (Huyen), `AI_builders_handbook.pdf` (LevelUp Labs), `Prompt_engineering_LLMs.pdf` (Berryman & Ziegler), `promp_engineering_generative_AI_guide.pdf` (Phoenix & Taylor), `Generative_AI_economic_potential.pdf` (McKinsey), `agentic_AI_for_engineers.pdf` (Nagasubramanian)
  - `TECHNOLOGY\raw\`: `Machine_learning_design.pdf` (Lakshmanan et al.), `r_for_data_science.pdf` (Wickham & Grolemund)
- Governing design doc: `C:\Users\chris\.ROOT\vault-skeleton-design.md` — §1-6 (functional roles, classification rule, `path_reference_audit.py` spec, skeleton tree), §7 (AI/human instruction register, added same day, partially sourced from 4 of these 8 books already).
- Reference-only: `C:\Users\chris\.ROOT\Untitled.md` — Codex's own competing migration plan, independently locks "Watchtower remains separate from CASTLE." Read for corroboration/conflict, not as a second design authority.
- Open question §5 of `vault-skeleton-design.md`: Watchtower merge-into-CASTLE vs. stay-separate. Leaning stay-separate (both this doc's own recommendation and Codex's independent lock). Not yet Chris-decided.
- Each hub's own `CLAUDE.md` plus `AGENT.md § Wiki Shared Layer` (restored today, flag #83) already govern generic ingest mechanics — raw immutability, 10-15pp/one-chapter chunking, session start/close minimums, update-over-create, contradiction flagging, recency markers, lint. Inherited in full. Not restated here.

## Task

For each of the 8 books, read against exactly four lenses — skip content that serves none of them:

1. **Functional-role validation.** Does this source support, complicate, or contradict the 10-role taxonomy or classification rule (`vault-skeleton-design.md` §2-3)?
2. **Move-integrity tooling.** Any pattern relevant to `path_reference_audit.py` (§4) — versioning, reference tracking, drift detection, anchor/heading integrity (the exact class of bug flag #83 was today).
3. **AI/human instruction register (§7).** `AI_builders_handbook.pdf` and `Prompt_engineering_LLMs.pdf` are already mined (see §7.2-7.6). Do a first real pass on `AI_engineering.pdf`'s prompt-engineering and context-construction chapters and `promp_engineering_generative_AI_guide.pdf` beyond the preface; a fresh pass on the 4 not yet touched at all.
4. **Watchtower-vs-CASTLE architecture evidence.** `agentic_AI_for_engineers.pdf` is the most likely direct hit (goal-driven system architecture — does separating sensing from deciding hold up as a design pattern, or does this source argue against it?). Check `AI_engineering.pdf`'s agent chapters too. Report evidence either direction; do not force a match.

Deliverable per book: 3-8 bullets, each tagged to lens 1-4, with chapter/section attribution. A book that hits nothing on any lens gets one line saying so — do not pad.

## Constraints

- Wiki Shared Layer rules apply in full and are not waived by this lens.
- No book is marked fully ingested by this pass. The full domain-knowledge ingest for all 8 remains queued (see each hub's `log.md`, 2026-07-24 entries) and is separate, later work.
- Do not edit `NORTH_STAR.md`, `AGENT.md` structure, or `WHERE_IT_GOES.md` from this pass. Findings land only in `vault-skeleton-design.md` (new `## 8`) and each hub's `log.md`.
- Do not resolve the Watchtower question. Report evidence only — Chris decides, informed by this pass and Codex's `Untitled.md`.

## Examples

Calibration for right-sized output (from today's earlier pass on 4 of these books):

> **AI Builder's Handbook §5.1** "Six Parts of a Working Prompt" (p.38-39): Role, Context, Task, Constraints, Examples, Output Format, fixed order — "Order matters. Models weight the earliest and latest sections of a prompt most heavily." [Lens 3]

That is the target density: one concrete claim, one attribution, one tag. Not a chapter summary.

## Output Format

- `vault-skeleton-design.md` gets one new `## 8. Redesign-Relevant Findings from the 2026-07-24 Book Batch` section, findings grouped by lens 1-4, each bulleted with book + chapter/section.
- Each hub's `log.md` gets one dated entry naming the exact page/chapter ranges actually read this pass (chunking-rule compliance, not a blanket "reviewed").
- Close with one paragraph: what the evidence says about Watchtower-vs-CASTLE, explicitly marked evidence-only, no verdict.

---

**Mandate, restated: read these 8 sources for what they say about implementing `vault-skeleton-design.md` — not for general domain knowledge.**
