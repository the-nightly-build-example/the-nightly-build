# Draft handoff: the-evidence/backpropagation (01)

## Original work

The article separates what the 1986 paper actually demonstrated (that a simple
weight-update rule makes hidden units build their own useful features, made
concrete on the family-tree net whose six units learned nationality,
generation, and family branch) from the algorithm it is popularly credited with
inventing, by reading the two 1986 documents against the Linnainmaa and Werbos
priority primaries and the 2014 saddle-point result, and it fixes the scale in
the sweep and pattern counts the papers report rather than a compute figure they
never state. The evidence record holds those claims and cautions separately; the
article is where the priority split and the observation-vs-explanation reading
become one thing a general reader can carry.

## Proof

- Command: `nb check .../the-evidence/backpropagation.html --series the-evidence
  --repo /home/user/the-nightly-build` (links included).
- Result: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** All six source URLs
  resolved under the on-by-default link check.
- Three W-SENTENCE-DENSITY warnings surfaced on the first pass (the opener's
  closing sentence, the scale section's compute-anchor sentence, and the
  takeaway's central sentence) and were all resolved by splitting; none left
  standing.
- `nb stamp`: words=2141, reading_minutes=9, sources=6 (band 1200-2200).
- Built the preview site: both source assets copy into
  `library/the-evidence/backpropagation/` and both `nb-figure` blocks resolve
  their `backpropagation/asset-N.png` references.

## Furniture and assets

- Two source assets, captured with `nb asset pdf` from the open Nature
  facsimile: Fig. 1 in-article = Nature Fig. 4 (the six hidden units' learned
  features, p.535), the paper's contribution made visible; Fig. 2 in-article =
  Nature Fig. 1 (the fully-labeled symmetry net, p.534), the "small net, legible
  solution" point. Each figure's argument spends what it shows.
- One `nb-table` of the four demonstrations with sizes and training lengths,
  cited to the Nature letter and the PDP chapter.

## Notes for the editor

- **Source hrefs.** The Nature letter (s1), the PDP chapter (s2), and Linnainmaa
  (s3) are all gated at their publishers, so each source links the open
  facsimile the researcher actually read (minesparis, stanford/jlmcc, baulab),
  which the reader can open and which the link check passed. Publisher of record
  is still named in the entry text.
- **Symmetry ratio.** The evidence paraphrase says "two weights ... in ratio
  1:2:4"; the printed Nature Fig. 1 caption and the captured figure show three
  weights per side of the midpoint (6 inputs, 3 per side) in that ratio, so the
  article says "three." Flagging the record's wording, not a departure from it.
- **Arithmetic in prose.** "twenty-eight years later" = 1986 to Dauphin et al.
  2014; the early-1970s priority dek spans Linnainmaa's 1970 thesis and Werbos's
  1974 thesis.

## Open questions

None blocking. The evidence record supported every claim the piece rests on; no
researcher request was needed.
