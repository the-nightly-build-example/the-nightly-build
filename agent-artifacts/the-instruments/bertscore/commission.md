# Commission: the-instruments/bertscore

## Assignment
Teach BERTScore, the metric from "BERTScore: Evaluating Text Generation with
BERT" by Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and
Yoav Artzi (ICLR 2020; arXiv:1904.09675), as one lesson on the Instruments desk.
Template: lesson. Publication date: 2026-09-13.

## Why this number, now
The Instruments desk has taught the two older ways to score generated text by
word overlap (`the-instruments/bleu`, `the-instruments/rouge`) and the newest way,
a model grading a model (`the-instruments/llm-as-a-judge`). It has not taught the
middle generation that is still reported constantly in machine-translation and
summarization comparisons: matching by meaning using contextual embeddings.
BERTScore is that number. Closing this gap completes the reader's picture of how
a machine decides that one generated sentence is "closer" to a reference than
another.

## The angle (the desk's arc)
Explain where the number comes from, step by step: a pretrained encoder turns
each token of the candidate and the reference into a context-dependent vector,
every candidate token is greedily matched to its most similar reference token by
cosine similarity, and those similarities are averaged into precision, recall,
and an F1 (with an optional idf weighting and an optional baseline rescaling).
Then show what the number can and cannot support, and give at least one real case
where it misled: the rescaling that makes raw scores look tiny or negative and is
not comparable across setups; the fact that two "BERTScore" numbers computed with
different underlying models or versions are not the same measurement; and its
inheritance of the encoder's blind spots (it rewards surface semantic overlap and
can miss negation or a flipped fact the way its encoder does).

## What the reader already holds — do not re-teach, link instead
- Word-overlap metrics and their weaknesses: link `the-instruments/bleu` and/or
  `the-instruments/rouge` in Background.
- What a contextual embedding is (a word's vector redrawn per sentence) and BERT:
  link `the-mechanics/word-embeddings` and/or `the-evidence/bert` rather than
  re-teaching embeddings from scratch. Define cosine similarity in one plain line
  where it first appears; do not build up linear algebra.
- Precision/recall/F1: the reader has met F1 (`the-instruments/f1-score`); recall
  it in a phrase, do not re-teach.

## Research directions (researcher owns depth)
1. The exact recipe from the paper: contextual embeddings from a pretrained
   encoder, greedy token matching by cosine similarity, precision/recall/F1,
   importance (idf) weighting, and the baseline rescaling. What the paper claims:
   higher correlation with human judgment than BLEU/ROUGE/METEOR on which tasks
   (machine translation WMT, image captioning), and by how much.
2. What it cannot support and where it misled: the rescaling caveat (rescaled
   scores are readability-only, not comparable across models/languages/versions),
   non-comparability of BERTScore numbers computed with different encoders or
   library versions, and documented failure modes (insensitivity to certain
   meaning-changing edits; adversarial or gamed inputs; bias inherited from the
   encoder). Find a concrete case or study, not a general worry.
3. How it is used in public now: reported alongside BLEU/ROUGE in translation and
   summarization papers and leaderboards; the hash/version reporting the authors
   ask for and whether people follow it.
4. A worked example with real numbers: a candidate/reference pair where word
   overlap and BERTScore disagree, or the rescaling turning a "0.9-ish" raw
   similarity into a small rescaled number, so the reader sees the gears.

## Contradictions to probe
Whether BERTScore's human-correlation advantage holds across tasks and later
studies, versus results where it is no better than cheaper metrics or is
outperformed by learned metrics (e.g., COMET, BLEURT). Record disagreement in
full.

## Sources
Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Primary: the
BERTScore paper, the metric's own documentation/repository for the rescaling and
versioning behavior, and papers that own any critique or comparison figure.
Secondary: reputable context only where no primary owns the point.

## Boundaries
No code. Teach only the metric; do not turn the lesson into a survey of every
text-generation metric. One number, its gears, its limits, one misleading case.

## Production policy (balanced; none required)
writing-coach model capable/effort low; researcher capable/high; writer
capable/medium; editor capable/high. "capable" is served by the run's default
subagent model (Opus-class); record the actual writer model in nb-meta.

## Neighbors in this run
the-evidence/mamba, the-mechanics/speech-to-text-hallucination,
what-could-go-wrong/capability-elicitation, when-ai-breaks/retinopathy-field-study.
No overlap.

## Habits from the recent record not to inherit
- Instruments headlines lean hard on the "a [metric] can hide / a [metric]
  misled" mold and on a single dramatic number. Find this piece's own headline.
- Keep the arc (where the number comes from / what it cannot support / a case
  where it misled) but name sections for BERTScore, never with stock labels.
