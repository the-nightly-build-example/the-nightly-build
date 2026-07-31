# Draft handoff — writer 02 (revision) — the-instruments/bleu

## Original work

Unchanged from round 1: the article builds a single self-authored,
hand-verified BLEU computation (candidate "the small brown dog chased the
red ball across the yard" against reference "...quickly chased...") and
carries it through every mechanical step — clipped n-gram precision for
n=1..4, the geometric mean, the brevity penalty, and the final score of
0.742/74 — then uses that same arithmetic (clipping's blindness to a word
absent from the reference) to explain, in the reader's own terms, why the
2005 NIST evaluation's hybrid entry could match fewer n-grams with fluent
synonyms and still deserve the human judges' 1st-place ranking that BLEU
denied it. This round made no argument change, so the original-work sentence
still holds; the round's only work was presentational (moving one packed
comparison into a table) and metadata honesty.

## Article and asset paths changed

- `.nb-work/the-instruments/bleu/library/the-instruments/bleu.html` (edited;
  no new assets/charts — none warranted by the evidence record's Source
  assets notes, unchanged from round 1).

## Proof result

```
nb check .nb-work/the-instruments/bleu/library/the-instruments/bleu.html --series the-instruments --library /home/user/the-nightly-build/library-checkout
BLOCK: 0
WARN: 0
verdict: PUBLISHABLE
```

Also ran `nb preview` (library-checkout + this press-check dir) to inspect
the rendered page after the layout change; the new table renders correctly
alongside the article's other two tables, using the same `nb-table` /
`nb-table-token` markup as the existing worked-example precision table.

## Editorial requests addressed

From `editor/01/editorial-review.md`, "Required work by owner — Writer":

- **Converted the Callison-Burch Table 4 n-gram comparison** in "The
  evaluation where the ranking flipped" from two packed prose sentences
  ("One hypothesis matched more reference words: 27 unigrams, 20 bigrams, 15
  trigrams, 10 4-grams. A second matched fewer: 24, 19, 15, 12.") into a
  small `nb-table` with columns n / matched-more-overall /
  matched-fewer-overall and one row per n=1..4, matching the format the
  primary worked-example table already uses. All eight numbers are the exact
  figures already in the article and in the evidence record's Numbers
  section (Callison-Burch et al. 2006, Table 4, p.253); no new figures were
  introduced. The surrounding prose now states the point plainly ("One
  hypothesis matched more reference words overall; a second matched fewer"
  before the table, "Human judges scored the hypothesis with fewer total
  matches higher on both adequacy and fluency" after it) instead of carrying
  the raw counts itself. I did not use the editor's illustrative phrasing
  "the hypothesis with fewer matches at every n scored higher" verbatim,
  because it is not accurate at the row level: the fewer-overall hypothesis
  has more 4-gram matches (12 vs. 10), not fewer. The claim I kept — fewer
  matches in aggregate, scored higher overall — is what the evidence record
  itself states ("a hypothesis with more matching n-grams... but lower human
  scores... than one with fewer matching n-grams... but much higher human
  scores") and is exact at that level.
- All other required items were already fixed directly by the editor in
  round 1 (brevity-penalty arithmetic, WMT correlation range, Verdict-block
  cut, two hedged-contrast cuts); none were reopened or undone.

Per the brief, also kept `nb-meta` counts honest since the table changed the
word count: recounted the article's actual word count with the same parser
`nb check` uses (`nb.article.Article.word_count`, which excludes the
`<script>`/`<style>` and sources-section text) — 2,170 words, down from the
2,200 an earlier round had recorded. Updated `nb-meta.words` to 2170,
`nb-meta.reading_minutes` to 9 (2170 words at the site's own
words-per-minute constant, `WORDS_PER_MINUTE = 230` in
`engine/nb/site/library.py`, rounds to 9), and the header byline's "11 min
read" to "9 min read" to match. `nb check`'s own W-SELF-COUNT tolerance is
20%, so the prior 2200 was never going to warn, but the brief asked for
honest counts, not just counts inside tolerance.

## Remaining evidence or voice question

None. No new claims were introduced; the claim set is identical to round 1.
