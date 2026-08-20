"""Regression checks for the canonical reasoning architecture.

Run from the repository root:
    python3 -m unittest tests/test_canonical_contracts.py
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

SKILL_DEPENDENCIES = {
    "clinical-workflow-router": {
        "00-system-principles/authority-and-uncertainty.md",
        "00-system-principles/behaviour-change-and-causality.md",
        "01-immediate-safety/override-principle.md",
        "06-escalation/decision-and-oversight.md",
    },
    "suicide-enquiry": {
        "00-system-principles/authority-and-uncertainty.md",
        "01-immediate-safety/override-principle.md",
        "02-suicide-enquiry/case-chronology-and-evidence.md",
    },
    "porf-formulation": {
        "00-system-principles/authority-and-uncertainty.md",
        "00-system-principles/behaviour-change-and-causality.md",
        "01-immediate-safety/override-principle.md",
        "03-formulation/porf-reasoning-boundaries.md",
    },
    "contact-pattern-analysis": {
        "00-system-principles/authority-and-uncertainty.md",
        "00-system-principles/behaviour-change-and-causality.md",
        "04-contact-pattern/pattern-and-function.md",
        "06-escalation/decision-and-oversight.md",
    },
    "cmp-access-review": {
        "00-system-principles/authority-and-uncertainty.md",
        "00-system-principles/behaviour-change-and-causality.md",
        "01-immediate-safety/override-principle.md",
        "05-intervention/intervention-usability-and-access.md",
    },
    "safety-planning": {
        "00-system-principles/authority-and-uncertainty.md",
        "00-system-principles/behaviour-change-and-causality.md",
        "01-immediate-safety/override-principle.md",
        "05-intervention/intervention-usability-and-access.md",
    },
    "crg-triage": {
        "00-system-principles/authority-and-uncertainty.md",
        "00-system-principles/behaviour-change-and-causality.md",
        "01-immediate-safety/override-principle.md",
        "06-escalation/decision-and-oversight.md",
    },
}

CANONICAL_DRAFTS = set().union(*SKILL_DEPENDENCIES.values())


class CanonicalContractTests(unittest.TestCase):
    def read(self, relative_path):
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_every_promoted_skill_declares_exact_dependencies(self):
        for skill, expected in SKILL_DEPENDENCIES.items():
            content = self.read(f"skills/{skill}/SKILL.md")
            self.assertIn("## Canonical dependencies", content, skill)
            actual = set(re.findall(r"\]\(/canonical/([^)]+)\)", content))
            self.assertEqual(expected, actual, skill)

    def test_all_dependency_targets_exist_and_remain_drafts(self):
        for relative_path in CANONICAL_DRAFTS:
            content = self.read(f"canonical/{relative_path}")
            self.assertIn("**Status:** DRAFT", content, relative_path)

    def test_regression_spec_is_complete_and_preserves_governance_boundary(self):
        content = self.read("tests/canonical-reasoning-regression-spec.md")
        self.assertEqual(
            {f"CR-{number:02d}" for number in range(1, 12)},
            set(re.findall(r"\bCR-\d\d\b", content)),
        )
        self.assertIn("None authorises Helpline", content)

    def test_consumption_register_matches_promoted_consumers(self):
        content = self.read("governance/canonical-consumption-register.md")
        for skill in SKILL_DEPENDENCIES:
            display_name = {
                "clinical-workflow-router": "Clinical Workflow Router",
                "suicide-enquiry": "Suicide Enquiry",
                "porf-formulation": "PORF Formulation",
                "contact-pattern-analysis": "Contact Pattern Analysis",
                "cmp-access-review": "CMP/Access Review",
                "safety-planning": "Safety Planning",
                "crg-triage": "CRG Triage",
            }[skill]
            self.assertIn(display_name, content)

    def test_organisational_rules_remain_blocked_without_controlled_source(self):
        content = self.read("governance/organisational-source-acquisition-register.md")
        for required_document in (
            "Lifeline immediate-safety and safeguarding procedure",
            "Lifeline CMP/contact-management policy",
            "CRG guide/remit and destination decision tool",
        ):
            self.assertIn(required_document, content)
        self.assertIn("not evidence that an existing skill rule is approved", content)


if __name__ == "__main__":
    unittest.main()
