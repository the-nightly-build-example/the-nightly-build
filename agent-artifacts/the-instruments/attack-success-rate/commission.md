# Commission: the-instruments/attack-success-rate

## Assignment

The Instruments teaches how one number used to compare AI systems is made.
Tonight's number is the attack success rate (ASR): the percentage a safety
benchmark reports for how often a model can be made to produce content it was
trained to refuse. It is the number behind claims that one model is "safer" or
"more jailbreak-resistant" than another. Explain, step by step, where the number
comes from: who produces it, from what set of prompts, run through what attack,
and judged by whom or what. Then show what it can and cannot support, including
at least one real case where it misled people and what that cost.

The reader should leave able to say what one ASR measurement actually counts,
why two labs can report very different ASRs for the same model, why a model that
refuses everything can score a perfect safety number, and why an ASR from six
months ago tells you little about today's attacks.

## How the number is made, precisely

Recover the pipeline from the benchmarks that own it: a fixed set of harmful
requests, an attack method applied to each (a template, an optimizer-found
suffix, or a rephrasing), the model's response, and a judge (a classifier, an
LLM grader, or a human) deciding whether the response counts as a successful
"comply." The researcher must get the concrete design of at least two current
safety benchmarks (for example HarmBench and StrongREJECT), including how each
defines success, how its judge was validated, and how much its ASR depends on
that judge. Get the real numbers and how far they move with the attack and the
grader.

## What the article must add to the evidence

The lesson's second half is where the number misleads. Draw out, from the
sources: that ASR is only as good as its judge, and grader disagreement swings
the number; that a model can lower its ASR simply by refusing more, which trades
against a separate over-refusal cost the number does not show; and that a static
benchmark measures resistance to yesterday's attacks, so a low ASR is a claim
with an expiration date. The real "case where it misled" should be concrete: a
safety score cited for a model that a new, cheap attack then defeated, or a
benchmark whose own authors showed its ASR was an artifact of its judge. Keep the
distinction between what the number measures and what a safety claim needs.

## Boundaries

- The subject is the number, not the argument about whether models can be
  jailbroken. That argument is its own published lesson in another desk
  (jailbreaks); link it for the mechanism if the reader needs it, do not re-argue
  it. Over-refusal is a published mechanics lesson; link, do not re-teach.
- Define "jailbreak," "refusal," and "attack success rate" in plain words at
  first use. Name the benchmarks and judges by what their papers call them.
- Name no company as an authority on which model is safest; report what each
  benchmark and each lab reported and let the evidence weigh it.

## Sources to start from

Primary: the papers that own the benchmarks (for example HarmBench, Mazeika et
al. 2024; StrongREJECT, Souly et al. 2024) for design and judge validation; a
transferable-attack paper (for example GCG, Zou et al. 2023) for how an attack
drives the number; and a source documenting a specific safety score defeated by a
later attack, or a benchmark's own judge-sensitivity analysis. At least one
secondary source for how ASR is cited in public. Series policy requires at least
eight sources, at least four primary. Verify every reported rate against the
benchmark that owns it and record which attack and which judge produced it; an
ASR with no attack and no judge attached is not a figure.

## This edition's neighbors

Four other lessons tonight: the-evidence/deep-double-descent,
the-mechanics/irrelevant-context, what-could-go-wrong/liars-dividend,
when-ai-breaks/houston-teacher-evaluation. No overlap; write for a reader who has
not read them.

## Recent coverage in this series, and habits not to inherit

The last five Instruments lessons were task-time-horizon, superglue, imo-gold,
toxicity-score, simpleqa. Break, do not reproduce:
- The banned comma-triad dek (three clauses joined by commas and closed with
  "and"); several recent deks lean on it. Write one lean sentence.
- The outline arc orientation → "how the single number is built" → "the
  measurement row is itself a measurement" → misled-case. This piece needs a
  how-built section and a misled case; name and build them in this piece's own
  terms and do not mirror recent heading shapes ("How eight tests become one
  number", "The line X crossed had already been crossed").
- A house catchphrase forming across recent pieces.

Furniture rotates through the stat strip, the table, the note, and the position
card. A judge-sensitivity or attack-versus-ASR comparison may want a table; use
only what the argument spends.

## Production record

Production policy (the-instruments): profile balanced; every stage required:
false; model "capable"; effort high for researcher and editor, medium for
writer, low for writing-coach. Harness: claude-code-routine. Model resolved to
claude-opus-4-8 for every role. No required directive traded down. Writer records
model claude-opus-4-8, harness claude-code-routine, date 2026-09-04.

## Tags

Suggested: attack-success-rate, jailbreak-benchmarks, safety-evaluation,
red-teaming. The writer may adjust.
