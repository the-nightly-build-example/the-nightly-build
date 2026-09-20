# researcher brief: the-evidence/flamingo (01)

Inputs:
- ../../commission.md — the assignment, angle, boundaries, required contribution.
- ../../editorial-direction.md — citation standard, series territory, declared reader.

Output: ./evidence.md

Sourcing floor (nb source-policy): at least 6 sources, at least 3 primary, at
least 1 secondary. Read the primary documents, including tables.

Primary documents to read and record with locators:
- Alayrac et al., "Flamingo: a Visual Language Model for Few-Shot Learning"
  (DeepMind, 2022, arXiv:2204.14198). Verify and record:
  - The core claim: few-shot, in-context learning across interleaved image/video
    and text with the vision and language backbones frozen. Exact wording of the
    "beats fine-tuned state of the art" claim and its bound (the paper states it
    set a new few-shot SOTA on a number of tasks and, on several, beat methods
    fine-tuned on far more data — get the exact counts, e.g. "X of 16 tasks",
    the number of shots, and which tasks fine-tuned systems still won).
    Distinguish 4-shot/32-shot results.
  - The architecture pieces: frozen pretrained vision encoder, frozen pretrained
    language model (Chinchilla-based), the Perceiver Resampler, and gated
    cross-attention layers. Record what each does in one plain line.
  - Scale: the largest model's parameter count (and the sizes of the frozen
    parts), and the training data (the M3W interleaved-webpage dataset, image-text
    pairs, video-text) with any stated sizes.
  - The paper's own documented limitations/failure modes (hallucination, weaker
    performance on classification-style tasks, etc.).
- OpenFlamingo (Awadalla et al., 2023) as a primary/secondary reproduction on open
  data — verify what it reproduced and any performance gap it reported.
- Where a claim rests on a predecessor (frozen-LM multimodal work, or the
  Chinchilla LM), cite the primary that owns it.

Numbers section: the headline benchmark figures (task, shots, Flamingo score vs
prior fine-tuned SOTA), the largest model's parameter count, and dataset sizes,
each with its owning primary and scope.

Contradictions to search for on purpose: any evidence that the "few-shot beats
fine-tuned" claim was narrower than remembered (which tasks it failed on), any
critique of the evaluation, and the fact that weights were never released. Record
in full.

Source assets: note any figure/table (e.g. the results table, the architecture
figure showing frozen backbones + resampler) that could carry an argument better
than prose. Do not prescribe crops.

Do not browse the repository for background. Confirm every URL resolves to the
document's own page. Flag any commission claim the evidence cannot support.
