# writer brief: when-ai-breaks/ai-writing-detectors (02)

Apply the single required item from the editor's review, nothing more.

Inputs:
- ../../editor/01/editorial-review.md — the review; see its "Required work" item
- ../01/brief.md — the round-01 writer brief (framing still applies)
- ../../researcher/01/evidence.md — the claim set; the six table values are correct, do not change any number
- ../../writing-coach/01/voice-guide.md — the sound to hold
- the article: /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-writing-detectors/library/when-ai-breaks/ai-writing-detectors.html

Output: draft-handoff.md (in this directory), plus the corrected article.

Required item (from editor/01): the paraphrase-collapse table misdescribes its
scale. The body sentence stating the score "runs from 50, a coin flip, up to 100"
and the DetectGPT row cell "detection score, 50 to 100" assert a floor of 50, but
the DetectGPT row's after-value is 25.2, which is below 50 (AUROC runs 0-100; 25.2
is worse than a coin flip). The 50-floor framing also only fits the DetectGPT row:
the OpenAI RoBERTa row and the watermarking row are detection rates that run 0-100
with a floor of 0. Reframe the scale honestly per metric, grounded in the Sadasivan
source, WITHOUT altering any of the six numbers. Fix the table/furniture and any
prose that describes its scale. Preserve all other settled work.

Proof: from repo root /home/user/the-nightly-build run
  ./nb check .nb-work/when-ai-breaks/ai-writing-detectors/library/when-ai-breaks/ai-writing-detectors.html --series when-ai-breaks
Iterate with --no-check-links, then `nb stamp` and the full check until BLOCK: 0.
Record in draft-handoff.md the one item resolved and the final proof result.
