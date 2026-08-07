# Evidence: the-instruments/hallucination-rate (01)

The evidence supports the commission's core claim firmly. A published
"hallucination rate" from Vectara's leaderboard is a summary-faithfulness score:
each model summarizes a private set of documents under a strict "use only this
passage" prompt, and a fine-tuned classifier (HHEM), not a human and not general
truth-checking, scores whether each summary is supported by its own source. The
rate is 100 minus that factual-consistency rate. Three independent facts show the
number cannot bear the weight of "how often the model lies": (1) it measures
faithfulness to a provided passage, so a summary that faithfully echoes a false
passage scores as clean; (2) the classifier that produces it is itself imperfect,
with balanced accuracy near 55% on FaithBench's hard cases and recall of only
~32% on RAGTruth summarization; (3) named benchmarks define hallucination in
incompatible ways (TruthfulQA scores imitative falsehoods with no source
document; RAGTruth annotates spans across three tasks; FaithBench uses a four-way
taxonomy), so the rates are not comparable. The record is thin on one point the
commission wants: a documented dollar cost caused specifically by trusting a
Vectara number. What is well documented is the press generalizing the
summarization rate into an overall "which AI hallucinates" ranking, and the
separate, primary-sourced fact that frontier reasoning models fabricate 33-48% on
an open factual-QA task (PersonQA) while scoring far lower on the summarization
board. Those two together carry the "misled" point; a clean procurement-cost
anecdote was not found and is flagged below.

Note on dates: the live leaderboard snapshot is stamped "Last updated on May 11,
2026" and includes 2026-dated models (GPT-5.x, Claude Opus 4.x). Rates below are
transcribed from that snapshot as the source presents them.

## Sources

```text
URL:         https://github.com/vectara/hallucination-leaderboard
Kind:        primary. Vectara owns and operates this leaderboard; the README is
             the method write-up and the published rates themselves.
Establishes: The entire pipeline. Models are fed a private dataset of 7,700+
             articles (50 words to ~24K words) across news, technology, science,
             medicine, legal, sports, business, education, and asked to summarize
             each using only the passage. HHEM-2.3 (Vectara's commercial
             classifier) scores each summary's factual consistency 0-1; the
             leaderboard reports factual-consistency rate and hallucination rate
             (= 100 - factual-consistency rate), plus an Answer Rate (share of
             documents the model actually summarized rather than refused) and
             average summary length.
Paraphrase:  The rate is a summarization-faithfulness measure, not general
             accuracy. Vectara states it evaluates summarization factual
             consistency "instead of overall factual accuracy" so the summary can
             be compared against the provided source; it is "not evaluating the
             quality of the summaries, only the factual consistency"; and it does
             not recommend the metric as a standalone score. The dataset is kept
             private to prevent models training on it.
Locators:    README top matter (Last updated on May 11, 2026), "Methodology"/
             "Prompt used" section, "Answer Rate" column note, and the
             caveats/FAQ near the foot.
Quote:       Prompt rule 1: "Summarize using only the information in the given
             passage. Do not infer. Do not use your internal knowledge."
             Method: "computed the overall factual consistency rate (no
             hallucinations) and hallucination rate (100 - accuracy) for each
             model."
```

```text
URL:         https://huggingface.co/vectara/hallucination_evaluation_model
Kind:        primary. Vectara authored HHEM-2.1-Open and this model card; it owns
             the classifier's definition and its validation numbers.
Establishes: HHEM is a pure classifier (fine-tuned google/flan-t5-base), NOT an
             LLM-as-a-judge, that outputs a 0-1 support score of a hypothesis
             against a premise. Its own measured accuracy is well short of
             perfect, which is the error rate of the instrument that produces the
             rate.
Paraphrase:  Validation figures on public benchmarks: AggreFact-SOTA balanced
             accuracy 76.55% (F1 66.77%); RAGTruth-Summ balanced accuracy 64.42%,
             F1 44.83%, recall 31.86%, precision 75.58%; RAGTruth-QA balanced
             accuracy 74.28%. The low RAGTruth-Summ recall means that on that
             set the classifier misses roughly two-thirds of the hallucinations
             it is asked to catch, even as its precision stays high.
Locators:    Model card "Overview", "Using with transformers" and the benchmark
             results table.
Quote:       "By 'hallucinated' or 'factually inconsistent', we mean that a text
             (hypothesis, to be judged) is not supported by another text
             (evidence/premise, given)."
```

```text
URL:         https://arxiv.org/abs/2410.13210  (ACL: https://aclanthology.org/2025.naacl-short.38/)
Kind:        primary. This is the FaithBench paper; it owns the FaithBench
             taxonomy and the detector-accuracy results reported here.
Establishes: Hallucination in summarization is not a single binary. FaithBench
             annotates 660 samples from 10 LLMs across 8 families (GPT, Llama,
             Gemini, Mistral, Phi, Claude, Command-R, Qwen) with a four-way scheme
             and shows that the best automatic detectors are near a coin flip on
             challenging cases.
Paraphrase:  Taxonomy: Consistent (no hallucination); Questionable (not clearly a
             hallucination, annotators may disagree); Benign (clearly a
             hallucination but supported by world knowledge, common sense, or
             logic); Unwanted (a clear, non-benign hallucination), split into
             Intrinsic (contradicts the passage) and Extrinsic (neither supported
             by, inferrable from, nor factual). On the challenging set, detector
             balanced accuracies cluster near 50%: Vectara HHEM-2.1 ~55.68%
             (F1-macro ~40.86%), GPT-4o zero-shot ~56.29% (F1-macro ~40.75%).
             By unwanted-hallucination rate, GPT-4o hallucinated least (~39.34%)
             and Command-R most (~73.77%); GPT-3.5-Turbo ~44.26%.
Locators:    Taxonomy/annotation section; detector results table; per-LLM results
             table.
Quote:       "even the best hallucination detection models have near 50%
             accuracies on FaithBench, indicating lots of room for future
             improvement."
```

```text
URL:         https://arxiv.org/abs/2109.07958  (ACL: https://aclanthology.org/2022.acl-long.229/)
Kind:        primary. The TruthfulQA paper (Lin, Hilton, Evans) owns this
             benchmark and its numbers.
Establishes: A different failure entirely. TruthfulQA measures whether a model
             reproduces human misconceptions ("imitative falsehoods") when
             answering open questions with no source document to be faithful to.
             It is not a summarization or grounding task, so its "truth" and
             Vectara's "faithfulness" are not the same quantity.
Paraphrase:  817 questions across 38 categories (health, law, finance, politics,
             others), written so that "some humans would answer falsely due to a
             false belief or misconception." Best model was truthful on 58% of
             questions vs 94% for humans, and the largest models were generally
             the least truthful, the opposite of the usual scaling trend.
Locators:    Abstract; benchmark construction section; scaling results.
Quote:       Questions were crafted so that "some humans would answer falsely due
             to a false belief or misconception."
```

```text
URL:         https://arxiv.org/abs/2401.00396
Kind:        primary. The RAGTruth paper (ParticleMedia) owns this corpus and its
             annotation scheme.
Establishes: A third, incompatible definition. RAGTruth annotates hallucinations
             at the word/span level across three RAG tasks, showing "hallucination
             rate" depends on task and granularity, not just model.
Paraphrase:  ~18,000 naturally generated RAG responses annotated at case and word
             levels. Hallucination is content that is "unsupported or
             contradictory" to the retrieved context. It covers three tasks
             (question answering, data-to-text, news summarization) and four span
             types (evident conflict, subtle conflict, evident baseless
             information, subtle baseless information). Reported annotator
             agreement ~91.8% at response level and ~78.8% at span level.
Locators:    Abstract; corpus construction and annotation sections.
Quote:       Abstract frames the problem as models presenting "unsupported or
             contradictory claims to the retrieved contents."
```

```text
URL:         https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf
Kind:        primary. OpenAI's own system card owns these PersonQA numbers.
             (Numbers verified via a faithful transcription of Table 4 at
             https://simonwillison.net/2025/Apr/21/openai-o3-and-o4-mini-system-card/
             because the PDF would not render through the fetch tool; the OpenAI
             URL above is the document's own home.)
Establishes: The "fabricates in open use" half of the misled case. On PersonQA, a
             factual-QA task about people with no passage to summarize, frontier
             reasoning models fabricate at high rates, and a newer, more capable
             model fabricated MORE, not less.
Paraphrase:  PersonQA hallucination rate: o3 0.33, o4-mini 0.48, o1 0.16
             (accuracy: o3 0.59, o4-mini 0.36, o1 0.47). o3-mini ~14.8% is cited
             by secondary coverage but was not confirmed against the primary
             table here. These sit far above the same model class's
             summarization-board rates, showing the two numbers measure different
             things.
Locators:    Hallucination evaluation section, PersonQA (Table 4).
Quote:       "o3 tends to make more claims overall, leading to more accurate
             claims as well as more inaccurate/hallucinated claims."
```

```text
URL:         https://www.nytimes.com/2023/11/06/technology/chatbots-hallucination-rates.html
Kind:        secondary. Cade Metz reporting for the New York Times on Vectara's
             launch; reports the claim from outside the authoring party.
Establishes: That the leaderboard's launch numbers reached a general audience as
             a statement about how often chatbots invent information. Content
             verified through a full-text mirror
             (https://thelivinglib.org/chatbots-may-hallucinate-more-often-than-many-realize/)
             because nytimes.com is not fetchable from this environment; the URL
             above is the article's own home and the Nov 6, 2023 date is
             corroborated by Techmeme (techmeme.com/231106/p38).
Paraphrase:  Reports that "chatbots invent information at least 3 percent of the
             time - and as high as 27 percent," with OpenAI lowest (~3%) and
             Google's PaLM-Chat highest (~27%). In the mirrored text the piece
             frames these as rates that hold "even in situations designed to
             prevent it"; the mirror I read did not foreground that the task was
             specifically document summarization, so the summarization scope was
             not made salient to the general reader.
Locators:    Opening paragraphs; the rate figures; the "situations designed to
             prevent it" framing.
Quote:       "chatbots invent information at least 3 percent of the time - and as
             high as 27 percent" (per the mirrored text).
```

```text
URL:         https://www.tomshardware.com/news/ai-hallucinations-ranked-chatgpt-best
Kind:        secondary. Trade-press write-up of the same Vectara release.
Establishes: The clearest documented instance of the summarization-faithfulness
             rate being read as a general reliability ranking. The headline
             itself ranks models by hallucination as an overall property.
Paraphrase:  Headline as indexed: "AI Models Ranked By Hallucinations: ChatGPT is
             Best, Palm-Chat Needs to Sober Up." This presents a narrow
             summary-faithfulness score as a general league table of which AI
             hallucinates. I could read the headline and framing via search
             indexing but the article body would not load through the fetch tool,
             so I did not verify whether the body carries the summarization
             caveat.
Locators:    Headline/subheadline.
Quote:       Headline (indexed): "AI Models Ranked By Hallucinations: ChatGPT is
             Best, Palm-Chat Needs to Sober Up."
```

```text
URL:         https://techcrunch.com/2025/04/18/openais-new-reasoning-ai-models-hallucinate-more/
Kind:        secondary. TechCrunch reporting on the o3/o4-mini system card.
Establishes: Independent confirmation that the o3/o4-mini PersonQA numbers were
             read as a surprising reliability regression, and context that a
             "better" model hallucinated more. Repetition here supports that the
             claim circulated, not the underlying figure, which is owned by the
             OpenAI system card above.
Paraphrase:  Reports o3 hallucinating on 33% of PersonQA questions (about double
             o1 and o3-mini at 16% and 14.8%) and o4-mini at 48%, and that
             OpenAI said "more research is needed" to understand why.
Locators:    Body, PersonQA figures.
Quote:       Reports o3 "hallucinated in response to 33% of questions on
             PersonQA."
```

## Contradictions

- Single number vs the operator's own caveats. Vectara publishes a precise
  per-model percentage yet states it is "not evaluating the quality of the
  summaries, only the factual consistency," measures summarization consistency
  "instead of overall factual accuracy," and does not recommend the metric as a
  standalone score. The public use of the number (Tom's Hardware headline; the
  NYT framing of "how often chatbots invent information") runs directly against
  those caveats.
- The rate's precision vs the classifier's own error. A published "9.6%" implies
  fine resolution, but the HHEM classifier that generates it scores ~55% balanced
  accuracy on FaithBench's challenging cases (near a coin flip) and only ~32%
  recall on RAGTruth summarization (misses most hallucinations there). The
  instrument is not precise enough to separate models that sit a point or two
  apart.
- Faithfulness vs truth. The leaderboard rewards a summary that is faithful to
  its passage. A summary that faithfully reproduces a false or misleading source
  scores as non-hallucinated, so the metric cannot speak to real-world truth, the
  thing readers assume it measures.
- Cross-benchmark incomparability. TruthfulQA (imitative falsehoods, no source
  document), RAGTruth (word-level spans across three tasks), and FaithBench
  (four-way taxonomy on hard cases) each define "hallucination" differently, so
  their rates are not interchangeable and cannot be stacked into one ranking.
- Task-vs-open-use divergence. Frontier reasoning models fabricate 33-48% on
  PersonQA (open factual QA) while the same class scores far lower on the
  summarization board, direct evidence that a low board rate does not predict
  open-use fabrication.
- Answer-rate confound. Phi-4 posts a low 3.7% hallucination rate but only an
  80.7% answer rate; refusing or failing to summarize ~19% of documents removes
  the cases most likely to be scored as hallucinated, flattering the rate. A
  model that answers less can look more faithful.

## Numbers

```text
Figure: 7,700+ articles; lengths ~50 to ~24,000 words
Owner:  Vectara hallucination-leaderboard README
Scope:  The private evaluation corpus summarized to compute every rate; snapshot "Last updated on May 11, 2026"
```

```text
Figure: hallucination rate = 100 - factual-consistency rate (percent of summaries HHEM scored as unsupported)
Owner:  Vectara hallucination-leaderboard README
Scope:  Per model, over the full corpus; summarization faithfulness only
```

```text
Figure: GPT-4o (2024-08-06) 9.6% hallucination / 90.4% consistency / 93.8% answer rate / 86.6 words
Owner:  Vectara hallucination-leaderboard README (May 11, 2026 snapshot)
Scope:  Summarization-faithfulness, full corpus
```

```text
Figure: Claude Opus 4 (2025-05-14) 12.0%; Sonnet 4 (2025-05-14) 10.3%; Opus 4.5 (2025-11-01) 10.9%
Owner:  Vectara hallucination-leaderboard README (May 11, 2026 snapshot)
Scope:  Summarization-faithfulness, full corpus
```

```text
Figure: Gemini 2.5 Flash-Lite 3.3%; Gemini 2.5 Pro 7.0%; Llama-3.3-70B-Instruct-Turbo 4.1%; Mistral Large (2411) 4.5%
Owner:  Vectara hallucination-leaderboard README (May 11, 2026 snapshot)
Scope:  Summarization-faithfulness, full corpus
```

```text
Figure: Phi-4 3.7% hallucination BUT 80.7% answer rate; o3-pro 23.3%; GPT-5.4-nano 3.1%; GPT-4.1 5.6%
Owner:  Vectara hallucination-leaderboard README (May 11, 2026 snapshot)
Scope:  Summarization-faithfulness, full corpus; Phi-4 answer rate shows the refusal confound
```

```text
Figure: HHEM-2.1-Open validation: AggreFact-SOTA balanced acc 76.55% / F1 66.77%; RAGTruth-Summ balanced acc 64.42% / recall 31.86% / precision 75.58%; RAGTruth-QA balanced acc 74.28%
Owner:  HHEM-2.1-Open model card (Hugging Face)
Scope:  The classifier's own accuracy on public benchmarks; bounds the precision of any rate it produces
```

```text
Figure: FaithBench detector balanced accuracy ~55.68% (HHEM-2.1), ~56.29% (GPT-4o zero-shot) on challenging cases
Owner:  FaithBench paper
Scope:  660 samples, 10 LLMs / 8 families; "challenging" = cases where SOTA detectors disagreed
```

```text
Figure: FaithBench unwanted-hallucination rate: GPT-4o ~39.34% (lowest), GPT-3.5-Turbo ~44.26%, Command-R ~73.77% (highest)
Owner:  FaithBench paper
Scope:  Per-LLM over the annotated set; not comparable to Vectara percentages (different denominator and label scheme)
```

```text
Figure: TruthfulQA: 817 questions, 38 categories; best model 58% truthful vs 94% human
Owner:  TruthfulQA paper
Scope:  Open-question imitative falsehoods; no source document, not a faithfulness task
```

```text
Figure: RAGTruth: ~18,000 responses; 3 tasks; 4 span types; annotator agreement 91.8% (response) / 78.8% (span)
Owner:  RAGTruth paper
Scope:  Word/span-level RAG hallucination across QA, data-to-text, summarization
```

```text
Figure: PersonQA hallucination rate: o3 0.33, o4-mini 0.48, o1 0.16 (accuracy 0.59 / 0.36 / 0.47)
Owner:  OpenAI o3 and o4-mini system card (Table 4)
Scope:  Open factual QA about people; the "fabricates in open use" contrast to the summarization board
```

## Source assets

```text
Asset: The ranked leaderboard table in the Vectara README (model, hallucination
       rate, factual-consistency rate, answer rate, average summary length).
Shows: The spread and the tight clustering of top models within a couple of
       points, which visually makes the case that the metric cannot separate
       leaders given its own classifier error.
Crop:  Must retain the Answer Rate and average-length columns beside the rate;
       cropping to model+rate alone hides the Phi-4 refusal confound and the
       clustering. Keep the "Last updated" stamp in view.
```

```text
Asset: HHEM-2.1-Open model-card benchmark table (AggreFact / RAGTruth balanced
       accuracy, F1, recall, precision).
Shows: That the classifier producing the rate scores well below perfect, with
       RAGTruth-Summ recall ~32%.
Crop:  Keep the recall column; a crop to balanced accuracy alone hides the
       missed-hallucination problem that the recall number exposes.
```

```text
Asset: FaithBench detector-accuracy table (balanced accuracy near 50% for HHEM
       and GPT-4o on challenging cases).
Shows: The judges disagree near chance on hard summaries, undercutting the
       apparent precision of any single published rate.
Crop:  Retain both the detector column and the "challenging" subset label so the
       near-50% figure is not mistaken for overall accuracy.
```

```text
Asset: OpenAI system card PersonQA table (Table 4): o3 0.33, o4-mini 0.48, o1 0.16.
Shows: Frontier models fabricate at 33-48% on open QA, the sharpest contrast to
       single-digit summarization rates.
Crop:  Keep the accuracy row beside the hallucination row so the "more claims
       overall" explanation is legible.
```

## Discarded

```text
URL: https://presenc.ai/research/ai-hallucination-rate-benchmarks-2026 — aggregator with no primary authorship; figures traceable to sources already read. Not cited.
```

```text
URL: https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/ — SEO roundup, no primary claim ownership. Not cited.
```

```text
URL: https://medium.com/@markus_brinsa/hallucination-rates-in-2025-... — opinion blog, unverifiable secondary aggregation. Not cited.
```

```text
URL: https://www.emergentmind.com/topics/vectara-s-hallucination-leaderboard — useful orientation but a topic-summary site, not a primary owner; all load-bearing facts taken from the README and model card directly.
```

```text
URL: https://www.idx.inc/newsroom/gen-ai-hallucinations — vendor marketing piece; not needed for the misled case, which is carried by the trade-press and system-card sources.
```

## Open gap (for the orchestrator/writer)

The commission asks for a documented case where reading the rate as general
reliability "cost" someone something concrete. What is documented is (a) the
press generalizing a summarization score into an overall ranking (Tom's Hardware
headline; NYT framing) and (b) the primary-sourced fact that frontier reasoning
models fabricate 33-48% in open QA. A specific, attributable dollar or
procurement cost caused by trusting a Vectara number was not found in this pass.
If the writer needs a hard cost figure, that is the remaining research gap; the
"misled" point otherwise stands on the press-generalization plus the
task-vs-open-use divergence.
