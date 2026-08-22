# researcher brief: the-evidence/whisper (01)

Inputs (at the artifact root, two levels up from this brief):
- ../../editorial-direction.md — citation standard, series territory, declared reader
- ../../commission.md — the assignment, angle, and the four ideas the lesson teaches

Output: ./evidence.md (beside this brief)

Read and verify from primary documents:

1. The Whisper paper, *Robust Speech Recognition via Large-Scale Weak
   Supervision* (arXiv 2212.04356). Get the exact figures the lesson depends on:
   total labeled hours (~680,000), the multilingual and translation breakdowns,
   what filtering removed (machine-generated transcripts), model sizes, and the
   paper's exact claims about robustness / approaching human word error rate. Read
   the sections on evaluation and on the model's failure modes (the paper
   discusses hallucination / repetition and non-speech). Quote the robustness and
   hallucination claims in the paper's own words with locators.
2. The definition and a worked example of word error rate (substitutions +
   insertions + deletions over reference words). Cite a primary/authoritative
   source for the definition.
3. Zero-shot / out-of-distribution evaluation as the paper defines and uses it:
   confirm exactly what "zero-shot" means for Whisper's numbers and why it changes
   the comparison against supervised baselines. Cite the paper.
4. Prior supervised-set scale for contrast (e.g. the ~1,000-hour order of common
   supervised English corpora) from a primary source, so the 680,000-hour figure
   has something the reader can scale against.
5. The present-day deployment failure: the October 2024 Associated Press
   reporting that Whisper hallucinates in transcription (including medical use),
   and any peer-reviewed or conference measurement of Whisper hallucination
   rates. Treat the AP piece as secondary; any claim of harm needs a second
   independent confirmation by parties in a position to know. Record the exact
   quantified findings and who measured them.

Confirm every URL resolves to the document's own page. Classify each source
primary or secondary with the authorship-and-stake test. In Contradictions,
record honestly where clean-benchmark accuracy favors specialized supervised
models over Whisper, and any dispute about how common/severe the hallucinations
are. Note whether the library already teaches word error rate or zero-shot
evaluation (a targeted `nb history` query), so the writer can link instead of
re-teach. Flag any source asset (e.g. a robustness scatter/figure from the paper)
that would carry an argument better than prose.
