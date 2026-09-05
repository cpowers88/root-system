#!/usr/bin/env python3
"""Run the canonical read-only `.ROOT` health scopes.

Default mode gates new/blocker regressions against the reviewed frontmatter
baseline. `--strict` requires zero wiki review debt and zero frontmatter debt.
Exit 0 means no blocker in the named scopes; it does not claim semantic freshness.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "00-BRAIN" / "scripts"
BASELINE = SCRIPTS / "frontmatter_baseline.json"
TEXT_SCAN_EXCLUDED = {
    "99-ARCHIVE", "raw", ".git", ".obsidian", "88-JOURNAL",
    "Report Archive",
    # vendored third-party distribution (Oracle JDK); its legal/ tree ships
    # hundreds of .md license files that are not vault prose (added 2026-08-02)
    "oracleJdk-26",
}
NOT_EVALUATED = [
    "semantic freshness and current project truth",
    "review-cadence completion outside CASTLE's named freshness checks",
    "source ownership/routing and duplicate-source disposition",
    "all ordinary direct-path prose outside the checked boot/wiki contracts",
]


def run(name: str, command: list[str], parse_json: bool = False) -> dict:
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {
            "name": name,
            "returncode": 1,
            "status": "BLOCKER",
            "data": None,
            "parse_error": None,
            "stdout": "",
            "stderr": f"child check could not complete: {exc}",
        }
    parsed = None
    parse_error = None
    if parse_json:
        try:
            parsed = json.loads(completed.stdout)
        except json.JSONDecodeError as exc:
            parse_error = str(exc)
    return {
        "name": name,
        "returncode": completed.returncode,
        "status": "PASS" if completed.returncode == 0 and not parse_error else "BLOCKER",
        "data": parsed,
        "parse_error": parse_error,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def text_integrity() -> dict:
    findings = []
    checked = 0
    disallowed = set(range(0, 9)) | {11, 12} | set(range(14, 32))
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if TEXT_SCAN_EXCLUDED.intersection(rel.parts):
            continue
        # rglob("*.md") also matches directories whose name ends in .md
        # (e.g. the JDK module dir legal/jdk.internal.md)
        if not path.is_file():
            continue
        checked += 1
        data = path.read_bytes()
        bad_controls = sorted({byte for byte in data if byte in disallowed})
        bare_cr = sum(
            1 for index, byte in enumerate(data)
            if byte == 13 and (index + 1 == len(data) or data[index + 1] != 10)
        )
        if bad_controls or bare_cr:
            findings.append({
                "path": str(rel),
                "control_bytes": bad_controls,
                "bare_cr": bare_cr,
            })
    return {
        "name": "live Markdown text integrity",
        "returncode": 1 if findings else 0,
        "status": "BLOCKER" if findings else "PASS",
        "data": {"files_checked": checked, "findings": findings},
        "parse_error": None,
        "stdout": "",
        "stderr": "",
    }


def public_check(check: dict) -> dict:
    data = check["data"] or {}
    summary = None
    if check["name"] == "wiki links and navigation":
        summary = {
            key: data.get(key)
            for key in (
                "status", "scanned_hubs", "vault_pages", "blockers",
                "review_debt", "expected",
            )
        }
    elif check["name"] == "frontmatter and timeline metadata":
        comparison = data.get("comparison") or {}
        summary = {
            "status": data.get("status"),
            "mode": data.get("mode"),
            "files_checked": data.get("files_checked"),
            "counts": data.get("counts"),
            "comparison": {
                "baseline_total": comparison.get("baseline_total"),
                "unchanged_total": comparison.get("unchanged_total"),
                "new": comparison.get("new", []),
                "resolved": comparison.get("resolved", []),
            } if comparison else None,
        }
    elif check["name"] == "live Markdown text integrity":
        summary = data
    result = {
        "name": check["name"],
        "returncode": check["returncode"],
        "status": check["status"],
        "data": summary,
        "parse_error": check["parse_error"],
    }
    if check["status"] == "BLOCKER" and check["stderr"]:
        result["error"] = check["stderr"]
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true",
                        help="require zero wiki review and frontmatter debt")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable summary")
    parser.add_argument("--verbose", action="store_true",
                        help="include child-check output in the human report")
    args = parser.parse_args()

    wiki_command = [sys.executable, str(SCRIPTS / "wiki_lint.py"),
                    "--strict", "--json"]
    frontmatter_command = [sys.executable, str(SCRIPTS / "frontmatter_audit.py"),
                           "--json"]
    if args.strict:
        wiki_command.append("--fail-on-review")
        frontmatter_command.append("--strict")
    else:
        frontmatter_command.extend(["--baseline", str(BASELINE)])

    checks = [
        run("boot and governance", [
            sys.executable, str(SCRIPTS / "validate_boot_chain.py")]),
        run("wiki links and navigation", wiki_command, parse_json=True),
        run("frontmatter and timeline metadata", frontmatter_command,
            parse_json=True),
        run("CASTLE freshness and review triggers", [
            sys.executable, str(SCRIPTS / "castle_freshness.py")]),
        run("shared skill mirrors", [
            sys.executable, str(SCRIPTS / "sync_shared_skills.py"), "--check"]),
        run("unstaged whitespace", ["git", "diff", "--check"]),
        run("staged whitespace", ["git", "diff", "--cached", "--check"]),
        text_integrity(),
    ]

    failed = [check for check in checks if check["status"] == "BLOCKER"]
    wiki = checks[1]["data"] or {}
    frontmatter = checks[2]["data"] or {}
    wiki_review = int(wiki.get("review_debt", 0))
    frontmatter_total = int(frontmatter.get("counts", {}).get("total", 0))
    debt = wiki_review + frontmatter_total
    strict_debt_names = set()
    if args.strict and checks[1] in failed and not wiki.get("blockers"):
        strict_debt_names.add(checks[1]["name"])
    if (
        args.strict and checks[2] in failed and frontmatter_total
        and checks[2]["parse_error"] is None
    ):
        strict_debt_names.add(checks[2]["name"])
    hard_blockers = [
        check for check in failed if check["name"] not in strict_debt_names
    ]
    overall = (
        "BLOCKER" if hard_blockers else
        "STRICT_FAILURE" if failed else
        "PASS_WITH_DEBT" if debt else "PASS"
    )

    result = {
        "overall": overall,
        "mode": "strict" if args.strict else "reviewed-baseline",
        "exit_code": 1 if failed else 0,
        "debt": {
            "wiki_review": wiki_review,
            "frontmatter_reviewed_baseline": frontmatter_total,
        },
        "checks": [public_check(check) for check in checks],
        "not_evaluated": NOT_EVALUATED,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("# .ROOT HEALTH")
        print(f"\nOverall: **{overall.replace('_', ' ')}**")
        print(f"Mode: {'zero-debt strict' if args.strict else 'reviewed baseline'}\n")
        for check in checks:
            label = check["status"]
            data = check["data"] or {}
            detail = ""
            if check["name"] == "wiki links and navigation":
                detail = (
                    f" - blockers {data.get('blockers', '?')}; review "
                    f"{data.get('review_debt', '?')}; expected {data.get('expected', '?')}"
                )
                if check["returncode"] == 0 and data.get("review_debt"):
                    label = "REVIEW DEBT"
            elif check["name"] == "frontmatter and timeline metadata":
                counts = data.get("counts", {})
                comparison = data.get("comparison") or {}
                detail = f" - total {counts.get('total', '?')}"
                if not args.strict:
                    detail += (
                        f"; new {len(comparison.get('new', []))}; "
                        f"resolved {len(comparison.get('resolved', []))}"
                    )
                if check["returncode"] == 0 and counts.get("total"):
                    label = "BASELINE DEBT"
            elif check["name"] == "live Markdown text integrity":
                detail = (
                    f" - {data.get('files_checked', '?')} files; "
                    f"{len(data.get('findings', []))} findings"
                )
            if check["name"] in strict_debt_names:
                label = "STRICT DEBT"
            print(f"- {label}: {check['name']}{detail}")
            if args.verbose and (check["stdout"] or check["stderr"]):
                for line in (check["stdout"] + "\n" + check["stderr"]).strip().splitlines():
                    print(f"    {line}")
        print("\nNot evaluated by this gate:")
        for scope in NOT_EVALUATED:
            print(f"- {scope}")
        print("\nExit meaning: 0 = no blocker/new baseline debt in named scopes; "
              "1 = blocker or strict zero-debt failure. Debt remains visible "
              "and is not called clean.")

    return result["exit_code"]


if __name__ == "__main__":
    sys.exit(main())
