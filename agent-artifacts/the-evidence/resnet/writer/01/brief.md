# writer brief: the-evidence/resnet (01)

Inputs:
- editorial-direction.md — house standard, press voice, lesson identity, series prompt
- commission.md — subject, angle, boundaries, required contribution
- writing-coach/01/voice-guide.md — the craft standard for this piece
- researcher/01/evidence.md — the complete claim set; use its Numbers section exactly
- library/the-evidence/resnet.html — the initialized article to edit
- .nb-context/ — effective template contract and furniture catalogs

Output: writer/01/draft-handoff.md (the article itself is edited in place)

Proof: ./nb check .nb-work/the-evidence/resnet/library/the-evidence/resnet.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/f20499a9-3e16-5d23-9725-45e099663299/scratchpad/library-checkout
  (iterate with --no-check-links; run the full command, links included, until BLOCK: 0)

nb-meta: set date 2026-08-07, harness "claude-code-routine", model "claude-opus-4-8", tags []. Run `nb stamp` for counts.

Two evidence corrections you MUST honor (the researcher caught these):
1. The paper DID forecast generality ("the residual learning principle is generic
   ... applicable in other vision and non-vision problems"). That is a forecast,
   not a demonstration, and it names no architecture. So write that the paper
   forecast generality but did not show it and did not foresee transformers — do
   NOT claim it made no generalization claim.
2. The paper explicitly argues the degradation problem is NOT vanishing gradients
   ("neither forward nor backward signals vanish," Sec 4.1). Do NOT repeat the
   common "ResNet solved vanishing gradients" gloss. The degradation is an
   optimization-difficulty result shown as higher TRAINING error (Fig 1).

Recent shapes to break (do not inherit): recent the-evidence pieces use a
"credited-with X / actually Y" or "never did Z" headline mold and one table of
the paper's printed numbers. Vary the headline; find this paper's own opener and
dek. Check the recent library's deks and headings first.

This round's focus: the paper as document, held against its legend, making the
counterintuitive result (deeper plain nets did WORSE on training error) click
before it is named. The present-day payoff is that residual connections are
reused in the transformer's Add & Norm (sourced from the attention paper itself);
state it, link, and do NOT re-teach attention or the transformer architecture
(other lessons own those). Do not re-tell alexnet; reference it for the ImageNet
backdrop only.
