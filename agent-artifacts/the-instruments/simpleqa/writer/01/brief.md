# writer brief: the-instruments/simpleqa (01)

Inputs:
- editorial-direction.md (house standard, the paper's voice, The Instruments prompt)
- writing-coach/01/voice-guide.md (how this piece should sound; exemplar passages)
- researcher/01/evidence.md (the complete claim set; use the Numbers section exactly)
- library/the-instruments/simpleqa.html (the initialized article to edit)
- .nb-context/ (effective template contract, runtime assets, furniture catalogs)

Output: writer/01/draft-handoff.md
Article: /home/user/the-nightly-build/.nb-work/the-instruments/simpleqa/library/the-instruments/simpleqa.html
Proof: ./nb check .nb-work/the-instruments/simpleqa/library/the-instruments/simpleqa.html --series the-instruments --library /home/user/library-checkout

## This round's focus
Teach how the SimpleQA number is built (adversarial selection: a question kept
only if at least one of four GPT-4-class completions was wrong; abstention-aware
scoring: correct / incorrect / not-attempted, plus correct-given-attempted), then
land the "real case where the number misled" as concrete content, not a generic
caution. The misled case is first-hand and strong: an OpenAI system card files
SimpleQA under "Hallucination Evaluations" and renames the incorrect share a
"hallucination rate," and reporting carries "GPT-4.5 hallucinated 37% of the
time" — when the set is deliberately hard, obscure-fact recall and abstention is
scored separately.

Attribution flags from the evidence record (get these exactly right in display
text and citations):
- The 62.5% / 37.1% GPT-4.5 SimpleQA figure comes from OpenAI's simple-evals
  leaderboard, NOT the GPT-4.5 system card's hallucination table (that table uses
  PersonQA). Attribute it to simple-evals.
- Absolute scores are low by design ("GPT-4o and Claude both score less than
  50%"). The same model's score differs a few points across snapshots/evaluators
  (e.g. GPT-4o 38.2 / 0.38 / 38.8) — this refines, not weakens, the lesson.
- TruthfulQA contrast (imitative human misconceptions, 817 questions) is sourced
  to both papers; use it only for the Background distinction.

Link the-instruments/truthfulqa, the-instruments/hallucination-rate,
the-instruments/llm-as-a-judge, the-mechanics/hallucination, and
the-mechanics/false-confidence in Background at first use rather than re-teaching.

## Recent habits to break (do not inherit these from recent pieces)
- Do not end the "Why this matters" opener with "By the end you will know / be
  able to …". Let the takeaway resolve the opener's setup.
- Do not open on a generic second-person everyday scene as a reflex.
- Check the dek against spec/headlines.md's banned molds: no comma-triad ("A, B,
  and C") — the recent the-instruments dek (mmlu-pro) was exactly that; no
  two-clause "and" contrast; no atmospheric colon subtitle.
- Write headings in this benchmark's own nouns; vary how they are built; a reader
  skimming only the headings should reconstruct THIS argument.
