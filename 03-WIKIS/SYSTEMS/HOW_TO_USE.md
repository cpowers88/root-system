---
type: guide
tags: [reference, systems]
---

# HOW TO USE — 03-WIKIS\SYSTEMS
### This wiki answers: *what system-dynamics or ISYE concept is worth knowing, and what audit or coursework does it strengthen?*

## Question Owned
System dynamics, factory physics, queuing theory, MRP/inventory theory, and the ISYE 2600 spine — feedback structures, stock-and-flow models, bottleneck/variability analysis, and their audit applications.

## Start Here
`wiki/index.md` for the full page list. Every page carries FORGE-era frontmatter — search by `subject/...` tag (e.g. `subject/queuing-theory`, `subject/factory-physics`) or `use-case/audit` for pages with direct client-diagnosis application. Every page's `Ranking` table's `Overall priority` line (NOW / NEXT / LATER / PARKED) says what to read next.

## Standard Work Loop
```text
concept -> diagnostic question/model -> course/audit application -> evidence
```
Every page has a `North Star Connection` section tying the concept to the audit business — the loop closes only when a concept gets used on real ISYE coursework or a real (or practice) audit, not when the page is merely read.

## What Counts as Proof
A concept is proven when it correctly diagnoses or models a real situation — an ISYE problem set answer, a practice audit finding, or a client-diagnosis pattern actually applied. Reading the page is not proof.

## Outputs and Where They Go
Study application stays in-vault (notes on how a concept applied). If a pattern becomes a repeatable audit diagnostic, it gets logged as a capability-library candidate (`05-BUSINESS\06-Capability Library`) or flagged to the castle's `field-observation` skill page — not duplicated as a new SYSTEMS page.

## Boundaries
Distinct from `03-WIKIS\BUSINESS` (offer layer, audit method, client-facing pathways) and `03-WIKIS\TECHNOLOGY` (tool/landscape research) — SYSTEMS feeds both but owns neither. No orphan knowledge: every concept studied connects to ISYE 2600 prep or a named audit use case.

## How the Hub Learns From Use
New ISYE coursework or system-dynamics sources follow the existing pages' shape (Summary/Sources/Last updated, Key Ideas, Connects to, North Star Connection, Ranking, Use/Retrieval Notes) so the wiki stays one consistent format as it grows past its FORGE-inherited base.

## Close
After a session: log which pages were used and how in `wiki/log.md`; update a page's `Ranking`/priority line only if its timing genuinely changed; update `wiki/index.md` only if a page was added.

## Current State
98 pages of system-dynamics, factory-physics, and operations-research reference live in `wiki/` (verified count, 2026-07-13). Base: 76 pages moved intact from FORGE's `wiki/systems/` folder on July 7, 2026, plus process-mining/VSM/BPMN/APQC direct intake (July 8–9). Added 2026-07-13: a genuine gap was found and closed — Hillier & Lieberman's *Introduction to Operations Research* had been listed as an already-covered source but its actual content had zero overlap with the existing pages. **The full 29-chapter book is now ingested** (24 new pages across four chunks this session), with deliberate, reasoned skips for content already covered elsewhere (most of Ch. 18 Inventory Theory — EOQ/newsvendor/Q,r already in Factory Physics/Supply Chain Science coverage), pure prerequisite review (Ch. 24 Probability Theory), and repeated worked-example chapters (most of Ch. 20 and all of Ch. 28's spreadsheet-simulation walkthroughs, Ch. 9.2's transportation-simplex tableau arithmetic, Ch. 26's example sections). See `wiki/log.md`'s 2026-07-13 entries for the full chunk-by-chunk coverage record. No ISYE 2600 coursework has activated yet (gate course is Spring 2027) — the wiki is reference-ready, not yet in active use.

## Last Updated
July 13, 2026 — local-root cutover: canonical workspace is `C:\Users\chris\.ROOT`; G: is backup only. Color language: `C:\Users\chris\.ROOT\START_HERE.md`.
