---
type: reference
tags: [school]
timeline: reference
---

# AI Programs in U.S. Universities — CIC Map & 2026 Status Report

**Sources — provenance corrected 2026-07-24; neither is in this hub's `raw/` any longer:**
- `AI Programs in U.S. Universities.md` — web clipping of [cicmap.ai](https://cicmap.ai/) (Center for Inclusive Computing, Northeastern Univ.), captured July 8, 2026; site data as of June 15, 2026. **No longer present anywhere in `.ROOT`.** The claims below were extracted while it was available and are not re-verifiable against a local copy; treat them as dated to the July 8 capture. Re-clip from the live site before relying on any figure.
- `2606.12428v1.pdf` — Muzny et al., *"Mapping AI Programs in the U.S.: A Status Report from Early 2026 and an Analysis of AI Majors and Minors"* (arXiv:2606.12428, May 2026); analysis snapshot April 2026. **Now located at `03-WIKIS\BUSINESS\raw\2606.12428v1.pdf`**, not here.

**What it is:** The most comprehensive survey to date of undergraduate technical AI programs (majors, minors, concentrations, certificates) in U.S. computer science departments. Scraped from 4-year institutions producing 86% of U.S. CS graduates, displayed on a live interactive map that refreshes roughly once a semester.

---

## The landscape (site data, June 2026)

- **584 universities** mapped, 51 states, **1,039 programs** total
- **78 AI majors** · **103 AI minors** · **130 concentrations/specializations** · **95 other tracks (certificates)** · 633 schools with no AI-specific program
- Growth is fast: the paper counted 62 majors in Jan 2026 → 73 in April → 78 by June
- ~44% of scraped schools had at least one AI program (April figure); over half still have none, though many teach AI via electives
- **Concentrations are the most common program type (~33%)** — they slot into existing degree structures and skip the 1–2 year governance process a new degree requires
- Scope limit: only programs housed in CS departments/schools; data science and business-school AI programs excluded (for now)

## What AI majors require (66 majors analyzed, April 2026)

- Huge variability: major requirements span 30%–89% of the ~120 credits to graduate (mean 65.5 credits, 54.6%)
- Required AI credits: mean 18.1 (min 3, max 42) — ~26% of the major
- **92% require a general AI course; those that don't require ML instead**
- Most-required courses: General AI (92%), ML (77%), then Deep Learning, Responsible/Ethical AI, and NLP (each just over a third)
- **37.9% of majors require an AI ethics course**
- Most common 3-course core: {Ethical AI, General AI, ML} — 31.8% of majors
- Trade-off noted: majors heavy on *required* AI credits produce consistent backgrounds; elective-heavy majors allow specialization

## What AI minors require (87 minors analyzed)

- More standardized than majors: mean 19.1 credits (~16% of degree)
- Required AI courses average 6.4 credits (~35% of the minor)
- General AI is the most-required course (78.2%); only **24.1% require AI ethics** (vs 37.9% of majors)
- Most minors name very few specific courses — 59 of 87 specify only one; none require both General AI *and* ML
- Caution from the paper: minors often have implicit prerequisites not stated in requirements, making them harder to finish than they look

## Context worth keeping

- ACM CS2023 guidelines allocate 12 of 270 core hours (4.4%) to AI — up from **zero** in the 2013 guidelines
- CS2023 core-recommended AI knowledge units: fundamental issues, search, knowledge representation & reasoning, ML, applications & societal impact
- Multiple states (NJ, MS, GA) are legislating AI/CS into K-12 graduation requirements starting ~2029–2032
- Stanford's 2025 AI Index found only 19 U.S. AI bachelor's programs as of 2023 (104 graduates) — the field roughly quadrupled in ~3 years
- Course-combination data: https://github.com/muzny/cicmap-april2026-snapshot-paper

## Stanford AI Index 2026 — Education Chapter Data (added July 9, 2026)

From the AI Index 2026 (Ch. 7; source PDF in `03-WIKIS\TECHNOLOGY\raw\`,
distillation in `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\adoption-delivery\ai-index-2026.md`) —
national context for the program landscape above:

- **CS undergraduate enrollment fell 11%** at US four-year universities
  between 2024 and 2025 — students responding to the entry-level software
  job squeeze (the Index's Economy chapter: employment for developers aged
  22–25 down ~20% from 2024).
- **AI-related specialization keeps growing anyway:** AI-software master's
  graduates +17% (2023→2024), +82% since 2022. The demand moved up-stack,
  not away.
- New AI PhDs +22% (2022–2024), but the growth went to **academia**, not
  industry — reversing a decade-long flow.
- **4 in 5 US high-school and college students use AI for schoolwork**;
  only half of schools have AI policies and just 6% of teachers call them
  clear (the syllabus-level policy chaos on
  [[course-briefs/fall-2026-course-briefs]] is the national norm, not a KSU quirk).
- The Index's useful distinction: **AI in education** (using AI to
  teach/learn) ≠ **AI literacy** (understanding it) ≠ **AI education**
  (technical skills to build it).
- Reading for Chris's path: enrollment cooling in generalist CS while
  AI-specialized credentials grow supports the systems-engineering +
  self-taught-AI-core route — the {General AI, ML, Ethical AI} spine below
  matters more, not less, as generic CS thins out.

## Relevance to Chris / KSU

- **KSU checked on the map (July 8, 2026): no AI-specific program — only a BS with a Major in Computer Science.** That puts KSU in the majority bucket (633 of 1,039 mapped entries are "no AI specific program"), alongside over half of U.S. institutions.
- Implication: any AI credential at KSU would come through electives or a future concentration — concentrations are the fastest program type for schools to launch (no new-degree approval), so this is the most likely thing to appear first. Worth re-checking the map each semester when CIC re-scrapes.
- Since no credentialed AI path exists at KSU, the {General AI, ML, Ethical AI} triad — the de facto national core required by most AI majors — is the self-study spine that substitutes for it.
- If an AI minor/concentration ever appears: the typical shape is ~19 credits, one required general-AI course, plus watch for hidden prerequisites.
