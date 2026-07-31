# Commission — when-ai-breaks / gemini-image-generation

Date: 2026-07-31 (UTC) · Mode: open · Template: lesson · Section: Working Knowledge

## The incident

In February 2024, Google's Gemini assistant (the rebranded Bard) added image
generation of people, powered by its Imagen 2 model. Within days users showed it
producing historically false images: racially and ethnically diverse "1943 German
soldiers," diverse US Founding Fathers, a female pope, and refusals to depict white
people on request. On 22 February 2024 Google paused Gemini's generation of images
of people. On 23 February, Prabhakar Raghavan (a Google Senior Vice President)
published an explanation: the tuning meant to show a *range* of people failed to
account for cases that should not show a range, and the model also became
over-cautious, wrongly refusing some prompts. CEO Sundar Pichai sent staff a memo
(reported ~27 February) calling the outputs "completely unacceptable." Image
generation of people was restored months later with changes.

## The angle (follow the desk's order)

1. **What happened, in order, with names and dates.** What Gemini image generation
   was built to do, what it actually produced, who reacted, and what Google did
   (pause 22 Feb; Raghavan's post 23 Feb; Pichai memo). Keep it to the record.
2. **Why that kind of system fails that way — the mechanism, from the record.**
   Image models trained on web-scale data reproduce the demographic skews of that
   data (ask for "a CEO" and you tend to get the same demographic). A common
   mitigation is to nudge for diversity in post-training and, crucially, to rewrite
   or append to the user's prompt behind the scenes — an invisible instruction the
   model then obeys. Gemini applied that diversity nudge as an always-on rule with no
   sense of when a prompt has a correct, non-diverse answer (a 1943 Wehrmacht
   soldier), so it overwrote history. Tie the "model obeys an appended instruction
   it never showed the user" step to the mechanism the course teaches in
   `the-mechanics/instructions-are-data` (if that lesson is already published, link
   it in Background; if not yet merged, teach the one needed sentence and link
   `the-evidence/instructgpt` instead). This over-correction is a post-training /
   guardrail choice, so connect it to RLHF/instruction tuning already taught.
3. **Where the same weakness lives today.** The bias-mitigation tradeoff is
   permanent and universal: every deployed model sits somewhere between reproducing
   its data's skew and over-correcting away from faithfulness, and many use hidden
   prompt-rewriting or system instructions the user never sees. Name concrete places
   the same tension recurs, from the record, without hype.

## Required contribution (the article's own work)

Trace the failure to its actual mechanism — an invisible, context-blind
prompt-augmentation/diversity rule that the model obeyed as an instruction — using
Google's own account, rather than the "the AI is woke/biased" framing the incident
was mostly discussed in. The reader should leave understanding that the same
engineering choice (counter data bias with a hidden nudge) produces both the useful
default and this failure, and able to spot the tradeoff elsewhere.

## Source obligations

From `nb source-policy --series when-ai-breaks`: **min 8 sources; primary ≥ 4,
secondary ≥ 1.** The desk mandates working **from the record**.

- **Primary:** Google's own statements — Prabhakar Raghavan's 23 Feb 2024 blog post
  ("Gemini image generation got it wrong. We'll do better."); Google's original
  pause statement (Gemini/Google X posts); the Pichai memo text as quoted by outlets
  that published it verbatim (e.g. Semafor/The Verge — treat the *quoted memo* as
  primary, the outlet's framing as secondary); Gemini/Imagen 2 product/technical
  documentation for what the system was. The generated images themselves are primary
  artifacts — cite reputable captures.
- **Secondary (context):** careful reporting from The Verge, NYT, Wired, BBC, AP,
  Ars Technica establishing the timeline and reactions. Accusations/impact claims
  need two independent confirmations.
- **Contradiction hunting:** was every viral example genuine and unedited? Establish
  which specific outputs Google itself acknowledged vs. cherry-picked screenshots.
  Present the strongest version of Google's defense (a real, hard bias problem it was
  trying to solve) and the strongest critique (it shipped a context-blind rule).
- Verify: exact dates; Raghavan's exact title; the exact wording of the "completely
  unacceptable" quote and its attribution; that the mechanism was prompt-augmentation
  /tuning as Google described, and mark clearly anything that is reconstruction vs.
  Google's stated account.

## Prior coverage in this library (link, do not re-teach)

- `the-evidence/instructgpt` (2026-07-22): RLHF / instruction tuning — the family of
  post-training this failure comes from. Background link.
- `when-ai-breaks/compas-recidivism` (2026-07-25) and other bias pieces: prior
  fairness cases. This one is distinct: not disparate impact on individuals but an
  over-correction that falsified content. Keep the mechanism (hidden prompt nudge)
  front and center so it does not read as "another bias story."
- Link `the-mechanics/instructions-are-data` (tonight) in Background **only if it is
  already merged to library** at prepare-pr time; otherwise omit the internal link.

## Structures NOT to repeat (recent habits)

The desk's recent pieces open on a sharp factual jolt (a dragged pedestrian, a
30-hour jail cell). This incident has no physical victim; do not manufacture false
gravity. Report the absurd-but-consequential failure plainly. No colon-subtitle
headline; no "not X but Y" thesis; vary heading cadence from the recent library.
Avoid the culture-war vocabulary the event was litigated in; teach the engineering.

## Neighboring articles tonight (make this distinct)

Cross-linked with `the-mechanics/instructions-are-data`, which owns the general
mechanism (a model obeying appended text). This piece owns the *incident* and the
*bias-mitigation tradeoff*; do not re-teach the general mechanism at length — spend
your words on what Google did, why, and the tradeoff.

## Output paths

- Article: `.nb-work/when-ai-breaks/gemini-image-generation/library/when-ai-breaks/gemini-image-generation.html`
- Role artifacts under `agent-artifacts/when-ai-breaks/gemini-image-generation/{writing-coach,researcher,writer,editor}/NN/`

## Harness / model

harness `claude-code-routine`; writer `claude-sonnet-5` effort medium; researcher &
editor `claude-sonnet-5` effort high; coach `claude-sonnet-5` effort low.

## Bans to watch

em-dash ≤ 4; `leverage` ≤ 1; `load-bearing` 0; `machinery` 0;
`revolutionary`/`transformative`/`game-changing` 0; "AI race" 0. Handle the
demographic/culture-war framing soberly and factually; the teaching is the
engineering tradeoff, not the politics.
