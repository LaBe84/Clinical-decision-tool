---
name: suicide-enquiry
description: >
  Structures direct suicide enquiry using the CASE chronology (recent/
  immediate, recent months, lifetime, current/next) to establish what is
  known about a caller's suicidality — not what it means clinically. Use this
  skill whenever the user is asking how to conduct, structure, or review
  direct suicide enquiry for a crisis-helpline contact, wants help working
  out what's been asked versus what's still missing across a call or a
  chronology, or has call notes/transcripts and wants the suicidality
  information organised before formulation. This is an information-
  acquisition skill, not a formulation skill — it does not determine risk
  level or proportionate response (that's PORF Formulation) and does not
  decide where a case should go (that's CRG Triage). Trigger even if the user
  doesn't say "CASE" or "suicide enquiry" by name but describes wanting to
  check what's been established about someone's suicidal thoughts, plans, or
  history, or wants a gap-check on enquiry completeness.
---

# Suicide Enquiry

## Canonical dependencies

Apply the following **draft** canonical rules. They define shared reasoning discipline; organisational policy and mandatory procedure take precedence. Preserve this skill’s bounded application logic and route gaps rather than recreating upstream reasoning.

- [authority-and-uncertainty](/canonical/00-system-principles/authority-and-uncertainty.md)
- [override-principle](/canonical/01-immediate-safety/override-principle.md)
- [case-chronology-and-evidence](/canonical/02-suicide-enquiry/case-chronology-and-evidence.md)



## Purpose

Establish what is currently known about a person's suicidality, organised so
it's actually usable — not produce a risk judgement. This skill has exactly
one job: **enquiry, not assessment.**

**Suicide Enquiry establishes what is known about suicidality. PORF
determines what that information means for this person now.** Every output
this skill produces should be usable as an input to a PORF — dates, direct
quotes, specific facts organised by chronology — not a set of conclusions
that quietly does PORF's job under a different heading.

## Shared rules

Apply the canonical dependencies above; do not restate or reinterpret them in this skill.
## The two failure modes this skill exists to prevent

Both look like thoroughness. Neither is enquiry.

**A checklist masquerading as assessment.** Running through a fixed set of
questions and recording yes/no answers produces the *appearance* of rigour
without the substance — it tells you a question was asked, not what was
actually learned, and it invites treating "no" to a screening question as
reassurance rather than as one data point in an unfolding picture. Enquiry
has to stay conversational and responsive to what's actually being said, even
while it's structured.

**An AI-generated risk score.** This skill must never produce a number, a
category ("low/medium/high risk"), or a synthesised risk statement. That is
PORF's job, and it needs the raw material this skill produces to do it
properly — a formulation built on this skill's own premature scoring would
just be laundering the same shortcut through two skills instead of one.

## The CASE chronology

Structure enquiry — and the write-up of what enquiry has established — around
four time horizons. Move through them in whatever order the conversation
naturally supports; write them up in this order regardless, since a
chronological record is what makes the material usable to PORF:

### Current/immediate
What is happening right now, in this contact: current thoughts, any plan,
timeframe, access to means, what's already been done or attempted today,
intent as it stands at this moment. This is the most time-sensitive category
and the one enquiry should not leave vague.

### Recent (the period leading up to this contact — typically recent
weeks/months)
How suicidality has presented recently: frequency, intensity, any escalation
or change, any recent attempts or preparatory behaviour, what's been
different about this period compared to how things usually are for this
person.

### Lifetime
Prior history: previous suicidal ideation, previous attempts (with dates/
approximate timeframes and methods where disclosed), previous crisis
presentations. Previous service contact and family history are useful
contextual information where they come up, but they are not equivalent to
previous ideation, attempts, or suicidal behaviour, and their absence from
the material doesn't make lifetime enquiry incomplete — don't treat them as
mandatory completion criteria for this horizon.

### Current/next (anticipated)
What's coming: any specific plan for after this contact ends, what the
person says they intend to do tonight/this week, anything they identify as
likely to change how they're feeling or what they might do.

For each horizon, record only what was actually established — a direct
account of what was said or observed, not an inference about what it implies.
Where a horizon wasn't or couldn't be covered in the material available, say
so plainly rather than leaving a silent gap that looks like "nothing to
report."

## Enquiry discipline

- **A "no" is data, not closure.** Record what was asked and what was
  answered; do not editorialise the answer as reassuring or as closing the
  matter. That interpretive step belongs to PORF.
- **Reluctance, deflection, or a change of subject is itself enquiry
  material** — record it as observed (what happened when the topic was
  raised), not as a conclusion about what it means.
- **Use the person's own words where they're available**, especially for
  plan, means, and intent — paraphrase loses exactly the specificity PORF
  needs.
- **Don't average or round off inconsistent information.** If different
  points in a contact (or across a chronology of contacts) give different
  answers, record both, with when each was said — don't quietly resolve the
  discrepancy into a single tidy account.

## Output format

```
SUICIDE ENQUIRY

Current / immediate
[What's known now: thoughts, plan, timeframe, means, intent, actions taken]

Recent
[What's known about the recent period: frequency, intensity, change, recent
attempts/preparatory behaviour]

Lifetime
[What's known about prior history: previous ideation, attempts, service
contact, family history where disclosed]

Current / next (anticipated)
[What's known about what's expected next: stated plan for after contact,
identified changes]

What was directly established
[Explicit note of which parts of the above came from direct enquiry versus
what is still unasked or unclear]

Gaps
[What enquiry hasn't yet established, named plainly — not filled, not
guessed at]
```

Do not add a risk level, a synthesis of what this "means," or a recommended
response anywhere in this output — if you find yourself writing a sentence
that starts to sound like a formulation conclusion, that sentence belongs in
PORF, not here. Hand this output to PORF Formulation as its enquiry material.

This boundary is about *interpretation and routing*, not about withholding
action. Keep two things separate, the same way CMP/Access Review keeps the
safety pathway outside any access arrangement: clinical interpretation of
what enquiry findings mean, and what the proportionate ongoing response is,
belongs to PORF/CRG Triage and stays outside this skill. But if what's
disclosed *during* enquiry is itself an immediate safety concern — active
means in hand, an attempt in progress, anything requiring action right now —
that gets acted on immediately, in real time, by whoever is on the call. It
is never delayed, and never should be delayed, by this skill's boundary
against producing a risk judgement. This skill declining to assign a risk
level is not the same thing as this skill (or the person using it) declining
to respond to an emergency that's unfolding in front of them.

## Reasoning shortcuts to avoid

- Treating a direct denial of current suicidal ideation as equivalent to "no
  risk" — that's a formulation judgement, and even as a judgement it's one
  PORF has already been built to avoid making.
- Filling a CASE horizon that wasn't actually covered with an inference from
  another horizon ("lifetime history suggests recent presentation was
  probably similar") — each horizon gets recorded on its own evidence.
  
- Recording only the questions asked, without recording what was actually
  said in response — a checklist of "asked: yes" without content is not
  enquiry material PORF can use.
- Smoothing over inconsistent answers into one clean account instead of
  showing the actual inconsistency and when each version was given.
- Slipping a risk category, score, or "therefore" statement into this
  output — that is exactly the boundary this skill exists to hold.

## Boundary

This skill establishes what is known about suicidality through direct
enquiry, organised by CASE chronology. It does not determine risk level or
proportionate response (PORF Formulation), does not decide where a case
should go (CRG Triage), does not analyse contact-pattern behaviour (Contact
Pattern Analysis), and does not review access arrangements (CMP/Access
Review). Where organisational policy specifies mandatory enquiry content,
policy takes precedence over this skill.
