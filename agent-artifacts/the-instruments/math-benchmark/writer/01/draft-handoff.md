# Draft handoff: the-instruments/math-benchmark (01)

## Original-work sentence

The evidence is a list of MATH scores and facts; the article takes them apart to
show that the headline "MATH" numbers labs put side by side are three different
measurements wearing one name (5,000 problems vs the 500 of MATH-500, single
attempt vs majority-of-64 vs Pass@1, string-match grading that both fails right
answers and passes wrong reasoning), and it lands the one owned, documented
misled case: MATH-500 exists only because OpenAI had put 4,500 of the 5,000 test
problems into its own training data, yet "MATH" and "MATH-500" now get reported
as interchangeable. That decomposition is visible in the five-row comparison
table, where the same model on the same set scores 33.6% or 50.3% by counting
rule alone and the 97.3% runs on a tenth of the problems the 6.9% did.

## Proof result

`./nb stamp` then `./nb check ... --series the-instruments --library <checkout>`
with links: **BLOCK: 0, WARN: 0, PUBLISHABLE.** words=1666, reading_minutes=7,
sources=8 (7 primary, 1 secondary). No warnings left standing.

`nb render-check` was skipped by the tool: no Chrome in this environment. The
preview site built cleanly with the draft merged (246 articles). Table and
stat-strip use the documented bare furniture markup, which the runtime dresses
client-side.

## How the brief's constraints were handled

- The rise is not all artifact: the "human-ceiling" section credits real
  capability (PhD ~40%, three-time IMO gold medalist 90%) and states that better
  grading moved Minerva only ~1%, so leakage and loose grading are not the whole
  story.
- Grading runs both ways: false negatives (formatting; SymPy recovered ~1%) and
  false positives (right answer, wrong reasoning; ~8% average, ~30% at Level 5)
  are both stated, with a stat strip carrying the two directions.
- The MATH-500 naming/leakage confusion is the spine (headline, the "two-names"
  section, and the table). Contamination of the MATH test set is shown through
  the PRM800K leakage (Lightman) and the Hugging Face DMCA takedown only.
- The AIME 2024 10-20% contamination figure (MathArena) is NOT borrowed for
  MATH. MathArena appears only as a Go-deeper link, with no number attached.
- Added the GPT-4 Technical Report as an 8th source (series floor is 8) for the
  owned negative fact that the report carries a GSM8K score but no MATH score, so
  any "GPT-4 on MATH" figure is unprovenanced. It reinforces the spine (a "MATH"
  number detached from its source) rather than padding.
- Recent shapes avoided: dek does not open on a scare-quoted score; no reuse of
  "the grader is part of the number" / "turns one X into two measurements" /
  "A single X branded Y." Table columns deliberately differ from aime's (the
  Problems column, 5,000 vs 500 vs "not stated", is the new load-bearing axis).

## Open questions

None blocking. One judgment call worth an editor's eye: the o1 96.4% MATH-500
figure is cited as reported by DeepSeek (evidence flags OpenAI owns it at
source); the prose says "the 96.4% it lists for OpenAI's o1," which keeps the
ownership honest without a separate o1 source.
