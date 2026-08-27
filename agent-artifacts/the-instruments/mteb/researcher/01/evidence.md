# Evidence record: the-instruments/mteb (01)

The evidence supports the commissioned mechanism in full and pins every count to a
dated version. MTEB v3 (submitted October 2022, last revised 19 March 2023) spans
8 task types, 58 datasets, 112 languages, and 33 benchmarked models; the per-task
main metrics named in the commission are verified word for word from the paper's
own descriptions; the overall score is a plain average of each dataset's main
metric across all datasets, and the leaderboard sorts on that mean. Both weaknesses
the commission names are acknowledged by the maintainers in their own writing, but
the timeline needs care and is the record's most useful correction: task imbalance
was flagged by the original authors in the original 2022 paper's own limitations
section, while contamination was first dismissed by those same authors in that same
paper and only reversed later, by the maintainers, in the 2025 revision work
(MMTEB, the "Maintaining MTEB" engineering paper, and the RTEB writeup). The
revision answers imbalance with Borda-count rank aggregation plus a per-category
average, and answers contamination by making the benchmark zero-shot (excluding
MS MARCO and Natural Questions) and, in RTEB, by holding out private datasets.

The record is thin on one point the writer must not overstate: no single named model
is documented topping the overall MTEB mean while being specifically weak at
retrieval. That claim is supported as a property of the averaging method and by both
maintainer and independent statements that a model's overall rank and its
per-category rank diverge, not by one verified chart-topper who flopped at
retrieval. The e5-mistral case below concerns a contamination leak percentage, not
retrieval weakness. Frame the "ordinary at retrieval" point as a mechanism, not as a
named scandal.

## Sources

```text
URL:         https://arxiv.org/abs/2210.07316
Kind:        primary. The paper that owns MTEB; the authors define the datasets,
             the per-task metrics, the averaging, and the benchmark's stated limits.
Establishes: The dated benchmark shape (v3, rev. 19 Mar 2023): 8 task types, 58
             datasets, 112 languages, 33 models. The main metric per task type. That
             the overall score is a plain average over all datasets. That the
             authors named task imbalance as a limitation and, separately, dismissed
             data contamination.
Paraphrase:  MTEB spans 8 embedding tasks over 58 datasets and 112 languages;
             33 models were run. Each task type is scored by one main metric:
             bitext mining by F1; classification by accuracy; clustering by
             v-measure; pair classification by average precision on cosine
             similarity; reranking by MAP; retrieval by nDCG@10; STS by Spearman
             correlation on cosine similarity; summarization by Spearman correlation
             on cosine similarity. Table 1 (the English results) reports the "Average
             of the main metric" across 56 datasets, the 58 minus the 2 multilingual
             bitext-mining sets. In the limitations appendix the authors write that
             because task types hold different numbers of datasets, the average,
             computed over all datasets, is biased toward the tasks with many
             datasets (retrieval, classification, clustering). Earlier, discussing
             reranking, they note SciDocsRR appears to overlap some models' training
             data, then state they ignore such overlap in the scores and believe the
             effect insignificant "as long as enough datasets are averaged."
Locators:    Abstract (counts). Section 3.2 task/metric descriptions. Table 1
             caption and header ("Average of the main metric"; "56"). Section 5
             "Reranking" paragraph (contamination dismissal). Appendix B
             "Limitations of MTEB," item 2 "Task imbalance."
Quote:       Metrics, verbatim: "F1 serves as the main metric for bitext mining."
             "The main metric is accuracy with average precision and f1 additionally
             provided." "The model is scored using v-measure." "The average precision
             score based on cosine similarity is the main metric." "Metrics are mean
             MRR@k and MAP with the latter being the main metric." "nDCG@10 serves as
             the main metric." (STS and summarization) "Spearman correlation based on
             cosine similarity serves as the main metric."
             Imbalance, verbatim (Appendix B.2): "Tasks in MTEB have a different
             amount of datasets with summarization consisting of only a single
             dataset. This means MTEB average scores, which are computed over all
             datasets, are biased towards tasks with many datasets, notably
             retrieval, classification and clustering."
             Contamination dismissal, verbatim (Section 5): "Our scale of experiments
             and that of model pre-training make controlling for data contamination
             challenging. Thus, we ignore overlap of MTEB datasets with model
             training datasets in MTEB scores. As long as enough datasets are
             averaged, we believe these effects to be insignificant."
```

```text
URL:         https://arxiv.org/abs/2502.13595
Kind:        primary. The maintainers' revision. Lead author Kenneth Enevoldsen;
             original MTEB lead Niklas Muennighoff is a co-author, so this is the same
             team revising its own benchmark. Published at ICLR 2025.
Establishes: What the revision changed to answer imbalance and contamination: rank
             aggregation by Borda count plus a per-category average, and a zero-shot
             design that excludes the datasets models fine-tune on. The revision's
             own scale.
Paraphrase:  MMTEB is a community-driven expansion of MTEB covering more than 500
             quality-controlled tasks across 250+ languages, with new task kinds
             (instruction following, long-document retrieval, code retrieval). To cut
             cost it downsamples by inter-task correlation and samples hard negatives.
             On aggregation, it reports scores across all tasks, scores per task
             category, and model ranks computed with the Borda count method from
             social choice theory, which it says is more robust for comparing NLP
             systems than a raw mean; results tables are ranked by Borda count and it
             also provides an average weighted by task category. It is designed as a
             zero-shot benchmark, excluding datasets frequently used in fine-tuning,
             naming MS MARCO and Natural Questions. The best publicly available model
             it finds is multilingual-e5-large-instruct at 560 million parameters, not
             a billion-parameter LLM.
Locators:    Abstract (500+ tasks, 250+ languages; downsampling; zero-shot English
             benchmark). Section 2.4 / benchmark-construction (zero-shot, MS MARCO and
             Natural Questions exclusion). Section 3.x on results reporting (Borda
             count; per-category scores). Table 2 area ("ranked using Borda count...
             weighted by task category").
Quote:       Zero-shot, verbatim: "To prevent overfitting, we intend it as a
             zero-shot benchmark, excluding tasks like MS MARCO (Nguyen et al., 2016)
             and Natural Questions (Kwiatkowski et al., 2019), which are frequently
             used in fine-tuning."
             Aggregation, verbatim: reports "scores across all tasks, scores per task
             category, and ... ranks using the Borda count method (Colombo et al.,
             2022)," a method "derived from social choice theory ... shown to be more
             robust for comparing NLP systems."
```

```text
URL:         https://arxiv.org/abs/2506.21182
Kind:        primary. "Maintaining MTEB," by the maintainers (Isaac Chung, Imene
             Kerboua, Márton Kardos, Roman Solomatin, Kenneth Enevoldsen). Their own
             account of the contamination problem and the fix they shipped.
Establishes: That the maintainers now treat benchmark overfitting as real, name the
             specific mechanism (training on splits from the same source as the
             evaluation tasks), and quantify it with a zero-shot score. A concrete
             per-model leak figure.
Paraphrase:  The paper states that the highest-ranking models on the legacy English
             MTEB reach their scores by training on the benchmark's tasks, and that
             lower-scoring models may generalize better out of distribution. It calls
             this a subtler problem than classic test-set leakage: models train on
             datasets that share a source with the evaluation tasks. The fix is a
             transparency approach: contributors disclose training datasets, and a
             zero-shot score z = 1 - n_train / n_total is computed, where n_train is
             the number of benchmark datasets a model trained on and n_total the total.
             Worked example: e5-mistral-7b-instruct scores 95% zero-shot on MTEB
             (English, v2), meaning it trained on only about 5% of the benchmark's
             training splits, a 5% leak; it still performs strongly, which the authors
             read as genuine generalization.
Locators:    Section 5.1 "Case Study 1: Assessing zero-shot levels." Figure 2 and its
             caption. The zero-shot-score definition and the e5-mistral example
             immediately following.
Quote:       Figure 2 caption, verbatim: "Models' mean performance against their
             zero-shot score on the legacy English MTEB. The highest ranking models
             achieve their scores by training on benchmark tasks, even though models
             with lower scores might generalize better to out-of-distribution
             environments."
             Mechanism, verbatim: "Unlike traditional data leakage (where test
             examples appear in training data) ... MTEB faces a more nuanced
             challenge: models being trained on datasets ... using training splits from
             the same source as benchmark evaluation tasks."
```

```text
URL:         https://huggingface.co/blog/rteb
Kind:        primary. RTEB announcement (1 Oct 2025), from the MTEB maintainers and
             collaborators (Kenneth Enevoldsen named). The maintainers' own statement
             of the generalization gap and the private-dataset remedy.
Establishes: The maintainers' plainest wording that public-benchmark scores diverge
             from real performance, and the specific remedy of maintainer-held private
             datasets. Distinct from MMTEB's remedy.
Paraphrase:  When models are repeatedly evaluated on the same public datasets, a gap
             opens between reported scores and performance on new, unseen data; when
             training sources overlap evaluation data a score inflates and undermines
             the benchmark's integrity. RTEB pairs open datasets with private ones
             kept by the maintainers and scored by them; a large open-vs-private gap
             signals overfitting.
Locators:    Opening problem statement; "Private Datasets" section.
Quote:       Verbatim: "When models are repeatedly evaluated against the same public
             datasets, a gap emerges between their reported scores and their actual
             performance on new, unseen data." "When training data sources overlap
             with evaluation datasets, a model's score can become inflated,
             undermining a benchmark's integrity." "A model with a significant
             performance drop between the open and the private datasets would suggest
             overfitting, providing a clear signal to the community."
```

```text
URL:         https://huggingface.co/spaces/mteb/leaderboard
Kind:        primary. The MTEB leaderboard itself, the ranked table people read,
             maintained by the mteb organization. It is the leaderboard, distinct
             from the benchmark (the datasets and scoring above).
Establishes: That the leaderboard exists as a live public ranked table and is the
             artifact teams actually consult, separate from the paper.
Paraphrase:  A Hugging Face Space run by the mteb organization presenting the ranked
             leaderboard. The table is rendered client-side and did not load as static
             text, so column names and the current live ranking method could not be
             read directly from the page; the ranking mechanics are documented in the
             MMTEB paper (Borda count) and the leaderboard blog below.
Locators:    Space header; the page loads its table dynamically.
Quote:       None readable (dynamic page).
```

```text
URL:         https://huggingface.co/blog/Samoed/mteb-v3-leaderboard
Kind:        primary. Maintainers' documentation of the v3 leaderboard (authors
             include Roman Solomatin, Kenneth Enevoldsen, Isaac Chung).
Establishes: That the leaderboard is meant to be filtered to the tasks a reader
             cares about, and that a default pre-defined board covers only part of
             them, which supports the point that retrieval is one slice of the mean.
Paraphrase:  The maintainers describe the rebuilt leaderboard as customizable and
             note that a pre-defined leaderboard may contain only about half of the
             tasks a given user cares about, encouraging users to build their own view
             rather than trust one overall number. It does not spell out the ranking
             algorithm.
Locators:    Body, on customization and task coverage.
Quote:       Verbatim: "A pre-defined leaderboard might only contain 50% of the tasks
             that you care about."
```

```text
URL:         https://zeroentropy.dev/concepts/mteb/
Kind:        secondary, with a commercial stake. Written by Alexander Rocha, founding
             engineer at ZeroEntropy, which sells a competing embedding model
             (zembed-1). It reports on the overfitting phenomenon from outside the
             maintaining party but promotes its own product, so it is context, not an
             independent judge.
Establishes: That the leaderboard-overfitting and contamination concern is discussed
             outside the maintainers, and names the binary-vs-graded-relevance issue
             in retrieval scoring. One of two independent retellings of the phenomenon.
Paraphrase:  The page argues MTEB uses binary relevance labels while real retrieval is
             graded, that models show within-dataset overfitting by training on MTEB
             splits and then underperforming on held-out corpora, and that many
             embedding models train on data overlapping MTEB datasets or close
             paraphrases, contaminating the leaderboard. It offers its own model as
             performing better under graded evaluation.
Locators:    Body sections on relevance labels, leaderboard tuning, contamination.
Quote:       Verbatim: "many embedding models are partially trained on data that
             overlaps with MTEB datasets (or close paraphrases). This contaminates the
             leaderboard."
```

```text
URL:         https://modal.com/blog/mteb-leaderboard-article
Kind:        secondary. Yiren Lu, Modal (30 Oct 2025), independent of the MTEB
             maintainers. Vendor blog but not selling an embedding model; used for the
             averaging point.
Establishes: An independent statement that the overall average mixes task categories,
             so a model's overall rank need not track the categories that matter for
             search and RAG. Second independent retelling.
Paraphrase:  The post explains that a model tuned for retrieval and STS, the two
             categories most correlated with production RAG and search, can be dragged
             down on the average by weaker clustering or classification, and that no
             benchmark captures a specific corpus, so the decisive test is performance
             on your own data.
Locators:    Body, on interpreting the overall score.
Quote:       Verbatim: "a model tuned for retrieval and semantic textual similarity
             (the two categories most correlated with production performance in RAG
             and search) may underperform on clustering or classification, which
             brings down the average."
```

## Contradictions

- The maintainers reversed themselves on contamination. In 2022 the original authors
  wrote that they "ignore overlap of MTEB datasets with model training datasets" and
  believed the effect "insignificant" as long as enough datasets are averaged
  (2210.07316, Section 5). By 2025 the same team treats overfitting as a first-order
  problem worth a zero-shot score, a zero-shot benchmark design, and a private-dataset
  benchmark (2506.21182; 2502.13595; RTEB). The writer should present this as a
  changed position over time, not as a single steady maintainer view. The commission's
  phrasing that the maintainers "have flagged contamination" is true only of the later
  work.

- Timeline on imbalance vs. contamination differ, against the commission's grouping.
  Task imbalance was flagged inside the original 2022 paper's own limitations
  (Appendix B.2). Contamination was flagged only later. Treating both as things the
  maintainers "flagged... and rebuilt the benchmark partly to answer" is right for
  contamination and only half-right for imbalance: imbalance was a stated known
  limitation from day one.

- The revision does not simply replace the biased mean. MMTEB reports the plain
  per-task-and-per-category scores and adds Borda-count ranking and a
  category-weighted average on top (2502.13595). The old plain average still exists;
  the fix is an added, more robust ranking, not a deletion of the mean. Do not write
  that MMTEB "removed" the biased average.

- Direction of the retrieval example is not settled by a named case. The commission's
  angle says a model can top the overall mean while being ordinary at retrieval. The
  Modal source states the opposite-direction case (a retrieval-strong model dragged
  down by weak clustering/classification), and the original paper only shows that
  models "rank significantly differently" across task types and that "no particular
  text embedding method dominates across all tasks." The mechanism is sound in both
  directions; a specific chart-topper who was weak at retrieval is not in the record.

## Numbers

```text
Figure: 8 task types
Owner:  MTEB paper (2210.07316), abstract
Scope:  MTEB v3, submitted Oct 2022, last revised 19 Mar 2023

Figure: 58 datasets
Owner:  MTEB paper (2210.07316), abstract
Scope:  MTEB v3. Full benchmark including 2 multilingual bitext-mining datasets.

Figure: 112 languages
Owner:  MTEB paper (2210.07316), abstract
Scope:  MTEB v3.

Figure: 33 models benchmarked
Owner:  MTEB paper (2210.07316), abstract
Scope:  MTEB v3, initial paper run.

Figure: per-task-type dataset counts: bitext mining 2, classification 12,
        clustering 11, pair classification 3, reranking 4, retrieval 15, STS 10,
        summarization 1 (sum = 58)
Owner:  MTEB paper (2210.07316), Section 3 and Table 1 header
Scope:  MTEB v3. The English Table 1 sums to 56, the 58 minus the 2 bitext sets.

Figure: retrieval 15 datasets vs summarization 1 dataset
Owner:  MTEB paper (2210.07316)
Scope:  The concrete face of the imbalance: the average weights retrieval 15x the
        weight it gives summarization, purely by dataset count.

Figure: main metric per task type: F1 (bitext), accuracy (classification),
        v-measure (clustering), average precision on cosine (pair classification),
        MAP (reranking), nDCG@10 (retrieval), Spearman on cosine (STS), Spearman on
        cosine (summarization)
Owner:  MTEB paper (2210.07316), Section 3.2 metric descriptions
Scope:  MTEB v3.

Figure: 95% zero-shot score for e5-mistral-7b-instruct, i.e. ~5% leak
Owner:  Maintaining MTEB (2506.21182), Section 5.1
Scope:  MTEB (English, v2). z = 1 - n_train/n_total; the model trained on ~5% of the
        benchmark's training splits.

Figure: 500+ tasks, 250+ languages
Owner:  MMTEB paper (2502.13595), abstract
Scope:  MMTEB, the multilingual revision, ICLR 2025.
```

## Source assets

```text
Asset: MTEB paper (2210.07316), Table 1 header row, showing the per-task-type dataset
       counts and the "Avg." column (Class. 12, Clust. 11, PairClass. 3, Rerank. 4,
       Retr. 15, STS 10, Summ. 1, Avg. over 56).
Shows: That the overall number is one flat average over datasets whose counts per task
       type are wildly uneven, so the mean is a dataset-weighted blend.
Crop:  Must retain the task-type labels and their dataset counts and the Avg. column
       header. A model row or two can stay to show the single number the reader sorts
       on; drop the long tail of models.

Asset: Maintaining MTEB (2506.21182), Figure 2, mean performance vs zero-shot score on
       legacy English MTEB.
Shows: That the top-mean models sit at lower zero-shot scores, the visual form of "the
       highest ranking models achieve their scores by training on benchmark tasks."
Crop:  Must retain both axes (mean performance and zero-shot score) and the caption.
       Do not crop to only the high-mean corner; the relationship is the point.

Asset: MTEB paper (2210.07316), Appendix B "Limitations of MTEB," item 2 "Task
       imbalance."
Shows: The authors stating the imbalance in their own words. Better as a pull quote
       than a screenshot, but the passage is the load-bearing admission.
Crop:  If shown as text, keep the full sentence naming summarization's single dataset
       and the bias toward retrieval, classification, clustering.
```

## Discarded

```text
URL: https://huggingface.co/papers/2502.13595 — Hugging Face landing page for the MMTEB
     paper; a portal, superseded by the arXiv primary read in full.
URL: https://www.semanticscholar.org/paper/... (MTEB and MMTEB) — index pages, not the
     source text.
URL: https://openreview.net/forum?id=zl3pfz4VCV — MMTEB review forum; the camera-ready
     arXiv version was read instead.
URL: https://www.geeksforgeeks.org/artificial-intelligence/mteb-leaderboard/ — tutorial
     content, no primary claim and no independent reporting worth citing.
URL: https://octen-team.github.io/octen_blog/posts/octen-rteb-first-place/ — a vendor
     announcing a first-place RTEB result; promotional, adds nothing verifiable to the
     mechanism or the concerns.
```
