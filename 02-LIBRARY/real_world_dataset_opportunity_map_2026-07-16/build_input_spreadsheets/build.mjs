import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputDir = "C:/Users/chris/.ROOT/outputs/real_world_dataset_opportunity_map_2026-07-16";
await fs.mkdir(outputDir, { recursive: true });

const wb = Workbook.create();
const decision = wb.worksheets.add("Decision Map");
const inventory = wb.worksheets.add("Dataset Inventory");
const pilot = wb.worksheets.add("Pilot Plan");
const scoring = wb.worksheets.add("Scoring");

const navy = "#17324D";
const blue = "#2F75B5";
const paleBlue = "#D9EAF7";
const paleGreen = "#E2F0D9";
const paleGold = "#FFF2CC";
const paleRed = "#FCE4D6";
const white = "#FFFFFF";
const grid = "#D9E1F2";
const dark = "#1F2937";

function titleBand(sheet, range, text) {
  sheet.getRange(range).merge();
  const cell = sheet.getRange(range.split(":")[0]);
  cell.values = [[text]];
  cell.format = {
    fill: navy,
    font: { color: white, bold: true, size: 18 },
    verticalAlignment: "center",
  };
  sheet.getRange(range).format.rowHeight = 32;
}

function header(range) {
  range.format = {
    fill: blue,
    font: { color: white, bold: true },
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "all", style: "thin", color: white },
  };
  range.format.rowHeight = 34;
}

for (const sheet of [decision, inventory, pilot, scoring]) sheet.showGridLines = false;

// Scoring model first so all cross-sheet formulas have targets.
titleBand(scoring, "A1:D1", "Dataset Opportunity Scoring Model");
scoring.getRange("A3:D3").values = [["Criterion", "Weight", "What a 5 Means", "Why It Matters"]];
header(scoring.getRange("A3:D3"));
scoring.getRange("A4:D9").values = [
  ["Goal relevance", 0.30, "Directly advances the construction / real-estate Advisor-Builder wedge", "Prevents interesting-but-detached analysis"],
  ["Decision actionability", 0.25, "Changes whom to contact, what to build, or what to stop", "Data must support a decision"],
  ["Local granularity", 0.15, "County, city, address, or project level", "Chris needs a reachable market, not only national context"],
  ["Freshness", 0.15, "Current and updated at least monthly", "Old data can misdirect present action"],
  ["Access ease", 0.10, "Download/API works without payment or account friction", "Supports autonomous repeatable work"],
  ["Repeatability", 0.05, "Stable schema and scheduled refresh path", "Makes dashboards and monitoring viable"],
];
scoring.getRange("B4:B9").format.numberFormat = "0%";
scoring.getRange("A11:D11").values = [["Rating", "Meaning", "Use", "Guardrail"]];
header(scoring.getRange("A11:D11"));
scoring.getRange("A12:D16").values = [
  [5, "Excellent", "Default first-wave source", "Still verify definitions and coverage"],
  [4, "Strong", "Use when it sharpens the pilot", "Document any access friction"],
  [3, "Useful context", "Add only after the core question is clear", "Do not let context become scope creep"],
  [2, "Weak fit", "Trigger-only", "Needs a specific question before use"],
  [1, "Poor fit", "Park", "Do not ingest for completeness"],
];
scoring.getRange("A18:D20").values = [
  ["Selection rule", "Start with the smallest source combination that changes a decision.", null, null],
  ["Evidence rule", "Public data can identify market flow and targets; it cannot prove willingness to pay.", null, null],
  ["Stop rule", "If the work produces only ‘construction is active,’ stop and return to a sharper question.", null, null],
];
scoring.getRange("A18:A20").format = { fill: paleGold, font: { bold: true } };
scoring.getRange("B18:D20").merge(true);

// Ranked inventory.
titleBand(inventory, "A1:T1", "Real-World Dataset Opportunity Inventory — Construction / Real Estate");
inventory.getRange("A2:T2").merge();
inventory.getRange("A2").values = [["Ranked for an autonomous, decision-bearing Atlanta-area pilot. Scores are formula-driven from the Scoring sheet."]];
inventory.getRange("A2:T2").format = { fill: paleBlue, font: { italic: true, color: dark }, wrapText: true };
inventory.getRange("A4:T4").values = [[
  "Priority Rank", "Dataset", "Owning Agency", "Decision Question", "Geographic Level", "Freshness / Cadence",
  "Key Fields", "Access Method", "API Key?", "Goal Relevance", "Actionability", "Local Granularity",
  "Freshness", "Access Ease", "Repeatability", "Weighted Score", "Recommended Use", "Important Limitation",
  "Official Source", "Activation Status"
]];
header(inventory.getRange("A4:T4"));

const rows = [
  ["Atlanta Building Permit Tracker", "City of Atlanta Department of City Planning", "Which project types and locations are moving through the city now?", "City / address / permit", "Bi-weekly", "Permit status, type, address, valuation, dates; export availability", "Interactive tracker with export", "No", 5, 5, 5, 4, 4, 4, "Project-level follow-on after county baseline", "City limits only; field coverage must be verified after export", "https://gis.atlantaga.gov/", "Next"],
  ["Census Building Permits Survey", "U.S. Census Bureau", "Where is residential construction flow growing, and in what unit mix?", "National / state / CBSA / county / place", "Monthly, YTD, annual", "Permits, units by structure size, valuation", "CSV / text downloads", "No", 5, 5, 4, 5, 5, 5, "Core project-flow signal for the first pilot", "Residential permitting is not total construction demand", "https://www.census.gov/construction/bps/index.html", "Now"],
  ["Quarterly Census of Employment and Wages", "U.S. Bureau of Labor Statistics", "Which counties have enough construction-business capacity to support a reachable niche?", "County / state / industry", "Quarterly / annual", "Establishments, employment, wages, location quotients, NAICS", "CSV slices and ZIP downloads", "No", 5, 4, 4, 4, 5, 5, "Core capacity signal paired with BPS", "Suppression and publication lag affect detailed cells", "https://www.bls.gov/cew/additional-resources/open-data/home.htm", "Now"],
  ["SAM.gov Contract Opportunities", "U.S. General Services Administration", "What active public construction solicitations fit a chosen geography or NAICS?", "Notice / place of performance", "Daily active updates", "NAICS, set-aside, dates, place, status, notice text", "Search without account; API with key", "Yes for API", 4, 4, 3, 5, 2, 4, "Trigger-only public-demand scan", "Federal opportunities are not representative of private contractors", "https://open.gsa.gov/api/get-opportunities-public-api/", "Trigger-only"],
  ["USAspending Contract Awards", "U.S. Department of the Treasury", "Who has actually won federal construction work, where, and for how much?", "Award / recipient / place", "Frequently updated", "Award amount, recipient, agency, NAICS/PSC, dates, location", "Open API and downloads", "No", 4, 3, 3, 5, 5, 5, "Validate awarded federal demand after a SAM signal", "Awards show government buying, not private pain or willingness to pay", "https://api.usaspending.gov/", "Trigger-only"],
  ["County Business Patterns", "U.S. Census Bureau", "How many establishments operate in each construction specialty by county?", "County / state / ZIP / NAICS", "Annual", "Establishments, employment, payroll, establishment size", "Census API / downloads", "Yes for API", 4, 3, 5, 2, 2, 4, "Deepen niche sizing after QCEW identifies a county", "Latest release lags and API now requires a key", "https://www.census.gov/data/developers/data-sets/cbp-zbp/cbp-api.html", "Next"],
  ["ACS 5-Year Housing", "U.S. Census Bureau", "What housing stock and household conditions shape renovation or development context?", "County to block group", "Annual 5-year estimates", "Housing age, tenure, vacancy, value, income, commuting", "Census API / downloads", "Usually key for API", 3, 2, 5, 3, 4, 5, "Context only after a construction niche is chosen", "Estimates and margins of error are not project demand", "https://www.census.gov/programs-surveys/acs/data/data-via-api.html", "Parked"],
  ["National Risk Index", "Federal Emergency Management Agency", "Which hazard exposures could materially affect property or project decisions?", "County / census tract", "Periodic", "Expected annual loss, social vulnerability, resilience, hazard scores", "Data download / web services", "No", 3, 3, 5, 2, 5, 4, "Add only for a risk-specific property question", "Not a lead list and not proof of immediate buying behavior", "https://www.fema.gov/flood-maps/products-tools/national-risk-index", "Parked"],
];

const values = rows.map((r) => [null, ...r.slice(0, 8), ...r.slice(8, 14), null, ...r.slice(14)]);
inventory.getRange("A5:T12").values = values;
for (let row = 5; row <= 12; row += 1) {
  inventory.getRange(`P${row}`).formulas = [[`=ROUND(J${row}*Scoring!$B$4+K${row}*Scoring!$B$5+L${row}*Scoring!$B$6+M${row}*Scoring!$B$7+N${row}*Scoring!$B$8+O${row}*Scoring!$B$9,2)`]];
  inventory.getRange(`A${row}`).formulas = [[`=RANK.EQ(P${row},$P$5:$P$12,0)`]];
}
inventory.getRange("A5:A12").format.numberFormat = "0";
inventory.getRange("J5:O12").format.numberFormat = "0";
inventory.getRange("P5:P12").format.numberFormat = "0.00";
inventory.getRange("T5:T12").dataValidation = { rule: { type: "list", values: ["Now", "Next", "Trigger-only", "Parked"] } };
inventory.getRange("P5:P12").conditionalFormats.add("colorScale", { colors: ["#F8696B", "#FFEB84", "#63BE7B"] });
inventory.getRange("T5:T12").conditionalFormats.add("containsText", { text: "Now", format: { fill: paleGreen, font: { bold: true, color: "#375623" } } });
inventory.getRange("A4:T12").format.borders = { preset: "all", style: "thin", color: grid };
inventory.getRange("A5:T12").format = { wrapText: true, verticalAlignment: "top" };
inventory.tables.add("A4:T12", true, "DatasetOpportunityTable").style = "TableStyleMedium2";
inventory.freezePanes.freezeRows(4);

// Pilot plan.
titleBand(pilot, "A1:F1", "Recommended Pilot — Atlanta-Area Construction Opportunity Baseline");
pilot.getRange("A3:B8").values = [
  ["Pilot decision", "Which nearby counties show enough residential construction flow and construction-business capacity to justify observation conversations and future estimating/workflow research?"],
  ["Core sources", "Census Building Permits Survey + BLS QCEW"],
  ["Bounded geography", "Cobb, Fulton, Cherokee, Paulding, Bartow, Forsyth, Douglas, and Gwinnett counties"],
  ["Time window", "2021–2025 annual trend; latest available quarterly context where useful"],
  ["Final artifact", "Private Looker Studio dashboard plus a one-page decision note"],
  ["Success test", "A sharper county + contractor segment + observation question emerges"],
];
pilot.getRange("A3:A8").format = { fill: paleBlue, font: { bold: true }, wrapText: true };
pilot.getRange("B3:B8").format = { wrapText: true, verticalAlignment: "top" };
pilot.getRange("A10:F10").values = [["Phase", "Work", "Primary Source", "Metrics / Fields", "Decision Output", "Stop / Continue Gate"]];
header(pilot.getRange("A10:F10"));
pilot.getRange("A11:F15").values = [
  ["1 — Flow", "Load 2021–2025 county residential permit totals and unit mix", "Census BPS", "Permits; units; 1-unit, 2-unit, 3–4, 5+; valuation; YoY change", "Rank counties by construction flow and direction", "Continue only if counties separate meaningfully"],
  ["2 — Capacity", "Add construction establishments, employment, wages, and location quotient", "BLS QCEW", "NAICS 23 and selected subsectors; establishments; employment; average weekly wage; LQ", "Identify reachable contractor density and specialty candidates", "Continue only if a narrower segment becomes plausible"],
  ["3 — Projects", "Export city permit records for the strongest question", "Atlanta Permit Tracker", "Type, status, address, valuation, issue date, contractor if present", "Create a project-level observation sample", "Stop if export fields cannot support the chosen question"],
  ["4 — Public demand", "Scan solicitations and awards only when public work becomes relevant", "SAM.gov + USAspending", "NAICS, place, deadlines, award recipients and amounts", "Test whether public procurement is a distinct lane", "Do not mix federal demand with private-contractor proof"],
  ["5 — Human proof", "Use findings to frame one non-sales observation conversation", "Explicit user approval required", "Pain frequency, workaround, consequences, existing spend, willingness to try", "B2 evidence: advance, revise, or kill", "Data is context; conversation is demand proof"],
];
pilot.getRange("A17:F19").values = [
  ["Autonomous next action", "Build Phase 1 + Phase 2 source tables and dashboard skeleton; no outreach and no Python-school edits.", null, null, null, null],
  ["Hard stop", "If the result says only ‘construction is active,’ park the analysis. It has not earned more data.", null, null, null, null],
  ["Why this pilot", "It joins project flow with industry capacity, stays local, uses official repeatable sources, and creates a concrete question for real-world validation.", null, null, null, null],
];
pilot.getRange("A17:A19").format = { fill: paleGold, font: { bold: true } };
pilot.getRange("B17:F19").merge(true);
pilot.getRange("B17:F19").format = { wrapText: true };
pilot.getRange("A10:F15").format.borders = { preset: "all", style: "thin", color: grid };
pilot.getRange("A11:F15").format = { wrapText: true, verticalAlignment: "top" };
pilot.freezePanes.freezeRows(10);

// Executive decision map.
titleBand(decision, "A1:H1", "Real-World Data: The Next Autonomous Move");
decision.getRange("A3:H4").merge();
decision.getRange("A3").values = [["Use real-world data when it narrows a decision. Start with Atlanta-area construction flow (BPS) + business capacity (QCEW), then earn project-level detail. Do not ingest datasets merely because they exist."]];
decision.getRange("A3:H4").format = { fill: paleGreen, font: { bold: true, color: "#375623", size: 13 }, wrapText: true, verticalAlignment: "center" };
decision.getRange("A6:B10").values = [
  ["Selected pilot", "Atlanta-Area Construction Opportunity Baseline"],
  ["Top core source", "Census Building Permits Survey"],
  ["Second core source", "BLS QCEW"],
  ["Number of sources ranked", null],
  ["Highest weighted score", null],
];
decision.getRange("B9").formulas = [["=COUNTA('Dataset Inventory'!B5:B12)"]];
decision.getRange("B10").formulas = [["=MAX('Dataset Inventory'!P5:P12)"]];
decision.getRange("B10").format.numberFormat = "0.00";
decision.getRange("A6:A10").format = { fill: paleBlue, font: { bold: true } };
decision.getRange("A6:B10").format.borders = { preset: "all", style: "thin", color: grid };
decision.getRange("D6:H6").merge();
decision.getRange("D6").values = [["Decision sequence"]];
decision.getRange("D6:H6").format = { fill: blue, font: { color: white, bold: true } };
decision.getRange("D7:H11").values = [
  ["1", "Question", "Where is flow + capacity concentrated?", "Output", "County/segment shortlist"],
  ["2", "Baseline", "BPS + QCEW", "Output", "Comparable metrics"],
  ["3", "Detail", "City permit export only if earned", "Output", "Observation sample"],
  ["4", "Human proof", "One approved conversation", "Output", "Advance / revise / kill"],
  ["5", "Guardrail", "No sharper target = stop", "Output", "Avoid analysis theater"],
];
decision.getRange("D7:H11").format = { wrapText: true, verticalAlignment: "center", borders: { preset: "all", style: "thin", color: grid } };
decision.getRange("A13:H15").values = [
  ["What I can do without Chris", "Download official BPS/QCEW files, normalize county/NAICS fields, document lineage, create the private dashboard skeleton, and write a decision note.", null, null, null, null, null, null],
  ["What waits for Chris", "Any contractor outreach, spending, account creation/API-key action, or change to Python-school/shared operating state.", null, null, null, null, null, null],
  ["System-growth principle", "Prefer an evidence loop (question → data → decision → human test) over adding more architecture or bulk ingestion.", null, null, null, null, null, null],
];
decision.getRange("A13:A15").format = { fill: paleGold, font: { bold: true } };
decision.getRange("B13:H15").merge(true);
decision.getRange("B13:H15").format = { wrapText: true };
decision.freezePanes.freezeRows(4);

// Sizing and final polish.
decision.getRange("A:H").format.columnWidth = 16;
decision.getRange("A:A").format.columnWidth = 24;
decision.getRange("B:B").format.columnWidth = 38;
decision.getRange("D:D").format.columnWidth = 7;
decision.getRange("E:E").format.columnWidth = 15;
decision.getRange("F:F").format.columnWidth = 34;
decision.getRange("G:G").format.columnWidth = 12;
decision.getRange("H:H").format.columnWidth = 24;

inventory.getRange("A:A").format.columnWidth = 11;
inventory.getRange("B:B").format.columnWidth = 28;
inventory.getRange("C:C").format.columnWidth = 25;
inventory.getRange("D:D").format.columnWidth = 38;
inventory.getRange("E:F").format.columnWidth = 22;
inventory.getRange("G:H").format.columnWidth = 35;
inventory.getRange("I:P").format.columnWidth = 13;
inventory.getRange("Q:R").format.columnWidth = 34;
inventory.getRange("S:S").format.columnWidth = 44;
inventory.getRange("T:T").format.columnWidth = 15;
inventory.getRange("A5:T12").format.rowHeight = 76;

pilot.getRange("A:A").format.columnWidth = 22;
pilot.getRange("B:B").format.columnWidth = 42;
pilot.getRange("C:C").format.columnWidth = 24;
pilot.getRange("D:F").format.columnWidth = 34;
pilot.getRange("A11:F15").format.rowHeight = 74;

scoring.getRange("A:A").format.columnWidth = 24;
scoring.getRange("B:B").format.columnWidth = 20;
scoring.getRange("C:D").format.columnWidth = 52;
scoring.getRange("A4:D20").format.wrapText = true;

// Inspect key regions and formula outputs before export.
const inventoryInspect = await wb.inspect({ kind: "region", sheetId: "Dataset Inventory", range: "A4:T12", maxChars: 5000 });
const formulaInspect = await wb.inspect({ kind: "formula", sheetId: "Dataset Inventory", range: "A5:P12", maxChars: 4000, options: { maxResults: 40 } });
const errorInspect = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, maxChars: 3000 });

for (const sheetName of ["Decision Map", "Dataset Inventory", "Pilot Plan", "Scoring"]) {
  const preview = await wb.render({ sheetName, autoCrop: "all", scale: 0.85, format: "png" });
  const safeName = sheetName.toLowerCase().replaceAll(" ", "_");
  await fs.writeFile(`${outputDir}/${safeName}.png`, new Uint8Array(await preview.arrayBuffer()));
}

const xlsx = await SpreadsheetFile.exportXlsx(wb);
const xlsxPath = `${outputDir}/advisor_builder_dataset_opportunity_map.xlsx`;
await xlsx.save(xlsxPath);

console.log(JSON.stringify({
  xlsxPath,
  inventoryInspect: inventoryInspect.ndjson?.slice(0, 1200),
  formulaInspect: formulaInspect.ndjson?.slice(0, 1600),
  errorInspect: errorInspect.ndjson,
}, null, 2));
