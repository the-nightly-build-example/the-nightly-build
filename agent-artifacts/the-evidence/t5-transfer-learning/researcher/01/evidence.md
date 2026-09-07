# Evidence: the-evidence/t5-transfer-learning (01)

The record supports the commission fully and firsthand. The T5 paper was read
from the JMLR version of record (volume 21, article 140, pages 1-67, 2020;
identical text to arXiv 1910.10683), extracted from the PDF, so every number here
comes from the document that owns it. The text-to-text framing, its four worked
examples, the C4 construction and size, the systematic study's findings, the five
model sizes, the pretraining scale, and the full final-results grid (Table 14) are
all confirmed against the paper. The 11-billion-parameter architecture is
independently confirmed against the released model config. Two teaching-relevant
gaps are honestly recorded: the paper reports no single absolute compute figure
(only hardware and relative FLOPs), and the released dataset and checkpoints carry
slightly different numbers from the paper's originals (a t5.1.0 versus t5.1.1
distinction the writer must not blur). The evidence does not undermine the angle.
It strengthens the "cites T5 for more than it showed" thread: T5 reached
state-of-the-art on 18 of 24 tasks but on none of the three translation tasks, and
its finding that the encoder-decoder form worked best sits in tension with the
field's later consolidation on decoder-only models.

Note on transport: the ar5iv and arXiv HTML renderings of the paper truncate before
Sections 3.6 and 3.7, and a summarizing fetch of them returned fabricated figures
(an 11B "d_ff=4096, 16 heads", a "97.9" SQuAD F1) that the primary PDF contradicts.
All numbers below are from the extracted JMLR PDF text, not from any summary.

## Sources

```text
URL:         https://www.jmlr.org/papers/v21/20-074.html
Kind:        primary. The paper itself; the authoring party owns every claim and number.
Establishes: What T5 is; the text-to-text framing and its worked examples; C4's
             construction, cleaning, and size; the systematic study's comparisons
             and findings; the five model sizes; the pretraining scale; and the
             final benchmark results.
Paraphrase:  A single encoder-decoder Transformer is trained to map input text to
             output text for every task, using one loss and one decoding procedure.
             The authors build C4 from Common Crawl, run a controlled comparison of
             objectives, architectures, and data, then combine the winning choices
             with scale (up to 11B parameters, ~1T pretraining tokens) to reach
             state-of-the-art on 18 of 24 tasks.
Locators:    Abstract and Sec. 1 (framing, release); Sec. 2.1 (baseline model);
             Sec. 2.2 (C4); Sec. 2.4 / Fig. 1 (input-output format, STS-B);
             Sec. 3.6 and 3.7 (model sizes, final scale); Table 14 and its
             surrounding prose pp. 38-40 (results); Sec. 4 "Takeaways" p. 41.
Quote:       "our text-to-text framework ... obtained comparable performance to
             task-specific architectures and ultimately produced state-of-the-art
             results when combined with scale" (Sec. 4, Takeaways).
```

```text
URL:         https://arxiv.org/abs/1910.10683
Kind:        primary. The preprint of the same paper; canonical arXiv landing page.
Establishes: Bibliographic identity and dates. Submitted v1 on 23 Oct 2019; the
             paper reports state-of-the-art baselines "as of October 24th, 2019."
             Same nine authors and title as the JMLR version.
Paraphrase:  Recorded so a reader can reach the openly hosted preprint; the JMLR
             entry above is the version of record and owns the page/table numbers.
Locators:    arXiv abstract page; JMLR masthead reads "Submitted 1/20; Revised
             6/20; Published 6/20."
Quote:       (none needed)
```

```text
URL:         https://www.tensorflow.org/datasets/catalog/c4
Kind:        primary. The released C4 dataset artifact, which the paper says it
             released; TensorFlow Datasets owns the shipped dataset's measurements.
Establishes: The released English C4 (c4/en) is 806.87 GiB with 364,613,570
             training examples and 364,724 validation examples; the uncleaned
             variant (c4/en.noclean) is 6.21 TiB. Confirms C4 is the cleaned
             Common Crawl corpus built per the T5 project.
Paraphrase:  The dataset the paper describes at "about 750 GB" ships, in its
             released form, at ~807 GiB of cleaned English text; the noclean
             version shows how much the cleaning removed (~6.2 TiB down to ~0.8).
Locators:    Dataset card, c4/en config; "Dataset size" and "Splits" fields.
Quote:       "C4 is a colossal, cleaned version of Common Crawl's web crawl corpus."
```

```text
URL:         https://huggingface.co/google-t5/t5-11b/blob/main/config.json
Kind:        primary. The released 11B model's own configuration file.
Establishes: The shipped 11B architecture: d_model=1024, d_ff=65536, d_kv=128,
             num_heads=128, num_layers=24, vocab_size=32128. Confirms the paper's
             text and refutes the fabricated "d_ff=4096, 16 heads" from an HTML
             summary.
Paraphrase:  The distinctive shape of T5-11B is a very wide feed-forward layer
             (d_ff=65,536) with 128 attention heads over a modest d_model of 1024,
             exactly as the paper explains (scale d_ff for accelerator efficiency).
Locators:    config.json fields.
Quote:       (numeric fields, quoted in Numbers below)
```

```text
URL:         https://github.com/google-research/text-to-text-transfer-transformer
Kind:        primary. The released code and checkpoint repository the paper points to.
Establishes: That code, C4, and pretrained checkpoints were released; the naming of
             the checkpoint families. The repo's released_checkpoints.md lists an
             improved t5.1.1 line whose parameter counts differ slightly from the
             paper's originals (its Small is ~77M, not the paper's ~60M), and notes
             the xl/xxl shapes differ "a bit" from the paper's 3B/11B.
Paraphrase:  The models a reader downloads today may be the improved t5.1.1
             checkpoints, which are not numerically identical to the paper's t5.1.0
             models. The article should attribute the paper's figures to the paper.
Locators:    Repository README ("Datasets") and released_checkpoints.md.
Quote:       (none verified verbatim; read through a summarizing fetch, so treat the
             t5.1.1 counts as directional and cite the paper for the paper's models.)
```

```text
URL:         https://arxiv.org/abs/2210.11416
Kind:        primary for its own claim (Chung et al., Google, 2022, "Scaling
             Instruction-Finetuned Language Models"). Here it is later work that
             built on T5, so it supplies the "bring it to now" thread on
             instruction tuning.
Establishes: Instruction finetuning was later applied to the T5 family, producing
             the publicly released Flan-T5 checkpoints, which "achieve strong
             few-shot performance even compared to much larger models, such as
             PaLM 62B." Shows T5 remained a live base years after 2020.
Paraphrase:  T5 as shipped in 2020 was pretrained-then-finetuned per task. A 2022
             line of work added instruction finetuning on top of T5 (among other
             model families), a capability the original paper did not study.
Locators:    Abstract; submitted 20 Oct 2022.
Quote:       "We also publicly release Flan-T5 checkpoints, which achieve strong
             few-shot performance even compared to much larger models."
```

```text
URL:         https://huggingface.co/docs/transformers/en/model_doc/t5
Kind:        secondary. Hugging Face documents T5 from outside the authoring party.
Establishes: How T5 is presented and used today: an encoder-decoder from 60M to 11B
             parameters, every task cast as text-to-text via a task-specific prefix
             (e.g. "translate English to German: ...", "summarize: ..."), with
             T5v1.1 and Flan-T5 listed as variants. Useful for the present-day usage
             framing; not a source for the paper's own numbers.
Paraphrase:  The text-to-text interface the reader meets in a modern library is the
             same prefix-per-task scheme the paper introduced.
Locators:    Page top ("T5 is a encoder-decoder transformer ... 60M to 11B").
Quote:       "each task is prepended with a task-specific prefix (e.g., translate
             English to German: ..., summarize: ...)."
```

## Contradictions

- **T5 was not state-of-the-art on translation, though it topped most benchmarks.**
  The paper reports SOTA on 18 of 24 tasks, but "We did not achieve
  state-of-the-art performance on any of the WMT translation tasks" (p. 39). T5-11B
  scored below the previous best on EnDe (32.1 vs 33.8), EnFr (43.4 vs 43.8), and
  well below on the low-resource EnRo (28.1 vs 38.5). The authors attribute this to
  English-only pretraining and to competitors' use of backtranslation. Any claim
  that T5 was best "at everything" overstates the record.

- **T5's controlled comparison found encoder-decoder best; the field went
  decoder-only.** The paper's Takeaways state "we found the original encoder-decoder
  form worked best in our text-to-text framework," noting it uses twice the
  parameters of encoder-only (BERT) or decoder-only (language-model) forms at
  "similar computational cost." The mainstream of large language models since
  consolidated on decoder-only architectures (the GPT-3 direction, a library lesson
  the writer can link). This is not a factual contradiction inside the paper, but it
  is the sharpest case of "later usage moved past what the paper showed": T5's
  finding was at matched, modest scale and did not settle the architecture question
  for the scale the field later reached.

- **The paper's absolute scores are 2019-era records, now surpassed.** The
  "previous best" baselines in Table 14 are dated "as of October 24th, 2019," and
  the paper notes its own scores exceed human performance on some SuperGLUE reading
  tasks (MultiRC, ReCoRD) while humans still reach 100% on COPA and WSC. The value
  the paper retains is its controlled comparison of choices, not its leaderboard
  numbers.

- **Released artifacts differ slightly from the paper's models.** The released C4
  ships at ~807 GiB against the paper's "about 750 GB," and the repo's improved
  t5.1.1 checkpoints carry different parameter counts (e.g. ~77M Small) than the
  paper's t5.1.0 models (~60M Small). Cite the paper for the paper's figures; cite
  the artifact for the artifact's.

## Numbers

```text
Figure: C4 size "about 750 GB" of cleaned English text
Owner:  T5 paper, Sec. 2.2
Scope:  The base C4 built from the April 2019 Common Crawl extract, after cleaning.
```

```text
Figure: Released C4 (c4/en) = 806.87 GiB; 364,613,570 train / 364,724 validation examples; noclean variant = 6.21 TiB
Owner:  TensorFlow Datasets catalog (released artifact)
Scope:  The shipped dataset as measured by TFDS; a later regeneration, not identical to the paper's snapshot.
```

```text
Figure: Common Crawl produces "about 20TB of text data extracted from web pages each month"
Owner:  T5 paper, Sec. 1
Scope:  Raw monthly Common Crawl text before any T5 cleaning; the anchor for how aggressively C4 filters.
```

```text
Figure: Baseline pretraining = 2^35 ≈ 34B tokens (2^19 = 524,288 steps, batch 128, ~2^16 = 65,536 tokens/batch)
Owner:  T5 paper, Sec. 3.1.2
Scope:  The baseline (T5-Base) pretraining budget. Paper contrasts it with BERT (~137B tokens) and RoBERTa (~2.2T tokens).
```

```text
Figure: Final models pretrained on "about 1 trillion pre-training tokens (about 32x as many as our baseline)"
Owner:  T5 paper, Sec. 3.7
Scope:  1,000,000 steps, batch of 2^11 sequences of length 512, on C4.
```

```text
Figure: Model sizes = Small ~60M, Base ~220M, Large ~770M, 3B ~2.8B, 11B ~11B parameters
Owner:  T5 paper, Sec. 3.7 ("Model sizes") and Table 14 caption
Scope:  The paper's t5.1.0 model family. Base is the baseline (d_model=768, d_ff=3072, 12 blocks each, 12 heads, ~2x BERT_BASE).
```

```text
Figure: 11B architecture = d_model=1024, d_ff=65,536, d_kv=128, 128 heads, 24 layers each (encoder and decoder)
Owner:  T5 paper Sec. 3.7; independently confirmed by released config.json (d_ff=65536, num_heads=128, num_layers=24, d_model=1024, vocab_size=32128)
Scope:  The 11B variant; d_ff scaled up deliberately for accelerator efficiency.
```

```text
Figure: Hardware = slices of Cloud TPU v3 Pods (1,024 TPU v3 chips), via model and data parallelism (Mesh TensorFlow)
Owner:  T5 paper, Sec. 2.1
Scope:  The training platform. NOTE: the paper reports NO single absolute compute total (e.g. petaflop-days); compute is discussed only as relative FLOPs (baseline = M, variants 2M/4M) and as token/step counts.
```

```text
Figure: T5-11B final results: GLUE 90.3; SuperGLUE 88.9; SQuAD EM 91.26 / F1 96.22; CNN/DM ROUGE-1 43.52, ROUGE-2 21.55, ROUGE-L 40.69
Owner:  T5 paper, Table 14
Scope:  Test set except SQuAD (validation). Previous best (as of 24 Oct 2019): GLUE 89.4, SuperGLUE 84.6, SQuAD EM 90.1 / F1 95.5, CNN/DM ROUGE-1 43.47 / ROUGE-2 20.30 / ROUGE-L 40.63.
```

```text
Figure: T5-11B translation BLEU: WMT EnDe 32.1; EnFr 43.4; EnRo 28.1 — below previous best on all three (33.8 / 43.8 / 38.5)
Owner:  T5 paper, Table 14 and p. 39 prose
Scope:  The three WMT tasks; T5 reached SOTA on none. Cause given: English-only pretraining, no backtranslation.
```

```text
Figure: State-of-the-art on 18 of 24 tasks studied
Owner:  T5 paper, Sec. 3.7 (opening of results discussion)
Scope:  The 24 task metrics in Table 14, against the previous best as of 24 Oct 2019.
```

```text
Figure: Human baselines cited by the paper: GLUE RTE 93.6, WNLI 95.9; SQuAD EM 82.30 / F1 91.22; SuperGLUE COPA and WSC 100%
Owner:  T5 paper, pp. 38-39 (citing Wang et al. 2018/2019, Rajpurkar et al. 2016)
Scope:  Context for reading the scores; the paper notes it exceeds human scores on MultiRC and ReCoRD, suggesting metric bias there.
```

## Source assets

```text
Asset: Figure 1, "diagram of our text-to-text framework," page 1 of the paper (beside the abstract).
Shows: Every task as one interface: a task-prefixed input feeding one model, which emits text. The four labeled examples carry the whole idea at a glance.
Crop:  Must retain the four input->output pairs verbatim (see Numbers/worked examples below) and the single shared model box. Omit nothing that pairs an input with its target; do not crop to a single example, since the point is that different task types share one interface.
```

Worked examples exactly as printed in Figure 1 (use these; they are the reader-followable cases the commission asks for):
- `translate English to German: That is good.` -> `Das ist gut.`
- `cola sentence: The course is jumping well.` -> `not acceptable`
- `stsb sentence1: The rhino grazed on the grass. sentence2: A rhino is grazing in a field.` -> `3.8`
- `summarize: state authorities dispatched emergency crews tuesday to survey the damage after an onslaught of severe weather in mississippi...` -> `six people hospitalized after a storm in attala county.`

The STS-B case is worth teaching: STS-B is a regression task scoring similarity
from 1 to 5, and T5 casts it as text by rounding to the nearest 0.2 and emitting
the number as a string (the paper's example: 2.57 becomes the string "2.6").

```text
Asset: Table 14, "Performance of our T5 variants on every task we study," pp. 38-40.
Shows: The full grid of Previous best vs T5-Small/Base/Large/3B/11B across GLUE, SuperGLUE, SQuAD, CNN/DM, and WMT. A reader can see scale climbing the ladder and, in the WMT columns, T5 sitting below the previous best.
Crop:  A useful crop keeps the "Previous best" and "T5-11B" rows and the WMT + SuppGLUE/GLUE/SQuAD columns, so the reader sees both the wins and the translation shortfall in one view. Retain column headers and the "as of October 24th, 2019" caption note; do not crop to only the winning columns, which would misrepresent the record.
```

C4 cleaning heuristics, exact, for a possible list or callout (T5 paper Sec. 2.2):
retain only lines ending in terminal punctuation; discard any page with fewer than
5 sentences and keep only lines with at least 3 words; drop pages containing any
word on the "List of Dirty, Naughty, Obscene or Otherwise Bad Words"; remove any
line with the word "Javascript"; remove any page with the phrase "lorem ipsum";
remove any page containing a curly bracket "{" (to exclude code); deduplicate by
"discarding all but one of any three-sentence span occurring more than once";
keep only pages classified as English by langdetect with probability >= 0.99.

## Discarded

```text
URL: https://ar5iv.labs.arxiv.org/html/1910.10683 — HTML render truncates before Sec. 3.6/3.7; a summarizing fetch returned fabricated model and result numbers. Replaced by the JMLR PDF (primary text).
URL: https://arxiv.org/html/1910.10683v4 — same truncation; not reliable for the tables. Used only to confirm the paper is the same document.
URL: https://www.jmlr.org/papers/volume21/20-074/20-074.pdf — the correct primary, but a summarizing fetch could not read the compressed PDF stream; the PDF was instead extracted to text locally and read directly. Kept as the source of record (its HTML landing page, v21/20-074.html, is the URL to cite).
```
