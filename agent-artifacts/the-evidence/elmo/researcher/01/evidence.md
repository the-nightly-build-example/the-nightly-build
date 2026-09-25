# evidence: the-evidence/elmo (01)

The commission's spine is fully supported by the two primary papers. The ELMo
paper (arXiv:1802.05365) states its own mechanism (a frozen two-layer biLSTM
language model whose internal states are combined per task and concatenated as
features into an existing supervised model) and reports the six-task Table 1
numbers, so the "idea vs machinery" split can be shown from the paper's own
words and results. The BERT paper (arXiv:1810.04805) names ELMo directly, files
it under "feature-based," contrasts it with fine-tuning, and calls ELMo's design
a "shallow concatenation of independently trained left-to-right and
right-to-left LMs" — the machinery BERT replaced. The "ImageNet moment for NLP"
framing is datable and attributable to Sebastian Ruder (The Gradient, 8 July
2018), but with an important qualification: Ruder applied it to the joint arrival
of ELMo, ULMFiT and the OpenAI transformer, not to ELMo alone, so a lesson that
credits the phrase to ELMo specifically would misattribute it. The credit
picture is complicated by two prior/concurrent primaries, CoVe (Aug 2017) and
ULMFiT (Jan 2018), recorded under Contradictions. What is thin: I could not
verify a total parameter count for the ELMo biLM (units and layers are stated,
a single parameter total is not in the passages I read), and I did not find a
primary claim that ELMo's biLSTM-feature recipe stayed competitive after BERT.

## Sources

```text
URL:         https://arxiv.org/abs/1802.05365
Kind:        primary — it is the ELMo paper; it owns its own method and its six-task results.
Establishes: What ELMo is and does, firsthand: contextual word representations
             from a pretrained deep biLM; the task-specific weighted combination
             of layers; the feature-based (concatenate, biLM frozen) use; and the
             Table 1 gains on six tasks.
Paraphrase:  ELMo assigns each token a representation that is a function of the
             entire input sentence, computed from the internal states of a
             pretrained bidirectional language model. Higher biLSTM layers
             capture context-dependent aspects of meaning; lower layers capture
             syntax. For each task, ELMo is a learned weighted sum of all biLM
             layers, scaled by one scalar; the weights and scalar are learned by
             the downstream task. To use it, the biLM weights are frozen and the
             ELMo vector is concatenated with the model's existing input.
Locators:    Abstract; Intro; §3.2 (ELMo definition, equation); §3.3 (use in a
             supervised model, "freeze the weights ... concatenate"); §3.4
             (biLM architecture); §4/Table 1 (six-task results).
Quote:       "We introduce a new type of deep contextualized word representation
             that models both (1) complex characteristics of word use (e.g.,
             syntax and semantics), and (2) how these uses vary across linguistic
             contexts (i.e., to model polysemy). Our word vectors are learned
             functions of the internal states of a deep bidirectional language
             model (biLM), which is pre-trained on a large text corpus." (Abstract)
             "Our representations differ from traditional word type embeddings in
             that each token is assigned a representation that is a function of the
             entire input sentence." (Intro)
             "the higher-level LSTM states capture context-dependent aspects of
             word meaning (e.g., they can be used without modification to perform
             well on supervised word sense disambiguation tasks) while lower-level
             states model aspects of syntax". (Intro)
             "To add ELMo to the supervised model, we first freeze the weights of
             the biLM and then concatenate the ELMo vector ... with x_k and pass
             the ELMo enhanced representation into the task RNN." (§3.3)
             Architecture: "The final model uses L=2 biLSTM layers with 4096 units
             and 512 dimension projections and a residual connection from the
             first to second layer. The context insensitive type representation
             uses 2048 character n-gram convolutional filters followed by two
             highway layers and a linear projection down to a 512 representation."
             (§3.4)
             Training data: "After training for 10 epochs on the 1B Word Benchmark
             (Chelba et al., 2014)". (§3.4)
```

```text
URL:         https://arxiv.org/abs/1810.04805
Kind:        primary — it is the BERT paper; it owns its own positioning of BERT
             against ELMo and its feature-based vs fine-tuning framing.
Establishes: Firsthand, how the field named and then displaced ELMo's mechanism:
             ELMo is the "feature-based" approach that uses task-specific
             architectures with the pretrained representations added as features;
             BERT is fine-tuning, with minimal task-specific parameters; ELMo is a
             "shallow concatenation" of two independent unidirectional LMs, which
             a deep bidirectional model is argued to beat.
Paraphrase:  BERT sorts pretraining transfer into two strategies. Feature-based
             (ELMo) keeps a task-specific model and feeds it the pretrained
             vectors as extra features. Fine-tuning (OpenAI GPT, and BERT) adds
             almost no task-specific parameters and trains all pretrained
             parameters on the task. BERT casts ELMo's forward-plus-backward LM
             design as a shallow concatenation of two separately trained
             directional models and argues a jointly bidirectional model is
             strictly more powerful.
Locators:    Intro; §2.1 "Unsupervised Feature-based Approaches"; §2 framing of
             feature-based vs fine-tuning.
Quote:       "The feature-based approach, such as ELMo (Peters et al., 2018a),
             uses task-specific architectures that include the pre-trained
             representations as additional features." (§2.1)
             "ELMo and its predecessor (Peters et al., 2017, 2018a) generalize
             traditional word embedding research along a different dimension. They
             extract context-sensitive features from a left-to-right and a
             right-to-left language model." (§2.1)
             "This is also in contrast to Peters et al. (2018a), which uses a
             shallow concatenation of independently trained left-to-right and
             right-to-left LMs." (Intro)
             "It is reasonable to believe that a deep bidirectional model is
             strictly more powerful than either a left-to-right model or the
             shallow concatenation of a left-to-right and a right-to-left model."
             (Intro)
```

```text
URL:         https://arxiv.org/abs/1606.05250
Kind:        primary — it is the SQuAD paper; it owns the SQuAD dataset and its
             scale that ELMo's SQuAD F1 (Table 1) is measured on.
Establishes: What the SQuAD task is and how big it is: 100,000+ crowd-written
             questions on Wikipedia articles, each answer a span of text from the
             passage. Needed because ELMo's largest headline gain (SQuAD) is a
             number owned by this dataset.
Paraphrase:  SQuAD is a reading-comprehension dataset of over 100,000 questions
             written by crowdworkers about Wikipedia passages, where each answer
             is a contiguous span from the passage. (Cited here only for the
             dataset's identity and scale; ELMo reports F1 on it.)
Locators:    Abstract; title.
Quote:       "We present the Stanford Question Answering Dataset (SQuAD), a new
             reading comprehension dataset consisting of 100,000+ questions posed
             by crowdworkers on a set of Wikipedia articles, where the answer to
             each question is a segment of text from the corresponding reading
             passage." (Abstract)
```

```text
URL:         https://arxiv.org/abs/1708.00107
Kind:        primary — it is the CoVe paper; it owns its own prior claim to
             contextualized word vectors.
Establishes: That contextualized word vectors predate ELMo: CoVe (McCann et al.,
             2017) took a deep LSTM encoder from a machine-translation model and
             used it to produce context vectors added to existing NLP models,
             improving several tasks. This bears on the credit question in the
             commission's angle.
Paraphrase:  CoVe contextualizes word vectors using a deep LSTM encoder from an
             attentional sequence-to-sequence machine-translation model, and adds
             these vectors on top of standard word/character vectors, improving
             sentiment, question classification, entailment and question
             answering. Its supervision source is translation, not a language
             model; ELMo's is an unlabeled-text language model.
Locators:    Abstract; title.
Quote:       "In this paper, we use a deep LSTM encoder from an attentional
             sequence-to-sequence model trained for machine translation (MT) to
             contextualize word vectors. We show that adding these context vectors
             (CoVe) improves performance over using only unsupervised word and
             character vectors on a wide variety of common NLP tasks". (Abstract)
```

```text
URL:         https://arxiv.org/abs/1801.06146
Kind:        primary — it is the ULMFiT paper; it owns its own concurrent claim
             to language-model pretraining plus fine-tuning.
Establishes: That LM pretraining as transfer learning was being demonstrated in
             the same window as ELMo (submitted 18 Jan 2018; ELMo v1 15 Feb 2018),
             and in the fine-tuning form (train the LM, then fine-tune it on the
             task) rather than ELMo's feature form. Bears on both credit and the
             idea/machinery split.
Paraphrase:  ULMFiT pretrains a language model and fine-tunes it for text
             classification, reducing error by 18-24% on most of six datasets and
             matching from-scratch training on 100x more data using only 100
             labeled examples. It is the fine-tuning use of LM pretraining, arriving
             alongside ELMo's feature-based use.
Locators:    Abstract; title; arXiv submission history (v1 18 Jan 2018).
Quote:       "We propose Universal Language Model Fine-tuning (ULMFiT), an
             effective transfer learning method that can be applied to any task in
             NLP ... Our method significantly outperforms the state-of-the-art on
             six text classification tasks, reducing the error by 18-24% on the
             majority of datasets." (Abstract)
```

```text
URL:         https://thegradient.pub/nlp-imagenet/
Kind:        secondary — a retrospective/analysis essay by a researcher writing
             about the field, not the authoring party of ELMo. Used only for the
             "ImageNet moment" framing and its attribution, never for a number.
Establishes: That the "ImageNet moment for NLP" phrase is datable and attributable
             (Sebastian Ruder, The Gradient, 8 July 2018) AND that Ruder applied it
             to the joint arrival of ELMo, ULMFiT and the OpenAI transformer, not
             to ELMo alone.
Paraphrase:  Ruder argues NLP has reached a watershed comparable to pretrained
             ImageNet models in vision, and cites ELMo, ULMFiT and the OpenAI
             transformer together as the methods that showed language-model
             pretraining works; he predicts practitioners will soon download
             pretrained language models instead of pretrained word embeddings.
Locators:    Title; opening/thesis paragraphs; the three-method paragraph.
Quote:       "Such methods herald a watershed moment: they may have the same
             wide-ranging impact on NLP as pretrained ImageNet models had on
             computer vision."
             "It is very likely that in a year's time NLP practitioners will
             download pretrained language models rather than pretrained word
             embeddings for use in their own models."
```

## Contradictions

- **Credit: ELMo did not originate contextualized representations.** CoVe (McCann
  et al., 2017, arXiv:1708.00107) produced contextualized word vectors from a
  machine-translation LSTM encoder and added them to existing models a year
  before ELMo. ELMo's own paper acknowledges predecessors. A lesson that says
  ELMo invented context-dependent word representations overstates it; the accurate
  claim is that ELMo made the language-model-pretraining version work broadly and
  set state of the art on six tasks at once.
- **Credit: LM pretraining transfer was concurrent, not ELMo-unique.** ULMFiT
  (Howard & Ruder, arXiv:1801.06146, submitted 18 Jan 2018) demonstrated
  language-model pretraining plus fine-tuning within weeks of ELMo's first version
  (15 Feb 2018), and in the fine-tuning form that BERT later generalized. The
  "pretraining era" has more than one origin document in this window.
- **The "ImageNet moment" is not ELMo-specific.** The datable source (Ruder, 8 July
  2018) attaches the phrase to ELMo + ULMFiT + OpenAI transformer jointly.
  Retrospective usage that pins it on ELMo alone is a later simplification, not
  what the cited source says.
- **"ELMo remained competitive" — not found in a primary.** I did not find a
  primary claim that ELMo's biLSTM feature-based recipe stayed competitive after
  BERT. BERT's paper positions ELMo as the feature-based baseline it improves on
  (§2.1). The evidence supports the commission's angle (the idea survived, the
  mechanism did not); it does not surface a strong counter-claim that the
  mechanism persisted. Recorded so the editor knows the counter-side was searched.

## Numbers

All from ELMo Table 1 ("Test set comparison of ELMo enhanced neural models with
state-of-the-art single model baselines across six benchmark NLP tasks"). The
"increase" column is absolute gain of ELMo+baseline over OUR BASELINE, and the
relative figure is that gain as a fraction of the baseline's remaining error.

```text
Figure: SQuAD — F1. Previous SOTA 84.4; baseline 81.1; ELMo+baseline 85.8; increase 4.7 / 24.9%.
Owner:  ELMo paper, Table 1 (SQuAD 1.1 dataset owned by arXiv:1606.05250).
Scope:  Single-model test-set F1 on SQuAD 1.1. Largest relative error reduction of the six.
```
```text
Figure: SNLI — accuracy. Previous SOTA 88.6; baseline 88.0; ELMo+baseline 88.7 ± 0.17; increase 0.7 / 5.8%.
Owner:  ELMo paper, Table 1.
Scope:  Test accuracy, textual entailment. Smallest absolute gain of the six.
```
```text
Figure: SRL (semantic role labeling) — F1. Previous SOTA 81.7; baseline 81.4; ELMo+baseline 84.6; increase 3.2 / 17.2%.
Owner:  ELMo paper, Table 1.
Scope:  Test F1.
```
```text
Figure: Coref (coreference resolution) — average F1. Previous SOTA 67.2; baseline 67.2; ELMo+baseline 70.4; increase 3.2 / 9.8%.
Owner:  ELMo paper, Table 1.
Scope:  Test average F1. Previous SOTA and baseline are the same number (67.2).
```
```text
Figure: NER (named entity recognition) — F1. Previous SOTA 91.93 ± 0.19; baseline 90.15; ELMo+baseline 92.22 ± 0.10; increase 2.06 / 21%.
Owner:  ELMo paper, Table 1 (CoNLL 2003 NER).
Scope:  Test F1.
```
```text
Figure: SST-5 (fine-grained sentiment, 5-class) — accuracy. Previous SOTA 53.7; baseline 51.4; ELMo+baseline 54.7 ± 0.5; increase 3.3 / 6.8%.
Owner:  ELMo paper, Table 1.
Scope:  Test accuracy, 5-class sentiment.
```
```text
Figure: biLM architecture — L=2 biLSTM layers, 4096 units, 512-dim projections, residual connection layer 1 to 2; character input = 2048 char n-gram convolutional filters + 2 highway layers + linear projection to 512.
Owner:  ELMo paper, §3.4.
Scope:  The final released biLM. A single total parameter count is not stated in the passages read.
```
```text
Figure: Training corpus — 1B Word Benchmark (Chelba et al., 2014), trained 10 epochs; ~30 million sentences.
Owner:  ELMo paper, §3.4 / related work.
Scope:  Unlabeled-text LM pretraining data.
```

## Limits

- No total parameter count for the ELMo biLM verified. Layers, units, projection
  dims and CNN filters are stated (§3.4); a single "N million/billion parameters"
  figure is not in the passages I read. If the lesson wants model size, use the
  architecture spec, not a parameter total.
- SQuAD's own metric definitions (Exact Match and F1) are not quoted from the
  SQuAD abstract, which states only the dataset and that answers are text spans.
  ELMo reports F1; that is safe. Do not attribute an EM/F1 definition to the SQuAD
  abstract without opening the SQuAD paper body.
- No primary evidence that ELMo's feature-based biLSTM recipe remained competitive
  after BERT; the record supports displacement, not persistence.
- Baseline model identities per task (e.g. which SQuAD or SNLI model ELMo was
  added to) are not individually verified here; only the metrics and numbers from
  Table 1 are. If the writer wants to name a baseline model, that needs a further
  read of ELMo §4.

## Source assets

```text
Asset: ELMo Table 1 — the six-task comparison (metric, previous SOTA, baseline, ELMo+baseline, absolute/relative increase). arXiv:1802.05365, §4.
Shows: The whole "six tasks at once" result and the honest spread of gains, from SQuAD's 24.9% relative error reduction down to SST-5's 6.8% and SNLI's 5.8%. Carries the scale point the series wants: the wins are real but uneven, not uniform.
Crop:  Keep the task column, the metric, and both the ELMo+baseline number and the relative-increase figure. Retain the SNLI/SST-5 rows so the small gains stay honest; do not crop to only the SQuAD row.
```
```text
Asset: ELMo Table 4 — nearest neighbors to the word "play" using GloVe (static) vs the biLM context embeddings. arXiv:1802.05365.
Shows: The core polysemy point directly — one word type gets different neighbors depending on sentence context under the biLM, unlike a fixed vector. This is the paper's own version of the "bank" example the commission uses.
Crop:  Keep both the GloVe column and the biLM/context column so the contrast is visible; keep at least two contrasting example sentences for "play."
```
```text
Asset: ELMo Figure 2 — "Visualization of softmax normalized biLM layer weights across tasks and ELMo locations." arXiv:1802.05365.
Shows: That the per-task weighting of biLM layers is real and differs by task — the "task-specific weighted combination of layers" made concrete. Useful only if the lesson chooses to teach the weighting mechanism; heavier than Table 1 or Table 4.
Crop:  Keep task labels and the layer-weight bars; retain the axis so the reader can read which layer is weighted where.
```

## Discarded

```text
URL: https://jalammar.github.io/illustrated-bert/ — surfaced in search ("The Illustrated BERT, ELMo, and co."); not opened/used. It is secondary explainer material; the framing it would support (ImageNet moment, feature-based vs fine-tuning) is already carried by the primaries and by Ruder, which are datable and attributable.
URL: https://arxiv.org/pdf/2010.04302 — "Masked ELMo" (2020); not used. It is later derivative work outside the commission's one-document scope and would pull the lesson into an NLP history the boundaries forbid.
URL: https://www.ruder.io/nlp-imagenet/ — the author's self-hosted mirror of the same Gradient essay; recorded the canonical thegradient.pub URL instead to avoid citing the same document twice.
```
