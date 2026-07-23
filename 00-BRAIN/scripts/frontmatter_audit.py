#!/usr/bin/env python3
"""frontmatter_audit.py — Metadata Standard enforcement.

Checks every live .md in .ROOT against WHERE_IT_GOES.md § Metadata Standard:

  - frontmatter block present
  - `type:` present
  - v2: one valid `timeline:` property and no legacy control tags
  - transition: exactly one legacy timeline-like tag remains accepted
  - optional `stage:`, `status:`, and `reference_priority:` are validated

Default mode reports without failing. `--strict` requires zero debt. `--baseline`
fails only for finding identities not present in a reviewed baseline. `--json`
provides machine-readable output; `--write-baseline` intentionally refreshes the
reviewed baseline artifact.
"""

import argparse
from datetime import date
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED = {"99-ARCHIVE", "raw", ".raw ARCHIVE", ".git", ".obsidian",
            "Report Archive", "77-INBOX", "88-JOURNAL", ".claude", ".agents",
            "SKILLS"}
TIMELINE = {"now", "next", "later", "parked", "reference", "log"}
REFERENCE_PRIORITY = {"core", "supporting", "lookup"}
NATIVE = re.compile(r"^(priority/\w+|stage-\d+|phase-(\d+|all)|stage-all)$")
CONTROL = re.compile(
    r"^(priority/[a-z0-9_-]+|status/[a-z0-9_-]+|stage-\d+|"
    r"phase-(\d+|all)|stage-all)$")


def parse_frontmatter(text: str):
    if not text.lstrip().startswith("---"):
        return None
    body = text.lstrip()[3:]
    end = body.find("\n---")
    if end == -1:
        return None
    return body[:end]


def tags_from(fm: str):
    tags = []
    inline = re.search(r"^tags:\s*\[([^\]]*)\]", fm, re.M)
    if inline:
        tags = [t.strip().strip("'\"") for t in inline.group(1).split(",") if t.strip()]
    else:
        block = re.search(r"^tags:\s*\n((?:\s+-\s+.+\n?)+)", fm, re.M)
        if block:
            tags = [ln.strip().lstrip("- ").strip().strip("'\"")
                    for ln in block.group(1).splitlines() if ln.strip()]
    return tags


def property_from(fm: str, name: str):
    """Return None when absent, otherwise the unquoted scalar (possibly empty)."""
    match = re.search(rf"^{re.escape(name)}:\s*([^#\n]*?)\s*$", fm, re.M)
    if not match:
        return None
    return match.group(1).strip().strip("'\"")


def property_count(fm: str, name: str):
    return len(re.findall(rf"^{re.escape(name)}:", fm, re.M))


def metadata_findings(fm: str):
    """Return timeline and v2-schema details for one frontmatter block."""
    tags = tags_from(fm)
    timeline = property_from(fm, "timeline")
    timeline_details = []
    schema_details = []

    if timeline is None:
        legacy = [tag for tag in tags if tag in TIMELINE or NATIVE.match(tag)]
        if len(legacy) != 1:
            timeline_details.append(", ".join(legacy or ["<none>"]))
        return timeline_details, schema_details

    if timeline not in TIMELINE:
        timeline_details.append(f"property:{timeline or '<empty>'}")

    for name in ("type", "timeline", "stage", "status",
                 "reference_priority", "tags"):
        if property_count(fm, name) > 1:
            schema_details.append(f"duplicate {name} property")

    legacy_controls = [
        tag for tag in tags if tag in TIMELINE or CONTROL.match(tag)
    ]
    for tag in legacy_controls:
        schema_details.append(f"legacy control tag with v2 properties: {tag}")

    for name in ("stage", "status"):
        value = property_from(fm, name)
        if value == "":
            schema_details.append(f"empty {name} property")
        elif value is not None and value.startswith(("[", "{")):
            schema_details.append(f"non-scalar {name} property")
    reference_priority = property_from(fm, "reference_priority")
    if reference_priority is not None and reference_priority not in REFERENCE_PRIORITY:
        schema_details.append(
            "invalid reference_priority: " + (reference_priority or "<empty>"))
    return timeline_details, schema_details


def audit():
    missing_fm, missing_type, timeline_bad, schema_bad = [], [], [], []
    checked = 0

    for p in sorted(ROOT.rglob("*.md")):
        if EXCLUDED.intersection(p.relative_to(ROOT).parts):
            continue
        checked += 1
        rel = p.relative_to(ROOT)
        fm = parse_frontmatter(p.read_text(encoding="utf-8-sig", errors="replace"))
        if fm is None:
            missing_fm.append(str(rel))
            continue
        if not re.search(r"^type:\s*\S+", fm, re.M):
            missing_type.append(str(rel))
        timeline_details, schema_details = metadata_findings(fm)
        for detail in timeline_details:
            timeline_bad.append((str(rel), [detail]))
        for detail in schema_details:
            schema_bad.append((str(rel), detail))

    findings = []
    findings.extend({"kind": "missing_frontmatter", "path": path, "detail": ""}
                    for path in missing_fm)
    findings.extend({"kind": "missing_type", "path": path, "detail": ""}
                    for path in missing_type)
    findings.extend({"kind": "timeline", "path": path, "detail": ", ".join(tags)}
                    for path, tags in timeline_bad)
    findings.extend({"kind": "schema", "path": path, "detail": detail}
                    for path, detail in schema_bad)
    for finding in findings:
        finding["id"] = "|".join(
            (finding["kind"], finding["path"], finding["detail"]))
    return {
        "checked": checked,
        "missing_frontmatter": missing_fm,
        "missing_type": missing_type,
        "timeline_bad": timeline_bad,
        "schema_bad": schema_bad,
        "findings": findings,
        "total": len(findings),
    }


def resolve_path(path: Path) -> Path:
    return path if path.is_absolute() else ROOT / path


def print_report(result, comparison=None):
    missing_fm = result["missing_frontmatter"]
    missing_type = result["missing_type"]
    timeline_bad = result["timeline_bad"]
    schema_bad = result["schema_bad"]
    checked = result["checked"]

    print("# FRONTMATTER / METADATA AUDIT")
    print(f"\nFiles checked: {checked}\n")
    print(f"## Missing frontmatter ({len(missing_fm)})")
    for f in missing_fm or []:
        print(f"- `{f}`")
    if not missing_fm:
        print("- none")
    print(f"\n## Missing `type:` ({len(missing_type)})")
    for f in missing_type or []:
        print(f"- `{f}`")
    if not missing_type:
        print("- none")
    print(f"\n## Timeline missing or invalid ({len(timeline_bad)})")
    for f, tl in timeline_bad or []:
        print(f"- `{f}` — has: {', '.join(tl)}")
    if not timeline_bad:
        print("- none")
    print(f"\n## Invalid v2 schema ({len(schema_bad)})")
    for f, detail in schema_bad or []:
        print(f"- `{f}` — {detail}")
    if not schema_bad:
        print("- none")
    total = result["total"]
    print(f"\n**Total findings: {total}** — "
          f"{'CLEAN' if total == 0 else 'fix at reviews per Metadata Standard'}")
    if comparison is not None:
        print("\n## Reviewed baseline comparison")
        print(f"- reviewed baseline debt: {comparison['baseline_total']}")
        print(f"- unchanged baseline debt: {comparison['unchanged_total']}")
        print(f"- new debt: {len(comparison['new'])}")
        print(f"- resolved since baseline: {len(comparison['resolved'])}")
        status = "REGRESSION" if comparison["new"] else "BASELINE MATCH"
        print(f"- status: **{status}**")
        for finding_id in comparison["new"][:40]:
            print(f"  - NEW `{finding_id}`")
        if len(comparison["new"]) > 40:
            print(f"  - ... {len(comparison['new']) - 40} more new finding(s)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 when any finding exists")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable results")
    parser.add_argument("--baseline", type=Path,
                        help="fail only for finding identities absent from baseline")
    parser.add_argument("--write-baseline", type=Path,
                        help="write the current reviewed finding identities")
    parser.add_argument("--self-test", action="store_true",
                        help="prove identity comparison catches equal-count substitution")
    args = parser.parse_args()
    if args.self_test:
        baseline_ids = {"missing_type|old.md|", "timeline|same.md|<none>"}
        current_ids = {"missing_type|new.md|", "timeline|same.md|<none>"}
        new = current_ids - baseline_ids
        resolved = baseline_ids - current_ids
        legacy_ok = metadata_findings("type: note\ntags: [now, topic]") == ([], [])
        v2_ok = metadata_findings(
            "type: note\ntimeline: now\nstatus: active\ntags: [topic]") == ([], [])
        dual_timeline, dual_schema = metadata_findings(
            "type: note\ntimeline: now\nstage: 2\ntags: [now, stage-2, topic]")
        bad_priority = metadata_findings(
            "type: note\ntimeline: reference\nreference_priority: urgent\ntags: [topic]")
        bad_stage = metadata_findings(
            "type: note\ntimeline: next\nstage: [2, 3]\ntags: [topic]")
        duplicate_timeline = metadata_findings(
            "type: note\ntimeline: now\ntimeline: next\ntags: [topic]")
        passed = (
            len(current_ids) == len(baseline_ids)
            and new == {"missing_type|new.md|"}
            and resolved == {"missing_type|old.md|"}
            and legacy_ok and v2_ok
            and not dual_timeline and len(dual_schema) == 2
            and bad_priority == ([], ["invalid reference_priority: urgent"])
            and bad_stage == ([], ["non-scalar stage property"])
            and duplicate_timeline == ([], ["duplicate timeline property"])
        )
        print("# FRONTMATTER / METADATA SELF-TEST - " + ("PASS" if passed else "FAIL"))
        print("- equal total counts still expose one new and one resolved identity")
        print("- legacy and valid v2 metadata are accepted")
        print("- dual controls and invalid reference priority are rejected")
        print("- non-scalar and duplicate control properties are rejected")
        return 0 if passed else 1
    if args.strict and args.baseline:
        parser.error("choose --strict or --baseline")
    if args.write_baseline and (args.strict or args.baseline):
        parser.error("--write-baseline cannot be combined with --strict or --baseline")

    result = audit()
    current_ids = {finding["id"] for finding in result["findings"]}
    comparison = None

    if args.write_baseline:
        baseline_path = resolve_path(args.write_baseline)
        baseline = {
            "schema_version": 1,
            "reviewed_date": date.today().isoformat(),
            "finding_count": result["total"],
            "finding_ids": sorted(current_ids),
        }
        baseline_path.write_text(
            json.dumps(baseline, indent=2) + "\n", encoding="utf-8", newline="\n")

    if args.baseline:
        baseline_path = resolve_path(args.baseline)
        try:
            baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
            baseline_ids = set(baseline["finding_ids"])
        except FileNotFoundError:
            print(f"MISSING frontmatter baseline: {baseline_path}", file=sys.stderr)
            return 1
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            print(f"INVALID frontmatter baseline: {exc}", file=sys.stderr)
            return 1
        comparison = {
            "baseline_total": len(baseline_ids),
            "unchanged_total": len(current_ids & baseline_ids),
            "new": sorted(current_ids - baseline_ids),
            "resolved": sorted(baseline_ids - current_ids),
        }

    machine = {
        "status": (
            "REGRESSION" if comparison and comparison["new"] else
            "CLEAN" if result["total"] == 0 else "BASELINE_DEBT"
        ),
        "mode": (
            "write-baseline" if args.write_baseline else
            "baseline" if args.baseline else
            "strict" if args.strict else "report"
        ),
        "files_checked": result["checked"],
        "counts": {
            "missing_frontmatter": len(result["missing_frontmatter"]),
            "missing_type": len(result["missing_type"]),
            "timeline": len(result["timeline_bad"]),
            "schema": len(result["schema_bad"]),
            "total": result["total"],
        },
        "comparison": comparison,
        "findings": result["findings"],
    }
    if args.json:
        print(json.dumps(machine, indent=2))
    else:
        print_report(result, comparison)
        if args.write_baseline:
            print(f"\nBaseline written: {resolve_path(args.write_baseline)}")

    if args.strict and result["total"]:
        return 1
    if comparison and comparison["new"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
