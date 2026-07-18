---
type: research
timeline: reference
tags: [ai-automation, advisor-builder, ai-adoption, sme-ai-adoption, toe-framework, maturity-model, forecasting, taxonomy, verification-capacity]
source: "raw/AI in Business and Economics.pdf — ed. Isabel Lausberg & Michael Vogelsang, De Gruyter 2024 (open access, ISBN 978-3-11-079005-4, DOI 10.1515/9783110790320), proceedings of the EPEAI conference (Ruhr West University of Applied Sciences, March 2023), 279 pdftotext pp. / 17 chapters across 7 Parts — chunk-ingested 2026-07-17, full main text (Preface through Chapter 17, all 17 chapters read in full including bibliographies) plus back matter (List of Contributors, About the Editors, List of Figures, List of Tables) inspected as reference-only"
---

# AI in Business and Economics (Lausberg & Vogelsang, De Gruyter 2024) — EPEAI Conference Proceedings

Open-access academic anthology: 17 short papers (10-20 pp. each) from the
March 2023 Economic Perspective of Artificial Intelligence (EPEAI)
conference, organized by the editors into seven Parts — Competition and
Regulation; Production and Processes; Finance and Accounting; Organisation
and Workflow; HR and Employment; Artificial Intelligence and Humans;
Forecasting. Unlike this hub's single-narrative books, each chapter is an
independent, self-contained empirical or conceptual paper — the retrieval
value is per-chapter (a named framework, a dataset finding, a taxonomy), not
one through-line argument. The editors' own three-conclusion summary
(Preface) still works as the volume's map: (1) broad corporate AI adoption
has just begun and needs low-threshold/SME-scaled approaches; (2)
consequences for employees/society are ambiguous, not simply positive or
negative; (3) adoption requires new *methods*, changing *perceptions*, and
updated *rules and regulations* together, not any one alone.

## Why this book matters to `.ROOT` — the cross-chapter pattern

The single most citable finding is **structural, not topical**: three
independent chapters in this one volume — Ch. 2 (KI-AGIL, SME AI process
model), Ch. 5 (management-reporting maturity model), and Ch. 14 (South
African SMME marketing adoption) — each reach for the same
**Technology-Organization-Environment (TOE) framework** to explain AI
adoption barriers, without citing each other as the reason (Ch. 14 does cite
Ch. 5's institution but arrives at TOE independently via its own literature
search). All three land on the same binding constraint: organisational
trust, data-infrastructure readiness, and skills gaps block adoption more
than AI capability itself. This is this hub's now-familiar
**verification-capacity** finding (see [[ai-index-2026]],
[[work-trend-index-2024-2026]], [[business-case-for-ai-ganesan-leader-playbook]],
[[generative-ai-for-software-development-pereira]]), restated here at three
different organisational scales — SME process design, corporate finance
function, emerging-market SMME marketing — inside a single book: the
clearest within-source convergence this hub has logged to date.

The book also supplies several genuinely reusable, field-tested or
empirically-derived frameworks for Advisor-Builder client engagements —
flagged per-chapter below — plus one directly relevant landscape taxonomy
(Ch. 8's Plug and Play AI / NoCode-LowCode taxonomy) that cross-checks and
sharpens this hub's existing tool-landscape pages
([[workflow-automation-tools-landscape]], [[agent-vetting-worked-examples]],
[[2025-ai-agent-index]]).

## Part 1: Competition and Regulation

**Ch. 1 — The Rise of Artificial Intelligence: Towards a Modernisation of
Competition Policy** (von Maydell & Menzel, ETH Zürich / German Federal
Ministry for Economic Affairs). No dataset yet links corporate AI adoption
directly to market concentration, so the authors proxy it with intangible-
asset investment (software/data, German ZEW innovation panel) cross-
referenced against CompNet market-concentration (Herfindahl-Hirschmann
Index) and markup data across seven European countries. Finding: industries
with high intangible-asset investment (ICT, financial/insurance services)
show both higher market concentration and higher markups, with markups
correlated to *lower* labour share — correlational only, no causal
AI-adoption dataset yet exists. Policy proposals: an "AI tax," subsidized
AI-infrastructure access for lagging/SME firms, an early-warning system for
anti-competitive concentration, and new IP frameworks for non-human-
generated work. Regulatory-landscape context, not an operational tool —
pairs with [[nist-ai-rmf]] and [[mcp-security-and-authorization]] as another
"governance hasn't caught up to deployment" data point, this time from
competition-policy economics rather than safety.

## Part 2: Production and Processes

**Ch. 2 — "KI-AGIL": An Agile Process Model to Make AI Development
Accessible to SMEs** (Feld, Arens-Fischer, Schumacher, Osnabrück UAS).
Field-tested across six SMEs in the German-Dutch INTERREG project
(2020-2022). Produces the **KI-AGIL process model**, compared directly
against CRISP-DM and CRISP-ML(Q): adds a **preceding "Initial Vision
Determination" phase** (novice SMEs can't specify a use case up front — they
need a medium-term vision statement first) and a **separate "Data
Acquisition" phase** split from data analysis (different people typically do
each, in an SME). Full cycle: Initial Vision → Vision Statement → [sprint:
Use Case → Data Acquisition → Data Exploration → AI Modelling → Evaluation,
with explicit redo-loops] → Usage → Integration → Operation/Maintenance,
with continuous feedback refining the vision. Cited barrier data: 75% of
experts rate AI-expertise shortage a "very strong obstacle" for SMEs
(Begleitforschung Mittelstand Digital 2021); 65% of 300+ surveyed German
SMEs agree it's their single greatest AI obstacle (Deloitte 2021). Field-
tested successfully in 2 of the participating companies. **High
Advisor-Builder value** — a second, independently field-tested, low-
threshold SME-AI-adoption process model, sitting alongside the
[[business-case-for-ai-ganesan-leader-playbook]] HI-AI Discovery Framework
and B-CIDS/Jumpstart approach as an alternate concrete phase structure for
AI-inexperienced SME clients.

**Ch. 3 — Automatic Classification of Files Based on the Classes of IEC
61355** (Menger, Ohler-Martins, Lemette, Martin — Menger Engineering GmbH +
three universities). Applied case study: classifying power-plant technical
documents (100,000+ files/plant, ~5 min/file manually) into the IEC 61355
Document Kind Classification Code. Compared a classical CNN against the
pre-trained **Document Image Transformer (DiT)** on three image-conversion
strategies (single-page, multi-page, cropped-part). CNN baseline: 30-40%
accuracy (effectively guessing one class). DiT transformer: 77-84% accuracy
across all three conversion strategies — single-page conversion performed
best; adding more images per file did not help. Narrow applied-engineering
case study; relevant only as a named-technique reference (IEC 61355 +
DiT/BEiT lineage) if a client has industrial/plant document-classification
needs.

## Part 3: Finance and Accounting

**Ch. 4 — Auditing Algorithms in the (Non-)Financial Audit: Status Quo and
Way Forward** (Bravidor, University of Freiburg). Conceptual synthesis:
static algorithms (deterministic, auditable via standard IT controls) vs.
dynamic/learning algorithms (behavior shaped by training data). Surveys
named audit frameworks: **SMACTR** (Raji et al. 2020 — six stages: scoping,
mapping, artefact collection, testing, reflection, post-audit); the
**"bobby audit" vs. "Sherlock audit"** metaphor (Le Merrer, Pons & Trédan
2022 — fixed-rulebook inspection vs. investigative-narrative audit); a
complexity/autonomy/impact risk triage (Boer, Beer & van Praat 2023); and a
two-way **access-level × target-state-dimension** framework (Koshiyama,
Kazim & Treleaven 2022 — black-box/process access through white-box/
parameter access, crossed against explainability, robustness, fairness,
privacy, oversight). Verdict: "standards are thin, at best" — no binding
financial-audit standard for learning algorithms exists (the IAASB's
2024-27 work plan doesn't mention AI). **High value as an audit-engagement
vocabulary** — distinct from and complementary to this hub's MCP/agent
vetting screen, since SMACTR/Koshiyama audit a model already in production,
not a tool pre-deployment; also complements [[nist-ai-rmf]]'s MEASURE
function.

**Ch. 5 — Barriers to the Use of Artificial Intelligence (AI) in Management
Reporting** (Lausberg, Eimuth, Stockem Novo — the volume's editors/
co-authors, Ruhr West UAS). 10 expert interviews + literature analysis.
Produces the **AI-Reporting maturity model**: four levels (0
Non-Algorithmic → 1 Assisted → 2 Intelligence-Assisted → 3 AI-Reporting)
scored across five dimensions (Data, AI Infrastructure, AI Culture, Team &
Skills, AI Applications); even at the top level, "human oversight" remains
a permanent architectural feature, not a scaffold to remove. Barriers
mapped onto **TOE**: technological (fragmented data, no single source of
truth, siloed systems); organisational (named the single biggest barrier by
experts: low German-market trust/change-readiness, weak top-management
buy-in, missing data-science skills); environmental (ethics/regulation —
acknowledged but explicitly excluded from the scorable model as
non-company-controllable). Quotable expert line: "First get your systems in
order!" — infrastructure precedes AI value. **Very high Advisor-Builder
value**: a five-dimension/four-level scoring grid is an immediately usable
client-diagnostic instrument, and pairs naturally with BUSINESS's
`smb-ai-audit-method`.

**Ch. 6 — Transforming Management Accounting with Robotic Process
Automation — Requirements and Implications** (Rautenstrauch, Hummel, Isoz,
Moser — Swiss universities/practitioners). 6 expert interviews at large
Swiss corporations. Finding: management accountants are **not displaced**
by RPA — evidence points to role transformation along two converging paths,
"business-partner"/internal-advisor or (citizen) data scientist. Freed time
reallocates to predictive/prescriptive analytics and business steering.
Named emerging-skill clusters: digital/IT literacy, methodological/
analytical (model design), social/coordination skills (increasingly
important as automation pushes accountants closer to leadership), process/
corporate-structure understanding, compliance. Small-N (6), single-country,
explicitly flagged as non-generalizable by the authors. Moderate
Advisor-Builder value: a citable "automation shifts the role, doesn't
eliminate the profession" change-management narrative, alongside the jobs-
thesis material in [[generative-ai-for-software-development-pereira]].

## Part 4: Organisation and Workflow

**Ch. 7 — Approach for the Identification of Requirements on the Design of
AI-supported Work Systems (in Problem-based Projects)** (Harlacher et al., 9
authors — RWTH/FH Aachen, German WIRKsam research project). Applied
methodology, field-tested across nine companies. Couples **CRISP-DM**
(technical pipeline) with a socio-technical process (APRODI's four-phase
Orientation→Focusing→Realisation→Stabilisation, SozioTex's human-technology-
organization/HTO iteration loops, and an AI-specific change-management
model) via **shared artefacts exchanged at defined handoff points**,
deliberately *not* interleaved into one synchronized pipeline — each team
keeps its own pace. Concrete toolkit: kickoff meeting, employee structure
analysis, a tech-affinity/culture/participation questionnaire (TA-EG-based
+ a "PASST" participation-ranking instrument), dual work-design analysis
(item-based + ethnographic observation), an "HTO workshop" surfacing which
functions AI should/shouldn't take over, and a socio-technical
specification catalogue. Central finding: "work processes do not always run
as they appear in manuals" — observed process beats documented process as
the spec baseline. **High Advisor-Builder value**: a concrete, sequenced
requirements-gathering playbook adaptable to small-business AI-adoption
engagements; the artefact-handoff-at-defined-gates coordination pattern is
structurally the same idea as this hub's MCP/Agents-SDK handoff findings,
applied at the human-process layer instead of the software layer.

**Ch. 8 — Plug and Play AI: How Companies Can Benefit from AI as a Service**
(Krüger, Stibe, Krüger). Formal taxonomy design (Nickerson, Varshney &
Muntermann 2013 method) over 553 candidate tools → 284 filtered products
(German AI Association membership, Capterra, Producthunt, 6 other sources;
15 explicit inclusion/exclusion filters; GPT-3/ChatGPT-assisted descriptions
cross-checked against scraped metadata; 4 coding iterations to stability).
Produces a citable taxonomy: **Code-Level** (NoCode/LowCode/ProCode),
**AI-Level** (AI-Tool < AI-Powered < AI-Model), **User** (five personas:
Domain Expert, AI Scientist, AI Operator, Maker, Anyone — each with a
worked example), and **AI Use Case** (Marketing & Sales, Chatbot Platform,
NLU, Generative AI-Text, Health/Pharma/Biotech, Automation, Manufacturing &
Engineering, Business Analytics, Rapid AI Model Dev & Deployment).
Counterintuitive finding: nearly every role×level combination exists in the
market except "Maker + AI-Model." Explicitly defines Plug and Play AI (=
NoCode+LowCode) as distinct from cloud-dependent AIaaS. **High value**: the
User-role × Code-Level × AI-Level cross-tab is a genuinely new client-
scoping lens ("does this client need a ProCode build, or does a
NoCode/LowCode tool already fit their use case and user population?") not
present in this hub's existing tool-landscape pages — but the specific named
tools are a **2022-23 snapshot, now stale**; the category structure is
durable, the vendor examples are not.

## Part 5: HR and Employment

**Ch. 9 — Developing Personas of Ideal-type Candidates in AI-related Jobs**
(Eichenberg, Pudill, Rüschoff, Stockem Novo, Vogelsang). Data-driven: 8,152
German AI-related job postings (Mar-Sep 2022) → cleaned to 2,240 → LDA topic
modelling (Gensim, coherence-tuned to 4 topics) plotted on two axes
(business-vs-technical; low-vs-high accountability). Four named personas:
**Junior Project Member** (low accountability, mixed background), **Senior
AI Manager** (high accountability, mixed background, customer-facing),
**Senior AI Architect** (high accountability, technical-only, Python/data-
science), **AI Developer** (low accountability, technical-only). Robustness
check: only 7/10 reruns on 90% subsamples replicated closely — a real,
disclosed limitation worth remembering before treating any single LDA run
as a stable finding. Reusable methodology for Advisor-Builder AI-hiring/
workforce conversations; the four personas are a ready-made vocabulary for
discussing AI team composition with SMB clients.

**Ch. 10 — Artificial Intelligence and Care Leaders: A Critical
Perspective** (Dandalt). Argumentative essay (not empirical): argues AI
won't displace physicians as "care leaders" because it can't replicate the
clinical+management skill blend, especially empathy. Cites: 60% of US
patients uncomfortable with AI-reliant care, only 38% believe AI improves
outcomes (Pew 2023); projected physician shortages (US 37,800-124,000 by
2034; Germany 106,000 by 2030); the "McDonaldisation" risk of de-
personalized, de-skilled medicine (physicians already spend 40% of time on
computers vs. 12% with patients); union/collective-bargaining resistance
(esp. France/Germany). Narrow healthcare-sociology domain study — no
`.ROOT` or general Advisor-Builder tie-back; citable only for a healthcare-
vertical client engagement.

## Part 6: Artificial Intelligence and Humans

**Ch. 11 — Public Perception of Artificial Intelligence: A Systematic
Evaluation of Newspaper Articles Using Sentiment Analysis** (Rana, Roemer,
Pitz, Sickmann). Sentiment analysis (R `syuzhet` package, NRC dictionary) of
2,240 articles from three German newspapers (2010-2022, tabloid/national/
regional). Findings: ~86% positive, ~1.5% neutral — far more positive than
expected; regional outlet Rheinische Post most positive (88.3%), tabloid
Bild most negative (12.67% negative share); coverage volume peaked 2018-19
(Cambridge Analytica era) then declined even as AI use rose; only ~30% of
articles engaged consumer-protection themes at all. Cross-checked against
TÜV-Verband public-opinion polling (positive sentiment 46%→51%, 2019-2021)
— media and public positivity move together, causality unestablished.
Directly reusable method template: a media-sentiment pipeline (scrape →
dedup → frequency-filter → dictionary sentiment → cross-check against
public polls) for any client-facing "how is AI perceived in
[industry/region]" deliverable; another public-trust data point alongside
[[work-trend-index-2024-2026]] and [[ai-index-2026]].

**Ch. 12 — Generational Differences in Framing for Social Robot Usage
Intention from a Consumer Behaviour Point of View** (Roth, Klicic).
Literature classification of social robots (embodiment × one-/two-way
communication) + n=17 semi-structured interviews (Jan 2023, Gen X/Y/Z) on
an education-sector application, analyzed for associative networks (three
content areas: appearance, features, human-robot relationship). Task
expectations rise by generation: Gen X expects simple physical assistance,
Gen Y expects communication/voice-assistant tasks, Gen Z expects an active
teaching/explanation role with higher autonomy. Applies Kahneman/Tversky
**risky-choice, attribute, and goal framing** theory to draft (not yet
tested) generation-specific adoption-messaging frames. Transferable
change-management/adoption-messaging technique — tailor AI-adoption pitches
by generational cohort using named frame types — domain content (social
robots) itself has no direct `.ROOT` tie.

**Ch. 13 — Towards a Structuralist Data Narratology** (Simon).
Structuralist (Todorov-based) analysis of 100 business data stories
(Tableau Public + Power BI galleries). Three recurring metanarratives:
**Compliance-Expansion** (35%, "plan executed"), **Rationalisation-
Reduction** (52%, dominant, "fixing what's broken"), **Transformation-
Change** (13%, rarest, richest/most interactive). Proposes a 5-level
AI-utilisation ladder for data storytelling (descriptive → explorative →
predictive → prescriptive → substantive/full NLU+NLG generation); current
commercial tools (Tableau Data Stories, Power BI Smart Narrative) sit only
at "prescriptive" — Tableau explicitly states its feature uses no
generative AI/LLMs (a dated-but-concrete vendor-capability data point,
worth re-verifying before citing since both products likely added genAI
since). Author's caution: fully AI-generated narratives risk being more
predictable/less "tellable" since AI reproduces existing patterns rather
than creating new meaning. Narrow relevance — useful only for a
BI/dashboard-narrative-tooling client question.

**Ch. 14 — Exploring the Adoption of AI for Customer Engagement Marketing
by Small and Medium Enterprises in South Africa: A Literature Review of
Challenges and Opportunities** (Mapila, Moloi — Johannesburg Business
School). Structured literature review (Scopus + Google Scholar, 2000-2023);
925 results narrowed to only 54 on adding "customer engagement," and only 3
South African studies matched at all — a real, disclosed research gap. The
**third chapter in this volume to independently apply TOE** (after Ch. 2
and Ch. 5) — see the cross-chapter pattern noted above. Produces two
literature-derived (unvalidated) checklists: **opportunities** (competitive
advantage, economies of scale, automated processes, 24/7 chatbot service,
increased profits/productivity, hidden-pattern decision support, process
accuracy, reliability) and **challenges** (no adoption strategy, resource/
expertise shortage, reliability concerns, data/security law compliance —
South Africa's POPI Act and EU GDPR both named, high investment cost,
integration difficulty, ethical concerns, perceived complexity, lack of
organisational/expert support, no risk-management framework, unclear ROI,
skills shortage, human resistance, algorithmic bias, weak government
support, job-displacement fear). Context: ~70% of South African CEOs agree
AI raises productivity, yet only ~30% intend significant investment — an
intent-action gap; South Africa leads Africa in AI startups/readiness but
has low AI-assistant usage (17% voice, 29% image, 33% translation) despite
~70% internet penetration. **High Advisor-Builder value** as a first-draft
discovery-interview checklist for SME AI-adoption engagements, particularly
in emerging-market or resource-constrained contexts — a Global-South data
point alongside Ch. 2, Ch. 5, and
[[business-case-for-ai-ganesan-leader-playbook]]; geography differs, but the
barrier categories (skills, cost, strategy, awareness) rhyme closely with
the German-market findings elsewhere in this same volume.

## Part 7: Forecasting

Three narrow, quantitative forecasting case studies — reference-only value
(named-model comparison evidence), no direct `.ROOT`/agent-pattern
tie-back, relevant chiefly if an Advisor-Builder client vertical touches
commodities, energy trading, or utility demand forecasting.

**Ch. 15 — Forecasting Brent Oil Volatility: DeepAR vs LSTM** (Köstner,
Llacay, Alaminos — Universitat de Barcelona). Univariate rolling-window
comparison (21/14/7-day-ahead). **DeepAR clearly outperforms LSTM on every
error metric** in every window, including through the 2020 COVID and 2022
Russia/Ukraine volatility shocks — notable since only univariate lagged
data was used, not DeepAR's full multi-series design strength. Authors flag
the missing GARCH-family baseline as a limitation.

**Ch. 16 — Energy Stock Price Forecast Based on Machine Learning and
Sentiment Analysis — Which Approach Performs Best in Day Trading?** (Vogt,
Bönner, Römmich, Weiß, Türkoglu — Hochschule Ruhr West/sipgate). Compared
GBRT, MLP, and LSTM on Uniper/Enel/EDF stock data (Jan 2019-Aug 2020) +
Twitter sentiment (VADER, machine-translated). **MLP had the lowest
prediction error** — a counterintuitive win over LSTM for time-series data.
Sentiment input improved simulated day-trading returns for all three
companies even where it *worsened* raw prediction error for two of them —
a real dissociation between point-accuracy and downstream decision quality,
a transferable AI-evaluation lesson (evaluate the actual decision metric,
not a proxy error metric).

**Ch. 17 — Optimising Water Supply: Application of Probabilistic Deep
Neural Networks to Forecast Water Demand in the Short Term** (Johnen,
Kley-Holsteg, Niemann, Ziel — University of Duisburg-Essen). The one
forecasting chapter where deep learning did **not** win outright: a linear
ARX-ARCH-Lasso model beat the proposed DNNAR(p) on every metric out-of-
sample, though a Diebold-Mariano significance test found the gap **not
statistically significant** — models are effectively tied. Weather data
gave the DNN model only a modest boost (+3.36% on the ES metric). Authors
recommend a hybrid linear+DNN approach and flag ReLU as a poor activation-
function choice for signed weather effects (Leaky ReLU/Tanh preferred).
Useful counter-example against reflexively assuming "more complex model =
better" without a rigor check.

## Back matter

List of Contributors, About the Editors (Isabel Lausberg — Professor of
Business/Management Accounting, HRW; co-director of HRW's "AI from an
Economic Perspective" research focus; certified data scientist; and Michael
Vogelsang — Professor of Economics, HRW; former Chief Economist, German
Association of SMEs), List of Figures, List of Tables — pure reference
material, no further content.

## Era and scope caveats

Conference held March 2023, published 2024 — pre-dates the current
generative-AI wave in most chapters except Ch. 8 (explicitly references
ChatGPT/GPT as a late-2022 development). Named vendor/tool landscapes
(Ch. 8's 284-product taxonomy) and dated statistics (unemployment rates,
CEO survey percentages, market-share snapshots) should be treated as
period evidence, not current facts — consistent with this hub's standing
era-warning pattern for vendor-landscape and dated-statistic sources. The
durable content is the frameworks and methodologies (TOE applications,
KI-AGIL, the AI-Reporting maturity model, SMACTR/audit frameworks, the
Plug-and-Play-AI taxonomy structure, the WIRKsam requirements playbook),
not the specific numbers or product names.

## Why this matters for `.ROOT` — summary

No single chapter here rises to landscape-research status on its own — this
is a proceedings volume of short papers, not a monograph. Its value is
breadth and convergence: five chapters (2, 5, 6, 7, 9) supply concretely
reusable Advisor-Builder material; three (1, 4, 8) add regulatory/
governance-landscape context; three (5, 11, 14) — with Ch. 2 as a fourth,
process-level instance — extend the hub's recurring verification-capacity/
trust-gates-adoption finding with new angles (a within-book TOE-framework
triple-convergence, media sentiment, an AI-maturity ladder for storytelling,
Global-South SME barriers); and the remaining chapters (3, 10, 12, 13,
15-17) are narrower empirical or human-factors evidence with little direct
agent-pattern relevance, honestly recorded as such rather than forced into
a false tie-back.
