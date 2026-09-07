# Draft handoff: the-evidence/t5-transfer-learning (01)

## Original-work sentence

The article separates the two things T5 is cited for and shows they are not the
same claim: it teaches the text-to-text interface from the paper's own four
worked examples (down to the STS-B trick of printing a similarity score as a
string), then uses the paper's scattered results — the 18-of-24 win count set
against the three lost WMT tasks, and the encoder-decoder finding set against the
field's move to decoder-only — to draw the line between what the controlled
bake-off actually demonstrated at modest scale and the larger recipe the paper
gets quoted as having settled.

## Proof

Final `nb check` (links included) against the series library checkout:
`BLOCK: 0, WARN: 0` — verdict PUBLISHABLE. `nb stamp` wrote words=2200,
reading_minutes=10, sources=7. No warnings left standing.

## Notes on judgment calls (for the editor, not gaps)

- **Paper vs released figures**, per the brief's constraint, are kept distinct:
  the dek and the "750 gigabytes" subhead/body use the paper's ~750 GB (Sec. 2.2)
  and attribute it to the paper; the released ~806.87 GiB, ~365M examples, and
  6.21 TiB uncleaned figures are cited only to the TFDS artifact (source 4). The
  t5.1.0-vs-t5.1.1 checkpoint distinction is stated and cited to the repo
  (source 6), with the paper's own model figures cited to the paper.
- **Compute stated in tokens, not petaflop-days**, per the constraint: baseline
  ~34B tokens against BERT ~137B and RoBERTa ~2.2T, final ~1T (~32x baseline).
  No absolute compute figure is asserted, since the paper reports none.
- **"Cited for more than it showed" thread** is carried in the reckoning section
  and the takeaway: the three WMT losses (with the paper's own caveat quoted),
  the 2019-era/now-surpassed scores, the encoder-decoder vs decoder-only tension,
  and instruction tuning (Flan-T5) as later work the original paper did not study.
- **Figure 1 was rendered as a table, not captured as a source asset.** The four
  input/output pairs are text, and a cited two-column table (Input / Output)
  preserves all four verbatim and carries the shared-interface point in prose,
  which the evidence's asset note required (do not crop to a single example). No
  PDF source was in hand to capture the asset cleanly, and the table serves the
  argument the section spends. Second table shows Previous best vs T5-11B across
  GLUE/SuperGLUE/SQuAD and the three WMT rows so the wins and the translation
  shortfall sit in one view.
- **Recent-shape breaks:** the dek does not use the "<Authors>'s <year> paper did
  X, then measured Y" mold, the "own report can't/does X" headline, or the
  "measured it directly" / "in its own experiments" phrasings; the four named
  library lessons (attention, bert, gpt-3-few-shot, scaling-laws-kaplan) are
  linked as plain prose links, not numbered sources.

## Open questions

None. Evidence settled every claim the draft makes.
