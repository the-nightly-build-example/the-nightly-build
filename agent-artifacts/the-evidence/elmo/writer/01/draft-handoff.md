# draft-handoff: the-evidence/elmo (writer 01)

## Original-work sentence

The article splits ELMo's contribution into two parts that the source papers
state but never separate for a reader: the idea (a word's representation should
come from a language model pretrained on unlabeled text) and the method that
delivered it (a frozen two-layer biLM whose layer states are weighted and
concatenated as features), then shows from ELMo's own results and BERT's own
positioning that the field kept the first and dropped the second inside a year.
That split is stated in the mechanism section and carried through the six-task
results, the credit correction, and BERT, so it lands as the spine rather than a
closing reveal.

## Proof status

- `./nb stamp` written: words=1967, reading_minutes=9, sources=6.
- `./nb check ... --no-check-links`: BLOCK: 0, WARN: 0, PUBLISHABLE.
- `./nb check ...` (with links): BLOCK: 0, WARN: 0, PUBLISHABLE.
- No warnings left standing. Four sentence-density warnings from the first pass
  were fixed by splitting the enumerated-tasks sentence, the Ruder sentence, a
  takeaway sentence, and the BERT-complaint sentence.

## Notes for the editor

- "machinery" is banned max 0 in `press/banned-terms.yaml`. The brief and
  commission use "idea vs machinery"; the article renders it as "the idea vs the
  method / the delivery it shipped" throughout. Zero uses of the banned word.
- Sharpenings applied: ELMo is credited with making language-model pretraining
  work broadly (six tasks at once), not with inventing contextual
  representations. CoVe (2017) and ULMFiT (2018) are weighed in the
  "not-first-not-alone" section as the material credit contradictions. The
  "ImageNet moment" phrase is attributed to Ruder (The Gradient, July 2018) and
  explicitly applied to ELMo + ULMFiT + the OpenAI transformer jointly, not to
  ELMo alone.
- Model size uses the architecture spec only (two biLSTM layers, 4,096 units,
  512-dim projections, char input, 10 epochs on the one-billion-word corpus,
  ~30M sentences). No single parameter total is claimed, per the evidence limit.
- The six-task table carries the paper's own baseline, ELMo, prev-SOTA and
  relative error-cut columns. The "error cut" is stated in the caption and prose
  as the reduction in the *paper's own baseline* error (not vs previous SOTA),
  because the ELMo Table 1 "increase" is measured over that baseline. Keeping the
  baseline column is what makes the relative figures internally consistent.
- No source asset or chart used. The built data table already carries the
  six-task result the record's Table 1 asset would show, and the polysemy point
  is carried in prose by the "bank"/"play" example; a screenshot would duplicate
  the table without adding evidence.
- word2vec, LSTM, and BERT are linked at first use in prose and in the Background
  bookend, not re-taught and not numbered as sources.

## Open questions

None blocking. One thing the editor may want to weigh: the evidence records no
primary claim that ELMo's feature-based recipe stayed competitive after BERT
(searched, not found). The article states displacement, not persistence, and
does not assert a counter-side that the record does not support.
