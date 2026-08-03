# Draft handoff: the-evidence/alphafold (writer 01)

## Original work (one sentence)

This lesson separates AlphaFold's single measured result — sub-ångström,
experiment-grade accuracy at predicting one protein chain's folded shape on the
CASP14 blind test — from the three things it is popularly credited with but
never tested: predicting what a protein does, simulating how it folds, and
replacing laboratory structure determination. The separation is made visible in
the claim-vs-record table in "Where the shorthand overshoots the test" and lands
in the single two-half verdict sentence that closes the body.

## Proof result

`./nb check --series the-evidence … alphafold.html --library <checkout>` (links
included, after `nb stamp`): **BLOCK: 0, verdict PUBLISHABLE.**

One WARN left standing, intentionally:

- `W-SENTENCE-DENSITY` on the closing sentence of the body ("On CASP14, AlphaFold
  matched the accuracy of a laboratory … three separate questions the test never
  scored"). This is the voice guide's licensed **two-half verdict**, which the
  guide requires to be one sentence stating both halves with a flat "and"
  juxtaposition (no "but"/"yet"/semicolon). Its three clause joins are the
  does/moves/replace triad the commission's separation names. Splitting it would
  break the licensed form; kept as one sentence by design. Both halves are cited
  earlier (CASP14 accuracy in the blind-test section; the three unshown claims in
  the table and the Terwilliger paragraph).

## Evidence handling worth flagging to the editor

- The unverified **~170,000 PDB training-structures** figure is NOT printed.
  Training scale is given only with verified figures: "roughly 100,000
  experimentally solved structures" (Jumper abstract) and "about 350,000"
  self-distillation sequences (Jumper Methods).
- **92.4 GDT** is attributed to DeepMind's CASP14 blog (source 2), not to the
  Nature paper's body, per the evidence record's ownership note. The Moult
  "~90 ≈ experiment" convention is likewise DeepMind's blog, quoted as an
  informal convention, not a formal CASP verdict.
- The **0.96 Å vs 2.8 Å** (backbone) and **1.5 Å vs 3.5 Å** (all-atom) figures,
  and the **244.02 vs 90.82** CASP Z-scores, are attributed to the sources that
  own them (Jumper paper; CASP14 table). The chart (Fig. 1) is drawn only from
  the four verified r.m.s.d.95 numbers; its `chart-1.py` script carries them.
- Two figures the evidence record did not verify firsthand were caught in the
  display-text pass and removed: CASP's "since 1994 / every two years" cadence
  and the Nobel announcement month ("October"). Neither appears in the piece.

## Open questions for the orchestrator

None blocking. If a later reviewer wants the ~170,000 PDB figure, it needs a
firsthand read of the Jumper 2021 Supplementary Information (a new researcher
artifact), not a writer estimate.
