# Canonical consumption register

**Status:** Migration-control draft. This register records what promoted skills consume; it is not a source of clinical authority.

## Rule

A promoted skill applies the canonical drafts listed below and retains only its bounded application logic. Canonical drafts remain draft material; organisational policy and mandatory procedure take precedence. A reference in this register does not approve a model, threshold, destination, or procedure.

| Consumer | Canonical drafts consumed | Regression contracts | Boundary retained in consumer |
|---|---|---|---|
| Clinical Workflow Router | [Authority and uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md); [Behaviour, change and causality](/canonical/00-system-principles/behaviour-change-and-causality.md); [Immediate safety override](/canonical/01-immediate-safety/override-principle.md); [Escalation, oversight and decision locus](/canonical/06-escalation/decision-and-oversight.md) | CR-01, CR-02, CR-05, CR-10, CR-11, CR-12, CR-13, CR-16 | Selects a minimum necessary reasoning sequence; does not perform the destination skill’s reasoning. |
| Suicide Enquiry | [Authority and uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md); [Immediate safety override](/canonical/01-immediate-safety/override-principle.md); [Suicide enquiry chronology and evidence](/canonical/02-suicide-enquiry/case-chronology-and-evidence.md) | CR-01, CR-05, CR-06, CR-11, CR-12, CR-13 | Establishes enquiry material; does not formulate risk or choose a destination. |
| PORF Formulation | [Authority and uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md); [Behaviour, change and causality](/canonical/00-system-principles/behaviour-change-and-causality.md); [Immediate safety override](/canonical/01-immediate-safety/override-principle.md); [PORF reasoning boundaries](/canonical/03-formulation/porf-reasoning-boundaries.md) | CR-01, CR-02, CR-03, CR-05, CR-07, CR-11, CR-12, CR-13, CR-14 | Produces formulation-led clinical response reasoning; does not prescribe organisational procedure. |
| Contact Pattern Analysis | [Authority and uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md); [Behaviour, change and causality](/canonical/00-system-principles/behaviour-change-and-causality.md); [Contact pattern and function](/canonical/04-contact-pattern/pattern-and-function.md); [Escalation, oversight and decision locus](/canonical/06-escalation/decision-and-oversight.md) | CR-01, CR-02, CR-03, CR-04, CR-10, CR-11, CR-12, CR-13, CR-16 | Describes pattern and decision question; does not convert volume into risk or prescribe access restrictions. |
| CMP/Access Review | [Authority and uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md); [Behaviour, change and causality](/canonical/00-system-principles/behaviour-change-and-causality.md); [Immediate safety override](/canonical/01-immediate-safety/override-principle.md); [Intervention usability and access](/canonical/05-intervention/intervention-usability-and-access.md) | CR-01, CR-02, CR-03, CR-04, CR-05, CR-09, CR-11, CR-12, CR-13, CR-15, CR-16 | Reviews the clinical purpose and proportionality of access arrangements; cannot override immediate safety. |
| Safety Planning | [Authority and uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md); [Behaviour, change and causality](/canonical/00-system-principles/behaviour-change-and-causality.md); [Immediate safety override](/canonical/01-immediate-safety/override-principle.md); [Intervention usability and access](/canonical/05-intervention/intervention-usability-and-access.md) | CR-01, CR-02, CR-05, CR-08, CR-11, CR-12, CR-13 | Designs/reviews an intervention from established material; does not recreate enquiry/formulation or conceal a CMP. |
| CRG Triage | [Authority and uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md); [Behaviour, change and causality](/canonical/00-system-principles/behaviour-change-and-causality.md); [Immediate safety override](/canonical/01-immediate-safety/override-principle.md); [Escalation, oversight and decision locus](/canonical/06-escalation/decision-and-oversight.md) | CR-01, CR-02, CR-05, CR-10, CR-11, CR-12, CR-13 | Identifies the unresolved decision and appropriate decision locus; no service destination is approved here. |

## Verification before approval

Before any canonical draft is designated approved, update:

1. the model/policy source and version in [model-source-register.md](model-source-register.md);
2. the proposition’s classification in [provenance-register.md](provenance-register.md);
3. affected consumer rows in this register;
4. the applicable contracts in [canonical-reasoning-regression-spec.md](/tests/canonical-reasoning-regression-spec.md);
5. the approval decision, rationale, and regression result.
