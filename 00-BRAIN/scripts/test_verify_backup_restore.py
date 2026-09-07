import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("verify_backup_restore.py")
SPEC = importlib.util.spec_from_file_location("verify_backup_restore", SCRIPT)
restore = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = restore
SPEC.loader.exec_module(restore)


class RestoreVerificationTests(unittest.TestCase):
    def test_latest_completed_snapshot_ignores_partial(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            complete = root / "2026-08-17_1200"
            partial = root / "2026-08-18_1200"
            complete.mkdir()
            partial.mkdir()
            (complete / restore.COMPLETE_MARKER).write_text("complete", encoding="utf-8")
            self.assertEqual([complete], restore.completed_snapshots(root))
            self.assertEqual(complete, restore.choose_source(root / "unused", root, True))

    def test_nonempty_restore_target_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            (target / "keep.txt").write_text("do not overwrite", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "must be empty"):
                restore.ensure_empty_target(target)

    def test_mirror_requires_sentinel(self):
        with tempfile.TemporaryDirectory() as directory:
            mirror = Path(directory)
            with self.assertRaisesRegex(ValueError, "sentinel"):
                restore.choose_source(mirror, None, False)

    def test_robocopy_summary_parser(self):
        output = "    Files :             5241\n    Bytes :       1812345678\n"
        self.assertEqual((5241, 1812345678), restore.summary(output))


if __name__ == "__main__":
    unittest.main()
