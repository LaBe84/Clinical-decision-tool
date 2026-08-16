---
name: contact-pattern-analysis
description: >
  Analyses how a person's pattern of contact with a crisis helpline (Lifeline
  or similar) has changed — frequency, clustering, duration, timing, connected
  vs attempted vs pre-call-disconnected contact, engagement, disconnection
  behaviour — and what that change does and doesn't tell you clinically. Use
  this skill whenever the user provides call logs, contact history, or a
  description of a caller's contact pattern and asks what it means, whether it
  represents escalation or deterioration, whether the pattern is understood,
  or whether it needs review/escalation. Also use it when the user mentions
  repeated calls, frequent contact, disengagement, call volume, pre-call
  disconnections, or dropping contact frequency and wants a clinical read
  rather than a raw count. This is a distinct skill from PORF Formulation —
  PORF formulates suicide risk from a presentation; this skill formulates what
  a contact pattern itself means, and can feed into a PORF but does not
  replace one. Trigger even if the user doesn't name "Contact Pattern
  Analysis" explicitly.
---

# Contact Pattern Analysis

## Purpose

Detect and describe meaningful change in how a person is using a crisis
helpline, and identify what that change needs clinically — not decide "risk"
from contact volume. The central question:

**What has changed in this person's pattern of contact, what might that
change mean, and what cannot yet be inferred from it?**

This is a distinct job from PORF. PORF formulates suicide risk from a clinical
presentation. This skill formulates what a *pattern of contact* means, and its
output can be one input into a PORF — but counting calls is not the same task
as assessing risk, and this skill must not collapse into doing PORF's job by
another route.

## Four invariants specific to this skill

1. **Observed behaviour ≠ inferred function.** What happened is data. Why is
   an inference, and stays labelled as one unless the person has directly and
   consistently stated their own reason (see Step 4).
2. **Stable pattern ≠ effective intervention.** A pattern staying the same,
   including a calm, non-escalating one, tells you the pattern is stable. It
   does not tell you the current response is achieving anything, or that it
   isn't quietly maintaining the thing it's responding to.
3. **Reduced contact ≠ improvement.**
4. **Increased contact ≠ deterioration.**

## Foundational rules (carried from Skill 01, apply here too)

1. **Unknown is not negative evidence.** A gap in the record is a gap, not a
   finding.
2. **Behaviour is not function.** What happened (frequency, timing, duration,
   disconnection point) is observable. Why it happened is not, unless directly
   evidenced — it remains a hypothesis.
3. **Oversight escalation is not risk escalation.** Persisting, unexplained
   pattern change can justify coordinated review even when nothing establishes
   elevated suicide risk.

## Hard constraints

These must hold in every analysis, stated because they are the errors this
skill exists to prevent:

- Frequency ≠ risk.
- Frequency ≠ function.
- Disengagement ≠ absence of need.
- Non-contact ≠ improvement.
- A statistical change is not automatically a clinically meaningful change —
  magnitude and persistence matter, and an isolated variation is not the same
  finding as a sustained or accelerating one.
- Observed behaviour must be reported separately from interpretation of it.
  Never write the interpretation as if it were the observation.
- This discipline has to survive all the way to the closing lines of the
  analysis, not just the middle sections. It's easy to hold multiple
  hypotheses open through "Possible function" and then let a single
  directional summary slip in at the end — e.g. "more consistent with
  disengagement than resolution." If the material leaves the question
  genuinely unresolved, the synthesis has to say so as plainly as the
  function section did, rather than quietly picking a side once the reader's
  guard is down.

## The OCD problem: contact is not one thing

Six connected, substantive calls looks like a manageable, well-understood
pattern. The same person may also have made seventy attempts that terminated
during the pre-call message before ever reaching a counsellor. An analysis
that only counts completed, connected contacts is not looking at this
person's contact pattern — it is looking at a subset of it that happens to be
the easiest to see, and it will produce a false and falsely reassuring
clinical picture.

Always distinguish these categories where the data allows, and say explicitly
when it doesn't:

- **Attempted contact** — every attempt to reach the service, including those
  that never connect to a person (terminated during a pre-call message,
  abandoned in a queue, dropped before pickup).
- **Connected contact** — attempts that reached a counsellor, regardless of
  how long the call lasted or what was discussed.
- **Substantive engagement** — connected contact in which the person actually
  engaged with the conversation (as opposed to connecting and immediately
  disengaging or hanging up).
- **Completed intervention** — contact in which whatever the service was
  trying to achieve (support, safety planning, assessment, de-escalation)
  was actually delivered, not just attempted.

Volume at one level tells you nothing reliable about volume or meaning at
another. If you only have data on completed/connected contacts, say so as a
limitation before drawing any conclusion about the pattern as a whole —
don't let the visible subset stand in for the whole picture.

## The five things to analyse

### 1. Baseline pattern

What is usual for this person: frequency, typical duration, time of day/week,
usual engagement level, recurring themes, how contacts typically end
(planned closure, disconnection, counsellor-initiated ending), whether they
tend to stay with one counsellor or switch, whether emergency escalation has
occurred before, and how they use any planned/scheduled contact. Where no
baseline exists (first contact, or insufficient history), say so — do not
infer a baseline from a single window of data.

### 2. Current pattern — what is observably different

State only what has actually changed, precisely: frequency, clustering
(e.g. multiple attempts in a short window vs spread out), duration, repeated
short calls, pre-call disconnection, contact at unusual times (e.g. overnight
where that wasn't previous), abrupt endings, reduced engagement once
connected, rapid recontact after a call ends. Describe these as observations,
not as a diagnosis of what they mean.

### 3. Magnitude and persistence

Distinguish an isolated variation (a single unusual night) from a sustained or
accelerating change (a new pattern maintained or worsening over days/weeks).
These call for different responses even when the raw behaviours look similar
on a single night. Say explicitly which one the data supports, or that there
isn't yet enough history to tell.

### 4. Function hypotheses

Default to restraint here. The list of things contact *could* theoretically
be doing for someone is almost unlimited — containment, connection,
reassurance, regulation, checking availability, an attempted disclosure,
avoidance, response to deterioration, and so on — and generating several of
these for every case creates the appearance of formulation without adding
information. Only include a hypothesis if something in the material actually
points toward it. If nothing does, the correct output is "function is not
established from available information," not a list of plausible-sounding
guesses included to fill the section out.

There are two genuinely different situations here, and the write-up should
say which one applies:

- **Function is not established.** Most cases land here, especially with
  irregular, brief, or disconnected contact. State this directly rather than
  offering an unweighted list of speculative alternatives.
- **Function is directly evidenced.** This is different from a hypothesis,
  and rare: it applies when the person has themselves stated, directly and
  consistently across contacts, what the contact is for (e.g. explicitly
  telling separate counsellors, in the same terms, why they're calling). Where
  that exists, describe it as the observed function at the behavioural level
  — not as "one hypothesis among several" — while still not treating it as a
  diagnosis or a complete clinical explanation of why the underlying need
  exists.

Either way, do not let a single well-evidenced detail (one disclosure, one
theme) become the assumed explanation for an entire irregular or mixed
pattern. And do not describe reviewing several contacts together as
confirmation that they form "one continuous presentation" — that's an
inference. Say instead that they should be reviewed together for continuity
until it's clear whether they represent one unfolding presentation or several
different contact purposes.

### 5. Clinical significance

Ask two separate questions here, not one:

- Is this pattern adequately *explained* by the existing formulation — do we
  understand why contact looks the way it does? A pattern can be unexplained
  without being alarming, and can be explained without needing further
  action.
- Is the existing response actually *achieving* something, or is it simply
  running alongside — or possibly maintaining — the pattern it's responding
  to? A pattern that stays calm and stable every time is not, by itself,
  evidence the intervention is working. Six weeks of the same reassurance
  cycle resolving cleanly every time is a stable pattern; whether it's also an
  effective one is a different question, and one worth asking explicitly
  when function is well evidenced but the pattern keeps recurring unchanged.

  Be careful how far this goes, though: contact-pattern data can show that a
  response and a repeating pattern coexist over time. It cannot, by itself,
  establish that the response is *causing* the pattern to continue — that's a
  reinforcement/maintenance claim, and this skill doesn't have the data to
  make it. Raise it as a credible question for formulation ("the unchanged
  cycle raises a question about whether the response may be maintaining
  reliance on it — this needs formulation, not assumption"), not as a
  conclusion ("the reassurance is maintaining the behaviour"). Temporal
  association is not the same claim as causal maintenance.

## Output format

Always structure the output like this, and keep it substantially shorter than
a PORF — this skill answers a narrower question:

```
CONTACT PATTERN ANALYSIS

Established pattern
[What's usual for this person, or "no established baseline"]

Observed change
[What is actually different — attempted/connected/substantive/completed,
as available. Observation only, not interpretation.]

Engagement pattern
[How the change plays out once contact is made, where known]

Possible function — hypotheses only
[Plausible readings, explicitly unresolved unless genuinely supported]

What remains unknown
[Material gaps — including which contact-category data is missing]

Clinical significance
[Whether the existing formulation/intervention adequately accounts for this]

Therefore
[One of: Helpline / TL-Safety Huddle / CRG — see below]
```

## The "Therefore": a narrower question than PORF's

Do not let "Therefore" default into prescribing a CMP, an access restriction,
or any other specific intervention — that is not this skill's job, and doing
so would be exactly the kind of unearned procedural leap Skill 01 had to be
corrected out of. The question is narrower and specific to pattern:

**Is the current contact pattern sufficiently understood, and is it
adequately managed by the existing formulation and intervention?**

That produces exactly three possible conclusions — pick one and say why, using
this decision logic in order:

1. Is the pattern adequately explained, and is there no actual operational or
   coordination problem in front of you right now? → **Helpline** — the
   pattern and function are recorded, kept under ordinary review, with
   escalation to follow only if genuinely new evidence emerges (the
   intervention turns out ineffective or maintaining, the pattern materially
   changes, inconsistent responses across staff appear, or an operational
   decision becomes actually necessary). An open formulation question about
   whether the response is optimal is worth recording and watching — it is
   not, by itself, a reason to escalate today. Don't invent a destination for
   a case just because it's clinically interesting to think about; route on
   what the case in front of you actually requires right now.
2. Is there an *actually evidenced* coordination or visibility problem —
   contact genuinely split across many people/short windows/disconnected
   attempts such that no one holds the full picture, or inconsistent
   responses across staff, or an operational decision that needs real-time
   agreement — that needs joining up before the pattern can even be properly
   understood? → **TL/Safety Huddle**, even if the underlying function may
   still turn out to be benign once the picture is complete. State the
   visibility gap in concrete terms (e.g. "the recorded picture is based on
   only 9% of total attempts") rather than a vaguer word like "fragmenting."

   Don't manufacture this trigger. A consistent pattern, independently and
   congruently observed by more than one counsellor, with no conflicting
   responses and no operational decision actually pending, is not a
   coordination problem just because there's an unresolved formulation
   question sitting underneath it. An unknown gap in the data (e.g. no
   visibility into attempted/pre-call contact) is something to note and check
   — it only becomes a TL/Safety Huddle trigger if there's a real reason to
   think it's material, not by default.
3. Only once the picture is as complete as it can reasonably be: does the
   pattern or its function remain genuinely unexplained, *or* does the
   existing intervention no longer appear to be achieving its intended
   outcome (including possibly maintaining the pattern it responds to)? →
   **CRG.**

The rule to hold onto: sustained change on its own is not the CRG trigger.
Sustained *unexplained* change is a reason to check whether the current
formulation still accounts for it; CRG follows specifically when that check
comes up short — either the pattern/function stays unexplained after
reasonable review, or the intervention isn't achieving its purpose — not
merely because a change has persisted for some number of weeks. Persistence
alone more often points to TL/Safety Huddle for coordinated review than to
CRG.

Never use frequency alone, or disengagement alone, to justify any of the
three — the conclusion must follow from whether the pattern is *understood
and adequately managed*, not from how much contact there has been.

## Reasoning shortcuts to avoid

- "High call volume therefore high risk" or "therefore attention-seeking" —
  volume tells you about behaviour, not about risk or motive.
- "Calls have dropped off therefore they're doing better" — declining contact
  can equally reflect disengagement, loss of trust in the service, or reduced
  capacity to reach out; it is not evidence of improvement on its own.
- "Can't tell why they're calling so much therefore nothing to do" — an
  unresolved function is itself sometimes the reason for TL/Safety Huddle or
  CRG involvement (oversight escalation, not risk escalation).
- "Six calls counted therefore that's the pattern" — when pre-call
  disconnections or attempted-but-unconnected contacts exist and haven't been
  reviewed, say so as a limitation before characterising the pattern.
- Treating a single dramatic night as proof of a new sustained pattern, or
  treating a sustained pattern as "just one bad night" because the most recent
  contact looked calmer.
- "Sustained change therefore CRG" — sustained change unexplained by the
  current formulation is a reason to check whether that formulation still
  holds; CRG follows only if the check shows the pattern/function still isn't
  explained or the intervention isn't working, not from persistence alone.
- "Calm and stable every time therefore the response is working" — a pattern
  not escalating is not the same finding as an intervention achieving its
  purpose; it may simply be running alongside, or maintaining, the thing it
  responds to.
- Filling the function-hypotheses section with several plausible-sounding
  explanations when nothing in the material points toward any of them —
  "function not established" is the correct answer far more often than a
  generated list.
- Inventing a coordination or visibility problem to justify TL/Safety Huddle
  when the actual evidence is a consistent pattern, congruently observed
  across staff, with no conflicting responses and no operational decision
  pending — an interesting unresolved formulation question is not the same as
  a coordination problem. Route on what the case needs right now, not on
  whether escalating gives you somewhere to put an open question.

## Boundary

This skill analyses contact behaviour. It does not itself formulate suicide
risk (use PORF Formulation for that, informed by this analysis where
relevant), does not prescribe a CMP, access agreement, or other specific
intervention, and does not determine the operational detail of how a
TL/Safety Huddle or CRG referral should be actioned — it identifies that a
question exists and at what level it should be resolved. Where organisational
policy specifies a mandatory review threshold, policy takes precedence over
this skill.
