# Draft handoff: the-instruments/toxicity-score (writer 01)

## What this article does to the evidence

The evidence is a set of separate findings across seven papers and one news
test. The article reassembles the toxicity score as a single continuous chain,
from a labeler's judgment to a model ranking, and pins each cited bias figure
(Dixon's identity-term imbalance, Sap's dialect correlations, Davidson's
cross-dataset ratios) to the exact link where a human judgment became the
number, so the identity-and-dialect penalty reads as a property of how the score
is built rather than a scatter of unconnected results.

## Proof

Final `nb check ... --series the-instruments` with links included: **BLOCK: 0,
WARN: 0**. Stamped words 2104, reading 9 min, sources 8 (7 primary, 1
secondary). No warnings intentionally left standing.

## Decisions the editor may want to weigh

- **Misleading-case framing.** Held to the brief: the defense (RTP's own 88%
  agreement / Pearson 0.83) opens the failure section, and the penalty is framed
  as a structured, group-concentrated error under a decent average, not noise.
  The sentence "The number is not noise" is a deliberate earned negation of the
  exact misconception the brief names; flagging it in case it reads as bare
  negative-parallelism on a fast pass.
- **Threshold 0.7 omitted.** Perspective's recommended 0.7 operating threshold
  and the "scores near 0.5 are least certain" point come only from the FAQ SPA
  the researcher could not read firsthand (recorded unverified). I left it out
  entirely and present 0.5 solely as RTP's chosen cutoff. If a later round wants
  the "rankings at 0.5 sit in the model's low-confidence band" argument, the
  researcher needs a verifiable source for the 0.7 recommendation.
- **Datasets kept distinct.** Only Wikipedia Talk + New York Times / news
  comments are attributed to the RTP-era CNN. Civil Comments appears once, in a
  Go-deeper row, explicitly labeled a separate later dataset; it is never
  imported into the training lineage.
- **Calibration claim** is cited to RTP's isotonic-regression statement (s1),
  not to the Perspective FAQ. AUC 0.97 is likewise cited to RTP.
- **Date-stamping.** RTP-era CNN vs the 2022 production Charformer (Lees, s4),
  Sap's Perspective query December 2018, Engadget's demo test September 2017, and
  Dixon's "early versions, before mitigation" are all marked in text, with an
  explicit note that every figure carries its study and year.
- **Identity-bias material** is reported with the sources' own figures and no
  evaluative adjectives in the body; the judgment is carried only in the takeaway
  bookend. The two bookends are the only sections that address the reader; the
  body closes on the cost section, with no Verdict block.

## Open questions

None blocking. The one live evidence gap is the unverified 0.7 threshold above.
