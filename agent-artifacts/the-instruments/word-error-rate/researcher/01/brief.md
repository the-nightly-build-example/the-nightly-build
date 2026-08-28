# researcher brief: the-instruments/word-error-rate (01)

Inputs:
- editorial-direction.md  (citation standard, the-instruments territory, declared reader)

Output: agent-artifacts/the-instruments/word-error-rate/researcher/01/evidence.md

The measurement under examination: Word Error Rate (WER) in automatic speech
recognition. Read the primary sources and cite to them.

Research questions the evidence record must answer, each traced to an owning
primary (give locators):
- The exact definition: WER = (Substitutions + Deletions + Insertions) / N
  reference words, computed by minimum-edit-distance alignment; note that WER can
  exceed 100%. Cite a primary standard (e.g., NIST scoring / sclite documentation
  or a canonical ASR reference) that owns the definition. Provide a clean worked
  micro-example (a short reference vs a hypothesis with the S/D/I counts) you have
  verified.
- The "human parity" case with exact numbers and provenance: Microsoft's
  conversational-speech-recognition result (Xiong et al., 2016 and the 2017
  update) — the WER figures on Switchboard and CallHome, the human-transcriber WER
  they compared against, and how that human baseline was measured. Read the
  paper(s).
- The pushback / contradiction: IBM's contemporaneous measurement (Saon et al.)
  of the human WER and any dispute over the parity claim. Record it in
  Contradictions in full.
- WER's blind spots, from primary/technical sources: that it weights all word
  errors equally regardless of meaning, is sensitive to text normalization, and
  is not comparable across corpora; and how scores degrade on accents, noise,
  children, and overlapping speech. Cite sources that own each claim.
- The modern hook: the Whisper paper's evidence that a system can post a strong
  WER yet hallucinate fluent text no one spoke — a failure WER barely penalizes.
  Cite the Whisper paper.

Search for what breaks the angle: evidence that WER's "human parity" was in fact
robust and generalized, or that WER captures meaning better than the commission
assumes. Record it in Contradictions with sources.

Source policy: at least 8 sources, at least 4 primary, at least 1 secondary.
Classify each by authorship and stake. Confirm every URL resolves to the
document's own page. Preserve any numeric series a chart could use (e.g., system
vs human WER across Switchboard/CallHome, or WER across noise/accent conditions).
