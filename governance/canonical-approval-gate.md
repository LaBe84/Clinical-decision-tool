# Canonical approval gate

**Review status:** NO CANONICAL DRAFT IS APPROVED.

This review assesses whether the current drafts are eligible to become authoritative. It is a governance readiness review, not clinical-model adoption or organisational approval.

## Review outcome

| Canonical area | Current classification | Evidence position | Approval outcome |
|---|---|---|---|
| Evidence discipline | Local reasoning design | Cross-skill provenance recorded; no organisational policy claim required | Remain DRAFT pending clinical-governance sign-off |
| Authority, uncertainty, behaviour/change | Local reasoning design | Explicitly bounded by the provenance register and regression contracts | Remain DRAFT pending clinical-governance sign-off |
| Immediate safety override | Policy-precedence boundary | Exact emergency/safeguarding procedure absent | Remain DRAFT; cannot be promoted as policy |
| Suicide enquiry/CASE | External model candidate + local implementation | Published CASE source identified; service adoption/version not confirmed | Remain DRAFT |
| PORF | External model candidate + local implementation | Published PORF source identified; service adoption and valid comparator use not confirmed | Remain DRAFT |
| Contact pattern/function | Local clinical design | Operational contact-data definitions not confirmed | Remain DRAFT |
| Safety planning/access | External model candidate + local design + policy candidates | Safety Planning source identified; local model/adaptation and CMP policy unavailable | Remain DRAFT |
| Escalation/oversight | Local service design/policy candidates | CRG remit, destinations and decision tool unavailable | Remain DRAFT |

## Accountable approval arrangement

- **Ultimate sign-off:** Harry Miller.
- **Clinical/governance counsel:** Claire O'Prey and the requesting author.
- **Current decision status:** sign-off authority identified; no adoption or approval decision has yet been recorded.

Harry’s decision should explicitly identify the adopted version of CASE, PORF and Safety Planning, any accepted local adaptation, scope, effective date, next review date, and any conditions or exceptions. Counsel informs the decision but does not itself change a draft’s status.

## Required decisions before any promotion

1. **Model adoption:** accountable clinical owner confirms the adopted CASE, PORF and Safety Planning source/version, and records approved local adaptations.
2. **Policy control:** organisational owner supplies current controlled documents in the [organisational source-acquisition register](organisational-source-acquisition-register.md).
3. **Data control:** information-governance owner confirms which contact categories can be reliably observed and documented.
4. **Clinical review:** reviewers confirm that each draft preserves the adopted model and does not add unsupported clinical claims.
5. **Regression evidence:** run [the canonical contract suite](/tests/test_canonical_contracts.py) and the approved case-evaluation suite; record results.
6. **Approval record:** name approving role, date, scope, source version, exceptions and next review date in the provenance register.

## Prohibited shortcut

Neither repetition across skills, a passing architectural test, nor a published external paper converts a draft into an approved Lifeline organisational rule. Approval requires the applicable controlled source and accountable governance decision.
