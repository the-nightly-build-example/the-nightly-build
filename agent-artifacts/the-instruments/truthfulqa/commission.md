# Commission: the-instruments/truthfulqa

## Authorized work

Scheduled duty for 2026-08-11 returned `the-instruments` as an open section:
choose one measurement within the beat, do not repeat a published slug. This
commission selects TruthfulQA. One article, lesson template, one Article PR.

## The measurement and why it

TruthfulQA, from Lin, Hilton, and Evans, "TruthfulQA: Measuring How Models Mimic
Human Falsehoods" (2021, ACL 2022). It is the number behind public claims about
how "truthful" or "honest" a model is, reported on model cards and in launch
posts. This desk teaches how a number is made and what it can and cannot support.
The reader meets "scores X% on TruthfulQA" with no way to know that the questions
were adversarially selected to bait known human misconceptions, or that the
headline score is often graded by a fine-tuned language-model judge rather than a
person.

The beat's job: explain where the number comes from, step by step (who produces
it, from what data, by what procedure), then show what it can and cannot support,
including at least one real case where the number misled people and what that
cost.

## The angle

Two design choices make TruthfulQA a very specific instrument that its headline
use erases. First, the questions are adversarial by construction: the authors
kept questions that at least one large model answered falsely by imitating a
common human misconception, so the benchmark is built to make capable models look
bad, and "larger models are less truthful" is partly a property of that selection,
not a free-standing law. Second, the reproducible score is produced by
"GPT-judge," a model fine-tuned on the authors' human labels to grade truthfulness
automatically; a frozen judge scoring newer models it was never calibrated on is
a moving foundation under a fixed-looking percentage. Add the split between the
generative task and the multiple-choice variants (MC1/MC2), which are different
numbers reported under one name, and contamination risk as the questions
circulate.

The misled-people case: the "inverse scaling / bigger models lie more" reading
that the paper's own framing invited and that traveled widely, set against what
the adversarial construction and later work actually support. Teach the reader to
ask, of any TruthfulQA figure, which variant, graded how, on questions selected
how.

## Sources

Source floor: at least 8 sources, at least 4 primary, at least 1 secondary.

Direct the researcher to read, at minimum:
- The TruthfulQA paper (arXiv 2109.07958): the construction procedure, the
  817-question / 38-category design, the adversarial filtering, the human-eval
  protocol, the GPT-judge automation and its reported agreement with humans, and
  the MC1/MC2 definitions. Read the methods and appendices, not the abstract.
- The TruthfulQA code/data repository, for how GPT-judge is trained and how the
  official score is computed.
- At least two model cards or technical reports that report a TruthfulQA number
  (e.g., a GPT-4-class report, a Llama report) to show how the figure ships and
  what measurement detail is or is not disclosed alongside it.
- Independent secondary analysis or critique of TruthfulQA's construction or of
  the inverse-scaling reading, for context and contradiction.

Verify every figure (question counts, category counts, human-eval agreement,
any reported model scores, the judge's agreement rate) against the primary that
owns it. Record contradictions between the "bigger = less truthful" reading and
the evidence. Distinguish generative vs multiple-choice numbers explicitly.

## Course placement and neighbors

The library holds `the-instruments/hallucination-rate` (Vectara summary
faithfulness), `the-instruments/llm-as-a-judge`, `the-instruments/mmlu`,
`the-instruments/glue`, and `the-mechanics/hallucination`. TruthfulQA is a
distinct construct from the Vectara hallucination leaderboard (imitative
falsehoods vs summary faithfulness) and from llm-as-a-judge (which teaches the
judging method in general); link them in Background rather than re-teaching. Do
not re-explain what a language-model judge is beyond what this lesson needs; link
`llm-as-a-judge`. Tonight's other new articles do not collide.

## Production policy

Profile `balanced`; no directive `required`. Plan: coach low, researcher high,
writer medium, editor high; model class `capable`. Harness `claude-code-routine`.
Model Claude Opus 4.8. No required directive traded down.

## nb-meta

Date 2026-08-11. Harness `claude-code-routine`. Model `Claude Opus 4.8`. Three
descriptive tags, writer's choice (no tag fragments configured for this open
series).

Recent habits to break travel with the writer brief.
