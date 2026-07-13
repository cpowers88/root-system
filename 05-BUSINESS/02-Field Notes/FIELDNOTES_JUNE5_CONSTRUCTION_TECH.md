---
type: log
tags: [log, business]
---

# FIELD NOTES — June 5, 2026
 #Start #log 
## Subject: Construction Industry — Operational Inefficiency as Business Opportunity
## Signal type: Build + Sell
## Source: Personal domain knowledge + strategic conversation with Claude

---

## What I observed

Construction jobsites — particularly small to mid-size GCs and specialty subs ($2M–$15M revenue) — run almost entirely on informal systems. Scheduling lives in a foreman's head. Accountability is visual and proximity-based. Change orders move slowly through phone calls and paper. Material tracking is manual. Crew productivity is invisible the moment someone rounds a corner.

The office layer is increasingly digitized (Procore, PlanGrid at the high end). The field layer is not. That gap is where margin dies on every job.

The core problem is not laziness — it is **visibility**. A foreman cannot manage what he cannot see. There is no feedback loop between "people on the clock" and "work actually moving."

---

## The friction I noticed

- No real-time field productivity visibility at the crew level
- Change orders and RFIs move slowly — primarily a communication and documentation handoff problem
- Material arrival, location, and consumption is tracked informally or not at all
- Daily time loss is never formally captured — material delays, waiting on inspections, crew waiting on crew, tool problems all disappear into "it just took longer"
- That untracked time directly corrupts future job estimates and scheduling
- Top-down tech solutions (Procore etc.) fail at field adoption because they were built for the office, not the foreman

---

## Who is involved

- Foremen — notoriously resistant to tech, but respond to tools that make their day easier not harder
- Small to mid-size GCs and specialty subs — can't afford enterprise software, underserved by current market
- Field crews — will not type, will use voice or 3-tap mobile input if it's simple enough

---

## What I think

The solution space requires field-first design. Any tool built top-down for reporting will be ignored. Any tool built to make the foreman's day easier will get used.

The right approach before building anything: spend 1-2 weeks following a foreman, then 1 week walking the job independently. Map what actually happens versus what's supposed to happen. Interview during natural downtime. The solutions will become obvious from direct observation — they always do.

This is a professional workflow audit applied to construction. The methodology is the same regardless of industry.

---

## Signal type breakdown

**Build signal:**
- Field productivity visibility tool — 3-tap daily crew check-in against task list
- Automated pace tracking — at current rate, are we on schedule? Surface to foreman by 10am
- Daily friction log — 2-minute end of day capture: what stopped work today? Builds estimation database over time
- Change order acceleration — voice memo → structured change order document automatically
- Material tracking — QR codes or RFID on materials, phone scan on arrival and use

**Sell signal:**
- Workflow audit offer — follow the foreman, map the gaps, deliver written report with tool recommendations and automation opportunities
- This is sellable before any software is built — the audit itself is the product first
- Natural entry: personal network in construction, speak the language, no trust barrier

---

## Why this industry specifically

- Asset-heavy, paper-heavy, relationship-driven, historically resistant to technology
- Enterprise solutions exist but don't reach the $2M–$15M contractor
- Cultural insider advantage — know how to talk to foremen, understand jobsite dynamics
- ISYE degree directly applicable — scheduling theory, operations research, productivity measurement, human factors
- Multiple problem layers visible from direct experience — not theoretical

---

## Broader principle confirmed

**Go find problems.** The business model stated plainly:
Find problems other people have normalized. Understand them better than anyone. Build the simplest possible solution. Charge for it.

This applies beyond construction. Construction is the highest-confidence entry point because of domain knowledge and cultural access. The methodology travels to any industry.

---

## Tools available to solve these problems

### Capture layer
- Mobile forms: JotForm, Google Forms, Typeform
- QR codes: free, works on any smartphone
- Voice input: Whisper (AI transcription) — converts speech to text
- Photos with metadata: GPS + timestamp built into every phone photo
- Wearables/sensors: GPS trackers, RFID tags, temperature/vibration sensors
- Computer vision: cameras that watch and count

### Move layer
- Make.com / Zapier: no-code automation between tools
- APIs: software talking to software via Python
- Twilio: automated texts and calls from any software
- Webhooks: real-time triggers between systems

### Store layer
- Google Sheets: simple structured data
- Airtable: no-code database
- SQLite / PostgreSQL: code-based database
- Notion: lightweight operational database

### Analyze layer
- Google Looker Studio: free dashboards from spreadsheet/database
- Python + pandas: complex data analysis
- SQL: query a database in plain English logic
- Claude/GPT API: plain-English analysis and summaries from raw data

### Act layer
- Automated alerts: threshold triggers → text foreman automatically
- Generated PDF reports: Python produces weekly/daily summaries
- AI-generated documents: voice memo → change order draft via Claude API
- Scheduling tools: Smartsheet, Google Sheets Gantt at small end

### Hardware
- Rugged tablets: Panasonic Toughbook, Samsung Galaxy Tab Active
- GPS trackers: $20-50 hardware, $10/month — know where every asset is
- RFID/barcode scanners: material tracking through a job
- Drones: site progress, surveying, inspection (FAA Part 107 for commercial use)
- Raspberry Pi / Arduino: $35 computers that make anything smart
- Smart PPE: hard hats and vests with sensors — early stage but real

---

## Technical capability roadmap noted

All of the following is reachable from current trajectory:

| Domain | Timeline | Connection to degree |
|---|---|---|
| Games (Unity/Unreal) | 2-3 years | Physics, state machines, AI behavior |
| Robotics (ROS + Python/C++) | 3-4 years | Control systems, kinematics, ISYE math |
| AI / Machine learning | 2 years | Linear algebra, probability, optimization |
| Systems automation / SCADA | 2-3 years | Core ISYE application |
| Embedded systems (C/C++) | 2 years | Hardware layer of everything smart |

The skeleton underneath all of it: State → Input → Logic → Output → Feedback. Same structure in every complex system regardless of domain.

---

## Next actions

- [ ] Park this as an active opportunity — revisit after July 4 when business track resumes
- [ ] Identify one contact in construction with field access for a future observation week
- [ ] Build the tools library in Notion Education Vault — living reference of what's possible
- [ ] Return to this note when ready to define first audit offer

---

## Connection to North Star

This is the clearest picture yet of where the business intersects personal domain knowledge, ISYE training, and technical capability. Construction is the highest-confidence entry point. The methodology (find problems, audit the workflow, build the simplest solution) travels to any industry.

The degree is not a detour. It is the credential that makes the conversation credible.

---

*Field Notes logged: June 5, 2026 | Session with Claude*
*Review at: July 4, 2026 — business track resumes*
