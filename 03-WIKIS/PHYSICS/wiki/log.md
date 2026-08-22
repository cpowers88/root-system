---
type: log
timeline: log
tags: [physics]
---

# Physics Education Log

Append-only session record.

## 2026-06-24 — Vault Initialized

### Objective
- Initialize physics education vault structure.

### Sources touched
- None yet.

### Files created/updated
- CLAUDE.md
- README.md
- FIRST_CLAUDE_PROMPT.md
- wiki core files
- templates

### Concepts/equations/problem types added
- None yet.

### Parked material
- None yet.

### Next action for Chris
- Add syllabus and textbook/chapter sources to `raw/`, then run `FIRST_CLAUDE_PROMPT.md` in Claude Code.

## 2026-06-25 — Source Intake and Stage 1 Packet

### Objective
- Run `FIRST_CLAUDE_PROMPT.md`: read syllabus and textbook, build the full learning path and core maps, and generate the first stage packet.

### Sources touched
- `raw/syllabus/syllabus.pdf` (PHYS 2211, KSU, Fall 2026, Dr. Behera)
- `raw/textbook/physic.pdf` (Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed.)

### Files created/updated
- `wiki/source-map.md`, `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/parking-lot.md`, `wiki/index.md`
- `wiki/concept-map.md`, `wiki/equation-map.md`, `wiki/calculus-map.md`, `wiki/problem-type-map.md`, `wiki/units-and-dimensions.md`
- `wiki/stages/stage-1-physics-and-measurement.md`
- `wiki/concepts/si-base-units.md`, `particle-model.md`, `dimensional-analysis.md`, `unit-conversion.md`, `order-of-magnitude-estimation.md`, `significant-figures.md`
- `wiki/equations/density.md`
- `wiki/problem-types/dimensional-consistency-check.md`, `unit-conversion.md`, `order-of-magnitude-estimation.md`, `sig-fig-arithmetic.md`
- `wiki/glossary/si-unit.md`, `dimension.md`, `order-of-magnitude.md`, `significant-figure.md`, `density.md`
- `wiki/flashcards/stage-1-physics-and-measurement.md`
- `wiki/drills/dimensional-analysis-drill.md`, `unit-conversion-drill.md`, `order-of-magnitude-drill.md`, `sig-fig-drill.md`
- `wiki/common-errors/stage-1-physics-and-measurement.md`
- `wiki/worked-examples/unit-conversion-speeding-example.md`

### Concepts/equations/problem types added
- Concepts: SI base units, particle model, dimensional analysis, unit conversion, order-of-magnitude estimation, significant figures.
- Equations: density (ρ = m/V).
- Problem types: dimensional consistency check, unit conversion, order-of-magnitude estimation, sig-fig arithmetic.

### Parked material
- Ch 10–12 (rotation, angular momentum, static equilibrium) and Ch 14 (fluid mechanics) — not mentioned in the syllabus course description; likely out of scope for PHYS 2211 specifically. Needs instructor/calendar confirmation.
- Full course calendar beyond Ch 5 (Sep 16, 2026) — the syllabus PDF's posted schedule table cuts off there.

### Next action for Chris
- ~~Confirm with the instructor or the full D2L calendar whether Ch 6, Ch 10–12, and Ch 14 are part of this course's scope.~~ **RESOLVED 2026-06-25.**
- Work through Stage 1: read the six concept pages, drill unit conversion and dimensional analysis until automatic, then check off the mastery checklist in `wiki/stages/stage-1-physics-and-measurement.md` before requesting the Stage 2 (Motion in One Dimension) packet.

## 2026-06-25 — Scope Confirmation: Ch 6–12 and Ch 14

### Objective
- Confirm and integrate Chris's report that Ch 6–12 and Ch 14 are all in scope for PHYS 2211.

### Sources touched
- `raw/textbook/Physics book-0101-0200.pdf` — sampled to confirm chapter locations
- `raw/textbook/Physics book-0201-0300.pdf`, `0301-0400.pdf`, `0401-0500.pdf`, `0501-0600.pdf` — first pages sampled to map chapter-to-file layout

### Files created/updated
- `wiki/source-map.md` — Ch 10, 11, 12, 14 moved from parked/uncertain to confirmed spine; textbook entry updated to reflect five split PDF files with textbook page ranges
- `wiki/learning-path.md` — Stage sequence expanded from 14 to 18 stages; Stage 10 (Ch 10), Stage 11 (Ch 11), Stage 12 (Ch 12), Stage 14 (Ch 14) added; Stages 13–18 renumbered
- `wiki/current-position.md` — confirmation note removed; full 18-stage scope noted
- `wiki/parking-lot.md` — Ch 10, 11, 12, 14, and Ch 6 calendar entry removed; only remaining parked item is full D2L lecture/exam calendar

### Concepts/equations/problem types added
- None (scope update only).

### Parked material
- Full D2L lecture/exam calendar for Ch 6+ — still needed to align stage dates to the syllabus schedule.

### Next action for Chris
- Share the full D2L course calendar (exam dates, Ch 6+ lecture dates) when available so stages can be aligned to deadlines.
- Continue working through Stage 1 — still the active unit. Do not move to Stage 2 until the mastery checklist in `wiki/stages/stage-1-physics-and-measurement.md` is complete.

## 2026-06-25 — Appendix Section Built

### Objective
- Extract all vital reference material from Serway & Jewett appendix PDFs and build a permanent wiki appendix section usable across all 18 stages.

### Sources touched
- `raw/textbook/Physics book-1201-1300-part-2.pdf` — Appendix A (Tables A.1–A.2) and Appendix B pp. A-4 to A-12
- `raw/textbook/Physics book-1301-1370.pdf` — Appendix B pp. A-13 to A-21, Appendix C (Periodic Table), Appendix D (SI Units)

### Files created/updated
- `wiki/appendix/index.md` — navigation page with quick-reference by stage
- `wiki/appendix/si-units.md` — 7 SI base units, all derived SI units (Table D.1, D.2), full SI prefix table
- `wiki/appendix/conversion-factors.md` — Table A.1: length, mass, time, speed, force, energy, pressure, angle
- `wiki/appendix/quantity-table.md` — Table A.2: all PHYS 2211 physical quantities with symbol, dimensions, SI unit; mechanics quantities organized by stage group
- `wiki/appendix/math-algebra.md` — B.1 scientific notation; B.2 algebra (fraction rules, Table B.1 exponents, factoring, quadratic formula, linear equations, simultaneous equations, logarithms)
- `wiki/appendix/math-geometry-trig.md` — B.3 geometry (areas, volumes, curve equations, radian measure); B.4 trigonometry (definitions, common angle table, Table B.3 identities, law of cosines/sines, vector decomposition diagram)
- `wiki/appendix/math-calculus.md` — B.5 series expansions and small-angle approximations; B.6 differential calculus (Table B.4 derivatives, chain/product/quotient/sum rules); B.7 integral calculus (Table B.5 indefinite integrals, Table B.6 definite integrals, integration by parts); calculus-physics quick reference table
- `wiki/appendix/uncertainty.md` — B.8 propagation of uncertainty (three rules: multiply/divide → percent, add/subtract → absolute, powers → multiply percent by exponent)
- `wiki/source-map.md` — two appendix PDF entries added
- `wiki/index.md` — appendix section added to top of index

### Concepts/equations/problem types added
- All core math tools from Appendix B fully documented
- All conversion factors from Table A.1 reproduced
- All PHYS 2211 physical quantities catalogued with symbols and units

### Parked material
- Appendix C (Periodic Table): not reproduced — minimal relevance for mechanics
- Table B.6 (Gauss's probability integrals): included in math-calculus.md but marked as beyond Stage 17 scope

### Next action for Chris
- The appendix section is now complete. Use `wiki/appendix/index.md` as a quick-reference during all problem-solving work.
- Continue working through Stage 1 — still the active unit.
- Share the full D2L course calendar (exam dates, Ch 6+ lecture dates) when available.

## 2026-06-25 — Full Vault Pre-Build (Cruise Preparation)

### Objective
- Build all 18 stage packets in full before a 10-day cruise with no internet access. Scope restriction bypassed per Chris's explicit request.

### Sources touched
- Appendix PDFs (already processed in previous session)
- Textbook knowledge (Serway & Jewett 10th ed., Ch 1–17 and Ch 38) used to author all stage content

### Files created/updated (this session)

**Stage packets (stage overview files):**
- `wiki/stages/stage-5-laws-of-motion.md` ✅ (built directly)
- `wiki/stages/stage-2-motion-in-one-dimension.md` ✅ (built by fork, previous session)
- `wiki/stages/stage-3-vectors.md` ✅ (built by fork)
- `wiki/stages/stage-4-motion-in-two-dimensions.md` ✅ (built by fork)
- `wiki/stages/stage-6-circular-motion.md` ✅ (built by fork)
- `wiki/stages/stage-8-conservation-of-energy.md` ✅ (built by fork)
- `wiki/stages/stage-9-linear-momentum.md` ✅ (built by fork)
- `wiki/stages/stage-10-rotation.md` ✅ (built by fork)
- `wiki/stages/stage-11-angular-momentum.md` ✅ (built by fork)
- `wiki/stages/stage-14-fluid-mechanics.md` ✅ (built by fork)
- `wiki/stages/stage-16-wave-motion.md` ✅ (built by fork)
- Stages 7, 12, 13, 15, 17, 18 — built by background forks (in progress as of this log entry)

**Stage 5 supporting files (all new):**
- `wiki/flashcards/stage-5-laws-of-motion.md`
- `wiki/common-errors/stage-5-laws-of-motion.md`
- `wiki/drills/fbd-drawing-drill.md`, `newtons-second-law-drill.md`, `friction-problems-drill.md`, `inclined-plane-drill.md`
- `wiki/equations/newtons-second-law.md`, `weight.md`, `kinetic-friction.md`, `static-friction.md`
- `wiki/concepts/force.md`, `newtons-first-law.md`, `newtons-second-law.md`, `newtons-third-law.md`, `mass-vs-weight.md`, `normal-force.md`, `friction.md`, `free-body-diagram.md`
- `wiki/problem-types/fbd-single-object.md`, `fbd-connected-objects.md`, `inclined-plane.md`, `atwood-machine.md`, `friction-problems.md`
- `wiki/worked-examples/fbd-block-on-table.md`, `inclined-plane-with-friction.md`, `atwood-machine-worked.md`
- `wiki/glossary/force.md`, `inertia.md`, `net-force.md`, `weight.md`, `normal-force.md`, `friction.md`, `tension.md`, `free-body-diagram.md`

**Appendix section (previous session, fully complete):**
- `wiki/appendix/index.md`, `si-units.md`, `conversion-factors.md`, `quantity-table.md`, `math-algebra.md`, `math-geometry-trig.md`, `math-calculus.md`, `uncertainty.md`

**Map files corrected (previous session):**
- `wiki/concept-map.md` — full 18-stage dependency chain added
- `wiki/calculus-map.md` — all 18 stages mapped
- `wiki/equation-map.md` — updated to 18-stage listing
- `wiki/learning-path.md` — stale note removed

### Concepts/equations/problem types added

**Stage 5:**
- Concepts: force, inertia, Newton's 1st/2nd/3rd laws, mass vs. weight, normal force, friction (static and kinetic), free body diagram
- Equations: F = ma, w = mg, f_k = μ_k n, f_s ≤ μ_s n
- Problem types: FBD single object, FBD connected objects, inclined plane, Atwood machine, friction problems

### Parked material
- None new this session.

### Next action for Chris
- All 18 stage packets are being built for offline cruise use. When complete, begin with Stage 1 and work forward through the sequence.
- Use `wiki/appendix/` as a reference for math, units, and conversions throughout all stages.
- When you return from the cruise, share the full D2L lecture/exam calendar so stage dates can be aligned to deadlines.

## 2026-07-07 — .ROOT System Alignment

### Objective
- Bring PHYSICS's instructional/navigation files into alignment with the July 7, 2026 wiki unification standard (matched against sibling hubs TECHNOLOGY, SYSTEMS, AI_AUTOMATION_SYSTEMS) and confirm North Star routing is current.

### Sources touched
- `00-BRAIN\AI_Agent.md`, `01-NORTH_STAR\NORTH_STAR.md`, `00-BRAIN\vault_map.md`, `00-BRAIN\WHERE_IT_GOES.md` — read for the current governance standard
- Sibling wikis' root structure and frontmatter conventions (TECHNOLOGY, SYSTEMS, BUSINESS, AI_AUTOMATION_SYSTEMS)

### Files created/updated
- Added Tag Standard frontmatter (`type:`/`tags:`) to `CLAUDE.md` and to 10 `wiki/` root files that lacked it: `index.md`, `log.md` (this file), `learning-path.md`, `source-map.md`, `concept-map.md`, `equation-map.md`, `calculus-map.md`, `problem-type-map.md`, `units-and-dimensions.md`, `parking-lot.md`, `current-position.md`

### Files archived (nothing deleted, per WHERE_IT_GOES.md)
- `CREATE_PHYSICS_STRUCTURE.ps1` → `99-ARCHIVE\ARCHIVED_2026-07-07_PHYSICS_CREATE_STRUCTURE_pre_ROOT_migration.ps1` — dead script, targeted the pre-migration `G:\My Drive\.PHYSICS_ED` path; skeleton is frozen so it can never run correctly again.
- `README.md` → `99-ARCHIVE\ARCHIVED_2026-07-07_PHYSICS_README_superseded_by_CLAUDE_and_index.md` — referenced a `FIRST_CLAUDE_PROMPT.md` bootstrap file that no longer exists; its job (orientation, key-file map, academic-integrity note) is now fully covered by `CLAUDE.md`'s Start-of-Session Protocol, `HOW_TO_USE.md`, and `wiki/index.md`. Matches the TECHNOLOGY/SYSTEMS root pattern (`raw/`, `wiki/`, `CLAUDE.md`, `HOW_TO_USE.md` — no root README).

### Concepts/equations/problem types added
- None — this was a governance/structure pass, not a content session.

### Verified, no change needed
- `vault_map.md` and `WHERE_IT_GOES.md` already list PHYSICS correctly under the 7-hub `03-WIKIS` structure (stages 1–18, Realm Check routing line intact).
- `CLAUDE.md` and `HOW_TO_USE.md` content already reflects the current course (PHYS 2211, Fall 2026, Aug 24 start) and North Star Track 1 priority — no factual drift found.

### Parked material
- Individual content pages (`wiki/concepts/`, `equations/`, etc.) carry `type:` frontmatter but are missing the `tags:` line the Tag Standard requires (timeline + topic tags). ~300 pages — out of scope for this pass; flag for a future dedicated cleanup session if Chris wants full Tag Standard compliance at the page level.

### Next action for Chris
- Nothing blocking. Resume the stage-packet build (see prior entry) or continue Stage 1 practice — the alignment pass did not touch stage content.

## 2026-07-07 — Stage 3 (Vectors) Data Review

### Objective
- Chris is currently working on Stage 3 (Vectors). Review the stage against the actual source textbook and process any missing or misfiled data before continuing.

### Sources touched
- `raw/textbook/Physics book-0001-0100.pdf` — extracted full text (pdftotext) and read Chapter 3 (Vectors) directly to verify section structure and content against `wiki/stages/stage-3-vectors.md`.

### Findings
1. **Missing content:** Section 3.1 "Coordinate Systems" (Cartesian vs. polar coordinates, conversion equations) was not covered anywhere in the Stage 3 packet, even though it's real, examinable Ch 3 content that comes before vector components in the textbook's own order.
2. **Wrong citation:** Stage 3's "Textbook Alignment" claimed "sections 3.1–3.6" — the chapter only has four sections (3.1–3.4). Corrected.
3. **Misplaced content:** The dot product was listed as a Stage 3 "Core Concept" and required mastery item. The textbook explicitly states (Preface, "Mathematical Level") that the dot product is not formally introduced until **Chapter 7** (Energy of a System) and the cross product not until **Chapter 11** (Angular Momentum) — this matches Stage 7's own packet, which already lists "dot product" as a prerequisite pulled forward from Stage 3. Reclassified dot product from required-now to Parked for Later (preview) in the stage packet, flashcards, and mastery checklist — the existing concept/equation pages were not deleted, just re-scoped, since the content is accurate and will be needed at Stage 7.
4. **Untracked raw source:** `raw/textbook/Physics book-0001-0100.pdf` exists in `raw/` and was already used to build Stages 1–3, but was never added to `wiki/source-map.md`'s Sources table. Added.
5. **Vault-wide gap (noted, not fixed beyond Stage 3):** `concept-map.md`, `equation-map.md`, and `problem-type-map.md` were never updated after Stages 2–18 were built in the cruise-prep session — they still only documented Stage 1. Added Stage 3 to all three; flagged Stages 2 and 4–18 in `parking-lot.md` for stage-by-stage backfill rather than one large batch session (matches "one stage's frontier at a time").

### Files created/updated
- **New:** `wiki/concepts/coordinate-systems.md`, `wiki/equations/polar-cartesian-conversion.md`, `wiki/problem-types/polar-cartesian-conversion.md`, `wiki/glossary/cartesian-coordinates.md`, `wiki/glossary/polar-coordinates.md`, `wiki/worked-examples/polar-coordinates-conversion-example.md`, `wiki/drills/polar-cartesian-conversion-drill.md`
- **Updated:** `wiki/stages/stage-3-vectors.md` (section citation fix, coordinate systems added, dot product reclassified), `wiki/flashcards/stage-3-vectors.md` (2 new cards, dot-product cards marked preview), `wiki/concept-map.md`, `wiki/equation-map.md`, `wiki/problem-type-map.md` (Stage 3 rows added + gap flagged), `wiki/current-position.md` and `wiki/index.md` (active stage corrected from Stage 1 to Stage 3), `wiki/source-map.md` (missing raw file logged), `wiki/parking-lot.md` (map-backfill item added)

### Concepts/equations/problem types added
- Concept: coordinate systems (Cartesian/polar). Equation: polar↔Cartesian conversion. Problem type: polar-Cartesian conversion. Glossary: Cartesian coordinates, polar coordinates.

### Parked material
- Stages 2, 4–18 backfill into the three master map files — see `parking-lot.md`.

### Next action for Chris
- Start Stage 3 with [[../concepts/coordinate-systems]] (the newly added piece) before vector components — that's the textbook's actual order. Ignore the dot product pages for now; they'll matter at Stage 7.

## 2026-07-07 — Stages 4–5 Data Review (Ahead-Check)

### Objective
- Chris asked to check the next couple of stages after Vectors so he isn't held up, and save the rest (Stages 6–18) for a later pass. Reviewed Stage 4 (Motion in Two Dimensions) and Stage 5 (The Laws of Motion) against the source textbook the same way Stage 3 was checked.

### Sources touched
- `raw/textbook/Physics book-0001-0100.pdf` and `Physics book-0101-0200.pdf` — extracted full text (pdftotext) and read Chapter 4 (all 6 sections) and Chapter 5 (all 8 sections) directly.

### Findings
1. **Stage 4 — real gap found:** Section 4.5 "Tangential and Radial Acceleration" (the non-uniform-circular-motion case: total acceleration = radial + tangential component when speed is also changing) was completely absent from the stage packet. Worse, both `wiki/concepts/uniform-circular-motion.md` and `wiki/equations/centripetal-acceleration.md` explicitly told Chris this topic "becomes important in Stage 10" — wrong. It's Chapter 4 material (right after uniform circular motion, Section 4.5), in scope for the Sep 4/9 lecture window. Stage 10 covers a different, later topic (rotational dynamics: torque, moment of inertia). Built out the missing piece and corrected both misdirecting notes.
2. **Stage 4 — citation fixed:** "Textbook Alignment" previously said only "approx. pp. 78–104" with no section list. Added the full 4.1–4.6 section breakdown for clarity.
3. **Stage 5 — verified clean:** Checked all 8 sections (5.1 Concept of Force through 5.8 Forces of Friction) against the existing concept pages (force, Newton's 1st/2nd/3rd laws, mass-vs-weight, normal-force, friction, free-body-diagram). Full coverage, citation ("sections 5.1–5.8") already correct. No changes made.

### Files created/updated
- **New:** `wiki/concepts/tangential-and-radial-acceleration.md`, `wiki/equations/tangential-and-radial-acceleration.md`, `wiki/problem-types/nonuniform-circular-motion.md`, `wiki/drills/tangential-radial-acceleration-drill.md`
- **Updated:** `wiki/stages/stage-4-motion-in-two-dimensions.md` (section citation, new concept/equation/problem-type/drill links, variables table, diagram, mastery checklist, Parked-for-Later corrected), `wiki/concepts/uniform-circular-motion.md` and `wiki/equations/centripetal-acceleration.md` (removed incorrect "Stage 10" deferral), `wiki/flashcards/stage-4-motion-in-two-dimensions.md` (2 new cards), `wiki/common-errors/stage-4-motion-in-two-dimensions.md` (2 new errors), `wiki/concept-map.md`, `wiki/equation-map.md`, `wiki/problem-type-map.md` (Stage 4 and Stage 5 rows added; gap flag narrowed to Stage 2 and 6–18), `wiki/current-position.md` (Ahead-Check section added), `wiki/parking-lot.md` (backfill flag updated)

### Concepts/equations/problem types added
- Concept + equation + problem type: tangential and radial acceleration (non-uniform circular motion).

### Parked material
- Stage 2 and Stages 6–18 still need the same source-verification pass this session gave Stages 3–5. Per Chris's instruction, not done now — check each one stage-ahead as he progresses, same method: extract the relevant textbook PDF range with `pdftotext`, read the actual section list, compare against the existing stage packet.

### Next action for Chris
- No blockers for Stage 3, 4, or 5 — all three are now verified against the source textbook. Continue with Stage 3 (coordinate systems first), and Stage 4/5 will be ready when reached.

## 2026-07-09 — CLAUDE.md dedup (system-wide, Chris-approved)

### Objective
- Record the operating-file change: duplicated shared blocks (academic integrity,
  chunking) replaced by a pointer to `00-BRAIN\AI_Agent.md § Wiki Shared Layer`;
  this wiki also gains the raw-immutability rule it previously lacked. Expanded
  session protocols stay. No physics content changed.
  Record: `00-BRAIN\Session_Logs\DAILY_2026-07-09.md`.

### Next action for Chris
- Resume Vectors — output reps begin July 10 (cross product ahead; flag 16 anchor
  due when vector products appear).

## 2026-07-09 — Citation/sort audit (Chris-directed, all-wikis sweep)

### Objective
- Sixth hub in the hub-by-hub citation-and-sorting sweep: index vs. live
  tree, frontmatter, raw/ coverage.

### Findings and fixes
- **Index Folders section was badly stale** — still described Stage-1-era
  counts ("concepts/ 6 pages", "common-errors/ 1 page") while the live tree
  holds 58 concepts, 42 equations, 36 problem-types, 35 drills, 46 glossary,
  18 flashcard decks, 18 common-errors pages, and all 18 stage packets from
  the July cruise-prep build. Rewrote the section with live counts, the
  stage-first navigation note, and the generated-vs-studied warning.
- `stages/stage-13-universal-gravitation.md` began with a UTF-8 BOM that
  can break frontmatter parsing — stripped (content untouched).
- raw/ fully accounted for: syllabus + textbook chunks 0001–0600 and
  1201–1370 are all referenced by wiki/log; the 0601–1200 gap is the parked
  Physics-II material, consistent with [[parking-lot]].
- Planned-page wikilinks inside packet pages (~138, e.g. drills and
  problem-types not yet generated) left alone — they resolve as stages
  activate; monthly lint owns the count.

### Next action
- Unchanged: Stage 3 Vectors output rep (Chris's active stage). No system
  work needed here before it.

## 2026-07-11 — CLAUDE.md slim pass (Chris-approved, flag 64)

### Objective
- Slim the always-loaded wiki OS per the Claude-docs review
  (`00-BRAIN\Session_Logs\CLAUDE_DOCS_SYSTEM_REVIEW_2026-07-11.md`).

### Sources touched
- None (system session, no physics content).

### Files created/updated
- CLAUDE.md slimmed 295 → 130 lines; frontmatter timeline tag fixed
  `now` → `reference` (Tag Standard). Old version archived:
  `99-ARCHIVE\ARCHIVED_2026-07-11_PHYSICS_CLAUDE.md`.
- NEW [[authoring-standards]] — core-file specs, four page types,
  stage-packet requirements, writing rules, intake protocol, session
  protocols (all moved from CLAUDE.md, nothing deleted).
- [[index]] — new page registered.

### Concepts/equations/problem types added
- None.

### Parked material
- None new.

### Next action for Chris
- Unchanged: Stage 3 Vectors output rep.

## 2026-07-14 — Stage 3 (Vectors) first live teaching session, paused mid-problem

### Objective
- Run the first live teaching pass on Stage 3 (Vectors) per this wiki's protocol
  (situation → model → quantities → equation → units → problem type → worked
  example → drill), with Chris solving live problems rather than only reading
  the packet.

### Sources touched
- `wiki/stages/stage-3-vectors.md`, `wiki/concepts/coordinate-systems.md`,
  `scalar-vs-vector.md`, `vector-components.md`, `wiki/common-errors/stage-3-vectors.md`
  (read as teaching source; not modified).

### Concepts/equations/problem types added
- None new. This was a teaching rep on existing packet content, not authoring.

### What Chris demonstrated live
- **Coordinate systems:** correctly converted Cartesian (−30, 40) m to polar
  (50 m, 126.87°); self-caught a degree/radian mode mixup on the first pass.
- **Scalar vs. vector:** correctly classified 4 examples; independently
  generalized that adding a direction converts a scalar (distance) into a
  vector (displacement) — one nuance correction given on tension's direction
  being along-the-rope, not assumed-downward.
- **Vector decomposition:** correctly computed Fx = 65.53 N, Fy = 45.89 N from
  80 N at 35°; initially dropped units (newton vs. joule confusion), corrected
  after discussion.
- **Vector reconstruction:** correctly found A = 13 m, θ = 157.38° from
  Ax = −12 m, Ay = 5 m, including the quadrant correction.
- **Vector addition by components:** introduced (40 N at 0° + 30 N at 90°) but
  not completed — Chris had to leave mid-problem.

### Parked material
- None new.

### Next action for Chris
- Resume the paused addition problem (40 N at 0°, 30 N at 90° — explain why
  70 N is wrong before computing the resultant by components).
- After that, one more independent pass over all four skills (conversion,
  scalar/vector ID, decomposition, reconstruction, addition) without notes,
  then check off the Stage 3 mastery checklist in
  `wiki/stages/stage-3-vectors.md` before moving to Stage 4.

## 2026-07-14 — Focused Physics Anki deck reset (Codex + Chris)

### Objective
- Convert the existing broad Physics flashcard stacks into a stage-aligned active
  deck that supports the Stage 3 Vectors frontier without cramming later physics.

### Sources touched
- `wiki/flashcards/stage-1-physics-and-measurement.md`
- `wiki/flashcards/stage-2-motion-in-one-dimension.md`
- `wiki/flashcards/stage-3-vectors.md`
- `wiki/flashcards/stage-4-motion-in-two-dimensions.md` (preview boundary only)

### Files created/updated
- New: `04-SCHOOL\02-Physics I\Flash Cards\Physics_Stages_01-03_Active.tsv`
  (35-card Anki import deck), `README_IMPORT_INSTRUCTIONS.md`, and
  `ADAPTIVE_REVIEW_LOG.md`.
- Updated: `wiki/index.md` and this log.

### Concepts/equations/problem types added
- None. This is a retrieval-layer reset using existing vetted stage cards; dot and
  cross products remain excluded because they are parked beyond the Stage 3 frontier.

### Parked material
- Stage 4 and later decks remain out of the active queue. Stage 4 is the next
  preview only; no later-stage cram deck is authorized.

## 2026-07-16 — Full stage-separated Anki package built (Claude Code, CASTLE hat)

### Objective
- Chris deleted the old Anki decks (they had grown unstructured and too far
  ahead of his actual position) and asked for a complete rebuild: the whole
  thing under one `Physics` deck in Anki, separated by stage, so he can open
  only the subdeck he actually needs instead of facing everything at once.

### What changed
- Wrote `04-SCHOOL\02-Physics I\Flash Cards\Physics_All_Stages.apkg`
  via a one-off `genanki` script (`build_physics_anki.py`, run from the
  scratchpad, not added to the vault). It parses all 18
  `wiki/flashcards/stage-N-*.md` files directly — no content re-authored — and
  emits one Anki package containing 18 subdecks (`Physics::Stage 01 - ...`
  through `Physics::Stage 18 - ...`), 223 cards total. Stage 3's two dot/
  cross-product preview cards carry a `preview` tag.
- Rewrote `README_IMPORT_INSTRUCTIONS.md` to point at the new package (single
  `File → Import`, no manual note-type/separator setup) and marked the July 14
  active TSV and the pre-7/14 mixed decks as superseded-but-preserved.
- Added a superseded note to `ADAPTIVE_REVIEW_LOG.md`'s rotation table.
- Updated this wiki's `index.md` Active Stage block to Stage 4 (Stage 3 closed
  earlier today) and pointed its recall-deck line at the new package.

### Why this shape
- One package instead of 18 separate TSV imports — Chris only performs one
  `File → Import` action, and Anki builds the `Physics::` hierarchy itself from
  the deck names.
- Generated straight from the existing wiki flashcard pages rather than
  rewritten, so the Anki deck and the wiki source cannot drift apart silently —
  regenerating the script after a flashcards/ edit reproduces the package.

### Not done
- Did not delete or archive the July 14 TSV or the pre-7/14 mixed decks;
  AGENT.md file-safety preserves superseded artifacts rather than removing them.
- Did not touch `wiki/flashcards/*.md` content itself — this session only reads
  that source; any card wording fix belongs in those files, then a package
  rebuild.

### Next
- Import `Physics_All_Stages.apkg`, rename/archive any leftover pre-7/14 mixed
  deck in Anki, and study only the `Stage 04` subdeck (plus Stage 01–03 for
  spaced review) going forward.

### Next action for Chris
- Rename the old mixed Physics deck to `Physics::Archive::Pre-2026-07-14`, import
  the focused deck as `Physics::Active::Stages 1-3`, and begin a baseline review.

## 2026-07-14 — Operating contract made model-neutral

- Changed the hub teaching contract from Claude-exclusive wording to “any AI
  teaching physics.” No lesson, stage, mastery, or learner-state content changed.
- Next action remains the paused Stage 3 vector-addition problem already recorded
  above and in the session handoff.

## 2026-07-14 — Learning-path truth reconciled to live Stage 3

- Replaced the stale Stage 1 path status with the live Stage 3 Vectors frontier.
- Marked all 18 packets as generated without calling them mastered; Stages 4–5 are
  source-verified but unstudied, and later stages await sequential re-verification.
- Fixed two broken relative stage links in `current-position.md`.
- Next: resume 40 N at 0° + 30 N at 90°, explain why the resultant is not 70 N,
  then complete a no-notes Stage 3 pass.

## 2026-07-14 — Human guide and prep-plan route verified

- Updated HOW_TO to point to the pre-semester plan and the live learner-state
  authority, including the exact paused Stage 3 action and provisional status of
  generated-but-unmastered packets.
- Cross-reference validation found no active dead link; the next action is unchanged.

## 2026-07-15 — Stage 3 vector-addition problem resumed and solved

### Objective
- Resume the paused 2026-07-14 problem (40 N at 0° + 30 N at 90°) live with Chris,
  per this wiki's teach-then-verify method.

### Sources touched
- `wiki/stages/stage-3-vectors.md`, `wiki/common-errors/stage-3-vectors.md` (read
  as teaching source; not modified).

### What Chris demonstrated live
- Explained why the resultant isn't 40+30=70 N (vector addition depends on
  direction, not just magnitude) after a vocabulary correction.
- Built components from the cos/sin formula: Ax=40, Ay=0, Bx=0, By=30.
- Added components correctly (Rx=40, Ry=30) and computed R=50 N independently.
- Made an angle error (53.13°, the complement of the correct answer) then
  self-corrected to 36.87° from the +x axis, correctly diagnosing that he'd
  measured off the wrong leg of the triangle — without being told.

### Concepts/equations/problem types added
- None new. Teaching rep on existing packet content (vector addition by
  components), the one Stage 3 skill previously flagged as not yet attempted.

### Parked material
- None new.

### Next action for Chris
- This was the easiest case (both vectors axis-aligned, no real decomposition
  needed). Do one more rep with two vectors at non-axis angles, so both actually
  get decomposed, then complete the required no-notes pass over all four Stage 3
  skills (conversion, scalar/vector ID, decomposition, reconstruction, addition)
  before checking off the mastery checklist in `wiki/stages/stage-3-vectors.md`.

## 2026-07-15 — Semester pathway and source-quality unification

### Objective
- Reconcile the full Physics wiki with the updated `.ROOT` context, finish the
  visible Stage 1–18 route, and create a stage-gated trigonometry/calculus refresh
  path grounded in real physical situations.

### Sources touched
- `raw/syllabus/syllabus.pdf` (visual review of the 19-page scan; no raw edits).
- All split Serway textbook PDFs and appendix PDFs (TOC/source screen; no raw edits).
- `02-LIBRARY/REF-META-HOW-TO-WORK/Christopher_Aptitude_Results.pdf` (visual and
  text review used only to choose learning sequence and retrieval supports).
- Official OpenStax, MIT OpenCourseWare, and PhET pages registered in
  `wiki/source-map.md` as optional support for diagnosed gaps.

### Structure completed
- Added `wiki/math-readiness-path.md`: physical sketch → exact math move → guided
  repetition → no-notes transfer → verbal explanation → later cold check.
- Added a complete Stage 1–18 semester control table to `wiki/learning-path.md`
  with math gates, real-life anchors, source status, and packet routes.
- Backfilled Stage 2 and Stages 6–18 into the concept, equation, and problem-type
  maps; fixed their root-map link paths.
- Corrected textbook alignment for Stage 2 (through 2.9), Stage 7 (through 7.9),
  and Stage 17 (17.1–17.7 active; 17.8 parked).
- Updated the hub, current-position, calculus map, source map, parking lot, and
  human guide. No learner mastery checkbox was changed.

### Source-quality findings
- The syllabus PDF is reliable for course identity, outcomes, grading categories,
  and AI policy, but not yet reliable for operations: its calendar ends at Ch 5;
  it includes a January access deadline, an impossible day/date pairing, a recycled
  holiday label, and conflicting exam-drop wording. Live D2L/Owl Express must
  settle those items.
- Textbook screens identified content/scope gates at Stage 6 section 6.3, Stage 9
  sections 9.7–9.9, Stage 11 precession, Stage 14 sections 14.3 and 14.7–14.8,
  and Stage 15 sections 15.6–15.7. These are parked until the live course scope is
  known; later supporting pages remain just-in-time work.
- The Serway appendices already supply the baseline algebra, trigonometry,
  derivatives, and integrals, so a second downloadable math textbook is not needed.

### Next action for Chris
- Resume Stage 3 with two non-axis vectors so both vectors require decomposition,
  then complete the full no-notes Stage 3 pass. Use the Stage 2 calculus bridge
  next: read slope and area from one position/velocity graph before applying a
  kinematic formula.

## 2026-07-15 — Full syllabus and learning-profile closure audit

### Objective
- Confirm that every syllabus page and every named physics outcome has a visible
  destination before closing the Physics folder; review the two additional
  YouScience files supplied by Chris.

### Sources touched
- All 19 pages of `raw/syllabus/syllabus.pdf`, visually inspected.
- `Christopher_Aptitude_Discussion.pdf` (6 pages), visually inspected and text
  checked.
- `Christopher_Aptitude_Results.pdf` (35 pages), previously visually/text reviewed
  during this session and reconfirmed as an input.
- `Christopher_One_Page_Summary.pdf` (1 page), visually inspected and text checked.

### Changes and findings
- Added `wiki/syllabus-coverage-ledger.md`, routing every PDF page to a stage,
  course operations, institutional governance, or student support.
- Applied the syllabus learning outcomes across all stages through a shared mastery
  standard: interpret, represent/model, solve symbolically and numerically, use
  vectors/calculus as needed, check units/reasonableness, and connect to real life.
- Confirmed that every named physics topic in the syllabus is represented in the
  Stage 1-18 sequence. The printed calendar itself still stops at Stage 5/September
  16, so later weeks cannot be assigned official dates without D2L.
- Added the late-homework contradiction to the data-quality gate: page 4 describes
  a 10% daily penalty, while page 7 says work is unavailable after answers release.
- Expanded the math-learning method with strengths from all three profile files:
  numerical pattern finding, spatial/tangible models, thinking aloud, alternate
  approaches followed by a stable process, visible future target, and one next
  action at a time.

### Next action for Chris
- The learning path is closed structurally. Supply the live D2L calendar and current
  grading/exam details when available; until then, treat only the chapter sequence
  as authoritative and all week/date assignments after Chapter 5 as provisional.

## 2026-07-16 — Non-axis vector-addition rep solved; real textbook problem set added

### Objective
- Complete the harder non-axis-angle vector-addition rep flagged 2026-07-15, then
  build a real-textbook problem set (not generated numbers) for Stage 3, per
  Chris's request to work actual Serway end-of-chapter problems going forward and
  flag specific ones for the full reflection/teaching treatment.

### Sources touched
- `raw/textbook/Physics book-0001-0100.pdf` — extracted via `pdftotext -layout`
  to pull the real Chapter 3 "Problems" section (problems 1–32, pp. 63–66) rather
  than generating new numbers.

### What Chris demonstrated live
- A⃗ = 25 N at 40°, B⃗ = 15 N at 120° (both from +x). Correctly computed
  Ax=19.15, Ay=16.07, Bx=−7.5, By=12.99, Rx=11.65, Ry=29.06, R=31.31 N,
  θ=68.15°, and correctly reasoned the quadrant (both Rx, Ry positive → no
  adjustment). This is the first rep where both vectors actually required
  decomposition (no axis-aligned shortcut). The "ladder against a wall"
  physical anchor (Ax = ground reach, Ay = wall height) is what made the
  cos/sin-to-component mapping click.
- Correctly reasoned through tip-to-tail addition geometrically: placing B's
  tail at A's tip (Ax, Ay) and following B out lands at (Rx, Ry) — independently
  connected the graphical and component methods.

### Files created/updated
- `wiki/drills/vector-addition-drill.md` — added Part E with today's problem and
  full worked solution.
- **New:** `wiki/drills/stage-3-textbook-problems.md` — real Serway Ch 3
  end-of-chapter problems (1–32, transcribed from raw PDF via pdftotext, with
  OCR-uncertain figure-dependent ones flagged), organized by section, with a
  blank Reflection? column for Chris to flag live in session.
- `wiki/stages/stage-3-vectors.md` — linked the new textbook problem set under
  Drills.

### Concepts/equations/problem types added
- None new — this closes out the addition skill's harder case and adds a
  retrieval resource; no new concept.

### Parked material
- Problems 15, 16, 20, 22, 23, 28–30, 32 (figure-heavy) not transcribed — pull
  the specific figure from the raw PDF if one is wanted later.

### Next action for Chris
- Full no-notes pass over all four Stage 3 skills (coordinate conversion,
  scalar/vector ID, decomposition, reconstruction, addition) before checking the
  mastery checklist in `wiki/stages/stage-3-vectors.md`. Then start working the
  new textbook problem set, flagging reflection-worthy ones as they come up.

## 2026-07-18 — Full Physics Math Crash Course

### Objective
- Build one complete, stage-mapped review of all math used by the Physics WIKI.

### Sources touched
- Read-only screen of `D:\SCHOOL\Chatt Tech Files\math` (algebra, geometry,
  trig/unit-circle, derivative, integral, calculus-application, Calc II, and
  statistics materials).
- Existing Physics WIKI equation, calculus, units, appendix, learning-path, and
  Stage 4 pages.

### Files created/updated
- Created `wiki/physics-math-crash-course.md`.
- Updated `wiki/index.md`, `wiki/math-readiness-path.md`, and `wiki/source-map.md`.

### Concepts/equations/problem types added
- Unified scientific notation, units, algebra, proportions, graphs, trig,
  vectors, dot/cross products, systems, quadratics, derivatives, integrals,
  rotation, fluids, oscillations, waves, relativity, uncertainty, and lab graphing
  into one physics-first guide with transfer checks.
- Added a Stage 4 projectile bridge and corrected the readiness path from stale
  Stage 3 wording to the active Stage 4 frontier.

### Parked material
- Most Calc II convergence/integration machinery, Laplace and hyperbolic
  functions, complex-number work, and statistics beyond lab uncertainty/graphs.

### Next action for Chris
- Work the crash course's Stage 4 cold projectile transfer rep on paper; review
  only the first module exposed as non-automatic, then retry with changed numbers.

## 2026-07-21 — Cross-Section Syllabus Reconciliation

### Objective
- Reconcile the two newly obtained Fall 2026 PHYS 2211 neighbor syllabi (Section
  51 and Section 55, neither is Chris's registered Section 54) against the
  existing 18-stage path; strengthen and tighten the vault.

### Sources touched
- `raw/syllabus/PHYS 2211 51 (83719) Fall 2026 Syllabus - Reference Only.md`
- `raw/syllabus/PHYS 2211 55 (83723) Fall 2026 Syllabus - Reference Only.md`
- Existing `source-map.md`, `syllabus-coverage-ledger.md`, `learning-path.md`,
  `current-position.md`.

### Files created/updated
- `wiki/source-map.md` — registered both new syllabi in the Sources table;
  identified `syllabus.pdf` as very likely an early truncated capture of the
  same Section 55 syllabus; updated the "later calendar is absent" data-quality
  row to partially resolved.
- `wiki/syllabus-coverage-ledger.md` — added a "Cross-Section Verification,
  2026-07-21" section: confirms Stage 1-12/15 order, flags that neither
  neighbor's calendar schedules Ch 14 or Ch 38 (kept in path per Chris's
  2026-06-25 confirmation), records the grading-structure mismatch, and adds
  soft pacing anchors (Exam 1 ~Sep 25, Exam 2 ~Oct 30, Exam 3 ~Nov 20 per
  Section 55).
- `wiki/learning-path.md` — added the cross-check summary under Path Status;
  flagged Stages 13/14/16/17/18 with the neighbor-calendar gap note; added soft
  pacing-anchor lines to the Stage 5, 10, and 12 detail sections.
- `wiki/current-position.md` — updated First 7-Day Priority item 3 with the new
  pacing evidence.
- `00-BRAIN\SYSTEM_FLAGS.md` flag #57 — logged that the PHYS neighbor syllabi
  are now cross-referenced into the wiki; flag stays OPEN pending real Section
  54 confirmation Aug 24.

### Concepts/equations/problem types added
- None — this was a source-reconciliation and path-integrity pass, not content
  generation.

### Parked material
- None newly parked. Existing Stage 13/14/16/17/18 scope stands unchanged;
  the neighbor-calendar gap is tracked as an open verification item, not a
  parking decision.

### Next action for Chris
- No change to the active Stage 4 study rep. When Section 54 populates in D2L
  (Aug 24+), re-check it against the pacing anchors and the Ch 13/14/16/17/38
  scheduling question logged in `syllabus-coverage-ledger.md`.

## 2026-07-21 — Stage 4-9 Tightening Pass

### Objective
- Chris directed a "chunk format intake" tightening pass on Stages 4-9 tonight,
  following the Source Intake Protocol in `authoring-standards.md`: resolve the
  two known expansion gaps `learning-path.md` had already flagged for this
  range, then check for structural completeness.

### Sources touched
- `raw/textbook/Physics book-0101-0200.pdf` (Ch 6, accelerated frames Sec 6.3;
  Ch 9 section list) — used from prior source-map registration, not re-parsed.
- Existing Stage 4-9 packets, their linked concept/equation/problem-type/
  common-errors/flashcards pages, and `parking-lot.md`.

### Files created/updated
- **New:** `wiki/concepts/accelerated-reference-frames.md` — full concept page
  for noninertial frames and fictitious force (Serway Sec 6.3), the exact gap
  `learning-path.md` had flagged since 2026-07-15.
- **New:** `wiki/glossary/noninertial-reference-frame.md`,
  `wiki/glossary/fictitious-force.md`.
- `wiki/stages/stage-6-circular-motion.md` — added the new concept to Core
  Concepts/Vocabulary/Diagrams, added 3 mastery-checklist items, strengthened
  Do Not Move On Until, fixed frontmatter (added timeline/stage/tags).
- `wiki/common-errors/stage-6-circular-motion.md` — added 2 new error entries
  (fictitious force in the wrong frame; true vs. apparent weight).
- `wiki/flashcards/stage-6-circular-motion.md` — added 3 new cards (13-15).
- `wiki/stages/stage-9-linear-momentum.md` — added the missing "Do Not Move On
  Until" and "Parked for Later" sections (previously absent), added a mastery
  item on p_total = M·v_cm, fixed frontmatter, resolved the Sec 9.7-9.9
  include/park decision using today's neighbor-syllabus evidence.
- `wiki/concepts/center-of-mass.md` — added the explicit p_total = M_total·v_cm
  link between center-of-mass velocity and total system momentum.
- `wiki/stages/stage-5-laws-of-motion.md`, `wiki/stages/stage-8-conservation-of-energy.md`
  — frontmatter-only fix (added timeline/stage/tags) for consistency with
  Stages 4, 6, 7, 9.
- `wiki/parking-lot.md` — marked the Stage 6 §6.3 row resolved; updated the
  Stage 9 §9.7-9.9 row with the park decision and evidence; updated the Stage
  15 §15.6-15.7 row with a lean-toward-include signal from Section 55's real
  calendar (not built tonight — out of the 4-9 scope).
- `wiki/learning-path.md` — flipped Stage 6 and Stage 9 control-table rows and
  detail-section packet-status lines from "needs expansion / needs decision"
  to "ready."
- `wiki/index.md` — updated concepts (58→59) and glossary (46→48) counts and
  the live-counts date.

### Concepts/equations/problem types added
- Concept: motion in accelerated reference frames (fictitious force, apparent
  weight in elevators, centrifugal force as a fictitious force).
- Verified (no gap found, no duplicate created): Stage 5 friction glossary
  already merges static/kinetic; Stage 8 isolated/nonisolated already merged;
  Stage 9 inelastic/perfectly-inelastic already merged; Stage 7/8 power/watt
  already merged. Checked before assuming these needed new stub pages.

### Parked material
- Serway Ch 9 §9.7-9.9 (many-particle systems, deformable systems, rocket
  propulsion) — see `parking-lot.md` for the full decision and unlock
  condition.

### Next action for Chris
- Stages 4-9 are now internally consistent and structurally complete for
  activation. Continue the Stage 4 study rep as planned; when Stage 6 and 9
  come up, both packets are ready with no outstanding expansion debt. Stage 15
  now carries a lean-toward-include signal for damped/forced oscillations —
  revisit when that stage's packet is next expanded.

## 2026-07-21 — Calculus-Link Build-Out for Stages 4-9

### Objective
- Chris asked to pull real content into the calculus material specifically:
  find the actual math connection for each Stage 4-9 topic, and post it with
  practice problems plus a real-world/engineering use-case explanation — not
  just the physics-textbook abstraction.

### Sources touched
- Existing `calculus-links/` pages, `calculus-map.md`, and the Stage 4/6/8/9
  packets' inline "Calculus Connections" sections (previously text-only, not
  linked to a dedicated page for three of the four).

### Files created/updated
- **New:** `wiki/calculus-links/tangential-radial-acceleration-derivative.md`
  — a_t = dv/dt on a curved path (Stage 4 §4.5 / Stage 6), previously only a
  brief inline mention with no dedicated page. 3 practice problems (including
  differentiating a nonlinear v(t)) + engineering use case (highway/conveyor
  curve design, ride/vehicle acceleration limits).
- **New:** `wiki/calculus-links/power-derivative.md` — P = dE/dt and
  ΔE = ∫P dt (Stage 8), previously inline-only. 3 practice problems + use
  case (motor/conveyor sizing, utility demand-charge billing).
- `wiki/calculus-links/kinematics-derivatives.md` (Stage 2, feeds Stage 4) —
  added 3 practice problems + use case (motion-control velocity profiles:
  robotic arms, CNC, elevators).
- `wiki/calculus-links/2d-kinematics-components.md` (Stage 4) — added 3
  practice problems + use case (material-handling conveyor transfer points,
  packaging drop-test trajectories).
- `wiki/calculus-links/stage-7-work-integral.md` (Stage 7) — added 3 practice
  problems + use case (springs/shock absorbers/packaging cushioning sizing).
- `wiki/calculus-links/impulse-integral.md` (Stage 9) — added 3 practice
  problems + use case (crash safety engineering, crumple zones/airbags —
  Δt vs. Δp tradeoff explained numerically).
- `wiki/stages/stage-4-motion-in-two-dimensions.md`, `stage-6-circular-motion.md`,
  `stage-8-conservation-of-energy.md`, `stage-9-linear-momentum.md` — their
  Calculus Connections sections now link out to the full derivation/practice/
  use-case page instead of only describing it inline.
- `wiki/concepts/tangential-and-radial-acceleration.md` — Calculus Connection
  section now links to the new full page.
- `wiki/calculus-map.md` — corrected Stage 6 ("none new" was wrong — a_t
  reused from Stage 4) and Stage 8 ("none new" was wrong — power is a real
  new derivative) roadmap rows; added a table indexing all 9 calculus-link
  pages now built, each tagged with what it covers.
- `wiki/index.md` — calculus-links count 7→9, noted the practice+use-case
  standard now applied to all of them.

### Concepts/equations/problem types added
- No new physics concepts — this was a calculus-depth and cross-linking pass
  on existing Stage 4-9 material, adding worked practice and applied context
  rather than new physical ideas.

### Parked material
- None.

### Next action for Chris
- All Stage 4-9 calculus connections now have a full page with practice
  problems and an engineering use case, not just a one-line mention. Work
  the practice problems cold (cover the Check Yourself section) as part of
  each stage's rep, not just the physics-only drills — the goal is fluency
  differentiating/integrating inside a physical setup, not just algebra with
  given numbers. Stages 10+ calculus-link pages (rotation, angular momentum,
  SHM) already exist from the July build but have not yet had this same
  practice+use-case pass; revisit when those stages activate.

## 2026-07-21 — Pacing Trigger Map Built

### Objective
- Chris asked for a trigger map: a concrete reference for when to read what
  to keep pace for the semester, not just the stage-order path.

### Sources touched
- `04-SCHOOL\View Registration Information.md` — the real,
  confirmed PHYS 2211 Section 54 meeting pattern (MWF 9:10-10:05 AM lecture,
  Friday 11:30 AM-12:25 PM breakout, Aug 24-Dec 14 2026, Marietta Campus) —
  had not previously been pulled into the PHYSICS wiki.
- The two neighbor syllabi and the 2026-07-21 cross-section verification
  already logged in `syllabus-coverage-ledger.md`.

### Files created/updated
- **New:** `wiki/pacing-trigger-map.md` — two trigger types: date triggers
  (a real-Monday-anchored week-by-week table, Aug 24-Dec 14, combining the
  confirmed MWF meeting pattern with the estimated topic/chapter/exam pacing
  from the neighbor syllabi) and state triggers (weekend read-ahead rule,
  exam-approach pre-sweep rule, mastery-moves-the-stage rule overriding the
  calendar, a 7-day stall check, and a hard trigger to re-run the syllabus
  cross-check the day Section 54's real D2L content appears).
- `wiki/index.md` — linked the new page under Core Maps.
- `wiki/current-position.md` — pointed to the new page from the top of the
  file.

### Concepts/equations/problem types added
- None — scheduling/pacing infrastructure, not physics content.

### Parked material
- Fall Break's exact date — neither neighbor syllabus states it clearly;
  left unplaced in the table with an explicit note to confirm via D2L/the
  official academic calendar.

### Next action for Chris
- Use `pacing-trigger-map.md`'s Sunday read-ahead rule starting immediately
  (it doesn't depend on Section 54's dates being final). The moment D2L
  populates real Section 54 content — expected around Aug 24 — re-run the
  cross-check (Trigger Rule 5) and replace the estimated column with real
  dates in the same pass.

## 2026-07-23 — Dead syllabus.pdf path found and fixed (Claude Code)

### Objective
- Chris asked for a second set of eyes on `CLAUDE.md` after the same class of
  issue was found and fixed in the Python wiki: incorrect/stale paths to the
  course syllabi governing this hub.

### Work completed
- Found that `source-map.md`, `syllabus-coverage-ledger.md`,
  `current-position.md`, and `learning-path.md` all cited `raw/syllabus/
  syllabus.pdf` as a live, currently-readable file — course outcomes, grading,
  AI policy, and the full 19-page data-quality gate were all written as if the
  file still lived there. It does not: `raw/syllabus/` currently holds only
  the two real Fall 2026 section syllabi (`PHYS 2211 51` and `PHYS 2211 55`)
  plus `README.md`. The original `syllabus.pdf` was moved on 2026-07-21 to
  `99-ARCHIVE\04-SCHOOL\SYLLABI_REPLACED_2026-07-21\02-Physics I\
  syllabus.pdf` — confirmed by direct filesystem search, not inferred.
- This is a harder break than the Python case (which cited an existing but
  non-canonical duplicate): here the exact cited file is genuinely gone from
  the path four separate pages pointed to.
- `syllabus-coverage-ledger.md`'s own July 21 Cross-Section Verification
  section had already reasoned that `syllabus.pdf` was "very likely an early,
  truncated capture" of the Section 55 syllabus and should be "treated as
  superseded" — but nothing had gone back to update the citing pages once
  that was known, and none of them had discovered the file was actually
  archived, not just superseded-in-place.

### Pages created/updated
- `source-map.md` — the `syllabus.pdf` Sources-table row now states it is
  superseded/archived with its current path; the Syllabus Data-Quality Gate
  section is relabeled historical, sourced from the archived PDF, not a live
  file.
- `syllabus-coverage-ledger.md` — added a Source note dating the archive move
  and pointing to the current file location; the "original spine source" line
  in Cross-Section Verification updated to past tense with the same pointer.
- `current-position.md`, `learning-path.md` — both "Built from `raw/syllabus/
  syllabus.pdf`" lines corrected to note the file is superseded/archived and
  point to the two real section syllabi as the live reference.
- `parking-lot.md` — the two rows sourced to `syllabus.pdf` (remaining
  calendar, operational corrections) updated with the archive pointer; the
  calendar row also notes the 2026-07-21 partial resolution already recorded
  in `source-map.md` (Section 55's real Ch 6-15 calendar) that these two rows
  hadn't been updated to reflect.

### Concepts/equations/problem types added
None — citation/path correction only.

### Progress evidence
n/a — governance session. No physics content changed; all data-quality
findings and course facts extracted from `syllabus.pdf` while it was live
remain accurate and are preserved, just correctly labeled as historical.

### Parked material
None new.

### Next action for Chris
None urgent — this was a citation-path repair, not a content change. The
existing next actions (Section 54 D2L confirmation, Aug 24+) are unchanged.

## 2026-07-24 — Machine-interface architecture conversion (Codex)

### Objective
- Convert the PHYSICS hub to the governed loader/contract/human-router pattern
  without changing learner progress, physics content, or raw evidence.

### Sources touched
- Existing PHYSICS operating files, current position, learning path, index,
  source map, and Fall 2026 semester goal.

### Files created/updated
- New `OPERATIONS.md`: canonical machine contract with authority, durable-spine
  and course-overlay lifespans, INGEST/QUERY/LINT operations, teaching contract,
  mastery proof, academic-integrity boundary, raw boundary, and close rule.
- `CLAUDE.md`: reduced to a thin deterministic AI loader.
- New `README.md`: human entry router.
- `HOW_TO_USE.md`: rewritten as the human study workflow; retired
  `PRE-SEMESTER_PREP_PLAN.md` pointer replaced by `fall_2026_semester.md`.
- `authoring-standards.md`, `source-map.md`, `calculus-map.md`, and
  `syllabus-coverage-ledger.md`: live authority pointers moved from
  `CLAUDE.md` to `OPERATIONS.md`.
- Added a Git-object archive manifest for the exact pre-conversion
  `CLAUDE.md` and `HOW_TO_USE.md` blobs. Historical log references remain
  historical.

### Concepts/equations/problem types added
- None. Stage 4 remains active; no learner proof or stage advancement claimed.

### Parked material
- Existing frontmatter normalization debt remains a separate mechanical pass.

### Next action for Chris
- Begin the Stage 4 projectile-motion rep in `wiki/current-position.md`, while
  using the Stage 3 textbook problems as the recorded durability check.

## 2026-07-25 — Stage 4 Week Plan, Stage 5 Readiness, and Report Repair

### Outcome
- Confirmed Stage 4 is the active learner frontier, installed a dated July
  26–August 1 deep-dive, prepared Stage 5's launch sequence, and repaired the
  PHYSICS session-report standard to match the canonical Return Packet.

### Evidence
- Direct PDF inspection verified Chapter 4 at book pp. 68–94 and Chapter 5 at
  pp. 95–126. The prior Stage 5 citation of pp. 109–143 was incorrect.
- `current-position.md`, `learning-path.md`, and `index.md` now agree that Stage
  3 closed July 16, Stage 4 is active, and Stage 5 is ready but not active.
- Root health: PASS WITH DEBT; 0 wiki blockers, 0 review links, 0 new
  frontmatter debt, 0 whitespace findings, and 0 live-text-integrity findings.
  The 320 reviewed metadata findings remain baseline debt.

### Capability/status movement
- Learner status did not move: no independent physics performance occurred.
- System readiness moved: Stage 4 now has a complete dated rep sequence and
  relative-velocity drill; Stage 5 has a verified reading/exercise order and
  cold entry check.

### Errors, uncertainty, or residual risk
- Corrected stale Stage 3 status in `learning-path.md`, the incorrect Stage 5
  page range, and unverified instructor/date claims in the active Stage 4–5
  interface.
- Section 54 instructor, lecture dates, and exam dates remain unknown until
  official D2L material appears. Later-stage historical instructor labels were
  not expanded into this Stage 4–5 task.
- The health gate does not evaluate semantic freshness outside its named scopes.

### Exact next independent rep
- July 26: read Ch 4 §4.1–4.2 (book pp. 68–74), write x(t), y(t), v_x(t), and
  v_y(t) from memory, then solve projectile drill Problems 1–2 cold.

### Reusable-asset candidate
- No. This is a domain learning plan and local report repair, not a commercial
  asset.

### System-learning candidate
- No open nomination. The local report-template mismatch was identified and
  repaired in the same session; monitor the next PHYSICS session report for
  outcome/evidence/frontier/next-rep quality before generalizing further.

### Sources and files touched
- Source PDFs: the immutable Chapter 4–5 textbook chunks in `raw/textbook/`
  (read only).
- Updated: `OPERATIONS.md`, `wiki/authoring-standards.md`,
  `wiki/current-position.md`, `wiki/index.md`, `wiki/learning-path.md`, and
  Stage 4–5 packets.
- Added: `wiki/drills/relative-velocity-drill.md`.

---

## 2026-07-26 — Forward-Path Operational Readiness Audit (Claude Code)

### Outcome
- Resolved every wikilink in all 18 stage packets against the live filesystem
  instead of against this wiki's own status claims. **Stages 4–9 are fully
  operational; all 78 unresolved links sit in Stages 10 and 12–18.** Corrected
  the Semester Pathway Control Table, which under-reported five stages and
  over-reported one.

### Evidence
- Stages 4–9 depend on 96 linked pages. All 96 resolve. 94 carry substantial
  content (≥25 lines); the two short ones are `glossary/elastic-collision.md`
  and `parking-lot.md`, both correctly brief for their type.
- Verified per-stage unresolved counts: Stage 10 = 10, Stage 11 = **0**,
  Stage 12 = 2, Stage 13 = 9, Stage 14 = 9, Stage 15 = 6, Stage 16 = 11,
  Stage 17 = 9, Stage 18 = 22.
- The prior table said Stage 11 had unfinished supporting links (it does not —
  its remaining item is a gyroscope/precession *scope* question) and said
  nothing about gaps in Stages 12, 14, 15, 17, or 18, which together hold 48
  unresolved links.
- `source-map.md`'s link to `../OPERATIONS.md` initially registered as broken;
  verified as a false positive — the file exists at 9,044 bytes outside `wiki/`,
  which is a legitimate target.

### Capability/status movement
- Learner status did not move: no physics performance occurred in this session.
- Map accuracy moved: the control table's readiness column is now filesystem-
  verified rather than asserted, per `AGENT.md`'s rule that maps are claims and
  not filesystem truth.

### Errors, uncertainty, or residual risk
- Link resolution proves a target page exists, not that it teaches well. Stages
  7–8 remain "TOC screened" in substance even though their links all resolve.
- No build-out of Stages 10–18 was performed, deliberately. The just-in-time
  rule expands a stage when Chris is one stage away; Stage 10 is five out, and
  Section 54's real D2L calendar (expected Aug 24) may still park or reorder
  Ch 13–18. Building 78 pages now would repeat the July cruise-prep pattern of
  generating content ahead of evidence that it is needed.
- Recorded in `learning-path.md` that advancement is mastery-gated, not
  calendar-gated — a weekly plan allocates hours and cannot hold a finished unit
  open or license leaving an unfinished one. This restates
  [[pacing-trigger-map]]; it is not a new rule.

### Exact next independent rep
- Unchanged from July 25: read Ch 4 §4.1–4.2 (book pp. 68–74), write x(t), y(t),
  v_x(t), and v_y(t) from memory, then solve projectile drill Problems 1–2 cold.

### Reusable-asset candidate
- Possibly. The link-resolution audit is subject-neutral and would answer the
  same "will this stall me?" question for PYTHON or any other staged hub. Not
  nominated yet — one use is not a pattern.

### System-learning candidate
- Nominated for evidence, not adoption: this wiki's status column drifted from
  its own filesystem in both directions while every individual edit was correct.
  Same class as the July finding that update output became truth without a
  check. Second instance; a third would justify a standing rule.

### Sources and files touched
- Read only: all 18 stage packets, 8 control files, and the linked page tree.
- Updated: `wiki/learning-path.md` (Path Status readiness block + 15 control-
  table rows), `wiki/log.md`.

## 2026-07-26 — Clean PHYSICS Hub System Load (Codex)

### Outcome
- Verified from a fresh session started inside `03-WIKIS/PHYSICS` that the new
  hub pointer resolves through `CLAUDE.md` to `OPERATIONS.md`,
  `wiki/current-position.md`, and `wiki/learning-path.md`.
- Confirmed Stage 4 remains the active learner frontier and the next independent
  physics work is the owner-defined projectile-motion rep; no mastery movement
  was claimed.

### Evidence
- Read the governed root boot chain, North Star, morning-launch state, CASTLE
  current position and weekly plan, then the PHYSICS local loader and learner
  truth chain.
- The clean learner-hub boot proof is complete. A non-learner hub boot remains
  the second acceptance check named in the July 26 handoff.

### Exact next independent rep
- Read Ch 4 overview and sections 4.1–4.2 (book pp. 68–74), draw one launch
  diagram, write x(t), y(t), v_x(t), and v_y(t) from memory, then complete
  projectile-motion drill Problems 1–2 cold.

### Files touched
- Updated: `wiki/log.md`.
- Root continuity updates: `MORNING_BRIEF.md` and
  `00-BRAIN/Session_Logs/DAILY_2026-07-26.md`.

---

## 2026-07-27 — Stage 4 first handwritten rep: launch diagram + full angled-launch solve (Claude Code)

### Outcome
- First real artifact under the handwritten-iPad method. Chris cold-picked
  and solved an angled-launch problem (soccer ball, v₀ = 18 m/s @ 40°, ground
  level) live in chat: launch diagram with axes, sign convention, θ marked,
  v₀ labeled — then, after one added correction, decomposed v₀ into v₀ₓ/v₀ᵧ,
  found flight time, range, and max height.

### Evidence
- Diagram received via a Google Drive share link, read directly from the
  source PDF — not yet exported into `wiki/handwritten/`.
- v₀ₓ = 18cos40° = 13.79 m/s, v₀ᵧ = 18sin40° = 11.57 m/s — both correct on
  the first attempt.
- First explain-back gap: the diagram initially skipped the v₀ₓ/v₀ᵧ
  decomposition entirely (stray î/ĵ notation placed in the wrong spots
  instead of drawn components). Corrected with one physical anchor (the v₀
  arrow's tip drops a dashed line to each axis, forming a right triangle)
  before Chris re-sent.
- Two arithmetic slips, both self-corrected fast once flagged: flight time
  first computed with g = 0.8 instead of 9.8 (misread the "9"); then range
  and max height both computed using total v₀ = 18 instead of the
  direction-specific component (v₀ₓ for range, the full y(t) equation for
  height).
- Final correct numbers: T = 2.36 s, range ≈ 32.5 m, max height ≈ 6.8 m —
  confirms Chris's own live hypothesis (stated mid-problem, before the
  numbers existed) that horizontal distance exceeds vertical rise.
- This problem is structurally the drill's **Problem 3** (angled launch, max
  height + range), not the assigned **Problems 1-2** (horizontal launch,
  v₀ᵧ = 0 at launch) — those remain open for this afternoon.

### Capability/status movement
- Stage 4 moves from "packet ready, zero attempts" to "first rep complete,
  with corrections." Not a mastery gate — Friday's conditional Stage 4 gate
  remains the real checkpoint. This rep functionally covers most of the
  Seven-Day Plan's original diagram/equations task, minus the specific
  Problems 1-2.

### Errors, uncertainty, or residual risk
- The three error classes hit today (missing component decomposition, a
  misread constant, substituting total magnitude for a directional
  component) are worth a quick cross-check against
  `common-errors/stage-4-motion-in-two-dimensions.md` to confirm they're
  already-named categories rather than new ones.
- Artifact still lives only on Chris's Google Drive as of this entry.
  Target filename: `2026-07-27_stage-04_launch-diagram.pdf`.
- Section 54's real syllabus/problem set is still unconfirmed (flag #57);
  today's problem was self-generated, not assigned.

### Exact next independent rep
- This afternoon (running ~30 min late after a family interruption):
  `[[drills/projectile-motion-drill]]` Problems 1 and 2 — horizontal launch,
  a genuinely different case since v₀ᵧ starts at zero.

### Files touched
- This log; `wiki/current-position.md` (Active Unit section — today's rep
  recorded, Seven-Day Plan date conflict flagged).

## 2026-07-26 — Handwritten-physics method adopted (Claude Code)

### Outcome
- Chris's decision recorded as hub method: **all physics work is handwritten on
  the iPad**, because the work is spatial — diagrams, axes, sign conventions, and
  vector decomposition cannot be typed without converting the problem into
  transcription. New page: `wiki/ipad-handwritten-physics-method.md`. New evidence
  folder: `wiki/handwritten/`.

### Evidence
- The method's page skeleton (sketch + knowns/unknowns → model → symbolic →
  numbers → check) maps one-to-one onto the syllabus-wide mastery standard and
  onto the eight evidence components the Stage 4 gate requires. Its purpose is
  that a miss can be located to a box rather than scored as one aggregate wrong
  answer.
- Colour convention fixed: black given, blue work, red answer, **green
  correction**. Wrong first attempts are never erased — the first attempt plus a
  green correction on one page is the artifact the teaching loop needs.
- Artifact naming: `handwritten/YYYY-MM-DD_stage-NN_drill-name.pdf`.

### Capability/status movement
- None. No physics was worked this session; Stage 4 remains active and the
  frontier is unchanged.

### Errors, uncertainty, or residual risk
- The method is unproven — zero artifacts exist yet. Deliberately *not*
  standardised further: per the July 24 source batch, run the week, keep whatever
  Chris actually does twice, and write that down after it exists.
- First rep is deliberately small: Monday 11:00, one launch diagram only.

### Exact next independent rep
- Monday July 27, 11:00 — Ch 4 §4.1–4.2 (pp. 68–74), hand-draw one launch
  diagram with axes and sign convention marked. Tonight's reading assigns the
  pages.

### Files touched
- Added: `wiki/ipad-handwritten-physics-method.md`, `wiki/handwritten/`.
- Earlier same day: `wiki/learning-path.md` (operational-readiness audit).

## 2026-07-27 — Neighbor Section 51 syllabus recapture routed (Codex)

- A fresh Simple Syllabus capture for PHYS 2211 Section 51 arrived during the
  CASTLE inbox sort. It now names Farhan Islam (`fislam7@kennesaw.edu`), where
  the July 21 capture omitted the top instructor block.
- Replaced the school-library Section 51 reference and preserved the July 21
  version under
  `99-ARCHIVE/04-SCHOOL/SYLLABI_REPLACED_2026-07-27/`.
- Corrected `source-map.md`, `syllabus-coverage-ledger.md`,
  `SYLLABUS_STATUS.md`, and flags #57/#85. The immutable PHYSICS `raw/` copy
  was not modified.

**Learner status:** unchanged. Section 51 is still a neighboring reference and
does not establish Chris's Section 54 instructor, grading, dates, or AI policy.

**Next exact rep:** unchanged — continue the active Stage 4 plan.

**Chris clarification:** Farhan Islam is also listed online for Chris's actual
Section 54. Updated `current-position.md`, `source-map.md`,
`SYLLABUS_STATUS.md`, and flag #57 to classify Farhan as the provisional likely
instructor. Exact-section grading, dates, and policies remain unconfirmed.
## 2026-07-28 — Math-first learning calibration and syllabus reconciliation (Codex)

### Outcome
- Calibrated the PHYSICS teaching system to use mathematical structure as
  Chris's entry ramp, followed by explicit physical translation, diagrams,
  parameter changes, units, limiting cases, and independent transfer.
- Kept the durable textbook stage numbers intact while adding a separate course
  execution overlay: Section 51/Farhan is the best provisional Fall pacing
  source; the Summer Section 54 file corroborates scope only.
- Marked Stages 14 (fluids) and 18 (relativity) as Fall-scope pending and added
  an early-readiness trigger for Stage 13 because Farhan's reference calendar
  places gravitation near Chapters 5-6.

### Evidence
- Direct comparison of the Fall Section 51/Farhan syllabus and Summer Section
  54/Akshay Agarwal syllabus: same Serway/Jewett 10th-edition spine and the same
  core through Chapters 1-13 and 15-16; Fall adds explicit Chapter 17 pacing.
- Active Stage 4 now explains projectile motion as one linear and one quadratic
  component function sharing the same time variable, with physical meaning for
  each term and parameter.

### Capability/status movement
- Learner stage did not move from this system work. Stage 4 remains active;
  Chris was reading Chapter 4 section 4.3 before the independent physics rep.

### Errors, uncertainty, or residual risk
- Exact Fall Section 54 syllabus remains unavailable. Section 51 dates,
  grading, and policies are nonbinding.
- The Summer Section 54 file is classified in `77-INBOX`; the protected
  filesystem refused the authorized move into `raw/syllabus`.

### Exact next independent rep
- Finish Chapter 4 section 4.3 reading, then solve the scheduled angled-launch
  work using `predict -> calculate -> interpret`.

### Reusable-asset candidate
- No. This is a domain-specific calibration of the existing PHYSICS method.

### System-learning candidate
- No new cross-system rule; the preference is recorded in the owning learning
  hub.

### Sources and files touched
- Updated PHYSICS operations, authoring standards, current position,
  math-readiness path, Stage 4 packet, learning path, source map, syllabus
  coverage ledger, local loader, this log, and the cross-course syllabus status.
- Classified `77-INBOX/PHYS 2211 54 (52148) Principles of Physics I.md` as a
  reference-only Summer source.

**Filename clarification:** Chris renamed the canonical Fall/Farhan reference to
`raw/syllabus/PHYS 2211 51 (83719) Fall 2026 Syllabus - Best copy.md`.
Live source pointers now use that name. Its frontmatter remains
`status: reference-only` because it is Section 51, not Chris's Section 54.

**Path-authority clarification:** Chris then explicitly selected that Fall/Farhan
syllabus—not ascending textbook order—as the preparation path until he says
otherwise. The textbook now supplies content in syllabus order. The execution
path is Stage 1→2→3→4→5→Stage 13 gravity foundation→6→7→8→9→10→11→12→15→16→17.
Printed chapter cells that contradict their topic labels do not control.

## 2026-07-28 — Angled Launch Drill (Problems 3–4) + Session Review Page

### Outcome
- Read Ch 4 §4.3 (pp. 74–80), then solved
  [[drills/projectile-motion-drill]] Problems 3 and 4 live with Claude.
  Both self-corrected to the right answer after a wrong first pass.

### Evidence
- Problem 3: max height and range correct on first try (5.10 m, 35.35 m);
  time of flight wrong first try (1.77 s — used v₀ᵧ/g, the time-to-peak
  formula, instead of 2v₀ᵧ/g), self-corrected to 2.04 s after being asked to
  compare the two formulas.
- Problem 4: max height and range correct (8.61 m, 19.89 m); first time-root
  attempt (3.06 s) repeated the same t_peak-vs-t_flight confusion plus
  plugged raw v₀ instead of v₀ᵧ. Redirected to the general quadratic
  (y = v₀ᵧt − ½gt² = 5.00); first quadratic attempt gave 1.59 s / 3.31 s,
  caught as physically impossible by comparing against the symmetric-case
  total flight time (~2.65 s) as an upper bound; corrected to 0.47 s / 2.18 s,
  matching the source answer key (0.466 s / 2.19 s).

### Capability/status movement
- Angled-launch time-of-flight formula: real, corrected miss — the
  t_peak-vs-t_flight confusion is now identified and named, not just
  "got it wrong once." Sanity-checking a quadratic root against a known
  physical bound is a technique Chris used unprompted-ish (with one nudge)
  and should keep using on every two-root projectile problem going forward.

### Errors, uncertainty, or residual risk
- Same error type surfaced twice in one session (Problems 3 and 4) before
  it stuck — worth a quick re-check on Problem 6 (cliff, asymmetric) later
  in the drill to confirm it's actually retained, not just corrected in
  the moment.

### Exact next independent rep
- Continue the drill or move to Ch 4 §4.4 (uniform circular motion) per
  the weekly plan; re-test the time-of-flight distinction cold before
  trusting it as mastered.

### Reusable-asset candidate
- Yes — created `wiki/worked-examples/2026-07-28-angled-launch-session-review.md`,
  a synthesis page tying trig decomposition, the calculus derivation, and
  the formula table together, anchored to this session's two real mistakes
  for review/retention. Cross-links the existing canonical pages rather than
  duplicating them.

### System-learning candidate
- No new cross-system rule.

### Sources and files touched
- `wiki/drills/projectile-motion-drill.md` (read only, no edit)
- `wiki/worked-examples/2026-07-28-angled-launch-session-review.md` (new)
- This log.

## 2026-07-28 (evening prep) — Local Calculus Library Screened + Pre-Semester Transfer Sprint Planned

### Outcome
- Chris asked for a month-long calculus review using his own books at
  `02-LIBRARY\ref-math\` (four calculus texts + a precalculus text), cross-
  referenced against the physics work ahead this semester. Screened each
  book's table of contents (read-only, nothing copied or moved) rather than
  reading them, per the existing "no second parallel course" rule already
  stated in `source-map.md`.

### Evidence
- Registered all four calculus texts (Strang, OpenStax Calc Vol.1-3) plus
  the local Precalculus copy in `source-map.md` § Local Calculus Library,
  each with a calculus-support role and a just-in-time intake rule matching
  the existing MIT OCW rows. Strang's table of contents is an unusually
  strong match — it has sections literally titled "Circular Motion,"
  "Second Derivatives: Bending and Acceleration," "Masses and Moments,"
  "Force, Work, and Energy," and a whole chapter, "Motion Along a Curve,"
  covering position vectors, projectiles, and curvature — i.e., today's
  exact topic. Two other books in that folder (statistics, data science)
  are out of scope and got no role.

### Capability/status movement
- No stage or gate moved. This is source registration and a planned
  sequence, not a completed rep.

### Errors, uncertainty, or residual risk
- None. Screening was TOC-only; no content claims made beyond chapter
  titles and page numbers.

### Exact next independent rep
- `math-readiness-path.md` § Pre-Semester Calculus Transfer Sprint now lists
  the 9 already-built calculus-link pages in order as the sprint sequence,
  starting from tonight's Stage 4 rep. Pull a Strang/OpenStax section only
  when a specific rep doesn't click — reading order is Serway appendix,
  then the calculus-link page, then Strang, then OpenStax volumes if still
  needed.

### Reusable-asset candidate
- Yes — the source-map registration and the sprint sequence are both now
  reusable for the rest of the semester, not just tonight.

### System-learning candidate
- No new cross-system rule; this follows the existing July 18 screening
  precedent exactly.

### Sources and files touched
- `wiki/source-map.md` (new § Local Calculus Library)
- `wiki/math-readiness-path.md` (new § Pre-Semester Calculus Transfer Sprint)
- This log.

## 2026-08-02 — Calc I/II Crosswalk added to calculus-map (Chris-directed)

### Session goal
Chris asked for a semester-preview view: every piece of calculus the Fall
path will use, tied back to what he already learned in Calc I/II, so no
material arrives as a surprise — "more of a calculus lesson than physics."

### Evidence
- `calculus-map.md` gains a new § Calc I/II Crosswalk between the roadmap
  and § Later Stages: (a) nine already-owned Calc I/II tools with their
  stage locations and a recall-risk rating grounded in the July 30 live
  drill (integration constants/boundary conditions marked High, the
  confirmed gap); (b) five genuinely-new items (dot product, cross
  product/right-hand rule, `dm` setup, reading a differential equation,
  ∂ notation) with what each actually demands; (c) an explicit list of
  Calc II machinery the course never uses (parts, trig sub, partial
  fractions, series tests, polar).
- `00-BRAIN\hats\HAT_PHYSICS.md` corrected: instructor line now names
  Farhan Islam (provisional, two-source match 2026-07-29, flag #57 still
  open on syllabus content) instead of the stale "Dr. Behera"; the flag
  #16 note no longer carries embedded learner position.

### Capability/status movement
- None. Reference/map content and a hat correction; no stage or gate moved.

### Errors, uncertainty, or residual risk
- Crosswalk stage locations were derived from this map's own roadmap
  (screened 2026-07-15), not re-verified against the textbook this
  session. Recall-risk ratings are calibrated from one live drill
  (July 30); Week B's P8 miss record will confirm or correct them.

### Exact next independent rep
- Unchanged — Monday P1 per the approved Aug 3–9 weekly plan:
  integration-constant repair, then the motion chain and 2D components.
  Use the crosswalk as the "which tool is this?" reference during P1–P8.

### Reusable-asset candidate
- Yes — the crosswalk serves every remaining stage and both C–D
  durability weeks.

### System-learning candidate
- No.

### Sources and files touched
- `wiki/calculus-map.md` (new § Calc I/II Crosswalk)
- `00-BRAIN/hats/HAT_PHYSICS.md` (instructor + flag-16 note corrections)
- This log.

## 2026-08-02 — Queue rule added to dated schedule (Fable, delta entry)

- Delta since this evening's crosswalk entry: `math-readiness-path.md`'s
  Dated Daytime Schedule now carries a Chris-directed queue rule — rows are
  an ordered queue with default pacing dates, advancement governed by the
  weekly plan's new Move-On Gate (cold transfer + explain-back = pass;
  two-block cap; misses routed to Weeks C–D). No stage, gate, or learner
  truth moved.

## 2026-08-16 — Row 2 PASSED: integral mechanics and the constant of integration (Claude Code)

**First learner rep since July 30.** Seventeen days, none of them idle — the
gap was the `.ROOT` pause and the pre-semester system update, not avoidance.

### What ran
- Entered at **row 2** of the Dated Daytime Schedule per `HAT_PHYSICS_MATH`'s
  entry-point rule, **not** at today's date. Rows 2–4 were still marked
  *"planned, did not run."* Advancement is proof-gated, not date-gated.
- Hats: `HAT_EDUCATOR` → `HAT_PHYSICS_MATH`. Delivery worked → faded → cold.

### Result — Move-On Gate met in full

| Phase | Problem | Outcome |
|---|---|---|
| Worked | Ball up at 12 m/s from ground; both constants shown, `C₂ = 0` | shown, not graded |
| **Faded** | Ball up at 7.0 m/s from a 20 m roof — **both constants nonzero** | **PASS** — `y(t) = −4.9t² + 7.0t + 20` |
| **Cold** | `a(t) = 6t`, `x₀ = 2.0 m`, `v₀ = −4.0 m/s` — no kinematic formula applies | **PASS** — `x(t) = t³ − 4t + 2` |
| **Explain-back** | *"Why can't you use `x = x₀ + v₀t + ½at²` here?"* | **PASS** — *"acceleration is not constant"* |

### What this proves — the July 30 gap specifically

July 30's diagnosis was *"the power rule came back fast, but 'why is C = 3
here' did not."* On the first attempt Chris gave the initial conditions as
**values** (`v = 7.0 at t = 0`). Prompted once for words, he produced them
unprompted and correctly thereafter: *"at time 0 the ball is at a height of
20 meters above the ground and is still moving at a velocity of 7.0 m/s."*
**The words-before-symbols step is the thing that broke in July, and it held
here** — including on the cold problem, where he read the sign correctly
(*"moving away from the motor"*, `v₀` negative against positive `a`).

**Evidence he integrated rather than pattern-matched:** the `−4t` term in the
cold answer. That is `C₁` carried through the *second* integration, and it
cannot appear from a formula lookup — it requires having written
`v(t) = 3t² − 4` first.

### Anchor delivered (closes the loop back to row 3)
`x = x₀ + v₀t + ½at²` **is** the double integration run once with constant `a`:
`v₀t` is literally `C₁t`, `x₀` is `C₂`, `½at²` is `∫∫a dt dt`. The kinematic
equations are a licensed shortcut, not a separate law. This sets up row 3
directly.

### Misses / weak points — logged, not repaired
1. **`v(t)` never written on either problem.** Twice. He clearly computed it
   (the `−4t` proves it), but the intermediate line is where `C₁` is fixed and
   it is the line that costs marks when algebra goes wrong under exam
   conditions. **Watch on row 3; correct if it recurs a third time.**
2. First-attempt initial conditions came out as values, not physical words.
   Self-corrected after one prompt. Not a miss; a tendency to watch.

### Exact next independent rep
- **Row 3** — cold rebuild of all three 1D kinematics equations from
  `a = const`, no formula sheet. **Flag `v² = v₀² + 2aΔx` explicitly:** it is
  algebraic elimination of `t` between the other two, **not** a third
  integration. Two of the three are already effectively derived by today's
  anchor; the third is the one that misleads.

### Stage / frontier movement
- **None.** Stage 4 remains active, still open at circular-motion drill 1–4.
  Row 2 is a math-readiness queue row, not a stage gate. `current-position.md`
  is unchanged and correctly so.

### Sources and files touched
- `wiki/math-readiness-path.md` (row 2 marked run and passed)
- This log.

---

## 2026-08-17 (Monday, midday) — math-readiness **row 3 PASSED**; reasonableness check is the new open habit

**Session:** Claude Code, full chain loaded (`HAT_EDUCATOR` → `HAT_PHYSICS` →
`HAT_PHYSICS_MATH` → hub `OPERATIONS.md` → `current-position.md` →
`math-readiness-path.md`). First rep after `.ROOT` resumed on `OK TO START`.

**Honest timing caveat, stated before the rep and repeated here:** row 2 ran the
previous night, so this sits ~15 hours later — **inside** the 48–72 h window, not
after it. Per the hub teaching contract this is a same-window rep and **is not
banked as durability evidence.** The durability check that counts for advancement
is still owed, Tue–Wed.

### Row 3 — cold rebuild, no formula sheet: PASS

Chris produced both integrations cold and unprompted:

- `v(t) = at + C₁`, with **`C₁` = initial velocity, found by setting t = 0**
- `x(t) = ½at² + v₀t + C₂`, with **`C₂` = "the starting position in measured frame"**

**"In measured frame" is better than the standard answer** and was not prompted.
`x₀` is a property of where the origin was placed, not of the object.

**Derive-vs-remember probe, and it came back clean.** He wrote `v₀t` where the raw
second integration gives `C₁t`. Asked whether that was a deliberate substitution or
memory of the printed formula, he described the correct procedure: resolve `C₁` at
t = 0, substitute it in, *then* integrate again. **That is derivation, and it is the
version that survives a problem where the object does not start at t = 0.** The July
30 words-before-symbols gap held for the third consecutive session, unprompted.

### The `v²` equation — flagged and shown once, per the failure-mode table

Delivered structurally before algebraically: `a = const` gives a chain with exactly
**two levels** (`a → v → x`), so there are exactly two integrations available and
**no third level to integrate to.** A third kinematic equation therefore cannot be
calculus. Reinforced by notation — the equation is written in **`Δx`, not `dx`** —
a finite change between two endpoints is the language of algebra, not accumulation.
Then the elimination of `t` shown term by term, with `2v₀v` cancelling.

**Chris supplied the same insight independently on the transfer problem** — asked why
he chose that equation, he answered *"there is no time involved in the question, it is
looking at the full sequence."* Endpoints, not process. Equation-choice reasoning is
sound.

### Transfer problem — cold: PASS

Car at 28 m/s, `a = −6.0 m/s²`, find stopping distance. Correct equation chosen with
correct stated reason; **found the hidden given** (`v = 0` supplied by the word
"stopping"); arithmetic correct at 65.3 m.

### Misses — logged

1. **Significant figures.** Reported `65.333 m` from two-sig-fig inputs. Corrected to
   **65 m**. Physics correct, reporting wrong — and WebAssign marks this wrong.
   **Error class: execution/reporting.** First occurrence.
2. **🔴 Reasonableness check skipped — third consecutive drop, now the standing gap.**
   Asked three times across the session; the eventual answer was *"sounds about right
   to me,"* which is assent, not verification. Root cause judged to be **missing form,
   not carelessness** — he had not been shown what the output looks like. Taught once,
   concretely: **a reasonableness check is arriving at the same number by a different
   road.** Demonstrated with `t = 4.7 s` → average velocity `14 m/s` → `Δx = 65.8 m`,
   matching the `v²` route. **Error class: execution/verification. Watch on row 4; if
   it drops a fourth time the cause is not form.**
3. **`v(t)` labelling — row 2's watch item did not recur in the same way** but the
   rebuild was still written as bare expressions (`at + C₁`) rather than
   `v(t) = at + C₁`. Named live, with the functional reason: the `v²` elimination
   substitutes *between two different functions*, and unlabelled lines lose track of
   which is which. **Third occurrence overall; corrected once, now watch.**

### Stage / frontier movement

- **None.** Stage 4 remains active and open at circular-motion drill 1–4. Row 3 is a
  math-readiness queue row, not a stage gate. `current-position.md` unchanged and
  correctly so.

### Exact next independent rep

- **Row 4** — `calculus-links/kinematics-derivatives` (Stage 2).
- **Owed separately:** the true 48–72 h durability check on rows 2–3, Tue–Wed. Cold
  reconstruction of the chain or a transfer problem, no scaffold. **Row 3's pass does
  not substitute for it.**

### Sources and files touched

- `wiki/math-readiness-path.md` (row 3 marked run and passed)
- This log.

---

## 2026-08-18 — Exact Section 54 syllabus received; semester pathway rebuilt

**Session type:** source intake + course-overlay reconciliation. **Not a learning session
— no learner status moved and none should be inferred from this entry.**

### What actually changed

Chris obtained the **exact PHYS 2211 Section 54 Fall 2026 syllabus** direct from Farhan
Islam, one day after the flag #57 escalation email, and placed it in two locations. Both
verified **byte-identical by SHA-256**:

- `raw/syllabus/Syllabus.pdf` — canonical evidence
- `04-SCHOOL\02-Physics I\Syllabus.pdf` — working copy

**It is Chris's section.** The syllabus lists four recitation sections under one lecture,
including **§54, Friday 11:30–12:25, Atrium 1116**, matching CRN 83722. This resolves a
standing ambiguity: **§51/52/53 are sibling recitations of Chris's own lecture**, not
rival sections — which is why the §51 capture paced this course as well as it did from
July 28 onward. §55 (Behera) is a genuinely separate lecture.

### The five material findings

1. **Scope shrank by roughly two chapters.** The 15-week schedule never reaches Ch 13.
   Week 4's "Gravitational Force and Free-Body Diagram (5.5, 5.7)" is §5.5 *weight in an
   FBD*, not universal gravitation. **Active path is now Ch 1–12, 15, 16.1–16.3.**
   Stages 13, 14, 17, 18 → durable reference, off the course path.
2. **The equation sheet is provided at every exam.** Closed book, but formulas are in the
   room. **This is the largest teaching consequence in the document.** Value moves from
   formula recall — Chris's known weak channel — to cold classification and setup.
   Derivation reps are unaffected in *frequency* and changed in *purpose*: they now train
   model selection, not insurance against a blank sheet.
3. **AI policy stated and permissive.** Explicitly permitted as a tutoring resource
   (explanations, guided technique, examples, clarification); prohibited in any submitted
   work. The hub's "most-restrictive-until-verified" holding position is retired.
   **WebAssign is graded — never produce a WebAssign answer.**
4. **Grading: exams 45% (4, lowest dropped) + final 30% = 75% on four closed-book
   sittings.** HW 10%, recitation worksheet 10%, quizzes 5%. **No attendance component**
   — the neighbour's 7.5% + 7.5% does not exist here.
5. **Pre-class reading is graded** (reading quizzes via WebAssign/D2L, unannounced in-class
   quizzes), so the one-week-ahead rule is now directly scorable, not just strategic.

### Date corrections — one would have cost marks

| Exam | Old estimate | Real | Drift |
|---|---|---|---|
| 1 | Fri Sep 18 | **Mon Sep 21** | +3 days, and now includes UCM 6.1–6.2 |
| 2 | Fri Oct 16 | **Mon Oct 12** | **−4 days** |
| 3 | Fri Oct 23 | **Wed Nov 4** | +12 days |
| 4 | Fri Nov 6 | **Wed Nov 18** | +12 days |
| Final | Dec 9 *or* Dec 10 | **Wed Dec 9, 8–10 AM** | resolved |

**Test 2 is the one that mattered:** the old pathway scheduled the Exam 2 sweep for
Oct 12–18 — the week the exam actually falls, on the Monday.

### Defects found in the §54 syllabus itself

1. Header says lecture meets M/W/**Th**; all 45 scheduled dates are M/W/F and the registrar
   agrees. **MWF is correct** — recorded so no later session "corrects" the vault.
2. Unit exams print at **10:20–11:15**, the §51/52/53 recitation slot, not §54's Friday
   11:30. Dates land Mon/Mon/Wed/Wed, so it is not any one section's slot. **Unresolved —
   day-one question.** No timetable conflict either way.
3. Email Policy prints `kpemasir@kennesaw.edu`; the instructor block gives `fislam7@`.
   Boilerplate debris — **use `fislam7@`**, which is what Chris used on Aug 17.
4. Nov 2 reading prints "11.2 – 1.4" → read as **11.2–11.4**.

### Stage / frontier movement

- **None.** This was source intake. Stage 4 remains active and open at circular-motion
  drill 1–4; math rows 2–3 remain `passed (immediate)` with the durability check still
  owed. `current-position.md`'s learner-truth sections were not touched — only its course
  baseline and scope target, which are course overlay, not learner evidence.

### One consequence for tomorrow

**Aug 19's prep block changed.** It was Stage 13 Universal Gravitation — a chapter this
course does not teach — scheduled the day before uniform circular motion, which *is*
taught (Fri Sep 18), *is* on Unit Exam 1, and *is* the exact drill Stage 4 has been open
at since July. Replaced with **[[drills/circular-motion-drill]] 1–4 cold**.

### Governance note — what was deliberately not done

`raw/syllabus/PHYS 2211 51 (83719) …md` was **left in place.** `raw/` is immutable capture
evidence, not a working set; archiving it to tidy would destroy the record that made
July–August pacing defensible — flag #97's exact failure mode in a new costume. Stale
sources are demoted **in pointers**, never removed. The two `04-SCHOOL` working copies
*were* archived, because they sat in the same folder as the real `Syllabus.pdf` and that
adjacency was the actual confusion risk.

### Sources and files touched

- **Source:** `raw/syllabus/Syllabus.pdf` (read-only; nothing written under `raw/`)
- `wiki/semester-pathway.md` — **rebuilt**
- `wiki/pacing-trigger-map.md`, `wiki/current-position.md`, `wiki/source-map.md`,
  `wiki/syllabus-coverage-ledger.md`, `OPERATIONS.md`
- `00-BRAIN\hats\HAT_PHYSICS.md`, `00-BRAIN\SYSTEM_FLAGS.md` (#57 half closed, #16 dated),
  `NOW.md`, the Aug 17–23 weekly plan
- `04-SCHOOL\SEMESTER_MAP.md`, `04-SCHOOL\SYLLABUS_STATUS.md`
- Archived: `99-ARCHIVE\ARCHIVED_2026-08-18_PHYS_neighbour_syllabi\` (2 files + README)

## 2026-08-18 — Math row 2 durability check: **PASSED → `proven (durable)`**

### Elapsed time, stated honestly

Row 2's immediate pass was **Aug 16 night**; this ran **Aug 18 ~14:00**, so elapsed was
**roughly 41 hours, not a strict 48.** The owner table's window (Aug 18–19) sanctioned the
day, and the substantive criterion — **two sleeps** — was met. Recorded rather than rounded up.

### Cold evidence

Given `a(t) = 12t − 4`, with `v(0) = 3 m/s` and `x(0) = 5 m`. No notes, no formula sheet.

```
v(t) = 6t² − 4t + 3          C₁ = 3
x(t) = 2t³ − 2t² + 3t + 5    C₂ = 5
```

Both integrations correct on the first attempt. **The load-bearing step landed: C₁ was carried
forward as the `3t` coefficient of the second integration** rather than left as a dangling
`C₁t`. That is the same move row 3 recorded on Aug 17 as deliberate substitution rather than
recall, and it repeated cleanly two days later without scaffold.

**Explain-back:** C₁ is initial velocity, C₂ initial position, *"both inside the measured
frame"* — a better answer than the one asked for, because it names frame-dependence unprompted.
Constants cannot come from `a(t)` alone because acceleration only describes how velocity is
changing, leaving a family of curves. **This is the July 30 gap ("why is C = 3 here"), and it
is closed.**

**Stretch probe — non-zero boundary condition.** Same `a(t)`, told `v(1) = 10` instead of
`v(0)`. Answer `C₁ = 8`, correct: `6 − 4 + C₁ = 10`. Passed. Harder route, same meaning —
C₁ is still v(0), but had to be reached from a condition elsewhere on the curve.

**Units on coefficients:** `2 m/s³`, `2 m/s²`, `3 m/s`, `5 m`. Passed after one term was
modelled. The intended trap — that the two `2`s are different physical quantities sharing a
digit — was seen once the form was shown.

### Defect logged: chained equals

Chris wrote `v(t) = 6t^2 - 4t + C_1 = 3`, which asserts `v(t) = 3`. Conceptually he was
correct; the notation is not. Corrected in session to two separate statements. **Exam risk,
not a comprehension risk** — closed-book, fast-reading grader, §54 exams are 45% of the grade.

### ⚠ Correction to this session's own diagnosis — AI-side

Mid-session this session proposed that Chris "has the understanding but does not produce the
verification move," generalising from the units question. **Chris corrected it:** *"on not
producing the move I did not understand the question, so I didn't even think that was what you
were on about."*

**Reclassified: the units item is an AI-side question-clarity defect, not a learner miss.**
The question was asked twice and skipped twice before `HAT_PHYSICS` Method 3 fired ("if Chris
skips a requested output twice, the problem is the request, not the answer"). The rule worked —
it just should have fired one ask earlier. **Do not carry the "doesn't produce verification
moves" generalisation forward; it rested on a question he could not parse.**

### 🔴 Chris's own ruling on the reasonableness check — supersedes the Aug 17 diagnosis

Chris, unprompted: *"my form is 100% careless, I need improvement on this I can't count the
amount of times I dropped a value and gotten an answer wrong."*

The Aug 17 entry attributed the third drop to *missing form, not carelessness*. **The learner's
own account overrides it.** Both are now on record; his is the operative one.

**Why this raises the habit's value rather than lowering it.** Dropped and mis-substituted
values are exactly the error class a second-road check catches — see 2026-07-27 (`g = 0.8` for
`9.8`; total `v₀` substituted for the direction-specific component, twice in one problem). The
reasonableness check is not generic good practice for Chris; it is **the specific antidote to
his documented error mode.** With the §54 equation sheet provided at every exam, marks will not
be lost to unknown formulas — they will be lost to unchecked substitutions.

### Symbolic form of the check — modelled for the first time

The check had only ever been modelled numerically ("the same number by a different road"),
which is likely why it never transferred to a symbolic rep. Modelled here:

```
v(t) = 6t² − 4t + 3
d/dt →  12t − 4  = a(t) ✓
```

Two lines. It caught nothing today because the work was right — which is what a passing check
looks like. **Watch on row 4; still do not re-explain it.**

### Teaching-method finding — record and reuse

Chris: *"that explanation from above on the units was perfect for me for understanding."*
The format that worked: **model one term completely, show that the units live in the
coefficient rather than the variable, then ask for the remaining terms.** He produced all three
instantly and correctly. Matches this hub's `physical situation → skeleton → guided rep →
transfer` loop and `HAT_PHYSICS` Method 3. Routed to
`03-WIKIS\EDUCATION\wiki\methods\hat-performance-log.md`.

### Frontier verdict

**Row 2 → `proven (durable)`.** Removed from the open durability table in
`current-position.md`. **No stage moved** — Stage 4 remains open at circular-motion drills 1–4.

**Row 3 not run.** Its immediate pass was Aug 17 midday, so its 48-hour floor is **~midday
Wed Aug 19**. Running it today would measure short-term memory — the exact error row 3's own
entry was written to avoid.

### Next exact action

Row 3 durability check from ~midday Aug 19, or row 4
(`calculus-links/kinematics-derivatives`) now, which is the held frontier item and the
designated observation point for the reasonableness check.

## 2026-08-19 — Root-level calculus-bridge scratch file relocated into the hub

### Outcome

- `.ROOT\needs_for_physics.md` — a loose root-level file since the July 30 – Aug 23
  calculus-physics bridge sprint — now lives at
  `worked-examples\projectile-first-principles-example.md`. **Chris directed the move; the
  destination choice was this session's.**
- **Moved with `git mv`, so its commit history survives** (originated `95668a0`). It was
  tracked, not untracked, which is why it never appeared in a `git status` sweep and part of
  why it sat at the root for three weeks.

### Evidence

*System session — files changed and checks run.*

- Placement authority: `WHERE_IT_GOES.md` § `04-SCHOOL` vs `03-WIKIS` tiebreaker — *"Did KSU
  give it to me, or did we make it?"* Chris's own Gemini-assisted derivation is **we made it**
  → `03-WIKIS\PHYSICS\`, not `04-SCHOOL\02-Physics I\`.
- Folder choice: the file's own header named **`calculus-links/` or `worked-examples/`**.
  Chose `worked-examples/` — the artifact is a complete worked problem, `calculus-links/` pages
  are single-concept bridges on a fixed template (`authoring-standards.md` § Calculus-Link
  Page), and `calculus-links/2d-kinematics-components.md` already owns that concept.
  **The Aug 12 update plan had recorded `calculus-links/` as the destination; this differs, and
  the reason is on the page.**
- Frontmatter corrected: `timeline: now` → `reference`, `status: active-scratch` → `draft`.
  It could not keep claiming scratch status in a permanent home.
- Numerical result independently checked: `t = √(2·1.20/9.80) = 0.4949 s`,
  `R = 2.50 × 0.4949 = 1.24 m` ✓. Derivation is sound.
- Files: the moved page · `index.md` (folder count line) ·
  `calculus-links\kinematics-derivatives.md` (cross-link) · this log.

### Capability/status movement

**None. No learner evidence was produced and no stage moved** — this is a filing action.
Stage 4 remains open at circular-motion drills 1–4; row 3's durability check is still owed.

### Errors, uncertainty, or residual risk

- **The prose is Gemini's and has not been rewritten to this hub's authoring standards.**
  Marked in-file rather than silently normalised — it is Chris's study record in his own
  working words, and rewriting it would destroy what makes it his. **Risk accepted and
  labelled:** a future session could mistake it for a hub-authored reference page. The
  in-file provenance block is the control.
- **No content was verified beyond the arithmetic.** The physics reads correctly, but a
  line-by-line check against Serway was not run.
- The page overlaps `worked-examples\projectile-cliff-example.md` in subject but not in
  method — that one pattern-matches to standard equations, this one derives them. Kept
  separate deliberately; the contrast is the point.

### Exact next independent rep

Unchanged: **row 3 durability check from ~midday Aug 19**, or row 4
(`calculus-links/kinematics-derivatives`) — which now links to this page.

### Reusable-asset candidate

No.

### System-learning candidate

**Nomination, not yet a flag.** A tracked file sat at the vault root for three weeks after
being flagged as misplaced twice (2026-08-02 review; Aug 12 update plan). Both times the
correct action — ask Chris — was taken, and both times the answer never came back and nothing
re-raised it. **The gap is that "asked Chris, awaiting answer" has no holder and no check
moment**, which is `AGENT.md` Execution Discipline 7's exact subject. Worth raising at the
weekly if a second instance appears; `claude_and_chris_direction.md` was flagged in the same
Aug 2 pass and **is still at the root**, so a second instance may already exist.

### Sources and files touched

`needs_for_physics.md` → `worked-examples\projectile-first-principles-example.md` ·
`wiki\index.md` · `wiki\calculus-links\kinematics-derivatives.md` · `wiki\log.md`

## 2026-08-19 (12:00–13:xx) — Math row 3 durability check: **MISS**, repaired same session; work-energy bridge built

### Row 3 durability check — `passed (immediate)` 2026-08-17 → **MISS 2026-08-19**

Run at 12:00, on its floor (48 h from the Aug 17 midday pass), cold, no formula sheet.

**Produced unprompted, correct:** `a = a₀` · `v = a₀t + v₀` · `x = ½a₀t² + v₀t + x₀`, with
`C₁` recovered as `v₀` and `C₂` as `x₀`, plus a correct statement of the mechanism
("obtained by integration back up the chain with respect to time").

**The miss:** the gate asks for **three** kinematics equations; Chris produced the premise
plus two. `v² = v₀² + 2aΔx` was absent, and his summary sentence — *"these are **all**
obtained by integration"* — asserted completeness over an incomplete set.

**Error class: concept — set structure.** Not algebra, not calculus mechanics. This is the
catalogued `v²` failure mode (`HAT_PHYSICS` § Failure modes) **arriving from the other
side**: he did not misclassify `v²` as a third integration, he omitted it while describing
the set as complete. Same root — what is not encoded is that the set has three members and
one has a non-integral origin.

**Repair, one structural cue, no content given.** Asked how many times `a = const` can be
integrated before the chain runs out. Answer: *"twice, and the third is algebra and
substitution, so `v² = v₀² + 2a(x − x₀)` or `Δx`."* Correct mechanism, correct equation,
correct `(x − x₀)`/`Δx` equivalence. **Recorded as a miss regardless** — the written bar is
a cold rebuild *with no scaffold*, and the standard does not grade scaffolds by size (same
rule applied to the 2026-08-01 Python quiz).

**Verdict: `owed`, new durability window Fri Aug 21 – Sat Aug 22.** Per the clearing rule, a
failed durability check does not erase the immediate pass; it reopens it.

**The reopened rep is re-aimed and is not a re-list.** §54 provides the equation sheet at
every exam, so reciting the set earns nothing on Sep 21 — *selecting* from it earns
everything. New form: a problem with no `t` given and no `t` wanted; Chris names the equation
and states that the absence of `t` is what selects it. Cold, no sheet.

### Same session, Chris-requested — `v² = v₀² + 2aΔx` derived and bridged

Chris asked to re-run the derivation "to make it stick." Worked phase (per the
worked → faded → cold ladder); faded and cold are still owed.

- **Road 1** — solve `v = v₀ + at` for `t`, substitute into `Δx = v₀t + ½at²`, clear by `2a`,
  cancel `2v₀v` against `−2vv₀`.
- **Road 2** — `v_avg = (v + v₀)/2` for constant `a`, times `t = (v − v₀)/a`, difference of
  squares. Two lines.
- **Reasonableness check MODELLED, twice** — the two roads, and an `F = ma` cross-check on the
  wheelbarrow case. This closes the "modelled once before asking" precondition in
  `HAT_PHYSICS` § Method 3. `NOW.md` records the habit as still not firing on written work;
  it has now been demonstrated, not merely requested. **Watch on row 4.**
- **Bridge built:** `×½m` → `½mv² = ½mv₀² + FΔx`, i.e. the work-energy theorem, with the
  physical reason `t` drops out (energy is indifferent to duration, only to distance).

### Three bridge misses — all one gap, and it is the hub's named gap

Chris nominated the energy step himself as the unfamiliar one. Each miss below is
**kinematics → dynamics, the point where mass enters** — `OPERATIONS.md` § Teaching contract's
identified gap, in his own words *"connecting to the physics is still hazy."*

1. **"multiplying by mass gives us the density of the object"** — density is mass/volume.
   Corrected with same-mass/different-density disambiguation; mass re-anchored as **inertia,
   the handle force grabs**.
2. **"work is more for the loaded wheelbarrow"** — no `m` in `W = FΔx`. Same force, same
   distance, **same work**. Corrected: mass is not in the work, mass is in the kinetic
   energy; `v = √(2FΔx/m)` is what differs.
3. **"time... only affects the work going into lifting"** — time is in no work term. Level
   travel means zero vertical displacement and gravity does zero work regardless of duration.
   The quantity he was actually describing is **power** (`W/t`) — correct instinct, wrong
   label. First half of that answer was right and unprompted: *"the time changes but that
   doesn't affect the work done."*

**Session judgment:** calculus and algebra were clean throughout; every miss was on the
bridge. Stopped adding after the third rather than pushing — escalation is earned by a
demonstrated miss, and three in one sitting on one bridge is the signal to let it set.

### Frontier verdict

**Stage 4 unchanged — still open at circular-motion drills 1–4.** Nothing this session
advanced it. Row 3 reopened. Row 4 unrun.

**Row 4 narrowing (recorded so the block is not spent twice):** two of its three practice
problems duplicate proven ground — Problem 1 is polynomial differentiation, Problem 2 is
`a(t) = 6t` integrated, an easier version of row 2's Aug 18 durable pass (`a(t) = 12t − 4`
with non-zero boundary conditions). **Row 4's unique content is Problem 3 (displacement as
area under a v–t graph) and the average-vs-instantaneous distinction** — neither
demonstrated, and the page itself calls graphical interpretation the most important Stage 2
intuition. Run row 4 aimed at the graph; half a block, not a full one.

### One exact next rep

**PHYS: circular-motion drills 1–4, cold** — closes Stage 4, blocked since July, and
6.1–6.2 sits on Unit Exam 1 (Mon Sep 21). **This outranks row 4.**

### Sources and files touched

`wiki\current-position.md` (durability table) · `wiki\log.md` ·
`wiki\calculus-links\kinematics-derivatives.md` (read only)

## 2026-08-19 — Exact §54 Math-First Semester Plan and Routing Repair

### Objective

Turn the exact Section 54 syllabus and the existing Physics wiki into one dated,
math-first execution plan from today through the final, and repair stale routing
before the semester begins.

### Built

- Added [[phys-2211-17-week-math-first-plan]]: exact lecture-by-lecture readings,
  printed and split-file local PDF pages, math lens, weekly output gates, exam
  sweeps, workload, academic-integrity boundary, and a 17-week sequence.
- Preserved two syllabus defects transparently: Sep 4 needs §§4.3–4.5 because
  §4.3 is projectile motion; Nov 2 means §§11.2–11.4.
- Made the current next rep explicit: §§6.1–6.2 plus circular-motion drills 1–4.

### Repaired

- Corrected [[textbook-page-map]] from the stale Ch 1–13/15–17 neighbor scope
  to exact §54 scope and documented how global PDF pages convert to local pages
  in every split file.
- Corrected [[current-position]] so Stage 6, not off-course Stage 13, follows
  Stage 5; refreshed [[index]] routing and its stale July next action.
- Corrected [[source-map]] instructor/course truth and its stale chapter-scope
  table; added the Sep 4 defect to [[semester-pathway]].
- Repaired renamed problem-type links for circular motion, work/energy, and
  collisions, plus the Stage 10 rotational-calculus link.
- Re-scoped Stage 12 to assessed §§12.1/12.3, made §§15.6–15.7 required in Stage
  15, and limited Stage 16's active gate to §§16.1–16.3.

### Learner truth

No stage advanced. Stage 4 remains open at circular-motion drills 1–4; Row 3's
durability check remains due Aug 21–22. This was curriculum and routing work,
not learner evidence.

### Next exact rep

Read §§6.1–6.2 at `0101-0200` local pp. 58–64, then complete
[[drills/circular-motion-drill]] Problems 1–4 cold.

## 2026-08-21 — Row 3 missed again; circular cold gate exposed prerequisite rust; printable formula sheet built

### Cold evidence

- **Math row 3 — miss.** Given 14.0 m/s → 26.0 m/s over 60.0 m, Chris first
  selected `a = (v_f - v_0) / delta_x` and answered 5 m/s². The expression has
  units s⁻¹, not acceleration, and the arithmetic reversed the division. After a
  units cue he answered 4.0 m/s² and supplied the correct no-time relationship,
  `a = (v_f² - v_0²) / (2 delta_x)`. The repair was correct; the cold selection
  was not. **Error class: equation choice/units; execution after recognition.**
- **Circular-motion Problem 1 — miss.** Chris correctly computed 5.0 m/s². The
  direction was described as "towards the curve" instead of toward the center,
  and static friction was not named as the real inward force until correction;
  the follow-up still tied the force to tire angle. **Error class: concept recall —
  real force versus centripetal role.**

Chris reported that he had not reviewed these equations in more than six months
and asked for reading plus a lesson. The cold gate therefore stopped. Problem 2
became worked lesson material and is no longer valid as a cold item. Problems 1–2
need fresh changed-parameter replacements after instruction; Problems 3–4 remain
untouched cold.

### Outcome and route

- No stage advanced. Stage 4 remains open.
- Row 3 reopened for **Sun Aug 23 – Mon Aug 24** with a fresh no-time transfer.
- Read §4.4 (printed pp. 81–83) and §§6.1–6.2 (printed pp. 128–134), then run
  worked → faded → fresh cold transfer.

### Reusable study asset

Built and visually verified the six-page
`04-SCHOOL\02-Physics I\work\exam-prep\output\pdf\PHYS_2211_Section_54_Master_Formula_and_Selection_Sheet.pdf`.
It follows the exact §54 scope (Chapters 1–12, 15, and §§16.1–16.3), uses
conventional mathematical notation, and pairs equations with model-selection cues,
conditions, and units. Chapters 13, 14, and 17 are explicitly excluded. This is a
study aid; the instructor-provided exam equation sheet remains authoritative.

### Return packet

- **Outcome:** two cold misses classified; repair route and study instrument built.
- **Evidence:** this entry, [[current-position]], and the printable PDF above.
- **Capability movement:** none; Stage 4 remains open.
- **Reusable asset:** compare the PDF against the official instructor sheet when it
  appears in D2L.
- **System-learning candidate:** terminal LaTeX was unreadable; the Codex profile now
  requires plain-text equations in terminal chat and reserves rendered notation for
  documents and compatible interfaces.

## 2026-08-22 — Circular-motion Problems 3–4 run; the Aug 21 diagnosis was wrong and is corrected here

**Run at Chris's direction** — *"we need to get the physics thing out of the way even if
it is a fail as it is holding things up."* Stage 4 has been the held frontier since July.

### Aid check, before the learner (`CASTLE\OPERATIONS.md` § Reviews 4c)

- `concepts/uniform-circular-motion.md` cites §4.4 as **pp. 96–100**; [[current-position]]
  and the miss log say **printed pp. 81–83**. PDF-page vs printed-page mismatch — the same
  shape as the TCOM 353-vs-634-page trap. **Recorded, not yet fixed.**
- Drill Problem 3 is dressed as a satellite orbit. **Ch 13 is not on this course**, but the
  problem hands over `r` and `v` and asks only for the period, so no gravitation is
  required and it is legitimate as written. It is still the weakest of the four as a §54
  rep — one substitution, no situation recognition.
- `drills/circular-motion-drill.md` remains `status: draft`.

### What Chris did

Both problems were run against a three-part answer requirement stated up front: the
number with units, **the direction of the acceleration**, and **the real force supplying
it**. That requirement is row 5's re-aim.

- **Problem 3 — cold, unaided.** `T = 5.59 × 10³ s`, 1.55 h per orbit. Correct, first
  attempt, **and the significant figures were correct** — three in, three out, no
  calculator-digit dump. That is one of this hat's listed failure modes not firing.
- **Problem 3, the other two parts — correct, but only after being asked again.**
  Acceleration inward; **gravity** named as the real force. Both right, immediately, with
  no hesitation and no scaffold beyond the question itself.
- **Problem 4 — cued, not cold.** Chris stopped: *"I am dropping the ball on the fourth
  problem, don't recall this information."* One cue was given — *what is physically
  touching the ball, and that one thing is the entire net inward force* — after which he
  produced **8.16 m/s**, correct with correct sig figs.
- **One label crossed:** 8.16 m/s was reported as the satellite's speed; it is the ball's.
  The satellite's speed was a given. Work correct, tag slipped. Noted once, not treated as
  an error class.

### The correction — this is the entry's real content

**The 2026-08-21 error class was wrong, and logging it forward unchanged would have
produced a false gap and a wasted week.**

Aug 21 recorded *"concept recall — real force versus the centripetal role,"* and prescribed
reading §4.4 and §§6.1–6.2 plus a worked → faded → cold rebuild. **Today shows the concept
recall is intact.** Chris named gravity as the inward force on an orbiting satellite
instantly — the harder case of the two, because there is no contact force to point at.

What actually fails is narrower: **he does not volunteer direction and the real force
unless the answer is explicitly asked for them.** Twice now — Aug 21 and Aug 22, five days
apart, same axis. That is an **answer-completion habit that is not firing**, structurally
identical to the standing reasonableness-check row already open in
`04-SCHOOL\miss-log.md`, and it closes the same way: by firing unprompted, not by being
re-explained.

**Consequence for the plan:** the two-section reading block prescribed on Aug 21 is
**not needed** and is withdrawn. The re-aim is one problem, not a chapter.

### Instruction given before the cold run

A 90-second derivation, on Chris's own pathway (calculus relationship → derive → connect
back): `r_vec(t) = r(cos wt, sin wt)`, differentiate twice to `a_vec = -w^2 r_vec`, so the
acceleration is antiparallel to the position vector — **the minus sign is the direction**,
rather than a remembered rule. Plus the distinction that `mv^2/r` is the left side of
`sum F = ma`, so centripetal is a **role** something real fills, never a force drawn on a
free-body diagram.

### Outcome and route

- **No stage advanced. Stage 4 remains open** — Problem 3's parts 2–3 were prompted and
  Problem 4 was cued, so neither meets the cold-with-no-scaffold bar.
- **Problems 3 and 4 are now consumed as cold items.** A fresh changed-parameter problem is
  required for the next attempt.
- **Row 3's durability check is untouched by this session** and remains due **Sun Aug 23 –
  Mon Aug 24** on a fresh no-time transfer.
- **Next rep (one problem, not a block):** a cold circular-motion problem in an unfamiliar
  setup — banked curve, conical pendulum, or vertical-loop bottom — with **no reminder that
  direction and the real force are wanted.** The number is not what is being tested. The
  gate is whether the three-part answer arrives complete, unprompted.

### Return packet

- **Outcome:** Stage 4 exercised and held open; the Aug 21 error class corrected on
  evidence; the prescribed reading block withdrawn as unnecessary.
- **Evidence:** this entry, [[current-position]] § Active Unit, `04-SCHOOL\miss-log.md`
  row 5.
- **Capability movement:** none. Physics stays `building` at Stage 4.
- **Reusable asset:** none this session.
- **System-learning candidate:** **a miss classified once should be re-tested before its
  prescription is scheduled.** Aug 21's class was recorded from a single failed rep and had
  already produced a reading assignment and a lesson plan; one cold question on Aug 22
  falsified it. This is the *learner-side* instance of the aid-check rule the hub already
  runs — check the diagnosis before spending a week on the treatment.
