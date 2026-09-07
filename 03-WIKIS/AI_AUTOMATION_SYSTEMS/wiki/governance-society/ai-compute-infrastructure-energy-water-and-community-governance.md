---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, compute, data-centers, energy, water, environment, supply-chain, community-governance, historical]
---

# AI Compute Infrastructure, Energy, Water, and Community Governance

**Summary**: Generative AI is a physical infrastructure system. Its models depend
on land, grids, cooling water, minerals, chips, transmission, backup power, and
communities that host extraction and data centers. Scaling concentrates benefits
in model and cloud firms while distributing water stress, pollution, noise,
ecological loss, and public opportunity costs across distant locations. Community
resistance in Chile and Uruguay shows a more complete governance pattern:
disclose resource use, give affected residents standing, assess the whole supply
chain, and redesign projects around local ecological and social constraints.

**Source**: `raw/empireofAIDreamsandNightmares.pdf` (Karen Hao, *Empire of AI:
Dreams and Nightmares in Sam Altman's OpenAI*, 2025), Chapter 12, “Plundered
Earth” (physical PDF pp. 260-287), reviewed as one complete dense chapter chunk.
Chapter 13 begins on physical p. 288; boundary visually verified.

**Last updated**: 2026-07-16

## Source Posture

Hao combines historical argument, company and government documents, published
estimates, interviews, and first-person reporting in Chile and Uruguay. Specific
energy, water, emissions, construction, and project numbers are time-bound and
depend on technical assumptions. Preserve the mechanism, then verify every live
quantity and project status from primary sources.

## The Physical AI Stack

“Cloud” language hides a material chain:

`mining -> chip and equipment manufacture -> power generation and transmission
-> data-center land and construction -> model training -> inference and cooling
-> hardware replacement and e-waste`

Each link has different owners, locations, impacts, and affected groups. A model
impact statement limited to training electricity misses minerals, construction,
water, inference growth, grid changes, backup generation, and disposal.

GPU-dense facilities also change the unit of planning. AI racks demand more power
than conventional server racks, while serving popular models can consume energy
continuously and at much greater cumulative scale than one training run. Proposed
megacampuses can become grid-scale industrial projects rather than ordinary
commercial buildings.

## Efficiency Does Not Guarantee Lower Total Impact

More efficient chips, models, and cooling can reduce the resource cost per query.
They do not guarantee a reduction in total resource use when lower cost and better
performance drive more users, queries, models, and data centers. This is a rebound
problem:

`unit efficiency gain -> cheaper/broader use -> greater total demand`

Environmental review must therefore report both intensity and absolute use:
energy per task and total energy; water per unit and total withdrawal/consumption;
emissions per model and portfolio emissions.

Claims that generative AI will solve climate problems also need a counterfactual.
Many useful climate applications rely on smaller supervised, anomaly-detection,
or time-series systems. A large generative model should not receive climate credit
for a task that a smaller system can perform with less impact.

## OpenAI-Microsoft Scaling Made Infrastructure Strategic

Hao describes a phased supercomputer plan in which GPT-3 and GPT-4 training
clusters were followed by much larger proposed facilities. Compute scarcity was
not only financial: chip supply, land, grid capacity, energy generation, water, and
the technical ability to train across sites constrained expansion. The reported
Stargate/Phase 5 concept illustrates how a model road map can implicitly commit
regions and utilities to infrastructure on the scale of a major city.

This creates a governance mismatch. A frontier lab can make a model-scaling
decision in one office, while cloud partners, utilities, municipalities, and mining
communities absorb the physical implementation across years and continents.

## Impact Is Unevenly Distributed

Hao uses Chile's copper and lithium extraction to connect AI infrastructure to a
long history of export-oriented resource dependency. Indigenous communities in
the Atacama have experienced water depletion, pollution, ecological loss, and
economic dependence while receiving a small share of the value produced from
their territories.

Data centers repeat the structure in a new layer. Firms seek inexpensive land,
tax treatment, reliable power, and water. Facilities may offer temporary
construction employment but relatively few permanent local jobs. Community
programs and public-relations projects do not compensate for resource extraction
when residents lack meaningful consent or basic services.

The relevant distribution questions are:

- who receives revenue, jobs, compute, and product benefits;
- who loses water, land, grid capacity, quiet, health, or ecological resilience;
- which impacts cross borders through minerals, manufacturing, and e-waste;
- which communities can stop or redesign the project;
- whether promised mitigation is enforceable after construction begins.

## Community Resistance Is an Audit Model

Groups in Cerrillos and Quilicura, Chile, and researchers in Uruguay used public
records, environmental filings, referenda, litigation, and international networks
to uncover water plans and challenge projects. Their work demonstrates several
governance mechanisms:

1. technical filings must be public and understandable;
2. water and energy use cannot be treated as commercial secrets;
3. cumulative regional impact matters more than one facility's efficiency;
4. affected communities need standing before permits are irreversible;
5. alternatives such as air cooling must be compared under local conditions;
6. review should follow minerals, labor, carbon, water, and waste across borders.

Successful resistance did not reject digital infrastructure categorically. It
changed designs, exposed hidden assumptions, and demanded a different scale and
relationship to place.

## From Community Benefit to Community Co-Design

The Chilean examples distinguish two models:

- **Benefit add-on**: the developer chooses the project, then funds a park,
  education program, or other local initiative.
- **Co-design**: residents help determine siting, scale, resource limits, public
  access, ecological restoration, monitoring, and whether the project proceeds.

Architecture workshops imagined data centers integrated with wetlands, visible
water systems, public walkways, biodiversity restoration, and local environmental
measurement. These proposals do not erase industrial impact, but they move the
community from recipient to design authority.

## Infrastructure Approval Gate

Before approving an AI compute project, require:

1. absolute and peak energy, water withdrawal, water consumption, and emissions
   estimates across training and expected inference growth;
2. watershed, grid, heat, noise, drought, and cumulative regional analysis;
3. full mineral, construction, labor, equipment, backup-power, and e-waste map;
4. comparison with smaller models, efficiency measures, alternative cooling,
   other sites, and no-build options;
5. public filings in local languages with no resource-use secrecy;
6. affected-community participation, appeal, and consent procedures before
   irreversible commitments;
7. enforceable limits, monitoring, public reporting, remediation, and shutdown
   triggers;
8. a distribution account of local jobs, taxes, infrastructure benefits, and
   opportunity costs.

## Connects To

- [[scaling-doctrine-compute-data-and-hidden-labor]] - compute is a coupled
  supply chain rather than a single model input.
- [[corporate-ai-research-control-transparency-and-accountability]] - opacity
  prevents independent environmental measurement as well as model audit.
- [[nist-ai-rmf]] - MAP must identify physical infrastructure and affected
  communities, while MEASURE tracks absolute lifecycle impacts.
- [[enterprise-ai-adoption-and-production-roadmap]] - model and infrastructure
  alternatives belong in the business-case gate before scale is committed.

## Limits and Recency

The chapter's projections and company plans extend through 2024 and may have
changed. Water accounting must distinguish withdrawal from consumption; energy
claims must state grid mix, time, geography, and operational boundary. Verify
current facility designs, permits, litigation, and corporate targets directly.
