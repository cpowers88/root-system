#!/usr/bin/env python3
"""Build a deterministic, read-only migration plan for metadata v2.

The script never edits vault targets. It maps every current audit finding to a
manual decision and separately lists only mechanically safe legacy conversions:
one plain timeline tag becomes the same `timeline:` property and is removed from
`tags`. Mixed controls, missing fields, and realm-specific meanings are not guessed.
"""

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import frontmatter_audit as audit

sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore

REPORT_DIR = audit.ROOT / "00-BRAIN" / "Session_Logs"


def finding_reason(kind: str) -> str:
    return {
        "missing_frontmatter": "frontmatter content requires human classification",
        "missing_type": "type cannot be inferred safely from path or filename",
        "timeline": "current action horizon requires human intent",
        "schema": "conflicting or invalid v2 control metadata requires review",
    }[kind]


def build_plan():
    result = audit.audit()
    safe = []
    inventory = Counter()
    finding_paths = {finding["path"] for finding in result["findings"]}

    for path in sorted(audit.ROOT.rglob("*.md")):
        rel = path.relative_to(audit.ROOT)
        if audit.EXCLUDED.intersection(rel.parts):
            continue
        fm = audit.parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        if fm is None or audit.property_from(fm, "timeline") is not None:
            continue
        tags = audit.tags_from(fm)
        controls = [
            tag for tag in tags if tag in audit.TIMELINE or audit.CONTROL.match(tag)
        ]
        for tag in controls:
            if tag in audit.TIMELINE:
                inventory["plain_timeline"] += 1
            elif tag.startswith("priority/"):
                inventory["reference_priority"] += 1
            elif tag.startswith("status/"):
                inventory["status"] += 1
            elif tag.startswith("stage-") or tag.startswith("phase-"):
                inventory["stage_or_phase"] += 1

        # Safe means the conversion can finish without leaving or creating a
        # second control interpretation. Mixed controls stay manual.
        if (
            len(controls) == 1
            and controls[0] in audit.TIMELINE
            and str(rel) not in finding_paths
        ):
            safe.append(
                {
                    "path": str(rel),
                    "set": {"timeline": controls[0]},
                    "remove_tags": [controls[0]],
                    "preserve_topic_tags": [tag for tag in tags if tag != controls[0]],
                }
            )

    finding_plan = [
        {
            "finding_id": finding["id"],
            "path": finding["path"],
            "kind": finding["kind"],
            "disposition": "manual_review",
            "reason": finding_reason(finding["kind"]),
        }
        for finding in result["findings"]
    ]

    plan = {
        "schema_version": 1,
        "mode": "read_only_dry_run",
        "source": "frontmatter_audit.py",
        "summary": {
            "files_checked": result["checked"],
            "current_findings": result["total"],
            "finding_identities_covered": len(finding_plan),
            "safe_complete_conversions": len(safe),
            "manual_decisions": len(finding_plan),
            "target_files_written": 0,
        },
        "legacy_control_inventory": dict(sorted(inventory.items())),
        "safe_complete_conversions": safe,
        "finding_plan": finding_plan,
    }
    canonical = json.dumps(plan, sort_keys=True, separators=(",", ":"))
    plan["plan_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return plan


def report_path(path: Path) -> Path:
    resolved = (path if path.is_absolute() else audit.ROOT / path).resolve()
    if (
        resolved.parent != REPORT_DIR  # type: ignore
        or resolved.suffix.lower() != ".json"
        or not resolved.name.startswith("ROOT_METADATA_MIGRATION_DRY_RUN_")
    ):
        raise ValueError(
            "report must be a ROOT_METADATA_MIGRATION_DRY_RUN_*.json file "
            "directly under 00-BRAIN/Session_Logs"
        )
    return resolved


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        help="write the dry-run report (never a migration target)",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="prove determinism and complete finding coverage",
    )
    args = parser.parse_args()

    first = build_plan()
    if args.self_test:
        second = build_plan()
        summary = first["summary"]
        covered = {item["finding_id"] for item in first["finding_plan"]}
        current = {item["id"] for item in audit.audit()["findings"]}
        passed = (
            first == second
            and covered == current
            and summary["finding_identities_covered"] == summary["current_findings"]
            and summary["target_files_written"] == 0
        )
        try:
            report_path(Path("NOW.md"))
            target_guard = False
        except ValueError:
            target_guard = True
        passed = passed and target_guard
        print(
            "# METADATA MIGRATION DRY-RUN SELF-TEST - " + ("PASS" if passed else "FAIL")
        )
        print(f"- deterministic plan hash: {first['plan_sha256']}")
        print(f"- finding identities covered: {len(covered)}/{len(current)}")
        print("- target files written: 0")
        print("- report path cannot resolve to a vault target")
        return 0 if passed else 1

    rendered = json.dumps(first, indent=2) + "\n"
    if args.output:
        try:
            output = report_path(args.output)
        except ValueError as exc:
            parser.error(str(exc))
        output.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"Dry-run report written: {output}")
        print(f"Plan SHA-256: {first['plan_sha256']}")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
