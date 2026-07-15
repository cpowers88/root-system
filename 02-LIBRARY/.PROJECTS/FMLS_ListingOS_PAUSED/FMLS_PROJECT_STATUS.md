---
type: project
tags: [parked, project]
---

# ListingOS / FMLS Packet Automation — Project Status
#FMLS 

## Parked Project | Reference Snapshot

> **Current vault status — July 15, 2026:** parked. The May 25 operating model
> below is historical project state, not current `.ROOT` authority. Resume only
> through a fresh CASTLE/current-strategy gate and reconcile external locations first.

### Last Synchronized: 2026-05-25 | Aligned with: GitHub listing-packet-clean1 @ c5c940b

---

## SYSTEM ROLE DEFINITION

This document resides in the local **`C:\Users\chris\.ROOT`** workspace — the
master file layer, cloud-backed by Google Drive. Per the three-tier system protocol:

- **Local `.ROOT` (this file):** Long-term storage, archival reference, conceptual documentation
- **Notion:** Active operational status, current session tasks, project tracking
- **GitHub (`listing-packet-clean1`):** Complete production code, versioned history

**Routing rule:** Operational status → Notion. Code → GitHub. This document → local
`.ROOT` reference only.

---

## PRODUCT DEFINITION

**ListingOS** is an end-to-end listing packet automation system for real estate agents. The system's objective is to reduce the per-listing administrative burden from 45–90 minutes of redundant data entry to a single structured intake event, from which all downstream documents — the FMLS packet, GAR contractual listing agreement, comp analysis, and seller follow-up correspondence — are generated programmatically with human review gates at appropriate confidence thresholds.

**Primary target (Phase 1):** Internal validation — agent (Heather Cote, Mark Spain Real Estate) uses the tool on real listings and confirms the workflow reduces friction.

**Secondary target (Phase 2):** Atlanta agent market — high-volume teams, REO specialists, fix-and-flip investors. Pricing model: $49–99/month per agent, $199–399/month team license.

---

## CURRENT STATUS — 2026-05-25

| Component | Status | Location | Notes |
| --- | --- | --- | --- |
| FMLS PDF fill engine (PyMuPDF native) | ✅ **OPERATIONAL** | GitHub `core/listing_intake_pipeline.py` | 102 commits, 10 merged PRs |
| Field registry and alias layer | ✅ **OPERATIONAL** | GitHub `core/pdf_field_registry.py` + `core/generated_registry.py` | Known ID drift — compatibility alias fix needed |
| JSON-to-PDF CLI | ✅ **OPERATIONAL** | GitHub `scripts/fill_fmls_from_json.py` | Confirmed working on 25 Fireside fixture |
| Notes extractor | ✅ **OPERATIONAL** | GitHub `scripts/run_notes.py` + `core/notes_extractor.py` | Added May 16 — not yet chained to fill CLI |
| Flask web UI (`/api/generate`) | 🔶 **NEEDS VERIFICATION** | GitHub `app.py` | Route exists, wired to same pipeline; launch not confirmed |
| Test suite | 🔶 **PARTIALLY STALE** | GitHub `tests/` | `test_fill_fmls_from_json_cli.py` reliable; `test_native_mvp_readiness.py` has stale assertions |
| 25 Fireside fixture data | ✅ **AVAILABLE** | GitHub `25_fireside_ct_packet_extract_v01.txt` (1,484 lines) | Full listing agreement extracted |
| Corrected reference PDFs | ⬜ **LOCAL ONLY** | `C:\Users\chris\projects\listing-packet-clean1\outputs\25_fireside_ct\` | Not in repo per `.gitignore` |
| Wife validation (Phase 1 gate) | ⬜ **NOT YET DONE** | — | **Critical path item. Nothing productizes until this happens.** |
| GAR contract fill | ⬜ Phase 2 | — | Not started |
| Comp analyzer integration | ⬜ Phase 2 | — | POC exists separately |
| iPad intake form | ⬜ Phase 3 | — | Not started |

---

## TECHNICAL ARCHITECTURE SUMMARY

### Data Flow (as implemented)

Appointment notification (address, seller name, date)
↓
scripts/run_notes.py — raw agent notes (.txt) → structured_extract.json
↓
scripts/fill_fmls_from_json.py — JSON → normalized payload → PDF widgets
↓
core/listing_intake_pipeline.run_listing_pipeline()
↓
`outputs/run_<timestamp>/`
draft_native_filled.pdf
final_listing_packet.pdf  [gated on production readiness]
draft_native_filled_report.csv
visual_review_checklist.md

### Key Engineering Decisions

- **PDF fill method:** PyMuPDF (fitz) native AcroForm widget writer. Not pypdf overlay (deprecated). Not reportlab. Direct widget value assignment using exact field names extracted from the FMLS master template.
- **Confidence and review gating:** Fields auto-fill at high confidence. Uncertain values produce review rows, not PDF fills. Final packet gate requires production-ready status.
- **Hard exclusions (permanent):** Room detail section (pages 3–4), page 8 remarks. These are enforced in code, not just documentation.
- **Data trust hierarchy for 25 Fireside:** Wife-reviewed corrections > listing agreement packet > public records > AI inference (review only, never auto-fill).

---

## REPOSITORY STATE — 2026-05-25

- **Repo:** `cpowers88/listing-packet-clean1` (Private)
- **Branch:** `main` | **HEAD commit:** `c5c940b` (May 21, 2026)
- **Total commits:** 102
- **Safe fallback tag:** `safe-native-pipeline-attached-20260508` (May 8)
- **Working CLI:** `.\.venv311\Scripts\python.exe .\scripts\fill_fmls_from_json.py .\inputs\25_fireside_ct\fmls_candidate_payload_v01.json`

---

## KNOWN ISSUES (DOCUMENTED IN REPO)

1. `tests/test_native_mvp_readiness.py` — stale assertions against old registry IDs and Flask mock signature. Does not block operation; blocks clean test run.
2. `core/accepted_terms.py` — duplicate `kitchen_features` dictionary block. Second block overwrites first at runtime.
3. Mapping ID drift: `pantry_walkin` ≠ `pantry_walk_in` ≠ `kitchen.has_walk_in_pantry`. Documented in `docs/FIELD_MAPPING_REDESIGN_PLAN.md`. Compatibility alias fix is next after wife validation.
4. Legacy overlay system files remain in repo (`core/mappings.py`, `pdf/overlay_text.py`, etc.) — dead code, pending safe removal per `docs/ARCHITECTURE_AUDIT.md`.

---

## NEXT MILESTONE

**Objective:** Wife completes one real listing using the tool without asking for help.

**Steps (in order):**

1. Run CLI on 25 Fireside JSON → produce filled PDF
2. Sit with wife — watch her go through the PDF against the handwritten notes
3. Log every friction point in `14-BUSINESS & CONSULTING/Field Notes/`
4. Fix the 5 items in known issues
5. Decision: does this productize for Atlanta agents or stay internal?

---

Drive file | Part of Chris Powers Second Brain | GitHub: listing-packet-clean1 | Notion: Projects > FMLS App | Sync: 2026-05-25
