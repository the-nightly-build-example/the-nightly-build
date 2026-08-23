# Commission: the-evidence/adam-optimizer

## Assignment

One lesson for The Evidence, on the lesson template, reading the paper that
introduced the Adam optimizer: Diederik P. Kingma and Jimmy Ba, "Adam: A Method
for Stochastic Optimization," first posted December 2014 and published at ICLR
2015. This is the scheduled open article for the series on 2026-08-23.

## Why this document

Adam is the default optimizer almost every practitioner reaches for, cited well
over a hundred thousand times. The paper made two kinds of claim: an empirical
one (Adam trains faster and as well as or better than the alternatives it tested)
and a theoretical one (a convergence guarantee, its Theorem 4.1, bounding the
regret). The theoretical claim is the seam The Evidence exists to open: Sashank
Reddi, Satyen Kale, and Sanjiv Kumar ("On the Convergence of Adam and Beyond,"
ICLR 2018, best-paper award) exhibited a simple convex problem on which Adam does
not converge to the right answer, showing the original proof was wrong, and
proposed AMSGrad as a fix. Yet practitioners kept using plain Adam, because in
practice it works well and AMSGrad rarely helps. That gap between what the
document proved and how the field uses it is the lesson.

## Required contribution

The reader should finish able to say what Adam actually is (a per-parameter
adaptive learning rate built from running averages of the gradient and its
square, with bias correction), what the 2015 paper actually demonstrated and at
what scale (the specific experiments: logistic regression, small MLPs, and a
convnet on MNIST/CIFAR-10, not a language model or anything near frontier
scale), what its convergence theorem claimed, exactly how Reddi et al. broke it,
and why the field shrugged and kept using Adam anyway. Show the size of the
foundation honestly: the experiments were small by any modern measure, and the
paper's lasting influence rests on empirical robustness, not on the proof it
led with.

## Boundaries

- Teach one document. Do not drift into a survey of optimizers (SGD, RMSProp,
  AdaGrad, AdamW) beyond what is needed to say what Adam changed and what later
  work corrected. AdamW (Loshchilov & Hutter) is worth a sentence as the variant
  that actually displaced plain Adam in transformer training, but this is not a
  lesson about weight decay.
- Do not teach gradient descent from scratch: the library already has
  `the-mechanics/gradient-descent`. Link it in Background at first use rather
  than re-teaching it. Algebra needs no introduction; anything else is taught or
  linked.
- Do not overstate the practical consequences of the convergence counterexample.
  The honest story is that the proof was flawed and the method is still fine in
  practice. No hype, no doom.

## Template, sources, policy

- Template: lesson. Word band 1200-2200. Section chrome fixed by the template
  contract under `.nb-context`.
- Source floor (nb source-policy the-evidence): at least 6 sources, at least 3
  primary, at least 1 secondary. Primaries here are the documents that own their
  claims: the Adam paper (arXiv 1412.6980 / ICLR 2015), the Reddi et al. paper
  (arXiv 1904.09237 / ICLR 2018 OpenReview), and, if used, the AdamW paper and
  the original AdaGrad/RMSProp sources. Read the actual papers, not summaries.
- Production policy (nb production-policy the-evidence, balanced profile):
  writing-coach effort low, researcher effort high, writer effort medium, editor
  effort high; model tier "capable" for every role. Resolved to the runtime's
  Claude Opus 4.8 for all roles. nb-meta harness `claude-code-routine`, model
  `claude-opus-4-8`. No required directive was traded down.
- Suggested nb-meta tags: optimization, adam, deep-learning, convergence.

## This edition's neighbors

Four other lessons run tonight; keep this piece distinct from them and coherent
with the paper as a whole. They are: `the-instruments/squad` (how a benchmark
number is made), `the-mechanics/false-confidence` (why a model's wrong answers
sound as sure as its right ones), `what-could-go-wrong/natural-selection` (the
argument that competition selects for power-seeking AI), and
`when-ai-breaks/michigan-midas` (an automated fraud system that falsely accused
tens of thousands). No overlap of subject with any of them.

## Recent shapes and phrasing to break

The series' last several pieces (whisper, direct-preference-optimization,
foundation-models, batch-normalization) share habits this piece should not
inherit:

- The "what 'trained with X' actually names" or "X's best score was never the
  point" opener-heading mold. Name the orientation section in this paper's own
  nouns.
- Leading the comparison with an `nb-table` of tasks/numbers as the structural
  spine. A table is welcome only where a real comparison is the point (e.g. the
  paper's own experiments and their scale), not as a default shape.
- Note that `the-evidence/batch-normalization` already ran the "the paper's own
  explanation was wrong" story about a different method. This Adam lesson is a
  distinct document and a distinct error (a disproven convergence theorem, not a
  wrong causal mechanism); make the distinction do work rather than repeating
  batch-norm's framing. Do not reuse its headings or its closer.
- The house closer that ties to present usage is expected, but write it in
  Adam's nouns, not as a reused "where the same X still runs" line.
