# Editor review-brief: when-ai-breaks/microsoft-tay (round 01)

## Inputs (begin here; read the voice guide first)
- This brief.
- Editorial direction: `../../editorial-direction.md`
- The EXACT writer brief (leak detection): `../../writer/01/brief.md`
- Voice guide: `../../writing-coach/01/voice-guide.md`
- Evidence record: `../../researcher/01/evidence.md`
- Draft handoff (open original-work sentence at third read):
  `../../writer/01/draft-handoff.md`
- Article: `/home/user/the-nightly-build/.nb-work/when-ai-breaks/microsoft-tay/library/when-ai-breaks/microsoft-tay.html`
- Template context: `.../microsoft-tay/.nb-context/`

Three ordered reads (skeptic, cut, reader); surgical edits only.

## Points to test hardest (skeptic read)
- **Peter Lee's title:** must read "then corporate vice president of Microsoft
  Research" (contemporaneous), NOT "Microsoft Healthcare". Check headline, dek,
  and body.
- **The disputed cause.** Microsoft's "coordinated attack exploited a
  vulnerability" vs the design-failure reading (Zoe Quinn on record; IEEE
  Spectrum). The piece may conclude the design-failure reading has stronger
  documentary support **because Microsoft never named the vulnerability or
  published a postmortem** — verify that is argued from the record (two outlets
  note the omission), attributed as synthesis, and does not overstate.
- **Parrot vs generated.** The "repeat after me" dictation vs genuinely
  generated output (the Gervais/Hitler-atheism reply) must be distinct, and
  Ottenheimer's rival claim (nearly all dictation) marked as a real but
  uncorroborated, unreviewed single-author doubt — not resolved either way.
- **Dates/numbers.** Verify: launch 23 March 2016; offline in ~16 hours (note
  Microsoft's "24 hours"); apology 25 March; relaunch 30 March; ~95,000–96,000
  tweets (approx, no official tally); XiaoIce ~40 million users. No invented
  figures; the derived 16h05m must not appear as a quoted stat.
- **Offensive content is minimal and evidentiary.** Confirm only what is needed
  to establish the failure and the parrot/generated split is quoted.
- Verify display text as claims and labels; audit `data-nb-kind` (Microsoft's
  own blog/statements/tweets = primary by authorship; reporting = secondary).

## The one accepted WARN — judge it
The writer left `W-PLACEHOLDER` standing on the verbatim quoted tweet
"HITLER DID NOTHING WRONG" (all-caps, from the Guardian), because rewriting its
case would misquote it and it is the only textual support for "antisemitic".
Confirm this is the right call: the quote is verbatim, necessary, minimal, and a
genuine false positive of the placeholder heuristic (not a leftover template
string). If you agree, record that the WARN stands with reason. If the quote is
not necessary, that is a cut, not a rewrite.

## Cut read
- Banned terms: load-bearing 0, machinery 0, em-dash ≤4, leverage ≤1 (verify).
- Cut self-grading, signposts, stock revelation frames, prompt leakage (compare
  against the writer brief). Do not echo the google-flu-trends "Two accounts,
  one gap in the timeline" mold or comma-triad headings; compare deks/headings
  against recent library.

## Reader read
One sentence on what the piece gives beyond its sources; compare with the
draft-handoff's original-work sentence (the two separations). Judge voice against
the exemplars. Retest the headline as the largest claim.

## Furniture
Inspect the `nb-timeline` (five dated beats), the `nb-note` (Microsoft's first
neutral statement), and the `nb-stat-strip` (Tay's ~16h vs XiaoIce's 40M): each
accurate and with clear purpose, sentence-case labels. Request corrections
through the writer; do not edit markup yourself.

## Output
Write `../../editor/01/editorial-review.md` with the three required lines, direct
edits, required work by owner, and the decision. Return `DONE editor <path>` only
if no redraft is required; otherwise `REQUEST writer/researcher <need>`. Do not
run the proof. Note: a single accepted WARN on the verbatim quote is acceptable
for this non-strict series and does not by itself require a redraft.
