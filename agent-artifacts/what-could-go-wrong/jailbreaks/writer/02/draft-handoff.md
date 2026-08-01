# Draft handoff — writer/02 (revision) — what-could-go-wrong/jailbreaks

## Original-work sentence
The revision weighs the demonstrated-jailbreak argument against a genuine
marginal-risk steelman (Kapoor et al.'s framework, corroborated by a
jailbreak-specific quote the researcher found inside RAND's own primary
red-team report) and its sharpest rebuttal (Soice et al.'s tacit-skill
argument), then names the one variable, which population a jailbreak's risk
gets measured against, that decides which side looks right, applying the
same both-directions discipline already used on Vassilev's impossibility
proof to a second, independent live debate no single cited source states as
connected.

## Paths changed
- Article: `.nb-work/what-could-go-wrong/jailbreaks/library/what-could-go-wrong/jailbreaks.html`
  (no chart/asset changes this round; `chart-1.py`/`chart-1.png` untouched).

## Proof result
Final command (with link checking):
```
./nb check .nb-work/what-could-go-wrong/jailbreaks/library/what-could-go-wrong/jailbreaks.html --series what-could-go-wrong --repo /home/user/the-nightly-build --library /home/user/library-checkout
```
Result: `BLOCK: 0`, verdict `PUBLISHABLE`.

**One warning left intentionally**: `W-LENGTH-HIGH`, lesson band is
1200-2200 words, found 2588. Reasoning for leaving it: the editor's 01
review marked the missing steelman publication-blocking, and the required
fix (full-strength steelman, attributed to a real developed source; the
sharpest rebuttal; honest weighing; the both-directions rule kept in both
old and new form) cannot be compressed into the vacated band without
cutting the very things the editor asked for. I trimmed the new material
from an initial ~500 body words to ~330, shortened four source citations,
cut the CJS paragraph's direct quote to a paraphrase, and tightened the
Vassilev caveat paragraph — recovering about 200 words — but did not cut
further into the DEMONSTRATED-band prose (GCG, Wei, many-shot) or the
adversarial-poetry paragraph, both of which the editor's 01 "Reader" pass
named as load-bearing for the piece's original-work contribution (the
cross-paper "resistance flips by attack family" thread). `nb-meta`
`words`/`reading_minutes`/`sources` are updated to the true counted totals
(2588 / 13 / 16), so the number itself is honest even though it sits above
the nominal band.

Also confirmed by `nb preview` + a rendered screenshot: the new passage,
its internal link to `what-could-go-wrong/bioweapon-uplift.html`, and the
renumbered Sources list (1-16, in first-citation order) all render
correctly; no seam or seam-adjacent citation error found on inspection.

## Editor/researcher requests addressed
- **Editor 01, "Required work by owner → Writer"**: added a full-strength
  steelman of the "jailbreak risk is overstated, the information is already
  public" position beside the CJS paragraph in "A mathematical proof is not
  the same as a measurement," exactly where the editor pointed to. Attributed
  to Kapoor, Bommasani, Narayanan et al.'s marginal-risk framework (new
  source 11) and corroborated with RAND's own red-team report (new source
  12), which turned out to contain a red-teamer's first-person account of
  jailbreaking a model and concluding the payload didn't matter because "it's
  all public online" — quoted in full, both clauses, per the researcher's own
  caution against quoting only one half.
- **Weighed, not just asserted**: gave the sharpest rebuttal (Soice et al.,
  new source 13 — the barrier was tacit skill, not the facts' existence, and
  that is what a model compresses), then named the actual variable the
  evidence record's contradiction section identifies as deciding the
  argument: which population (expert red-teamer vs. first-time searcher) a
  jailbreak's marginal risk gets tested against. Closed with an explicit
  both-directions sentence mirroring the Vassilev section's own hedge.
- **RAND/bioweapon-uplift linked, not re-taught**: one plain-prose link to
  `../what-could-go-wrong/bioweapon-uplift.html` at first mention of RAND;
  the study's 45-red-teamer/15-cell design is not re-derived here, only the
  jailbreak-specific quote and the topline null result (both new claims this
  article needed, not already in the neighbor piece).
- **Sharp DEMONSTRATED-vs-CONJECTURED line preserved**: untouched. The new
  material sits entirely inside the existing "proof is not a measurement"
  section as a second present-day debate about how much the demonstrated
  jailbreaks matter, not about whether they occurred.
- **Seam mended**: the paragraph that used to open "What practitioners are
  doing now is building shared vocabulary..." now opens "A separate response
  avoids the argument entirely: build shared vocabulary..." so it reads as a
  third position (after doom-side Vassilev critics and dismissal-side
  marginal-risk) rather than a non sequitur after the insertion. The takeaway
  gained one new clause tying the addition back to the opener's "how worried
  to be" framing, so opener and closer still read as a matched pair.
- **`nb-meta` updated to true totals**: `sources` 12 -> 16, `words` -> 2588,
  `reading_minutes` -> 13 (visible byline updated to match).
- Editor 01's other direct edits (Kolter/Fredrikson chronology fix, dek
  precision fix, the 3 sentence cuts, 9 semicolon-to-period conversions) were
  left exactly as the editor made them; nothing in this revision touches
  that prose except where the new insertion's neighboring sentences required
  a transition.

## Remaining evidence or voice questions
None. All four new sources (Kapoor et al., RAND, Soice et al., Peppin et
al.) were verified firsthand by the researcher in `researcher/02/evidence.md`
and are cited only for the specific claims that record supports.
