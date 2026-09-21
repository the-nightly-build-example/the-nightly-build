# writer brief: the-instruments/comet-score (01)

Inputs:
- ../../editorial-direction.md — house standard, voice, series prompt, template identity
- ../../commission.md — subject, angle, required contribution, source floor, recent shapes to break
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages
- ../../researcher/01/evidence.md — the complete set of claims available to you
- ../../../../library/the-instruments/comet-score.html — the initialized article to edit in place
- ../../../../.nb-context/ — effective template contract and furniture catalogs
Output: ./draft-handoff.md
Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-instruments/comet-score/library/the-instruments/comet-score.html --series the-instruments --repo /home/user/the-nightly-build

This round's focus, from the researcher's cautions in the record:
- The "misled" case is about *using COMET to select or optimize* translations and about comparing *bare scores across versions or directions*. It is not a claim that COMET ranks systems worse than BLEU. COMET does not: it tops both the To Ship study (83.4 vs 74.6 accuracy) and WMT22 (mean rank 1.32 vs BLEU 5.31). Do not imply COMET is the weaker metric.
- The concrete cost the record supports: optimizing toward COMET selects translations with wrong numbers and mangled names (a date flipped, a person's name garbled) — Amrhein & Sennrich 2022, with over-optimization framed by Zouhar et al. 2024.
- A bare COMET number is uninterpretable without its version, language direction, and whether it is reference-based or reference-free QE; the tool's own docs say pre-2022 scores "do not have a direct interpretation." Anchor this to the primary.
- Handle with care the recorded contradiction that the newer MQM-trained checkpoint is *more* blind to numbers than the older DA one; use it only as the record states it.

The commission's "Recent shapes to break" applies: avoid the "honest in the report, misleading the moment it is quoted" dek mold and the "reading it as if it were X" closer.
