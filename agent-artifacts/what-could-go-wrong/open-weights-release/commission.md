# Commission: what-could-go-wrong/open-weights-release

## The argument

Releasing a capable model's weights openly is an irreversible proliferation risk:
once the weights are public, anyone can strip the safety fine-tuning off them, the
release cannot be recalled, and whatever misuse the model enables (bio or cyber
uplift, targeted abuse material, mass fraud) is then permanently available. The
lesson teaches this argument on its merits — first at full strength, then tested
against what open models have actually been shown to do.

## What the lesson must do

Follow the desk's shape exactly.

- Open at full strength. Name who made the argument in its careful form (e.g.
  Seger et al., "Open-Sourcing Highly Capable Foundation Models," GovAI 2023) and
  what they had seen: that safety guardrails on open weights are cheaply removable,
  and that a release is a one-way door. Lay out the reasoning its best defender
  would give — irreversibility, the low cost of removing refusal training, and the
  offense-favoring asymmetry for some misuse types. The reader should believe
  serious people hold this before reading a word against it.
- Draw the sharp line. Separate what has been demonstrated in a working system
  from what is still analogy about systems that do not exist yet. Demonstrated:
  fine-tuning removes safety alignment cheaply (Qi et al. 2023); jailbreaks and
  uncensored derivatives exist. Not demonstrated / contested: that open models
  give a meaningful real-world uplift for catastrophic bio or cyber harm — the
  RAND red-team study (Mouton et al. 2024) found no statistically significant
  operational uplift from LLM access, and open weights trail the frontier.
- Bring it to the present. Who argues it now and what they want done (pre-release
  evaluations, staged or gated release, licensing, KYC), and the strongest reply:
  the marginal-risk framing (Kapoor, Narayanan et al., "On the Societal Impact of
  Open Foundation Models," 2024), which asks what open weights add over already-
  available tools, plus the defensive and research value of openness. Name where
  confidence outruns proof on both sides: the doom that assumes uplift not yet
  shown, and the dismissal that treats today's null results as permanent.

## Required contribution

The reader leaves able to evaluate an "open weights are dangerous" or "open
weights are fine" claim by asking the marginal-risk and irreversibility questions
this lesson teaches, and able to tell a demonstrated harm from a projected one.
The article's work is holding both the irreversibility argument and the marginal-
risk rebuttal at full strength and locating exactly where the evidence runs out.

## Boundaries and continuity

- Neighboring taught arguments: what-could-go-wrong/bioweapon-uplift,
  what-could-go-wrong/cyber-uplift, what-could-go-wrong/data-poisoning,
  what-could-go-wrong/model-collapse. This lesson is about the release decision
  and its irreversibility, not a re-run of the uplift lessons — cite the uplift
  evidence for the demonstrated/speculative line, link the taught pieces in
  Background, and keep the subject on open release.
- Work from the original documents (the reports and the safety-removal test),
  never commentary about them. Name no company as an authority; discuss Meta's
  open-weight releases and any lab's position as events and documents, reported as
  fact, and leave the reader to decide how worried to be.

## This run's neighbors

Four other lessons publish tonight on other desks (constitutional-ai, superglue,
counting-objects-in-images, bard-jwst-demo). No overlap.

## Source policy

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Candidate
primaries: Seger et al. 2023 (GovAI open-sourcing report); Kapoor & Narayanan et
al. 2024 (2403.07918); Qi et al. 2023, "Fine-tuning aligned language models
compromises safety" (2310.03693); Mouton et al. 2024 (RAND, LLMs and biological
weapon attack planning); a primary Meta Llama release document / license. Secondary:
policy reporting. The researcher confirms kind and count and steelmans both sides
with sources that change the interpretation.

## Production policy (recorded)

profile balanced. writing-coach low, researcher high, writer medium, editor high.
Model "capable" for every role, none required; roles run on this harness's
default capable model. Record actual models in handoffs.

## Recent patterns to break (habits, not rules)

- Deks recur as a two-clause ", and"-twist or a comma triad (banned by
  spec/headlines.md). This desk's recent deks name an author and what their
  argument survives (gradient-hacking, ai-boxing). Don't copy the "the worry X
  named survives Y" shape.
- Headlines default to a negative-fact reveal or a trailing second clause. The
  desk likes a sharp factual reveal ("Every AI escape on record was staged by the
  people running the test"); reach for this lesson's own reveal, not that mold.
- The present-day closing section keeps getting a "Where X still Y" heading; vary
  it.
