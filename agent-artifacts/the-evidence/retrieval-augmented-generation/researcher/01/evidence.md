# Evidence: the-evidence/retrieval-augmented-generation

The record covers the commission's angle from primaries in both eras. Lewis et
al. (2020) reported Exact Match gains of 3.0 points over DPR-extractive on
Natural Questions (44.5 vs 41.5) and 7.9 points over the T5-11B+SSM closed-book
baseline on the same benchmark (44.5 vs 36.6), plus wins on TriviaQA,
WebQuestions, and CuratedTrec; the numbers reproduce from the paper's Table 1. The primaries on modern RAG — Xu et al.
(ICLR 2024) on long-context-vs-retrieval, Barnett et al. (CAIN 2024) on
engineering failure modes, and Niu et al. (ACL 2024) on hallucination under
retrieval — all use off-the-shelf embedding models paired with off-the-shelf
LLMs with no joint training, and the Gao et al. survey defines "Naive RAG" as
that inference-time pipeline. Two things the record cannot cleanly deliver.
First, Lewis et al. did not train the retriever from scratch: they initialised
DPR from its pre-trained checkpoint, froze the document encoder and the FAISS
index, and only fine-tuned DPR's query encoder together with BART. The "joint
training" contrast with modern RAG holds, but the shape of it is narrower than
the commission's phrasing suggests — today's stack fine-tunes neither side, and
Lewis et al. fine-tuned one side. Second, no primary in the record measures
hallucination rate on the same model with and without retrieval. RAGTruth
reports rates under retrieval only; Lewis et al.'s own "hallucinates less" claim
is a 452-item Jeopardy pairwise human evaluation against BART, not a general
benchmark.

## Sources

```text
URL:         https://arxiv.org/abs/2005.11401
Kind:        primary — the paper the lesson teaches; authored by the team that
             built and evaluated the system (Facebook AI Research, Patrick Lewis
             et al.); published at NeurIPS 2020.
Establishes: The RAG method (DPR retriever + BART-large generator, marginalizing
             over top-K retrieved passages, jointly fine-tuned end-to-end with the
             document encoder frozen), the Wikipedia knowledge source (December
             2018 dump, 21M 100-word passages, FAISS/HNSW index), the four
             open-domain QA benchmarks (Natural Questions, TriviaQA, WebQuestions,
             CuratedTrec), and the reported Exact Match scores against closed-book
             and open-book baselines. Also establishes the paper's own hallucination
             claim on Jeopardy question generation, the FEVER results, and the
             index-hot-swap demonstration for updating world knowledge.
Paraphrase:  "We build RAG models where the parametric memory is a pre-trained
             seq2seq transformer, and the non-parametric memory is a dense vector
             index of Wikipedia, accessed with a pre-trained neural retriever."
             "The retriever (Dense Passage Retriever [26], henceforth DPR)
             provides latent documents conditioned on the input, and the seq2seq
             model (BART [32]) then conditions on these latent documents together
             with the input to generate the output." "Updating the document
             encoder BERTd during training is costly ... We do not find this step
             necessary for strong performance, and keep the document encoder (and
             index) fixed, only fine-tuning the query encoder BERTq and the BART
             generator." Table 1 EM scores: RAG-Sequence NQ 44.5, TQA 56.8 (open)
             / 68.0 (TQA-Wiki), WQ 45.2, CT 52.2; RAG-Token 44.1 / 55.2 / 66.1 /
             45.5 / 50.0. Baselines: DPR extractive 41.5 / 57.9 / 41.1 / 50.6;
             REALM 40.4 / — / 40.7 / 46.8; T5-11B closed-book 34.5 / — / 60.5 /
             37.4 / —; T5-11B+SSM 36.6 / — / 60.5 / 44.7 / —. Jeopardy human
             eval, 452 pairs: RAG more factual than BART in 42.7% of cases, BART
             more factual than RAG in 7.1%. FEVER label accuracy: 2-way 89.5%
             (within 2.7% of a RoBERTa baseline given gold evidence); 3-way 72.5%
             (within 4.3% of pipelined SoTA). Index hot-swap: 70% correct on 2016
             world leaders with the 2016 index, 68% correct on 2018 leaders with
             the 2018 index, 12% and 4% under the mismatched combinations.
Locators:    Abstract; §2.2 Retriever: DPR; §2.3 Generator: BART; §2.4 Training;
             §3 Experiments (Wikipedia dump and 21M documents); §4.1 Table 1;
             §4.4 (FEVER); §4.3 Table 4 (Jeopardy human eval); §4.5 (index
             hot-swap and hallucination-less claim on MSMARCO).
Quote:       "We do not find this step necessary for strong performance, and keep
             the document encoder (and index) fixed, only fine-tuning the query
             encoder BERTq and the BART generator."
```

```text
URL:         https://arxiv.org/abs/2004.04906
Kind:        primary — Karpukhin, Oğuz, Min, Lewis, Wu, Edunov, Chen, Yih at
             Facebook AI, Univ. of Washington, Princeton; EMNLP 2020; owns the
             DPR retriever architecture and its numbers.
Establishes: DPR's dual-encoder BERT-base architecture, in-batch negatives with
             one BM25 hard negative per question, the 21,015,324 Wikipedia
             passages built from the Dec. 20, 2018 English Wikipedia dump split
             into disjoint 100-word blocks, and the top-20/top-100 retrieval
             accuracy that RAG later relies on.
Paraphrase:  "Following (Lee et al., 2019), we use the English Wikipedia dump
             from Dec. 20, 2018 as the source documents ... We then split each
             article into multiple, disjoint text blocks of 100 words as
             passages, serving as our basic retrieval units, following (Wang et
             al., 2019), which results in 21,015,324 passages in the end." Table
             2 Top-20 (Multi encoder, no BM25 fusion): NQ 79.4, TriviaQA 78.8,
             WQ 75.0, TREC 89.1, SQuAD 51.6; BM25 (Lucene) baselines: 59.1,
             66.9, 55.0, 70.9, 68.8. Top-100 (Multi): NQ 86.0, TriviaQA 84.7,
             WQ 82.9, TREC 93.9, SQuAD 67.6; BM25: 73.7, 76.7, 71.1, 84.1, 80.0.
             Abstract's headline gap: "9%-19% absolute in terms of top-20 passage
             retrieval accuracy" over Lucene-BM25.
Locators:    Abstract; §4.1 Wikipedia Data Pre-processing; §4.2 QA Datasets;
             §5.1 Table 2 (main retrieval results); §3.2 Training (in-batch
             negatives).
```

```text
URL:         https://arxiv.org/abs/2002.08909
Kind:        primary — Guu, Lee, Tung, Pasupat, Chang at Google Research (2020);
             the REALM system paper Lewis et al. build on and compare against.
Establishes: REALM's pre-training method (masked language modeling with a latent
             retriever, salient span masking, Inverse Cloze Task warm-start,
             asynchronous MIPS index refresh, null document, prohibition of
             trivial retrievals), model size (~330M parameters, 30× smaller than
             T5-11B), and the Open-QA test scores that anchor "REALM in Table 1"
             for the lesson.
Paraphrase:  "For the first time, we show how to pre-train such a knowledge
             retriever in an unsupervised manner, using masked language modeling
             as the learning signal and backpropagating through a retrieval step
             that considers millions of documents." Table 1 (test EM): REALM
             (X=CC-News, Z=Wikipedia) NQ 40.4, WQ 40.7, CT 42.9; REALM
             (X=Wikipedia, Z=Wikipedia) NQ 39.2, WQ 40.2, CT 46.8. Baselines in
             the same table: T5-11B NQ 34.5, WQ 37.4; ORQA NQ 33.3, WQ 36.4, CT
             30.1; BERT-baseline NQ 26.5, WQ 17.7, CT 21.3. REALM has 330M
             parameters; T5-11B has 11,318M. Retrieval corpus: 13M passages
             (documents "greedily split into chunks of up to 288 BERT
             wordpieces"). Abstract's range: outperforms prior methods "by
             4-16% absolute accuracy."
Locators:    Abstract; §3.4 Injecting inductive biases (salient span masking,
             ICT warm-start, null document); §4.3 Implementation Details
             (Dec 20, 2018 Wikipedia, ~13M chunks, top-5 at fine-tuning); §4.4
             Table 1; §4.5 Table 2 (ablations).
```

```text
URL:         https://arxiv.org/abs/2310.03025
Kind:        primary — Xu, Ping, and colleagues at NVIDIA; published at ICLR
             2024; owns the head-to-head comparison of long-context and
             retrieval-augmentation on 43B/70B decoder-only LLMs.
Establishes: That retrieval-augmentation improves both 4K-context and long-
             context LLMs at the 43B/70B scale, that a 4K model with retrieval
             matches or approaches a 16K model without retrieval, and that "lost
             in the middle" behaviour also appears in Llama2-70B. Uses Dragon,
             Contriever, and OpenAI text-embedding-ada-002 as off-the-shelf
             retrievers with 300-word chunks. No joint training of retriever and
             generator.
Paraphrase:  "We find that LLM with 4K context window using simple
             retrieval-augmentation at generation can achieve comparable
             performance to finetuned LLM with 16K context window via positional
             interpolation on long context tasks, while taking much less
             computation." Table 2 averages across seven datasets (QM, QASP, NQA,
             QLTY, MSQ, HQA, MFQA), Llama2-70B: 4K baseline 31.61, 4K+ret 36.02,
             16K baseline 36.78, 16K+ret 37.23, 32K baseline 37.36, 32K+ret
             39.60. GPT-43B: 4K 26.44, 4K+ret 29.32, 16K 29.45, 16K+ret 29.65.
             Table 3 seven-task averages: Davinci-003 (175B) 39.2, GPT-3.5-turbo
             (4K) 38.4, GPT-3.5-turbo-16K 42.8, Llama2-70B-32K 40.9,
             Llama2-70B-32K-ret 43.6. Table 5 shows that going from top-5 to
             top-20 retrieved chunks does not monotonically help and can hurt.
             Retrieval-augmented Llama2-70B is "4× faster on NarrativeQA" than
             its 32K non-retrieval baseline.
Locators:    Abstract; §1 contributions; §3.1 Language Models; §3.4 Retrieval;
             §4.1 Table 2 and Figure 1 (lost-in-middle in Llama2-70B); §4.2
             Table 3; §4.4 Table 5.
```

```text
URL:         https://arxiv.org/abs/2401.05856
Kind:        primary — Barnett, Kurniawan, Thudumu, Brannelly, Abdelrazek at
             Deakin University (Applied Artificial Intelligence Institute);
             CAIN 2024. An experience report on three deployed RAG systems,
             including an empirical BioASQ study; the authors ran the systems.
Establishes: A named taxonomy of seven engineering failure points in the
             inference-time retrieve-then-read RAG pipeline (which is the modern
             usage of the name); three case studies (Cognitive Reviewer at
             Deakin; AI Tutor for 200 students starting 30 Oct 2023; BioASQ
             benchmark run using GPT-4 and OpenAI Evals for automated grading).
Paraphrase:  The seven failure points, verbatim from §5:
             "FP1 Missing Content ... asking a question that cannot be answered
             from the available documents."
             "FP2 Missed the Top Ranked Documents ... the answer to the question
             is in the document but did not rank highly enough to be returned to
             the user."
             "FP3 Not in Context - Consolidation strategy Limitations ...
             Documents with the answer were retrieved from the database but did
             not make it into the context for generating an answer."
             "FP4 Not Extracted ... the answer is present in the context, but
             the large language model failed to extract out the correct answer."
             "FP5 Wrong Format ... question involved extracting information in a
             certain format such as a table or list and the large language model
             ignored the instruction."
             "FP6 Incorrect Specificity ... the answer is returned in the
             response but is not specific enough or is too specific to address
             the user's need."
             "FP7 Incomplete ... Incomplete answers are not incorrect but miss
             some of the information even though that information was in the
             context and available for extraction."
             Key stated takeaways: "validation of a RAG system is only feasible
             during operation" and "the robustness of a RAG system evolves
             rather than designed in at the start."
Locators:    Abstract; §1 Introduction (research questions and BioASQ headline
             figure "15,000 documents and 1000 question and answer pairs"); §4
             Case Studies and Table 1 (which lists BioASQ dataset size as 4017);
             §4.3 Biomedical Question and Answer ("We downloaded 4017 open
             access documents from the BioASQ dataset and had a total of 1000
             questions"); §5 Failure Points; §6 Lessons and Future Research
             Directions.
Quote:       "The purpose of this paper is to provide 1) a reference to
             practitioners and 2) to present a research road map for RAG
             systems."
```

```text
URL:         https://aclanthology.org/2024.acl-long.585/
Kind:        primary — Niu, Wu, Zhu, Xu, Shum, Zhong, Song at NewsBreak and
             Zhang at UIUC; ACL 2024 long paper. The authors built RAGTruth and
             ran the LLMs; the numbers are theirs.
Establishes: That an off-the-shelf-LLM RAG pipeline still produces hallucinations
             at measurable rates across question answering, data-to-text, and
             summarization tasks, even when the retrieved passages are provided
             in the prompt. Reports per-model hallucination densities and
             response-level rates from six LLMs (GPT-3.5-turbo-0613, GPT-4-0613,
             Mistral-7B-Instruct, Llama-2-7B-chat, Llama-2-13B-chat, and 4-bit-
             quantized Llama-2-70B-chat).
Paraphrase:  "RAGTruth comprises nearly 18,000 naturally generated responses ...
             annotations at both the individual case and word levels." Table 2
             totals: 2,965 instances, 17,790 responses; 7,664 responses flagged
             as containing hallucinations (43.1% of all responses); 14,289
             hallucinated spans. Task splits: QA (MS MARCO) 989 instances / 5,934
             responses / 29.1% hallucinated; Data-to-text (Yelp Open Dataset)
             1,033 / 6,198 / 68.6%; Summarization (CNN/DM) 628 / 3,768 / 30.9%
             and (Recent News) 315 / 1,890 / 27.6%. Table 3 hallucination density
             (hallucinated spans per 100 words) — GPT-4-0613: QA 0.06, D2T 0.27,
             Sum 0.08; GPT-3.5-turbo: 0.12, 0.18, 0.05; Llama-2-7B-chat: 0.59,
             1.27, 0.58; Llama-2-13B-chat: 0.48, 1.53, 0.41; Llama-2-70B-chat
             (4-bit): 0.40, 1.15, 0.26; Mistral-7B-Instruct: 0.59, 1.51, 0.86.
             Table 7 whole-response hallucination rate on the 450-instance test
             set: GPT-4-0613 9.3%, GPT-3.5-Turbo-0613 10.9%, Llama-2-7B-chat
             51.8%, Mistral-7B-Instruct 57.6%. Fine-tuning Llama-2-13B on
             RAGTruth as a hallucination detector, then selecting the response
             with no detected hallucinations from two candidates, brings the
             GPT-3.5/GPT-4 pair's rate from 9.8% to 4.8% and the 7B/Mistral
             pair's from 52.4% to 19.3%. Their statement of the underlying
             finding: "Despite the integration of RAG, LLMs may still present
             unsupported or contradictory claims to the retrieved contents."
Locators:    Abstract; §3.2 Response Generation (six models, three tasks); §4.1
             Table 2 (basic statistics); §4.2 Table 3 (hallucination density);
             §5.2 Data Split (450-instance test set); §6.3 Table 7 (suppression
             experiment).
Quote:       "Despite the integration of RAG, LLMs may still present unsupported
             or contradictory claims to the retrieved contents."
```

```text
URL:         https://arxiv.org/abs/2307.03172
Kind:        primary — Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang
             at Stanford, UC Berkeley, and Samaya AI; TACL, arXiv v3 20 Nov
             2023. The authors designed the controlled experiments; the numbers
             are theirs.
Establishes: The U-shaped accuracy curve when the answer-bearing passage is
             moved through the input context, on both an NQ-derived multi-
             document QA task and a synthetic key-value retrieval task. The
             evaluated models are GPT-3.5-Turbo (4K) and GPT-3.5-Turbo-16K,
             Claude-1.3 (8K) and Claude-1.3-100K, MPT-30B-Instruct, and
             LongChat-13B (16K). Extended-context variants do not use the
             enlarged window better than their base versions when the input
             fits in both.
Paraphrase:  "Performance is often highest when relevant information occurs at
             the beginning or end of the input context, and significantly
             degrades when models must access relevant information in the middle
             of long contexts, even for explicitly long-context models." Table 1
             closed-book vs oracle accuracy on multi-document QA: LongChat-13B
             (16K) 35.0% / 83.4%; MPT-30B-Instruct 31.5% / 81.9%; GPT-3.5-Turbo
             56.1% / 88.3%; GPT-3.5-Turbo (16K) 56.0% / 88.6%; Claude-1.3
             48.3% / 76.1%; Claude-1.3 (100K) 48.2% / 76.4%. On the 20- and 30-
             document settings, GPT-3.5-Turbo's mid-context accuracy falls below
             its 56.1% closed-book number — so with those retrieval sizes,
             feeding the model documents can be worse than feeding it none.
Locators:    Abstract; §1 Introduction; §2.3 Results (Figure 5 and Table 1);
             §3 Key-Value Retrieval (Figures 6-7); Appendix D notes GPT-4 (8K)
             shows the same trend on a subset.
Quote:       "GPT-3.5-Turbo's multi-document QA performance can drop by more
             than 20% — in the worst case, performance in 20- and 30-document
             settings is lower than performance without any input documents
             (i.e., closed-book performance; 56.1%)."
```

```text
URL:         https://arxiv.org/abs/2312.10997
Kind:        secondary — Gao, Xiong, Gao, Jia, Pan, Bi, Dai, Sun, Wang at Fudan
             and Tongji (2023); a survey that describes how the field uses the
             term "RAG" today. Reports on the state of practice rather than
             running new experiments, so it is a repeater for definitions
             (though a stake-holding one for its own taxonomy).
Establishes: That the field currently uses "Naive RAG" to name the inference-
             time retrieve-then-read pipeline — indexing, retrieval, and
             generation with no joint training — and treats Lewis et al.'s work
             as the ancestor rather than the referent of the deployed name.
             Anchors the "off-the-shelf retriever plus off-the-shelf LLM"
             description the commission asks for.
Paraphrase:  Naive RAG "follows a traditional process that includes indexing,
             retrieval, and generation, which is also characterized as a
             'Retrieve-Read' framework." Indexing: "Documents are split into
             chunks, encoded into vectors, and stored in a vector database."
             Retrieval: "Retrieve the Top k chunks most relevant to the question
             based on semantic similarity." Generation: "Input the original
             question and the retrieved chunks together into LLM to generate the
             final answer." The paper's taxonomy separates Naive RAG (this
             pipeline), Advanced RAG (adds pre- and post-retrieval steps), and
             Modular RAG (rearranges components). It describes Naive RAG as
             having "gained prominence shortly after the widespread adoption of
             ChatGPT."
Locators:    Abstract; §III RAG Framework (definitions of Naive, Advanced,
             Modular RAG); §III-A Naive RAG (Retrieve-Read description).
```

## Contradictions

The commission calls the paper's system "trained together" and contrasts modern
RAG for having "no joint training." That contrast is real but narrower than a
paraphrase would suggest, and the record has to keep the shape of Lewis et al.'s
own training loop honest. The paper initialises its retriever from a pre-trained
DPR bi-encoder that was already supervised on Natural Questions and TriviaQA,
freezes DPR's document encoder and the FAISS index, and only fine-tunes DPR's
query encoder together with the BART generator (§2.4 of Lewis et al.). No
component is trained from scratch in the RAG paper. The gap with today's stack
is that today's stack fine-tunes neither side — the retriever is an off-the-
shelf embedding model (Dragon, Contriever, OpenAI text-embedding-ada-002 in
Xu et al.; unspecified vector stores in the deployed systems Barnett et al.
report), and the generator is an off-the-shelf instruction-tuned LLM
(GPT-3.5/GPT-4, Llama-2, Mistral in Niu et al. and Xu et al.). Gao et al.'s
"Naive RAG" is that inference-only pipeline. The lesson can honestly say the
name has drifted from a jointly fine-tuned system to a wired-together one; it
should not say the paper trained the retriever from scratch.

Barnett et al. contradicts its own headline. The paper's abstract and §1 say
the BioASQ experiment used "15,000 documents and 1000 question and answer
pairs," but §4.3 and Table 1 report 4,017 documents and 1,000 questions. The
"15,000" number appears nowhere in the case-study section that describes the
run. The 1,000 questions figure is consistent. The record should not repeat the
15,000 figure without flagging it; the run itself was on 4,017 documents.

Xu et al. contradicts a concurrent long-context study. LongBench (Bai et al.,
Aug 2023) reports that retrieval helps small models but not long-context ones
(GPT-3.5-Turbo-16K, ChatGLM2-6B-32K). Xu et al. find the opposite for larger
models: retrieval helps Llama2-70B-32K (39.60 vs 37.36 average score across
seven long-context tasks). Xu et al. explain the disagreement as a scale effect
— zero-shot ability to use retrieved chunks grows with parameter count — but
the disagreement itself is unresolved between primaries.

The commission asks for evidence on hallucination with retrieval versus
without, and the record cannot supply a like-for-like comparison. RAGTruth
(Niu et al.) measures hallucination on RAG outputs only; it does not run the
same models without retrieval on the same prompts. Lewis et al.'s own
"hallucinates less" claim rests on a 452-item Jeopardy pairwise human eval
(RAG rated more factual than BART 42.7% of the time, BART more factual than
RAG 7.1%; §4.3 Table 4). Modern secondary reports and industry leaderboards
exist but were not admitted here because the commission required primaries;
the lesson has to note the gap rather than fill it with a headline number.

Lewis et al.'s framing of "state of the art" holds on the four QA benchmarks
they report on. Their comparison uses the DPR extractive system as the strong
open-book baseline (NQ 41.5, TQA 57.9, WQ 41.1, CT 50.6) and RAG-Sequence
beats each (44.5, 56.8/68.0, 45.2, 52.2). No source found here disputes those
2020 numbers. The disagreement with the present begins downstream, in what
the deployed pipeline that inherits the name is actually delivering.

## Numbers

```text
Figure: RAG-Sequence Exact Match, Natural Questions open test set: 44.5
Owner:  Lewis et al. (2020), Table 1
Scope:  test split of Natural Questions (open-domain QA), 3,610 questions
```

```text
Figure: RAG-Sequence EM, TriviaQA open test set / TriviaQA-Wiki test set: 56.8 / 68.0
Owner:  Lewis et al. (2020), Table 1
Scope:  TriviaQA unfiltered open test (11,313 questions) and the TQA-Wiki
        test used for T5 comparison
```

```text
Figure: RAG-Sequence EM, WebQuestions: 45.2; CuratedTrec: 52.2
Owner:  Lewis et al. (2020), Table 1
Scope:  WQ test 2,032 questions; CT test 694 questions
```

```text
Figure: T5-11B closed-book EM, Natural Questions: 34.5; WebQuestions: 37.4
Owner:  Roberts, Raffel, Shazeer (2020), reproduced in both Lewis et al. Table 1
        and Guu et al. Table 1
Scope:  same test splits as above; T5-11B has 11,318M parameters
```

```text
Figure: T5-11B+SSM EM, Natural Questions: 36.6; WebQuestions: 44.7; TriviaQA-Wiki: 60.5
Owner:  Roberts et al. (2020), via Lewis et al. Table 1
Scope:  same splits; +SSM denotes salient-span-masking continued pre-training
```

```text
Figure: REALM EM, Natural Questions: 40.4; WebQuestions: 40.7; CuratedTrec: 42.9
Owner:  Guu et al. (2020), Table 1 (X=CC-News, Z=Wikipedia)
Scope:  same splits; REALM ~330M parameters (30× smaller than T5-11B)
```

```text
Figure: DPR top-20 passage retrieval accuracy: NQ 79.4, TQA 78.8, WQ 75.0, TREC 89.1, SQuAD 51.6
Owner:  Karpukhin et al. (2020), Table 2 (Multi encoder, DPR without BM25 fusion)
Scope:  test splits of the five QA datasets, retrieving from 21,015,324 Wikipedia
        passages
```

```text
Figure: BM25 top-20 passage retrieval accuracy: NQ 59.1, TQA 66.9, WQ 55.0, TREC 70.9, SQuAD 68.8
Owner:  Karpukhin et al. (2020), Table 2 (Lucene BM25 baseline)
Scope:  same splits and index
```

```text
Figure: RAG Wikipedia knowledge index size: 21,015,324 passages
Owner:  Karpukhin et al. (2020), §4.1; Lewis et al. (2020), §3 (rounds to 21M)
Scope:  English Wikipedia dump of 20 December 2018, split into non-overlapping
        100-word blocks
```

```text
Figure: RAG BART generator size: 400M parameters
Owner:  Lewis et al. (2020), §2.3
Scope:  BART-large pre-trained checkpoint used as the parametric memory
```

```text
Figure: Jeopardy pairwise factuality — RAG rated more factual than BART 42.7% of cases;
        BART more factual than RAG 7.1%; both good 11.7%; both poor 17.7%
Owner:  Lewis et al. (2020), §4.3 Table 4
Scope:  human evaluation over 452 pairs of generations
```

```text
Figure: Llama2-70B seven-task average, 4K without retrieval 31.61 vs 4K with retrieval 36.02
Owner:  Xu et al. (2024), Table 2
Scope:  average of exact-match/F1/ROUGE metrics across QM, QASP, NQA, QLTY,
        MSQ, HQA, MFQA using best retriever (Dragon or Contriever or OpenAI
        embeddings), top-5 chunks
```

```text
Figure: Llama2-70B seven-task average, 32K without retrieval 37.36 vs 32K with retrieval 39.60
Owner:  Xu et al. (2024), Table 2
Scope:  same seven-task average, Dragon retriever, top-5
```

```text
Figure: Llama2-70B-32K-ret seven-task average 43.6 vs GPT-3.5-turbo-16K 42.8
Owner:  Xu et al. (2024), Table 3
Scope:  authors' evaluation on the seven datasets; GPT-3.5-turbo-16K scores
        drawn from ZeroSCROLLS leaderboard for four of the seven
```

```text
Figure: Response-level hallucination rate on the RAGTruth 450-instance test set —
        GPT-4-0613 9.3%, GPT-3.5-Turbo-0613 10.9%, Llama-2-7B-chat 51.8%,
        Mistral-7B-Instruct 57.6%
Owner:  Niu et al. (2024), Table 7 (bracketed group values)
Scope:  test set of 450 instances (150 per task type) across QA, data-to-text,
        summarization; retrieval passages provided in prompt
```

```text
Figure: Whole-corpus response-level hallucination rate: 7,664 of 17,790 responses = 43.1%
Owner:  Niu et al. (2024), Table 2
Scope:  full RAGTruth corpus across six models and three tasks
```

```text
Figure: GPT-3.5-Turbo multi-document QA closed-book accuracy 56.1%; oracle 88.3%
Owner:  Liu et al. (2023/24), Table 1
Scope:  2,655 NQ-derived multi-document QA questions with 10, 20, or 30
        retrieved passages; closed-book means no passages provided; oracle
        means only the answer-bearing passage provided
```

```text
Figure: On 20- and 30-document retrieval settings with the answer in the middle,
        GPT-3.5-Turbo scores below its 56.1% closed-book number
Owner:  Liu et al. (2023/24), §2.3
Scope:  same multi-document QA setup; establishes that adding retrieved
        passages can hurt when the answer sits in the middle
```

```text
Figure: BioASQ empirical run — 4,017 documents, 1,000 questions
Owner:  Barnett et al. (2024), §4.3 Case Study and Table 1
Scope:  Publicly downloadable BioASQ open-access documents; questions include
        yes/no, factoid, list, and text-summarisation types; responses graded
        by OpenAI Evals with manual review of flagged items and a sample of
        correct labels. The paper's abstract and §1 give the size as "15,000
        documents" — an inconsistency with the case-study section.
```

## Source assets

```text
Asset: Lewis et al. (2020), Table 1 (Open-Domain QA Test Scores)
Shows: The RAG-Sequence, RAG-Token, DPR-extractive, REALM, T5-11B, and T5-11B+SSM
       EM scores side by side on NQ, TQA, WQ, and CT. A reader can see with
       one glance where RAG-Sequence beats each baseline and by how much, and
       where the closed-book baselines sit below the open-book ones.
Crop:  Must keep the "Closed Book" and "Open Book" row labels, all four benchmark
       columns, and both TQA columns (open test and Wiki test). Cutting one of
       the closed-book baselines defeats the point of the comparison.
```

```text
Asset: Lewis et al. (2020), Figure 1 (RAG overview)
Shows: Query x flows into a query encoder, MIPS over a document index returns
       top-K passages z, and the BART generator produces y marginalised over
       those z. The figure names the three components the lesson has to name:
       DPR retriever, MIPS/document index, BART generator.
Crop:  Must keep the "End-to-End Backprop through q and p_theta" arrow and
       the "Retriever p_eta (Non-Parametric)" / "Generator p_theta (Parametric)"
       labels, since those two labels carry the paper's core claim.
```

```text
Asset: Karpukhin et al. (2020), Table 2 (Top-20 & Top-100 retrieval accuracy)
Shows: DPR beats BM25 in top-20 accuracy on four of five datasets and loses on
       SQuAD; the win-margin varies by dataset. Establishes the retriever
       quality that RAG inherits.
Crop:  Must keep the SQuAD column, since that is where DPR loses and the
       lesson may want to say retrieval quality is dataset-dependent. Must
       keep the "Training" column so a reader can tell Single from Multi
       encoders.
```

```text
Asset: Liu et al. (2023/24), Figure 5 (U-shaped curve for multi-document QA)
Shows: Accuracy of five closed-source and open-source models plotted against
       the position of the answer-bearing passage among 10 or 20 distractor
       passages; the curve dips in the middle for all of them. The image
       carries the argument better than a sentence would.
Crop:  Must keep both the closed-book horizontal reference lines and the full
       position axis. Cropping to just the answer curves loses the point that
       middle-context accuracy can dip below closed-book.
```

```text
Asset: Niu et al. (2024), Table 3 (hallucination counts and density per model)
Shows: Six models' hallucination density on QA, data-to-text, and
       summarisation; a reader sees at a glance that data-to-text hallucinates
       an order of magnitude more than QA, and that GPT-4 is not immune.
Crop:  Must retain the density column for all three tasks — cropping to only
       QA would hide the data-to-text spike.
```

```text
Asset: Xu et al. (2024), Table 2 (seven-task averages)
Shows: For both GPT-43B and Llama2-70B, retrieval boosts the 4K row to
       roughly the 16K baseline, and 32K+retrieval beats 32K alone. Reads as
       a compact answer to "which is better."
Crop:  Must keep the "Avg." column and at least one non-average column so a
       reader can see the averaging isn't hiding a single benchmark. Must
       keep both GPT-43B and Llama2-70B blocks — the effect grows with
       model size and cropping one hides that.
```

## Discarded

```text
https://arxiv.org/abs/2407.16833: Li et al. "Retrieval Augmented Generation or
Long-Context LLMs? A Comprehensive Study and Hybrid Approach" — a Google-DeepMind
primary that reaches partly opposite conclusions to Xu et al. (long-context often
beats RAG on the same tasks). Read the abstract and introduction; not added to
the record because Xu et al. already anchors the long-context-vs-RAG evidence
and the two disagree on model sizes and tasks that the lesson does not have
room to reconcile. Worth reopening for a follow-up article.

https://medium.com/tr-labs-ml-engineering-blog/rag-in-the-era-of-long-context-llms-b8ecda2d5693:
Thomson Reuters Labs blog on RAG in the long-context era — secondary, restates
the Xu et al. and Li et al. findings. Not added because the record already has
the primary these summaries repeat.

https://arxiv.org/abs/2309.01431: Chen, Lin, Han, Sun. "Benchmarking Large
Language Models in Retrieval-Augmented Generation" (RGB benchmark). Skimmed the
abstract; would have added useful failure-mode numbers on noise robustness, but
the record's failure-mode coverage is already carried by Barnett et al. and Liu
et al. Kept in reserve if the writer needs a third primary on modern RAG limits.

https://openai.com/blog/... and Anthropic/Google product pages — dropped
because product blogs are secondary and there is only room for one secondary
here; Gao et al. is the more useful secondary because it defines the term
"Naive RAG" the lesson will need to use.
```
