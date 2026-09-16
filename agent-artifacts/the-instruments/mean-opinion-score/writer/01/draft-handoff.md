# Draft handoff: the-instruments/mean-opinion-score (writer 01)

**Original work.** The evidence record hands over a standards body's comparability
warning, a controlled same-audio replication, seven papers' disagreeing figures
for the "known-good" ground-truth anchor, and one paper's own footnote admission,
as separate items. The article turns them into a single test a reader can run on
any future "near-human" MOS claim: whether the human recordings it's compared
against sat in the same test, rated by the same listeners, under the same rules
as the system claiming to match them. That test is stated once, in the takeaway,
and every section builds one piece of what it requires.

**Proof.** `./nb check ... --series the-instruments --library <preview-library>`
(links included): `BLOCK: 0`, `WARN: 1`, verdict `PUBLISHABLE`. Word count 2,185
(band 1200-2200). 10 sources, 9 primary + 1 secondary (floor: 8 total, 4 primary,
1 secondary), cited in strict first-citation order 1-10.

**Warning intentionally left.** `W-SENTENCE-DENSITY`, 54 words / 3 clause joins,
on the sentence carrying the P.800.2 quotation ("it is not meaningful to
directly compare MOS values produced from separate experiments..."). The length
is the standard's own sentence, quoted verbatim per the editorial standard;
splitting it would mean rewriting a direct quotation, which I didn't do. Every
other sentence the proof flagged on the first two passes has been split or
tightened, and the article is under the word band's ceiling.

**Evidence scoping decisions, not open questions.**
- I did not cite Cooper & Yamagishi's own range-equalizing experiment (the
  1.28-point drop, 2-vs-25 significant-pairs figures). I used that source only
  for the claim the evidence record itself flags as genuinely independent
  reporting on three other papers' Tacotron 2 figures, so its `data-nb-kind`
  stays honestly `secondary` rather than mixing primary and secondary use under
  one label. The Le Maguer replication carries idea 4's primary evidence
  instead, which the evidence record calls the stronger case.
- I left out the VITS/StyleTTS discrepancy the evidence record flags as
  "recorded from one side only," since VITS's own claim was never independently
  read and a contested figure needs a primary source.
- NaturalSpeech's two differing "Human Recordings" figures (4.52 vs. 4.58) are
  presented as two different numbers in two different table contexts, without
  asserting they came from two separate test administrations, matching the
  evidence record's own uncertainty on that point.

No open evidence or voice question remains for the editor.
