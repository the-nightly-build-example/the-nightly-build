# editor review-brief: the-mechanics/getting-math-wrong (01)

Inputs:
- Editorial direction: ../../editorial-direction.md
- Commission: ../../commission.md
- Writer brief: ../../writer/01/brief.md
- Voice guide: ../../writing-coach/01/voice-guide.md
- Evidence record: ../../researcher/01/evidence.md
- Draft handoff: ../../writer/01/draft-handoff.md
- The article: ../../../../library/the-mechanics/getting-math-wrong.html
- Template context: ../../../../.nb-context/

Output: ./editorial-review.md (editor/01/editorial-review.md)

Proof (for your verification if needed; the writer owns running it): from repo root —
`./nb check .nb-work/the-mechanics/getting-math-wrong/library/the-mechanics/getting-math-wrong.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/b1bf3c94-3553-5519-8a12-b9ebb7eba930/scratchpad/library-checkout`

## Recent-pattern notes (`the-mechanics` tics to compare against)

- Dek: mechanism-as-subject + because/comma cause resolving on a flat limiting
  declarative ("is all the generator ever does").
- Headings: imperative/second-person ("Ask for ten words, get a hundred," "You
  did not ask for a list"); subject-dropped past-participle ("Trained to run
  long..."); and the stock heading "What's settled, and what's still open" —
  which must NOT appear (the settled/open split belongs in the prose).
- Opener: the exact second-person "Ask a model to..." frame.
- Closer: the terse "The next time..." reframing kicker.
- Diction: "one token at a time," "settled/unsettled/open" as a refrain, "honest"
  as a virtue word, "a weaker signal than it looks." Cross-series: "By the end you
  will be able to...", "The next time..., ask...".

## This round's focus

- Verify the three scopings hold and are not overstated: (1) the lesson is about
  the raw model with no tool and no scratchpad — a reader watching a current
  product multiply correctly must not be able to falsify it; (2) the "numbers
  arrive in chunks, not clean digits" cause is scoped to OpenAI-style tokenizers,
  not single-digit-tokenizer models (Llama/PaLM); (3) step 4 (how the model
  implements addition) is left open, with the bag-of-heuristics vs helix dispute
  named and Nanda's modular-addition circuit flagged as a toy, not the explanation
  of real multiplication.
- Check the worked anchor's arithmetic and its display: 57,897 x 12,832 =
  742,934,304 (true); the model's 742,021,104; the miss (~913,200, ~0.12%). The
  Dziri fall-off figures (GPT-4 zero-shot ~59% / 4% / ~0% at 3/4/5-digit) and
  their scope.
- Confirm the settled/open split is marked in prose without a stock heading and
  without leaning on "unsettled"; confirm differentiation from the published
  `the-mechanics/letter-counting` (characters in a token) is clear, and that
  thinking-out-loud / tool-use are linked, not re-taught.
