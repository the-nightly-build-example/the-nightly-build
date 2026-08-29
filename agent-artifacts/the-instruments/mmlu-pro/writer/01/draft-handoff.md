# Draft handoff: the-instruments/mmlu-pro (01)

## Original-work sentence

The evidence lists MMLU-Pro's construction, its robustness figures, and the
Gema error case as separate facts; the article grades each of MMLU's three named
defects (guess rate, label noise, prompt sensitivity) one at a time against
MMLU-Pro's actual construction, reaches a different verdict for each (finished /
reduced-not-removed / improved-but-order-untested), and converts that split
result into a single operating rule the evidence never states: a large gap
between like-for-like runs is signal, a small gap or a gap across different eval
settings is not.

## Proof result

`./nb check ... --series the-instruments --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Stamped
words=1759, reading_minutes=8, sources=9.

No warnings left standing. Sources: 8 primary, 1 secondary (Data Phoenix, s3),
meeting the commission's min-8 / >=4-primary / >=1-secondary policy.

## Deliberate calls the editor should read as intentional, not gaps

- **Order-robustness is deliberately NOT claimed.** The prompt-sensitivity grade
  (s2) covers 24 prompt styles only. Gupta et al. (s9) measured answer-order
  sensitivity on MMLU, not MMLU-Pro, so the article states MMLU-Pro is "steadier
  against prompt wording and simply untested against answer order." This honors
  the evidence record's explicit caution.
- **Label noise is graded "reduced, not removed"** because no source measures
  MMLU-Pro's own post-review error rate. The v1 Gema figures (~9% / 3,000 / 30
  subjects) are not used; the settled 6.49% / 5,700 / 57-subject figures are.
- **The "not simply a harder MMLU" contribution is carried in the construction
  section** (43% new items, Math the largest discipline), per the evidence
  contradiction note, and again in the closing rule (a high score now certifies
  STEM multiple-choice more than general knowledge).
- **Two arxiv entries for the same paper are intentional** (s2 abstract for
  headline/robustness figures, s4 full text for the pipeline and composition
  tables), matching the researcher's source composition; each citation lands on
  the document that owns its specific claim.
- **One earned negative-parallelism turn is kept**: "So MMLU-Pro is not MMLU made
  harder. It measures a different, STEM-weighted subject mix." The misconception
  it corrects is the commission's central one and is named in the piece.
- **Furniture is deliberately light**: nb-steps for the five-stage build,
  nb-stat-strip for the two design levers. The MMLU-vs-MMLU-Pro construction
  table the brief flagged as optional was left out to avoid duplicating the steps
  and the nb-table reflex the brief named. No Verdict note at the close; the
  takeaway bookend lands the judgment, per press editorial.

## Open questions

None blocking. The saturation figures (near 88%, top four within a point) are
dated "As of August 2026" in prose because the leaderboard updates; if the run
slips materially past that read date the editor may want the researcher to
refresh the top rows.
