"""Deterministic tests for castle_freshness.py (flag #103).

Builds a throwaway CASTLE wiki in a temp dir per test and mocks Git explicitly.
Run: python 00-BRAIN/scripts/test_castle_freshness.py
"""

import datetime as dt
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest.mock import patch

import castle_freshness as cf

TODAY = dt.date(2026, 8, 19)


def make_vault(base: Path, *, reconciled="August 10, 2026",
               review_dates=("2026-08-23",), phase_status="planned",
               phase_window="August 24, 2026 – May 2027") -> Path:
    wiki = base / "00-BRAIN" / "CASTLE" / "wiki"
    (wiki / "phases").mkdir(parents=True)
    (wiki / "current-position.md").write_text(
        f"# Current Position\n\n### Reconciled: {reconciled}\n", encoding="utf-8")
    rows = "\n".join(
        f"| OPP-2026071{i}-01 | 2026-07-14 | t | s | [[a/b#x|link]] | parked | n "
        f"| realm | act | {d} | result |"
        for i, d in enumerate(review_dates))
    (wiki / "opportunity-queue.md").write_text(
        "# Queue\n\n| ID | ... | Review date | Result |\n|---|---|---|---|\n"
        + rows + "\n", encoding="utf-8")
    (wiki / "phases" / "phase-1-test.md").write_text(textwrap.dedent(f"""\
        ---
        type: phase
        status: {phase_status}
        ---
        # Phase 1
        **Window**: {phase_window}
        """), encoding="utf-8")
    (wiki / "log.md").write_text("# Log\n\n## 2026-08-19 — entry\n", encoding="utf-8")
    return base


class CastleFreshnessTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self._git_patch = patch("castle_freshness.subprocess.run")
        self.git_run = self._git_patch.start()
        self.git_run.return_value.stdout = ""
        self.addCleanup(self._git_patch.stop)

    def test_all_fresh_passes(self):
        self.assertEqual(cf.run(make_vault(self.base), TODAY), [])

    def test_stale_reconciliation_fails(self):
        root = make_vault(self.base, reconciled="July 1, 2026")  # 49 days
        findings = cf.run(root, TODAY)
        self.assertEqual(len(findings), 1)
        self.assertIn("reconciled", findings[0])

    def test_past_review_date_fails(self):
        root = make_vault(self.base, review_dates=("2026-08-01",))
        findings = cf.run(root, TODAY)
        self.assertEqual(len(findings), 1)
        self.assertIn("review date 2026-08-01 is past", findings[0])

    def test_missing_review_date_fails(self):
        root = make_vault(self.base, review_dates=("—",))
        findings = cf.run(root, TODAY)
        self.assertEqual(len(findings), 1)
        self.assertIn("missing", findings[0])

    def test_wikilink_pipes_do_not_shift_cells(self):
        # The evidence cell contains [[page|label]]; a naive split would
        # misread the review-date column. A future date must still pass.
        root = make_vault(self.base, review_dates=("2026-12-31",))
        self.assertEqual(cf.run(root, TODAY), [])

    def test_planned_phase_with_open_window_fails(self):
        root = make_vault(self.base, phase_window="August 1, 2026 – May 2027")
        findings = cf.run(root, TODAY)
        self.assertEqual(len(findings), 1)
        self.assertIn("planned but its window opened", findings[0])

    def test_active_phase_past_window_fails_after_grace(self):
        root = make_vault(self.base, phase_status="active",
                          phase_window="July 2026")
        findings = cf.run(root, TODAY)  # closed Jul 31; 19 days > 14 grace
        self.assertEqual(len(findings), 1)
        self.assertIn("window closed", findings[0])

    def test_active_phase_inside_grace_passes(self):
        root = make_vault(self.base, phase_status="active",
                          phase_window="July 2026")
        self.assertEqual(cf.run(root, dt.date(2026, 8, 10)), [])  # 10 <= 14

    def test_window_parser(self):
        cases = [
            ("July 2026", dt.date(2026, 7, 1), dt.date(2026, 7, 31)),
            ("Aug 2026 – May 2027", dt.date(2026, 8, 1), dt.date(2027, 5, 31)),
            ("Feb – Mar 2027", dt.date(2027, 2, 1), dt.date(2027, 3, 31)),
            ("August 24, 2026 – May 2027 (Fall + Spring)",
             dt.date(2026, 8, 24), dt.date(2027, 5, 31)),
            ("2028", dt.date(2028, 1, 1), dt.date(2028, 12, 31)),
            ("2030 – mid 2031", dt.date(2030, 1, 1), dt.date(2031, 12, 31)),
        ]
        for window, start, end in cases:
            with self.subTest(window=window):
                self.assertEqual(cf.parse_window(window), (start, end))

    def test_git_failure_is_a_gate_error(self):
        root = make_vault(self.base)
        wiki = root / "00-BRAIN" / "CASTLE" / "wiki"
        self.git_run.side_effect = OSError("git unavailable")
        with self.assertRaisesRegex(RuntimeError, "git history unavailable"):
            cf.check_log_recency(root, wiki, TODAY)

    def test_expired_now_review_trigger_fails(self):
        root = make_vault(self.base)
        (root / "active.md").write_text(textwrap.dedent("""\
            ---
            type: plan
            timeline: now
            review_trigger: 2026-08-18
            tags: []
            ---
            # Active
            """), encoding="utf-8")
        findings = cf.run(root, TODAY)
        self.assertEqual(len(findings), 1)
        self.assertIn("review_trigger 2026-08-18 is past", findings[0])

    def test_future_now_review_trigger_passes(self):
        root = make_vault(self.base)
        (root / "active.md").write_text(textwrap.dedent("""\
            ---
            type: plan
            timeline: now
            review_trigger: 2026-08-20
            tags: []
            ---
            # Active
            """), encoding="utf-8")
        self.assertEqual(cf.run(root, TODAY), [])


if __name__ == "__main__":
    unittest.main()
