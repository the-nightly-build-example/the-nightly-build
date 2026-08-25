# Draft handoff: the-evidence/clip (01)

## Original work

The article holds CLIP's most-cited number, 76.2% zero-shot on ImageNet,
against the paper's own prompt ablation, its undisclosed 400-million-pair
dataset, and its own weak-task list, so the reader can separate what
"zero-shot" genuinely measured from the prompt engineering and private data it
borrowed, without flattening the real distribution-shift robustness the paper
earned.

## Proof result

Final `nb check` with links: **BLOCK: 0, WARN: 0, PUBLISHABLE.** All six source
URLs and both bookend links (the arXiv paper and the OpenCLIP repo) resolve.
`nb stamp` wrote words=1776 (band 1200-2200), sources=6, reading 8 min.

No warnings left standing. The four W-SENTENCE-DENSITY notes from earlier drafts
were all fixed by splitting the long sentences, not waved off.

## Composition notes for the editor

- Source mix meets the floor as 5 primary + 1 secondary (HF docs is the lone
  secondary, used only for present-day usage). Every source is cited in prose.
- The two contradictions the round focus required are credited in the body: the
  up-to-75% distribution-shift robustness (with Fang 2022 tracing its cause to
  data diversity) and the paper's own contamination audit (median 2.2% overlap,
  accuracy shift rarely > 0.1%). The piece does not read as "only prompts and
  scale."
- The 76.2% (ViT-L/14) and the +1.3 / +3.5 prompt gains (ResNet-50 variant) are
  kept as distinct models in the prompt section, per the evidence's warning.

## Open questions

- **Evidence, resolved by choice, flag for confirmation:** I did not print
  ResNet-50's own ImageNet figure (~76.1%). The evidence marks it a context-only
  anchor not to be cited as a CLIP claim, so I stated parity in the paper's own
  words instead and added no context-only source. I also dropped the 85.4%
  linear-probe number, which the evidence said to verify against the paper's
  table before printing as exact; the teach list stays complete without it. If
  the editor wants the linear-probe gap in, it needs that verification first.
- **Voice/design:** the evidence recommends Figures 4 and 5 as source assets for
  the prompt-gain and strong-vs-weak points. I carried those with a prose table
  and the paper's own weak-task quote instead, judging that lower-risk and
  sufficient at this length. If the editor wants a figure, Figure 5 (the
  per-dataset strong-vs-weak spread) is the one that would add the most.
