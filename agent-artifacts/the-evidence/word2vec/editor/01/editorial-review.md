# Editorial review: the-evidence/word2vec (editor/01)

## Skeptic

Thesis: the famous `king - man + woman = queen` is a measured result, best
word-analogy accuracy 65.6% on the authors' own 19,544-question set, and the
"the vectors reason about meaning" folklore overstates what the offset does;
the regularities are real, the reasoning was added on top.

Load-bearing claims and how each held:

1. **65.6% best word-analogy, paper 1 (Skip-gram, 1000-dim, 6B Google News).**
   Matches the evidence record (Table 6: 65.6% total, 66.1% semantic, 65.1%
   syntactic). Correctly attributed to the FIRST paper. Holds.

2. **Companion best word-analogy is 61% (Skip-gram, 300-dim, ~1B words); the
   72% is a separate phrase-analogy test at ~33B words.** Both attribution traps
   the brief named are handled explicitly and correctly (the piece even names the
   72% misquote and quarantines it with the phrases). The 6B corpus stays with
   paper 1. Holds.

3. **Levy & Goldberg decomposition.** I opened the PDF as an opponent. The paper
   states the offset argmax, once vectors are unit-normalized, is mathematically
   `cos(b*,b) - cos(b*,a) + cos(b*,a*)` with a, a*, b excluded — a balance of
   three similarities, exactly as the "In plain language" note renders it. Holds.

4. **The regularities reproduce in plain count vectors.** Here the draft broke.
   The article read "sparse vectors scored 45% with the additive method and 68%
   with a multiplicative variant, matching or beating the neural embedding's 62.7%
   and 66.7%." The primary's GOOGLE column is: 3CosAdd embedding 62.70% vs
   explicit 45.05% (embedding *wins*); 3CosMul embedding 66.72% vs explicit 68.24%
   (explicit wins). So the sparse vectors do NOT match or beat under the additive
   method; they only match-or-beat under the multiplicative one. "matching or
   beating ... 62.7% and 66.7%" was false for the additive pair and quietly
   flattered the argument. Fixed by cutting to the true, cited comparison (the
   3CosMul win, 68% vs 66.7%), which is Levy & Goldberg's own headline comparison
   and fully carries the "the pattern lives in the counts" point.

5. **Linzen's skip-the-inputs result.** Verified against the PDF: without
   exclusion the nearest neighbor of `a*-a+b` is b in 93% of cases and a* in 5%
   (never a) — an input word 98% of the time; reversing direction changes mean
   accuracy by -0.11 and tracks the ONLY-B baseline at Pearson r = .72. All exact.
   The 70%-on-plurals figure for the offset-free baseline is the researcher's
   firsthand read; every independently checkable Linzen number matched, so I trust
   it. Holds.

Display text, descriptor by descriptor: headline (65.6%, "word2vec's own test")
is a claim the piece defends and is accurate; dek (Mikolov + colleagues at
Google, 19,544-question benchmark, 2013, offset leans on excluding the inputs)
is accurate and makes a claim about the world, not a grade of the article; nb-meta
dek is identical to the dekline; subheads are named from the papers' own steps,
not a stock shape; the recent "result beneath the <hype>" opener and nb-figure +
nb-math pairing are both avoided. "It is the founding example of word embeddings"
in the Why bookend is loose (embeddings predate word2vec) but reads as "the
canonical popular example," not a claim word2vec invented them — acceptable, not
blocking.

data-nb-kind audit: s1, s2 primary (the papers own their claims); s4 Levy &
Goldberg and s5 Linzen correctly primary (they ARE the critique, not reports of
it); s3 NeurIPS record correctly secondary. s6 GloVe is labeled secondary, but
the claim it carries ("GloVe reached comparable scores on the same set") is
GloVe's own result, owned by the GloVe paper the href points to — that is a
primary use. Conservative mislabel, routed to the writer, non-blocking.

href audit: I opened the two round-focus citations (s4, s5) and confirmed each
lands on the correct document by title and author; the remaining four are the
canonical arXiv / ACL / NeurIPS pages for the named papers and resolve. The GloVe
href uses the canonical ACL page rather than the author PDF the record fetched.

## Cut

Three cuts, all surgical, no new prose past the sparse-vector repair:

- **Signpost.** "This lesson is about the distance between that number and the
  legend" closed the orientation section by announcing where the piece would go.
  The Why bookend already states the same through-line, and the paragraph is
  stronger ending flat on the number. Cut.
- **Attitude.** "Neither run is magic and neither is cheap to beat:" front-loaded
  two vague editorial asides onto a sentence whose real cargo — "the score depends
  heavily on which training shortcut you pick" — is what the table then
  demonstrates. "cheap to beat" is also questionable given GloVe matched the score
  within a year. Cut to the cited claim.
- **Overclaim (see Skeptic 4).** Cut the false additive comparison, leaving the
  accurate multiplicative one.

Worst tell: the sparse-vector overclaim — an inaccurate number-pairing dressed as
a fair "matching or beating," in exactly the sentence the round focus asked me to
push on (is the deflation earned by the decomposition or asserted).

Formula and furniture checks: paragraph endings run varied, no repeated mold, no
comma-and triad in dek or headings. The nb-note carries the hardest concept (the
decomposition) in plain language and earns its emphasis; the method table is the
"real numbers behind the folklore" and earns its place; no Verdict block (the
press bans it) slipped back in. No prompt leakage: the takeaway's "vectors capture
how words pattern together, not meaning" is subject matter, reworded, not a
planning label.

## Reader

Read straight through as the smart, time-poor reader the press declares: the piece
gives something the sources alone would not — one honest ledger that sets the two
measured accuracies (65.6%, 61%) beside the two critiques and lets the legend
shrink as the mechanism appears, so the reader can separate "65.6% on a defined
test" from "the vectors understand meaning." That is the draft-handoff's stated
original work, and it survives the read. The prose sits with the voice-guide
exemplars (Speer's credit-then-press, Willison's wonder-and-doubt-in-one-breath),
not a median summary: it credits what stunned people in 2013 in specific terms
before pressing, and it deflates by showing the operation rather than announcing a
verdict. The headline, reread as the largest claim, is defended by the body.

## Edits

- Cut "This lesson is about the distance between that number and the legend." (orientation).
- Cut "Neither run is magic and neither is cheap to beat:" leaving "The score depends heavily on which training shortcut you pick." (one-test).
- Cut the false additive comparison: "45% with the additive method and ... matching or beating the neural embedding's 62.7% and" so the sentence reads "Those sparse vectors scored 68% with a multiplicative variant, beating the neural embedding's 66.7% on the same task." (what-the-arithmetic-does).
- Ran `./nb stamp`: words 1636, reading_minutes 7, sources 6.

## Required work

- **writer (minor, non-blocking):** s6 (GloVe) carries GloVe's own result and its
  href points to the GloVe paper; change `data-nb-kind="secondary"` to `primary`,
  or re-scope the citation to a claim GloVe genuinely witnesses from outside.
- **writer (optional):** soften "the founding example of word embeddings" (Why
  bookend) to signal it is the canonical popular example, not word2vec's invention
  of the technique.

## Decision

approve — every load-bearing claim was verified against the primaries and the one
break (an inaccurate sparse-vector comparison) is fixed by a surgical cut; the
remaining s6 kind-label is a conservative mislabel that does not block publication.
