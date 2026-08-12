# Commission: the-evidence/grokking

## Authorized work

Scheduled duty for 2026-08-12 returned `the-evidence` as an open section: choose
one document within the beat, do not repeat a published slug. This commission
selects the grokking paper. It is one article, on the lesson template, delivered
as one Article PR.

## The document and why it

Alethea Power, Yuri Burns, Igor Babuschkin, and colleagues (OpenAI), "Grokking:
Generalization Beyond Overfitting on Small Algorithmic Datasets" (2022, arXiv
2201.02177; presented at the ICLR 2022 workshop on mathematical reasoning). The
paper reported a startling training curve: a small network trained on a tiny
algorithmic task memorized its training set almost immediately, sat near chance
on held-out data for a very long time, and then, long after it had apparently
finished learning, snapped to near-perfect generalization. The authors named the
effect "grokking." The word travels now well past the experiment: it is invoked
whenever a large model seems to improve suddenly, as evidence that networks
harbor hidden phase changes and that more training can unlock generalization out
of nowhere. This desk reads the document so the reader knows what it actually
measured.

The beat's job here: state what the paper is, who wrote it, and why it became
famous; walk through what it actually did (the tasks, the model, the data
fraction, the number of optimization steps to generalization, the exact figures)
with honest scale; then bring it to the present (how grokking is cited in
arguments about emergent abilities and large-model training, what later work
established about its cause, and whether the everyday usage matches the result).

## The angle

Grokking is a real, reproducible phenomenon and a small one, and the reader
should be able to hold both. What the paper showed is delayed generalization on
toy algorithmic datasets: a small transformer trained on problems like modular
arithmetic (e.g. a mod-p operation table), given only a fraction of the table as
training data, with weight decay, generalizes to the rest only after orders of
magnitude more optimization steps than it needed to fit the training set. That is
a controlled, deliberately minimal setup, not a frontier training run. The fame
is the extrapolation: "models grok" as a general claim about why big systems
improve, which the paper did not test and its scale cannot carry.

Two things later work established that the article must carry accurately, from the
documents themselves rather than commentary: the mechanism (mechanistic
interpretability of the modular-addition case reverse-engineered the algorithm the
network learns and gave progress measures showing the generalizing circuit forms
gradually beneath a flat test curve, so the "sudden" jump is sudden only in the
metric being watched), and the cause (regularization, weight decay in particular,
drives the transition from the memorizing solution to the generalizing one).
Report what grokking is, the honest size of the foundation under it, what the
follow-up work confirmed and corrected, and where today's shorthand outruns the
evidence. Do not inflate it into a theory of emergence, and do not dismiss it;
show the figures and let the scale speak.

## Sources

Source floor for this series: at least 6 sources, at least 3 primary, at least 1
secondary. Primary here is each cited paper's own authors reporting their own
result.

Direct the researcher to read, at minimum:
- The grokking paper itself (arXiv 2201.02177). Read the experimental setup, not
  the abstract: the exact tasks and operation(s), the modulus/dataset size, the
  fraction of data used for training, the optimizer and weight-decay setting, and
  the figures showing steps-to-generalization. Record the real numbers and the
  paper's own hedges about scope.
- Neel Nanda and colleagues, "Progress Measures for Grokking via Mechanistic
  Interpretability" (2023, ICLR 2023), primary for the reverse-engineered
  modular-addition circuit and the progress measures showing gradual formation
  under a flat test curve.
- Ziming Liu and colleagues, "Towards Understanding Grokking: An Effective Theory
  of Representation Learning" (2022), and/or a second follow-up establishing the
  role of weight decay and regularization in driving the transition.
- At least one independent secondary source (reporting or a survey) for how
  "grokking" is used in current argument about emergent abilities and large-model
  training. A restatement of the paper's own claim is not independent
  confirmation.

Every figure (modulus, data fraction, step counts, accuracies) is checked against
the primary that owns it. Where later papers refine or contradict the original
framing, record the disagreement in full; the editor will test the angle against
it.

## Course placement and neighbors

The library already holds `the-evidence/emergent-abilities`,
`the-evidence/emergence-loss-perspective`, `the-evidence/scaling-laws-kaplan`,
and `the-mechanics/memorization`. This lesson is the missing piece on delayed
generalization and what "sudden" improvement does and does not mean, and it pairs
naturally with the emergence pieces without repeating them. Link the emergence
and memorization lessons in Background rather than re-teaching overfitting,
generalization, or memorization; if the reader needs the plain idea of a model
fitting training data versus generalizing, link where it was taught rather than
building it fresh. Tonight's other new articles are in unrelated desks (mmmu,
image-generation, reward-tampering, rite-aid-facial-recognition); no
cross-collision to manage. Link only already-published library pages, never
tonight's siblings.

## Production policy

Profile `balanced`; no role directive is `required`. Recorded plan: writing-coach
low effort, researcher high effort, writer medium effort, editor high effort;
model class `capable`. The runtime maps `capable` to the session's capable model
and runs each role at the session's effort; no `required` directive exists to
trade down. Actual harness: `claude-code-routine`. Actual model recorded in
nb-meta: `Claude Opus 4.8`.

## nb-meta

Date 2026-08-12. Harness `claude-code-routine`. Model `Claude Opus 4.8`. Tags are
the writer's to set as descriptive keywords (this open series configures no tag
fragments); three concise topical tags.

Recent habits to break travel with the writer and editor briefs.
