# writer brief: the-instruments/superglue (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — house standard, paper
  voice, series prompt, lesson template identity
- commission.md (../../commission.md) — the measurement, angle, boundaries
- voice-guide.md (../../writing-coach/01/voice-guide.md) — how this piece sounds
- evidence.md (../../researcher/01/evidence.md) — the verified claim set; your only
  source of facts
- the initialized article: ../../../../library/the-instruments/superglue.html
  (edit in place; keep skeleton, engine assets, required labels)
- the effective template contract and furniture under ../../../../.nb-context/

Output: draft-handoff.md (this directory)

Proof: /home/user/the-nightly-build/nb check
  /home/user/the-nightly-build/.nb-work/the-instruments/superglue/library/the-instruments/superglue.html
  --series the-instruments --library /home/user/library-checkout
  (iterate with --no-check-links; run nb stamp then the full check, links included,
  until BLOCK: 0)

Honor these decisions from the evidence and commission:

- The crossing precision is load-bearing: "DeBERTa was first to beat the human
  baseline" is true ONLY with the qualifier the DeBERTa authors use themselves.
  DeBERTa (1.5B) was the first SINGLE model to cross the human macro-average
  (89.9 vs the 89.8 human aggregate, announced 6 January 2021); an ensemble entry
  (T5+Meena, 90.2) had already crossed by then, and reporting named both Microsoft
  and Google. State it that way; do not write the flat "first to beat humans."
- Use the figures the evidence records with their scope: human aggregate 89.8,
  DeBERTa single 89.9 / ensemble 90.3, T5 89.3, T5+Meena 90.2. Show that the one
  leaderboard number is an equal-weight average across eight tasks measured in
  different metrics (evidence cites the aggregation rule). Show how the human
  baseline was built (the MTurk protocol the evidence quotes) so the reader sees
  the human row is itself a measurement with a method.
- The strongest support for the angle: the people who built the number said the
  crossing did not mean human-level understanding, in the same week (DeBERTa
  authors' own caveat; SuperGLUE co-author Bowman on the benchmark no longer
  detecting progress). Give that its weight.
- Sourcing note: the live leaderboard could not be rendered by the researcher; the
  crossing numbers are pinned to the DeBERTa paper table, Microsoft's dated
  reproduction, and two secondaries. Cite the leaderboard as the examined artifact
  but take numbers from the owning primaries as the evidence directs. Dedicated
  primary evidence on task shortcut/artifact features is light — keep the
  saturation point to what the evidence supports and link the taught GLUE lesson.
- GLUE is taught: link the-instruments/glue in Background for the
  predecessor/saturation context; do not re-explain GLUE. One measurement only.
  Name no company as an authority.

Recent shapes to break (see commission): avoid the two-clause ", and"-twist dek and
the comma-triad dek; a number can earn the headline here but don't reuse imo-gold's
"same number, two readings" shape; vary the closing present-day heading away from
"Where X still Y."

This round's focus: take the one leaderboard number apart into the averaging and
the constructed human baseline, land the misleading "AI beats humans" crossing at
the correct single-vs-ensemble precision, and give the reader the three questions
to ask of any "beats human baseline" headline.
