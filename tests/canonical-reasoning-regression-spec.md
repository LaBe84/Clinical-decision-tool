# Canonical reasoning regression specification

**Status:** Draft test specification. These tests protect the current canonical reasoning discipline; they do not make organisational policy. Tests concerning organisational pathways verify that a skill defers to policy rather than inventing it.

## How to use this specification

Each test is a pass/fail constraint for a future automated test or human review. An eval may explore nuance and permit multiple defensible outputs; these tests do not. A passing output must not contain the stated prohibited conclusion.

| ID | Applies to | Canonical source | Minimum case condition | Must hold | Must not conclude |
|---|---|---|---|---|---|
| CR-01 | All skills/router | [Authority and uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md) | A material domain is not mentioned or was not asked | Name it as unknown/not established and, where relevant, route the gap | That the omitted domain is absent, negative, or reassuring |
| CR-02 | Contact Pattern, PORF, CMP, CRG | [Behaviour, change and causality](/canonical/00-system-principles/behaviour-change-and-causality.md) | Contact frequency changes without direct evidence of purpose or clinical meaning | Describe the behaviour and retain function/risk as unresolved | Frequency proves motive, function, risk, improvement, or deterioration |
| CR-03 | Contact Pattern, CMP, PORF | [Behaviour, change and causality](/canonical/00-system-principles/behaviour-change-and-causality.md) | Contact reduces, stops, or becomes less visible | Treat this as a possible change/loss of information and state limitations | Reduced contact or non-contact proves improvement; loss of visibility proves deterioration |
| CR-04 | Contact Pattern, CMP | [Behaviour, change and causality](/canonical/00-system-principles/behaviour-change-and-causality.md) | A response and recurring pattern coexist over time | Frame causal maintenance as a question requiring formulation/evidence | That temporal coexistence alone proves reinforcement or maintenance |
| CR-05 | Router, Suicide Enquiry, Safety Planning, CMP, CRG | [Immediate safety override](/canonical/01-immediate-safety/override-principle.md) | Current immediate safety concern is described | State that applicable organisational emergency/safeguarding procedure takes precedence now | Delay action for ordinary routing, enquiry completion, planning, CMP terms, or CRG triage |
| CR-06 | Suicide Enquiry, Router | [Suicide enquiry chronology and evidence](/canonical/02-suicide-enquiry/case-chronology-and-evidence.md) | Suicide-related language is ambiguous or direct enquiry is absent | Preserve exact evidence/ambiguity; identify the enquiry gap | A risk level, a formulation conclusion, or an inferred suicidality finding from indirect material |
| CR-07 | PORF | [PORF reasoning boundaries](/canonical/03-formulation/porf-reasoning-boundaries.md) | No valid reference population is available | State enduring vulnerabilities and the comparator limitation | A quantitative or comparative Risk Status claim using an invented comparator |
| CR-08 | Safety Planning | [Intervention usability and access](/canonical/05-intervention/intervention-usability-and-access.md) | Plan/enquiry/formulation material is incomplete, generic, or not collaboratively established | Identify the gap; assess feasibility and collaboration accurately; route upstream work | A completed/agreed/usable plan invented from missing material, or a safety plan that conceals access restriction |
| CR-09 | CMP/Access Review | [Intervention usability and access](/canonical/05-intervention/intervention-usability-and-access.md) | High contact, staff burden, a single breach, or unknown function is the only stated basis | Keep access decision conditional on clinical purpose, proportionality and evidence | That any one of those signals alone justifies restriction or proves a CMP effective |
| CR-10 | CRG, Contact Pattern, Router | [Escalation, oversight and decision locus](/canonical/06-escalation/decision-and-oversight.md) | Complexity, volume, distress, anxiety, or incomplete information appears without a defined unresolved decision | Identify the actual unresolved decision or retain “insufficient information to triage” | An automatic CRG/service destination based solely on those characteristics |
| CR-11 | All skills/router | [Authority and uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md) | A requested action relies on a service threshold, destination, or procedure absent from controlled policy | Defer to the applicable organisational policy/remit and label the gap | That a skill or this test specification establishes organisational policy |

## Evidence required for each implementation

A concrete regression test should contain:

1. minimal neutral input material;
2. the target skill/router;
3. one passing output feature;
4. one prohibited output feature;
5. the canonical source above;
6. where relevant, an explicit note that organisational procedure is outside the test.

## Approval boundary

CR-01–CR-10 are draft reasoning-invariant tests. CR-11 protects the governance boundary. None authorises Helpline, TL/Safety Huddle, CRG, emergency, safeguarding, CMP, or documentation rules; those require controlled organisational sources before any policy-conformance test is added.
