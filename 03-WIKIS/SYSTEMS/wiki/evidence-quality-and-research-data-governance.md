---
type: framework
timeline: reference
status: active
reference_priority: supporting
tags: [systems, evidence, data-management, audit]
---

# Evidence Quality and Research Data Governance

**Summary**: Evidence is trustworthy when its claim, method, data lineage, limits, and challenge path remain inspectable. Reputation, citation volume, statistical significance, or successful replication alone cannot establish decision fitness.

**Sources**: *Why Trust Science*; “What's Wrong with Social Science and How to Fix It”; NIH Final Policy for Data Management and Sharing (NOT-OD-21-013); *Eight Principles of Good Data Management*; *Data Management for Researchers: Three Tales*; AIMOS 2021 Rose O'Dea talk; Ehlers and Lonsdorf (2022), *Data sharing in experimental fear and anxiety research* (physical pp. 1-28); MIT 9.401 course materials (course archive parked, not compiled).

**Last updated**: 2026-08-02

## Open is not enough

Ehlers and Lonsdorf's 2022 fear-conditioning inventory makes the reuse gap concrete. Across 103 public datasets, only 31% included analysis code, 13% included materials, 55% had a reuse license, 36% had a codebook or README, 38% lacked a publication link, and 31% lacked a persistent identifier. None was reusable for secondary analysis without additional information from the original authors. These are field-specific results, not universal rates, but they demonstrate why public availability is not the same as functional reuse.

Their ten-step operating sequence is reusable beyond that field:

1. Plan ethical, legal, consent, access, and de-identification requirements before collection.
2. Give variables meaningful standardized names and distinguish raw from transformed values.
3. Organize files with a documented domain structure.
4. Prefer non-proprietary, human- and machine-readable formats; retain raw and processed data when permitted.
5. Supply a separate codebook or README covering units, scales, provenance, transformations, exclusions, and collection conditions.
6. Use a sustainable searchable repository, not a fragile personal or project link.
7. Assign a persistent identifier.
8. State reuse and attribution terms through an appropriate license or agreement.
9. Link data, code, versions, preprint, and final publication bidirectionally.
10. Integrate with domain standards and curated collections where those improve compatibility.

## Evidence gate

For any consequential analytical claim, record:

1. The exact claim and decision it is meant to support.
2. Whether the evidence is observational, experimental, modeled, testimonial, or inferred.
3. Sample selection, exclusions, transformations, outcome choice, and plausible confounders.
4. Effect size and uncertainty—not only direction or a significance threshold.
5. Reproducibility of the analysis and whether the central claim, rather than an easier side claim, was tested.
6. External-validity limits: where, when, and for whom the result may fail.
7. Independent challenge evidence, contradictions, and the result that would change the recommendation.

Replication is useful but incomplete: a repeatable association may still have the wrong causal explanation, a trivial effect, or no fit outside the study setting.

## Data-governance packet

Plan data handling before collection or analysis. Preserve source and collection context; definitions, units, schema, and metadata; validation and quality checks; transformations and intermediate artifacts; access, privacy, legal, ethical, and security constraints; repository, retention, version, and preservation decisions; the sharing timeline and justified restrictions; and a responsible owner.

The NIH policy is a domain-specific authoritative example. For covered research it requires a prospective Data Management and Sharing Plan, appropriate preservation and sharing of scientific data and metadata, and revision when direction, repository, or timing changes. Its legal scope should not be generalized beyond NIH-funded work, but its planning structure is reusable.

## Audit application

Treat an operational dataset like a material trace in construction: if labels, cuts, substitutions, and custody disappear, the finished assembly may look sound while nobody can verify what is inside it. An audit should test both the output and the evidence pipeline that produced it.

## Connects to

[[model-validation-and-testing-practice]], [[operations-research-study-lifecycle]], [[responsible-process-mining-fact-gate]], and [[the-art-of-spreadsheet-modeling]].

## Proof

An independent reviewer can reproduce the evidence path, identify its limits, and state what would invalidate or narrow the conclusion.
