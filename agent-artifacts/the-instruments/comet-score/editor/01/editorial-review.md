# Editorial review: the-instruments/comet-score (editor/01)

## Skeptic

Thesis: a COMET score is a neural model's predicted human grade for a
translation, so it is only as good as the ratings it learned from, it carries no
meaning without its version, reference mode, and language direction, and aiming
a system at it selects translations whose broken numbers and names it cannot
see.

The claims it stands on, and how each held:

1. **COMET is a supervised model that predicts a human rating, not a formula.**
   Held. Rei et al. (s3) own the design; the article's encoder detail
   (XLM-RoBERTa), the source/candidate/reference inputs, and the fine-tuning to
   match DA and MQM scores all match the evidence record. The three numbered
   steps and the QE paragraph track s3 and s7.

2. **COMET displaced BLEU at the top; it does not rank systems worse than
   BLEU.** Held, and this was the brief's first concern. WMT22 (s2): COMET-22
   1.32, BLEU last at 5.31. Kocmi (s4): 83.4 vs 74.6 on the All-pairs accuracy
   column, used only within that table as the record scopes it. The
   over-optimization section states outright that COMET is the stronger ranker
   and that its blind spot appears only when it becomes the optimization target,
   not the judge. The piece never implies COMET is the weaker metric; it
   pre-empts that misreading and corrects it with the two cited rankings.

3. **A bare COMET number cannot be read or compared alone.** Held. The Unbabel
   docs (s7) supply the pre-2022 "does not have a direct interpretation" quote,
   verbatim, and the 0-to-1 rescaling from 2022. Zouhar (s8) supplies the
   software-version shift (0.796 vs 0.837, same checkpoint, En->De), the
   per-direction human-score span 0.51 to 0.91, and the 12 percent
   under-reporting figure. All match their owners.

4. **Optimizing toward COMET selects wrong numbers and names.** Held, and this
   is the article's own contribution. Amrhein and Sennrich (s9): the sensitivity
   drops (number 0.037, name 0.068, ordinary noun 0.232), the 1970-to-1980 date
   flip, the Tebboune/Tebboene name garble, and the DA-vs-MQM number-error rates
   (7.2 vs 16.6 percent) all match the record exactly. The article correctly
   frames the case as *using* COMET as a target under MBR decoding, and it
   handles all three recorded contradictions: the Kocmi exoneration, the
   minimal-pair-versus-realistic-pool nuance ("shown a clean pair... it usually
   prefers the correct one"), and the newer-MQM-checkpoint-is-more-blind figure.

Tried to break the hardest claim (the dek's "means little on its own"). It
survives: the article's own text is more careful than the dek and walks the
0.85 down through version, reference mode, and direction before resting the
claim on comparability rather than on absolute meaninglessness.

Citation hrefs: opened all nine as printed. Each lands on the source's own page
(ACL Anthology, arXiv abstract, or the Unbabel GitHub repo), and each is the
paper the source entry names. The two Go-deeper links duplicate s9 and s8. The
Background links (bleu.html, bertscore.html) both exist in the published library
snapshot, so the taught-BLEU lesson is linked in prose at first use, not
re-taught and not a numbered source. No routed miscitation.

data-nb-kind audit: s2-s9 are correctly primary, each cited for a claim its
authors own (including Zouhar for its own version/direction/empty-output
experiments). One relayed fact rides on s8: the WMT24 Tower70B MBR result, which
Zouhar reports rather than runs. It is a non-central corroborating example,
clearly presented as reported, so it does not block, but the owning primary is
the WMT24 findings, not Zouhar. s1 (Marie et al.) is labeled secondary and is
cited only for its own survey statistics (98.8 percent, 74.3 percent), which by
the "owns the claim" test reads as primary. I judge the secondary label
defensible: a meta-evaluation reports on a body of primary papers from outside
them, which is the definition's own sense of secondary, and nothing is hidden by
it because the article's independence from COMET's authors is carried
elsewhere (Kocmi, Freitag, Amrhein, Zouhar are all independent of Unbabel).
Recorded, not routed.

## Cut

Ran the slop test on every sentence, then walked the edges out of order, then
read cold as an arrival-from-a-link, then ran the delete test. Three sentences
failed and were cut or trimmed:

- The orientation topic sentence "That is the first thing to understand about a
  COMET score, and it governs everything the number can and cannot do" is a pure
  importance signpost; the substance sits in the sentence after it. Deleted, and
  the paragraph now opens on that substantive sentence.
- "they are worth seeing up close" announced what the next two paragraphs do
  without saying anything. Trimmed, keeping the reasoning clause ("it can only
  be as discerning as they were").
- "and walking it down shows why" summarized the article's own method just
  before the method runs. Deleted.

No repeated slop pattern across the piece. The edges otherwise carry facts or
reasoning: section closers land on earned lines ("Where they were thin, it is
blind"; "cannot honestly be set beside another") rather than on assessments of
the argument. Negative-parallelism check: "not a setting on the same model" and
"It would be easy to read this as a sign that COMET is the weaker metric" each
correct a real, named misconception, so both stay. No prompt leakage: the
"bare COMET number" framing is the article's sourced thesis, not lifted
instruction, and the reader-facing bookend sentences are the template's one
allowed self-reference. Grammar and punctuation are clean; the one semicolon
(DA-versus-MQM contrast) is an earned tight pairing.

Formula check against the recent-pattern notes: the dek avoids the "honest in
the report, misleading the moment it is quoted without Z" mold; the piece does
not open on a bare headline figure, does not run the "how built / limit /
misled" march, and closes on a concrete three-part check plus a warning about
aiming at COMET rather than on a "reading it as if it were Y" reframe. Formula
broken.

Furniture: the stat strip (two heterogeneous software-version numbers), the
table (three sensitivity rows, one shape), and the numbered steps (an ordered
process) each match the family the catalog assigns them and each earns its
place. The piece reads as a continuous article, not a stack of blocks. No
component added or removed.

## Reader

Read straight through as the paper's declared reader. What I have that the
sources alone would not give me: a procedure for reading any COMET number,
walking it down to its version, reference mode, and direction before trusting or
comparing it, plus the single mechanism that ties COMET beating BLEU to COMET
choosing a translation with the year wrong, both flowing from its being a
trained imitation of human ratings. The original-work sentence claims exactly
that synthesis, and the article delivers it; neither answer collapses into
restatement, so no redraft is needed. The prose sits closer to the voice-guide
exemplars than to a median summary: the 0.85 walk-down mirrors Fung's
878-to-235 narrowing, the flat mechanism landings ("the model was trained not to
notice either") echo O'Neil, and the takeaway names concrete checks in
Alexander's closing register. The headline reads as the largest claim and is one
the piece defends.

## Edits

- Cut "That is the first thing to understand about a COMET score, and it governs everything the number can and cannot do." and reopened the paragraph as "A COMET score is a guess at a human judgment..."
- Trimmed "and they are worth seeing up close, because the model can only be as discerning as they were" to "and it can only be as discerning as they were."
- Cut "and walking it down shows why" from the 0.85 setup sentence.

## Required work

None publication-blocking. Minor items for the orchestrator to weigh at
re-stamp, none forcing a revise cycle:

- **writer (minor):** "already trained on large amounts of text in about a
  hundred languages" states a specific figure for XLM-RoBERTa that the evidence
  record does not carry (it records only the encoder identity). The number is a
  true, trivially sourceable property, but it should be sourced or generalized
  to the record's "multilingual/cross-lingual" characterization.
- **writer (optional):** for consistency with the article's own version thesis,
  the WMT22 "1.32" figure is specifically COMET-22 and the sensitivity table is
  specifically wmt20-comet-da; naming those versions would match how the piece
  treats every other figure. Left as the writer's call, since both figures are
  accurate and the surrounding argument does not turn on the version there.
- **orchestrator:** re-stamp and re-prove after these edits (word count moved
  slightly). I did not run the final links proof; nothing I found would fail it.

## Decision

approve — every claim holds against its owning primary, all citations resolve,
the brief's four focus points are satisfied, and the remaining items are minor
polish that does not block publication.
