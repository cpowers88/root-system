"""Focused negative tests for frontmatter_audit register enforcement."""

import unittest

import frontmatter_audit as fa


class RegisterMetadataTests(unittest.TestCase):
    def test_approved_register_on_instruction_interface_passes(self):
        fm = "type: pointer\ntimeline: reference\nregister: ai-loader\ntags: [governance]"
        self.assertEqual(fa.metadata_findings(fm, "AGENTS.md"), ([], []))

    def test_retired_register_value_fails(self):
        fm = "type: report\ntimeline: log\nregister: system-review\ntags: []"
        _, findings = fa.metadata_findings(fm, "report.md")
        self.assertIn("invalid register: system-review", findings)

    def test_valid_register_on_report_still_fails_scope(self):
        fm = "type: report\ntimeline: log\nregister: ai-loader\ntags: []"
        _, findings = fa.metadata_findings(fm, "report.md")
        self.assertEqual(findings, ["register not allowed on non-instruction file"])

    def test_duplicate_register_fails(self):
        fm = ("type: pointer\ntimeline: reference\nregister: ai-loader\n"
              "register: ai-profile\ntags: [governance]")
        _, findings = fa.metadata_findings(fm, "AGENTS.md")
        self.assertIn("duplicate register property", findings)


if __name__ == "__main__":
    unittest.main()
