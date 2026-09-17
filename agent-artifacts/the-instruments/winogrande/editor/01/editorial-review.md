# Editorial review: the-instruments/winogrande (editor/01)

## Skeptic

The thesis: a WinoGrande score is not a fixed reading of a model's commonsense.
It is the rate at which a model answers one adversarially filtered set of pronoun
questions, and that rate moves with the training budget and with the model family
the filter was tuned against, so the benchmark's difficulty is engineered rather
than intrinsic.

It stands on five claims. I tried to break each and pushed hardest on the spine.

- **The original WSC was small and shortcut-resistant, and "273" is the later
  standardized set.** Held. The article attributes "a little more than a hundred"
  schemas to the 2012 KR paper and pins 273 on WSC273 explicitly (the round's
  headline risk). The stat-strip label reads "SCHEMAS IN THE 2012 CHALLENGE" over
  ~100, correctly. No figure pins 273 on Levesque, Davis, and Morgenstern.
- **WSC got solved without the reasoning.** Held. IJCAI-16 best of 58% on 60 PDPs,
  transformers above 90% on WSC273 by 2019, 13.5% of WSC273 associative
  (Trichelair), and the authors' own verdict quote, all match the record.
- **WinoGrande rebuilt it at scale and filtered it with AFLite.** Held. 43,972
  built / 12,282 debiased, ~53k validated, KL 2.53 to 0.12, and the cross-dataset
  SNLI drop 92.0 to 63.5 all match the Numbers section. The plain-language
  definitions of annotation artifact and adversarial filtering land where the
  terms first appear, as the voice guide asks.
- **The score moves with the training budget (the spine).** Held, and it is the
  strongest part of the piece. The learning curve (160/50.4, 640/58.6,
  2558/67.6, 10234/74.7, 40938/79.1, against human 94.0) matches Table 4 exactly,
  and the article draws the right conclusion: same items, different budget, so
  "50% hard or 79% hard depending on a number you get to set."
- **The near-human scores returned.** Held. UNICORN 86.6% (firsthand, not the
  offline-leaderboard 91.2%, which appears nowhere), GPT-3 few-shot 77.7%, Llama 2
  70B 80.2%, both model reports flagging contamination in their own words. The
  AFLite "hard relative to RoBERTa" caveat and the Davis/Morgenstern
  word-association critique are both present, so the counter-case is steelmanned.

Directional and arithmetic checks: 94.0 - 79.1 = 14.9 ("fifteen-point gap"),
94.0 - 86.6 = 7.4 ("roughly seven points"), all correct. The 118K extrapolation
is carried as the paper's own claim with the fit-mismatch noted ("overreaches its
own math"), not as endorsed arithmetic.

One break, in display-adjacent prose, found and fixed. The takeaway said the
designers "rebuilt it forty times larger." The article's own figures are ~100
schemas to 43,972 problems, which is roughly four hundred times, not forty. I
recast it to the concrete figures the article already carries ("from about a
hundred schemas to nearly forty-four thousand problems"), introducing no new
number.

Source kinds audit: seven primary, one secondary. The Defeat paper is marked
secondary, the conservative call for a paper the article leans on for outside
critique of WinoGrande; the model reports are primary for their own firsthand
figures. No wrong label hides a missing independent source. The eight source
hrefs match the evidence record's verified URLs character for character; I did not
re-fetch each, since the record confirmed them firsthand and they are canonical
arXiv and author-hosted addresses.

Chart: the committed provenance (`chart-1.py`) plots exactly the Table 4 pairs,
with a dotted human-94.0% reference line and a labeled log x-axis. The rendered
image reads honestly: axis titles present, the log scale is named, the curve sits
below the human line throughout, and every plotted value is annotated. No chart
correction to route.

## Cut

Made a sentence-by-sentence slop pass, then walked the edges alone, then read cold
for dangling referents, then ran the delete test. Five sentences were cut or
recast; two of those were template-scope failures rather than ordinary slop.

- Cut the self-referential clause "the fix is the reason the benchmark is worth a
  lesson." The lesson template confines self-reference to the two bookends; the
  body names the lesson here, and the clause was also puffery. "The shortcuts were
  the hard part." carries the transition alone.
- Recast "Two things should slow a reader down before reading that as reasoning" to
  "Two things complicate reading the closing gap as reasoning gained." The body
  addresses no one in this template; the original gestured at the reader.
- Recast the body's second-person "what does a WinoGrande number ... license you to
  conclude" to "... license in 2026," keeping the license / does-not-license pair.
- Cut "Now the numbers the benchmark is known for," a topic-announcing signpost
  that failed the delete test; the section now opens on the 94.0% figure.
- Recast the puffery edge "is the result that made WinoGrande a standard" to "is
  what made WinoGrande look like a real measure of it," which states what the gap
  seemed to show and sets up the very next paragraph's reversal.

One leak, from the voice guide rather than the commission. The why-this-matters
bookend previewed the lesson as "say what it measures, what the filtering bought,
and where it stops," which mirrors the voice guide's own instruction ("say what it
was built to measure, what the filtering bought, and where the gap ... can still
open up") in clause order, with "what the filtering bought" verbatim. The point
underneath is the article's own, so I rewrote the preview in its terms: how the
makers built it, why the same questions score 50% or 79%, and what a high number
does not settle. This also tightens the opener/takeaway pairing, since the opener
now previews the 50-to-79 spine the headline and body deliver.

Negative parallelism recurs (the "not a fixed reading," "is not a reading ...,
it is," "not the finish line" family), but each instance corrects the one real
misconception the piece names throughout, so each is earned; I left them, with the
concentration of two in the takeaway noted as acceptable for a judgment landing.
Checked distinctive phrasing against the Luu, Evans, and Shalizi quotations: the
fair-crediting move and the falsification shape are techniques applied, not clauses
borrowed. No banned punctuation or lexical tells surfaced (zero em-dashes). Against
the recent-pattern notes: no Goodhart closer, no compression-definition heading
mold, no "checked on X, trusted on Y." The dek closes on "and," but it is a fronted
purpose clause plus two coordinated main clauses carrying an ironic reversal, not
the banned three-parallel-clause comma triad; I judged it clear and left it, after
fixing its one real fault below.

One dek fault fixed on this pass: it said the designers "filtered out every
question a model could already guess." "Every" overstates AFLite and contradicts
the article's own finding that word-association items remained. Changed to "the
questions a model could already guess" in both the rendered dekline and the nb-meta
copy, so the two stay identical.

Furniture: the stat strip, the labeled quotation note, the learning-curve figure,
and the holds-up grid each do real work and are documented in the lesson catalog.
No component reads as filler and none repeats a prior article's mold. The bookends
carry no citations, as apparatus should not.

## Reader

Read straight through as the paper's declared reader. What I have that the sources
alone would not give me: the learning curve set directly beside the return of
near-human scores and the two model cards that flag their own contamination, so
that separately recorded facts become one argument, the WinoGrande number is a dial
set by construction and training budget, not a fixed measure of reasoning. The
draft-handoff's original-work sentence claims exactly this synthesis, and it
survives the read; both answers hold, so the piece teaches rather than restates.
The prose sits with the voice-guide exemplars, not a median summary: it says what a
figure measures before reporting it, works the numbers the reader can hold, and
credits the benchmark before pressing its limits. The headline, read as the largest
claim, is the article's genuine best finding and the piece defends it.

## Edits

- nb-meta dek: "every question a model could already guess" to "the questions a
  model could already guess."
- Rendered dekline: same change, kept identical to nb-meta.
- Why this matters: recast the preview list from "say what it measures, what the
  filtering bought, and where it stops" to "know how its makers built it, why the
  same questions can score 50% or 79%, and what a high number does not settle about
  a model's reasoning" (leak fix).
- Filtering section: cut "and the fix is the reason the benchmark is worth a
  lesson" (self-reference); sentence now ends "The shortcuts were the hard part."
- Score-moves section: cut the opening signpost "Now the numbers the benchmark is
  known for."
- Score-moves section: "is the result that made WinoGrande a standard" to "is what
  made WinoGrande look like a real measure of it."
- Scores-came-back section: "Two things should slow a reader down before reading
  that as reasoning" to "Two things complicate reading the closing gap as reasoning
  gained."
- Scores-came-back section: "license you to conclude in 2026?" to "license in
  2026?"
- Takeaway: "rebuilt it forty times larger" to "rebuilt it from about a hundred
  schemas to nearly forty-four thousand problems" (arithmetic fix).

## Required work

None blocking. The orchestrator re-stamps and re-proves after these direct cuts;
the dek edit touched both the rendered dekline and the nb-meta `dek`, which must
remain identical through the re-stamp.

## Decision

approve. The spine, the numbers, and this round's attribution exactness all hold
against the record; the remaining faults were prose, self-reference, one voice-guide
leak, one dek overstatement, and one arithmetic slip, all fixed in place.
