# Editorial review: the-instruments/squad (editor/01)

## Skeptic

Thesis: the January 2018 "machines out-read people" headlines rested on a
SQuAD number that means far less than the phrase implied — a few-tenths lead on
exact match over a one-person human baseline, on a benchmark the same systems
failed the moment a single sentence was added to the passage.

The claims it stands on, and how each held:

- **The crossing was human exact match, not human F1.** This is the
  load-bearing fact and it is correct everywhere it appears: the headline
  ("human exact-match score"), the dek ("passed the exact-match line ... while
  still trailing humans on F1"), the "Which score the systems actually crossed"
  section, and the leaderboard table caption ("above the human exact-match line
  (82.304) ... below the human F1 line (91.221)"). Every figure matches the
  evidence: Microsoft 82.650 EM / 88.493 F1, Alibaba 82.440 / 88.607, Hybrid AoA
  82.482 / 89.281, human 82.304 / 91.221, best machine F1 89.281 trailing 91.221
  by "nearly two points" (1.94). No sentence asserts an F1 crossing. Held.

- **The human line was one crowdworker's single second answer, no vote.** The
  "Which score" section states it plainly ("one crowdworker's single answer ...
  not a panel, not a vote, and not an expert"), matching the SQuAD 1.0 paper.
  The majority-vote method is nowhere attributed to 1.0; SQuAD 2.0's later
  construction is discussed without importing its human-scoring method. The two
  are kept straight. Held.

- **The added sentence collapsed the scores.** 75.4 to 36.4 average F1 across
  sixteen 2017 systems, 96.6 percent of failures moving the answer into the
  inserted sentence, with the human-control caveat (about 13 points harshest,
  about 3 on the milder version). All match Jia & Liang. Held — but see the one
  fix below.

- **The number was not empty.** BERT's 93.2 F1 clearing the 91.2 human F1 line,
  SQuAD 2.0 reopening the gap (66.3 F1 vs human 89.5, a 23.2-point difference).
  Both match the evidence and keep the piece from overclaiming. Held.

One break, fixed in place. The dek read "cut the same systems' accuracy in
half." "The same systems" points back to Microsoft and Alibaba, asserting that
the January 2018 ensembles were the ones the added sentence halved. The evidence
supports no such identity: Jia & Liang tested sixteen published systems in 2017,
before those specific ensembles topped the board, and the body correctly says
"sixteen published systems" and "the top systems," never naming the January
ensembles. A wrong label in the dek reaches every scanner, so I corrected it to
"the field's best reading systems," which the evidence supports and the body
already reflects. No new fact, no routing needed.

EM and F1 are defined in plain words at first use — EM as an identical
character-for-character string match, F1 built from a worked bag-of-words case
where precision (2/3) and recall (2/2) are each defined before the harmonic mean
is named. The reader is never assumed to know precision or recall. The worked
arithmetic checks: harmonic mean of 2/3 and 1 is 0.80.

Every citation href was opened as printed. All nine land on their source:
the SQuAD 1.0 paper (D16-1264), the eval script (rajpurkar/SQuAD-explorer,
labeled v2.0 but the operative EM/F1 definitions), SQuAD 2.0 (P18-2124), Jia &
Liang (D17-1215), the SLQA paper (arXiv 1811.11934, Wang/Yan/Wu), BERT (arXiv
1810.04805), the ymcui 24-Jan-2018 leaderboard PDF snapshot, and the two
secondaries (GeekWire, TechStartups). GeekWire returns 403 to a headless client
(the documented anti-bot gate) but the printed address is the article's own
page, which a browser reaches. data-nb-kind labels audit clean: 7 primary, 2
secondary. The ymcui snapshot is labeled primary; it is a dated archival capture
of the leaderboard state the coverage read, corroborated by two independent
primaries (the SQuAD 2.0 wording and the Stanford announcement), and the article
does not imply a live URL shows the historical scores. Defensible as the
researcher recorded it.

## Cut

The prose is lean and concrete; it carries almost no slop. The negative-
parallelism constructions all correct a real, named misconception the lesson is
teaching against — "not the word 'won' rephrased but the exact stretch of text"
(what a span is), "not to write an answer but to point at one" (selection vs
generation), "not by watching people read" (the human line is a measured
number). Each is earned, not a strawman. The section-opening and section-closing
edges hold up read alone: "Even the exact-match line was soft," "That is the
tell," "So the crossing was on exact match only" all carry a fact or a reasoning
step rather than announcing where the argument stands.

No sentence failed the delete test cleanly enough to cut; the closest calls
("What the headlines made of it was another matter," "The deeper problem was
structural") each do real pivot work into substantive claims that follow, and
removing them would drop a reasoning step. Zero body sentences cut.

Two writing fixes made directly. The Why-this-matters opener listed two "how"
clauses joined by a bare comma ("how ... are computed ..., how ... was
measured"); I added the conjunction so the pair reads as a list. And the worked
example reported its F1 two ways — "0.80" in the table and caption, "80" in the
prose — so I aligned the prose to "0.80" to name the figure one way (the leader-
board averages stay on their own 0-100 scale, which is the standard convention
and reads unambiguously in its separate context).

Furniture: two tables, each load-bearing (the worked EM/F1 computation; the
leaderboard crossing with its F1 column kept precisely to make the EM-not-F1
point). No stacked notes or decorative blocks — the commission's block-stacking
risk from the imagenet/bbh pieces is avoided. Nothing to remove, nothing missing.

Against the recent-pattern notes: no "one X per Y, N tries to match it" opener,
no numeric "fall from A to B" heading, and the closing takeaway ("reading an
exact-match tie as the ability to read") does not echo imagenet's "Whose vision
the 5.1 percent belonged to." The dek carries none of the banned molds
(semicolon reversal, suspended question, comma triad). Headings reconstruct the
argument in SQuAD's own nouns. No prompt leakage: the commission's own wrong "human
F1" framing appears nowhere.

## Reader

Read straight through as the paper's declared reader, the piece gives what the
sources alone would not: it resolves the same leaderboard the "superhuman"
coverage read into one grid that shows the crossing was exact match while humans
kept the F1 lead, and it builds a SQuAD score from a single copied span so the
reader can compute EM and F1 themselves and see what each does and does not
reward. The draft-handoff's original-work sentence claims exactly that, and both
answers survive. The prose sits closer to the voice-guide exemplars than to a
median summary: it builds each number in front of the reader (Luu and Shalizi's
move) and lands the misread quietly ("'beat humans at exact match' became 'beat
humans at reading'"), in Rogers's register. The headline, read as the largest
claim, is defended by the body.

## Edits

- Dek (nb-meta JSON and dekline): "cut the same systems' accuracy in half" to
  "halved the scores of the field's best reading systems" — the added-sentence
  collapse was measured on sixteen 2017 systems, not the January 2018 Microsoft
  and Alibaba ensembles the phrase pointed to.
- Why-this-matters opener: added "and" between the two "how" clauses ("... from
  a copied span of text, and how its 'human performance' figure ...").
- Worked example: "scores 80 on F1" to "scores 0.80 on F1" to match the table
  and caption and name the per-example figure one way.

## Required work

None. All routed corrections were within the editor's remit and made in place;
no evidence gap, broken central claim, or source-policy failure remains for the
researcher or writer.

## Decision

approve — the load-bearing exact-match-not-F1 fact is correct in headline, dek,
subheads, and both tables, every citation lands on its source, and the one dek
overreach plus two writing flaws were fixed in place.
