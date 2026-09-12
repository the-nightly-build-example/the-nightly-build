# Editorial review: the-instruments/f1-score (editor/01)

## Skeptic

Thesis: F1 is the harmonic mean of precision and recall, it is trustworthy where
it was built to work, and where true negatives matter and the classes are skewed
it can read high while a model misses a whole class. The claims it stands on:

- **Precision and recall come from four counts; F1 is their harmonic mean, and
  the harmonic mean sits near the smaller of the two.** Held. The worked search
  (10 returned of 1,000, 12 relevant, TP 8 / FN 4 / FP 2 / TN 986) is internally
  consistent: precision 8/10 = 0.8, recall 8/12 = 0.67. The fingerprint pair
  (precision 1.0, recall 0.2 -> arithmetic 0.6, harmonic 0.33) matches Sasaki
  exactly. The annotated F1 equation, 2PR/(P+R) = 2TP/(2TP+FP+FN), is correct.

- **F1 never touches the true-negative cell, so a genuinely worse system can
  score higher.** Held against Powers (s5), who owns the TN-independence and the
  "worse system can appear better" claim.

- **The three questions: which positive class, which averaging, at what base
  rate.** Each maps to a cited failure mode: class-swap asymmetry (Chicco, s2),
  base-rate dependence and the all-positive maximizer (Lipton, s6), and the
  micro/macro/weighted split (scikit-learn, s7). The "recall climbs to 1,
  precision settles at the base rate" gloss is sound arithmetic on Lipton's
  result, not an added fact.

- **F1 crowns the wrong classifier (the misleading case).** Held. Every figure
  in the Chicco table and prose checks against the evidence Numbers block: A1
  (91% positive, 0 of 9 negatives, accuracy 0.90, F1 0.95, MCC -0.03) and B1
  (50/50, 5 of 50 negatives, accuracy 0.52, F1 0.66, MCC +0.07). The article
  uses the confusion-matrix numbers, not Chicco's inconsistent prose label, and
  prints MCC -0.03 (the honest reading), not the Fig. 1 -0.04 slip. The
  colon-cancer flip is exact: k-NN F1 0.87 over gradient boosting 0.81, reversed
  by MCC (+0.55 to +0.48); k-NN catches 92% of the sick and clears 52% of the
  healthy. Opitz & Burst (s8) is used only as mechanism (two macro-F1 formulas,
  0.50->0.55 vs 0.49->0.48, gap up to 0.5), correctly mapped: F1-of-averages =
  the rising harmonic-mean formula, averaged-F1 = the falling scikit-learn
  default. No named-leaderboard micro-vs-macro flip is invented, as the record
  and brief require.

- **The fairness turn holds.** F1 ignoring TN is presented as correct in the
  retrieval/needle setting (van Rijsbergen, s1), misleading only where TN matters
  and classes skew, and the MCC-is-no-free-lunch caveat (undefined on an empty
  row/column, resolved by convention) is kept. This is the balance the brief
  asked for, and it is not overstated in either direction.

Origin attributions verified against the record: van Rijsbergen owns the
effectiveness measure E and the recall/precision weighting; the F-measure name
and the Fβ form come from MUC-4/Chinchor (s4); the harmonic-mean derivation and
the naming accident come from Sasaki (s3). The P/R-vs-R/P crossover slip is not
reproduced, and Dice/Sørensen is not claimed at all (safely omitted).

Display text verified descriptor by descriptor. Headline "A high F1 score can
hide a model that missed an entire class" is the A1 result and is defended.
Dek claims (F1 under many leaderboards; F1 never touches the TN cell) are claims
about the world, not a grade of the article's method. Names Chicco, Jurman,
Powers, Sasaki, Chinchor, van Rijsbergen, Opitz, Burst, Lipton, Elkan,
Naryanaswamy all carry the affiliations and roles the record states. Every
`data-nb-kind` is correct: seven primaries own their claims; scikit-learn is
labeled secondary for the averaging definitions, and no label hides a missing
independent source.

All eight citation hrefs opened as printed. Seven land directly on the source
(Glasgow Ch. 7, the Sasaki PDF, ACL M92-1002, and the arXiv abstracts for
Powers, Lipton, and Opitz & Burst; scikit-learn's model-evaluation page). The
Chicco citation (s2) is the `doi.org` persistent identifier the record records
as the article's home; it resolves through the publisher to the open-access
article, and the Springer IDP cookie challenge a bot hits is transport, not a
paywall a reader meets. No break found; nothing routed.

## Cut

Four sentences failed the slop test and were cut or trimmed directly; no pattern
recurs across them beyond edge-position filler.

- "Build the table and the rest follows." Section-closing signpost with no fact
  or reasoning step; the sentence before it (F1 comes from four counts on a small
  table) already carries the point.
- "Notice that neither one uses the box holding 986. Hold on to that." The
  "Notice that" is a lecturing opener and "Hold on to that" is an empty
  foreshadowing signpost that addresses the reader in the body. Kept the load-
  bearing fact as "Neither precision nor recall uses the box holding 986"; the
  next section re-anchors the four boxes on its own.
- "...and that is the whole reason to prefer the harmonic mean." The "X is the
  whole Y" tell, grading the argument. The clause before it states the reasoning
  and stands alone.
- "...and it is worth being exact about when it is the right one." Throat-clearing
  that announces fairness instead of granting it; the retrieval explanation that
  follows does the granting, which is the Shalizi move the voice guide asks for.

The W-SENTENCE-DENSITY the writer left on the opener's three-question setup earns
its place: it is a single parallel list the takeaway resolves item for item, the
opener/takeaway pairing the lesson template endorses, and splitting it would
break that structure. Left as is.

Edges, leakage, and formula all clean after the cuts. The body's second-person
("counts you can read off", "any F1 you are handed", "you ship the model") is
generic expository voice, not bookend-style address, and reads within the voice
guide's register; I left it. The three-question frame echoes the commission's
required contribution but is reworded and grounded in the cited failure modes,
so it is synthesis, not prompt leakage. Headline avoids the stat-as-indictment
mold; the dek's second clause is the untouched-cell mechanism, not the outside-
comparison mold the recent deks stamp; the misleading-case heading ("F1 crowns
the wrong classifier") is a fresh subject-verb line, not the "When the
leaderboard rewrote its own answers" shape. No Verdict note or restating block
closes the body; it ends on the steelman, and the takeaway bookend carries the
judgment, as press/editorial.md requires. Furniture is all documented (bookends,
two tables, one annotated equation, inline math) and each piece does work; no
component is a stack-filler and none is missing.

## Reader

What the piece gives beyond its sources: a reader can build F1 from the four
confusion-matrix counts, see on a worked pair why the harmonic mean punishes a
lopsided score, and leave with three questions to put to any reported F1 (which
positive class, which averaging, at what base rate) that no single source
assembles. That matches the draft-handoff's original-work statement, which points
to the "cell F1 never reads" section and the takeaway. The prose sits closer to
the voice-guide exemplars than to a median summary: small checkable counts in the
Downey manner, the Shalizi grant-then-qualify turn in the fairness paragraph, and
O'Neil-style flat verdicts earned by the numbers ("ship the model that sends
nearly half of the healthy patients on for more tests").

## Edits

- Cut "Build the table and the rest follows." from the orientation section.
- Replaced "Notice that neither one uses the box holding 986. Hold on to that."
  with "Neither precision nor recall uses the box holding 986."
- Cut "and that is the whole reason to prefer the harmonic mean." from the
  harmonic-mean section, leaving "A lopsided pair cannot buy back a low recall
  with a high precision."
- Trimmed "None of this makes F1 a bad measure, and it is worth being exact about
  when it is the right one." to "None of this makes F1 a bad measure."

## Required work

- writer: run a fresh proof (`nb check` and `nb stamp`) over the edited article.
  My cuts changed body prose and lowered the word count slightly, so the stamped
  counts must be regenerated before the PR. No reporting, redraft, source asset,
  or chart provenance work is owed.
- researcher: none. No evidence gap or broken claim surfaced.
- orchestrator: none beyond stamping after the writer's proof.

## Decision

approve. Every figure, attribution, and label checks against the evidence record,
all eight hrefs land on their sources, and the four slop cuts were made in place;
only a fresh writer proof of the edited prose remains before the PR.
