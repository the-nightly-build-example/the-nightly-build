# writer brief: the-evidence/flamingo (01)

Inputs:
- ../../commission.md — assignment: angle, boundaries, required contribution, habits to break.
- ../../editorial-direction.md — house standard, paper voice, series prompt, template identity.
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting.
- ../../researcher/01/evidence.md — the complete claim set; cite only what it opened; Numbers section used exactly.
- article to edit: /home/user/the-nightly-build/.nb-work/the-evidence/flamingo/library/the-evidence/flamingo.html
- template context: /home/user/the-nightly-build/.nb-work/the-evidence/flamingo/.nb-context/

Output: ./draft-handoff.md

Proof (from repo root /home/user/the-nightly-build, links included, until BLOCK: 0):
  ./nb check .nb-work/the-evidence/flamingo/library/the-evidence/flamingo.html --series the-evidence --library .nb-work/library
Run ./nb stamp before the final check.

This round's focus and decisions the inputs do not settle:
- Evidence caveat: the paper contradicts itself on the headline count — abstract,
  body, and a recomputation from Table 1 give "6 of 16" tasks where few-shot
  Flamingo beat fine-tuned SOTA, but the Table 1 caption says "seven." Use six.
  You may note the printed discrepancy in one line if it earns its place; do not
  silently average or pick seven.
- Keep the commission's anchor foregrounded: the surprise was few-shot, in-context
  multimodal learning beating systems fine-tuned on far more data on a bounded set
  of tasks, with the vision and language backbones frozen — not a raw benchmark
  record.
- The paper does not say why the weights were withheld; that is genuinely unknown
  (only that they were, confirmed by OpenFlamingo/the survey). Do not speculate a reason.
- No code. Link (plain prose links, not numbered sources) rather than re-teaching
  CLIP, Vision Transformer, GPT-3 few-shot / in-context learning, and Segment
  Anything; confirm library URLs via a specific ./nb history query if needed.
- Break the recent habits the commission lists. In particular, do NOT close on a
  "reproduced on open data" beat even though OpenFlamingo invites it (clip and
  vision-transformer already end that way). Outline the reasoning before naming
  sections.

nb-meta fields to fill: "date": "2026-09-20"; "harness": "claude-code"; "model":
your exact running model ID (capable-tier this run; if unknown use
"claude-sonnet-4-5"); "tags": 3-5 concrete topical tags; "dek": identical to the
rendered dekline. ./nb stamp writes counts.

Do not tour the repository or expand the claim set. If a needed fact is missing,
return a precise researcher request. Report the draft-handoff path, the
original-work sentence, the final BLOCK count, and any gap.
