---
name: inference-control
description: >
  Given established facts about a crisis-helpline case, determines what
  conclusions actually follow from them and how strong a claim the evidence
  legitimately supports. Use this skill whenever the user has established
  facts (not gaps — that's Evidence-Gap Detection's job) and needs to know
  whether a proposed conclusion is warranted, whether "consistent with" is
  being quietly upgraded to "demonstrates," whether a pattern claim or causal
  claim is actually supported by the record, or whether competing
  explanations have been prematurely collapsed into one. This is not a
  formulation skill — it does not build an explanatory model or decide what
  a case means clinically (that's PORF), does not detect missing information
  (that's Evidence-Gap Detection), and does not decide what to do (that's a
  decision skill). It governs the inferential step between established facts
  and the claims built on them: what follows, and how strongly can it be
  said to follow. Trigger even if the user doesn't say "inference" by name
  but asks whether a conclusion "holds up," whether something has actually
  been shown or just seems to fit, or wants a check on whether a pattern or
  causal claim in a write-up is actually supported by what's documented.
---

# Inference Control

## Purpose

**Given the facts that are established, what conclusions actually follow
from them, and how strong can that claim legitimately be?**

This is the step between "what do we know" (Evidence-Gap Detection's
territory) and "what does it mean" (Formulation's territory). Evidence-Gap
Detection governs missingness — is a decision-relevant fact unresolved.
This skill governs overreach — given the facts that ARE resolved, does the
conclusion drawn from them actually follow, or does it claim more than the
evidence supports. A record can be complete, with no gaps at all, and still
license a conclusion the facts don't actually prove. That is a different
failure mode from a gap, and it needs its own discipline.

## Foundational rules (carried from Skills 01–09)

1. Unknown is not negative evidence.
2. Behaviour is not function — carried forward as the founding case of this
   skill's whole territory: an observed behaviour is direct evidence: why it
   happened is an inference, and the strength of that inference has to be
   assessed on its own terms, not smuggled in as if it were part of the
   observation.
3. This skill does not overwrite the conclusions of any upstream skill and
   does not build the explanatory model itself — it tests whether a
   proposed or existing conclusion is actually entailed by the evidence, and
   states how strong a claim the evidence supports. What to do with that
   assessment belongs to whoever owns the formulation or decision.
4. Evidence gap ≠ decision gap (Evidence-Gap Detection's invariant) has a
   sibling here: **evidence present ≠ conclusion proven.** A complete record
   is not the same claim as a record that entails the conclusion drawn from
   it.

## The core distinction: observation vs. inference

Every claim in a case record sits somewhere on this line, and conflating the
two ends is the central failure this skill exists to catch:

- **Observation** — what was directly seen, heard, said, measured, or
  documented. "The caller said X." "Contact frequency doubled in week 3."
  "A call was logged on each of these dates." Observations are not
  themselves in question here — Evidence-Gap Detection and the enquiry
  skills establish what was observed; this skill starts from observations
  taken as given.
- **Inference** — anything derived from observations that isn't itself
  directly observed: why something happened, what a pattern means, whether
  one thing caused another, what an observation is "consistent with" versus
  what it "demonstrates." Every inference needs its own justification and
  its own calibrated strength — it does not inherit the certainty of the
  observations it's built on.

Never let inference language ("suggests," "indicates," "reflects," "is
driven by," "shows") attach to a claim without first checking whether that
claim is actually an inference from stated observations or is being
presented as though it were the observation itself.

## The five overreach patterns to catch

### 1. Correlation presented as causation
Two things co-occurring, or one following the other in time, is evidence of
an association at most. "X happened, then Y deteriorated" describes a
temporal sequence, not a causal mechanism. Causal language ("caused,"
"triggered," "led to," "resulted in") requires more than sequence — it
requires either a stated, testable mechanism, or a pattern robust enough
(see #2) to support a calibrated causal inference, and even then the
strength of that claim has to be stated honestly, not asserted as fact.

### 2. Repetition presented as corroboration
The same claim appearing in multiple places in a record is not the same
thing as independent corroboration of that claim. Distinguish: the same
source repeating a claim across several occasions (multiple observations of
that source's consistency, which is worth something — it's evidence the
account is stable and not a one-off remark — but each repetition is still a
report from the same single source, not an independent check on whether the
claim is actually true), the same observer documenting the same event
multiple times (still one observation), versus genuinely independent
observations, by different observers, of separate instances of the same
pattern (this is what actually strengthens an
inference). Count instances honestly — don't let volume of documentation
substitute for number of independent instances.

### 3. "Consistent with" quietly becoming "demonstrates"
"Consistent with X" means the evidence does not rule X out and fits a
plausible account — it does not mean X has been shown. Watch for this
exact drift within a single piece of reasoning: a finding introduced as
"consistent with reassurance-seeking" that two sentences later is being
treated as an established reassurance-seeking mechanism. If the evidence
only supports "consistent with," the conclusion has to stay at "consistent
with" — upgrading it partway through the reasoning is the overreach, even
when no single sentence looks wrong in isolation.

### 4. Competing explanations collapsed prematurely
Where the evidence is equally consistent with more than one explanation,
name more than one. Selecting the most clinically interesting, the most
alarming, or the most convenient explanation among several equally
supported ones is overreach, even if that explanation later turns out to be
right — it wasn't warranted by the evidence at the time it was asserted.
State what would distinguish between the competing explanations if that's
known, and if it isn't, say so rather than picking one.

### 5. Conclusion strength uncalibrated to evidence strength
Every conclusion has to be stated at a strength the evidence actually
supports — no stronger, and no weaker than warranted either (excessive
hedging on a well-supported conclusion is its own failure, since it denies
the case the confidence it has actually earned). Use a deliberately graded
vocabulary and hold it consistently:
- **Established** — directly observed, not an inference.
- **Well-supported** — a calibrated inference from a genuinely robust
  pattern (independent instances, consistent findings, no equally-plausible
  competing explanation).
- **Consistent with / plausible** — fits the evidence, does not contradict
  it, but doesn't rule out alternatives and isn't independently
  corroborated.
- **Speculative** — a single data point, an untested hypothesis, or a claim
  resting on an inferential leap the evidence doesn't yet support. Name it
  as speculative rather than dressing it in more confident language.

## Boundary rules

- **Do not build the explanatory model.** This skill tests whether a
  specific conclusion follows from stated evidence and at what strength — it
  does not construct the case formulation itself. Say what's warranted and
  at what strength; hand the synthesis to Formulation (PORF).
- **Do not detect missing information.** If the reason a conclusion can't be
  reached is that a decision-relevant fact is unresolved, that's Evidence-
  Gap Detection's territory, not this skill's. This skill starts from facts
  already established (or already flagged as established/hypothesis/gap by
  upstream skills) and tests what follows from them.
- **Do not decide what should happen as a result of a calibrated
  conclusion.** Whether a well-supported pattern warrants escalation,
  intervention, or further enquiry is a decision skill's call. This skill's
  output is an input to that decision, not the decision itself.
- **Do not resolve a genuine ambiguity by picking the more clinically
  serious-sounding interpretation.** Erring toward the alarming explanation
  "to be safe" is still overreach — it just fails in a specific direction.
  State the competing explanations and their relative support honestly, even
  when one of them is less concerning than the other.
- **Do not let strength language drift over the course of an output.** If a
  claim starts as "consistent with," every later reference to it in the same
  output has to stay at that strength unless something in the reasoning
  actually earns an upgrade — and if it does, that upgrade has to be shown,
  not asserted.
- **Do not treat this skill's own calibration as itself a risk judgement.**
  "Well-supported" or "speculative" describes the evidential relationship
  between the claim and the record — it is not a statement about how
  concerning the underlying situation is. A speculative claim can concern a
  serious possibility; a well-supported claim can concern something benign.
  Keep those two axes (evidential strength, clinical seriousness) separate.

## Inputs

The specific conclusion or claim under examination (stated explicitly), and
the established facts or observations it's meant to rest on — supplied
directly, or drawn from upstream skills' output where those facts are
already marked as established, hypothesis, or gap. This skill does not go
looking for additional facts; it tests the inferential step from what's
already on the table.

## Output format

```
INFERENCE CONTROL ANALYSIS

Claim under examination
[The specific conclusion, as stated or proposed]

Underlying observations
[What is directly established, listed separately from any interpretation
of it]

Inferential step required
[What has to be inferred to get from the observations to the claim —
named explicitly, not skipped over]

Overreach check
[Which of the five patterns, if any, the claim is at risk of: correlation
as causation / repetition as corroboration / "consistent with" drifting to
"demonstrates" / competing explanations collapsed / strength uncalibrated]

Competing explanations
[Other accounts equally or near-equally consistent with the same
observations, if any — named rather than silently ruled out]

Calibrated conclusion
[The claim restated at the strength the evidence actually supports:
established / well-supported / consistent with-plausible / speculative —
with the reasoning for that grading shown]

What this does not establish
[What the claim, even at its calibrated strength, cannot be used to
support]

Residual interpretive uncertainty
[Where more than one account remains live, and what would be needed to
distinguish between them, if known]
```

## Reasoning shortcuts to avoid

- Writing "X happened, then Y" and letting causal language attach to it two
  sentences later without ever stating the causal claim needs its own
  justification.
- Counting the same account, restated across several contact notes, as
  multiple pieces of evidence rather than one.
- Introducing a finding as "consistent with" a pattern and later in the same
  output treating that pattern as established.
- Picking the more clinically serious of two equally-supported explanations
  because it feels safer to assume the worse case, without naming the less
  serious alternative at all.
- Hedging a conclusion that the evidence actually supports strongly, out of
  general caution, denying the case the confidence it has legitimately
  earned.
- Treating "the record doesn't rule this out" as equivalent to "the record
  supports this" — absence of contradiction is not evidence for a claim.
- Letting the strength label on a claim change silently between one section
  of an output and another without new reasoning to justify the change.

## Boundary

This skill tests whether a proposed conclusion is entailed by stated
evidence and at what strength. It does not conduct enquiry, detect missing
information, formulate risk, analyse contact pattern, decide triage
destination, review access arrangements, build safety plans, or select
interventions — those are Skills 01 through 09, and this skill does not
redo or substitute for their work. It does not decide what should happen as
a result of a calibrated conclusion — that belongs to whichever skill owns
the decision. It does not override the immediate risk pathway — where
danger is already directly established (not inferred), that is acted on
directly, not routed through an inference-strength assessment. Where
organisational policy specifies mandatory evidentiary standards, policy
takes precedence over this skill.
