# writer brief: the-evidence/dropout (01)

Inputs:
- .nb-work/the-evidence/dropout/agent-artifacts/the-evidence/dropout/editorial-direction.md
- .nb-work/the-evidence/dropout/agent-artifacts/the-evidence/dropout/commission.md
- .nb-work/the-evidence/dropout/agent-artifacts/the-evidence/dropout/writing-coach/01/voice-guide.md
- .nb-work/the-evidence/dropout/agent-artifacts/the-evidence/dropout/researcher/01/evidence.md
- Article to edit: .nb-work/the-evidence/dropout/library/the-evidence/dropout.html
- Template context dir: .nb-work/the-evidence/dropout/.nb-context/

Output:
- .nb-work/the-evidence/dropout/agent-artifacts/the-evidence/dropout/writer/01/draft-handoff.md

Proof:
- ./nb stamp .nb-work/the-evidence/dropout/library/the-evidence/dropout.html
- ./nb check .nb-work/the-evidence/dropout/library/the-evidence/dropout.html --series the-evidence --library /home/user/library-checkout
  (iterate --no-check-links; final proof with links, to BLOCK: 0)

nb-meta: harness="Claude Code", model="claude-opus-4-8". Tags e.g. dropout, regularization, overfitting, srivastava, hinton, neural-networks.

This round's focus: teach dropout's mechanism (keep-probability p, drop units not weights, test-time weight scaling), the authors' co-adaptation/ensemble justification (as theirs, and note the paper itself calls the weight-scaling an approximation of the true model average, Section 7.5), the actual results with sizes, then the honest present-day arc.

Accuracy cautions from the evidence record (respect exactly):
- Do NOT say dropout was abandoned. Frame it as: its role NARROWED to specific regimes. It remains p=0.1 in the original Transformer (Vaswani calls it very helpful), in PaLM finetuning, and after batch-norm in vision, and it produced large real gains on the small-data benchmarks of 2012-2014.
- The "off in the largest models" claim generalizes from a few DISCLOSED reports (PaLM states no pretraining dropout; LLaMA omits it; a 2025 Stanford study tests removal). Frontier proprietary settings are not published. Say the claim rests on disclosed reports, not a survey. GPT-3's paper states weight decay, not a disclosed dropout of zero.
- Cite Vaswani (attention-is-all-you-need paper) for the exact Transformer dropout rate: base P_drop=0.1 (0.3 only for the large EN-DE model). The 2025 Stanford paper's "0.3 at each layer" is wrong; do not repeat it.
- The paper's own Section 7.4 shows the benefit declines as data grows and vanishes on tiny data; that is the spine of the "does it still hold" argument.

Link the-evidence/batch-normalization in Background (and it exists in the library, so a Background link to ../the-evidence/batch-normalization.html is valid); optionally deep-double-descent or scaling-laws-kaplan. Do not re-teach overfitting from zero.

Habits not to inherit (from commission): vary heading construction; avoid the "What X took to build" counting-heading and negative-closer headings; avoid comma-triad and negative-parallelism deks; do not reuse a neighbor's dek shape.
