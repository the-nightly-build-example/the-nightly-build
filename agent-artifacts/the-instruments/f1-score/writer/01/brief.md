# writer brief: the-instruments/f1-score (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md          (house standard, press voice, series prompt)
- ../../writing-coach/01/voice-guide.md (how this piece should sound)
- ../../researcher/01/evidence.md       (the complete claim set; do not exceed it)
- Article to edit (in place):
  /home/user/the-nightly-build/.nb-work/the-instruments/f1-score/library/the-instruments/f1-score.html
- Effective template context:
  /home/user/the-nightly-build/.nb-work/the-instruments/f1-score/.nb-context/

Output: ./draft-handoff.md

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then
full including links until BLOCK: 0):
  ./nb check .nb-work/the-instruments/f1-score/library/the-instruments/f1-score.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/f68f1d9c-d5c2-58e1-960b-5ffb60cad58d/scratchpad/library-checkout
Run `nb stamp` before the final check.

This round's focus and decisions the inputs do not carry:
- The "misled people" case: the record does NOT support a named public leaderboard
  where a micro-vs-macro choice flipped the announced winner. Do not invent one.
  Build the misleading-case section on what the record does own: Chicco & Jurman's
  imbalanced-data argument (F1 and accuracy read misleadingly optimistic where MCC
  does not), with their colon-cancer example, and Opitz & Burst for the
  micro-vs-macro mechanism (two defensible macro-F1 definitions rank systems
  differently). Use the confusion-matrix numbers from Chicco, not its prose labels
  (its use case A1 label and one MCC printout are inconsistent in the source).
- Be fair to F1: ignoring true negatives is the correct behavior in the
  retrieval/needle setting F1 was built for, where true negatives are unbounded and
  uninformative. Present F1 as misleading specifically when true negatives matter
  and classes are skewed, not as broken in general. Note MCC is not a free lunch
  (undefined or unstable in extreme cases).
- Attribute origins carefully per the record: van Rijsbergen's effectiveness
  measure E and the beta weighting; the Fβ formula and the "F-measure" name from
  the MUC-4/Chinchor line; the harmonic-mean derivation from Sasaki. Do not
  overclaim the Dice/Sørensen provenance (recorded only as reported within Chicco).
- Link the-instruments/auroc, the-instruments/calibration-error, and
  the-instruments/squad in Background (all exist); build precision and recall here.
- Commission's "Recent habits not to inherit" binding: no stat-as-indictment
  headline reflex, no negative parallelism in headline/dek, vary the misleading-
  case heading. Fill `nb-meta` harness "Claude Code", model "claude-opus-4-8".
