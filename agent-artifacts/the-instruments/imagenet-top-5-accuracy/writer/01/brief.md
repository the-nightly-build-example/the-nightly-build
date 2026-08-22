# writer brief: the-instruments/imagenet-top-5-accuracy (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson template, series direction
- ../../commission.md — the metric, the two cracks, the misled case, boundaries
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with verified exemplar passages
- ../../researcher/01/evidence.md — the complete, verified claim set; the only claims available
- The initialized article to edit in place: /home/user/the-nightly-build/.nb-work/the-instruments/imagenet-top-5-accuracy/library/the-instruments/imagenet-top-5-accuracy.html
- Effective template contract and furniture catalogs: /home/user/the-nightly-build/.nb-work/the-instruments/imagenet-top-5-accuracy/.nb-context/

Output: ./draft-handoff.md (beside this brief)

Proof (from /home/user/the-nightly-build): iterate with
`./nb check .nb-work/the-instruments/imagenet-top-5-accuracy/library/the-instruments/imagenet-top-5-accuracy.html --series the-instruments --library /home/user/library-checkout --no-check-links`
then the same WITH links until `BLOCK: 0`. Run `./nb stamp <that article path>` before the final check.

This round's focus and decisions the inputs do not settle:
- Lead the misled case with the LABELS (the primary finding), not the human baseline. The metric definition itself carries it: top-5 was introduced to handle single-label/multi-object ambiguity (the strawberry-and-apple example). Then the key is noisy. The human baseline is a SECONDARY crack, told in ImageNet's own terms: one trained expert (Karpathy, annotator A1) over many hours, not a crowd.
- Do NOT merge the three different "error rate" measurements. Keep them distinct: Russakovsky's ~0.3% small-sample human/label estimate, Northcutt's ~6% outright wrong labels, Beyer's ~29% multi-label/ambiguous share. They measure different things.
- Do NOT claim that corrected labels reorder the whole leaderboard. Northcutt found overall rankings "unaffected"; instability is confined to near-top comparisons (e.g. ResNet-18 vs ResNet-50 flips only once the mislabeled share is raised). Say exactly that.
- Numbers you may use (verified): winning top-5 error 28.2% (2010) to 3.57% (2015), the ~5.1% human line, best models still err ~9-11% under corrected/multi-label scoring. Do NOT use the 2016-2017 figures (~2.99%, ~2.25%) unless you separately source them — the evidence flags them as unverified.
- Distinguish from the GLUE lesson (the-instruments/glue): GLUE's finding is a hurried untrained-crowd human line on leaky language tasks. This lesson's finding is a flawed single-label KEY on a vision task; the human-baseline point is secondary and about one trained annotator. REQUIRED Background link to the GLUE lesson; do not re-argue it.
- This lesson OWNS defining top-1 and top-5 (no prior lesson does). ImageNet is touched by other lessons (alexnet, generalization, fid, batch-normalization, google-photos-gorilla) — link where useful, don't re-teach. ai-foundations/generalization already used ImageNet-v2 and top-1 accuracy, so keep this piece on the label-key / top-5 ground.
- Break the recent Instruments dek mold ("A perfect X score means Y" / "An X rate is Z"). Write a dek in ImageNet's own nouns stating the concrete finding (single label, noisy key, saturation). Vary the orientation heading.
- Furniture: a small table (year-by-year winning top-5 error, or top-1 vs top-5 on one worked image) or a single figure can help IF the evidence supports the exact numbers. labelerrors.com could not be read as a page — do not cite it as read; the Northcutt paper owns those examples. Don't stack furniture.
- Write the original-work sentence in draft-handoff.md.
