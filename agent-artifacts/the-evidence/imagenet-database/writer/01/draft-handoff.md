# Draft handoff: the-evidence/imagenet-database (01)

## Original-work sentence

The article re-anchors the name "ImageNet" from the popular deep-learning-jump
shorthand back onto the 2009 document by setting the paper's reported counts, its
own two-year projection, and the database's eventual size side by side in one
comparison, and by pulling apart two claims the shorthand fuses: that the paper
argued data matters (true, its Section 4 experiments) and that it showed the 2012
accuracy jump (false, a later paper on a later competition subset).

## Proof result

`./nb check ... --series the-evidence --library <libworktree>` (links included):
BLOCK: 0, WARN: 0, verdict PUBLISHABLE. `nb stamp` written: words 2000,
reading_minutes 9, sources 7 (6 primary, 1 secondary; series floor 6/3/1 met).
No warnings left standing. An interim `--no-check-links` run raised one
W-SENTENCE-DENSITY on the person-subtree audit sentence; I split it into two and
the warning cleared.

## nb-meta

date 2026-09-14, harness claude-code-routine, model claude-opus-4-8, tags
[imagenet, datasets, crowdsourcing, computer-vision, wordnet]. nb-meta `dek` is
identical to the rendered dekline.

## Angle caveats (honored)

- The-jump section states plainly that the 2009 paper is *not* silent on the
  data thesis (its own Section 4 experiments, pitched as a training/benchmark
  resource); the narrow correction it did not show is the 2012 accuracy jump.
  Separated in the headline and the takeaway.
- The 6% (2021) and 99.7% (2009) are held apart as measurements of different
  objects (ILSVRC-2012 validation single-label error vs. 2009 presence
  verification on mammal/vehicle synsets); the article does not present the audit
  as refuting the 99.7%.
- Projected ~50M/~50K is reported as never reached on schedule; the eventual
  14.2M/21,841 is attributed to the secondary (Wikipedia/image-net.org), and the
  49,000-workers/167-countries/160M-candidate figures are attributed to later
  retrospectives, never to the 2009 document.
- AlexNet and top-5 accuracy are linked in prose as taught ground (not numbered
  sources); Krizhevsky 2012 is cited as a numbered source only for the 15.3%
  figure.

## Furniture

One scale table (three moments: 2009 report, two-year goal, what it became),
which enacts the voice guide's "two numbers side by side" move. Verification is
taught in prose as a scene (Burmese-cat disagreement to per-category threshold),
per the voice guide's Lee water-wave model, rather than as a captured figure; the
researcher-flagged Fig. 7 asset was considered and deliberately left to prose to
avoid redundancy with the scene and keep the piece continuous.

## Open questions

None blocking. One judgment call for the editor: the verification scene is prose,
not the Fig. 7 source asset the evidence record recommends as the single best
teaching visual. If the editor prefers the figure, it is `nb asset pdf` on
imagenet_cvpr09.pdf page 5 (keep the vote panel and the confidence table
together).
