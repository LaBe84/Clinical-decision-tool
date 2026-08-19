# Lifeline Clinical Reasoning System — Architecture

## Purpose

This repository is evolving from a collection of individually engineered clinical reasoning skills into a version-controlled clinical reasoning system.

The architecture separates:

1. **Canonical knowledge** — authoritative propositions and decision principles.
2. **Policies** — organisational requirements that take precedence where applicable.
3. **Skills** — bounded reasoning capabilities that apply canonical knowledge.
4. **Router/orchestration** — selects the minimum necessary skill or sequence of skills.
5. **Evals** — test the quality and discrimination of clinical reasoning.
6. **Tests** — protect hard invariants against regression.
7. **Development history** — preserves experimental iterations and learning without treating them as current production logic.
8. **Governance** — records authority, provenance, approval, version and rationale for consequential rules.

## Authority order

Where sources conflict, the intended order is:

1. Applicable organisational policy / mandatory procedure
2. Approved canonical rule or model
3. Skill-specific application logic
4. Router/orchestration logic
5. Example/eval material
6. Historical development artefacts

Historical examples and eval outputs must never silently become canonical rules.

## Core system invariants

The initial canonical layer will formalise cross-skill principles already present in the repository, including:

- Unknown is not negative evidence.
- Behaviour is not function.
- Oversight escalation is not risk escalation.
- Stable pattern is not equivalent to effective intervention.
- Reduced contact is not equivalent to improvement.
- Increased contact is not equivalent to deterioration.
- Immediate safety requirements override normal workflow routing.
- A downstream skill must not manufacture missing upstream information.
- Organisational policy takes precedence where it specifies mandatory action, process or thresholds.

## Reasoning dependencies

Dependencies are conditional rather than a rigid waterfall.

- Suicide Enquiry establishes and organises suicide-related information.
- PORF interprets clinically relevant information and formulates what the presentation means now.
- Safety Planning consumes established enquiry/formulation material to design an intervention; it does not recreate assessment or formulation.
- Contact Pattern Analysis describes change and examines plausible function without treating contact volume as clinical meaning.
- CMP/Access Review evaluates whether an access arrangement is clinically justified, proportionate and functioning as intended.
- CRG Triage addresses unresolved decisions about the appropriate level or locus of shared clinical decision-making; complexity or contact volume alone do not determine escalation.
- The Clinical Workflow Router selects only the reasoning capability required by the material and current decision question.

## CARE

CARE should be treated as the operational/documentation framework through which clinical reasoning is expressed, not as a competing clinical reasoning skill.

CONNECT → ASSESS → RESPOND → EXTEND can consume outputs from the relevant clinical skills. Completion of CARE documentation must not be treated as evidence that the underlying reasoning was adequate.

## Target structure

```text
canonical/
  00-system-principles/
  01-immediate-safety/
  02-suicide-enquiry/
  03-formulation/
  04-contact-pattern/
  05-intervention/
  06-escalation/

policies/
skills/
evals/
tests/
governance/
docs/
development-history/
```

Existing promoted skills remain untouched during the first migration phase. Experimental build folders and workspaces will be preserved until their current/superseded status has been verified.

## Change discipline

Consequential clinical rules should not be changed merely by editing a skill prompt. A substantive change should identify:

- the rule being changed;
- its authority/source;
- rationale;
- affected skills;
- affected evals/tests;
- expected behaviour change;
- regression results;
- approval/status where organisational governance is required.

## Current migration rule

The `architecture/canonical-v1` branch is a migration workspace. Existing production-candidate skills on `main` are not to be deleted, renamed or clinically amended until the canonical layer and migration map have been validated.