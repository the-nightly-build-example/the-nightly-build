# Commission: the-evidence/elmo

## The document

"Deep contextualized word representations," Peters, Neumann, Iyyer, Gardner,
Clark, Lee, Zettlemoyer (Allen Institute for AI / University of Washington),
NAACL 2018 (arXiv:1802.05365). It introduced ELMo (Embeddings from Language
Models). Best paper at NAACL 2018. The document people cite as the moment word
meaning in NLP stopped being fixed and started depending on context.

## The angle and the original work

The reader has the published lessons on word2vec (fixed word vectors) and BERT
(the model that took over NLP). ELMo is the missing hinge between them, and this
desk should read the actual paper. Teach what ELMo actually did: it ran a
two-layer bidirectional LSTM language model over a sentence and used its
internal states as features, so the vector for "bank" differed in "river bank"
and "bank account." It set new state of the art on six diverse NLP tasks at
once by being added on top of existing task models.

The honest reputation-vs-reality point (the desk's job): ELMo is remembered as
the start of the "pretraining era" / the ImageNet moment for NLP, but the exact
recipe it proposed, LSTM features frozen and concatenated into a task-specific
model, was displaced within months by BERT's fine-tune-the-whole-Transformer
recipe. What survived is the idea (contextual representations from a language
model pretrained on unlabeled text); what did not survive is ELMo's mechanism
(the biLSTM, the feature-based use). Show this from the paper's own method and
results, and from BERT's own paper positioning itself against ELMo.

Original work for the writer: separate the idea ELMo is credited with
(context-dependent word meaning from an LM) from the machinery it actually
shipped (a frozen biLSTM feeding features), and show that the field kept the
first and discarded the second within a year. State that sentence and show it
from the ELMo and BERT papers.

## What the lesson teaches (short list, in order)

1. The problem ELMo addressed: a fixed word vector gives "bank" one meaning
   everywhere. Link the published word2vec lesson for what fixed embeddings are;
   do not re-teach them. ELMo's claim: let the representation depend on the whole
   sentence.
2. How ELMo worked, plainly: a bidirectional LSTM language model (define
   language model = predicts the next/previous word) pretrained on a large text
   corpus; the internal layer states, combined per task, become the "contextual"
   word representation. Keep the biLSTM at the level the explanation needs; the
   reader has the LSTM lesson to link. No code.
3. The actual results and scale: six benchmark tasks (question answering =
   SQuAD, textual entailment = SNLI, semantic role labeling, coreference, named
   entity recognition, sentiment), the pattern of gains (relative error
   reductions), and that ELMo was added on top of each task's existing model
   rather than replacing it. Give the real numbers the paper reports; show the
   scale honestly.
4. What replaced it and what it left behind: BERT (2018) fine-tuned a
   Transformer end to end and cited ELMo as the feature-based alternative it beat;
   the idea (LM pretraining gives contextual representations) is now universal,
   the biLSTM-features recipe is not. Say plainly how usage today differs from
   what ELMo shipped.

Keep to these. Depth over breadth.

## Boundaries

- One document. Do not turn into a history of NLP or a BERT explainer. Name BERT
  and word2vec only to place ELMo.
- Taught ground to link, not re-teach: word2vec (fixed embeddings), LSTM
  (recurrence), BERT (the model that followed). All are published; link, do not
  re-teach.
- The "eclipsed by BERT" point is honest, but do NOT stage it as a final
  gotcha reveal (see recent-pattern notes). Build the idea/machinery split into
  the body's spine.

## Neighbouring articles this run (avoid overlap)

Tonight also runs the-instruments/mlperf, the-mechanics/hangman,
what-could-go-wrong/ai-environmental-cost, when-ai-breaks/babylon-health. No
overlap risk; this is the only paper-reading piece.

## Recent-pattern notes (habits to break)

the-evidence recently closed on a "the famous X was not the real X" reveal
(LSTM: "The LSTM that got famous was not the one from 1997"; backprop: "The
algorithm predates the paper that made it famous"). ELMo's angle (idea kept,
machinery discarded) is structurally tempting to stage the same way. Do NOT.
Build it into the spine; do not make the last body section a reveal of that
mold. Vary headings; recent leaned on "What X actually claimed/did" and "How
small the demonstrations were." Deks recently used comma-triads and "and"
continuations; write one lean dek with one concrete detail.

## Source obligations

lesson under the-evidence: min 6 sources, >=3 primary, >=1 secondary. Primary:
the ELMo paper (owner of its method and six-task numbers); the BERT paper
(Devlin et al. 2018/2019, arXiv:1810.04805) for how it positions against ELMo
and the fine-tuning vs feature-based distinction; the datasets/tasks' own papers
only if a specific number needs its owner (e.g. SQuAD). Secondary: reputable
retrospective coverage for the "ImageNet moment for NLP" framing, attributed
precisely, never for a number.

## Production record

Profile balanced. Recorded (policy "capable"): writing-coach Opus 4.8/low,
researcher Opus 4.8/high, writer Opus 4.8/medium, editor Opus 4.8/high. No
required directive; no deviation.

## Bookend link candidates

Background: `the-evidence/word2vec` (fixed embeddings), `the-evidence/bert` (the
model that followed), `the-evidence/long-short-term-memory` (the biLSTM's cell).
Go deeper (beyond this paper): the ELMo paper; the BERT paper. Lesson works for
a reader who opens none.
