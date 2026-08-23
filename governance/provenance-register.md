# Canonical Provenance Register

Status labels used during migration:

- **ESTABLISHED MODEL** — attributable to a defined clinical model/framework; source still needs controlled citation where not yet stored.
- **ORGANISATIONAL RULE** — requires an applicable Lifeline/BHSCT policy, SOP or formally agreed service rule.
- **LOCAL DESIGN DECISION** — deliberate architecture/clinical-governance design used in this system; not automatically organisational policy.
- **SKILL-SPECIFIC LOGIC** — implementation instruction that belongs in a skill rather than canonical.
- **NEEDS VERIFICATION** — proposition is currently asserted in one or more skills but its authority/status has not yet been established.

| Proposition | Current location/evidence | Migration classification | Action before approval |
|---|---|---|---|
| Unknown is not negative evidence | Repeated across Contact Pattern Analysis, CRG Triage, PORF, Suicide Enquiry, CMP, Safety Planning | LOCAL DESIGN DECISION / evidence-discipline invariant | Retain as system-wide reasoning invariant; document rationale |
| Behaviour is not function | Contact Pattern Analysis; CRG Triage; PORF; Suicide Enquiry; CMP; Safety Planning | LOCAL DESIGN DECISION grounded in formulation discipline | Retain; distinguish observation, hypothesis and directly evidenced stated function |
| Stable pattern is not equivalent to effective intervention | Contact Pattern Analysis; CRG Triage; CMP | LOCAL DESIGN DECISION | Retain; ensure causal maintenance is not inferred from temporal association |
| Reduced contact is not equivalent to improvement | Contact Pattern Analysis; CMP | LOCAL DESIGN DECISION | Retain as anti-shortcut invariant |
| Increased contact is not equivalent to deterioration | Contact Pattern Analysis | LOCAL DESIGN DECISION | Retain as anti-shortcut invariant |
| Frequency alone does not establish risk or function | Contact Pattern Analysis | LOCAL DESIGN DECISION | Retain; regression-test |
| Immediate safety requirements override normal skill routing | Router/CRG/CMP/Suicide Enquiry/Safety Planning family | ORGANISATIONAL RULE boundary + LOCAL DESIGN DECISION for router behaviour | Verify exact emergency/safeguarding procedures; canonical layer should state precedence, not invent procedure |
| Suicide Enquiry establishes information; PORF interprets meaning | Suicide Enquiry and PORF skills | LOCAL DESIGN DECISION aligned to model separation | Verify against adopted CASE/PORF model descriptions |
| CASE chronology is Current/immediate → Recent → Lifetime → Current/next | Suicide Enquiry | ESTABLISHED MODEL candidate | Add controlled CASE source/version; verify terminology/time horizons |
| Unasked suicide-enquiry domains should be recorded as 'not established', not as negative findings | Suicide Enquiry | LOCAL DESIGN DECISION / documentation discipline | Retain; regression-test wording that converts omission into reassurance |
| Direct denial, non-disclosure, and not-established are distinct evidential states | Suicide Enquiry | LOCAL DESIGN DECISION | Retain if operational documentation can support the distinction consistently |
| Suicide Enquiry does not score or determine risk level | Suicide Enquiry | LOCAL DESIGN DECISION aligned with formulation-led model | Retain; test against checklist/score drift |
| Ambiguous death-related language should not be labelled passive/active until clarified | Suicide Enquiry | LOCAL DESIGN DECISION / evidence discipline | Retain; regression-test against premature categorisation |
| PORF is comparative interpretation rather than risk-factor counting | PORF | ESTABLISHED MODEL candidate | Add controlled PORF source/version and compare current implementation with source |
| Risk Status is a between-person comparison against a specified reference population | PORF | ESTABLISHED MODEL candidate | Verify exact PORF model wording and whether Lifeline has a valid comparator available in practice |
| Risk State is a within-person comparison against the person's baseline | PORF | ESTABLISHED MODEL candidate | Verify exact PORF model wording; retain if source-concordant |
| Resources must be available, accessible, acceptable and likely to be used to function as usable protections | PORF | ESTABLISHED MODEL / LOCAL IMPLEMENTATION candidate | Verify source language; preserve distinction between existing and usable resources |
| Foreseeable Change should be plausible and credibly connected to risk rather than speculative | PORF | ESTABLISHED MODEL candidate | Verify source language and local operationalisation |
| Absence of historical attempts does not itself predict low future risk | PORF | LOCAL DESIGN DECISION / evidence discipline | Retain as anti-shortcut rule |
| Loss of contact/visibility is loss of information, not proof of deterioration | PORF | LOCAL DESIGN DECISION | Retain; regression-test against escalation by inference |
| Safety Planning consumes established enquiry/formulation and must not manufacture missing upstream information | Safety Planning | LOCAL DESIGN DECISION | Retain as authority boundary; verify safety-planning model source separately |
| A safety plan existing is not evidence that it is usable | Safety Planning | ESTABLISHED MODEL / LOCAL DESIGN candidate | Verify against adopted safety-planning model; retain usability test |
| Safety planning should be person-specific and feasible in the actual crisis state | Safety Planning | ESTABLISHED MODEL candidate | Verify against adopted safety-planning source/version |
| Protective factors are not automatically usable plan resources | Safety Planning / PORF | LOCAL DESIGN DECISION aligned to formulation | Retain |
| Agreement with a safety-plan step is not the same as feasibility under crisis conditions | Safety Planning | LOCAL DESIGN DECISION | Retain; regression-test |
| Immediate danger takes precedence over completing a safety plan | Safety Planning | ORGANISATIONAL RULE boundary + LOCAL DESIGN DECISION | Verify exact emergency procedure; retain precedence rule |
| Safety planning must not be used to disguise an access restriction | Safety Planning / CMP boundary | LOCAL DESIGN DECISION | Retain; regression-test cross-skill boundary |
| Planning status should distinguish offered/declined/partial/agreed/operationally completed states | Safety Planning | LOCAL DESIGN DECISION | Check against documentation requirements before canonising exact labels |
| Means-safety reasoning should remain clinical and feasible rather than generating technical handling instructions | Safety Planning | LOCAL DESIGN DECISION / safety boundary | Retain |
| Contact Pattern Analysis must separate attempted, connected, substantive and completed contact where data permit | Contact Pattern Analysis | LOCAL DESIGN DECISION | Retain if these categories match operational data definitions; otherwise revise terminology |
| Contact-pattern data alone cannot establish that a service response is causally maintaining the pattern | Contact Pattern Analysis | LOCAL DESIGN DECISION / evidence discipline | Retain; regression-test against overclaiming reinforcement |
| A CMP is a clinical intervention rather than an administrative control for volume | CMP/Access Review | ORGANISATIONAL RULE candidate / LOCAL DESIGN DECISION | Verify against current contact-management guidance and governance approval |
| High contact does not itself establish dysfunctional contact or a need for restriction | CMP/Access Review | LOCAL DESIGN DECISION | Retain; regression-test |
| Service impact does not establish client intent/manipulation | CMP/Access Review | LOCAL DESIGN DECISION | Retain |
| An existing CMP is not evidence that the CMP is effective | CMP/Access Review | LOCAL DESIGN DECISION | Retain |
| A single boundary breach does not automatically justify tighter restriction | CMP/Access Review | LOCAL DESIGN DECISION | Retain; test against mechanical escalation |
| Compliance with a boundary is not evidence that the boundary is clinically effective | CMP/Access Review | LOCAL DESIGN DECISION | Retain |
| Staff emotional burden alone is not an access-restriction criterion | CMP/Access Review | ORGANISATIONAL RULE candidate / LOCAL DESIGN DECISION | Verify with service governance; distinguish from evidenced operational impact |
| Evidenced disproportionate service-delivery impact can inform proportionality but does not determine the form of restriction by itself | CMP/Access Review | LOCAL DESIGN DECISION / service-design rule | Verify against service guidance |
| Access changes should be clinically purposeful, proportionate and least restrictive while remaining workable | CMP/Access Review | ESTABLISHED PRINCIPLE / ORGANISATIONAL RULE candidate | Verify legal/policy/service source before formal canonical approval |
| A CMP cannot block or delay an applicable immediate-safety response | CMP/Access Review | ORGANISATIONAL RULE boundary | Verify exact emergency procedure; retain as hard regression invariant |
| Unknown function is not evidence for restriction | CMP/Access Review | LOCAL DESIGN DECISION | Retain |
| Risk escalation and access restriction are separate decisions | CMP/Access Review / CRG / PORF | LOCAL DESIGN DECISION | Retain as architecture boundary |
| Complexity alone does not justify CRG | CRG Triage | LOCAL DESIGN DECISION / service-design rule | Verify against formally agreed CRG remit before organisational approval |
| Contact volume alone does not justify CRG | CRG Triage | LOCAL DESIGN DECISION / service-design rule | Verify against CRG remit |
| Staff anxiety alone does not justify CRG | CRG Triage | LOCAL DESIGN DECISION | Retain as anti-shortcut rule; verify wording with CRG governance |
| CRG is for a shared formulation/material change of approach when current formulation/intervention no longer accounts for presentation | CRG Triage | ORGANISATIONAL RULE candidate | Verify against current CRG guide/remit |
| TL/Safety Huddle is for immediate operational, coordination or oversight decisions | CRG Triage / Contact Pattern Analysis | ORGANISATIONAL RULE candidate | Verify against current service decision tool |
| Helpline is appropriate where formulation explains presentation, intervention remains proportionate and no higher-level decision is pending | CRG Triage | ORGANISATIONAL RULE candidate | Verify against current service decision tool |
| 'Insufficient information to triage' is an output, not a destination | CRG Triage | LOCAL DESIGN DECISION | Retain; protects against fabricated reassurance/escalation |
| Organisational policy takes precedence over skills | Multiple skills | ARCHITECTURE / GOVERNANCE RULE | Retain; policy sources must be controlled and current |

## Immediate provenance risks identified

1. Several destination rules (Helpline / TL-Safety Huddle / CRG) are written with the force of organisational rules but the repository does not yet contain their approved source.
2. The Contact Pattern skill contains operationally specific contact categories. These are useful, but should not become canonical until checked against actual Lifeline data definitions.
3. Skills repeatedly defer to organisational emergency/safeguarding procedures that are not yet present in the repository. This is an appropriate boundary, but means the system is not yet self-contained.
4. Clinical model names (CASE, PORF, safety planning) need controlled source/version records so that a skill cannot drift while still claiming fidelity to the model.
5. PORF currently makes specific claims about Risk Status comparators. These need source verification because a theoretically correct between-person construct can become pseudo-precision if Lifeline has no valid reference population available at the point of use.
6. CMP/Access Review contains several ethically and operationally strong rules that may reflect intended service practice but are not yet tied to an approved contact-management policy or governance record.
7. Safety Planning contains detailed usability and collaboration-state logic. Much of it is clinically sensible, but the exact required content/status labels should be checked against the safety-planning model and local documentation requirements before being called canonical.
8. Suicide Enquiry uses exact evidential labels ('denied', 'not disclosed', 'not established'). These should be retained as a reasoning discipline unless local record standards require different wording; the labels themselves are not yet organisationally approved documentation terms.

## Migration rule

No proposition classified as **ORGANISATIONAL RULE candidate** should be promoted to approved canonical status merely because it appears consistently across existing skills. Consistency of AI-generated implementation is not evidence of organisational authority.