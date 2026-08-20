---
name: crg-triage
description: >
  Decides where a crisis-helpline case needs to go — continued Helpline
  management, TL/Safety Huddle, CRG (Clinical Review Group), or an immediate
  risk/safeguarding pathway. Use this skill whenever the user has a
  formulation, a contact-pattern analysis, or a general case summary (from
  Lifeline or a similar service) and is asking whether it needs escalating,
  who should look at it, whether it warrants CRG, or "what do we do with
  this." Also trigger when the user describes a case as complex, unusual,
  high-contact, uncertain, or uncomfortable and is unsure what that implies
  for escalation — this skill exists specifically to stop those feelings from
  being treated as the answer. This is a routing skill: it consumes the
  output of PORF Formulation and/or Contact Pattern Analysis (or a case
  summary covering similar ground) and decides the destination — it does not
  redo the clinical formulation or the pattern analysis itself.
---

# CRG Triage

## Canonical dependencies

Apply the following **draft** canonical rules. They define shared reasoning discipline; organisational policy and mandatory procedure take precedence. Preserve this skill’s bounded application logic and route gaps rather than recreating upstream reasoning.

- [authority-and-uncertainty](../canonical/00-system-principles/authority-and-uncertainty.md)
- [behaviour-change-and-causality](../canonical/00-system-principles/behaviour-change-and-causality.md)
- [override-principle](../canonical/01-immediate-safety/override-principle.md)
- [decision-and-oversight](../canonical/06-escalation/decision-and-oversight.md)



## Purpose

Decide where a case needs to go, using the reasoning already produced by a
formulation (PORF) and/or a contact-pattern analysis as its input. This skill
does not re-formulate risk and does not re-analyse contact behaviour — it
takes those conclusions and answers a narrower, different question:

**What decision cannot appropriately be made within the current level of
care?**

If that question cannot be answered precisely, escalation has not been
justified — regardless of how complex, unusual, or uncomfortable the case
feels. Complexity is a property of the case. Escalation is a property of the
decision. This skill exists to keep those two things from being treated as
the same.

## Shared rules

Apply the canonical dependencies above; do not restate or reinterpret them in this skill.
## What this skill is not

This is a triage/routing skill, not a formulation skill. It should not:

- Reproduce a full PORF (Risk Status, Risk State, Resources, Foreseeable
  Change) — reference the formulation's conclusions, don't redo the work.
- Reproduce a full Contact Pattern Analysis — same principle.
- Invent new clinical content the source formulation/analysis didn't
  establish, in order to make the routing decision feel more justified.

If the case comes in without a prior formulation or pattern analysis, say so,
and note that triage without one is inherently limited — do not backfill the
missing formulation yourself under this skill's heading.

## Five possible outputs, not four

There are four genuine destinations, and one output that is not a destination
at all: **Insufficient information to triage.** This applies when there is no
formulation, no pattern analysis, and no other material sufficient to name a
pending decision. It is not a fifth escalation route and it is not the same
as Helpline.

This distinction matters because of the same discipline this whole skill
family is built on: unknown is not negative evidence. When the material
needed to triage is missing, the honest output is that triage cannot yet be
completed — not a quiet default to the calmest-sounding destination. Defaulting
to Helpline when information is genuinely absent manufactures reassurance the
same way defaulting to CRG manufactures alarm; both fabricate a decision that
isn't supported. Say plainly that triage requires the source formulation or
pattern analysis (or, failing that, an actual pending decision stated in
concrete terms), and stop there — don't pick a destination to have an answer.

Keep separate two things that sound similar but aren't: "the formulation
isn't available to this triage" (an information problem — get it) and "no
formulation exists / hasn't been done" (a governance/practice gap worth
naming as such, not smoothed over as if it were the same thing).

## The four destinations

- **Helpline** — the existing formulation sufficiently explains the
  presentation, and the current intervention remains proportionate. No
  decision is pending that Helpline-level management can't make itself.
- **TL/Safety Huddle** — an immediate operational, coordination, or oversight
  decision needs to be made now (e.g. genuinely fragmented visibility across
  contacts, inconsistent responses across staff, a real-time decision about
  how to handle the next contact). This is about *this shift's* decision, not
  a standing question about the person's care.
- **CRG** — the existing formulation or intervention no longer adequately
  accounts for what is happening, and a shared formulation or a material
  change of approach is required. This is a considered, non-urgent review of
  the plan itself, not an emergency mechanism.

  Do not encode this as a failure quota — "two failed attempts to explore it"
  or "three contacts with no new understanding" is not the rule, and treating
  it as one teaches a mechanical threshold that isn't the actual principle.
  The rule is that the current formulation no longer adequately explains a
  sustained, material change. Prior attempts to explore or resolve it are
  *supporting evidence* that the uncertainty is persistent rather than
  momentary — they strengthen the case, they are not themselves the
  threshold. A single contact could in principle be enough to show a
  formulation no longer fits, if the change is clear and sustained enough;
  conversely, several inconclusive contacts don't automatically add up to CRG
  if nothing suggests the formulation itself has stopped fitting.
- **Immediate risk pathway** — action is required now because of acute
  safety or safeguarding need. This sits entirely outside CRG. If the case
  needs something to happen in the next few minutes, CRG is the wrong
  destination regardless of how well it might otherwise fit CRG's remit —
  say so explicitly and route to the immediate pathway instead.

These are mutually exclusive for the purpose of this triage decision — pick
one primary destination and justify it. A case can legitimately need more
than one thing over time (e.g. immediate pathway now, CRG once the acute
period passes), but say that explicitly as a sequence rather than blurring
the two into one recommendation.

## What does NOT justify escalation, by itself

None of the following, alone, routes a case anywhere other than Helpline:

- Complexity ≠ CRG.
- Uncertainty ≠ CRG.
- High contact/frequency ≠ CRG.
- Elevated or unresolved risk ≠ CRG (risk that needs acting on now is the
  immediate pathway; risk that's adequately formulated and managed is
  Helpline, however serious it looks on paper).
- Staff anxiety about the case ≠ CRG.
- "Someone senior should probably look at this" ≠ CRG — that instinct is
  worth naming, but it has to cash out as an actual unanswered decision, or
  it isn't a justification.

Naming one of these in a case does not disqualify escalation — plenty of
genuinely CRG-worthy cases are also complex, high-contact, and anxiety-
provoking. The point is that none of them does the justificatory work on its
own. The justification has to be the specific unanswered decision, stated
plainly, not the presence of these surrounding features.

## The forcing question

Before naming a destination, answer this explicitly, in one or two sentences:

**What decision cannot appropriately be made within the current level of
care?**

Then check the answer against the destinations above — the decision named
should point unambiguously at one of them. If the honest answer is "no
specific decision is actually pending, the case is just difficult to sit
with," that is itself the answer: **Helpline**, with the difficulty
acknowledged but not treated as a routing criterion.

If the case is genuinely urgent, the forcing question still applies, but the
decision it surfaces will itself be time-critical ("does someone need to act
in the next few minutes to keep this person safe") — which is precisely what
distinguishes the immediate risk pathway from CRG.

## Output format

Keep this short — shorter than a PORF, comparable to a Contact Pattern
Analysis output. This skill is answering one question, not producing a
formulation.

```
CRG TRIAGE

Source material
[What formulation/pattern analysis this triage is drawing on — or "no prior
formulation available" if that's the case]

What decision is actually pending
[The forcing question, answered directly, in a sentence or two]

Why the surrounding features don't settle it
[Name any of complexity/uncertainty/frequency/risk/anxiety present in the
case, and state explicitly that none of them is doing the justificatory
work by itself]

Destination
[Helpline / TL-Safety Huddle / CRG / Immediate risk pathway / Insufficient
information to triage — exactly one, or an explicit sequence if more than one
destination genuinely applies over time. If choosing "Insufficient
information," say exactly what's missing and stop there — do not also name a
provisional destination alongside it.]

Therefore
[One sentence connecting the pending decision to the destination — the
destination must follow from the decision named above, not from case
features. If the destination is "Insufficient information," this states what
needs to be obtained before triage can run, not a fallback recommendation.]
```

## Reasoning shortcuts to avoid

- Routing to CRG because the case is hard to think about, rather than because
  a specific decision the current level of care can't make has been named.
- Treating "someone should keep an eye on this" as equivalent to "this needs
  TL/Safety Huddle" — ongoing awareness is not the same as an operational
  decision pending right now.
- Sending an acute safety situation to CRG because CRG feels like the
  "serious" option — CRG is not an emergency mechanism, and using it as one
  delays the response the situation actually needs.
- Working backward from a destination that feels proportionate to how serious
  the case seems, then constructing a decision to justify it, rather than
  identifying the decision first and letting the destination follow.
- Treating the presence of a prior formulation's uncertainty (e.g. "Risk
  Status could not be established against a comparator") as itself a
  triage-level decision — an unresolved formulation detail only becomes a
  triage matter if it blocks a decision that actually needs making now.
- Defaulting to Helpline when the source material needed to triage is simply
  missing, rather than naming "Insufficient information to triage" as the
  actual output. Absence of evidence for CRG is not evidence that Helpline is
  correct — it's evidence you don't yet have enough to decide either way.
  Writing "cannot be determined" and then naming a "default" destination in
  the same breath is a contradiction, not a hedge — pick one.
- Encoding CRG eligibility as a minimum number of failed contacts or
  exploration attempts. Persistence of unexplained change is the evidence;
  it is not counted against a threshold.

## Boundary

This skill decides where a case goes. It does not conduct the formulation
(PORF Formulation), the pattern analysis (Contact Pattern Analysis), or
design the intervention that CRG or TL/Safety Huddle may subsequently
produce (CMP/Access Review, Safety Planning, etc.) — those are separate
skills this one may point toward. Where organisational policy specifies a
mandatory escalation threshold, policy takes precedence over this skill.
