# researcher brief: the-mechanics/overused-words (01)

Inputs (at the artifact root, two levels up from this brief):
- ../../editorial-direction.md — citation standard, series territory, declared reader
- ../../commission.md — the assignment, the causal chain, and settled-vs-open marking

Output: ./evidence.md (beside this brief)

Read and verify from primary documents:

1. The corpus-measurement evidence that specific words rose in frequency. Kobak et
   al., *Delving into ChatGPT usage in academic writing through excess vocabulary*
   (2024): the method (excess word frequency vs a pre-2023 baseline), the specific
   words flagged, and the size of the shift. Get exact figures and the word list
   with locators. Add any primary measurement of word frequency in model output
   itself.
2. The proximate mechanism: a primary source establishing that a language model
   emits a next-token probability distribution and a sampler draws from it (enough
   to cite; the lesson links the taught mechanics rather than re-teaching). Confirm
   the library's exact lesson titles/paths for next-token generation, sampling
   temperature, and RLHF via `nb history`.
3. The settled cause: primary RLHF / preference-optimization literature documenting
   reduced output diversity, distribution sharpening, or mode collapse from
   post-training (e.g. work measuring diversity loss after RLHF/PPO/DPO, or the
   InstructGPT paper's own notes on alignment tax / distribution). Get a concrete,
   quotable finding that post-training narrows the output distribution, with
   locators.
4. The open question: the origin of specific words such as "delve". Find the actual
   primary source of the Nigerian/African-English annotator hypothesis (the
   original analysis or write-up, not a repetition of it) and any data behind it
   (e.g. "delve" base rates by region, or annotator-workforce geography). Record
   exactly how strong the evidence is and label it a hypothesis. Two retellings of
   one origin count as one.
5. The consequence: primary evidence that word-frequency / stylometric AI
   detectors are unreliable or gameable, and evidence that human writing now
   carries the same words (the Kobak follow-through, or detector evaluations).

Verify every figure against its owning primary and confirm every URL resolves. In
Contradictions, record the honest limits: correlation of word frequency with
"AI-written" is not proof any single instance is AI, base pretraining frequency
also matters, and the annotator hypothesis is contested/unproven. Draw the line
the lesson needs between the settled mechanism (post-training concentrates the
distribution) and the open specific-word question. Flag any source asset (e.g. a
frequency-over-time chart from Kobak et al.) that would carry the measured shift
better than prose.
