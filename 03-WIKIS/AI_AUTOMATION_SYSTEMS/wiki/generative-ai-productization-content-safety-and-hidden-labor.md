---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, productization, trust-and-safety, rlhf, data-labor, supply-chain, historical]
---

# Generative-AI Productization, Content Safety, and Hidden Labor

**Summary**: Generative-AI productization couples model improvement to user
interaction, moderation, and outsourced human judgment. APIs and consumer tools
create a data flywheel, but they also expose foreseeable abuse before trust-and-
safety systems are mature. Output filters and RLHF can improve usability without
removing the underlying model's probabilistic failure modes. Both techniques
depend on people who classify traumatic material, write ideal responses, and
rank outputs - often through outsourcing chains designed to minimize price and
distance the model developer from labor conditions.

**Source**: `raw/empireofAIDreamsandNightmares.pdf` (Karen Hao, *Empire of AI:
Dreams and Nightmares in Sam Altman's OpenAI*, 2025), Chapter 8, “Dawn of
Commerce” (physical PDF pp. 172-184), and Chapter 9, “Disaster Capitalism”
(pp. 185-216), reviewed as two complete, connected chunks. Physical p. 217 is
the Part III divider; Chapter 10 begins p. 218. Boundaries visually verified.

**Last updated**: 2026-07-16

## Source Posture

Hao combines company documents, employee accounts, prior reporting, labor
research, and first-person interviews with data workers. Company and vendor
responses sometimes dispute her characterizations. Preserve those disputes and
treat specific motives and contract practices as attributed reporting. The labor
supply-chain mechanisms are the durable retrieval target.

## Productization Became a Research Method

OpenAI's 2021 road map linked research and products in a self-reinforcing loop.
The lab planned to scale language, code, image, multimodal, and agentic systems;
turn selected models into products; collect user interaction data; and feed the
result back into capability development. Productization therefore served four
jobs at once:

- revenue and partner value;
- real-world capability and misuse discovery;
- behavioral data for model refinement;
- distribution and brand recognition.

This makes deployment scientifically useful, but also creates a conflict: the
same incidents that reveal what to fix occur in real user contexts. “Learning
from exposure” is not a safety control unless the release is bounded, monitored,
reversible, and supported by a mature incident-response function.

## Trust and Safety Arrived After the API

The GPT-3 API initially lacked a formal trust-and-safety organization and robust
content filtering. Access and use-case decisions were developed through ad hoc
review. Early filters overblocked benign references to Black and trans people and
were made optional after customer complaints. Replika raised concerns about
sexual and emotionally manipulative companion interactions. AI Dungeon exposed
text generation involving child sexual abuse, a foreseeable recurrence from an
earlier model.

The lesson is not that a policy team can predict every misuse. It is that product
infrastructure must exist before broad exposure:

- explicit use-case and prohibited-content standards;
- abuse telemetry and customer escalation paths;
- tested mandatory controls for high-severity harms;
- authority to suspend a customer or feature despite commercial relationships;
- support for affected users and reviewers;
- evidence-driven release expansion and rollback.

Calling informal prompt attacks “red teaming” can create false assurance. A real
test program defines threat models, coverage, pass criteria, residual risk, and
the limits of what testing can guarantee.

## Codex and Copilot Expose the Data-and-Control Bargain

OpenAI and Microsoft developed Codex using public GitHub repositories plus
other programming sources. The work produced GitHub Copilot and then an OpenAI
API release. Hao identifies two governance problems that recur in generative AI:

1. public availability was treated as permission to convert community-created
   work into a proprietary commercial training asset without consent or direct
   compensation;
2. dependence on a distribution partner reduced OpenAI's brand recognition,
   user visibility, feedback data, and product control, motivating direct
   consumer products.

Data rights and channel control are therefore connected. Whoever owns the user
relationship gains telemetry, iteration speed, pricing power, and the ability to
define acceptable use.

## Output Control Moves Harm to Human Reviewers

Scaling broad web data shifted the operational strategy from carefully curating
inputs toward filtering outputs. To train a moderation filter for later models,
OpenAI contracted Sama workers in Kenya to classify large volumes of sexual,
violent, hateful, self-harm, and abusive text. Hao reports low hourly pay,
inadequate psychological support, traumatic exposure, and workers who did not
know the ultimate client or product because of confidentiality rules.

This is a supply-chain risk, not a vendor anomaly. Outsourcing creates two layers
of margin pressure and several layers of distance:

`model developer -> data vendor -> platform/management -> worker`

The developer specifies the disturbing material and price; the vendor controls
day-to-day conditions; nondisclosure hides the client and purpose; each party can
attribute failure to the other. Procurement must therefore treat worker welfare
as part of model safety, with direct audit rights and remedy obligations.

## RLHF Is Human Production, Not Automatic Alignment

OpenAI used contractors to write preferred answers and rank model outputs for
helpfulness, truthfulness, and harmlessness. This produced InstructGPT and helped
make conversational GPT-3.5 usable as ChatGPT. RLHF became a standard product
pipeline because it improved instruction following, tone, and visible safety.

Its limits matter:

- workers interpret underspecified value tradeoffs;
- detailed guidelines encode company choices about acceptable behavior;
- contractor-written material becomes hidden product content;
- preference tuning changes output probabilities but does not make a neural
  model a deterministic fact database;
- hallucination remains possible when the model must guess;
- scaling demand encourages vendors to seek cheaper or more specialized labor.

RLHF is better understood as distributed editorial and evaluation labor layered
onto a model, not proof that the system is aligned.

## The Crisis-Labor Playbook

Hao traces a recurring labor-market strategy from self-driving-car annotation to
generative AI. Platforms found educated, connected populations experiencing
economic crisis; attracted workers with comparatively strong initial pay; used
global competition and task-based contracting to reduce costs; and could remove
workers or entire countries when quality, language, or customer needs changed.
Workers carried income volatility, unpaid waiting, payment failures, surveillance,
health costs, and the risk of sudden offboarding.

The generative-AI phase changed the task mix from tracing objects to producing
language and expert judgment. As customers sought coding, science, and other
professional capability, labor sourcing moved toward credentialed specialists.
The hidden-work system did not disappear; it climbed the skill ladder.

## Human-Supply-Chain Gate

Before approving a data, moderation, or preference contract, require:

1. a complete subcontractor and worker-location map;
2. local living-wage evidence, predictable paid hours, sick leave, and clear
   contracts;
3. informed disclosure of the client, purpose, and exposure class;
4. individual trauma screening, private counseling, exposure limits, and paid
   recovery time for sensitive work;
5. worker appeal, collective-action, payment, and anti-retaliation mechanisms;
6. direct developer audit rights and joint responsibility for remedy;
7. data lineage, consent/licensing, and creator-compensation review;
8. separate evidence for model quality, abuse resistance, and worker welfare.

## Connects To

- [[scaling-doctrine-compute-data-and-hidden-labor]] - this page extends the
  Part I supply-chain model into moderation and RLHF operations.
- [[preference-inference-feedback-and-human-ai-cooperation]] - feedback is a
  sociotechnical measurement process, not direct access to human values.
- [[mcp-security-and-authorization]] - product access control requires threat
  models and enforcement, not informal allowlists.
- [[oecd-ai-incidents-monitor]] - severe incidents should feed explicit release,
  escalation, and rollback decisions.
- [[nist-ai-rmf]] - MAP and MEASURE must include labor and data provenance, not
  only model outputs.

## Limits and Recency

The chapter's vendor, wage, platform, and contract details are time-bound and in
some cases disputed. Verify current labor conditions and supplier policies
directly. The source documents recurring mechanisms; it does not establish that
every current RLHF, moderation, or expert-data program uses the same conditions.
