# Commission: the-evidence/word2vec

## Authorization
Scheduled run for 2026-08-08 (Sat). `nb duty` returned the-evidence as an open
section: choose a topic within the beat, do not repeat a published slug. Verified
against the FULL published shelf (21 slugs); `word2vec` is not among them and is
not editorially covered by any existing the-evidence article. One article only.
Template `lesson` (series-pinned).

## Subject
The 2013 word2vec papers by Tomas Mikolov and colleagues at Google: "Efficient
Estimation of Word Representations in Vector Space" (Mikolov, Chen, Corrado, Dean;
arXiv:1301.3781) and its companion "Distributed Representations of Words and
Phrases and their Compositionality" (Mikolov, Sutskever, Chen, Corrado, Dean;
NeurIPS 2013, arXiv:1310.4546). The document that made "word vectors" and the
king - man + woman = queen analogy famous.

## Angle (the desk's shape: what the document is, what it actually did, its true scale, then the present)
- What it is and why it became famous: cheap, shallow models (CBOW and skip-gram)
  that learn a vector per word from raw text by predicting neighboring words, and
  the striking result that simple vector arithmetic on those vectors recovers
  analogies. State who wrote it and where.
- What it actually did, with honest scale: the training procedure (predict-context,
  negative sampling / hierarchical softmax in the companion paper), the exact
  analogy benchmark (the Google analogy set, ~19,544 questions across semantic and
  syntactic categories), the reported accuracy on it, vector dimensionality, and
  the corpus size (report the real numbers, e.g. the ~1.6B-word and larger corpora
  and the 6B-word Google News set for the companion). Show that "king - man +
  woman = queen" is a measured accuracy on a defined test, not magic.
- The present: how word2vec is cited today (as the origin of embeddings, invoked in
  arguments about whether models "understand meaning"), what held up (dense
  distributed word representations became foundational; the embedding idea lives
  inside every current model), and what later work corrected (the analogy result is
  weaker and more method-dependent than the shorthand implies - later analyses
  showed the arithmetic often excludes the input words and is sensitive to
  normalization; GloVe and contextual embeddings followed). When today's usage
  overreaches the paper, say so.

## Required contribution
The reader can say what word2vec measured, on what test, at what scale, and can
separate the demonstrated analogy accuracy from the "vectors capture meaning"
folklore. Reported fact (benchmark, corpus, accuracy) stays distinct from later
synthesis. Contested framing (does arithmetic really "do" analogies) is steelmanned
and weighed against later critiques.

## Sources and policy
Source policy (lesson/the-evidence): min 6 sources; primary >= 3, secondary >= 1.
Primaries: both word2vec papers (1301.3781 and 1310.4546); a primary for the
later critique of the analogy method (e.g. Levy & Goldberg, or the "Linguistic
Regularities" / analysis papers that examined the arithmetic). Secondary reporting
only for context. Every claim about what the papers did comes from the papers.

## Boundaries
This course already teaches embeddings as a mechanic (the-mechanics/word-embeddings)
and related ideas (attention, autoregressive-generation). Link, do not re-teach:
this is a DOCUMENT lesson about what the word2vec papers say and proved, not a
from-scratch explainer of what an embedding is. No code. Algebra assumed.

## Neighboring articles this edition (read as one paper, avoid overlap)
the-instruments/needle-in-a-haystack, the-mechanics/why-replies-stop,
what-could-go-wrong/data-poisoning, when-ai-breaks/optum-health-algorithm. This
piece owns the founding embeddings document; keep it to the papers.

## Habits not to inherit (recent the-evidence shapes)
Recent pieces (resnet, gans, atari-dqn, alexnet) open on "the result beneath the
<hype> headline" and run 5-6 declarative-claim headings, often pairing nb-figure
with nb-math. Do not reuse that opener mold or default to figure+math; name
headings from these papers' own steps and choose furniture (a small table of
analogy-benchmark accuracies may serve) from this document's needs.

## Harness and model
harness `claude-code-routine`; model `claude-opus-4-8` for every role. Balanced
production policy; per-role effort not independently settable in this harness
(mechanism deviation only, model unchanged).
