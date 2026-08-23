# writer brief: the-evidence/adam-optimizer (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/editorial-direction.md — house standard, press voice, series prompt, template identity
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/commission.md — assignment, boundaries, required contribution, recent shapes/phrasing to break
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/writing-coach/01/voice-guide.md — how this piece should sound, with exemplars
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/researcher/01/evidence.md — the complete claim set
- Article to edit in place: /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/library/the-evidence/adam-optimizer.html
- Template context: /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/library/the-evidence/adam-optimizer.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/97d053c3-1b59-5f4b-8b78-5c56b444e4a1/scratchpad/library-checkout

This round's focus — the evidence record sharpens the angle; hold two claims apart:
- The 2015 proof was flawed: uncontested fact. Reddi et al. name the exact error
  (the original proof wrongly assumes Γ_t is positive semidefinite). Write that
  plainly.
- Adam still converges under the settings practice uses: later primaries (Zhang
  et al. 2022; Défossez et al., TMLR) prove convergence in the large-β2 regime,
  and argue Reddi's counterexample picks the problem after fixing the
  hyperparameters. So do NOT write a blanket "Adam does not converge." The honest
  story is: the paper's headline theorem was wrong, and Adam is still fine — and
  has since been given real guarantees — in practice. That gap (a disproven proof
  under a method everyone trusts) is the lesson.
- Back the "field shrugged / AMSGrad rarely helps" point with the concrete
  artifacts in the record (PyTorch ships amsgrad=False by default; Schmidt et al.
  ICML 2021 benchmark of 15 optimizers found none consistently beats Adam).
- Show the scale honestly: every 2015 experiment is small (MNIST / CIFAR-10 /
  IMDB, largest model a 2×1000-unit MLP), which the paper itself calls "large."

Everything else per your skill. Fill nb-meta: date 2026-08-23, harness
`claude-code-routine`, model `claude-opus-4-8`, tags per the commission
(optimization, adam, deep-learning, convergence). Write the one-sentence
original-work statement in draft-handoff.md. Note the commission's warning that
`the-evidence/batch-normalization` already ran a "the paper's own explanation was
wrong" story about a different method — make this a distinct error (a disproven
convergence theorem) and do not reuse batch-norm's headings or closer. Iterate
with --no-check-links, then run full `nb stamp` + `nb check` until `BLOCK: 0`, and
do the display-text self-test before handing off.
