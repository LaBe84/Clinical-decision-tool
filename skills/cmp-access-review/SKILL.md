---
name: cmp-access-review
description: >
  Reviews whether a Contact Management Plan (CMP) or other access arrangement
  for a crisis-helpline caller is still clinically purposeful, proportionate,
  and working — or whether it needs to be introduced, modified, or reduced.
  Use this skill whenever the user mentions a CMP, access agreement, access
  restriction, boundary-setting, high/frequent contact that staff want to
  manage, or asks whether someone's access to the service should change.
  Also trigger when the user describes a caller whose contact pattern or
  behaviour is difficult for staff and asks what to do about it — this skill
  exists specifically to separate that difficulty from the clinical question
  of whether access itself needs to change. This is a decision skill, not a
  formulation or pattern-analysis skill: it consumes PORF Formulation and/or
  Contact Pattern Analysis output (or equivalent case material) rather than
  redoing that work.
---

# CMP / Access Review

## Canonical dependencies

Apply the following **draft** canonical rules. They define shared reasoning discipline; organisational policy and mandatory procedure take precedence. Preserve this skill’s bounded application logic and route gaps rather than recreating upstream reasoning.

- [authority-and-uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md)
- [behaviour-change-and-causality](/canonical/00-system-principles/behaviour-change-and-causality.md)
- [override-principle](/canonical/01-immediate-safety/override-principle.md)
- [intervention-usability-and-access](/canonical/05-intervention/intervention-usability-and-access.md)



## Purpose

The question this skill answers is not "does this person need a CMP?" It is:

**Is the current way of providing access still clinically purposeful,
proportionate, and workable — and if not, what specifically needs to
change?**

A CMP is an intervention aimed at a clinical purpose, not an administrative
tool for managing call volume, and not a punitive response to behaviour staff
find difficult. Every recommendation this skill produces has to be traceable
to a clinical or safety purpose, not to service convenience alone.

This doesn't mean operational reality is irrelevant — it means it can't do
the deciding on its own. Operational impact may contribute to the rationale
for change where it's evidenced and disproportionate (other callers
demonstrably unable to get through is a real problem worth addressing), but
it cannot by itself determine the *form* the restriction takes. Any access
change still has to be clinically coherent, proportionate, least restrictive,
and designed so the person can continue to get the service response they
need. Operational evidence can establish that something needs addressing;
formulation still determines what the intervention should be. "The queue is
struggling" tells you there's a problem to solve — it doesn't tell you one
contact per day is the clinically correct answer to it.

## Shared rules

Apply the canonical dependencies above; do not restate or reinterpret them in this skill.
## The invariants specific to access review

- **High contact ≠ dysfunctional contact.** Frequent use of the service can be
  exactly what the service is for.
- **Service impact ≠ evidence of client intent or manipulation.** A pattern
  being demanding on the service says nothing on its own about why the person
  is contacting, or whether they mean to be demanding.
- **Behaviour ≠ function.** Carried forward directly from Contact Pattern
  Analysis — don't re-infer function from volume or form here either.
- **A CMP is an intervention, not an administrative control.** If a proposed
  change can't complete the "because / we expect / we will review by"
  sentence below with a clinical or safety rationale, it isn't ready to
  propose.
- **Existing CMP ≠ effective CMP.** A plan being in place tells you nothing
  about whether it's achieving anything. Review it on the same terms as a
  fresh decision, not as a default to preserve.
- **Boundary breach ≠ automatic restriction.** A single breach is information,
  not a trigger. But the reverse claim needs equal caution: **compliance
  with a boundary is not evidence the boundary is clinically effective.**
  Months of adherence tell you the person can follow the arrangement — that's
  a behavioural fact. It does not, on its own, establish that the
  arrangement is clinically purposeful, proportionate, or beneficial, any
  more than a stable Contact Pattern Analysis pattern proves an intervention
  is working. Purpose, effectiveness, and proportionality each need their own
  evidence — don't let evidence for one (e.g. compliance, which speaks to
  workability) stand in for the others (whether it's achieving anything,
  whether it's proportionate to a defined problem).

  Equally, don't overcorrect a single exception into a normative judgement
  either way. When one contact falls outside an agreement's terms, the skill
  only needs to establish that one contextually distinct exception doesn't
  evidence failure, misuse, erosion of the agreement, or a need for tighter
  restriction — it doesn't need to decide, and shouldn't claim, that the
  exception was "appropriate" or "warranted." That's a normative call this
  review doesn't need to make and isn't positioned to make well; just report
  what happened and state plainly that it doesn't change the analysis.
- **Restriction must have a defined clinical/operational purpose and be
  proportionate to that purpose** — not proportionate to how uncomfortable
  the current arrangement feels.
- **Do not increase restriction merely because the current arrangement is
  difficult for staff.** Staff difficulty is real and worth naming and
  supporting through supervision — but hold two things apart, don't collapse
  them into one rule. Staff *emotional burden* (finding a caller exhausting,
  demanding, hard to sit with) is, by itself, never a restriction criterion —
  it's a supervision matter, full stop. *Evidenced, disproportionate
  service-delivery impact* (other callers demonstrably unable to get through,
  a specific operational failure that's actually been observed, not just
  felt) is different — it's a legitimate input into the proportionality
  question in step 3, alongside impact on the person themselves. The
  distinction is evidence: a feeling of exhaustion doesn't clear that bar; a
  demonstrated effect on service delivery might. Don't rule out real,
  evidenced service impact just to keep the "staff comfort isn't a criterion"
  principle clean — and don't smuggle staff discomfort in by relabelling it
  as service impact without actual evidence of the impact.
- **Do not preserve ineffective unrestricted access merely because
  restriction feels uncomfortable.** The discomfort of proposing a boundary
  is not evidence the boundary is wrong, any more than staff difficulty is
  evidence a boundary is needed. Both directions require an actual clinical
  rationale, not a feeling about the decision.
- **Risk escalation and access restriction are separate decisions.** A CMP
  answers "how should access be structured." It does not, and cannot,
  substitute for what CRG Triage or PORF Formulation determine about risk.
- **Immediate risk always remains respondable; a CMP cannot extinguish the
  safety pathway.** No access arrangement should be written or read in a way
  that would block or delay a response to an immediate safety concern. And
  once the immediate response is handled, don't automatically generate a
  follow-on CRG referral just because something notable happened outside the
  plan's terms. A crisis occurring outside permitted hours is not, by itself,
  evidence the plan's purpose, proportionality, or workability needs
  reformulating — that's the same "something interesting happened, therefore
  invent an escalation destination" error this skill family had to remove
  from Contact Pattern Analysis. Review the event against the CMP only if
  there's actual evidence it raises a genuine question about the plan; if
  not, log it and continue.
- **Unknown function ≠ evidence for restriction.** Not knowing why someone
  contacts the way they do is a gap to name, not a justification to tighten
  access "to be safe."
- **A stable pattern can still represent an ineffective intervention.**
  Calm and unchanging is not the same finding as working.
- **Prefer the least restrictive workable response — but "least restrictive"
  does not mean "no boundaries."** Declining to set any boundary because
  restriction feels uncomfortable is not the least-restrictive option if the
  current unstructured arrangement isn't actually working either; it's just
  the option that avoids the harder conversation.

## The five questions, in order

Work through these in sequence — each depends on the one before it.

### 1. What is happening?

Report the observed contact/access pattern only: frequency, timing,
duration, engagement, how contacts end, any existing CMP terms and how
contact has actually run against them. This is description, not
interpretation — don't let a judgement about whether the pattern is a problem
leak into how it's described.

### 2. What function is the current access arrangement serving?

Draw on the existing formulation and/or contact-pattern analysis where
available — don't redo that analysis here, reference its conclusions. Where
function has already been established there (directly evidenced, per
Contact Pattern Analysis's own distinction), use it. Where it hasn't, say so
explicitly and preserve that uncertainty rather than assuming a function to
make this review feel more complete.

This step is where behaviour-as-function creeps back in most easily, because
behaviour that *looks* appropriate is just as easy to over-read as behaviour
that looks alarming. "Frequent, on-topic, risk-relevant contact" describes
the content and form of the calls — it does not, by itself, establish that
the function is "appropriate use of the service." That's still an inference
from behaviour, just a flattering one. State function as unknown unless it's
been directly evidenced (the person has said what it's for) or genuinely
formulated elsewhere — a pattern looking clinically unremarkable is not the
same evidentiary category as function being established.

### 3. Is the current intervention working?

This is not "has the behaviour reduced?" A drop in contact volume is not
itself success, and a stable, calm pattern is not itself success either —
both are consistent with either a working intervention or one that's simply
not doing anything (or, worse, doing harm quietly). The actual question: is
access, as currently structured, achieving its intended purpose without
disproportionate adverse impact on the person, other callers, or service
delivery? An arrangement that protects the service at the person's expense,
or protects the person's comfort at the expense of the service being usable
by others, both fail this test.

Consider staff impact *separately*, and be precise about which kind you're
looking at: evidenced operational effects (e.g. this caller's contact pattern
demonstrably displacing other callers) may inform the proportionality
question above. Staff emotional burden or difficulty holding the work is
real and matters, but it belongs in supervision — it is not, by itself, an
access criterion, and folding it into "harm to staff" alongside service
delivery would quietly reopen the exhaustion-to-restriction shortcut this
skill exists to close.

### 4. What decision is actually required?

Name exactly one of these, and justify it against what steps 1–3 established
— not against how the case feels:

- **Continue current access** — no CMP, current arrangement is working.
- **Clarify/standardise existing approach** — no formal CMP needed, but the
  current informal approach needs to be made consistent (e.g. across staff)
  rather than structurally changed.
- **Modify existing CMP** — the plan exists but isn't achieving its purpose
  as written, or circumstances have changed.
- **Introduce a CMP** — no current plan, but the review has identified a
  specific, defined problem a plan should address. Ground the "defined
  problem" in the broadest available evidence of failure to reach a usable
  outcome (repeatedly, across contacts and staff) — not a single rigid
  proxy like "every call must reach a coping plan," which can quietly become
  a hidden universal standard this skill never asked for. And where function
  is unknown, say explicitly that the CMP being introduced is a limited,
  testable structural intervention, not a full formulation of what the
  person needs — if it doesn't work, that's evidence for formulation review,
  not a reason to tighten further.
- **Review/reduce restriction** — the current arrangement is more
  restrictive than the evidence supports; least-restrictive-workable points
  toward loosening it. Where a restriction appears to be impairing usability
  (the person disengaging, minimising, or reporting the service unusable)
  but the original contact function was never established, the defensible
  move is to reduce or loosen the restriction and establish function — not
  to design a detailed replacement structure on top of an unknown function.
  Don't let the fact that the original volume concern was operationally real
  carry forward as justification for keeping some restriction in place;
  operational reality doesn't retroactively establish that restriction had a
  valid clinical rationale.
- **Escalate for shared formulation** — function and/or intervention
  effectiveness cannot presently be resolved at this level; this is a CRG
  question (or a call to run CRG Triage), not a decision this review can
  make alone.

### 5. What is the least restrictive proportionate change that addresses
that problem?

Only relevant if step 4 named a change. State the specific change, not a
general tightening or loosening — and complete this sentence explicitly, in
the output, for every proposed change:

**"We are changing access from [X] to [Y] because [specific reason tied to
steps 1–3], and we expect this to achieve [specific, checkable outcome]; we
will review whether it has done so by [a stated point/date]."**

If any part of that sentence can't be filled in with something concrete, the
proposed change isn't ready — that's the discipline that turns a boundary
into a testable intervention rather than a standing reaction to difficult
behaviour.

## Output format

```
CMP / ACCESS REVIEW

What is happening
[Observed pattern and any existing CMP, description only]

Function of current access arrangement
[From existing formulation/pattern analysis, or "not established" if genuinely
unknown — don't infer to fill the gap]

Is the current intervention working
[Assessed against intended clinical purpose and adverse impact on the person,
other callers and service delivery. Consider staff emotional burden separately
as a supervision issue; only evidenced operational effects enter the
proportionality assessment. Not assessed against volume or calmness alone.]

Decision required
[One of the six options, named explicitly]

Proposed change (if any)
[For Modify / Introduce / Review-reduce: the full "changing access from X to
Y because... we expect... we will review by..." statement, filled in
concretely — clarification is still a change in practice, even when access
itself isn't being tightened or loosened, and skipping this discipline for it
would let "Clarify" become a way to avoid the testable-intervention standard
the other decisions are held to.
For Clarify/standardise: state exactly what is being standardised, why
consistency across staff/contacts is required, and how and when
implementation will be checked.
For Continue current access: "No change proposed."]

Safety pathway note
[Explicit confirmation that nothing in this review restricts or delays
response to immediate safety concerns]
```

## The pair every version of this skill should be tested against

Two cases probe whether this skill actually understands what a CMP is for,
rather than having learned to manage call volume in clinical-sounding
language:

- A caller with very high contact volume, under an existing CMP, whose
  contacts are now markedly shorter, safer, and more purposeful than before
  the plan. High volume alone does not justify further restriction here —
  the intervention is working.
- A caller whose contact volume has dropped sharply after a restrictive CMP,
  but who now disengages before discussing risk, delays contact until crisis
  is severe, or reports the service no longer feels usable. Reduced
  utilisation here is not treatment success — it may be the CMP achieving
  the opposite of its clinical purpose.

If this skill can't tell these two apart, it hasn't learned the actual
question — it's learned to read volume as the whole answer, in either
direction.

## Reasoning shortcuts to avoid

- "Contact volume is high therefore restriction is needed."
- "Contact volume has dropped therefore the CMP is working" — check what
  happened to the *quality* and *purpose* of remaining contact, and to
  whether risk-relevant content is still being reached, before calling this
  success.
- "There's an existing CMP therefore no review is needed" — an existing plan
  gets reviewed on the same terms as a fresh decision.
- "Staff find this difficult therefore restrict" or the mirror image,
  "restriction feels uncomfortable therefore don't."  Neither staff comfort
  nor clinician discomfort is the rationale; the clinical purpose is.
  Staff difficulty is a supervision matter to raise alongside this review,
  not folded into the access decision itself.
- "One boundary breach therefore restrict further" — a breach is
  information to fold into the "is this working" question, not an automatic
  trigger.
- Proposing a change without being able to complete the "because / we
  expect / we will review by" sentence concretely — a boundary without a
  statable purpose and review point is not a considered intervention.
- Writing or implying an access arrangement that would delay or block
  response to an immediate safety concern — that is never an acceptable
  side effect of a CMP, regardless of how well-justified the plan otherwise
  is.
- Generating a CRG referral automatically after an acute event that occurred
  outside CMP terms, once the immediate response is handled — an out-of-hours
  crisis is not itself evidence the plan needs reformulating.
- "Months of compliance therefore the arrangement is working" — compliance
  is evidence of workability, not of clinical effectiveness or purpose. Don't
  let it answer a question it doesn't speak to.
- Treating "appropriate-sounding" contact (on-topic, risk-relevant, calm) as
  itself evidence that function is "legitimate use of the service" — that's
  still inferring function from behaviour, just optimistically.
- Designing a detailed, structured replacement CMP on top of a function that
  was never established — reduce the harmful restriction and go find the
  function first.
- Ruling out evidenced, disproportionate service-delivery impact entirely
  just because staff emotional burden isn't a valid criterion on its own —
  they're different things and need different evidence.

## Boundary

This skill reviews and recommends changes to access arrangements. It does
not conduct the underlying formulation (PORF Formulation), the pattern
analysis (Contact Pattern Analysis), or the triage decision about where a
case should go (CRG Triage) — it draws on their conclusions. It does not
override the immediate risk pathway. Where organisational policy specifies
mandatory CMP process or approval requirements, policy takes precedence over
this skill.
