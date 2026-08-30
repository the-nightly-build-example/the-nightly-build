# researcher brief: the-instruments/simpleqa (01)

Inputs:
- editorial-direction.md (house standard, citation rule, the reader, The
  Instruments series prompt)
- this brief

Output: researcher/01/evidence.md

## Subject
SimpleQA, OpenAI's short-form factuality benchmark. Primary document: "Measuring
short-form factuality in large language models" (Jason Wei et al., OpenAI,
released 30 October 2024), plus the SimpleQA release post and the public dataset
/ grader. Read the paper and the dataset documentation in full first.

## Questions the evidence record must answer
1. What SimpleQA is and who made it: exact release date, authors/lab, and the
   stated purpose.
2. How the number is built, step by step: how many questions (the exact count),
   how questions were written and by whom, the criterion for inclusion (single,
   indisputable, unchanging answer), and how they were verified (independent
   verification by separate people). Record whether questions were selected to be
   adversarial / hard for a reference model, and exactly how.
3. The grading procedure: that a model grader classifies each response as
   correct, incorrect, or not-attempted, and the exact definitions. The metrics
   reported: overall percent correct, and the "correct given attempted" (and any
   F-score) that rewards calibrated abstention.
4. Real reported scores, each with its owner: SimpleQA numbers OpenAI reported
   for its own models (e.g. GPT-4o and the o1 family), and any SimpleQA figures
   reported in other labs' model cards. Give each figure with the exact model,
   the metric, and the source that owns it. Note that absolute scores are low by
   design.
5. The misled case: find a concrete instance of a SimpleQA score being reported
   or read as a general accuracy or hallucination rate, and what that
   misreading implied that the benchmark does not support. If the cleanest case
   is the structural misreading rather than a single named article, document the
   structural case precisely (adversarial selection + abstention scoring make the
   raw percent non-representative) and cite the paper's own cautions.
6. Contrast, for the Background distinction: what TruthfulQA measures instead
   (common human misconceptions) and why a SimpleQA number is not a TruthfulQA
   number. One precise paragraph, sourced to both papers.
7. Contradictions / limits: record the benchmark's own stated limitations
   (short-form only; not representative of typical use; grader reliance).

## Source policy for this article
At least 8 sources; at least 4 primary, at least 1 secondary. Primaries: the
SimpleQA paper, the dataset/grader documentation, the TruthfulQA paper (for the
contrast), and lab model cards that report a SimpleQA score (each owns its
number). Classify each and say why.

## Source assets
Name any exact visual worth using (e.g. a results table with the correct /
not-attempted / incorrect breakdown, or the calibration figure), in the evidence
asset shape. No crop coordinates.

## Focus / risk
The two distinctive ideas — adversarial/hard selection and abstention-aware
scoring — are the lesson. Verify both against the primary, not a summary. Confirm
every reported score against the model card or paper that owns it, not against
reporting that quotes it.
