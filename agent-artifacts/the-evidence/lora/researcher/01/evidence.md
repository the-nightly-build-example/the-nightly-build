# Evidence record: the-evidence/lora (01)

The evidence supports the commission's angle firsthand. The LoRA paper's own
abstract and tables confirm the headline claims: about 10,000 times fewer
trainable parameters and roughly a threefold VRAM cut for GPT-3 175B, ranks as
small as 1 in the analysis and 4 to 8 in the shipped experiments, LoRA applied
to the attention projection matrices, and at least one benchmark (GPT-3 on
MNLI-matched and SAMSum, RoBERTa/DeBERTa on GLUE, GPT-2 on E2E) where LoRA
matches or beats full fine-tuning. The "intrinsic rank" hypothesis is quotable
in the authors' own words and traces to Aghajanyan et al. (2020), whose 200-
parameter RoBERTa result the writer should not conflate with LoRA's own claim.
QLoRA and the 2024 limitation study are verified from their own papers, and the
limitation study is the load-bearing counterweight: it shows the "matches full
fine-tuning" claim breaks on code and math, especially in continued
pretraining. Adoption is anchored to Hugging Face's own Hub measurement. The
record is thin in one place: whether the limitation study's formal venue is TMLR
(see Contradictions), a labeling detail, not a numbers question.

## Sources

```text
URL:         https://arxiv.org/abs/2106.09685
Kind:        primary — the LoRA paper itself; owns every headline number and the hypothesis
Establishes: what LoRA is, the parameter/memory/checkpoint reductions, the ranks, the benchmarks, the intrinsic-rank hypothesis, and zero inference latency
Paraphrase:  LoRA freezes the pretrained weights and injects a trainable pair of low-rank matrices (A, B) into each Transformer layer, training only that pair. For GPT-3 175B it reports 10,000x fewer trainable parameters and a 3x GPU memory cut versus Adam full fine-tuning, while performing on-par or better than full fine-tuning on RoBERTa, DeBERTa, GPT-2, and GPT-3. Because BA can be added back into W, there is no extra inference latency, unlike adapter layers. In their experiments they apply LoRA to the attention query and value projections (Wq, Wv).
Locators:    Abstract; Introduction (hypothesis); Section 4.1 (no added inference latency); Section 5 / Table 4 (GPT-3); Table 2 (GLUE); Table 3 (E2E); Section 7.2 / Table 6 (rank analysis)
Quote:       "we hypothesize that the change in weights during model adaptation also has a low 'intrinsic rank'"
Quote:       "Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times."
Quote:       "we reduce the VRAM consumption during training from 1.2TB to 350GB" and "the checkpoint size is reduced by roughly 10,000x (from 350GB to 35MB)"

URL:         https://arxiv.org/abs/2012.13255
Kind:        primary — Aghajanyan, Zettlemoyer, Gupta (2020); owns the "intrinsic dimension" finding LoRA builds on
Establishes: the prior empirical result that motivates LoRA's hypothesis, and the exact boundary between the two claims
Paraphrase:  Fine-tuning can be done in a very low-dimensional reparameterization: optimizing only 200 parameters randomly projected into the full weight space tunes RoBERTa to 90% of full-parameter performance on MRPC. This is a claim about the intrinsic dimension of the whole fine-tuning update measured in a random subspace, not a claim that the weight-change matrix is itself low rank. LoRA's contribution is to hypothesize the latter and to structure the update as an explicit low-rank product so it can be merged back into the weights.
Locators:    Abstract; MRPC / d90 result
Quote:       "by optimizing only 200 trainable parameters randomly projected back into the full space, we can tune a RoBERTa model to achieve 90% of the full parameter performance levels on MRPC"

URL:         https://arxiv.org/abs/2305.14314
Kind:        primary — the QLoRA paper (Dettmers, Pagnoni, Holtzman, Zettlemoyer, University of Washington, 2023)
Establishes: the quantized successor that made single-GPU fine-tuning of very large models routine
Paraphrase:  QLoRA finetunes a 65B-parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance. It backpropagates through a frozen 4-bit quantized base model into LoRA adapters, using three techniques: 4-bit NormalFloat (NF4), double quantization, and paged optimizers. The resulting Guanaco family reaches 99.3% of ChatGPT's level on the Vicuna benchmark after 24 hours of finetuning on one GPU. Caveat for the writer: the Vicuna benchmark is judged by GPT-4, an automated preference score, not a task-accuracy number.
Locators:    Abstract; Section 3 (NF4, double quantization, paged optimizers); Guanaco / Vicuna results
Quote:       "an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance"
Quote:       "reaching 99.3% of the performance level of ChatGPT while only requiring 24 hours of finetuning on a single GPU"

URL:         https://arxiv.org/abs/2405.09673
Kind:        primary — "LoRA Learns Less and Forgets Less" (Biderman et al., 2024); owns the limitation finding
Establishes: where the "matches full fine-tuning" claim fails, and why
Paraphrase:  On programming and mathematics, LoRA substantially underperforms full finetuning, most sharply in continued pretraining (20B tokens of code, 14.7B of math) and less so in instruction finetuning. The base model is Llama-2-7B throughout; 13B is not used. LoRA nonetheless forgets less: it better preserves the base model's out-of-domain abilities and keeps more diverse generations. The paper's mechanism is that training few parameters constrains the finetuned model from diverging from the base; it also finds that full finetuning learns weight perturbations of rank 10 to 100 times higher than typical LoRA ranks, which partly explains the gap. Ranks studied: 16, 64, 256. Their best-practice recommendation is to use LoRA for instruction finetuning rather than continued pretraining, target all transformer modules, and use rank as high as 256.
Locators:    Abstract; results on code/math; rank-of-perturbation analysis; recommendations section
Quote:       "LoRA substantially underperforms full finetuning"
Quote:       "By training fewer parameters, LoRA is hypothesized to constrain the finetuned model from diverging significantly from the base model"

URL:         https://huggingface.co/blog/peft-beyond-lora
Kind:        primary to the adoption measurement — Hugging Face measuring its own Hub (Bossan, Paul, Tietz, Rasul; June 18, 2026)
Establishes: how dominant LoRA is among parameter-efficient methods in current practice
Paraphrase:  Of 20,834 Hugging Face Hub model cards that mention exactly one PEFT technique, 20,509 (98.4%) mention LoRA. Among a sample of 10,000 image-generation checkpoints, 7,111 (95.0%) are LoRAs. A GitHub code search for the PEFT import line returns LoRA in 71.3% of results. These are Hugging Face's firsthand counts of its own platform, so primary to the adoption figure; on LoRA's efficacy it would only be secondary.
Locators:    Hub model-card statistic; image-checkpoint statistic; GitHub code-search statistic
Quote:       "Of a sample of 20,834 model cards on Hugging Face Hub that mention exactly one PEFT technique, 20,509 mention LoRA (98.4%)."

URL:         https://github.com/huggingface/peft
Kind:        secondary — the PEFT library, a third party reporting LoRA's status and reach from outside the LoRA authors
Establishes: that LoRA is the primary, default-demonstrated method in the standard open fine-tuning toolkit, and a rough adoption signal
Paraphrase:  Hugging Face's PEFT library adapts large pretrained models by fine-tuning only a small number of extra parameters, and uses LoRA as its primary quickstart demonstration, integrated across Transformers, Diffusers, Accelerate, and TRL. The repository shows roughly 21.6k stars. Star counts are a coarse popularity signal, not a usage census; the Hub measurement above is the firmer figure.
Locators:    README description; quickstart; star count on repo page
Quote:       (none load-bearing)
```

## Contradictions

- The core productive tension the commission wants: LoRA (2021) reports "on-par
  or better than fine-tuning" on RoBERTa, DeBERTa, GPT-2, GPT-3; the 2024 study
  reports LoRA "substantially underperforms full finetuning" on code and math.
  These do not actually conflict. LoRA's claim is bounded to its models and
  tasks (GLUE, E2E, WikiSQL, MNLI, SAMSum, all relatively constrained NLU/NLG),
  and the 2024 study probes harder generative domains and the continued-
  pretraining regime the original paper never tested. The gap widens with task
  difficulty and with how much new knowledge the finetune must add. This
  supports, not undermines, the commissioned angle.
- Aghajanyan (2020) vs LoRA (2021) on what "low-dimensional" means. Aghajanyan
  measures the intrinsic dimension of the full fine-tuning update inside a random
  projection (200 parameters reach 90% on MRPC). LoRA hypothesizes the weight-
  change matrix itself is low rank and builds that structure directly. A writer
  who cites the 200-parameter figure as LoRA's own result would misattribute it.
- The web returns an uncited claim that "LoRA achieves 97-99% of full fine-tuning
  accuracy on GLUE" and a Gartner "85% by 2027" forecast. Neither traces to a
  primary I could open, and the 97-99% figure papers over exactly the domain gap
  the 2024 study documents. Not cited. See Discarded.
- Venue label for the limitation study is unresolved (see the note in the opening
  paragraph and Discarded): one reading places it in TMLR 2024, the arXiv HTML
  does not state a venue. It is cited by its arXiv page, which it owns regardless.

## Numbers

```text
Figure: 10,000x fewer trainable parameters (LoRA vs Adam full fine-tuning)
Owner:  LoRA paper, Abstract
Scope:  GPT-3 175B. Headline ratio; the checkpoint-size cut is also ~10,000x (350GB to 35MB). Exact trainable-parameter ratio depends on config: 175,255.8M full vs 4.7M LoRA is ~37,000x, vs 37.7M is ~4,650x.

Figure: 3x GPU memory reduction; VRAM 1.2TB to 350GB
Owner:  LoRA paper, Abstract and Section 5 (GPT-3)
Scope:  GPT-3 175B training, LoRA vs Adam full fine-tuning.

Figure: GPT-3 175B, WikiSQL / MNLI-m / SAMSum (R1/R2/RL)
Owner:  LoRA paper, Table 4
Scope:  Full FT (175,255.8M params): 73.8 / 89.5 / 52.0-28.0-44.5. LoRA (4.7M): 73.4 / 91.7 / 53.8-29.8-45.9. LoRA (37.7M): 74.0 / 91.6 / 53.4-29.2-45.1. LoRA matches on WikiSQL and beats FT on MNLI-m and SAMSum.

Figure: GLUE average, RoBERTa/DeBERTa (LoRA vs full FT)
Owner:  LoRA paper, Table 2
Scope:  RoBERTa base 86.4 FT (125M) vs 87.2 LoRA (0.3M). RoBERTa large 88.9 FT (355M) vs 89.0 LoRA (0.8M). DeBERTa XXL 91.1 FT (1500M) vs 91.3 LoRA (4.7M). r=8.

Figure: E2E NLG BLEU, GPT-2 (LoRA vs full FT)
Owner:  LoRA paper, Table 3
Scope:  GPT-2 Medium 68.2 FT (354.92M) vs 70.4 LoRA (0.35M). GPT-2 Large 68.5 FT (774.03M) vs 70.4 LoRA (0.77M). r=4.

Figure: ranks used
Owner:  LoRA paper
Scope:  Shipped experiments: r=4 (GPT-2 E2E, GPT-3 primary), r=8 (RoBERTa/DeBERTa GLUE). Rank study (Table 6) sweeps r=1,2,4,8,64 and finds "a rank as small as one suffices for adapting both Wq and Wv on these datasets." LoRA applied to attention projections Wq, Wv (and optionally Wk, Wo).

Figure: intrinsic-dimension prior result
Owner:  Aghajanyan et al. (2020), Abstract
Scope:  200 trainable parameters (random projection) reach 90% of full RoBERTa performance on MRPC.

Figure: QLoRA — 65B model on a single 48GB GPU; Guanaco 99.3% of ChatGPT
Owner:  QLoRA paper, Abstract
Scope:  Preserves full 16-bit finetuning performance; 99.3% is on the GPT-4-judged Vicuna benchmark after 24h on one GPU.

Figure: full FT learns rank 10-100x higher than typical LoRA
Owner:  Biderman et al. (2024)
Scope:  Llama-2-7B on code/math; partial explanation of the performance gap.

Figure: LoRA share of PEFT usage — 98.4% of single-technique Hub model cards
Owner:  Hugging Face blog (peft-beyond-lora), firsthand Hub count
Scope:  20,509 of 20,834 model cards mentioning exactly one PEFT technique. Image checkpoints: 7,111/10,000 (95.0%).
```

## Source assets

```text
Asset: LoRA paper, Figure 1 (the A/B low-rank pair beside the frozen weight matrix W)
Shows: the entire mechanism in one diagram — W is frozen, only the thin down-projection A and up-projection B are trained, and their product adds to W
Crop:  keep the frozen-W block, both A and B with the r bottleneck labeled, and the addition; a crop that drops the r dimension loses the whole point

Asset: LoRA paper, Table 4 (GPT-3 175B: FT vs LoRA on WikiSQL, MNLI-m, SAMSum, with parameter counts)
Shows: LoRA matching or beating full fine-tuning while training ~4.7M of 175B parameters
Crop:  must retain the trainable-parameter column beside the scores, or the comparison is meaningless

Asset: LoRA paper, Table 6 (accuracy vs rank r = 1, 2, 4, 8, 64)
Shows: performance flattens by r=1-2, the empirical basis for the low-intrinsic-rank hypothesis
Crop:  keep the r=1 and r=2 rows; those carry the claim

Asset: QLoRA paper, Figure 1 (memory footprint of full finetuning vs LoRA vs QLoRA)
Shows: the stacked memory savings that put a 65B finetune on one 48GB GPU
Crop:  keep all three bars side by side; a single bar shows nothing

Asset: Biderman et al. (2024), learning-curve / bar figures comparing LoRA and full finetuning on code and math
Shows: LoRA trailing full finetuning on target-domain accuracy while forgetting less out of domain
Crop:  keep both the target-domain and out-of-domain panels; showing only one hides half the finding

Asset: Hugging Face blog, the PEFT-method share chart (LoRA vs everything else)
Shows: LoRA's near-total dominance of current parameter-efficient fine-tuning
Crop:  retain the denominator (sample size) in the caption or the percentage misleads
```

## Discarded

```text
https://www.google.com/search aggregation ("97-99% of full FT on GLUE"; Gartner "85% by 2027"): uncited secondary aggregations with no openable primary; the 97-99% figure also elides the code/math gap the 2024 study documents.
https://brics-econ.org/parameter-efficient-fine-tuning-... : SEO explainer, secondary, adds nothing the primaries do not own.
https://apxml.com/... and Medium tutorial: how-to tutorials, no primary claim to cite.
```

## Unresolved

The publication venue of "LoRA Learns Less and Forgets Less" is unconfirmed:
one source places it in TMLR (August 2024, Featured Certification, OpenReview
forum id aloEru2qCG), the arXiv HTML states no venue. This affects only how the
paper is labeled, not any figure. Cited by its arXiv page, which it owns either
way. If the writer wants to call it a TMLR paper, confirm against the OpenReview
forum first.
