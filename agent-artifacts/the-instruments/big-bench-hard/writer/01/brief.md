# writer brief: the-instruments/big-bench-hard (01)

Inputs:
- Editorial direction: ../../editorial-direction.md — house standard, paper voice, series prompt.
- Voice guide: ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages.
- Evidence record: ../../researcher/01/evidence.md — your complete claim set (add no facts it lacks).
- The initialized article: ../../../../library/the-instruments/big-bench-hard.html (edit; do not recreate the skeleton).
- Template context: ../../../../.nb-context/ — effective contract, furniture catalogs, runtime assets.

Output: ./draft-handoff.md (writer/01/draft-handoff.md)

Proof: run from repo root /home/user/the-nightly-build —
`./nb check .nb-work/the-instruments/big-bench-hard/library/the-instruments/big-bench-hard.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/b1bf3c94-3553-5519-8a12-b9ebb7eba930/scratchpad/library-checkout`
New slug; no `--revision`. Use `--no-check-links` while iterating; run it links-on until `BLOCK: 0`.

## Recent patterns to break (the-instruments tics)

- Dek: avoid "[Benchmark] scores/grades a [thing] by [measure]..., [reversal]",
  and score-failing metaphors ("collapse that score," "goes blind").
- Headings: avoid the "The [noun] that [verb]..." relative-clause heading and the
  wh-heading bank.
- Opener: do NOT open with the flat definitional "BBH is a 2022 benchmark..."
  (benchmark as grammatical subject).
- Closer (hard tic): do NOT hand the reader numbered decode-questions.
- Diction: avoid "the bare number / a bare ... percentage," "Read every score as
  a claim, not a fact," "by design / manufactured to," "two scores a point apart
  is noise."
- Cross-series: no "By the end you will be able to..."; no "The next time..., ask"
  numbered-questions close; "what the bare number hides"; "honest" as a virtue word.

## Decisions the inputs may not settle (from the researcher's report)

- **Verified figures to build on** (use the record's exact values/scopes): BIG-
  bench ~204 tasks, 450 authors, 132 institutions; BBH is 23 tasks (selection
  funnel 209 to 78 to 36 to 23); the average human-rater score is 67.7% and the
  max human score 94.4%; with 3-shot chain-of-thought, PaLM 540B goes 52.3% to
  65.2%, Codex 56.6% to 73.9%, InstructGPT 51.8% to 68.4%; Claude 3 Opus reports
  86.8% BBH at 3-shot CoT; BIG-Bench Extra Hard's best general model scores 9.8%
  and its best reasoning model 44.8%.
- **The task count is contested** (204 in the paper vs a 209 selection funnel vs
  "more than 200" in the repo). Record the scope you use; do not cross the readings.
- **Report the human-rater gap honestly.** The number of human raters behind the
  "average human" bar is not stated in BIG-bench (its Appendix E detail is not
  available); the bar rests on an unspecified, small team of EXPERT raters who
  were allowed to use internet search, and it sits well below the max-human 94.4%.
  Say this — do not imply a lay-person baseline.
- **"Chain-of-thought beats humans" is model- and task-specific.** On the 23-task
  average, Codex-with-CoT (73.9%) clears the average human (67.7%) but PaLM-with-
  CoT (65.2%) does not, even though PaLM beats the bar on 10 of 23 tasks. Do not
  state "CoT beats humans" flatly.
- **Sharpest "where it misled" case:** OpenAI's GPT-4 technical report WITHHELD
  GPT-4's BBH score because BIG-bench was found in the training data, yet a GPT-4
  BBH figure of 83.1% still circulates in model cards (e.g. the Claude 3 card,
  sourced from Google's Gemini report). Same model, same benchmark — one party
  withholding for contamination, a rival publishing anyway. Build the misled case
  on this.
- The chain-of-thought PAPER is a separate published lesson
  (`the-evidence/chain-of-thought`) — link it for what CoT is, do not re-teach it.
  Link `the-mechanics/prompt-sensitivity` for why prompting moves scores.
