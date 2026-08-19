# Canonical Provenance Register

Status labels used during migration:

- **ESTABLISHED MODEL** — attributable to a defined clinical model/framework; source still needs controlled citation where not yet stored.
- **ORGANISATIONAL RULE** — requires an applicable Lifeline/BHSCT policy, SOP or formally agreed service rule.
- **LOCAL DESIGN DECISION** — deliberate architecture/clinical-governance design used in this system; not automatically organisational policy.
- **SKILL-SPECIFIC LOGIC** — implementation instruction that belongs in a skill rather than canonical.
- **NEEDS VERIFICATION** — proposition is currently asserted in one or more skills but its authority/status has not yet been established.

| Proposition | Current location/evidence | Migration classification | Action before approval |
|---|---|---|---|
| Unknown is not negative evidence | Repeated across Contact Pattern Analysis, CRG Triage and other skills | LOCAL DESIGN DECISION / evidence-discipline invariant | Retain as system-wide reasoning invariant; document rationale |
| Behaviour is not function | Contact Pattern Analysis; CRG Triage | LOCAL DESIGN DECISION grounded in formulation discipline | Retain; distinguish observation, hypothesis and directly evidenced stated function |
| Stable pattern is not equivalent to effective intervention | Contact Pattern Analysis; CRG Triage | LOCAL DESIGN DECISION | Retain; ensure causal maintenance is not inferred from temporal association |
| Reduced contact is not equivalent to improvement | Contact Pattern Analysis | LOCAL DESIGN DECISION | Retain as anti-shortcut invariant |
| Increased contact is not equivalent to deterioration | Contact Pattern Analysis | LOCAL DESIGN DECISION | Retain as anti-shortcut invariant |
| Frequency alone does not establish risk or function | Contact Pattern Analysis | LOCAL DESIGN DECISION | Retain; regression-test |
| Immediate safety requirements override normal skill routing | Router/CRG/CMP family | ORGANISATIONAL RULE boundary + LOCAL DESIGN DECISION for router behaviour | Verify exact emergency/safeguarding procedures; canonical layer should state precedence, not invent procedure |
| Suicide Enquiry establishes information; PORF interprets meaning | Skill-family dependency | LOCAL DESIGN DECISION aligned to model separation | Verify against adopted CASE/PORF model descriptions |
| Safety Planning consumes established enquiry/formulation and must not manufacture missing upstream information | Safety Planning skill | LOCAL DESIGN DECISION | Retain as authority boundary; verify safety-planning model source separately |
| Contact Pattern Analysis must separate attempted, connected, substantive and completed contact where data permit | Contact Pattern Analysis | LOCAL DESIGN DECISION | Retain if these categories match operational data definitions; otherwise revise terminology |
| Contact-pattern data alone cannot establish that a service response is causally maintaining the pattern | Contact Pattern Analysis | LOCAL DESIGN DECISION / evidence discipline | Retain; regression-test against overclaiming reinforcement |
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

## Migration rule

No proposition classified as **ORGANISATIONAL RULE candidate** should be promoted to approved canonical status merely because it appears consistently across existing skills. Consistency of AI-generated implementation is not evidence of organisational authority.