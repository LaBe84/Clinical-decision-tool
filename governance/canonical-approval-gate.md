# Canonical approval gate

**Review status:** MODEL BASIS CONFIRMED FOR CASE, PORF AND SAFETY PLANNING ON 2026-08-21; LIVE USE PENDING. Canonical documents remain DRAFT until the operational go-live decision.

This review assesses whether the current drafts are eligible to become authoritative. It is a governance readiness review, not clinical-model adoption or organisational approval.

## Review outcome

| Canonical area | Current classification | Evidence position | Approval outcome |
|---|---|---|---|
| Evidence discipline | Local reasoning design | Cross-skill provenance recorded; no organisational policy claim required | Remain DRAFT pending clinical-governance sign-off |
| Authority, uncertainty, behaviour/change | Local reasoning design | Explicitly bounded by the provenance register and regression contracts | Remain DRAFT pending clinical-governance sign-off |
| Immediate safety override | Policy-precedence boundary | `Lifeline_ERO_v6 Merged.docx` identified; full controlled-document verification pending | Remain DRAFT pending operational source control and go-live |
| Suicide enquiry/CASE | Confirmed model basis + local implementation | Model basis confirmed 2026-08-21; operational release pending | Remain DRAFT pending live-use validation |
| PORF | Confirmed model basis + local implementation | Model basis confirmed 2026-08-21; valid local comparator use remains a release check | Remain DRAFT pending live-use validation |
| Contact pattern/function | Local clinical design | Operational contact-data definitions not confirmed | Remain DRAFT |
| Safety planning/access | Confirmed model basis + local design + policy candidates | Safety Planning model basis confirmed; `Clinical Contact Management Framework v2.docx` identified; full source control pending | Remain DRAFT pending operational source control and live-use validation |
| Escalation/oversight | Local service design/policy candidates | `CRG_Quick_Referral_Guide_Tracked_Changes.docx` identified; approved final version/full source control pending | Remain DRAFT pending operational source control and live-use validation |

## Accountable approval arrangement

- **Ultimate sign-off:** Harry Miller.
- **Clinical/governance counsel:** Claire O'Prey and the requesting author.
- **Current decision status:** Harry Miller confirmed CASE, PORF and Safety Planning model basis effective 2026-08-21. Live use remains pending.

Harry’s decision should explicitly identify the adopted version of CASE, PORF and Safety Planning, any accepted local adaptation, scope, effective date, next review date, and any conditions or exceptions. Counsel informs the decision but does not itself change a draft’s status.

## Required decisions before any promotion

1. **Model adoption:** complete — Harry Miller confirmed the model basis effective 2026-08-21. Any later local adaptation must be recorded and reviewed before live use.
2. **Policy control:** source identities and summaries are recorded. Complete the remaining secure-location, version/owner, final-version and full-text verification requirements in the [organisational source-acquisition register](organisational-source-acquisition-register.md).
3. **Data control:** information-governance owner confirms which contact categories can be reliably observed and documented.
4. **Clinical review:** reviewers confirm that each draft preserves the adopted model and does not add unsupported clinical claims.
5. **Regression evidence:** run [the canonical contract suite](/tests/test_canonical_contracts.py) and the approved case-evaluation suite; record results.
6. **Approval record:** name approving role, date, scope, source version, exceptions and next review date in the provenance register.

## Operational release boundary

This decision confirms the model basis only. It does **not** authorise live use, promote all canonical drafts to approved operational rules, or replace the outstanding organisational policy, data-definition, case-eval, and final release-validation steps.

## Prohibited shortcut

Neither repetition across skills, a passing architectural test, nor a published external paper converts a draft into an approved Lifeline organisational rule. Approval requires the applicable controlled source and accountable governance decision.
