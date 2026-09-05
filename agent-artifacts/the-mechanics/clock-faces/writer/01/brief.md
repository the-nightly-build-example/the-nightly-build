# writer brief: the-mechanics/clock-faces (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, series prompt, template rules
- ../../commission.md — subject, angle, boundaries, required contribution
- ../../writing-coach/01/voice-guide.md — how this piece should sound; read before drafting
- ../../researcher/01/evidence.md — the complete, only set of claims available to you
- ../../../../library/the-mechanics/clock-faces.html — the initialized article to edit in place
- ../../../../.nb-context/ — effective template contract and runtime assets

Output: draft-handoff.md (this directory)

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-mechanics/clock-faces/library/the-mechanics/clock-faces.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/643ba5c9-25c5-59fc-9937-7e74191ccd45/scratchpad/library-checkout
(iterate with --no-check-links; run the exact command above, links on, until BLOCK: 0 before handoff)

This round's focus — the evidence record moves the settled/open line, and the article must be honest about it:
- The generation behavior (asking for 3:15 and getting ~10:10) has NO measured, peer-reviewed study; it rests on reputable demonstrations. Scope the claim to what those demonstrations show; do not present it as a measured result.
- "Training data is overwhelmingly 10:10" is INFERRED from the advertising convention (Karim et al.), not a corpus count. State it as the well-grounded inference it is, not a counted fact.
- The measured weight sits on the reading side (ClockBench, MeasureBench, TickTockVQA) and the diffusion objective (DDPM's own words). Let those carry the mechanism.
- The desk requires marking settled vs. open. The open part is real and current: the reading gap is closing fast (ClockBench best model 13.3% at Sept 2025 -> ~66.7%, vs 90.7% human; Swap-DPO lifts a base model 1.41% -> 46.22%), and at least one 2026 image model (GPT Image 2) largely overrides the 10:10 prior on a requested time. The prior is strongest for watches; wall clocks vary more. Build the closing gap into the lesson as the honest present state, not a footnote — it is evidence for the mechanism, not against it.

Recent-pattern habits in this series to break (vary construction, do not clone):
- Do NOT reuse a "Where this leaves the [reasoning] question" closer (irrelevant-context, 2026-09-04).
- The closest published neighbors are counting-objects-in-images and hands-in-generated-images (both image-generation failures) and random-numbers (a learned lopsided distribution). Link them for shared machinery; do NOT re-teach how diffusion works from scratch. This lesson's distinct point is a learned convention PLUS a missing rule (time-to-hand-angle) — sharper than "counting/parts are hard" and a single-mode version of the random-numbers point. Make the contrast; do not restate those lessons.
- Vary heading construction from the recent run; write headings in this behavior's own nouns.
