# Commission: the-mechanics/memorization

## Authorized work
Scheduled run for 2026-08-06. `nb duty` returned `the-mechanics` in open mode.
One article this edition; process this one only. Topic verified absent from the
full published-slug list recorded below.

## Subject
The behavior: ask a chatbot for the opening lines of a famous book, a poem, or a
passage, and it can reproduce them word for word; in documented cases models have
regurgitated long verbatim passages of training text. Work backward from that
behavior to its cause, the series' way. No code.

The cause to reach, step by step:
- The model's weights are fit to a training corpus, and for some strings the
  training signal drives the model to reproduce the exact sequence rather than a
  paraphrase. That is memorization: the model has, in effect, stored a specific
  string in its parameters and can emit it verbatim.
- Why it happens: two settled drivers. (1) Duplication — strings that appear many
  times in the training data are far more likely to be emitted verbatim; teach
  this with a real figure from the extraction/memorization literature. (2) Scale —
  larger models memorize more of their data. Explain in plain words why gradient
  descent on next-token prediction stores some sequences exactly (they reduce loss
  to near zero) while most content is generalized.
- Worked example / real case: the extraction-attack results (Carlini et al. 2021
  extracting verbatim training data from GPT-2; Carlini et al. 2023 quantifying
  memorization) and/or the New York Times v. OpenAI regurgitation exhibits, with
  real numbers (how many memorized examples, what fraction, the duplication
  threshold). Give the reader a concrete sense of scale.
- Reach ground and mark it: settled engineering (models memorize some training
  sequences; duplication and scale increase it; deduplication reduces it) versus
  open/graded questions (the exact boundary between memorization and
  generalization; how much a given deployed model has memorized; whether
  "memorization" and "understanding" are even separable). Mark each.

Keep to two or three ideas taught completely: (1) verbatim output means the string
is stored in the weights, not looked up; (2) duplication and scale drive it;
(3) why that is different from retrieval and from hallucination, and where the
ground is.

## Required contribution
Give the reader the actual chain from a word-for-word quote to a specific
sequence stored in the weights by next-token training, with real extraction
numbers, so they can explain why a model can quote text it never "looked up" and
distinguish that from retrieval (RAG) and from hallucination.

## Boundaries / do not repeat
FULL published the-mechanics slugs: attention, autoregressive-generation,
gradient-descent, hallucination, in-context-learning, instructions-are-data,
knowledge-cutoff, letter-counting, losing-the-thread, nondeterminism,
over-refusal, prefill-and-decode, reading-images, retrieval, reversal-curse,
sampling-temperature, sycophancy, tool-use, word-embeddings. Memorization is
unrepresented. Keep it DISTINCT from three neighbors and link them as Background,
not re-teach: retrieval (RAG looks text up at query time from an external store —
memorization is the opposite: the text is in the weights), hallucination (making
plausible text up — memorization is emitting real stored text), and
gradient-descent (the training mechanism it can link for how weights are fit).

## Template & policy
- Template: lesson; body 1200-2200 words; bookends fixed. No code.
- Tags: none (`--tag` unused); editorial `data-nb-tags` are the writer's choice.
- Source policy: min 8 sources, at least 4 primary, at least 1 secondary.
- Balanced profile, model "capable", no `required`. Harness: claude-code-routine.
  Efforts: coach low, researcher high, writer medium, editor high.

## Neighboring articles this edition
the-evidence/gans; the-instruments/glue; what-could-go-wrong/sandbagging;
when-ai-breaks/facebook-myanmar. No subject overlap.

## Recent shapes to break (habits, not rules)
Recent the-mechanics headlines use the "A chatbot <verb>s your <thing>" opener
(reading-images, retrieval, prefill-and-decode all start "A chatbot ..."). Do NOT
open the headline with "A chatbot". Let the headline state the mechanism finding.
Vary heading cadence away from comma-and pairs. These travel to the writer.
