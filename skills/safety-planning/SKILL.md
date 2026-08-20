---
name: safety-planning
description: >
  Builds or reviews a collaborative, person-specific safety plan for someone
  in or approaching a period of elevated suicide/self-harm risk. Use this
  skill whenever the user wants to create, review, or strengthen a safety
  plan, asks whether an existing safety plan is actually usable, or has
  PORF/Suicide Enquiry material and needs to turn it into a concrete plan for
  getting through the next crisis period. This is an intervention-design
  skill, not an assessment skill — it consumes Suicide Enquiry and PORF
  output rather than redoing that work, and does not itself formulate risk.
  Trigger even if the user doesn't say "safety plan" by name but describes
  wanting a plan for what someone will do when things get worse, or asks you
  to check whether a plan someone already has would actually hold up under
  pressure.
---

# Safety Planning

## Canonical dependencies

Apply the following **draft** canonical rules. They define shared reasoning discipline; organisational policy and mandatory procedure take precedence. Preserve this skill’s bounded application logic and route gaps rather than recreating upstream reasoning.

- [authority-and-uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md)
- [behaviour-change-and-causality](/canonical/00-system-principles/behaviour-change-and-causality.md)
- [override-principle](/canonical/01-immediate-safety/override-principle.md)
- [intervention-usability-and-access](/canonical/05-intervention/intervention-usability-and-access.md)



## Purpose

**Given what is already known about this person's current crisis pattern,
what concrete, collaborative plan will help them get through the next period
of elevated risk without relying on vague reassurance or inaccessible
strategies?**

Safety planning is an intervention, not an assessment. It consumes Suicide
Enquiry and PORF Formulation material — it does not re-run either. If the
material this skill is handed doesn't already establish what the crisis
pattern looks like, that's a gap to route back for (via Suicide Enquiry
and/or PORF), not something this skill should infer or reconstruct itself.

The dependency runs Suicide Enquiry → PORF Formulation → Safety Planning,
but this isn't a rigid waterfall this skill executes blindly. Safety
Planning can expose that something upstream is missing — but when it does,
the honest move is to name the gap and route the question back, not to
manufacture the missing answer itself so the plan looks complete. And when
the material indicates immediate danger, the immediate-risk pathway takes
precedence over completing the planning workflow — see the immediate-danger
guidance below.

## Shared rules

Apply the canonical dependencies above; do not restate or reinterpret them in this skill.
## The invariants specific to safety planning

- **Safety planning is an intervention, not an assessment.** Don't let this
  skill drift into re-establishing risk level or re-running enquiry; use what
  PORF/Suicide Enquiry have already established.
- **"Has a safety plan" ≠ "has a usable safety plan."** A document existing
  is not evidence it will work. Review existing plans on the same terms as
  building a new one.
- **Generic coping strategies ≠ person-specific strategies.** "Distract
  yourself," "reach out to someone," "practice self-care" are not safety
  plan content — they're placeholders that read like content.
- **A strategy being theoretically helpful ≠ available in the actual crisis
  state.** Journalling might genuinely help some people in general. Whether
  this person can physically or psychologically do it at 3am, intoxicated,
  alone, and ashamed is a separate question the plan has to answer.
- **Protective factors ≠ automatically usable resources.** Carried directly
  from PORF — a sibling existing is not a sibling being available and
  willing to be called at 2am.
- **Agreement/compliance ≠ feasibility.** A person agreeing "yes, I'll do
  that" in the calm of a supportive call does not establish that the step is
  realistic under crisis conditions. Don't mistake politeness or a wish to
  please the counsellor for a workable plan.
- **"Call us if it gets worse" ≠ a complete safety plan.** That's one line in
  a plan, usually near the end, not the plan itself.
- **Escalation instructions cannot be buried beneath coping steps when
  immediate danger is already present.** If the material indicates danger is
  current, not anticipated, don't produce a five-step plan that reaches "get
  emergency help" as step five. Structure and sequence matter as much as
  content.
- **Removing means/access to lethal methods is a concrete safety
  intervention, not a moral instruction or a proxy for judging intent.**
  Frame it as practical risk reduction where relevant and feasible — not as
  a test of how seriously the person means it.
- **Safety planning should reduce reliance on the service where
  appropriate, but must not become disguised access restriction.** A plan
  that quietly limits when/how someone can contact the service is a CMP
  question, not a safety-planning outcome — if that's what's actually being
  proposed, name it and route to CMP/Access Review rather than letting it
  pass as a safety plan.
- **If the person cannot or will not collaborate, record that accurately.**
  Do not fabricate a plan on their behalf and present it as agreed. A
  documented "unable to collaborate on a plan at this time, here's what was
  attempted and why" is more useful and more honest than an invented
  document with someone's name on it.
- **Planning status must be represented faithfully, as one of several
  distinct states — not collapsed into "safety plan completed."** Offered,
  declined, partially developed, collaboratively agreed, and operationally
  completed (e.g. means actually removed, not just agreed to be) are
  different states. Say which one actually applies; don't round up.
- **Unknown is not absent, here specifically.** Where the material doesn't
  establish whether prior enquiry, formulation, planning, or intervention
  exists or occurred, say "not established in the material provided" — never
  assert it didn't happen just because nothing about it was supplied. This
  is the same discipline the router was built on, applied to this skill's
  own inputs.
- **Means safety stays clinically operational, not a technical handling
  protocol.** The reasoning is: what's the access problem, what's a feasible
  reduction in access, who can safely implement it, is it actually feasible,
  and has it actually happened. That's the skill's job. Specific mechanics
  of how to store, disable, or transport a particular means (ammunition
  separation, lock types, loaded/unloaded handling, etc.) are not — that's
  operational/procedural detail for the person and service actually
  implementing the step, not content this skill should generate.
- **A coping strategy must not create a competing safety problem.**
  Person-specific and memorable isn't sufficient on its own — check that the
  action doesn't impair emergency communication (e.g. disabling access to a
  phone), create a new physical hazard, or undermine another safety
  intervention already in the plan. A friction technique that also cuts off
  the person's ability to call for help if the friction doesn't work is a
  net-negative trade, not a positive one, even if it's genuinely
  person-specific.

## Test every plan against the person's actual crisis state

A plan that reads well calm and sober is not necessarily a plan that works
under the conditions it needs to work under. For each element of the plan,
check it against what's actually known (or unknown) about how this person
presents in crisis: memory (can they recall or find the plan then?),
motivation, access (is the resource physically/practically reachable?),
shame (will they actually use a strategy that requires disclosure or being
seen?), intoxication, dissociation, interpersonal conflict (is a listed
support person part of what's driving the crisis?), time of day, isolation.
Where this isn't known, say so rather than assuming the plan will hold.

## The six operational questions

Work through these in order — each should produce plan content, not just
information gathering (that's Suicide Enquiry's job, already done).

### 1. What crisis state are we planning for?

Name the specific state this plan addresses, drawn from the existing
formulation/enquiry material — not a generic "if things get bad" but the
actual pattern established (e.g. "escalating hopelessness after evening
contact with [specific person], typically with access to [specific means]").

### 2. How will the person recognise that state early enough to act?

Specific, person-described early warning signs — thoughts, physical
sensations, behaviours — not generic ones. Early enough to act matters: a
sign that only appears once the person is already in crisis is too late to
be a "recognise early" cue.

### 3. What can they do independently that is actually feasible then?

Internal coping steps, tested against the crisis-state check above. Not what
sounds helpful in general — what this person can actually do, in that state,
with what's actually accessible to them.

### 4. Who or what can they access for interpersonal/environmental support?

Specific people, specific ways to reach them, and — critically — whether
they're actually available and willing at the relevant times, not just
named because they exist in the person's life.

### 5. What specific means/environmental safety actions are relevant and
feasible?

Work this at the level of clinical reasoning, not technical instruction:
what's the access problem, what's a feasible reduction in access, who can
safely implement it, is that actually feasible given what's known about
them, and has it actually happened (or is it still pending). Only include
what's relevant to the established pattern (e.g. don't propose "give your
medication to a family member" if no such person is established as available
and willing). Don't generate the operational mechanics of how a specific
means should be handled, stored, or disabled — that's for the person and
service actually carrying out the step, not content this skill produces.

### 6. What happens if the plan is not enough?

Explicit, specific escalation: what constitutes "this isn't working," and
what happens next — crisis line, emergency services, a specific person. This
step's position in the plan should reflect urgency, not just habitually sit
last.

## Output format

```
SAFETY PLAN

Crisis state this plan addresses
[Specific, drawn from existing formulation/enquiry material]

Early warning signs
[Person-specific, early enough to act on]

Independent coping steps
[Tested against feasibility under the actual crisis state]

Interpersonal / environmental support
[Specific people/resources, with availability and willingness noted or
flagged as unknown]

Means / environmental safety
[Concrete and feasible steps, framed as risk reduction — omit if not
relevant to the established pattern]

If this isn't enough
[Explicit escalation step(s) — positioned according to urgency, not habit]

Collaboration status
[Whether the person actively collaborated, partially engaged, or could not/
would not collaborate — recorded accurately, not smoothed over]

Feasibility check
[Brief note on what's tested/untested against the person's actual crisis
state per the discipline above, and what remains genuinely unknown]
```

Use this template for each plan item, and don't let vaguer language survive
into the final plan:

**"When [recognisable state/cue] happens, I will [specific action], using
[specific resource/person/place], because this is realistically available to
me then. If that does not reduce immediate danger, [next safety step]."**

## Reasoning shortcuts to avoid

- Producing a plan full of generic strategies ("practice self-care," "reach
  out to someone," "try deep breathing") that reads thoroughly but contains
  no person-specific, testable content.
- Treating a person's calm agreement to a strategy as evidence it will work
  under crisis conditions.
- Listing a protective factor from PORF (a relationship, a hobby, a pet) as
  a plan resource without checking it's actually accessible and usable in
  the relevant state.
- Ending with "call the crisis line if things get worse" as the sole
  escalation content, or placing genuinely urgent escalation instructions
  after several pages of coping strategies when danger is current.
- Discussing means restriction in moralising language ("you need to get rid
  of the pills to show you're serious") rather than as a practical
  intervention.
- Quietly building a service-access restriction into a "safety plan" (e.g.
  "only contact Lifeline between 9-5") without naming it as a CMP question
  and routing it there.
- Writing up a plan as agreed and collaborative when the person actually
  disengaged, refused, or could only partially engage — fabricating
  collaboration to make the document look complete.

## Boundary

This skill builds and reviews safety plans. It does not formulate suicide
risk (PORF Formulation), does not conduct suicide enquiry (Suicide Enquiry),
does not decide escalation destination (CRG Triage), and does not design or
review access restrictions (CMP/Access Review) — if a safety-planning
conversation surfaces a need for one of those, name it and route there
rather than absorbing the work into this skill. It does not override the
immediate risk pathway — a safety plan is not a substitute for responding to
current danger. Where organisational policy specifies mandatory safety
planning content or format, policy takes precedence over this skill.
