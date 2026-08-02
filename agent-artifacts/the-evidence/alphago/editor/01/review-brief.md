# Editor review-brief: the-evidence/alphago (round 01)

## Inputs (begin here; read the voice guide first)
- This brief.
- Editorial direction: `../../editorial-direction.md`
- The EXACT writer brief (for leak detection): `../../writer/01/brief.md`
- Voice guide: `../../writing-coach/01/voice-guide.md`
- Evidence record: `../../researcher/01/evidence.md`
- Draft handoff (open the original-work sentence only at the third read):
  `../../writer/01/draft-handoff.md`
- Article: `/home/user/the-nightly-build/.nb-work/the-evidence/alphago/library/the-evidence/alphago.html`
- Chart provenance + image:
  `.../library/the-evidence/alphago/chart-1.py` and `chart-1.png`
- Template context: `.../alphago/.nb-context/`

Make the three ordered reads (skeptic, cut, reader) per your skill. Make cuts and
small prose fixes directly in the article. New prose past a word or clause returns
to the writer; evidence gaps return to the researcher.

## Points to test hardest (skeptic read)
- **Naming discipline.** The piece must not fuse AlphaGo Fan (beat Fan Hui, 2016
  paper), the Lee Sedol match (2016, secondary sources, NOT in the paper), and
  AlphaGo Zero (2017). AlphaGo Zero's 100–0 was against **AlphaGo Lee**, not the
  Fan Hui system. Check every sentence and the chart labels.
- **The two myths.** "AlphaGo beat the world's best" (the 2016 paper claims only
  play "at the level of the strongest human players"; Fan Hui = professional 2
  dan, European champion) and "learned from nothing" (= Zero). Confirm each is
  corrected by fact, and the "not X but Y" shape appears at most once (the writer
  says once, in the takeaway — verify).
- **Present-day honesty.** The DeepSeek-R1 use must read as a lab marking where
  the analogy *breaks*, not manufactured overreach.
- **Numbers.** Recompute/verify against the evidence: 29.4M positions / 160,000
  games; 99.8% (494/495); Fan Hui 5–0, Oct 2015; Lee Sedol 4–1, March 2016;
  Zero 100–0 vs AlphaGo Lee; the Elo ladder in the chart (Fan 3,144 / Lee 3,739 /
  Master 4,858 / Zero 5,185, Silver et al. 2017). Confirm distributed (not
  single-machine) AlphaGo played Fan Hui.
- **Display text.** Verify headline, dek, and every subhead as claims and as
  labels (Fan Hui's title/rank; dates; scores).
- **Source kinds.** Audit `data-nb-kind`: Nature 2016, Nature 2017, DeepSeek-R1
  primary; Wikipedia, People's Daily, Google blog secondary.

## Chart (inspect as a reader)
Open `chart-1.png`: labels, scale, legend, and the line-vs-bar choice (writer
used a line chart because Elo has no true zero — judge whether that reads
honestly). Compare its numbers to the evidence and the cited primary. Caption
must be a factual cited label. Request corrections through the writer; never edit
the asset yourself.

## Cut read
Apply the prose/punctuation standards in `editorial-direction.md`. Cut
self-grading, signposts, stock revelation frames, and any prompt leakage
(compare against the writer brief). Watch for inherited shapes: do not let a
"The number X published about itself" opener or comma-triad headings stand;
compare deks/headings against recent library habits noted in the writer brief.

## Reader read
State in one sentence what the piece gives beyond its sources; compare with the
draft-handoff's original-work sentence (the three-document ledger). Retest the
headline as the largest claim.

## Output
Write `../../editor/01/editorial-review.md` with the three required lines
(Skeptic, Cut, Reader), direct edits made, any required work by owner, and the
decision. Return `DONE editor <path>` only if no redraft is required; otherwise
`REQUEST writer <need>` / `REQUEST researcher <need>`. Do not run the proof; the
writer reruns it on any revision. Do not prolong for optional polish.
