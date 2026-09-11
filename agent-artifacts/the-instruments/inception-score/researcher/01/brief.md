# researcher brief: the-instruments/inception-score (01)

Inputs:
- editorial-direction.md (citation standard, The Instruments territory, declared reader)

Output: researcher/01/evidence.md

Source floor (from nb source-policy --series the-instruments): at least 8
sources, at least 4 primary and at least 1 secondary. Exceed it where a source
changes the interpretation.

Research questions to answer from primary documents:

1. The construction. From Salimans et al. 2016 ("Improved Techniques for Training
   GANs," arXiv 1606.03498): the exact definition of the Inception Score, the
   Inception network and ImageNet training it depends on, and the two properties
   it was meant to reward (per-image confidence and across-set diversity). Record
   the formula in the paper's own terms and what the authors claimed for it.
2. What it cannot see. From Barratt & Sharma 2018 ("A Note on the Inception
   Score," arXiv 1801.01973): the specific failures. Get the concrete
   demonstration (optimizing directly against the Inception network to inflate
   the score; sensitivity to the network weights/implementation; blindness to
   intra-class diversity and to memorization). Record exact claims and any
   numbers.
3. Why FID replaced it. From Heusel et al. 2017 (FID / "GANs Trained by a Two
   Time-Scale Update Rule," arXiv 1706.08500): the explicit critique of IS (it
   ignores real data) and what FID does instead. One or two further primary
   critiques of IS if available (e.g., precision/recall-for-generative-models
   papers) strengthen the "what it cannot support" section.
4. The cost. How widely IS was used as the GAN yardstick and examples of it being
   reported as the headline comparison. Keep this sourced, not impressionistic.

Hunt for contradictions: defenders of IS, cases where IS and FID agreed, and any
claim that the Barratt-Sharma failure is contrived rather than practically
relevant. Record them in full so the editor can test the angle.

The reader already has the fid lesson in this library (the-instruments/fid);
note where a Background link replaces re-teaching. Do not browse the archive for
background beyond confirming that slug exists.
