---
name: clinical-workflow-router
description: >
  Decides which clinical reasoning skill (or sequence of skills) a Lifeline/
  crisis-helpline query actually needs — Suicide Enquiry, PORF Formulation,
  Contact Pattern Analysis, CRG Triage, or CMP/Access Review — and in what
  order. Use this skill whenever the user presents a case, question, or piece
  of material from this domain and it isn't already obvious which single
  skill applies, when the case plausibly needs more than one skill in
  sequence (e.g. high contact volume, an existing CMP, and a suicide
  disclosure all in the same case), or when the user asks "what do I do with
  this" / "where does this go" without specifying which kind of analysis they
  want. Also trigger to sanity-check that a request isn't asking one skill to
  quietly do another skill's job (e.g. asking Suicide Enquiry to also assign
  a risk level). Do not use this skill when the user has already clearly
  named which single skill/analysis they want — route directly instead of
  routing the routing.
---

# Clinical Workflow Router

## Purpose

This skill does not do clinical reasoning. It decides **which reasoning
operation the material actually requires**, in what order, and flags when
none of the five skills apply, or when a request is asking one skill to
overstep into another's job.

The five skills this router dispatches to, and the distinct question each
one answers:

- **Suicide Enquiry** — What has actually been established about
  suicidality?
- **PORF Formulation** — What does this information mean for this person
  now?
- **Contact Pattern Analysis** — What is happening across contact over time?
- **CRG Triage** — What decision is unresolved, and where does it belong?
- **CMP/Access Review** — Is the way access is currently structured actually
  working?

Each of those skills already enforces its own boundary against doing another
skill's job. This router's job is upstream of that: get the material to the
right skill(s), in the right order, without letting one stage's output get
mistaken for a different stage's conclusion.

## The one override that comes before any routing decision

**Acute safety unfolding right now bypasses routing entirely.** If the
material describes an immediate safety concern — active means in hand, an
attempt in progress, anything requiring action in the next few minutes — say
so first, plainly, and state that organisational immediate-risk/emergency
procedures take precedence and apply now, ahead of and independent of any
skill routing. Don't let "which skill handles this" become the first
question when the honest first answer is "nobody's waiting on a skill
selection right now."

Stay at that level — naming that the override applies and pointing to
existing emergency procedure. This skill should not start prescribing the
specific medical or operational actions to take (what to say, whether to
keep someone talking, how to obtain a location); that's exactly the kind of
role a routing skill shouldn't drift into, and it's covered by
organisational procedure and clinical judgement in the moment, not by this
skill's output.

## Single-skill routing

Most cases need exactly one skill. Match the actual question being asked,
not the surface topic:

- Material or a question centred on **what's known about suicidal
  thoughts/plans/history** → Suicide Enquiry.
- A request to **understand what a presentation means and what response is
  proportionate**, when suicidality/formulation material is already
  available → PORF Formulation.
- A change in **how someone is contacting** (frequency, clustering,
  disconnection, engagement) and what that means → Contact Pattern
  Analysis.
- A question about **whether a case needs to escalate and to where** →
  CRG Triage.
- A question about **whether an existing or proposed access
  arrangement/CMP is justified** → CMP/Access Review.

If the surface framing doesn't match the underlying question — e.g. someone
asks "is this person high risk?" but hands over a raw call transcript with no
direct suicide enquiry recorded — route to the skill the material actually
needs first (here, Suicide Enquiry, to check what has and hasn't been
directly established), and say explicitly that the question as asked can't
be answered until that groundwork exists.

Be precise about what Suicide Enquiry does with material like this, because
it's easy to get subtly wrong in exactly the way Suicide Enquiry itself was
built to prevent: if suicide was never directly asked about, the correct
Suicide Enquiry result is that suicidality is **not established** and direct
enquiry did not occur — full stop. Suicide Enquiry does not scan a transcript
for hopelessness, warning signs, functional decline, or goodbye-type language
and convert that into a suicidality finding by inference; that's exactly the
behaviour-to-function-style leap Suicide Enquiry was built to refuse. Those
other observations may well be clinically important, but they're PORF's
material to weigh directly from the source, not Suicide Enquiry's to launder
into a suicide-enquiry conclusion.

Also don't let "high risk" survive the reframe as PORF's product. PORF
answers what the presentation means for this person and what response is
proportionate — not a categorical risk label — unless the version of PORF in
use explicitly produces categorical levels. Reframe the manager's question
into those terms rather than promising PORF will answer "is this caller high
risk" as asked.

And don't overcorrect into concluding PORF "cannot yet be meaningfully run"
just because direct suicide enquiry is absent. PORF is broader than
suicidality — a transcript with hopelessness, deterioration, agitation, loss,
altered behaviour, or reduced resources can contain genuinely
formulation-relevant material even with no suicide enquiry recorded. The
correct constraint is narrower and more precise: **PORF must not treat the
absence of suicide enquiry as evidence that suicidality is absent.** PORF can
and should run on whatever formulation-relevant material exists, while
explicitly carrying forward "suicidality not established" as an unresolved
gap rather than a negative finding — not be blocked from running at all.

## Multi-stage sequencing

Some cases genuinely need more than one skill, in a specific order, because
each skill's output is the next one's input. Don't collapse a multi-stage
case into a single skill just because one skill's topic sounds closest to
the surface complaint. Two patterns to recognise by name, since they recur:

**The high-contact pattern (OCD pattern)** (the "Nicola" pattern): a case
presenting as "this person's contact has changed dramatically" should not
jump straight to CMP/Access Review. But it also shouldn't be forced through
every other skill regardless of what's actually needed — treat this as a
starting point plus a branch, not a fixed four-step pipeline:

1. **Contact Pattern Analysis always comes first** for this pattern —
   establish what's actually changed and what's known/unknown about
   function. Nothing downstream can be decided honestly without this.
2. **Branch from what stage 1 actually establishes:**
   - If the pattern analysis provides enough established context/function to
     answer the access question directly, go straight to **CMP/Access
     Review** — don't insert PORF just because the case involves suicide-
     adjacent territory in general terms.
   - If the clinical meaning of the change is genuinely unresolved (not just
     "a formulation would be nice to have," but something CMP/Access Review
     actually needs and doesn't have), run **PORF Formulation** before
     CMP/Access Review.
   - If suicide-specific information needs establishing before PORF can do
     that work, **Suicide Enquiry** precedes PORF.
3. **CRG Triage** remains conditional throughout — only if, after whichever
   of the above stages actually ran, a shared formulation or decision
   genuinely remains unresolved. Apply CRG Triage's own forcing question
   ("what decision cannot be made at the current level of care") to whatever
   is left unresolved, rather than assuming high volume — or having run
   several stages — earns a CRG referral by itself.

Do not infer that a formulation is missing (or present) from indirect facts
like "there's no existing CMP" or "there's no case file flagged." Absence of
a CMP tells you nothing about whether a formulation exists — that's the same
unknown-as-negative-evidence error this whole skill family exists to avoid,
just relocated into the routing layer. If it's not established either way,
say so and let Contact Pattern Analysis's output (not an inference from
adjacent facts) determine whether PORF is actually needed.

**The suicide-disclosure pattern**: a case presenting with suicidal content
should not let Suicide Enquiry's output get read as if it were already a
risk judgement or a response recommendation. The sequence is:

1. **Suicide Enquiry** — establish what's known, organised by CASE
   chronology.
2. **PORF Formulation** — use that material to determine what it means and
   what response is proportionate.

Stopping after step 1 and treating its output as the answer is exactly the
failure this router exists to prevent — Suicide Enquiry was deliberately
built not to answer "so what does this mean," and a routing layer that
quietly treats its output as sufficient reintroduces the problem all five
skills were built to remove.

Two adjacent inference errors are easy to make when routing and worth naming
directly:

- **An existing CMP does not establish that a formulation exists.**
  CMP/Access Review was deliberately built to detect poorly-formulated
  plans — don't assume the presence of a CMP means the groundwork is already
  there. If nothing in the material indicates whether a formulation exists,
  say "no formulation question is identified in the material provided"
  rather than asserting one way or the other.
- **"Suicide was asked about" does not automatically establish that CASE
  enquiry is complete** — but don't overcorrect this into auditing every
  upstream skill's completeness by default. The distinction that actually
  matters: **"not mentioned in the routing request" is not the same claim as
  "not done clinically."** If the material presented says enquiry was
  completed and documented ("the counsellor completed suicide enquiry and
  documented it — what do I do with this?"), accept that as the upstream
  product and route to PORF, unless the material itself gives a concrete
  reason to doubt it (e.g. it directly says certain domains weren't covered,
  or the answers given are visibly partial/contradictory). Don't infer a gap
  merely because the routing request's summary didn't individually re-list
  every CASE component — a summary omitting detail is not the same as the
  underlying enquiry having omitted it. Route to (or back to) Suicide Enquiry
  specifically when completeness is the actual open question being asked, or
  when the material itself shows a concrete gap — not as a default check run
  on every handoff. Otherwise the router becomes recursive: every downstream
  skill re-triggering an audit of the upstream skill because the prompt
  didn't reproduce its full working, which is exactly the process inflation
  this skill exists to prevent.

These two patterns are illustrations, not an exhaustive list — the same
logic (each skill's actual output feeds the next skill's actual input;
don't skip a stage because the last one felt conclusive) applies to any
combination the material calls for. Name the stages and their order
explicitly in the output; don't just declare a destination skill and leave
the reasoning implicit.

## What this skill must never do

- Perform the clinical reasoning itself. If you notice yourself drafting
  formulation content, pattern-analysis content, or a triage decision while
  "routing," stop — that content belongs in the destination skill's output,
  not this one's.
- Assume a sequence must include every skill. A case might genuinely need
  only PORF, or only CMP/Access Review, if the necessary groundwork already
  exists. Padding a routing decision with extra stages "to be thorough"
  is its own kind of manufactured process.
- Skip a stage because a later one feels more clinically satisfying to
  reach — e.g. jumping straight to CRG because the case is complex, when
  Contact Pattern Analysis or PORF haven't actually been done yet. The
  destination skills already have their own "don't manufacture escalation"
  discipline; the router shouldn't manufacture a shortcut to them either.
- Assign a risk level, a CASE finding, an access decision, or a triage
  destination itself, even provisionally, "to save a step." That output
  belongs to whichever skill actually does that reasoning.

## Output format

```
CLINICAL WORKFLOW ROUTING

Immediate safety check
[State explicitly whether the material describes an acute safety concern
requiring action now, independent of any routing decision. If yes, say so
first and note that routing resumes only once the immediate situation is
being handled.]

What's actually being asked
[The underlying question(s), which may differ from how the request was
framed]

Routing decision
[Single skill, or an explicit ordered sequence, naming each skill and why
it's needed at that stage]

What each stage needs from the previous one
[Only if more than one skill is involved — state what output stage N produces
that stage N+1 requires as input]

Not routed to
[Any skill that might seem relevant on the surface but isn't actually needed,
and why — this keeps the routing decision honest rather than defaulting to
"run everything"]
```

## Reasoning shortcuts to avoid

- Routing by surface topic ("this mentions suicide, so Suicide Enquiry") when
  the actual question is a formulation or triage question.
- Treating Suicide Enquiry or Contact Pattern Analysis output as if it
  already answers "what should happen" — both are enquiry/analysis skills,
  not decision skills, and this router exists partly to stop their outputs
  being mistaken for conclusions.
- Jumping straight to CMP/Access Review or CRG Triage on high contact volume
  alone, skipping Contact Pattern Analysis (and PORF where relevant) as the
  necessary groundwork.
- Running every skill "to be safe" regardless of whether the material
  actually calls for each one — that's not thoroughness, it's avoiding the
  actual judgement this skill exists to make.
- Deciding a sequence is needed and then doing the reasoning for each stage
  inline instead of naming the stage and its required input.
- Describing Suicide Enquiry as scanning indirect material (hopelessness,
  functional decline, goodbye language) for suicidality when suicide was
  never directly asked about — that's Suicide Enquiry inferring what it was
  built to refuse to infer.
- Describing PORF as answering a categorical "is this person high risk"
  question rather than what the presentation means and what response is
  proportionate.
- Inferring that a formulation exists (or doesn't) from an adjacent fact like
  the presence or absence of a CMP.
- Treating "suicide was asked about" as equivalent to "CASE material is
  sufficient for PORF" — occurrence and sufficiency are different claims.
- Hardcoding a fixed multi-stage pipeline (e.g. always CPA → PORF → CMP)
  instead of branching from what each stage actually establishes.
- Prescribing specific emergency/medical actions in the immediate-safety
  override instead of naming that organisational procedure takes precedence.
- Treating a routing request's summary as the complete record of what
  clinical work was done — "not mentioned here" is not "not done." Only
  route back to an upstream skill when completeness is the actual question
  or the material gives concrete reason to doubt it, not as a default
  re-check triggered by every handoff.
- Concluding a downstream skill "cannot yet be meaningfully run" because one
  specific input (e.g. direct suicide enquiry) is missing, when the skill has
  other genuinely relevant material to work with — name the specific
  constraint (don't treat the gap as a negative finding) rather than
  blocking the skill from running at all.
- "Running every skill to be thorough" remains one of the most important
  failure modes to keep testing against — a case with nothing risk-relevant,
  no pattern change, and no access question should route to none of the
  five skills, explicitly and by name, not default to comprehensive coverage.

## Boundary

This skill decides which clinical reasoning skill(s) apply and in what
order. It does not perform enquiry, formulation, pattern analysis, triage,
or access review itself — those are the five destination skills. It does not
override the immediate safety pathway; it states that override up front and
gets out of the way. Where organisational policy specifies a mandatory
workflow or escalation sequence, policy takes precedence over this skill.
