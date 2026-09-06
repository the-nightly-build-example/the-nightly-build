# researcher brief: the-evidence/dropout (01)

Inputs:
- .nb-work/the-evidence/dropout/agent-artifacts/the-evidence/dropout/editorial-direction.md
- .nb-work/the-evidence/dropout/agent-artifacts/the-evidence/dropout/commission.md

Output:
- .nb-work/the-evidence/dropout/agent-artifacts/the-evidence/dropout/researcher/01/evidence.md

Read the primary documents: the 2014 JMLR paper "Dropout: A Simple Way to
Prevent Neural Networks from Overfitting" (Srivastava et al.) and the 2012 tech
report "Improving neural networks by preventing co-adaptation of feature
detectors" (Hinton et al., arXiv 1207.0580).

Answer, each traced to its owning primary with locators:
- The exact mechanism: the keep/drop probability p, what is dropped (units, not
  weights), and the test-time weight-scaling rule the paper specifies (and the
  "inverted dropout" variant if the paper or a primary states it). Get the
  paper's own wording.
- The authors' justification: the co-adaptation argument and the "ensemble of
  exponentially many shared-weight subnetworks" interpretation, as they state
  it, plus any caveat they give.
- The results: for each dataset the paper reports (MNIST, SVHN, CIFAR-10/100,
  ImageNet, TIMIT, Reuters/text), the concrete error rates with and without
  dropout, the model sizes, and what state-of-the-art it claimed. Give the exact
  figures and their units.
- The present-day shift: find primaries documenting that dropout is often
  reduced or disabled in large transformer training (e.g. a transformer/LLM
  training report's stated dropout hyperparameter), and the documented tension
  between dropout and batch normalization (a primary studying "disharmony"
  between them). Establish how today's practice diverges from the paper's
  general-cure framing. Record contradictory evidence: cases where dropout still
  helps.

Confirm every URL resolves to the document's own page (JMLR, arXiv). Classify
each source primary/secondary with the authorship-and-stake test. Meet the
6-source, 3-primary / 1-secondary floor with sources that change the
interpretation, not padding.
