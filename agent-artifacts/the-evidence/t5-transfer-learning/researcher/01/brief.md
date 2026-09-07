# researcher brief: the-evidence/t5-transfer-learning (01)

Inputs:
- `editorial-direction.md` — citation standard, series territory, declared reader
- `commission.md` — the assignment, its boundary, and the source floor
- this brief

Output: `researcher/01/evidence.md`

Subject: the T5 paper, "Exploring the Limits of Transfer Learning with a Unified
Text-to-Text Transformer" (Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou,
Li, Liu; Google, 2019, revised 2020). Read the paper firsthand (arXiv 1910.10683,
JMLR 2020) and the artifacts it released.

Answer these, each traceable to the owning source:

- What T5 is and the exact "text-to-text" framing: how every task becomes text
  in, text out, with a worked example the reader can follow.
- The C4 dataset: how it was built from Common Crawl, its cleaning steps, and its
  size (state the figure and unit the paper gives).
- What the paper's systematic study actually compared (objectives, architectures,
  pretraining data size, scaling) and the headline results it reported, with the
  benchmark names and numbers.
- The scale: parameter counts of the model sizes, the largest 11B model, and the
  pretraining compute the paper reports. Anchor the largest figures to a
  comparison a general reader holds.
- What later work confirmed, corrected, or moved past (decoder-only scaling,
  instruction tuning). Where does T5's controlled comparison still get cited, and
  where does today's usage claim more than the paper showed?

Meet the floor with sources that change the interpretation, not padding: at least
6 sources, at least 3 primary, at least 1 secondary. Search for what breaks the
commission's angle and record it in Contradictions. Confirm every URL resolves to
the document's own page.
