#!/usr/bin/env python3
"""Fixture tests for the read-only path reference audit prototype."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from path_reference_audit import audit


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="root-path-audit-") as temp:
        root = Path(temp)
        write(root / "03-WIKIS" / "PHYSICS" / "wiki" / "index.md",
              "# Physics\n\n[[known]]\n[[known#Missing Heading]]\n[[missing]]\n")
        write(root / "03-WIKIS" / "PHYSICS" / "wiki" / "known.md",
              "# Present Heading\n")
        write(root / "03-WIKIS" / "PYTHON" / "wiki" / "index.md",
              "# Python\n\n[[known]]\n")
        write(root / "03-WIKIS" / "PYTHON" / "wiki" / "known.md",
              "# Python Known\n")

        baseline = root / "baseline.json"
        baseline.write_text(json.dumps({
            "rules": [{
                "id": "fixture-missing",
                "target_exact": ["missing"],
                "classification": "accepted-fixture",
            }]
        }), encoding="utf-8")

        report = audit(root, include_archive=False, baseline_path=baseline)
        kinds = report["issue_counts"]
        assert kinds.get("broken_anchor") == 1, kinds
        assert kinds.get("unresolved_wikilink") == 1, kinds
        assert report["baselined_count"] == 1, report
        assert report["unbaselined_count"] == 1, report

    print("path_reference_audit fixtures: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
