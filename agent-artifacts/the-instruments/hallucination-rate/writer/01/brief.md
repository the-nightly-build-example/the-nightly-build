# writer brief: the-instruments/hallucination-rate (01)

Inputs:
- editorial-direction.md — house standard, press voice, lesson identity, series prompt
- commission.md — subject, angle, boundaries, required contribution
- writing-coach/01/voice-guide.md — the craft standard for this piece
- researcher/01/evidence.md — the complete claim set; use its Numbers section exactly
- library/the-instruments/hallucination-rate.html — the initialized article to edit
- .nb-context/ — effective template contract and furniture catalogs

Output: writer/01/draft-handoff.md (the article itself is edited in place)

Proof: ./nb check .nb-work/the-instruments/hallucination-rate/library/the-instruments/hallucination-rate.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/f20499a9-3e16-5d23-9725-45e099663299/scratchpad/library-checkout
  (iterate with --no-check-links; run the full command, links included, until BLOCK: 0)

nb-meta: set date 2026-08-07, harness "claude-code-routine", model "claude-opus-4-8", tags []. Run `nb stamp` for counts.

Evidence limitation to honor: the researcher found NO specific attributable
dollar/procurement cost tied to trusting a hallucination-rate number. Do not
invent one. The documented "misled" case is (a) the press generalizing a narrow
summary-faithfulness score into an overall "which AI hallucinates least" ranking,
and (b) the task-vs-open-use gap — frontier reasoning models fabricate 33-48% on
open factual QA (PersonQA) while scoring far lower on the summarization board.
Frame the cost as misinformed public/buyers and the false sense of reliability,
honestly, at that scale. Also: several leaderboard entries are 2026-dated models
as the live source presents them; attribute rates to the source's snapshot date
("last updated May 11, 2026") and do not overstate currency.

Recent shapes to break (do not inherit): the-instruments headlines almost all
pair two conflicting numbers ("X and Y are both true") and lean on a stacked-
choices table. Do not inherit that reflex. Find this instrument's own opener and
dek. Check the recent library's deks and headings first.

This round's focus: the number as a manufactured chain — what text is summarized,
how faithfulness is scored, what the judge/classifier model is and how weak it is
(≈55% balanced accuracy on hard cases; ~32% recall on RAGTruth summarization),
and that "faithful summary of a false passage passes." Teach that a hallucination
rate measures summary faithfulness, not general truthfulness, and that three named
benchmarks define hallucination incompatibly so their rates cannot be stacked.
Reference (do not re-derive) the-mechanics/hallucination for WHY models fabricate
and the-instruments/llm-as-a-judge for the automated-judge bias.
