import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("stale_overwrite_guard.py")
SPEC = importlib.util.spec_from_file_location("stale_overwrite_guard", SCRIPT)
guard = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = guard
SPEC.loader.exec_module(guard)


class StaleOverwriteGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.email", "test@example.invalid"], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "Test"], check=True)

    def tearDown(self):
        self.temp.cleanup()

    def commit(self, text, message):
        (self.root / "authority.md").write_text(text, encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", "authority.md"], check=True)
        subprocess.run(["git", "-C", str(self.root), "commit", "-qm", message], check=True)

    def test_exact_historical_reversion_blocks(self):
        old = "old\n" * 40
        self.commit(old, "old")
        self.commit("new\n" * 40, "new")
        (self.root / "authority.md").write_text(old, encoding="utf-8")
        findings = guard.inspect(self.root, ["authority.md"])
        self.assertIn("historical-reversion", {item.kind for item in findings})

    def test_material_shrink_blocks(self):
        self.commit("line\n" * 100, "baseline")
        (self.root / "authority.md").write_text("line\n" * 50, encoding="utf-8")
        findings = guard.inspect(self.root, ["authority.md"])
        self.assertIn("material-shrink", {item.kind for item in findings})

    def test_small_edit_passes(self):
        self.commit("line\n" * 100, "baseline")
        (self.root / "authority.md").write_text("line\n" * 99 + "changed\n", encoding="utf-8")
        self.assertEqual([], guard.inspect(self.root, ["authority.md"]))


if __name__ == "__main__":
    unittest.main()
