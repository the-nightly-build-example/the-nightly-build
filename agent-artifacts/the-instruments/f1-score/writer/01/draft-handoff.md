# Draft handoff: the-instruments/f1-score (01)

## Original-work statement

The article turns eight separate primary and reference sources into one teachable
arc, building F1 from the four confusion-matrix counts and then converting its
documented failure modes into three questions a reader can put to any reported
score: which class was positive, which averaging produced it, and at what base
rate. That synthesis, and the three-question frame the takeaway resolves, is
visible in the "cell F1 never reads" section and the takeaway, and is not present
in any single source.

## Proof result

`./nb check ... --series the-instruments --library <scratchpad>/library-checkout`
(links included): **BLOCK: 0**, WARN: 1, verdict PUBLISHABLE. `nb stamp` written
(words 2147, reading 9 min, sources 8). All eight source URLs resolve.

Warning intentionally left:

- **W-SENTENCE-DENSITY** (one instance, 40 words / 2 clause joins). This is the
  opener's three-question setup ("...ask the three questions that decide whether
  it means anything: which class counted as positive, how the per-class scores
  were averaged, and how rare the positives were."). It is a single deliberate
  parallel list that the takeaway answers item-for-item, the opener/takeaway
  pairing the lesson template endorses. Splitting the three-item list would break
  that structure, so the sentence stands.

## Source composition

8 sources: 7 primary (van Rijsbergen, Chicco & Jurman, Sasaki, Chinchor/MUC-4,
Powers, Lipton et al., Opitz & Burst) and 1 secondary (scikit-learn docs, for the
micro/macro/weighted averaging definitions). Meets the-instruments policy (>=8
sources, >=4 primary, >=1 secondary).

## Decisions honored from the brief

- Built the misleading-case section on Chicco & Jurman's imbalance argument (use
  cases A1 and B1, from the confusion-matrix numbers, not Chicco's prose labels)
  plus Opitz & Burst for the two-macro-F1 divergence, and the real colon-cancer
  ranking flip. No named public micro-vs-macro leaderboard flip was invented.
- Kept F1 fair: presented ignoring true negatives as correct in the retrieval /
  needle setting it was built for, misleading only where TN matters and classes
  are skewed; noted MCC is undefined in extreme cases and resolved by convention.
- Attributed origins per the record and did not reproduce the P/R-vs-R/P
  crossover slip; the Dice/Sørensen ecology provenance was omitted rather than
  overclaimed.
- Varied the misleading-case heading ("F1 crowns the wrong classifier"); no
  stat-as-indictment headline and no negative parallelism in headline or dek.
- nb-meta harness "Claude Code", model "claude-opus-4-8".

## Open evidence or voice questions

None. The one place the record was thin (a named public leaderboard where a
micro-vs-macro choice flipped the announced winner) was handled exactly as the
brief directed, so no researcher request is needed.
