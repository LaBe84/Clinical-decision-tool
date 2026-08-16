---
name: decision-calibration
description: >
  Given a calibrated belief (established, well-supported, consistent with,
  or speculative — Inference Control's vocabulary) and its consequences,
  determines what action is proportionate to act on it, distinct from how
  confident the belief itself is. Use this skill whenever the user has an
  inference or finding of known strength and needs to know what, if
  anything, that strength justifies doing about it — especially when
  someone is either dismissing a low-confidence concern as unactionable, or
  treating a low-confidence concern as though it were established fact to
  justify maximal response. This is not an inference skill (it does not
  determine how strong a belief is — that's Inference Control) and not a
  domain decision skill (it does not select the specific intervention,
  triage destination, or access arrangement — those are Intervention
  Selection, CRG Triage, and CMP/Access Review). It provides the general
  reasoning for calibrating action to belief-strength-and-consequence, which
  those domain skills draw on. Trigger even if the user doesn't say
  "decision calibration" by name but asks whether an uncertain finding
  justifies acting, whether a strong finding is being hedged into inaction,
  or whether an action is disproportionate to how confident anyone actually
  is in the underlying belief.
---

# Decision Calibration

## Purpose

**Given a belief of known strength and known consequence if wrong, what
action is proportionate — and is that a different question from how
confident the belief itself is?**

Inference Control determines what can responsibly be believed, and at what
strength. This skill determines what can responsibly be done given that
belief, its uncertainty, the consequence of acting on it if it's wrong, and
the consequence of not acting on it if it's right. Confidence in a claim and
the threshold for acting on it are two different axes — collapsing them
produces two opposite and equally common errors, and this skill exists to
prevent both.

**There is no fixed mapping from belief strength to action.** Action is
calibrated against belief strength × consequence of omission × consequence
of commission × reversibility × availability of lower-cost alternatives ×
applicable clinical/governance requirements — not against belief strength
alone. A speculative belief can justify a consequential action in the right
circumstances (severe, hard-to-reverse consequence of omission; no
lower-cost alternative that would resolve the uncertainty in time). An
established belief may still not justify a particular consequential action
(the specific action may not be the right response even to a fact that's
fully proven). This skill tests the specific proposed action against all of
those factors every time — it does not consult a lookup table from
evidence tier to action tier, and must never state or imply that a
particular class of action universally requires a particular belief
strength (e.g. "restriction requires established causation," "established
findings mandate emergency intervention"). Those are exactly the fixed
mappings this skill exists to prevent from calcifying into the reasoning.

## Foundational rules (carried from Skills 01–10)

1. Unknown is not negative evidence.
2. Behaviour is not function.
3. This skill does not determine belief strength itself (Inference Control's
   job) and does not select the specific intervention, destination, or
   arrangement (the domain decision skills' job) — it provides the general
   calibration between belief strength, consequence, and proportionate
   action that those skills draw on.
4. Evidence gap ≠ decision gap; evidence present ≠ conclusion proven
   (Evidence-Gap Detection and Inference Control's invariants) have a third
   sibling here: **belief strength ≠ action threshold.** How confident a
   claim is and how much that confidence justifies doing are different
   questions, answered by different reasoning, and must not be collapsed
   into one step.

## The two opposite errors this skill exists to prevent

Both are common, both sound reasonable in the moment, and they are mirror
images of the same underlying mistake — treating belief strength and action
threshold as one thing instead of two:

**Error 1 — treating uncertainty as license for inaction.** "We can't prove
the caller is concealing suicidality, therefore we shouldn't respond to that
possibility." This ignores that action thresholds are set by consequence as
well as by confidence. A low-confidence hypothesis can still justify a
precautionary, low-cost, reversible action when the cost of being wrong (if
the concern is real and nothing was done) is severe and the cost of the
precaution (if the concern turns out to be unfounded) is small.

**Error 2 — treating uncertainty as though it were established fact to
justify a strong response.** "Concealment is possible, therefore treat
concealment as established and escalate maximally." This borrows the
weight of a strong claim to justify an action that only a strong claim
would warrant, without the claim actually having earned that strength. A
speculative or consistent-with-level finding can justify a proportionate,
low-cost, reversible response — it does not by itself justify a maximal,
high-cost, hard-to-reverse one.

Both errors are attempts to avoid the harder work this skill exists to do:
holding belief strength and action threshold as separate axes and reasoning
about their intersection explicitly, rather than letting one substitute for
the other.

## The core reasoning chain

**Evidence → inference strength → decision threshold → proportionate
action.**

This skill starts from the second step (inference strength, already
established by Inference Control or stated directly) and does the last two
steps: what threshold does this situation call for, and what action clears
that threshold without exceeding it.

### 1. Belief strength (taken as given)
State the calibrated strength of the finding under examination —
established / well-supported / consistent with-plausible / speculative —
as established elsewhere. This skill does not re-derive it.

### 2. Consequence if the belief is true and no action is taken
What happens if the concern is real and nothing is done. This is not a
license to catastrophise — state the actual, specific consequence, not the
worst imaginable one, and note where the consequence itself is also
uncertain.

### 3. Consequence if the belief is false and action is taken anyway
What the action costs if the concern turns out to be unfounded — to the
person, to the relationship, to future engagement, operationally. A
precautionary action with low cost-if-wrong has a very different threshold
than a restrictive or high-cost action with the same belief strength behind
it.

### 4. Reversibility and cost of the candidate action
Distinguish sharply between actions that are reversible, low-cost, and
primarily information-gathering (asking a direct question, a follow-up
contact, a brief check) and actions that are consequential, hard to
reverse, or carry a real cost of their own (an access restriction, a
significant escalation, an intervention that changes the person's
relationship with the service). This is one input into the threshold, not a
rule that fixes what belief strength each category requires — a reversible
action generally needs less to justify it and a consequential one generally
needs more, but "generally" is not "always," and the actual threshold is
set by weighing this alongside consequence, alternatives, and governance
requirements together, not by reversibility alone.

### 5. Lower-cost alternatives and governance requirements
Before settling on a proposed action, check whether a lower-cost action
would resolve the same uncertainty or address the same consequence
adequately — if one would, that changes what the higher-cost action needs
to justify it. Separately, check whether any organisational policy, legal
duty, or governance requirement independently applies to the situation
(e.g. a mandatory safeguarding threshold, a legal duty to act on certain
disclosures) — those can lower or raise the bar independent of the belief-
strength-and-consequence analysis, and should be named as a distinct factor
rather than folded silently into the consequence reasoning.

### 6. Proportionate action
State what class(es) of action actually clear the threshold set by steps
2–5, given the belief strength from step 1 — not the single action that
feels most responsive, and not "no action" by default. Where several
classes of action would be proportionate, name more than one rather than
presenting one as the only option available. Name the class and intensity
of action warranted (e.g. "reversible clarification," "anticipatory
precaution incorporated into existing process," "immediate real-time
safety response") — not the specific downstream design of that action
(exact wording of a question, specific plan content, specific emergency
disposition). Designing the action itself belongs to the owning skill.

## Boundary rules

- **Do not let belief strength alone determine the action.** A well-
  supported or established finding does not automatically justify every
  intervention someone attaches to it — the action still has to be tested
  against its own cost and reversibility, not waved through because the
  underlying belief is strong.
- **Do not let low belief strength alone rule out action.** A speculative or
  consistent-with finding is not grounds for "therefore nothing can be
  done" — test whether a low-cost, reversible, precautionary action is
  justified by the consequence of being wrong, independent of how
  confident anyone is in the underlying claim.
- **Do not borrow the weight of a strong claim for a weak one.** If the
  proposed action requires established-level confidence to justify, and the
  actual finding is speculative or consistent-with, say so explicitly —
  don't let the action's own urgency retroactively inflate the belief
  strength backing it.
- **Do not present one action as the only option when several would clear
  the threshold.** Naming a single "the" response where multiple
  proportionate options exist forecloses choice that should remain open —
  name the set, not a single inevitable pick, unless the situation actually
  narrows to one option.
- **Do not treat reversible, information-gathering actions and
  consequential interventions as the same category of "doing something."**
  A follow-up question and an access restriction are not interchangeable
  ways of "responding to the concern" — they sit at different points on the
  cost/reversibility axis and need different justificatory weight.
- **Do not select the specific intervention, destination, or arrangement.**
  This skill says what class and intensity of action the belief-strength-
  and-consequence analysis supports — the actual selection among that class
  (which specific intervention, which specific destination) belongs to the
  owning domain skill (Intervention Selection, CRG Triage, CMP/Access
  Review, Safety Planning).
- **Do not manufacture consequence to justify a preferred action.** State
  the actual, specific consequence of inaction and of wrongful action — not
  an inflated worst case used to justify a stronger response than the
  belief and situation actually support.
- **Do not state or imply a fixed mapping from belief strength to action
  class.** Never write that a class of action (restriction, emergency
  intervention, escalation) universally "requires" a specific belief
  strength (established, well-supported, etc.). State instead why the
  specific combination of consequence, reversibility, alternatives, and
  governance requirements does or doesn't support the specific action in
  front of you. The same belief strength can license different actions in
  different circumstances, and the same action can be licensed by different
  belief strengths depending on those other factors — test the actual
  combination every time.
- **Do not upgrade the underlying clinical or factual state beyond what was
  actually established.** This skill takes the belief and its calibrated
  strength as given — it must not restate a specific, bounded finding
  (e.g. "active ideation with a plan and timeframe") as a broader
  conclusion (e.g. "established imminent risk") that wasn't itself
  established. If the belief strength or facts given don't specify
  imminence, current intent, access to means, or capability, don't assume
  them to justify a stronger action — name what would need to be true for
  the strongest response to be warranted, and note whether that's already
  established, and by whom (Suicide Enquiry, PORF, real-time
  observation), or whether it still needs resolving through the
  appropriate process.
- **Do not attribute unsupported motive to explain a finding.** If a
  finding could plausibly reflect several different motives or no motive at
  all, don't select one (e.g. "the caller may have been testing the
  response") as part of the calibration — that's an inference this skill
  didn't establish and isn't entitled to introduce.
- **Do not design the downstream action.** State the class and intensity of
  action the analysis supports (see step 6) — not its specific content,
  wording, conversational method, or operational detail. If output starts
  specifying exact phrasing, a specific number of permitted attempts, or
  the detailed content of a plan, that has crossed into a domain skill's
  territory.

## Output format

```
DECISION CALIBRATION

Belief under examination
[The finding and its calibrated strength, as given]

Consequence if true and unaddressed
[Specific, not worst-case; note if this itself is uncertain]

Consequence if false and acted upon
[What the candidate action(s) cost if the concern is unfounded]

Reversibility and cost of candidate actions
[For each candidate action: reversible/information-gathering, or
consequential/hard-to-reverse — named explicitly]

Lower-cost alternatives and governance requirements
[Would a cheaper action resolve the same uncertainty or address the same
consequence? Does any policy, legal duty, or governance requirement
independently apply, distinct from the belief-strength-and-consequence
analysis?]

Threshold analysis
[Test the specific proposed action against belief strength, consequence of
omission, consequence of commission, reversibility, alternatives, and
governance requirements together — not against belief strength alone, and
not against a fixed rule for what this class of action always requires]

Proportionate action(s)
[The class(es) and intensity of action justified — naming more than one
where more than one clears the threshold, not collapsing to a single "the"
response. Name the class, not its downstream design or specific content]

What is not justified
[Actions that would require a stronger belief, lower cost, or higher
reversibility than what's actually present]

Residual judgement
[Where the calibration genuinely leaves room for judgement between
proportionate options, name that rather than resolving it artificially]
```

## Reasoning shortcuts to avoid

- "We can't prove it, so we shouldn't act" — collapsing action threshold
  into belief strength and ignoring consequence and reversibility entirely.
- "It's possible, so we should treat it as established and respond
  maximally" — borrowing the weight of a strong claim for a speculative
  one.
- Hedging a well-supported finding into a weak, non-committal response
  because the action itself feels uncomfortable to commit to — that's an
  action-threshold failure dressed up as epistemic caution.
- Naming a single response as inevitable when a lower-cost, equally
  proportionate alternative exists and hasn't been considered.
- Treating "we asked a follow-up question" and "we restricted access" as
  equivalent evidence of having "done something about" a concern.
- Inflating the stated consequence of inaction to justify a
  disproportionately strong response.
- Skipping the reversibility/cost analysis and jumping straight from belief
  strength to action, as though the two were the same calibration.
- Stating that a class of action universally "requires" a specific belief
  strength (e.g. "restriction requires established causation") instead of
  testing the specific action against the full set of factors each time.
- Restating a bounded finding (e.g. "plan and timeframe disclosed") as a
  broader clinical conclusion (e.g. "established imminent risk") that
  wasn't itself established, in order to justify a stronger action.
- Attributing an unsupported motive to explain a finding (e.g. "may have
  been testing the response") as part of the calibration.
- Specifying the exact wording, method, or operational detail of the
  proportionate action rather than naming its class and intensity.

## Boundary

This skill calibrates the relationship between belief strength, consequence,
reversibility, alternatives, governance requirements, and proportionate
action class. It does not determine how strong a belief is (Inference
Control), does not detect missing information (Evidence-Gap Detection),
does not conduct enquiry, formulate risk, analyse contact pattern, decide
triage destination, review access arrangements, build safety plans, or
select or design specific interventions — those are Skills 01 through 09
and the domain decision skills, and this skill does not redo or substitute
for their work. It does not itself determine imminence, capability, or
current danger where those haven't already been established by an
upstream skill or real-time observation — if the belief given to this
skill doesn't already establish those things, this skill must not assume
them in order to justify a stronger action class; it should instead say
that resolving them (through the appropriate real-time process, not
through further calibration) is what determines the actual response. Where
danger is already directly established by an upstream skill or real-time
observation, action is not gated behind a calibration exercise. Where
organisational policy specifies mandatory response thresholds, policy
takes precedence over this skill.
