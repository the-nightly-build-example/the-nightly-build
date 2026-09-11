# Editorial review: the-instruments/inception-score (editor/01)

## Skeptic

Thesis, stated from the draft alone: a high Inception Score proves only that a
frozen ImageNet classifier was confident about each generated picture and that
the pictures spread across its categories, and nothing more. Because the score
never looks at a real image and measures spread across classes but never within
one, it can be pushed to 900 of a possible 1000 by a generator that makes a
single tuned image per class, so the field retired it for a measure that
compares against real data.

The claims it stands on, and how each held:

1. Headline claim: "Barratt and Sharma drove the Inception Score to 900 of 1000
   with one image per class." Reopened Barratt & Sharma (arXiv 1801.01973) via
   the printed href. The WGAN-initialized attack cycles the target class 1..1000,
   producing one optimized image per class, and reaches 900.10 (appendix) /
   900.15 (Figure 1, Section 4.2.2). The href lands on the paper itself. Names
   (Shane Barratt, Rishi Sharma) and the 900-of-1000 framing are correct. Held.

2. Construction and the range 1..1000. Recomputed the KL/score reasoning:
   ln(IS) = I(y;x) = H(y) - H(y|x); the maximum occurs when each image is
   perfectly confident (H(y|x)=0) and the marginal is uniform over the 1000
   classes (H(y)=ln 1000), giving IS = 1000, and the floor is 1. The draft's
   "the score runs from 1 to 1000" and "a score of 900 means 900 out of a
   possible 1000" are exactly right. The formula in the nb-math block matches
   Eq. 1 in both Salimans and Barratt & Sharma. ImageNet "1.2 million
   photographs sorted into 1000 categories" matches the record. Held.

3. Validation. MTurk accuracy 78.7% (all samples) falling to 71.4% (top 1% by
   IS), and real CIFAR-10 scoring highest at 11.24, both trace to Salimans Table
   3 / Section 4. Barratt & Sharma's concession that IS worked "within a
   significant regime of its usage" is preserved as "did not dispute that it
   worked there." Held. This is the O'Neil credit-before-critique move the voice
   guide asks for, and it is honest.

4. The "it misled" case. Tried hardest to break this, since it is the load-
   bearing claim. A defender's best move is "the attack is contrived — nobody
   ships FGSM noise." The draft pre-empts this cleanly: the noise result (986.10,
   "colored static") is conceded as the case the authors themselves warned about
   (the nb-note quotes "directly optimizing Inception score will lead to the
   generation of adversarial examples," Salimans Section 4 p.7), and the argument
   leans on the WGAN case (~900, "realistic-looking"). Crucially, the mode-
   collapse / within-class-blindness point is then derived from the construction
   itself (one image per class satisfies both terms of the score), so it stands
   even if a reader waves off both attacks. The whole case cannot be dismissed as
   contrived. Held, and the round-focus concern is satisfied.

5. Within-class-diversity blindness is framed as a consequence of the
   construction ("one picture per category ... the spread is measured across
   categories and never within them"), not attributed as any paper's named
   finding. The [3] on that sentence is cited for the construction fact (the
   marginal over 1000 classes) and the one-per-class attack, both of which
   Barratt & Sharma own; it does not claim they headline "intra-class blindness."
   Correct handling. Held.

6. Scope discipline on "what it cost." BigGAN's IS 166.5 (up from 52.52) is
   compared generator-to-generator, never to a real-data IS, so the apples-to-
   oranges trap is avoided. "Most widely used" is not overclaimed into a
   systematic count. The 900.10-vs-900.15 discrepancy is disclosed in the table
   caption with both locations. All three held.

Display text audited descriptor by descriptor. Headline, dek, and every subhead
check out against the owning primaries. "introduced in 2016 by Tim Salimans, Ian
Goodfellow, and their colleagues at OpenAI" rests on the evidence record's
inference (arXiv abstract prints no affiliation; the reference implementation
lives at github.com/openai). This is the record's call and is historically
accurate for this well-known OpenAI work; left as-is, noted here for
transparency. "then at Stanford" for Barratt & Sharma matches the PDF footnote.

data-nb-kind audit: seven primaries (s1 Salimans, s2 BigGAN, s3 Barratt &
Sharma, s4 Lucic, s5 Sajjadi, s6 Theis, s8 Heusel) each own the claim they
carry; s7 (Borji) is correctly labeled secondary as a survey of others' work.
Floor met: 8 sources, 4+ primary, 1+ secondary.

Every citation href opened as printed. All eight arXiv abs URLs land on the
source itself and the abstract-level claims match (BigGAN 166.5/52.52; Lucic
"similar scores with enough hyperparameter optimization"; Sajjadi "one-
dimensional scores"; Theis "need not imply"; Borji "more than 24 quantitative
and 5 qualitative"; Heusel introduces FID "better than the Inception Score").
The two internal prose/Background links (../the-instruments/fid.html,
../the-evidence/gans.html) resolve to existing library files. No broken or
redirected link; no endpoint standing in for a source.

No broken central claim, no missing evidence, no source-policy failure. Nothing
routed to the researcher.

## Cut

Ran the slop pass over every sentence, including display text and the prose
inside the nb-math caption, nb-note, and nb-table caption. The draft is clean:
it holds the plain, concrete register the voice guide sets (goldfish / tabby cat
/ minivan for the label spread; "one picture per category"; naming the wrong
reading before correcting it, the Gould move). No empty conclusions, no puffery,
no decorative-analysis verbs, no vague attribution, no prompt leakage. Negative-
parallelism constructions ("rather than," "need not mean," "reflect tuning and
compute rather than a better model") each correct a real, named position or
report a source's actual finding, so none is a reflex. No em-dashes. The body
speaks to no one except at the two bookends, as the template allows.

Four sentences failed a test and were fixed directly:

- One lecturing imperative, "Now look at what 'one picture per category' quietly
  allows," failed both the slop rule against lecturing openers (Note, Consider,
  Imagine) and the lesson rule that the body speaks to no one. Recast as a plain
  statement that carries the same reasoning step ("One picture per category is
  all the score asks for").
- One pre-grading signpost opening the second orientation paragraph, "The strange
  part is how the number is produced," labeled the surprise instead of stating
  it and lost no fact on deletion. Cut; the paragraph now states the fact plainly
  and names its subject, which also repairs a cross-paragraph "It" referent.
- Two period-appropriate semicolons (the MTurk sentence; the "no agreement ...
  one review counted more than two dozen" sentence) were converted to periods per
  the editorial direction's punctuation standard.

Edges walked separately: first and last sentence of every paragraph, section,
and furniture component, read out of order. The article's last sentence (the
takeaway closer) states the portable judgment the argument built and survives the
delete test. Section-opener edges ("The score was not pulled from nowhere," "The
second result is harder to wave away," "The deeper problem is not special to this
score") are hinges that each carry the argument's next move rather than filler,
and were kept.

Formula check against the recent library (48 The Instruments pieces). The desk's
signature closing heading is the verdict-of-limits stamp ("What a utilization
number cannot see," "A high GAIA score licenses less than the headline says,"
"The dimensions overlap cannot see," "What a high score would not prove"). This
article's closer, "Why the field stopped ranking on a single number," is built
differently and keeps the required "what it cannot support" content in the body.
The orientation heading, "A classifier's verdict became the field's scoreboard,"
is its own concrete step, not a paraphrase of the headline. The dek passes the
three banned molds (no two-clause "claim/twist," no comma-triad, no "The [number]
that" opener); it sits in the looser desk family of "the score does X, never/
blind to Y," but its phrasing is specific and load-bearing (the never-sees-real-
images fact is the spine), so it stays. The gaming-section heading, "The
generator that scored 900 and made one picture per class," echoes the headline's
nouns, but it is a genuine argument step and no desk formula, so it stays.

Furniture: three components, each earning its place. The nb-math block is the
metric's own equation, the thing the lesson is about (not a reflex). The nb-note
carries the authors' printed caveat, which is what makes the noise case
dismissible, so it does argumentative work. The nb-table sets the two attack
scores against the ceiling and discloses the 900.10/900.15 discrepancy. No stat-
strip, no decorative component. Nothing added, nothing removed.

## Reader

Read straight through as the paper's declared reader. What I have that the
sources alone would not give me: a step-by-step build of the number, then the
single fused judgment that a high Inception Score proves classifier confidence
plus spread across categories and nothing else, then the reason that judgment
holds (one image per class satisfies the whole score, so the metric is blind to
within-class variety and to mode collapse), and finally the portable habit of
asking what any single score compares against and what it never looks at. The
draft-handoff's original-work sentence claims exactly that fusion, and the
article delivers it: neither answer restates the sources, so this is not a
redraft case. The prose sits closer to the voice-guide exemplars (Downey's and
O'Neil's concreteness, Gould's naming of the wrong reading) than to a median AI
summary. The headline, read as the largest claim, is one the piece defends in
full.

## Edits

- Orientation, second paragraph: cut the signpost "The strange part is how the
  number is produced." and named the subject, so the paragraph opens "The
  Inception Score reads only the generator's own output."
- Gaming section: replaced the lecturing opener "Now look at what 'one picture
  per category' quietly allows." with "One picture per category is all the score
  asks for.", and joined the two following sentences so the reasoning runs
  without addressing the reader.
- Validation section: changed the semicolon in the MTurk sentence to a period
  ("asked which were real. The workers were right 78.7 percent of the time.").
- Retirement section: changed the semicolon in the Borji sentence to a period
  ("no agreement on which measure to trust. One review counted more than two
  dozen.").

## Required work

- orchestrator: stamp and re-run the proof over the edited article (four direct
  prose/punctuation edits since the writer's last proof), then prepare the PR.
  No evidence gap and no writer rework outstanding.

## Decision

approve — the central "it misled" case is sound and defender-proof, every figure
matches its owning primary, every citation lands on its source, and the four slop
and punctuation faults were fixed in place; only a fresh proof over the edits
remains.
