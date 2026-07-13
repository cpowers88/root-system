---
type: project
tags: [parked, project]
---

# listing-packet-clean1 — README & Known State
#FMLS 
## Repository: FMLS Listing MVP | cpowers88/listing-packet-clean1
### Status as of: 2026-05-25 | Branch: main | Commit: c5c940b

---

## SYSTEM ROLE

This repository is the **Git layer** of a three-tier personal knowledge and production system.
**Location correction (July 13, 2026):** the `.ROOT` layer is now the local
`C:\Users\chris\.ROOT` workspace, cloud-backed by Google Drive; it is not a
Google Drive working tree.

| Tier | System | Role |
|---|---|---|
| 1 | Local `.ROOT` on C: | Master file storage — long-term, archival, conceptual; cloud-backed by Google Drive |
| 2 | Notion (Second Brain) | Active operations layer — current projects, tasks, status |
| 3 | GitHub (this repo) | Production code layer — complete programs, versioned history |

**Sync rule:** Information flows local `.ROOT` → Notion → GitHub. Code lives only
in the repository. Status lives in Notion. Long-term reference lives in the local
`.ROOT` workspace and its cloud backup.

---

## WHAT THIS IS

A Python/Flask application that automates the generation of FMLS (First Multiple Listing Service) residential listing packets for real estate agents. The system accepts raw property data (structured JSON or agent appointment notes in plain text), normalizes it through a field mapping and alias layer, fills a 9-page FMLS master PDF template using PyMuPDF's native AcroForm widget system, and produces a draft packet with audit reports and a human review checklist.

**Product vision:** One intake event fills everything — FMLS packet, GAR contracts, comp analysis, seller follow-up questions. No double entry. No paper chaos.

**Current scope:** FMLS PDF fill pipeline only. All other modules are future-phase.

---

## KNOWN STATE — 2026-05-25

### Repository Metrics
- **Total commits (main):** 102
- - **Branches:** 13 (5 active, rest merged or stale)
-  - **Closed PRs:** 10 (all merged)
  - - **Open PRs:** 0
  - - **Tags/Checkpoints:** 2
   - - **Primary language:** Python (97.1%), HTML (2.9%)
   - - **Test property:** 25 Fireside Ct NW, Cartersville, GA 30120
           
 - ### Saved Checkpoints (Tags)
            - | Tag | Commit | Description |
            - |---|---|---|
            - | `safe-native-pipeline-attached-20260508` | d52dcac | Stable native pipeline post-May 8 stabilization |
            - | `safe-before-claudecoded-compare` | 3a89c74 | Last known-good state before AI-assisted code pass |
           
  - ### Branch Inventory
            - | Branch | Status | Purpose |
            - |---|---|---|
            - | `main` | Active — HEAD | Production branch. All work merged here. |
            - | `qa-25-fireside-field-corrections` | Active — merged via PR #11 | QA pass for 25 Fireside property |
            - | `packet-stabilization-field-inventory` | Active | Field inventory and stabilization work |
            - | `native-acroform-filler` | Active | Native PyMuPDF filler development |
            - | `acroform-filler-fixes` | Active | Bug fixes for AcroForm fill path |
            - | `field-inventory-full-test-fixture` | Active | Full-field test fixture (merged via PR #10) |
           
            - ---

## ACTIVE PIPELINE — HOW IT WORKS

  ### Data Flow
            ```
            Raw input (JSON payload OR plain-text appointment notes)
                   ↓
            core/raw_file_ingest.py + core/raw_listing_parser.py
                   ↓
            core/native_value_normalizer.py  [alias resolution, synonym mapping, warnings]
                   ↓
            core/pdf_field_registry.py + core/generated_registry.py  [widget name lookup]
                   ↓
            core/listing_intake_pipeline.native_fill_pdf()  [PyMuPDF AcroForm writer]
                   ↓
            outputs/run_<timestamp>/
                draft_native_filled.pdf         ← Primary output
                final_listing_packet.pdf        ← Created only when production-ready
                draft_native_filled_report.csv
                validation_report.csv
                final_validation_report.csv
                native_text_capacity_audit.csv
                visual_review_checklist.md
            ```

   ### Entry Points
            ```bash
            # CLI — primary, confirmed working
            .\.venv311\Scripts\python.exe .\scripts\fill_fmls_from_json.py .\inputs\25_fireside_ct\fmls_candidate_payload_v01.json

            # Notes extractor — raw appointment notes to structured JSON
            python scripts/run_notes.py --run-id <property_id> --input notes.txt

            # Web (Flask)
            python app.py  →  POST /api/generate

            # Full verification
            .\.venv311\Scripts\python.exe -m pytest tests/test_fill_fmls_from_json_cli.py tests/test_native_mvp_readiness.py -q
            ```

            ---

 ## HARD EXCLUSION RULES (DO NOT REMOVE)

            The following sections of the FMLS 9-page master template are permanently excluded from auto-fill:

            - **Pages 3–4:** Room Type / Room Dimensions / Room Description / Level fields (all 10 slots)
            - - **Page 8:** Public Remarks, Private Remarks, Directions (handled separately, not through this pipeline)
              - - **Any price or commission fields:** Require human review and explicit source confirmation
               
                - These rules are enforced in `scripts/fill_fmls_from_json.py` via `apply_25_fireside_visual_qa_corrections()`.
               
                - ---

 ## KNOWN ISSUES (DOCUMENTED, NOT BLOCKING)

      1. **Stale test assertions** — `tests/test_native_mvp_readiness.py` expects old registry IDs (`pantry_walkin`, `stone_counters`) and an outdated Flask mock signature. `test_fill_fmls_from_json_cli.py` is the reliable test. Fix: update assertions to match current active registry.
               
     2. **Mapping ID drift** — Three-layer naming problem documented in `docs/FIELD_MAPPING_REDESIGN_PLAN.md`. Legacy IDs (e.g., `pantry_walkin`) differ from active native registry IDs (`pantry_walk_in`) and proposed canonical IDs (`kitchen.has_walk_in_pantry`). Compatibility alias layer planned.
                  
     3. **Duplicate dictionary keys** — `core/accepted_terms.py` has two `kitchen_features` blocks. The second overwrites the first at runtime. Fix pending.
                     
     4. **Legacy overlay system present** — Files in `pdf/overlay_text.py`, `core/mappings.py`, `core/overlay_geometry_profiles.py`, etc. are dead code from the pre-PyMuPDF era. Not on active pipeline path. Do not delete until native coverage is complete.
                        
     5. **`tools/run_full_field_smoke_test.py`** — Broken import/call signature. Do not use.
                           
     6. ---
                           
## NEXT REQUIRED ACTIONS (PRIORITY ORDER)
                           
    1. **Run on Fireside. Get wife to use it.** Execute the CLI on `inputs/25_fireside_ct/fmls_candidate_payload_v01.json`. Produce the filled PDF. Watch a real agent use it. Document friction.
                              
    2. **Fix stale test assertions** — Update `tests/test_native_mvp_readiness.py` to match current active registry without changing production code.
                                 
    3. **Wire notes → fill end-to-end** — Chain `scripts/run_notes.py` output (`structured_extract.json`) into `scripts/fill_fmls_from_json.py` as input. This closes the full loop from appointment notes to filled PDF.
                                    
    4. **Add compatibility aliases** — In `core/native_value_normalizer.py`: map `pantry_walkin → pantry_walk_in`, `stone_counters → stone_counter`. Do not touch the PDF registry.
                                       
    5. **Verify Flask `/api/generate`** — Confirm the web UI launches cleanly and the route produces the same output as the CLI.
                                          
     ---
                                          
   ## FUTURE PHASES (NOT CURRENT SCOPE)
                                          
    - GAR contract auto-fill
    - - Comp analyzer integration (CSV → Claude analysis → pricing recommendation)
    - - iPad/mobile intake form
    - - Productization for Atlanta agent market ($49–99/month per-agent SaaS)
    - - OCR for scanned handwritten notes
    - - Public remarks drafting assistant
                                                       
                                                        - ---

   ## RELATED REPOS (cpowers88 — All Known State 2026-05-25)

   | Repository | Visibility | Description | Last Updated | Status |
   |---|---|---|---|---|
   | `listing-packet-clean1` | Private | FMLS listing MVP (this repo) | 2026-05-21 | **ACTIVE — PRIMARY** |
   | `atlas-python-foundations` | Public | Python learning foundation — KSU CSE 1321 prep | 2026-05-20 | Active — ongoing |
   | `lean1` | Public | First repo — learning Git workflow | 2026-05-18 | Learning artifact |
   | `skills-introduction-to-github` | Public | GitHub Skills exercise | 2026-05-18 | Complete — exercise |
   | `skills-review-pull-requests` | Public | GitHub Skills exercise (PR review) | 2026-05-18 | Complete — exercise |
   | `Repository-name-market-scanner-lab` | Private | Stock scanner / paper trading lab | 2026-05-09 | Paused |
   | `reconciliation-engine` | Private | Python reconciliation engine | 2026-05-08 | Paused |
   | `listing-packet-clean` | Private | FMLS overlay MVP (predecessor to this repo) | 2026-05-01 | **ARCHIVED — superseded** |
   | `real88project` | Private | Early PDF filler (automatepdffiller) | 2026-04-29 | **ARCHIVED — superseded** |
   | `realestate88` | Private | Early real estate experiment | 2026-04-19 | **ARCHIVED — superseded** |
   | `real88project8` | Private | Early real estate experiment | 2026-04-19 | **ARCHIVED — superseded** |

                                                        ---

     *Repository: listing-packet-clean1 | Owner: cpowers88 | Sync date: 2026-05-25 | Aligned with: local `.ROOT` system | Notion Second Brain*
