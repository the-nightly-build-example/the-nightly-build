# Editor review-brief: the-mechanics/over-refusal (round 01)

## Inputs (begin here; read the voice guide first)
- This brief.
- Editorial direction: `../../editorial-direction.md`
- The EXACT writer brief (leak detection): `../../writer/01/brief.md`
- Voice guide: `../../writing-coach/01/voice-guide.md`
- Evidence record: `../../researcher/01/evidence.md`
- Draft handoff (open original-work sentence at third read):
  `../../writer/01/draft-handoff.md`
- Article: `/home/user/the-nightly-build/.nb-work/the-mechanics/over-refusal/library/the-mechanics/over-refusal.html`
- Template context: `.../over-refusal/.nb-context/`

Three ordered reads (skeptic, cut, reader); surgical edits only.

## Points to test hardest (skeptic read)
- **The settled/open boundary is the spine — verify it holds.** Settled:
  (1) refusal is installed by fine-tuning, not native (InstructGPT/Constitutional
  AI); (2) it generalizes by surface features (XSTest "lexical overfitting");
  (3) harmful-refusal is mediated by a single direction in **open-weight** models
  (Arditi et al.). Open: (4) whether *over-refusal* rides that same direction or
  a separate higher-dimensional, task-conditioned mechanism (Wollschläger vs
  Maskey). Confirm the piece does not overclaim step 4 as settled, and does not
  let the single-direction result imply closed models behave identically.
- **Precision on InstructGPT vs Constitutional AI.** InstructGPT is the RLHF
  mechanism and *predicted* over-refusal (2022); it was NOT itself refusal-
  trained wholesale. Constitutional AI reports refusal over-generalizing in
  practice. Flag any sentence that credits InstructGPT with wholesale refusal.
- **Agency language.** The model must never "decide", "judge", "understand", or
  "want". Verify (the writer claims 0 such uses). The one "not X but Y"
  correction is spent in the takeaway — verify only once.
- **Numbers.** Verify against evidence: XSTest 250 safe / 200 unsafe; the
  Minecraft example refused 96%+4% by Llama-2 vs ~0 by GPT-4; OR-Bench 80,000
  prompts / Hard-1K rejection rates (Claude-2.1 99.8, GPT-4o 6.7, Llama-3.1-70B
  3.0). The Hasan & Biswas complication (r = −0.032) must temper any tight-
  tradeoff claim.
- **Do not invent a vendor quote** — the vendor-framing point rides on OpenAI's
  own safe-completions paper conceding "brittle" / "when to refuse rather than
  what constitutes unsafe output". Confirm no fabricated vendor statement.
- Verify display text (headline, dek, subheads) as claims and labels; audit
  `data-nb-kind` (Hasan & Biswas secondary; the rest primary).

## Cut read
- **Banned term "machinery" must be 0**; also load-bearing 0, em-dash ≤4,
  leverage ≤1. Verify by search.
- Cut self-grading, signposts, stock revelation frames, prompt leakage (compare
  against the writer brief — e.g. the brief's "settled vs open" language should
  be realized as prose, not copied as a label). Do not echo
  `instructions-are-data`'s "The prompt a model actually sees" or comma-triad
  headings; compare deks/headings against recent library.

## Reader read
One sentence on what the piece gives beyond its sources; compare with the
draft-handoff's original-work sentence (the marked causal chain). Judge voice
against the exemplars. Retest the headline as the largest claim.

## Furniture
Inspect the two `nb-table` components (XSTest rates; OR-Bench Hard-1K across
vendors): accurate to the evidence, clear purpose, sentence-case labels. Request
corrections through the writer; do not edit markup yourself.

## Output
Write `../../editor/01/editorial-review.md` with the three required lines, direct
edits, required work by owner, and the decision. Return `DONE editor <path>` only
if no redraft is required; otherwise `REQUEST writer/researcher <need>`. Do not
run the proof.
