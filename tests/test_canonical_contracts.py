"""Repository-level architecture checks for canonical reasoning contracts.

Run from the repository root:
    python3 -m unittest tests/test_canonical_contracts.py
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

SKILL_DEPENDENCIES = {
    "clinical-workflow-router": {"00-system-principles/authority-and-uncertainty.md", "00-system-principles/behaviour-change-and-causality.md", "01-immediate-safety/override-principle.md", "06-escalation/decision-and-oversight.md"},
    "suicide-enquiry": {"00-system-principles/authority-and-uncertainty.md", "01-immediate-safety/override-principle.md", "02-suicide-enquiry/case-chronology-and-evidence.md"},
    "porf-formulation": {"00-system-principles/authority-and-uncertainty.md", "00-system-principles/behaviour-change-and-causality.md", "01-immediate-safety/override-principle.md", "03-formulation/porf-reasoning-boundaries.md"},
    "contact-pattern-analysis": {"00-system-principles/authority-and-uncertainty.md", "00-system-principles/behaviour-change-and-causality.md", "04-contact-pattern/pattern-and-function.md", "06-escalation/decision-and-oversight.md"},
    "cmp-access-review": {"00-system-principles/authority-and-uncertainty.md", "00-system-principles/behaviour-change-and-causality.md", "01-immediate-safety/override-principle.md", "05-intervention/intervention-usability-and-access.md"},
    "safety-planning": {"00-system-principles/authority-and-uncertainty.md", "00-system-principles/behaviour-change-and-causality.md", "01-immediate-safety/override-principle.md", "05-intervention/intervention-usability-and-access.md"},
    "crg-triage": {"00-system-principles/authority-and-uncertainty.md", "00-system-principles/behaviour-change-and-causality.md", "01-immediate-safety/override-principle.md", "06-escalation/decision-and-oversight.md"},
}
CANONICAL_DRAFTS = set().union(*SKILL_DEPENDENCIES.values())

class CanonicalContractTests(unittest.TestCase):
    def read(self, relative_path):
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_promoted_skills_declare_exact_dependencies(self):
        for skill, expected in SKILL_DEPENDENCIES.items():
            content = self.read(f"skills/{skill}/SKILL.md")
            self.assertIn("## Canonical dependencies", content, skill)
            self.assertEqual(expected, set(re.findall(r"\]\(/canonical/([^)]+)\)", content)), skill)

    def test_dependency_targets_remain_drafts(self):
        for relative_path in CANONICAL_DRAFTS:
            self.assertIn("**Status:** DRAFT", self.read(f"canonical/{relative_path}"), relative_path)

    def test_contract_specification_contains_all_fifteen_contracts(self):
        content = self.read("tests/canonical-reasoning-regression-spec.md")
        self.assertEqual({f"CR-{number:02d}" for number in range(1, 17)}, set(re.findall(r"\bCR-\d\d\b", content)))
        self.assertIn("necessary but not sufficient for live use", content)
        self.assertIn("Policy-conformance tests", content)

    def test_source_lifecycle_and_governance_safeguards_are_present(self):
        content = self.read("governance/organisational-source-register.md")
        self.assertIn("Identified → acquired → controlled status verified → rule mapped → approved for operational reliance", content)
        self.assertIn("preserve that uncertainty", content)
        self.assertIn("revert to provisional status", content)
        self.assertIn("not evidence that a canonical rule is organisationally approved", content)

    def test_acquisition_criteria_require_stable_rule_mapping_and_conflict_handling(self):
        content = self.read("governance/organisational-source-acquisition-register.md")
        self.assertIn("specific section, heading or other stable locator", content)
        self.assertIn("conflict with another controlled source", content)
        self.assertIn("fully support, partially support or do not support", content)
        self.assertIn("Lifeline contact-data definitions / proposed data dictionary", content)
        self.assertIn("not what contact meant", content)

if __name__ == "__main__":
    unittest.main()
