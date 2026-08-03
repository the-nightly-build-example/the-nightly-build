# Evidence: the-evidence/alphafold (invocation 01)

The record strongly supports the commission's core claim: the 2021 Nature paper
and CASP14's own scoring measured one thing precisely — the accuracy of predicted
3D protein structures on a blind assessment — and that measurement was a large,
verifiable jump. The headline numbers are sourced firsthand from the paper (median
backbone accuracy 0.96 Å r.m.s.d.95 vs 2.8 Å for the next method) and from CASP14's
official results table (AlphaFold2 sum Z-score 244.02 vs 90.82 for the runner-up),
plus DeepMind's own CASP14 announcement (median 92.4 GDT; GDT explained on its 0–100
scale). The record is equally firm that the paper did NOT measure protein function,
folding dynamics, or the obsolescence of experimental structural biology: the paper
predicts single static chains, its authors flag low accuracy when sequence homologs
are scarce, and an independent 2024 evaluation (Terwilliger et al.) found even
very-high-confidence predictions carry about twice the coordinate error of experiment
and should be treated as "exceptionally useful hypotheses." The commissioned angle
holds and is not undermined; if anything the sources sharpen it, because DeepMind's
own blog is titled "a solution to a 50-year-old grand challenge" and the Nobel body's
prose says they "solve" the problem, while the formal Nobel citation is the narrow
"for protein structure prediction." Two thin spots: the brief's "~170,000 PDB training
structures" figure is NOT present in the main-text I could read (it lives in the
Supplementary Information I could not open), and the median-92.4-GDT figure is owned by
DeepMind's own announcement and the CASP14 assessment, not stated as a single median in
the Nature paper's readable body. Both are flagged below.

## Sources

```text
URL:         https://www.nature.com/articles/s41586-021-03819-2
             (open-access full text read at https://pmc.ncbi.nlm.nih.gov/articles/PMC8371605/)
Kind:        primary — the document itself. Jumper et al. author and own every claim
             about what AlphaFold does; DeepMind is the authoring party with the stake.
Establishes: What the 2021 paper reported and claimed. Title: "Highly accurate protein
             structure prediction with AlphaFold." Nature 596 (7873): 583–589, 15 Jul 2021,
             DOI 10.1038/s41586-021-03819-2. Corresponding authors John Jumper and Demis
             Hassabis; author affiliation DeepMind, London, UK (Martin Steinegger also
             Seoul National University). CASP14 accuracy; the "protein folding problem"
             scope; MSA/template inputs; Evoformer + structure module; pLDDT; the stated
             limits (shallow MSAs, single chains).
Paraphrase:  The paper presents a redesigned neural-network model, validated blind in
             CASP14, that predicts a protein's 3D structure from its amino-acid sequence
             with accuracy competitive with experiment in a majority of cases and far
             ahead of other methods. It defines its scope as the structure-prediction
             component of the protein-folding problem, open "for more than 50 years."
             Backbone median accuracy 0.96 Å r.m.s.d.95 vs 2.8 Å for the next best method;
             all-atom 1.5 Å (1.2–1.6) vs 3.5 Å. Inputs are the sequence, an MSA (multiple
             sequence alignment — the query lined up against evolutionarily related
             sequences, built with jackhmmer and HHblits), and templates (coordinates of a
             few homologous structures where available). The Evoformer block treats
             structure prediction as "a graph inference problem in 3D space in which the
             edges of the graph are defined by residues in proximity." A structure module
             then builds explicit 3D backbone coordinates. pLDDT (predicted local-distance
             difference test) is the per-residue confidence; low-pLDDT regions are
             low-confidence and often intrinsically disordered.
Locators:    Abstract (quoted below); "AlphaFold structures had a median backbone accuracy
             of 0.96 Å r.m.s.d.95" (Abstract); all-atom and 2.8 Å comparison in the opening
             Main paragraph; Evoformer/structure-module and MSA/template descriptions in the
             "AlphaFold network" Main section and Methods; pLDDT in Main text; MSA-depth
             limit (accuracy drops below ~30 sequences) and single-chain/complex limits in
             the "MSA depth and cross-chain contacts" section.
Quote:       "AlphaFold structures had a median backbone accuracy of 0.96 Å r.m.s.d.95"
             "leveraging multi-sequence alignments, into the design of the deep learning
             algorithm" (Abstract).
```

```text
URL:         https://predictioncenter.org/casp14/zscores_final.cgi
Kind:        primary — CASP's own, independent scoring. The Prediction Center (CASP
             organizers) ran the blind assessment and owns these rankings; this is the
             independent check on DeepMind's claims, not DeepMind reporting on itself.
Establishes: AlphaFold2's dominance in CASP14 by CASP's own Z-scores, independent of the
             paper's framing.
Paraphrase:  In the official CASP14 final Z-score table, group 427 (AlphaFold2) leads all
             groups with a summed Z-score of 244.02 (average 2.65). The next-best group,
             473 (BAKER, David Baker's group), sums to 90.82 (average 0.99). The gap is
             roughly 153 Z-score points across the assessed targets.
Locators:    CASP14 final Z-scores table, group 427 vs group 473; ~92 assessed
             targets/domains in the table.
Quote:       (numeric table; no prose quote)
```

```text
URL:         https://deepmind.google/blog/alphafold-a-solution-to-a-50-year-old-grand-challenge-in-biology/
Kind:        primary — DeepMind's own technical/announcement material (30 Nov 2020).
             Owns DeepMind's public framing and reports the CASP14 GDT figure.
Establishes: The median-92.4-GDT figure; a plain definition of GDT and its 0–100 scale;
             the "~90 GDT ≈ experimental" convention attributed to CASP chair John Moult;
             and DeepMind's own "a solution to a 50-year-old grand challenge" framing.
Paraphrase:  GDT (Global Distance Test) is CASP's main accuracy metric, ranges 0–100, and
             can be read roughly as the percentage of residues within a threshold distance
             of their correct position. Per Professor Moult, a score around 90 GDT is
             informally considered competitive with experiment. AlphaFold's CASP14 median
             was 92.4 GDT across all targets, an average error (RMSD) of about 1.6 Å,
             "comparable to the width of an atom."
Locators:    Body paragraphs on the CASP14 result and the GDT metric; page title carries
             "a solution to a 50-year-old grand challenge in biology."
Quote:       "our latest AlphaFold system achieves a median score of 92.4 GDT overall across
             all targets"; "a score of around 90 GDT is informally considered to be
             competitive with results obtained from experimental methods."
```

```text
URL:         https://www.nature.com/articles/s41586-021-03828-1
             (title, journal, authors, and full abstract read via Europe PMC core record,
             EXT_ID:34293799)
Kind:        primary — the companion database paper. Tunyasuvunakool et al. (DeepMind + EMBL-EBI)
             author and own the human-proteome coverage claims.
Establishes: The scale and the honest confidence limits of the first big AlphaFold release.
             Title: "Highly accurate protein structure prediction for the human proteome."
             Nature 596: 590–596 (2021), DOI 10.1038/s41586-021-03828-1.
Paraphrase:  Before this work, 17% of residues in human protein sequences were covered by an
             experimentally determined structure. AlphaFold was run across almost the entire
             human proteome (98.5% of human proteins). The resulting dataset covers 58% of
             residues with a confident prediction, of which 36% of all residues are very high
             confidence. The paper introduces metrics to flag likely-disordered regions and
             frames predictions as a way to "generate biological hypotheses."
Locators:    Abstract (full text quoted in Numbers section).
Quote:       "The resulting dataset covers 58% of residues with a confident prediction, of
             which a subset (36% of all residues) have very high confidence."
```

```text
URL:         https://deepmind.google/discover/blog/alphafold-reveals-the-structure-of-the-protein-universe/
Kind:        primary — DeepMind's own announcement (28 Jul 2022) of the AlphaFold DB expansion.
Establishes: The 200M figure and its date; the ~1M → 200M+ growth; EMBL-EBI partnership.
Paraphrase:  On 28 July 2022 DeepMind and EMBL-EBI expanded the AlphaFold Protein Structure
             Database by over 200x, from nearly 1 million structures to over 200 million,
             covering nearly all catalogued proteins known to science, freely available.
Locators:    Announcement body; date 28 Jul 2022.
Quote:       Growth described as "from nearly 1 million structures to over 200 million
             structures" covering "nearly all catalogued proteins known to science."
```

```text
URL:         https://www.nobelprize.org/prizes/chemistry/2024/press-release/
Kind:        primary — the Royal Swedish Academy of Sciences' official award citation.
Establishes: Exactly what the 2024 Chemistry Nobel was awarded for, and the precise wording
             (which is narrower than popular "AI solved biology" usage).
Paraphrase:  The Nobel Prize in Chemistry 2024 was divided: one half to David Baker
             (University of Washington, Seattle; Howard Hughes Medical Institute) "for
             computational protein design," the other half jointly to Demis Hassabis and
             John Jumper (both Google DeepMind, London) "for protein structure prediction."
             The press release's own explanatory prose, by contrast, says Hassabis and Jumper
             "have developed an AI model to solve a 50-year-old problem: predicting proteins'
             complex structures."
Locators:    Opening citation line; second paragraph ("They cracked the code...").
Quote:       "the other half jointly to Demis Hassabis ... John Jumper ... 'for protein
             structure prediction'"; "an AI model to solve a 50-year-old problem: predicting
             proteins' complex structures."
```

```text
URL:         https://www.nature.com/articles/s41592-023-02087-4
             (figures read from the open bioRxiv preprint v2:
             https://www.biorxiv.org/content/10.1101/2022.11.21.517405v2.full)
Kind:        primary — an independent evaluation. Terwilliger et al. (Los Alamos / New Mexico
             Consortium and collaborators, published Nature Methods 21: 110–116, 2024) own
             this finding and are outside DeepMind; this is the source that bounds the overclaim.
Establishes: That even the best AlphaFold predictions are not interchangeable with experimental
             structures, quantified, and that the authors class predictions as hypotheses.
Paraphrase:  Comparing AlphaFold predictions against experimental crystallographic maps and
             structures, Cα atoms in very-high-confidence regions differed from the matching
             crystal structures by a median of 0.6 Å, and about 10% of these differed by more
             than 2 Å — each roughly twice the discrepancy seen between two experimental crystal
             structures of the same thing solved in different space groups. The authors conclude
             predictions should be treated as "exceptionally useful hypotheses" and do not
             replace experimental determination.
Locators:    Abstract; map-model comparison of 102 AlphaFold predictions (Fig. 2).
Quote:       "about 10% of these differed by more than 2 Å, each about twice the values found
             for pairs of crystal structures ... We suggest considering AlphaFold predictions
             as exceptionally useful hypotheses."
Caveat:      The exact figures above are quoted from the bioRxiv v2 preprint; if a number is
             quoted verbatim in the article, confirm it against the published Nature Methods
             version, which may differ slightly. The finding is the same in both.
```

```text
URL:         https://www.nature.com/articles/d41586-020-03348-4
Kind:        secondary — Nature's news desk (Ewen Callaway, 30 Nov 2020) reporting on the
             CASP14 result. It repeats and frames; it does not own the underlying claim.
Establishes: That mainstream science press framed the result as "solving" protein structures —
             the popular framing the commission tests against the paper's actual scope. A
             repetition supports that the framing was made, not that "solved" is accurate.
Paraphrase:  The headline reads "'It will change everything': DeepMind's AI makes gigantic leap
             in solving protein structures," attributing the "change everything" line to a
             structural biologist. Useful as a live specimen of the "solved / will change
             everything" framing to contrast with the measured result.
Locators:    Headline and standfirst. (Article body was cookie-gated on fetch; the headline and
             deck, which carry the framing evidence, resolved.)
Quote:       "'It will change everything': DeepMind's AI makes gigantic leap in solving protein
             structures" (headline).
```

## Contradictions

- **"Solved" vs "predicted structure."** DeepMind's own CASP14 blog is titled "a solution
  to a 50-year-old grand challenge," and the Nobel press release's explanatory prose says
  Hassabis and Jumper built a model "to solve" the folding problem. But the formal Nobel
  citation is narrow — "for protein structure prediction" — and the Nature paper scopes
  itself to "the structure prediction component of the 'protein folding problem'," i.e.
  predicting the final static 3D coordinates, not simulating the folding process or dynamics.
  The looser "solved biology / solved folding" usage in circulation outruns all three
  primary framings. This is the commission's central point and the sources support it.

- **CASP organizers vs DeepMind framing.** CASP's contribution (predictioncenter.org) is a
  ranking (Z-scores) on blind targets; it establishes that AlphaFold2 was far ahead of the
  field on that specific test. The "competitive with experiment" and "solution" language is
  DeepMind's and the popular press's. Even the "~90 GDT ≈ experimental" convention is
  attributed in DeepMind's blog to CASP chair John Moult as "informally considered,"
  not a formal CASP verdict. The claim is real but softer than "as good as experiment."

- **Prediction vs experiment.** Terwilliger et al. (independent) directly bounds the
  "obsoletes wet-lab structural biology" overclaim: even very-high-confidence predictions
  carry ~2x the error of experiment and ~10% miss by >2 Å; they are hypotheses, not
  replacements. This does not contradict the paper (the paper claims accuracy "competitive
  with experimental structures in a majority of cases," not identity) but it contradicts the
  popular reading.

- **Function.** No source found — including the paper — claims AlphaFold predicts protein
  function or dynamics. The paper predicts structure; the human-proteome paper offers
  predictions as inputs to "generate biological hypotheses." Any "predicts function" claim in
  circulation has no support in the primary record. (Contradiction searched for and confirmed
  absent from the primaries, i.e. the overclaim is unsupported rather than disputed.)

## Numbers

```text
Figure: 0.96 Å median backbone accuracy (r.m.s.d.95)
Owner:  Jumper et al. 2021 (Nature paper, Abstract)
Scope:  Median over CASP14 assessed domains; r.m.s.d.95 = Cα RMSD over the best-covered 95%
        of residues. Next best method: 2.8 Å on the same measure.
```

```text
Figure: 1.5 Å all-atom accuracy (r.m.s.d.95), 95% CI 1.2–1.6 Å
Owner:  Jumper et al. 2021 (Main, opening paragraph)
Scope:  CASP14; best competing method 3.5 Å on the same measure.
```

```text
Figure: median 92.4 GDT overall across all targets
Owner:  DeepMind CASP14 blog (30 Nov 2020); the CASP14 assessment (Kryshtafovych et al.,
        Proteins 89:1607–1617, 2021) is the peer-reviewed owner of the assessment.
Scope:  CASP14, all targets. GDT is 0–100. NOT stated as a single median in the Nature
        paper's readable body; use the DeepMind blog (or the CASP assessment) as the owner.
Caveat: The CASP14 assessment PDF (escholarship copy) was image-only and could not be
        text-extracted; 92.4 is verified from DeepMind's blog, not from the assessment PDF.
```

```text
Figure: sum Z-score 244.02 (AlphaFold2, group 427) vs 90.82 (BAKER, group 473)
Owner:  CASP14 official results (predictioncenter.org/casp14/zscores_final.cgi)
Scope:  Summed over ~92 assessed CASP14 targets/domains; average Z 2.65 vs 0.99.
```

```text
Figure: "around 90 GDT ... competitive with results obtained from experimental methods"
Owner:  DeepMind CASP14 blog, attributed to Prof. John Moult (CASP chair)
Scope:  Informal convention, not a formal metric. Frames why 92.4 GDT was called a landmark.
```

```text
Figure: 17% of residues in human protein sequences had an experimental structure (before)
Owner:  Tunyasuvunakool et al. 2021 (Nature, Abstract)
Scope:  Human proteome, residue-level, pre-AlphaFold baseline.
```

```text
Figure: 98.5% of human proteins predicted; 58% of residues confident; 36% very high confidence
Owner:  Tunyasuvunakool et al. 2021 (Nature, Abstract)
Scope:  Human proteome. The 58%/36% figures are the honest ceiling: ~42% of residues are NOT
        confidently predicted, and low-confidence often marks intrinsic disorder.
```

```text
Figure: MSA depth below ~30 sequences → accuracy drops substantially
Owner:  Jumper et al. 2021 (Nature, "MSA depth and cross-chain contacts")
Scope:  Author-stated limit: orphan/low-homology proteins are the weak case.
```

```text
Figure: ~350,000 Uniclust30 sequences used for self-distillation training
Owner:  Jumper et al. 2021 (Methods, "Training regimen")
Scope:  Self-distillation set (model predicts these, high-confidence subset re-used to train).
        Distinct from the PDB experimental training set.
```

```text
Figure: >200 million structures (from ~1 million), 28 Jul 2022
Owner:  DeepMind AlphaFold DB blog (28 Jul 2022)
Scope:  AlphaFold Protein Structure Database; ~200x expansion, "nearly all catalogued proteins."
        By 2023–24 the DB reports coverage for 200M+ / 214M+ UniProt sequences.
```

```text
Figure: median 0.6 Å; ~10% of very-high-confidence Cα differ by >2 Å (≈2x experiment)
Owner:  Terwilliger et al. 2024 (Nature Methods 21:110–116; figures quoted from bioRxiv v2)
Scope:  102 AlphaFold predictions vs matching crystal structures/maps. Independent bound.
```

UNVERIFIED (brief-named, not found firsthand):
```text
Figure: ~170,000 PDB training structures
Owner:  Attributed to Jumper et al. 2021, but the string/number does NOT appear in the
        main-text I could read (PMC full text). It lives in the Supplementary Information,
        which I could not open. The main text gives only a training cutoff date
        ("maximum release date of 30 April 2018") and the ~350,000 self-distillation set.
Action: Writer should either source ~170,000 from the paper's Supplementary Information
        (verbatim) or use the verified figures instead: the Abstract's "around 100,000
        unique proteins" experimentally determined, and the ~350,000 self-distillation set.
```

## Source assets

```text
Asset: Figure 1 accuracy panels, Jumper et al. 2021 (Nature paper). The CASP14 backbone-
       accuracy panel (AlphaFold vs top-15 groups) and the r.m.s.d.-vs-competitors comparison.
Shows: The size of the jump in one image — AlphaFold's distribution sitting far below the
       field on error. Carries the "measured jump" half of the lesson better than prose.
Crop:  Retain the y-axis label and units (Å r.m.s.d.95 or GDT) and the AlphaFold-vs-field
       separation; a crop that drops the axis units is useless.
```

```text
Asset: A pLDDT-colored structure (blue = high confidence, orange/red = low), as used in
       Tunyasuvunakool et al. 2021 and across the AlphaFold DB (alphafold.ebi.ac.uk entries).
Shows: What "confidence" looks like — ordered domains in blue, likely-disordered tails in
       red. Makes the 58%/36% confident-residue numbers concrete and teaches pLDDT visually.
Crop:  Must keep the color legend/scale; the colors are meaningless without the pLDDT key.
```

```text
Asset: CASP14 final Z-score bar chart / table (predictioncenter.org/casp14/zscores_final.cgi),
       AlphaFold2 (427) towering over BAKER (473) and the rest.
Shows: The independent margin (244 vs 91) in CASP's own scoring, not DeepMind's.
Crop:  Keep the group labels (427 = AlphaFold2, 473 = BAKER) and the Z-score axis.
```

```text
Asset: Terwilliger et al. 2024 error-distribution figure (Fig. 2/4), predictions binned by
       pLDDT (>90, 80–90, 70–80, <70) against experiment.
Shows: That confidence tracks error but even the top bin is not error-free — the honest bound.
Crop:  Retain the pLDDT bins and the error axis in Å.
```

## Discarded

```text
URL: https://escholarship.org/content/qt3119w22w/qt3119w22w_noSplash_ecaec2fd788d46d6c7a48c2cf995da0a.pdf
     CASP14 assessment (Kryshtafovych et al.) open PDF — image-only scan, no text layer; could
     not extract quotes/figures. Its GDT figures are carried instead by DeepMind's CASP14 blog.
```

```text
URL: https://www.researchgate.net/publication/353412304_... (human proteome, ResearchGate)
     403 to the fetcher; superseded by the primary abstract via Nature/Europe PMC.
```

```text
URL: https://proteopedia.org/wiki/index.php/AlphaFold2_examples_from_CASP_14
     Tertiary wiki; not needed once DeepMind's blog and CASP's table supplied GDT primary sourcing.
```

```text
URL: nobelprize.org and api.nobelprize.org via WebFetch — 403 to the fetch user agent (host
     bot-blocking, not proxy policy: recentRelayFailures empty). The press-release page itself
     resolves in a browser and was read via a browser-agent request; the recorded URL is the
     source's own page.
```
