# Editorial review 01 — the-instruments/bleu

## Skeptic

Skeptic: thesis "BLEU counts overlapping word runs against a human
reference, not meaning, and its score depends on measurement choices and a
sample size most reports never state, badly enough that it once ranked the
human judges' 1st-place system 6th"; tested 6 claims (the worked-example
arithmetic end to end; 28.4 EN-DE vs Vaswani 2017; the tokenization/
reference-count swing table; the Papineni correlation figures and sample
size; the Reiter WMT year-by-year correlation range; the 2005 NIST
misranking direction and R² figures); broke 2, both fixed directly:

1. **Brevity-penalty arithmetic error.** I recomputed the worked example by
   hand (candidate 11 words / reference 12 words, p1..p4 = 1.000, 0.900,
   7/9, 0.625, geometric mean ≈0.813, BP = e^(−1/11) ≈0.913, final
   ≈0.813×0.913≈0.742). The draft said applying the brevity penalty "costs
   another 8.7 percentage points." That number is 1−BP (0.087), a property
   of the BP factor itself — not the actual point-drop the multiplication
   produces on the running score, which is 0.813−0.742 ≈ 0.071, i.e. 7.1
   points. Read next to the immediately preceding "almost 19 percentage
   points" (the correctly-computed n-gram-precision drop from 1.000 to
   0.813), the wrong figure implied a reader doing the sum would land on
   the wrong final number. Fixed: "8.7" → "7.1 percentage points, from
   0.813 down to the final score below."
2. **WMT correlation range error.** The draft's "for the other, from
   −0.43 to 0.88" reports the English→German column of Reiter's Table 1
   (evidence Numbers section). The English→German column's actual max is
   0.83 (WMT13); 0.88 belongs to the German→English column (WMT16). Fixed:
   "0.88" → "0.83", verified against every value in the evidence record's
   reproduced table.

Everything else re-derived clean: 28.4 EN-DE is confirmed in Vaswani et
al.'s Abstract, Table 2, and §6.1 text per the evidence record and the
article states it correctly, with the correct "more than 2 points above"
framing (the abstract's own words). The Callison-Burch direction is exact
in both directions the piece uses it: "Human judges ranked that hybrid
entry 1st. BLEU ranked it 6th," matching Callison-Burch et al. 2006 §4
verbatim, and the headline states the same direction correctly. R²
figures (0.14→0.87 adequacy, 0.002→0.742 fluency), the Table 4 n-gram
counts (27/20/15/10 vs 24/19/15/12), the 10^73 permutation figure, the
1.8-point and 3.2-point tokenization/reference swings, and the Mathur
outlier-correlation figures (0.97→0.81, 0.85→0.58) all check out exactly
against the evidence record. `data-nb-kind` audited source by source
against the evidence record's own primary/secondary calls: s1 Vaswani,
s2 Papineni, s4/s5 Post, s7 Mathur, s8 Callison-Burch correctly `primary`;
s3 Google Cloud and s6 Reiter correctly `secondary`. No mislabels found.

## Cut

Cut: 2 sentences/clauses removed as prose, plus one full furniture block
removed as a template-direction violation; worst tell: a "not X" trailing
clause invented for cadence rather than correcting a real misconception.

- The piece used the "X, not Y" / "rather than" hedged-contrast mold five
  times against the house ceiling of one or two per piece: the dek
  ("rather than reading what it means"), the orientation ("BLEU is not a
  percentage of sentences judged correct. It is the output of..."), the
  holds-up grid ("...real across the surveyed literature, not one lab's
  artifact"), "built by people rather than tuned against the metric," and
  the takeaway's closing sentence ("a claim worth checking, not a finding
  worth repeating"). Kept the two load-bearing ones (dek and orientation,
  which together set up the piece's central claim that BLEU counts words
  rather than reading meaning). Cut the holds-up grid's trailing "not one
  lab's artifact" (a strawman clause; nothing before it claimed the
  correlation was one lab's artifact) and cut the takeaway's closing
  sentence, which was a generic maxim about BLEU rather than a
  piece-specific fact. The paragraph's prior sentence — "Across WMT19, a
  1-2 point BLEU difference...reflected a real improvement only about half
  the time" — is the stronger, already-earned ending; the cut sentence had
  gone soft one beat past it.
- Removed the mid-body `nb-note nb-note-strong` block labeled "Verdict"
  from the "what-the-number-holds" section. `press/editorial.md` states
  plainly for this template: "The takeaway bookend is where a lesson lands
  its judgment. Do not close the body with a Verdict note, or any block
  that restates the finding. Some older articles still carry that block
  from the paper's earlier template. It is a leftover, not a model to
  copy." The engine's base `FURNITURE.md` catalogue does sanction a
  Verdict note generally (paired with a holds-up grid), but this press has
  explicitly opted out of it for lesson pieces, reserving judgment for the
  takeaway bookend — which the article's takeaway already does
  independently. The cut block restated the holds-up grid immediately
  above it without adding anything new. No other section or citation
  depended on it; source 6 (Reiter) was already cited earlier in the same
  paragraph, so removing this instance did not change first-citation
  order or the source count.

Checked recent-pattern notes from the voice guide (no colon-subtitle
headline, no shocking-swing opener, no comma-and-clause heading cadence,
no reuse of the humaneval/mmlu/swe-bench openers) — the piece avoids all
of them. Section headings read as argument steps, not scaffolding
("A score built from one sentence pair" → "Counting runs of words, then
capping the count" → "What one score does and does not settle" → "The
evaluation where the ranking flipped").

One item found but **not** fixed here, because the fix needs a new table
(markup), which is the writer's job: the Callison-Burch Table 4
comparison in "The evaluation where the ranking flipped" packs eight
numbers into two prose sentences — "One hypothesis matched more reference
words: 27 unigrams, 20 bigrams, 15 trigrams, 10 4-grams. A second matched
fewer: 24, 19, 15, 12." This is exactly the pattern the voice guide bans
("a paragraph of '1-grams: 5, 2-grams: 3'... a sentence carrying more than
one count has stopped explaining and started listing"), and the review
brief specifically flagged checking for it. The primary worked example
already obeys this rule with its own table; this second, real-case count
comparison does not.

## Reader

Reader: this gives me the ability to compute a BLEU score by hand from a
real sentence pair, to name the exact measurement choices (tokenizer,
reference count) that move a reported score without moving the
translation, and a specific historical case — with the arithmetic
mechanism named, not just asserted — for why a headline BLEU delta can
point the wrong way. Comparing against the original-work sentence in
`writer/01/draft-handoff.md`: the draft's claimed original contribution is
connecting the toy arithmetic's blind spot (clipping cannot credit a
correct synonym absent from the reference) to the 2005 NIST case's
mechanism (the human-preferred hybrid entry used synonyms BLEU could not
credit) — a link no single source states as one argument. That connection
survives every cut made here; the "wording BLEU could not credit" note
explicitly reuses the clipping vocabulary from the worked example
("Clipping caps a matched word's count at how often it appears in the
reference; it has no rule at all for a word that never appears there") to
explain the real case, exactly the link the draft handoff claims. The
piece reads closer to the voice-guide exemplars (Reiter's quantified-claim
habit, Alammar's one-running-example discipline) than to a median AI
summary — it never asserts "scores don't always reflect quality" without
immediately attaching a number to it. The headline, re-read as the
piece's largest claim, is exact: Callison-Burch et al. 2006 states the
human 1st-place entry finished 6th on BLEU, word for word what the
headline claims.

## Edits made directly in the article

1. `"8.7 percentage points"` → `"7.1 percentage points, from 0.813 down to
   the final score below"` (brevity-penalty arithmetic, re-derived by
   hand).
2. `"−0.43 to 0.88"` → `"−0.43 to 0.83"` (WMT English→German correlation
   range, checked against the evidence record's reproduced Reiter table).
3. Removed the mid-body `nb-note nb-note-strong` "Verdict" block (press
   direction: judgment belongs in the takeaway for this template).
4. Cut the holds-up grid's trailing `", not one lab's artifact"` clause
   (strawman "not" clause, over the hedged-contrast ceiling).
5. Cut the takeaway's closing sentence, `"A higher BLEU score is a claim
   worth checking, not a finding worth repeating."` (formulaic closer,
   over the hedged-contrast ceiling; the preceding sentence is the
   stronger, already-earned ending).

Proof after all edits:
```
nb check .nb-work/the-instruments/bleu/library/the-instruments/bleu.html --series the-instruments --library /home/user/the-nightly-build/library-checkout
BLOCK: 0
WARN: 0
verdict: PUBLISHABLE
```

## Required work by owner

- **Writer**: convert the Callison-Burch Table 4 n-gram comparison in "The
  evaluation where the ranking flipped" ("27 unigrams, 20 bigrams, 15
  trigrams, 10 4-grams" vs. "24, 19, 15, 12") from packed prose into a
  small table or listing, matching the format the primary worked example
  already uses, so the surrounding prose can state the point plainly
  ("the hypothesis with fewer matches at every n scored higher with human
  judges") instead of carrying the raw counts itself. Re-run the proof and
  confirm `nb-meta` word count/reading time still match after the change.
- **Researcher**: none.

## Decision

Not clean for publication as-is: one structural fix remains that requires
new markup (a table), which is outside the editor's surgical remit. All
arithmetic, sourcing, `data-nb-kind`, and prose-ceiling issues found in
this review are already fixed directly in the article, and the proof is
`BLOCK: 0 WARN: 0` after those fixes.
