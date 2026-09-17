# Evidence record: the-evidence/gpt-1 (01)

The GPT-1 paper was read in full, including all five results tables. The record
firmly supports the commission's core factual spine: a 12-layer decoder-only
Transformer, pre-trained with a plain language-modeling objective on the
BooksCorpus book corpus, then fine-tuned per task with traversal-style input
transformations, improving prior state of the art on 9 of 12 datasets. Two
figures the commission asks for firsthand are not in the paper and had to be
sourced elsewhere or recorded as gaps: the paper states **no total parameter
count** (the famous "117M" comes from the GPT-2 report, which calls its smallest
model "equivalent to the original GPT"), and it gives the training corpus only as
"over 7,000 unique unpublished books," a smaller figure than the 11,038 books in
the origin BooksCorpus paper. The evidence is strongest where the commission is
most careful: several headline gains are small (SNLI 0.6, MNLI 1.5, STS-B ~1
point), the model lost to a prior baseline on 3 of the 12 datasets, and the
ablation table shows the auxiliary LM objective slightly *lowered* the average
score. None of this undermines the commissioned angle; it sharpens it. The
"present-day" arc (fine-tuning and input transformations giving way to prompting)
is cited firsthand from the GPT-2, GPT-3, and GPT-4 reports.

## Sources

```text
URL:         https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
Kind:        primary. It is the document the lesson teaches; OpenAI authored the
             claim and owns every number in it. This cdn PDF is the paper's own
             page. (The human-facing announcement at
             openai.com/index/language-unsupervised/ is Cloudflare-gated: it
             returns 403 to automated requests including a browser user agent.
             The PDF above is the artifact itself and resolves 200.)
Establishes: What GPT-1 is, its method, scale, and results — all firsthand.
             - Authors: Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya
               Sutskever, all OpenAI (title block).
             - Status: the footer of page 1 reads "Preprint. Work in progress."
               It is an OpenAI technical report, not a peer-reviewed conference
               paper. It never appeared on arXiv; the cdn PDF is the release.
             - Method: two stages. (1) Unsupervised pre-training maximizes a
               standard left-to-right language-modeling likelihood (Eq. 1) with a
               multi-layer Transformer *decoder* using masked self-attention.
               (2) Supervised fine-tuning adds one linear output layer (Wy) and
               delimiter-token embeddings, and reuses task-specific "traversal-
               style" input transformations so one architecture handles
               classification, entailment, similarity, and multiple-choice
               (Sec. 3.1-3.3). Fine-tuning also carries an auxiliary LM objective
               L3 = L2 + λ·L1, with λ = 0.5 (Eq. 5, Sec. 4.1).
             - Architecture: "12-layer decoder-only transformer with masked
               self-attention heads (768 dimensional states and 12 attention
               heads)"; 3072-dim feed-forward inner states; BPE vocabulary with
               40,000 merges; GELU activation; learned position embeddings
               (Sec. 4.1, "Model specifications").
             - Corpus: "We use the BooksCorpus dataset for training the language
               model. It contains over 7,000 unique unpublished books" (Sec. 4.1).
               Token-level perplexity on it: 18.4.
             - Scope: four task types, twelve datasets (Table 1). State of the
               art improved on "9 out of the 12 tasks studied" (Abstract; repeated
               Sec. 4.2 conclusion, "9 out of the 12 datasets").
Paraphrase:  A single task-agnostic Transformer language model, pre-trained on
             unlabeled books and then lightly fine-tuned per task, beat
             purpose-built architectures on most of a twelve-dataset suite.
Locators:    Abstract; Sec. 3 (Framework), Eqs. 1-5; Sec. 4.1 (Setup / Model
             specifications); Tables 1-5; Sec. 6 (Conclusion).
Quote:       "We trained a 12-layer decoder-only transformer with masked
             self-attention heads (768 dimensional states and 12 attention
             heads)." / "It contains over 7,000 unique unpublished books"
```

```text
URL:         https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
Kind:        primary for the two claims cited from it: GPT-1's parameter count and
             the first step away from fine-tuning. OpenAI authored it (Radford,
             Wu, Child, Luan, Amodei, Sutskever, 2019). cdn PDF is its own page.
Establishes: (1) The 117-million-parameter figure that GPT-1 itself never prints.
             Table 2 lists four model sizes; the smallest is 117M params, 12
             layers, d_model 768 — architecturally identical to GPT-1 — and the
             text states "The smallest model is equivalent to the original GPT."
             The largest, GPT-2, is 1542M (1.5B) params, 48 layers, d_model 1600,
             "over an order of magnitude more parameters than GPT."
             (2) The first thing the recipe dropped: "We demonstrate language
             models can perform down-stream tasks in a zero-shot setting –
             without any parameter or architecture modification." GPT-2 keeps the
             pre-training half and discards supervised fine-tuning and the
             task-specific input heads for downstream evaluation.
Paraphrase:  GPT-2 reused GPT-1's architecture at ~13x the parameters and tested
             tasks with no fine-tuning at all, purely by conditioning the language
             model on text.
Locators:    Sec. 2.3 (Model) and Table 2; Sec. 1 (final paragraph, "without any
             parameter or architecture modification").
Quote:       "The smallest model is equivalent to the original GPT" / "without any
             parameter or architecture modification"
```

```text
URL:         https://arxiv.org/abs/2005.14165
Kind:        primary for the scaling and few-shot claims cited from it. Brown et
             al., "Language Models are Few-Shot Learners," 2020 (OpenAI). arXiv
             abstract page is the document's own page.
Establishes: The end state of the "drop fine-tuning" arc. GPT-3 is "an
             autoregressive language model with 175 billion parameters." "For all
             tasks, GPT-3 is applied without any gradient updates or fine-tuning,
             with tasks and few-shot demonstrations specified purely via text
             interaction with the model." The paper names this "in-context
             learning" and contrasts it explicitly with fine-tuning, which it
             defines as "updating the weights of" a pre-trained model. This is
             where GPT-1's per-task supervised fine-tuning is replaced outright by
             prompting at scale.
Paraphrase:  By 175B parameters, downstream tasks were done with text prompts and
             a few examples in context, and no weight updates — the opposite of
             GPT-1's fine-tune-per-task procedure.
Locators:    Abstract; Sec. 1 (Introduction, "175 billion parameter" and the
             three evaluation settings); Sec. 2.1 (definitions of Fine-Tuning vs.
             Few-Shot / One-Shot / Zero-Shot).
Quote:       "GPT-3 is applied without any gradient updates or fine-tuning, with
             tasks and few-shot demonstrations specified purely via text
             interaction with the model."
```

```text
URL:         https://arxiv.org/abs/2303.08774
Kind:        primary for the non-disclosure claim. OpenAI, "GPT-4 Technical
             Report," 2023. arXiv abstract page is its own page.
Establishes: How far the 2018 framing has receded. The report withholds exactly
             the numbers GPT-1 published openly: "this report contains no further
             details about the architecture (including model size), hardware,
             training compute, dataset construction, training method, or similar."
             It also documents a post-training stage GPT-1 did not have —
             reinforcement learning from human feedback (RLHF) — noting "RLHF does
             not significantly affect the base GPT-4 model's capability."
Paraphrase:  GPT-4's report discloses no parameter count or architecture and adds
             an RLHF post-training stage, so neither GPT-1's openness nor its
             two-stage shape survives intact.
Locators:    Sec. 1 (Introduction), the disclosure paragraph; Sec. on RLHF /
             model capability (the "does not significantly affect" evaluation).
Quote:       "this report contains no further details about the architecture
             (including model size), hardware, training compute, dataset
             construction, training method, or similar."
```

```text
URL:         https://arxiv.org/abs/1506.06724
Kind:        primary for the corpus-size claim. Zhu, Kiros, Zemel, Salakhutdinov,
             Urtasun, Torralba, Fidler, "Aligning Books and Movies," ICCV 2015.
             This is the paper that built BooksCorpus, so it owns the corpus
             statistics. arXiv abstract page is its own page.
Establishes: The origin figures for the dataset GPT-1 trained on. Table 2:
             11,038 books, 74,004,228 sentences, 984,846,357 words (~1 billion),
             1,316,420 unique words. The corpus spans 16 genres (Romance 2,865,
             Fantasy 1,479, Science fiction 786, Teen 430, etc.), and included
             only books over 20K words, from unpublished authors on the web.
Paraphrase:  The source corpus as first published held 11,038 books and about a
             billion words across 16 genres — more books than the "over 7,000"
             GPT-1 reports using.
Locators:    Sec. 3 (The MovieBook and BookCorpus Datasets), Table 2 and the
             surrounding paragraph on genres and the 20K-word filter.
Quote:       "# of books: 11,038 ... # of words: 984,846,357"
```

```text
URL:         https://arxiv.org/abs/1804.07461
Kind:        primary for what the GLUE score refers to; used only for context, not
             to re-teach the benchmark (a neighbor piece owns GLUE). Wang, Singh,
             Michael, Hill, Levy, Bowman, "GLUE," 2018. arXiv abstract is its own
             page.
Establishes: GLUE is "a suite of nine sentence or sentence-pair NLU tasks." This
             fixes what GPT-1's reported GLUE score of 72.8 is a score *on*: an
             aggregate over nine tasks. GPT-1 draws several of its individual
             datasets (CoLA, SST-2, MRPC, STS-B, QQP, MNLI, QNLI, RTE) from GLUE.
Paraphrase:  GLUE bundles nine language-understanding tasks into one aggregate
             score; GPT-1's 72.8 is that aggregate.
Locators:    Abstract; Sec. 1 ("collection of NLU tasks"); the "In summary, we
             offer: (i) A suite of nine ... NLU tasks" contribution list.
Quote:       "A suite of nine sentence or sentence-pair NLU tasks"
```

## Contradictions

- **The paper reports no parameter count at all.** The commission asks to verify
  the parameter count firsthand against the paper. It cannot be. The GPT-1 PDF
  gives layers (12), state width (768), heads (12), and FFN width (3072), but
  never a total. The universally cited "117 million" is not GPT-1's own number;
  it is the GPT-2 report's figure for its smallest model, which that report calls
  "equivalent to the original GPT." A lesson that says "GPT-1 had 117M parameters"
  is citing GPT-2, and should either attribute it that way or say the paper left
  the total unstated.

- **Corpus size disagrees with its origin.** GPT-1 says "over 7,000 unique
  unpublished books"; the BooksCorpus origin paper reports 11,038 books. The word
  "unique" in GPT-1 suggests OpenAI deduplicated or filtered the set, but the
  paper does not explain the gap. State the corpus as GPT-1 states it ("over
  7,000 books"), not as the round 11,038 from the origin, and flag that the two
  numbers differ if the lesson names both.

- **The auxiliary LM objective slightly hurt the average.** The paper frames the
  fine-tuning-time auxiliary language-modeling objective as helpful ("improving
  generalization ... and accelerating convergence," Sec. 3.2). But its own
  ablation (Table 5) shows the full model with the auxiliary objective scoring
  74.7 average, versus 75.0 *without* it. The paper's honest reading — "the
  auxiliary objective helps on the NLI tasks and QQP ... larger datasets benefit
  from the auxiliary objective but smaller datasets do not" — qualifies the
  headline: on the unweighted average, removing it was a wash to slightly better.

- **One headline task was a loss, not a win.** On RTE the model scored 56.0%,
  "which is below the 61.7% reported by a multi-task biLSTM model" (Sec. 4.2). The
  "9 of 12" claim is honest precisely because 3 datasets were not improved: RTE
  (56.0 vs 61.7), MRPC (F1 82.3 vs 86.0 for TF-KLD), and SST-2 (91.3% vs 93.2%
  for Sparse byte mLSTM), which the paper calls only "competitive." A lesson
  should not imply a clean sweep.

- **The GLUE gain is stated two different ways.** The introduction claims "5.5%
  on the recently introduced GLUE multi-task benchmark." The body (Sec. 4.2,
  Classification) reports the GLUE score as 72.8 "significantly better than the
  previous best of 68.9" — a 3.9-point gap, not 5.5. The two use different
  reference baselines (the 5.5 figure is not reconcilable against 68.9 from the
  paper's own text). If the lesson quotes a GLUE improvement, prefer the body's
  concrete "72.8 vs 68.9" and avoid the intro's 5.5% without a stated baseline.

- **The framing itself is what later practice discarded.** The paper's central
  mechanism — supervised fine-tuning per task plus task-specific input
  transformations — is exactly the part GPT-2, GPT-3, and GPT-4 moved away from.
  GPT-2 does downstream tasks "without any parameter or architecture
  modification"; GPT-3 applies the model "without any gradient updates or
  fine-tuning"; GPT-4 adds RLHF and discloses none of its architecture. The
  surviving half is the unsupervised generative pre-training. This is not a
  contradiction against the commission (the commission asks for it) but it is the
  contradiction against the *paper's own 2018 self-description* that the editor
  will test: the recipe's ancestor kept the pre-training and dropped nearly
  everything the paper spends Section 3.3 building.

## Numbers

```text
Figure: 12 transformer layers; 768-dimensional states; 12 attention heads; 3072-dim FFN inner states
Owner:  GPT-1 paper, Sec. 4.1 (Model specifications)
Scope:  The single trained model. No total parameter count is given in the paper.
```

```text
Figure: ~117 million parameters (GPT-1's size, as attributed later)
Owner:  GPT-2 paper, Table 2 (smallest model, "equivalent to the original GPT"). NOT stated in GPT-1.
Scope:  Total trainable parameters of the model architecture GPT-1 used.
```

```text
Figure: over 7,000 unique unpublished books (training corpus)
Owner:  GPT-1 paper, Sec. 4.1. Origin BooksCorpus (Zhu et al. 2015) Table 2 reports 11,038 books / ~984.8M words.
Scope:  The unlabeled pre-training corpus. GPT-1's count is lower than the origin's; the gap is unexplained.
```

```text
Figure: 18.4 token-level perplexity on BooksCorpus
Owner:  GPT-1 paper, Sec. 4.1
Scope:  The pre-trained language model's fit to its own training corpus.
```

```text
Figure: 12 datasets evaluated; state of the art improved on 9; 4 task types
Owner:  GPT-1 paper, Abstract, Table 1, Sec. 4.2
Scope:  NLI (5: SNLI, MNLI, QNLI, RTE, SciTail), QA (2: RACE, Story Cloze), similarity (3: MRPC, QQP, STS-B), classification (2: CoLA, SST-2). Not improved: RTE, MRPC, SST-2.
```

```text
Figure: headline absolute gains — Story Cloze +8.9, RACE +5.7 (overall), MNLI +1.5, SNLI +0.6, SciTail +5.0, QNLI +5.8
Owner:  GPT-1 paper, Abstract and Sec. 4.2, Tables 2-3
Scope:  Absolute point gain over the prior best reported per dataset. Note the spread: some large (8.9), some small (0.6).
```

```text
Figure: CoLA 45.4 (vs prior best 35.0); GLUE aggregate 72.8 (vs prior best 68.9); SST-2 91.3%
Owner:  GPT-1 paper, Sec. 4.2 and Table 4
Scope:  CoLA Matthews correlation; GLUE nine-task aggregate; SST-2 accuracy. SST-2 did not beat the 93.2 prior best.
```

```text
Figure: ablations — full 74.7; no pre-training 59.9 (−14.8); no aux LM 75.0; LSTM w/ aux LM 69.1 (−5.6)
Owner:  GPT-1 paper, Table 5 and Sec. 5
Scope:  Unweighted average score across the ablation task set. Removing pre-training is the largest single hit (14.8 points); removing the auxiliary objective slightly raised the average.
```

```text
Figure: scaling of the descendants — GPT-1 ~117M -> GPT-2 1542M (1.5B) -> GPT-3 175B
Owner:  GPT-2 paper Table 2 (117M, 1542M); GPT-3 paper Abstract/Sec. 1 (175B)
Scope:  Total parameters. GPT-3 is ~1,500x GPT-1 (175,000M / 117M ~= 1,496). A usable anchor for "how small it was." GPT-4 discloses no count.
```

## Source assets

```text
Asset: Figure 1 (GPT-1 paper, page 4). Left: the Transformer stack with the two
       training objectives. Right: the four input-transformation diagrams
       (classification, entailment, similarity, multiple choice), each showing
       Start/Delimiter/Extract tokens feeding one linear+softmax head.
Shows: The paper's actual thesis in one image — one frozen architecture, four
       task shapes, handled by rewriting each task's structured input into a
       single token sequence. It is the clearest possible illustration of the
       exact mechanism later models dropped.
Crop:  Keep the right-hand panel intact with all four rows and their token labels;
       the left stack can be omitted or kept small. Do not crop away the
       Delimiter/Extract tokens — they are the point.
```

```text
Asset: Figure 2 left (GPT-1 paper, page 7). Accuracy on MultiNLI and RACE as a
       function of the number of pre-trained layers transferred.
Shows: The rising curve — each transferred Transformer layer adds task
       performance, "up to 9% for full transfer on MultiNLI." Concrete evidence
       that depth of pre-training, not just embeddings, carries the transfer.
Crop:  Retain both axes and both task curves; keep the x-axis (layers 0-12)
       legible. Note the non-zero y-axis baseline if reproduced.
```

```text
Asset: Table 5 (GPT-1 paper, page 8). The ablation grid: full model vs. no
       pre-training vs. no auxiliary LM vs. LSTM.
Shows: The two honest qualifiers in one place — pre-training is worth 14.8 points,
       and the auxiliary objective is not (75.0 without vs 74.7 with).
Crop:  Keep the "Avg. Score" column and the four method rows; per-task columns are
       optional. The contrast lives in the average column.
```

None of the later-report PDFs offer a visual this lesson needs; their role here is
the parameter and framing text, not a figure.

## Discarded

```text
URL: https://openai.com/index/language-unsupervised/  — OpenAI's own announcement
     blog for GPT-1. Live but Cloudflare-gated (403 to automated and browser-UA
     requests alike). Not recorded as a citable URL because it will not resolve
     for a fetcher; the cdn PDF above is the same content and resolves cleanly.
     It is secondary anyway (announcement, not the paper).
```

```text
URL: The 1B Word Benchmark (referenced in GPT-1 Sec. 4.1 as ELMo's corpus, "shuffled
     at a sentence level"). Read the mention; not opened as a source. It is a
     contrast the paper draws, not a claim this lesson rests on, so citing it would
     be padding against the source floor rather than changing the interpretation.
```
