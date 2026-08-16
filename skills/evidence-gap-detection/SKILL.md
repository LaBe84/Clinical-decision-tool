---
name: evidence-gap-detection
description: >
  Performs an epistemic audit on the material presented for a crisis-helpline
  case: identifies what is not established, and classifies whether that
  absence materially constrains the decision currently being made. Use this
  skill whenever the user needs to know if missing information actually
  matters to a specific decision, is under pressure to "get more information"
  before deciding, is being asked to treat an absence of documentation as
  reassuring or as evidence of risk, or has material that looks thorough but
  may be silently avoiding the one fact a decision depends on. This is not a
  formulation, enquiry, triage, or intervention skill — it does not gather
  missing information, decide risk, select interventions, or route workflow.
  It classifies gaps by decision consequence and hands that classification to
  whichever skill owns the actual decision. Trigger even if the user doesn't
  say "evidence gap" by name but asks whether something is "enough to go on,"
  whether a missing piece of information changes anything, or wants a second
  opinion on whether a decision is being made on solid ground.
---

# Evidence-Gap Detection

## Purpose

**What is not established, and does that absence materially constrain the
decision currently being made?**

This is an epistemic audit, not an information-gathering exercise and not a
clinical judgement. It examines the material already presented for a specific
decision and classifies what's missing by whether it could change that
decision — not by how important the missing fact sounds in the abstract.

**Evidence gap ≠ decision gap.** A gap becomes decision-critical only when
resolving it could reasonably alter the current decision, its safety, its
proportionality, or the confidence with which it can be defended. Most
unknowns in a case are residual uncertainty, not decision gaps — treating
every unknown as decision-critical would be clinically timid and
operationally useless, and would turn this skill into defensive escalation
machinery. That failure mode is exactly what this skill exists to prevent,
not produce.

## Foundational rules (carried from Skills 01–08)

1. Unknown is not negative evidence.
2. Behaviour is not function.
3. This skill does not overwrite the conclusions of any upstream skill, does
   not gather the missing information itself, and does not decide what
   should happen as a result of a gap — it classifies the gap and hands that
   classification to whoever owns the decision.
4. Stable pattern is not the same as effective intervention — carried
   forward because "nothing looks wrong" and "this has been established as
   fine" are different claims, and this skill exists partly to keep that
   distinction visible at the evidentiary level.

## The central distinction: three kinds of "not established"

These are routinely collapsed in clinical reasoning and they require
completely different handling. Never write "not established" as a catch-all
without specifying which of these applies:

- **Missing evidence** — the question was never asked, the domain was never
  assessed, or the record simply doesn't address it. Nothing can be
  concluded either way.
- **Absent evidence** — the question was directly asked or assessed, and
  the answer was negative or not present ("asked, denied," "assessed, not
  found"). This is itself a finding, distinct from missing evidence, and
  should not be flattened into the same category.
- **Contradictory evidence** — different sources or different points in the
  record give inconsistent answers on the same question. This is not the
  same as either missing or absent — it is a specific finding (the record
  disagrees with itself) that has its own materiality question: does the
  contradiction itself change what can safely be concluded?

## When the person's own stated preference is the missing information

Apply an explicit threshold rather than defaulting either way. A person's
unestablished preference or view becomes decision-critical when the decision
under examination concerns acceptability, burden, adherence, or
configuration in a way the person's answer could independently change the
supportable conclusion — not merely because a decision touches something the
person is affected by. Where the decision is about acceptability, burden, or
which configuration to use, the person's own view is often exactly the fact
the counterfactual test turns on, and should be tested as such rather than
filed as residual uncertainty by default. Where the decision doesn't turn on
acceptability or configuration (e.g. a purely factual or immediate-safety
question), the person's unestablished preference stays residual uncertainty.
Run the counterfactual test on the preference itself, the same as any other
gap — don't give it a free pass to residual uncertainty just because
preferences feel softer than clinical facts, and don't make it automatically
decision-critical just because it's a preference.

## Do not bundle adjacent variables into one gap

State the decision under examination as a precise proposition, and classify
each candidate gap against exactly that proposition — not against a wider
question the adjacent, clinically related variable would answer. Two
variables can be clinically related (plan and intent; means and access;
housing and safety) while only one of them is actually what the stated
decision turns on. If the decision is "is it safe to conclude there is no
current plan," the decisive gap is plan status specifically — intent is a
genuinely important, closely related variable, but resolving intent does not
resolve whether a plan exists, and the reverse is also true. Bundling them
into a single "plan/intent" gap smuggles a wider, unstated decision in under
the cover of the narrower one that was actually asked. Where a clinically
adjacent variable isn't itself part of the stated decision, name it
separately — as its own gap against its own (likely wider or different)
decision, or as residual uncertainty for the decision actually in front of
you — rather than folding it into the gap that answers the question asked.

## The counterfactual test

This is the mechanism that does the actual work, and it is the test to apply
to every candidate gap:

**If this missing information were resolved in either plausible direction,
could it change the decision?**

- If no — the gap is **residual uncertainty**. Name it, don't dwell on it,
  don't let it block the decision that's actually supported.
- If yes — the gap is **decision-critical** (or safety-critical, see below).
  The decision under examination should not proceed as though the gap were
  resolved.

Materiality is contextual, not a fixed property of the missing fact. The
same missing fact can be residual uncertainty for one decision and
decision-critical for another — apply the counterfactual test fresh to the
decision actually in front of you, never to a general sense of "this seems
like important information."

**Materiality beats salience.** If plausible resolution in either direction
genuinely changes the decision, the absence of any existing signal pointing
toward the "bad" branch does not demote the gap to residual uncertainty.
"Nothing indicates this is a problem" is a statement about likelihood, not
about materiality — and using it to downgrade a gap that has already passed
the counterfactual test reintroduces unknown-as-negative-evidence through
the back door. Once you've established that both plausible answers move the
decision, the gap is decision-critical regardless of which answer seems more
likely. Do not require a "signal" of trouble before treating a materially
consequential gap as material.

**Fix decision granularity before testing gaps, and hold it fixed.** State
the decision under examination precisely, at the resolution it was actually
asked, and test every gap against that exact decision — not a narrower
version quietly substituted partway through the analysis because it makes a
gap easier to dismiss. If the decision is "should the current intervention
(fortnightly calls, as configured) continue," evidence bearing on whether a
different configuration (frequency, format) would serve better is material
to that decision, not a "follow-on question" set aside as out of scope. If
the decision you actually want to test is narrower (e.g. "some contact
versus none"), say that explicitly as the decision under examination — don't
silently narrow the framing to protect a preferred conclusion.

**No speculative gap generation.** Do not nominate something as an evidence
gap merely because additional information could conceivably exist — every
case has infinitely many conceivable unknowns, and treating all of them as
candidate gaps turns this skill into an evidence-gap generator rather than a
detector. Only nominate a gap where the missing information is: implied by
the decision under examination, ordinarily expected content for that kind of
decision, contradicted somewhere in the material, or explicitly and directly
relevant to a specific element the decision depends on. "This isn't
mentioned and more detail is generally available" is not, by itself, grounds
to list something as a gap.

## Gap classification — four states, not a binary

Use exactly these four labels. Don't introduce a fifth ("not applicable,"
"out of scope," or similar) for information that's genuinely unknown but
non-material to the decision at hand — that's what "no material gap" or
"residual uncertainty" already exist to cover. A variable that's unknown and
simply isn't material to this decision is residual uncertainty (or, if it
isn't material to anything the decision depends on at all, doesn't need
naming as a gap in the first place per the no-speculative-gap-generation
rule) — not a new category invented to describe it.

### 1. No material gap
Enough is established for the decision under examination. Say so plainly —
this is a legitimate and common outcome, not a failure to find something.

### 2. Residual uncertainty
Something relevant is unknown, but resolving it in either plausible
direction would not reasonably change the current decision. Name it for the
record. Do not let it block or qualify the decision beyond that.

### 3. Decision-critical gap
The missing evidence could change which decision is justified. The decision
under examination should not be completed as though this gap didn't exist —
it needs resolving, or the decision needs to be framed around not knowing.

### 4. Safety-critical gap
The uncertainty concerns information whose absence prevents safe reliance on
the specific decision under examination — right now, for that decision. This
is not "unknown risk = high risk" — it does not manufacture danger out of an
absence. It changes what can safely be concluded, not the underlying facts.
A safety-critical gap means: we cannot responsibly say this decision is safe
to proceed on, not: this is dangerous. Where established information
elsewhere already indicates immediate danger, that's an
immediate-safety-pathway matter, not a gap-classification exercise — this
skill classifies epistemic gaps, it does not substitute for acting on danger
that's already established.

**Safety-critical describes consequence, not topic.** A gap is not
safety-critical merely because its subject matter is clinically sensitive
(suicide history, means access, and so on). "Has this person previously
attempted suicide" being unresolved is decision-critical to the factual
question of whether the record establishes a prior attempt — it only becomes
safety-critical when that specific unresolved answer is being relied on for
a safety decision being made now (e.g. building or endorsing a current
safety plan on the assumption of no prior attempts). Test each candidate
safety-critical gap by asking: is unresolved uncertainty here actually
preventing safe reliance on the decision in front of us, or is this
important-sounding information whose absence hasn't yet been shown to block
this particular decision? If it's the latter, it's decision-critical, not
safety-critical — don't upgrade a gap's classification because its subject
matter sounds serious.

**Test each element of a decision separately when it depends on several
distinct pieces of information.** A safety plan's usability can depend on
several independent variables (literacy for written elements, phone access
for phone-based elements, housing stability for other elements). Each
element blocks reliance on the specific plan components that depend on it —
literacy being unknown blocks reliance on a written plan, not on every
possible plan format. Don't collapse "several implementation variables are
unknown" into "the whole decision is safety-critical" — name what each
specific gap actually blocks, and let the classification track that.

## Adjacency does not propagate criticality

Two gaps can be causally or clinically related while having different
materiality. Every gap must pass the counterfactual test against the
decision **independently** — do not let a gap inherit decision-critical (or
safety-critical) status merely because it's related to one that already has
that status. There are three distinct relationships a gap can have to a
decision-critical gap, and they are not interchangeable:

- **Independent gap.** A relevant unknown that does not bear on any
  decision-critical gap. Classify on its own counterfactual test.
- **Adjacent gap.** Related to a decision-critical issue, and potentially
  informative about it, but not necessary for resolving it — the
  decision-critical gap could be resolved without ever answering this one.
  Adjacent gaps stay at whatever classification their own counterfactual
  test produces; adjacency alone does not elevate them.
- **Dependency gap.** Information that is actually necessary to resolve a
  decision-critical gap — the decision-critical gap cannot reasonably be
  resolved without it. A dependency gap is **not independently classifiable
  at this stage, because its answer depends on resolving the decision-
  critical gap it feeds first** — do not describe this as the dependency
  "inheriting" the parent gap's status. Dependencies inherit sequencing and
  answerability, not materiality: once the parent gap is resolved, the
  dependency gap may turn out to be decision-critical, residual, or even
  moot in its own right, and that has to be assessed fresh at that point,
  not assumed from the parent's classification. Keep materiality and
  dependency separate in the output: **materiality** asks whether resolving
  this gap changes the decision; **dependency** asks whether resolving this
  gap is required to resolve a different, materially critical gap. Say so
  as a dependency ("not independently classifiable — depends on resolving
  [gap X] first"), not by mislabelling it with that gap's classification.

**Explanatory provenance is not a dependency.** If the operative fact behind
a decision-critical gap can be established directly, do not elevate the
question of *why* the record became unclear or inconsistent into a
dependency of that gap. Example: if two sources disagree about a caller's
current living situation, direct confirmation of the current fact resolves
the operative uncertainty; the separate question of why Monday's and
Thursday's notes disagree (recording error, a genuine change, ambiguous
phrasing) does not need to be answered for the current decision to proceed,
even though it might matter for record quality. If one enquiry resolves the
decision-critical gap "as a byproduct," that's a sign the byproduct question
was never actually a dependency — don't elevate it after the fact.

## Boundary rules

- **Do not fill your own gaps.** The moment this skill's output contains
  "probably," "likely," "given the pattern we can assume," or any
  reasoning that infers an unestablished fact from a plausible pattern, it
  has defeated its purpose. State what's established, what isn't, why the
  distinction matters to the decision, and what remains supportable — never
  bridge the gap with a plausible guess, however reasonable it sounds.
- **Do not gather the missing information.** This skill identifies what's
  missing and whether it matters; it does not go and get it, and does not
  instruct that a named list of upstream skills be run. Name the type of
  information needed and hand the classification to whoever owns the
  decision.
- **Do not decide what should happen as a result of a gap.** Whether a
  decision-critical gap means "wait," "escalate," "seek information first,"
  or something else is the owning skill's call (e.g. Intervention
  Selection's destination 6), not this skill's. This skill's output is an
  input to that decision, not the decision itself.
- **Do not convert "unknown" into "unlikely," "low risk," or "probably
  fine."** That is the same failure mode as converting it into "high risk"
  — both manufacture a conclusion the absence doesn't support.
  Absent-and-negative (asked, denied) and missing-and-unknown (never asked)
  must never be collapsed into the same reassuring reading.
- **Do not treat volume of documentation as evidence of completeness.**
  Extensive material can still avoid the one fact a decision depends on.
  Thoroughness on adjacent questions is not evidence the decisive question
  was addressed.
- **Do not treat a request to "get more information" as self-justifying.**
  If the material already establishes what the decision needs, say so, even
  under pressure to keep gathering. Continuing to gather information past
  the point of decision-sufficiency is its own failure mode, not diligence.
- **Do not let a gap classification drift into a clinical judgement.**
  "Decision-critical" describes the evidentiary relationship between the
  gap and the decision — it is not a statement about risk level, and this
  skill does not produce one.
- **Do not design the downstream decision's content.** This skill says that
  different answers to a gap would materially alter the assumptions
  available to whichever decision or plan depends on them — it does not
  specify what the resulting plan, intervention, or decision should contain.
  If an output starts describing what a safety plan "would need to
  address," who should be involved, or what a resulting arrangement should
  look like, that content has crossed into the owning skill's territory and
  must be cut back to naming the materiality only.
- **Keep dependency descriptions abstract, not illustrative of downstream
  content.** When naming what a gap blocks reliance on, use abstract
  category language — "phone-dependent components," "written components,"
  "location-dependent components" — not concrete examples of what those
  components might be ("calling a crisis line," "written coping steps,"
  "means-restriction steps"). Concrete examples start to sketch the
  downstream plan's actual content even when framed as illustrative, and
  the closer this skill sits to a downstream skill's territory (Safety
  Planning especially), the more that habit erodes the boundary above. Say
  what kind of information a component depends on, never what the
  component should be.
- **State only the assumption that changes, not what the downstream process
  should do about it.** The output's job stops at: resolving this gap in
  either direction changes what [the downstream decision] can safely assume
  or rely on. Do not go further and say whether a component should proceed,
  be omitted, be reframed, or be retained once the gap is resolved — even
  as a hedge or a possibility ("could reasonably proceed without X," "might
  not need to include Y"). That is the owning skill's determination to make
  once it has the resolved fact, not a conclusion this skill reaches on its
  behalf. If a sentence describes what the downstream process could or
  should do rather than what it can or can't currently assume, cut it back
  to the assumption alone.

## Inputs

The decision or question actually under examination (stated explicitly, not
inferred), the material presented in support of it, and — where relevant —
what decision the requester is trying to reach. This skill does not go
looking for additional material beyond what's presented; it audits what's
there against what the stated decision requires.

## Output format

```
EVIDENCE-GAP ANALYSIS

Decision under examination
[The actual decision/question the evidence must support — stated
explicitly, not assumed]

Established evidence
[What is genuinely established, and how — direct assessment, disclosure,
documented finding]

Evidence gaps
[What relevant information is not established — for each, specify: missing
(never asked/assessed), absent (asked/assessed, negative), or contradictory
(sources disagree)]

Gap classification
[For each gap: No material gap / Residual uncertainty / Decision-critical
gap / Safety-critical gap. Where a gap is a dependency of another
decision-critical or safety-critical gap rather than independently
material, say so explicitly ("dependency of [gap X]") rather than
mislabelling it with that gap's classification]

Materiality analysis
[For each gap classified as more than "no material gap": apply the
counterfactual test explicitly, at the decision's actual stated
granularity — if resolved in either plausible direction, would the decision
change? Show the reasoning, not just the conclusion. Do not demote a gap
that passes this test merely because no signal currently points toward the
consequential branch — materiality, not likelihood, governs the
classification. For dependency gaps, state what they're necessary to
resolve rather than re-running the counterfactual test against the original
decision]

What remains supportable
[The conclusions/actions still justified despite the gaps]

What is not supportable
[Conclusions the available evidence cannot justify, given the gaps found]

Information requirement
[What needs establishing, if anything — named by type of information
needed, not by instructing which upstream skill to run]

Residual uncertainty
[What can legitimately remain unresolved without blocking the decision]
```

## Reasoning shortcuts to avoid

- Treating every unknown as decision-critical by default — this produces
  permanent destination-6 behaviour across the stack and is exactly the
  defensive-escalation failure mode this skill exists to prevent.
- Collapsing "never asked" and "asked, denied" into the same "not
  established" language — they are different findings with different
  implications.
- Treating a contradiction in the record as automatically decision-critical
  without running the counterfactual test on the contradiction itself —
  some contradictions don't matter to the decision at hand.
- Inferring an unestablished fact from a nearby established one ("the
  pattern suggests," "given how the rest of the case reads") instead of
  naming it as unestablished.
- Converting a safety-critical gap into a risk assertion ("this is
  dangerous") rather than an epistemic limit ("this cannot be concluded
  safe from what's here").
- Being reassured by the sheer volume or apparent thoroughness of the
  material instead of checking whether the specific decisive question was
  actually addressed anywhere in it.
- Continuing to flag gaps or request more information once the material
  genuinely already supports the decision under examination.
- Naming the classification without running the counterfactual test
  explicitly — "this seems important" is not materiality analysis.
- Deciding what should happen next (escalate, wait, proceed) rather than
  classifying the gap and handing that off to the owning skill.

## Boundary

This skill performs an epistemic audit of the material available for a
specific decision. It does not conduct enquiry, formulate risk, analyse
contact pattern, decide triage destination, review access arrangements,
build safety plans, or select interventions — those are Skills 01, 02, 03,
04, 05, 07, and 08, and this skill does not redo or substitute for their
work. It does not gather missing information itself. It does not decide
what should happen as a result of a gap it identifies — that belongs to
whichever skill owns the decision under examination (e.g. Intervention
Selection's destination 6, CRG Triage's insufficient-information state).
It does not override the immediate risk pathway — where danger is already
established, that is acted on directly, not routed through a gap
classification. Where organisational policy specifies mandatory information
requirements, policy takes precedence over this skill.
