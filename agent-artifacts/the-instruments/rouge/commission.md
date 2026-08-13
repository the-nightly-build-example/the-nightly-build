# Commission: the-instruments/rouge

## The measurement

ROUGE, the family of scores (ROUGE-N, ROUGE-L) used to grade automatic
summaries by overlap against human reference summaries. It is the number behind
most "this system summarizes well" claims for two decades, and it still appears
in model cards and papers. One lesson: how a ROUGE number is made and what it can
and cannot support.

## The angle

Teach where the number comes from, step by step, then show a real case where it
misled and what that cost.

- Who produces it and how: Chin-Yew Lin's 2004 paper defined ROUGE as
  recall-oriented n-gram overlap between a candidate summary and one or more human
  references. Explain ROUGE-N (overlapping n-grams) and ROUGE-L (longest common
  subsequence) in plain words, with a tiny worked example the reader can follow:
  count the overlapping units, divide by the reference's count. Make clear it is a
  string-overlap measure that never reads meaning.
- What the number can support: a fast, reproducible, cheap proxy that correlates
  with quality when systems are weak and references are good, which is why it
  became the field standard.
- What it cannot support, with a real, costed case. The strongest documented
  story: ROUGE rewards lexical overlap, so an extractive or lead-biased summary
  scores well while a faithful abstractive one can score poorly, and ROUGE does
  not measure factual faithfulness at all. Meta-evaluations (Fabbri et al.,
  "SummEval," 2021; Bhandari et al., 2020) found ROUGE correlates weakly with
  human judgments of quality and consistency. The cost: years of summarization
  research optimizing a metric that did not track what it was taken to measure,
  and fluent-but-unfaithful summaries clearing the bar. Establish the exact
  correlation findings from the primary meta-evaluations.

Keep the honest center: ROUGE is not worthless. It measures overlap under real
limits, and the reader should finish able to read a ROUGE score for exactly what
it is.

## Template and furniture

Lesson template. A tiny worked ROUGE calculation is the natural carrier and may
want a table; a comparison of ROUGE vs human ranking, if the evidence supplies a
clean series, could be a chart. Furniture is the writer's call with the editor.

## Sources and production

- Source policy: lesson under the-instruments, minimum 8 sources, at least 4
  primary, at least 1 secondary. Primary: Lin 2004 (the ROUGE paper), the SummEval
  and Bhandari meta-evaluations, and the original DUC/TAC evaluation context.
  Read the primary documents.
- Production policy (balanced), model/effort used this run: writing-coach capable
  (claude-opus-4-8) low; researcher capable (claude-opus-4-8) high; writer capable
  (claude-opus-4-8) medium; editor capable (claude-opus-4-8) high. Harness:
  claude-code-routine.

## This edition's neighbors (all distinct)

- On the-instruments shelf, bleu is the translation analogue and
  hallucination-rate covers faithfulness metrics. This piece is about the
  summarization overlap metric specifically. Do not re-teach BLEU; link it if the
  reader needs the contrast. Keep the faithfulness point as ROUGE's blind spot,
  not a re-run of hallucination-rate.
- The four other lessons tonight (lottery-ticket-hypothesis, multilingual-gap,
  emergent-misalignment, tessa-eating-disorder-chatbot) are unrelated in subject.

## Habits not to inherit

- Do not open Why-this-matters with the paper-wide "By the end you will know X.
  You will also see Y" formula, and do not model The Instruments' recent "every
  flagship ships an X score" opener.
- Do not land the takeaway on negative parallelism ("a high X score is worth what
  it measures ... It is not a reading of ..."). Deks: avoid the banned molds in
  the headline standard.

## Required contribution

The article assembles the metric's construction and the meta-evaluations into a
single account a reader can use to read any ROUGE number, separating what
overlap-with-a-reference can establish from the quality and faithfulness it is
often taken to prove.
