# editor review-brief: the-instruments/big-bench-hard (01)

Inputs:
- Editorial direction: ../../editorial-direction.md
- Commission: ../../commission.md
- Writer brief: ../../writer/01/brief.md
- Voice guide: ../../writing-coach/01/voice-guide.md
- Evidence record: ../../researcher/01/evidence.md
- Draft handoff: ../../writer/01/draft-handoff.md
- The article: ../../../../library/the-instruments/big-bench-hard.html
- Template context: ../../../../.nb-context/

Output: ./editorial-review.md (editor/01/editorial-review.md)

Proof (for your verification if needed; the writer owns running it): from repo root —
`./nb check .nb-work/the-instruments/big-bench-hard/library/the-instruments/big-bench-hard.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/b1bf3c94-3553-5519-8a12-b9ebb7eba930/scratchpad/library-checkout`

## Recent-pattern notes (`the-instruments` tics to compare against)

- Dek: "[Benchmark] scores/grades a [thing] by [measure]..., [reversal]"; score-
  failing metaphors ("collapse that score," "goes blind").
- Headings: the "The [noun] that [verb]..." relative-clause heading; the wh-
  heading bank.
- Opener: the flat definitional "BBH is a 2022 benchmark..." (benchmark as
  subject).
- Closer (hard tic): the numbered decode-questions handed to the reader ("the
  two/three questions that decode it," "A third question matters just as much").
- Diction: "the bare number / a bare ... percentage," "Read every score as a
  claim, not a fact," "by design / manufactured to," "two scores a point apart is
  noise." Cross-series: "By the end you will be able to...", "The next time...,
  ask...", "what the bare number hides", "honest" as a virtue word.

## This round's focus

- The writer left 3 W-SENTENCE-DENSITY warnings standing on deliberate parallel
  enumerations (an opener colon-list of what the lesson covers, a closing
  question-list the takeaway resolves, and an orientation "three earlier
  decisions" preview). Judge each against `spec/slop.md` and clarity: keep the
  parallel structure only where it is load-bearing and reads cleanly; split any
  that reads as packed. In particular, check the takeaway's question-list: the
  lesson template permits posing questions in the opener and resolving them in the
  takeaway, but it must NOT read as the series' stock "here are the N questions to
  ask about the next score" decode-questions close. If it does, recast it.
- A chart is committed (answer-only vs chain-of-thought against the average- and
  max-human-rater lines). Inspect its provenance and read it as a reader: labels,
  scales, legend, and every plotted number must match the evidence record and the
  owning primary. Route any chart correction to the writer (they hold the tooling).
- Verify the misled case is accurate: OpenAI withheld GPT-4's BBH score for
  contamination; Google published 83.1%; the Claude 3 card cites it. Confirm the
  human-rater gap is reported honestly (small unspecified expert team allowed web
  search; 67.7% average vs 94.4% max), "chain-of-thought beats humans" stays
  model/task-specific (Codex yes, PaLM no on the 23-task average), and the
  204/209/">200" task-count readings are not crossed.
- Confirm `the-evidence/chain-of-thought` and `the-mechanics/prompt-sensitivity`
  are linked, not re-taught.
