---
type: map
timeline: reference
status: active
reference_priority: core
tags: [physics, textbook, sources]
created: 2026-08-08
confidence: verified
verified_on: 2026-08-08
---

# Textbook Page Map — Serway & Jewett 10e

**What this owns:** the chapter → printed-page → PDF-page → file mapping for
`raw/textbook/`, and the offset between the two page numberings.

**What it does not own:** what to read when — that is
[[semester-pathway]] — or what a chapter contains — that is `wiki/stages/`.

## The offset — read this before opening a PDF

> **PDF page = printed page + 30.**

The split files restart their viewer page count. Convert a global PDF page to a
local viewer page as follows:

| File | Local viewer page |
|---|---|
| `0001-0100` | global PDF page |
| `0101-0200` | global PDF page − 100 |
| `0201-0300` | global PDF page − 200 |
| `0301-0400` | global PDF page − 300 |
| `0401-0500` | global PDF page − 400 |
| `0501-0600` | global PDF page − 500 |

Verified 2026-08-08 by extracting the running header from every page of all six
chunk files: 479 of ~481 headers agree on an offset of exactly 30.

**Every page number cited anywhere in this wiki is a printed page number.** That
convention was correct but undocumented until today. The consequence of not
knowing it: opening `Physics book-0001-0100.pdf` and jumping to "page 95" for
Chapter 5 lands on printed page 65 — Chapter 3, Vectors. Two chapters early, no
error message.

Spot-verified against chapter openers: Ch 4 opener is printed 68 / PDF 98;
Ch 15 opener is printed 386 / PDF 416. Both exactly +30.

## Coverage — exact §54 scope

The captured chunks hold **PDF pp. 1–600 = printed pp. −29 to 570**, which covers
**Chapters 1 through 21** complete.

**Every chapter on the active Fall path (Ch 1–12, Ch 15, and §§16.1–16.3) is
fully on disk.** Chapters 13, 14, 17, and 38 remain durable reference material,
but the exact Fall 2026 §54 syllabus does not assign them.

The gap at PDF 601–1200 is Chapters 22–37 — thermodynamics, electricity and
magnetism, optics. Physics II material, correctly excluded. `1201-1300-part-2`
(12 pp.) and `1301-1370` (70 pp.) hold the modern-physics tail used by Stage 18,
which is off the active path.

## Chapter map

Chapter start = the opener spread, which sits two pages before the first running
header. End = the page before the next chapter's opener. Treat boundaries as ±1;
they are exact enough to open the right page and land on the right chapter.

| Ch | Title | Printed | PDF | File |
|---:|---|---|---|---|
| 1 | Physics and Measurement | 2–19 | 32–49 | `0001-0100` |
| 2 | Motion in One Dimension | 20–51 | 50–81 | `0001-0100` |
| 3 | Vectors | 52–67 | 82–97 | `0001-0100` |
| 4 | Motion in Two Dimensions | 68–93 | 98–123 | `0001-0100` → `0101-0200` |
| 5 | The Laws of Motion | 94–125 | 124–155 | `0101-0200` |
| 6 | Circular Motion and Other Applications | 126–149 | 156–179 | `0101-0200` |
| 7 | Energy of a System | 150–179 | 180–209 | `0101-0200` → `0201-0300` |
| 8 | Conservation of Energy | 180–209 | 210–239 | `0201-0300` |
| 9 | Linear Momentum and Collisions | 210–247 | 240–277 | `0201-0300` |
| 10 | Rotation of a Rigid Object | 248–283 | 278–313 | `0201-0300` → `0301-0400` |
| 11 | Angular Momentum | 284–311 | 314–341 | `0301-0400` |
| 12 | Static Equilibrium and Elasticity | 312–331 | 342–361 | `0301-0400` |
| 13 | Universal Gravitation *(off active path)* | 332–357 | 362–387 | `0301-0400` |
| 14 | Fluid Mechanics *(off active path)* | 358–385 | 388–415 | `0301-0400` → `0401-0500` |
| 15 | Oscillatory Motion | 386–413 | 416–443 | `0401-0500` |
| 16 | Wave Motion *(§§16.1–16.3 active only)* | 414–449 | 444–479 | `0401-0500` |
| 17 | Superposition and Standing Waves *(off active path)* | 450–481 | 480–511 | `0401-0500` → `0501-0600` |
| 18 | Temperature *(Physics II)* | 482–501 | 512–531 | `0501-0600` |

File names are `Physics book-<range>.pdf` in `raw/textbook/`.

### Chapters that span two files

Three active-path chapters cross a chunk boundary — 4, 7, and 10. Opening the
chapter start and reading forward will run off the end of the file.

## Semester mapping

The exact lecture-by-lecture sections, printed pages, and **local split-file
viewer pages** live in [[phys-2211-17-week-math-first-plan#Exact lecture reading
schedule]]. That table supersedes the earlier neighbor-section estimate that
appeared here.

## How this was verified

`pypdf` extraction of the running header from every page of the six sequential
chunk files. Headers carry both the printed page number and the chapter number
and title, so the map is read off the book itself rather than inferred from
chapter-length averages. Method and the two spot checks are reproducible; nothing
here is estimated.

Related: [[source-map]] · [[semester-pathway]] ·
[[phys-2211-17-week-math-first-plan]] · [[current-position]]
