# Draft handoff: the-instruments/clipscore (01)

## Original work

The evidence records the task-transfer contradiction; the article turns it into
the lesson's spine. It frames CLIPScore from the first section as one model's
opinion of another model's output, then reads every cited failure as a
consequence of that one fact: the headline human-correlation number (Kendall
51.2) was earned grading captions for real photos, not the text-to-image prompt
alignment it is now spent on (Spearman 33.2, roughly half); the below-chance
Winoground result, the adversarial CLIP-score step, and the selection gap follow
as the same inherited weakness rather than a list of unrelated benchmark losses.
The task-transfer claim, which the evidence marks as partly misleading in the
commission, is made the reader's own takeaway.

## Proof

`./nb check ... --series the-instruments --library <checkout>` (links included):
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** `nb stamp` run before the final
proof (words 2080, reading 9 min, sources 8: 7 primary, 1 secondary). Chart
rendered with `nb chart` and inspected; the equation is standard KaTeX (it
typesets live from the site's CDN, and shows as raw TeX only in an offline
screenshot). nb-meta `dek` matches the rendered dekline.

No warnings were left standing. Five W-SENTENCE-DENSITY notes on the first pass
were all resolved by splitting the flagged sentences.

## Angle caveats honored

- Hessel's captioning correlations (tau-c 51.2) are presented as a captioning
  credential that did **not** transfer to T2I, never as the reason CLIPScore is
  trusted for prompt alignment.
- Reward-hacking is CLIP-specific: FuseDream (FGSM against CLIP score) and
  PickScore (selection gap). The DDPO "sixx ttutttas" turtle case is **not**
  used, since its reward was a LLaVA-based VLM, not CLIP.
- Composition is framed as "insufficient sensitivity," not blindness: ARO's
  retrieval drop (50.3% -> 34.1%) is given as a real but small fall. Winoground
  group chance (1/6, ~16.7%) is stated so 7.8% reads as genuinely below chance.
- PickScore uses only CLIP-H 60.8, PickScore 70.5, human-expert 68.0; the
  suspect "Random 56.8" row is not used. FuseDream is cited as "Liu et al."
  without asserting a fuller byline.

## Open questions

- The Winoground chance floor (16.7%) and human ceiling (85.5%) reach the
  article through Lin et al.'s comparison table and the group metric's
  definition, not from the Winoground paper directly. The brief cleared this
  framing; if the editor wants those two numbers pinned to Thrush et al., a new
  researcher artifact opening that primary would be needed. The 85.5% appears
  only in the Fig. 1 caption.
- FuseDream's full author list was not verified against arXiv (evidence flagged
  this); the source entry uses "Liu et al." to stay safe. Confirm before any
  fuller byline.
