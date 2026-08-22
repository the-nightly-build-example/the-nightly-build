# researcher brief: the-instruments/imagenet-top-5-accuracy (01)

Inputs (at the artifact root, two levels up from this brief):
- ../../editorial-direction.md — citation standard, series territory, declared reader
- ../../commission.md — the assignment, the two cracks, and the five ideas the lesson teaches

Output: ./evidence.md (beside this brief)

Read and verify from primary documents:

1. The ILSVRC paper, Russakovsky et al., *ImageNet Large Scale Visual Recognition
   Challenge* (IJCV 2015). Get: the exact definitions of top-1 and top-5 error,
   the class count (1,000), image counts (~1.2M train, 50,000 validation), the
   single-label ground truth, and the human-evaluation section — exactly how the
   ~5.1% human top-5 error was obtained, by how many annotators, and the authors'
   own caveats. Quote with locators.
2. The AlexNet 2012 top-5 error figure and the 2015 "superhuman" model figure
   (e.g. ResNet / the PReLU result reporting ~3.57% or ~4.94% top-5), each from
   the paper that owns it, so the milestone numbers are primary.
3. Beyer et al., *Are we done with ImageNet?* (2020): the single-label vs
   multi-label problem, their ReaL labels, and how top model rankings and scores
   change under corrected labels. Exact figures with locators.
4. Northcutt, Athalye, Mueller, *Pervasive Label Errors in Test Sets...* (2021)
   and/or labelerrors.com: the measured ImageNet validation label-error rate
   (~6%) and its effect on benchmark conclusions. Exact figures.
5. A primary anchor for how top-5 error fell year over year across ILSVRC
   (2010-2017) so the saturation-against-noise point has real numbers.
6. Contemporaneous secondary reporting of the 2015 "computers beat humans at image
   recognition" claim, for the misled-case framing (kept secondary).

Verify every figure against the primary that owns it, and confirm every URL
resolves to the document's own page. In Contradictions, record the honest counter:
ImageNet-scale supervised training genuinely drove real vision progress, and the
label critiques do not erase that; also record any disagreement about the exact
label-error rate. Note (via `nb history`) whether the library already teaches
top-1/top-5 or the ImageNet dataset, and confirm the GLUE lesson's exact finding
so the writer can cite/link it and stay off that ground. Flag any source asset
(e.g. a labelerrors.com example image, or a multi-object ImageNet image with a
single label) that would let the reader test the single-label problem directly.
