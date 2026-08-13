# Draft handoff: the-instruments/rouge (writer 01)

## Original work

The article works one ROUGE score by hand on a six-word pair and then reuses
that same tiny example to reconcile the field's two apparently opposed
faithfulness findings, SummEval's moderate consistency correlation and Maynez's
near-zero faithfulness correlation, into one rule a reader can carry: overlap
tracks faithfulness only where summaries copy their source, and not at all where
they reword it. The evidence record states those findings separately and flags
the reconciliation; the article builds the worked walkthrough and the single
applicable rule that let a reader read any reported ROUGE number.

## Proof result

`./nb check ... --series the-instruments --library /home/user/library-checkout`
(links included) returns `BLOCK: 0`, `WARN: 0`, verdict PUBLISHABLE. Stamped at
2006 words (band 1200-2200), 9 min, 8 sources.

Warnings intentionally left: none. The first proof raised five warnings, all
resolved rather than accepted:

- W-CITE-ORDER: Lin was cited before the BART card, so the source list was
  renumbered to first-citation order (Lin now source 1, BART source 2).
- Four W-SENTENCE-DENSITY warnings: the Graham, NIST/DUC, lead-baseline, SummEval
  dimension, and Kryscinski sentences were split into shorter sentences with the
  figures and quotations unchanged.

## Reframe compliance (this round's focus)

- No general "ROUGE correlates weakly with human judgment" claim. The dimension
  picture is kept distinct in a SummEval Kendall-tau table and prose: weak on
  coherence and relevance, confounded (low-abstractiveness) on consistency,
  ROUGE-L weak throughout.
- Meaning-blindness carried by Lin's own reversed-sentence example (ROUGE-2 = 1/3
  for both the correct and the reversed candidate; ROUGE-L 0.75 vs 0.50 noted as
  a surface-order by-product). The headline names ROUGE-2 specifically, not ROUGE
  in general, to stay accurate.
- Faithfulness stated as "ROUGE does not track faithfulness," never "rewards the
  unfaithful," with Maynez's best-ROUGE-and-most-faithful model (BERTS2S) used as
  the explicit guard.
- Graham cited for variant fragility (0.79 to 0.29 across 192 variants, standard
  variants suboptimal, BLEU matching the best ROUGE), not for weak correlation.
- Bhandari not cited, avoiding the miscite.
- Sai et al. 2022 is the secondary, used for the field's outside characterization
  and the meaning-insensitivity of LCS matching, not for any standalone
  correlation number.
- BLEU and the faithfulness/hallucination neighbors are prose links to the
  existing lessons, not numbered sources.

## Open evidence or voice questions

None blocking. One deliberate choice for the editor's awareness: no source asset
was captured. The evidence offered several (Maynez Fig. 1, SummEval and Lin
tables), but the two hand-built tables and the worked arithmetic carry the
argument, and the piece reads as a continuous lesson without a captured figure.
If the editor wants the "fluent but unfaithful" case shown rather than counted,
Maynez Fig. 1 is the asset to add.
