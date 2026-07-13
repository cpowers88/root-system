---
type: project
tags: [parked, project]
---

# PROJECT REPAIR REPORT — 496 Highpoint Xing
#FMLS 
**Date:** 2026-06-02  
**Status:** Phase 1 complete. Phase 2 (raw scanned PDF extraction) requires API key.

---

## What Was Fixed

### 1. Stale test path — FIXED
**File:** `tests/test_source_loader.py` line 21  
**Old path:** `C:\Users\chris\.00-PROJECTS-v2.0\DATA SETS\496 Highpoint Xing`  
**New path:** `C:\Users\chris\.00-PROJECTS-v2.0\05-PROJECT DATA SETS\496 Highpoint Xing`  
**Impact:** OCR integration tests (Tests 2 and 3) were silently skipping on every run.
They will now execute when the source folder is present.

### 2. `anthropic` SDK — INSTALLED
Installed into `.venv314`. Added to `requirements.txt`.  
This is required for the Claude vision OCR adapter.

### 3. `core/ocr_claude_vision.py` — CREATED (NEW FILE)
New OCR adapter using Claude vision API (`claude-sonnet-4-6`).  
- Uses PyMuPDF to render each PDF page to a PNG at 200 DPI (no Poppler required)
- Sends page images to Claude vision with a structured extraction prompt
- Flags handwritten content with `[HANDWRITTEN]`
- Flags uncertain readings with `[UNCERTAIN]`
- Includes page-level provenance headers: `[SOURCE: filename | PAGE: n | METHOD: claude_vision]`
- Same interface as `core/ocr_tesseract.py` — drop-in replaceable
- Never logs the API key

### 4. `core/source_loader.py` — UPDATED
Added `claude_vision` as a supported OCR adapter alongside `tesseract`.  
Updated the install/help message to explain both options.

### 5. `scripts/run_source_loader.py` — UPDATED
Added `claude_vision` example to the usage docstring.

### 6. Listing ID reconciled — `inputs/496_highpoint_xing/listing_notes.txt` — CREATED
Canonical listing ID is now **`496_highpoint_xing`**.  
Created `inputs/496_highpoint_xing/listing_notes.txt` with:
- All data from the known-good `inputs/496_highpoint/listing_notes.txt` (unchanged)
- Clear provenance header documenting that this is hand-keyed data
- Instructions for when to run the source_loader OCR step
The original `inputs/496_highpoint/listing_notes.txt` is **untouched**.

### 7. New pipeline run — GENERATED
**Output folder:** `outputs/run_496_repair_20260602/`  
Successfully produced:
- `draft_native_filled.pdf` — 112 fields filled, 0 failures
- `draft_native_filled_manifest.json`
- `draft_native_filled_report.csv`
- `final_validation_report.json` / `.csv`
- `normalization_warnings.csv`
- `raw_ingest_warnings.csv`
- `native_text_capacity_audit.json` / `.csv`
- `visual_review_checklist.md` / `.csv`

---

## Tool Availability Results

| Tool | Status | Notes |
|------|--------|-------|
| PyMuPDF (fitz) 1.27.2.3 | ✅ OK | Renders PDF pages to images without Poppler |
| pypdf 6.12.1 | ✅ OK | PDF form field fill |
| Pillow 12.2.0 | ✅ OK | Image handling |
| pdf2image Python package | ✅ installed | Needs Poppler binary to run |
| pytesseract Python package | ✅ installed | Needs Tesseract binary to run |
| **Tesseract binary** | ❌ NOT INSTALLED | Required for tesseract OCR adapter |
| **Poppler binary** | ❌ NOT INSTALLED | Required for pdf2image / tesseract PDF path |
| anthropic SDK 0.105.2 | ✅ installed (just now) | Required for claude_vision adapter |
| **ANTHROPIC_API_KEY** | ❌ NOT IN .env | Required to activate claude_vision adapter |
| Flask | ✅ OK | Web UI works |

**Bottom line:** All 5 source PDFs are fully scanned (0 extractable text via PyMuPDF).
Neither Tesseract nor Claude vision can run without their respective setup (binaries / API key).

---

## Source PDF Analysis

All 5 files in `05-PROJECT DATA SETS/496 Highpoint Xing/`:

| File | Pages | PyMuPDF chars | Type | Requires |
|------|-------|--------------|------|---------|
| `496.pdf` | 24 | 0 | Fully scanned | OCR |
| `4961.pdf` | 24 | 0 | Fully scanned (appears identical to 496.pdf) | OCR |
| `496handnotes.pdf` | 4 | 0 | Scanned handwriting | Claude vision strongly recommended |
| `496previouslisting.pdf` | 3 | 0 | Scanned (prior MLS listing) | OCR |
| `496publicrecord.pdf` | 3 | 0 | Scanned (public record/tax) | OCR |

None of these files have been read by the pipeline yet.

---

## Handwriting Extraction Status

**Not yet run.** `496handnotes.pdf` contains handwritten agent notes across 4 pages.

Tesseract is unreliable on handwriting. The recommended path is Claude vision
(`core/ocr_claude_vision.py`), which is now built and wired in, but requires
`ANTHROPIC_API_KEY` in `.env` before it can execute.

Once the key is set, the extraction prompt specifically:
- Asks Claude to flag handwritten sections with `[HANDWRITTEN]`
- Flags uncertain readings with `[UNCERTAIN]`
- Checks boxes and captures all visible content
- Does NOT guess — unclear content is flagged, not invented

---

## PDF Fill Results

### New run: `outputs/run_496_repair_20260602/`

| Metric | Value |
|--------|-------|
| Fields attempted | 133 |
| Fields filled | 133 (112 unique logical fields) |
| Fill failures | 0 |
| Required missing | 0 |
| Required unfilled | 0 |
| Overflow/capacity issues | 0 |
| Normalization warnings | 1 |
| Production ready | **YES** |
| Final packet created | No — awaiting human visual approval |

### Comparison vs. previous runs

| Run | Filled | Review | Missing | Ready |
|-----|--------|--------|---------|-------|
| `run_496_final` | 112 | 1 | 0 | ✅ yes |
| `run_496_session2` | 108 | 1 | 4 | ❌ no |
| `run_496_v2` | 110 | 1 | 2 | ❌ no |
| `run_496_20260525` | 112 | 1 | 0 | ✅ yes |
| **`run_496_repair_20260602`** | **112** | **1** | **0** | **✅ yes** |

The repair run matches the two best previous runs. No regression introduced.

---

## Remaining Review Items

### 1. `patio_porch_features: patio` — unknown option token
**Severity:** warning (not error — does not block production ready)  
**Present in all previous good runs** — this is a pre-existing mapping gap.  
**Meaning:** The value "patio" is not in the accepted vocabulary for `patio_porch_features`.
The field is likely not filled on the PDF, or filled with an approximation.  
**Action needed:** Check the FMLS form for what checkbox or value covers "patio".
Add the correct mapping to `core/accepted_terms.py` or the field registry.

### 2. Raw scanned PDFs — NOT YET EXTRACTED
The 5 source PDFs have never been read. The current filled PDF is based entirely on
the hand-keyed `listing_notes.txt`. Values from the signed listing agreement,
handwritten notes, prior MLS listing, and public records have NOT been cross-checked.

**Fields that should be verified against source documents once OCR runs:**
- Tax ID (031919) — verify against public record
- Square footage (2256) — verify against public record  
- Lot size (0.46 acres) — verify against public record
- Legal description — verify against deed
- Deed Book/Page (1739/20) — verify against paperwork
- HOA fee ($330/yr) — verify against listing agreement
- School names — verify against current MLS standards
- Any seller-disclosed conditions in the listing agreement

---

## Uncertain Fields (Requiring Human Review)

The current output has NO uncertain fields — all values came from the verified
hand-keyed notes file. However, these fields should be re-verified once the
scanned documents are extracted:

| Field | Current Value | Verify Against |
|-------|--------------|----------------|
| Tax ID | 031919 | `496publicrecord.pdf` |
| Square Footage | 2256 | `496publicrecord.pdf` |
| Acres | 0.46 | `496publicrecord.pdf` |
| Year Built | 1995 | `496publicrecord.pdf` |
| Taxes | 2027 | `496publicrecord.pdf` |
| Deed Book | 1739 | `496.pdf` or `4961.pdf` |
| Deed Page | 20 | `496.pdf` or `4961.pdf` |
| Association Fee | 330 | `496.pdf` listing agreement |
| Directions | "UPDATE BEFORE SUBMITTING" flag | Confirm correct route |
| `496handnotes.pdf` | (unknown — not yet extracted) | All 4 pages need Claude vision |

---

## Files Generated This Session

| File | Status |
|------|--------|
| `tests/test_source_loader.py` | Fixed (1-line path correction) |
| `core/ocr_claude_vision.py` | Created (new OCR adapter) |
| `core/source_loader.py` | Updated (claude_vision adapter wired in) |
| `scripts/run_source_loader.py` | Updated (usage example added) |
| `requirements.txt` | Updated (anthropic added) |
| `inputs/496_highpoint_xing/listing_notes.txt` | Created (baseline with provenance header) |
| `outputs/run_496_repair_20260602/` | Created (full pipeline output, 112 filled) |
| `PROJECT_AUDIT_496_HIGHPOINT_XING.md` | Created (audit report) |
| `PROJECT_REPAIR_REPORT_496_HIGHPOINT_XING.md` | This file |

**NOT modified / NOT deleted:**
- `inputs/496_highpoint/listing_notes.txt` — original baseline, untouched
- `outputs/run_496_final/` — best previous run, untouched
- `templates/ResidentialDataInput_MASTER_ORIGINAL.pdf` — never touched
- All other previous output runs — untouched

---

## Next Steps — Exactly What's Needed

### Step A — Add API key to enable OCR (requires your action)

Add one line to `.env`:
```
ANTHROPIC_API_KEY=sk-ant-...your key here...
```

Your Anthropic API key is the same one you use with Claude Code.

### Step B — Run the Claude vision source loader

```powershell
.\.venv314\Scripts\python.exe scripts\run_source_loader.py `
  --listing-id 496_highpoint_xing `
  --data-sets-folder "C:\Users\chris\.00-PROJECTS-v2.0\05-PROJECT DATA SETS\496 Highpoint Xing" `
  --ocr-adapter claude_vision
```

This will:
- Process all 5 source PDFs (5 + 24 + 24 + 4 + 3 + 3 = 58 pages total)
- Call Claude vision on each page (~58 API calls)
- Write per-page extracted text to `raw_extracted_text/496_highpoint_xing/`
- Write combined output to `inputs/496_highpoint_xing/combined_notes.txt`

**Note:** This will use Anthropic API credits. At roughly 1-2 cents per page for
vision requests, estimate $0.60–$1.20 for the full run.

### Step C — Review the OCR output

Open `inputs/496_highpoint_xing/combined_notes.txt` and look for:
- `[HANDWRITTEN]` sections — review for accuracy
- `[UNCERTAIN]` flags — decide correct value
- Any values that conflict with the hand-keyed notes

### Step D — Merge OCR findings into a final payload

After reviewing the OCR output, update `inputs/496_highpoint_xing/listing_notes.txt`
with any corrections or additions from the scanned documents. Then re-run the pipeline:

```powershell
.\.venv314\Scripts\python.exe tools\run_listing_intake_pipeline.py `
  --input-dir inputs\496_highpoint_xing `
  --out-dir outputs\run_496_ocr_verified
```

### Step E — Fix `patio_porch_features` mapping (optional but clean)

Check what "patio" maps to in the FMLS PDF and add it to `core/accepted_terms.py`.
This is a minor mapping gap that exists in all runs.

### Step F — Visual approval and final packet

Once you've reviewed the draft PDF and confirmed all fields are correct:
Re-run with `--force-final` to create `final_listing_packet.pdf`:

```powershell
.\.venv314\Scripts\python.exe tools\run_listing_intake_pipeline.py `
  --input-dir inputs\496_highpoint_xing `
  --out-dir outputs\run_496_final_approved `
  --force-final
```

---

## Questions Still Needing Your Decision

1. **API key:** Will you add `ANTHROPIC_API_KEY` to `.env` to enable OCR?
   This is the single remaining blocker for reading the scanned source documents.

2. **`4961.pdf` appears identical to `496.pdf` (same size, same page count).**
   Is this a duplicate scan? If so, it can be safely skipped in the source loader.
   No action needed now — the source loader will attempt both and produce identical text.

3. **`patio_porch_features: patio`** — do you want this fixed in the accepted terms?
   Takes 5 minutes once you confirm what the correct FMLS checkbox value is.

---

*This report covers Phase 1 of the repair pass. Phase 2 (raw scanned PDF extraction + OCR merge) requires the API key from Step A above.*