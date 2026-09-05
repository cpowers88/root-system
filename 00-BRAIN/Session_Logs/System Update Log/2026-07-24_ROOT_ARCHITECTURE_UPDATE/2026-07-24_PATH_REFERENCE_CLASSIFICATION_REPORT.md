---
type: system-update
timeline: now
status: active
tags: [architecture, castle, path-integrity, baseline]
created: 2026-07-24
---

# Path Reference Classification Report — 2026-07-24

## Result

The first conservative classification pass reviewed the 1,285 findings from
the read-only audit. Only clearly intentional or historical classes were
allowlisted. Unclassified candidates remain visible for the next review.

| Classification | Count | Treatment |
|---|---:|---|
| Intentional template/placeholder | 15 | Baseline allowlist |
| Historical narrative/archive | 97 | Baseline allowlist |
| Intentional external reference | 109 | Baseline allowlist |
| Unclassified candidate | 1,064 | Remains open; no suppression |
| **Total** | **1,285** | |

## Baseline artifact

The rules are recorded in:
`00-BRAIN\scripts\path_reference_baseline.json`.

The baseline is rule-based and conservative. It is now accepted by
`path_reference_audit.py --baseline` and reported separately from
unbaselined findings. It does not claim that every
finding in a historical or external-reference scope is harmless; it only
removes those scopes from the first active-link defect queue. The audit tool
now machine-enforces the distinction while preserving every finding in the
report.

## Open candidate queue

The 1,064 remaining candidates include:

- 217 ambiguous wikilinks;
- 241 unresolved wikilinks;
- 514 unresolved Markdown links;
- 92 broken or unverified anchors.

These require targeted review by owner realm. The highest-value next slice is
the live CASTLE and wiki navigation surface, followed by canonical owner-path
references. Do not repair links in bulk until each candidate has an owner and
the intended target is confirmed.

## Next exact action

Final post-integration run: 1,670 Markdown files scanned, 221 findings
baselined, and 1,064 findings unbaselined. The command exits `1` while
unbaselined findings remain; this is the intended safety gate.

Next: inspect the unbaselined CASTLE/wiki subset before producing the CASTLE
relocation impact report.

## Live CASTLE/wiki subset run

The first subset run exposed a validator false-positive: wikilinks were
falling back to the entire vault instead of the owning hub's `wiki/` root.
The auditor was corrected to scope resolution to CASTLE or the current domain
hub, then rerun without changing Markdown.

The corrected full scan reports 1,165 total findings, 221 baselined, and 944
unbaselined. The live CASTLE/domain-wiki subset contains 266 unbaselined
findings:

| Owner | Unresolved wikilink | Unresolved Markdown link | Broken anchor | Total |
|---|---:|---:|---:|---:|
| CASTLE | 0 | 0 | 1 | 1 |
| BUSINESS | 1 | 0 | 0 | 1 |
| PHYSICS | 145 | 2 | 2 | 149 |
| PYTHON | 13 | 0 | 0 | 13 |
| REVENUE_LAB | 0 | 4 | 0 | 4 |
| SYSTEMS | 29 | 0 | 0 | 29 |
| TECHNOLOGY | 69 | 0 | 0 | 69 |
| **Total** | **257** | **6** | **3** | **266** |

## Recommended repair order

1. PHYSICS owner review: 149 findings, mostly references to missing or
   renamed problem-type, drill, and worked-example pages.
2. TECHNOLOGY owner review: 69 unresolved wikilinks.
3. SYSTEMS and PYTHON owner review: 42 combined unresolved wikilinks.
4. CASTLE/BUSINESS/REVENUE_LAB: resolve the six isolated findings manually.

No link was repaired in this pass. Each candidate needs owner confirmation of
the canonical target before correction or baseline approval.

## PHYSICS disposition

The PHYSICS queue is carried forward as **deferred structural work**, not
bulk-repaired and not added to the baseline allowlist. The PHYSICS log already
records roughly 138 planned-page wikilinks intentionally left unresolved, and
the current 149-finding cluster is concentrated in the later-stage packet
architecture. When Chris lands on that material, the packet/page structure may
need a new design rather than individual link patches.

Until then, the findings remain visible and count as unbaselined, with the
disposition `deferred-owner-review: PHYSICS architecture revision`.

**Check-at:** after baseline integration and CASTLE/wiki subset review.
