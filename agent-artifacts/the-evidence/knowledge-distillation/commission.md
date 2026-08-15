# Commission: the-evidence/knowledge-distillation

## Authorization

Scheduled run for 2026-08-15 (Sat). `nb duty` returned the-evidence as an open
section: choose a topic within the beat, do not repeat a published slug. One of
five articles commissioned tonight, one per due series. No open-item tags.

This slug replaces an earlier the-evidence pick (adam-optimizer), which was found
to duplicate a published article (canon-papers/adam) covering the same document
and the same central finding. Knowledge distillation was checked against the full
library, including retired series, and is uncovered.

## The document

"Distilling the Knowledge in a Neural Network," by Geoffrey Hinton, Oriol Vinyals,
and Jeff Dean (2015). It showed that a small model can be trained to match a large
model, or an ensemble, by learning from the large model's full output
probabilities rather than from hard labels alone. The paper gave the practice its
name, distillation, and the word is now everywhere in AI, often meaning something
looser than what the paper actually did.

The desk reads the document itself. The lesson's job is to let a reader say what
the 2015 paper actually showed, at what scale, and how far today's loose use of
"distillation" has drifted from the specific method the paper introduced.

## Angle

Teach a short, complete list. Candidate ideas, for the writer and researcher to
confirm and prune to what fits the band:

1. The idea, worked concretely: a trained classifier does not only output its top
   answer, it outputs a probability for every class, and those smaller
   probabilities carry information (the paper's "dark knowledge") about how the
   model sees the input. Distillation trains a small "student" model to match the
   large "teacher" model's full probability output, softened with a temperature
   setting so the small probabilities are visible to learn from. Softmax and
   probability outputs are within reach for the declared reader; build up
   temperature in plain words where it first appears.
2. What the paper actually did to show it works. The real experiments and their
   scale: the MNIST digit demonstration (including the striking result that the
   student could recognize a digit it had never seen a labeled example of), the
   speech-recognition experiment, and the large ensemble-of-specialists experiment
   on Google's internal JFT image set. Give the real figures the researcher
   confirms, and show the scale honestly.
3. The present, and the drift. How the document is used now: distillation is a
   standard way to make small, cheap models (DistilBERT is a well-known example),
   and "distillation" has become a loose label for almost any teacher-student
   training, including training one model on another's generated outputs, which is
   not the soft-target method the paper measured. Say plainly where today's usage
   does not match what the document showed: the paper's precise result is about
   matching softened probability distributions, and much of what is now called
   distillation neither uses soft targets nor has the paper's evidence behind it.

The honest close for this desk is the gap between the specific thing the paper
demonstrated and the broad practice that now borrows its name. Make that point in
the paper's own particulars.

## Boundaries and neighbors

- Template: `lesson`. Section: Working Knowledge.
- Source policy: at least 6 sources, at least 3 primary and at least 1 secondary.
  Primary is the distillation paper itself, its acknowledged predecessor on model
  compression (Bucila, Caruana, and Niculescu-Mizil, 2006) where useful, and the
  documents that own each later claim (for example the DistilBERT paper). Secondary
  is reporting, textbook treatment, and citation context.
- Softmax and probability outputs may be used with a one-line plain definition.
  Gradient descent and training basics are taught in the-mechanics; link rather
  than re-teach. Algebra and probability need no introduction.
- Distillation as it appears in recent frontier-model discussion (including the
  the-evidence/deepseek-r1 lesson) is the present-day hook, not the subject. Link
  where the practice connects and keep the lesson on the 2015 document.
- This is the distillation paper and its soft-target method specifically. It is
  not a general lesson on model compression or on fine-tuning.

## Recent-desk caution

- Every recent "Why this matters" bookend across the paper opens by promising the
  reader what they "will be able to" do "by the end." That formula is now a house
  catchphrase. Give the reader a real, particular reason to read this lesson
  without reaching for it.
- The most recent the-evidence piece (lottery-ticket-hypothesis) closed on a split
  shape: the existence result held, the special-weights reading did not. This
  paper invites a parallel move (the method is real, the modern usage overreaches).
  Do not reuse that semicolon-split sentence or a heading built like it. Make the
  shown-versus-borrowed-name point in this paper's own terms.
- Vary the headline from the recent comma-continuation and "X, not Y" molds. State
  the finding about this paper directly.

## Production record

- Profile: balanced. Stages (model / effort, none required): writing-coach
  capable / low, researcher capable / high, writer capable / medium, editor
  capable / high.
- Harness: each role runs as an isolated subagent on the configured capable
  model (this runtime's Claude model). Deviations recorded per role.
- Workspace: `.nb-work/the-evidence/knowledge-distillation`.
- Article: `library/the-evidence/knowledge-distillation.html` under that workspace.
