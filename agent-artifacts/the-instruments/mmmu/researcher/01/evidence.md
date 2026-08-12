# Evidence record: the-instruments/mmmu (01)

The evidence supports the commission's core claim on firsthand primary reading.
The MMMU paper documents the construction (11,550 questions, 6 disciplines / 30
subjects / 183 subfields, 30 image types, 94.03% multiple-choice) and its own
vision-blind baseline: GPT-4 with text only and no image scores 34.9% on the
validation set against random-choice 22.1% and against GPT-4V's 56.8%. So a
text-only language model banks roughly 13 points above chance without ever
seeing the image, while vision still adds about 22 points on top. The MMMU-Pro
paper, by the same lead author, documents the three changes (filter
text-answerable questions using four open LLMs, expand options from four to ten,
add a vision-only setting that embeds the question in a screenshot) and reports
overall drops of 16.8% to 26.9% from MMMU to MMMU-Pro, with a full per-model
table. Two named model makers' own MMMU claims are quoted from their own reports
(Anthropic's Claude 3.5 Sonnet at 68.3%; Google's Gemini 1.5 Pro at 62.2% and
Gemini Ultra at 59.4%), plus Alibaba's Qwen2-VL-72B at 64.5%. An independent
secondary (MMStar) measures the text-answerable share directly. Where the record
is thin: no single primary states a clean "X% of MMMU is answerable without the
image" figure, so that share is triangulated from three sources rather than
quoted from one; and OpenAI's own GPT-4o page (the 69.1% "number in
circulation") is bot-blocked, so that one figure is corroborated from three
opened records rather than read on OpenAI's own page. The evidence does not
undermine the angle, but it sharpens one boundary the writer must respect: the
angle is "a meaningful share is text-answerable," not "most of the score is
text." The vision-blind ceiling (~35%) sits far below top multimodal scores
(68-69%), and the MMMU authors show OCR and captions do not close that gap.

## Sources

```text
URL:         https://arxiv.org/abs/2311.16502
Kind:        primary — this is the benchmark's authoring paper (Yue et al.,
             CVPR 2024 Oral); it owns MMMU's construction and its own baselines.
Establishes: MMMU's size, discipline/subject spread, question sources, image-type
             variety, answer formats, and the paper's own text-only and
             vision-blind baseline scores. Firsthand.
Paraphrase:  MMMU holds 11,550 questions split dev:validation:test =
             150:900:10,500, across 6 disciplines, 30 subjects, and 183
             subfields, spanning 30 image types (charts, diagrams, maps, tables,
             music sheets, chemical structures, and more). 10,861 questions
             (94.03%) are multiple-choice and 689 (5.97%) are open; 11,264
             (97.52%) carry an image in the question. Questions were collected
             from college exams, quizzes, and textbooks and from online
             resources, with new questions written by the annotators where
             needed. In Table 2, a text-only GPT-4 (no image) scores 34.9%
             (val) / 33.8% (test), above random-choice 22.1% / 23.9% and
             frequent-choice 26.8% / 25.8%, while GPT-4V(ision) scores 56.8%
             (val) / 55.7% (test). The paper reports that text-only LLMs
             augmented with OCR or generated captions "do not see notable
             improvement, indicating that MMMU necessitates deeper joint
             interpretation of images and text."
Locators:    Table 1 (Key Statistics); Table 2 (Selected results, validation and
             test); Section 3 text-only LLM paragraph; contributions list.
Quote:       "LLMs augmented with optical character recognition (OCR) or
             generated captions do not see notable improvement, indicating that
             MMMU necessitates deeper joint interpretation of images and text."
             The six disciplines: Art & Design, Business, Science, Health &
             Medicine, Humanities & Social Science, Tech & Engineering.
```

```text
URL:         https://arxiv.org/abs/2409.02813
Kind:        primary — the follow-up paper (Yue et al., 2024; ACL 2025) by the
             same lead author; it owns the MMMU-Pro design and its score changes.
Establishes: Exactly what MMMU-Pro changed and the per-model score changes
             against plain MMMU. Firsthand.
Paraphrase:  MMMU-Pro applies three changes to MMMU: (1) filter out questions
             answerable by text-only models, (2) augment candidate options from
             four to ten, (3) add a vision-only setting where the question is
             embedded in a screenshot or photo with no text fed to the model.
             Filtering used four open LLMs (Llama3-70B-Instruct,
             Qwen2-72B-Instruct, Yi-1.5-34B-Chat, Mixtral-8x22B-Instruct), each
             run ten times per question; a question counts as "answerable" for a
             model if it answers correctly more than five times, and a question
             is excluded if at least three of the four models answer it
             correctly across the majority of trials. Option augmentation was
             done by human experts with GPT-4o generating and Claude 3.5
             filtering options, then two rounds of human review. The final set is
             1,730 questions (after a human-review pass removed 70), rendered in
             both standard and screenshot form (3,460 items total). The overall
             MMMU-Pro score is the average of the ten-option Standard setting and
             the Vision setting. Model performance is "substantially lower on
             MMMU-Pro than on MMMU, ranging from 16.8% to 26.9% across models."
Locators:    Abstract; Section 2 (Filtering Questions / Augmenting Candidate
             Options / Vision-Only Input); Section 3.1 ("The overall performance
             score for MMMU-Pro is calculated as the average of scores from
             settings (2) and (3)"); Table 1 (Results of models on MMMU-Pro and
             MMMU (Val)); Figures 2, 3, 4.
Quote:       "we increase the number of candidate options from four to ten,
             making it more challenging for models to rely on guessing."
             "model performance is substantially lower on MMMU-Pro than on MMMU,
             ... ranging from 16.8% to 26.9% across models."
```

```text
URL:         https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf
Kind:        primary — Anthropic's own model card addendum for Claude 3.5 Sonnet;
             owns Anthropic's claim about its own model's MMMU score.
Establishes: Claude 3.5 Sonnet's MMMU number as reported by its maker, and the
             evaluation protocol behind it. Firsthand for the claim; secondary
             for whether it reflects multimodal reasoning.
Paraphrase:  Table 1 reports MMMU (validation), labeled "Visual question
             answering," at 68.3% for Claude 3.5 Sonnet, 59.4% for Claude 3 Opus,
             53.1% for Claude 3 Sonnet, 69.1% for GPT-4o (cited to OpenAI), 63.1%
             for GPT-4 Turbo, and 62.2% for Gemini 1.5 Pro. The table note states
             all evaluations are 0-shot and that on MMMU, MathVista, and ChartQA
             all models use chain-of-thought. Anthropic's GPT-4o and Gemini
             figures here are its citations of others' numbers, not its own
             measurements.
Locators:    Table 1 (reasoning/math/coding/QA evaluations), MMMU row; the
             0-shot / chain-of-thought table note.
Quote:       "MMMU (validation) — Visual question answering — 68.3%" for Claude
             3.5 Sonnet. "All of these evaluations are 0-shot. On MMMU,
             MathVista, and ChartQA, all models use chain-of-thought."
```

```text
URL:         https://www.anthropic.com/news/claude-3-5-sonnet
Kind:        primary — Anthropic's own launch post; owns the qualitative claim.
Establishes: How the maker frames the model's vision ability in prose. The page
             carries no MMMU number in fetchable text (the benchmark table is not
             in the page text I could read).
Paraphrase:  The post advertises "State-of-the-art vision" and says Claude 3.5
             Sonnet improves on "tasks that require visual reasoning, like
             interpreting charts and graphs." It names new benchmark records for
             GPQA, MMLU, and HumanEval in text but does not print an MMMU figure
             in readable page text.
Locators:    "State-of-the-art vision" section; opening benchmarks paragraph.
Quote:       "State-of-the-art vision" and improvements on "tasks that require
             visual reasoning, like interpreting charts and graphs."
```

```text
URL:         https://arxiv.org/abs/2403.05530
Kind:        primary — Google DeepMind's Gemini 1.5 technical report; owns
             Google's claim about Gemini 1.5 Pro's MMMU score.
Establishes: Gemini 1.5 Pro's MMMU number as stated by its maker. Firsthand for
             the claim.
Paraphrase:  The report states, "Gemini 1.5 Pro scores 62.2% on MMMU, improving
             over Gemini 1.0 Ultra," describing MMMU as a benchmark where models
             "understand images, and use that information to solve college-level
             problems." Table 18 reports MMMU (val) across the Gemini 1.0/1.5
             family (row cells not cleanly separable in the HTML, but the 62.2%
             prose figure is unambiguous).
Locators:    Section 6.2 image-understanding text; Table 18 (image understanding
             benchmarks), MMMU (val) row.
Quote:       "Gemini 1.5 Pro scores 62.2% on MMMU, improving over Gemini 1.0
             Ultra."
```

```text
URL:         https://arxiv.org/abs/2312.11805
Kind:        primary — Google's original Gemini 1.0 technical report; owns the
             first flagship MMMU claim used to advertise "expert" vision.
Establishes: The origin of the "flagship prints MMMU to prove it sees" pattern,
             and a settings-mismatch worth flagging. Firsthand for the claim.
Paraphrase:  Gemini Ultra's MMMU (val) is reported as 59.4% (pass@1) and 62.4%
             (Maj@32), against GPT-4V at 56.8% (pass@1) and a prior state of the
             art of 47.9%. The report says Gemini Ultra "achieves the best score
             on this benchmark advancing the state-of-the-art result by more than
             5 percentage points ... thus showcasing its multimodal reasoning
             capabilities." Note the reported comparison sets Gemini Ultra's
             best-of-32-samples number beside GPT-4V's single-sample number.
Locators:    Multimodal results table (MMMU (val) row); Table 8 (Gemini Ultra
             per-discipline MMMU, with Maj@32 and pass@1 columns); the
             accompanying claim sentence.
Quote:       "Gemini Ultra achieves the best score on this benchmark advancing
             the state-of-the-art result by more than 5 percentage points ...
             thus showcasing its multimodal reasoning capabilities."
```

```text
URL:         https://arxiv.org/abs/2409.12191
Kind:        primary — the Qwen2-VL technical report (Alibaba); owns Qwen's claim
             about its own model's MMMU score.
Establishes: A third/fourth maker's own MMMU claim, and independent corroboration
             of the Claude and GPT-4o figures. Firsthand for Qwen's own number.
Paraphrase:  The main results table (labeled MMMU val, Yue et al.) reports
             Qwen2-VL-72B at 64.5%, Qwen2-VL-7B at 54.1%, and Qwen2-VL-2B at
             41.1%, alongside cited figures of Claude 3.5 Sonnet 68.3%, GPT-4o
             69.1%, and a "Previous SoTA" of 66.1% (attributed to X.AI). The
             report adds that increasing image resolution barely moves MMMU
             accuracy, hypothesizing "the performance bottleneck in MMMU is more
             related to the model's reasoning capability rather than image
             resolution."
Locators:    Main capability-comparison table, MMMU val row; ablation discussion
             on image tokens / resolution.
Quote:       Qwen2-VL-72B "MMMU val ... 64.5"; "the performance bottleneck in
             MMMU is more related to the model's reasoning capability rather than
             image resolution."
```

```text
URL:         https://arxiv.org/abs/2403.20330
Kind:        secondary — MMStar (Chen et al., 2024), an independent group's
             analysis of multimodal benchmarks including MMMU. It reports on
             MMMU's properties from outside the authoring party.
Establishes: An independent measurement of how much of MMMU is answerable with
             no image, and the data-leakage problem. This is the independent
             confirmation the angle needs.
Paraphrase:  MMStar finds that "GeminiPro achieves 42.9% on the MMMU benchmark
             without any visual input, and outperforms the random choice baseline
             across six benchmarks by over 20% on average," and that
             "Sphinx-X-MoE gets 43.6% on MMMU without accessing images,
             surpassing its LLM backbone with 17.9%." It names two problems in
             current multimodal benchmarks: many samples do not need the image,
             and unintentional data leakage lets models answer visual questions
             from memorized training data.
Locators:    Abstract; Section 1 (the two problems, with the GeminiPro and
             Sphinx-X-MoE figures).
Quote:       "GeminiPro achieves 42.9% on the MMMU benchmark without any visual
             input"; "Sphinx-X-MoE gets 43.6% on MMMU without accessing images,
             surpassing its LLM backbone with 17.9%."
```

## Contradictions

- **Vision contributes most of a top score; text-answerability is a share, not
  the whole.** The MMMU paper's own Table 2 puts text-only GPT-4 at 34.9% (val)
  and GPT-4V at 56.8% (val): vision adds roughly 22 points, larger than the ~13
  points a text-only model wins above random. The angle's "meaningful share can
  be answered from text alone" is correct, but it must not slide into "most of
  the number is text." The majority of a 68-69% score is not banked by text
  alone.
- **The MMMU authors defend the benchmark's vision requirement.** The paper
  reports that giving text-only LLMs OCR output or generated captions "do not see
  notable improvement," which they read as evidence MMMU "necessitates deeper
  joint interpretation of images and text." The paper also shows GPT-4V making
  basic perceptual errors (Figure 6), i.e. the benchmark does test perception.
  This is the strongest steelman for MMMU's validity and belongs in the piece.
- **Even after MMMU-Pro's filtering, a large residual remains.** MMMU-Pro removed
  questions that three of four open LLMs answered text-only, then added six more
  distractor options, yet top models still score in the low-to-mid 50s on the
  ten-option Standard setting (GPT-4o 54.0, Claude 3.5 Sonnet 55.0). The
  benchmark is not mostly a disguised text test; the text-answerable and
  guessing components are a measurable slice, quantified by the 16.8-26.9 point
  overall drop, not the bulk.
- **The "number in circulation" mixes evaluation protocols.** Gemini 1.0
  reported Gemini Ultra with Maj@32 (62.4%) next to GPT-4V's single-sample pass@1
  (56.8%); Anthropic and Qwen report 0-shot chain-of-thought pass@1. A headline
  MMMU comparison across makers is therefore not always like-for-like, a
  distortion separate from the vision-versus-text one and worth naming so the
  writer does not attribute a protocol gap to a capability gap.

## Numbers

```text
Figure: 11,550 total questions (dev 150 : validation 900 : test 10,500)
Owner:  MMMU paper (Yue et al., CVPR 2024), Table 1
Scope:  full benchmark; splits as listed
```
```text
Figure: 6 disciplines / 30 subjects / 183 subfields; 30 image types
Owner:  MMMU paper, Table 1 and abstract
Scope:  full benchmark
```
```text
Figure: multiple-choice 10,861 (94.03%); open 689 (5.97%); image-in-question
        11,264 (97.52%)
Owner:  MMMU paper, Table 1
Scope:  full benchmark (11,550 questions)
```
```text
Figure: text-only GPT-4 (no image) 34.9% val / 33.8% test
Owner:  MMMU paper, Table 2
Scope:  MMMU validation (900) and test (10,500) overall accuracy
```
```text
Figure: random choice 22.1% val / 23.9% test; frequent choice 26.8% val / 25.8% test
Owner:  MMMU paper, Table 2
Scope:  MMMU validation and test overall accuracy
```
```text
Figure: GPT-4V(ision) 56.8% val / 55.7% test
Owner:  MMMU paper, Table 2
Scope:  MMMU validation and test overall accuracy
```
```text
Figure: overall MMMU-to-MMMU-Pro drop ranges 16.8% to 26.9% across models
Owner:  MMMU-Pro paper, abstract (overall = average of Standard 10-opt and Vision)
Scope:  MMMU (val) minus MMMU-Pro overall, per model
```
```text
Figure: MMMU-Pro Table 1, full series
        columns: Standard(4 opt) | Standard(10 opt) | Vision | MMMU(Val) |
        D1 = Standard(10) - Val | D2 = Vision - Val
Owner:  MMMU-Pro paper, Table 1
Scope:  MMMU-Pro settings vs MMMU validation, accuracy
  GPT-4o (0513):          64.7 | 54.0 | 49.7 | 69.1 | -15.1 | -19.4
  Claude 3.5 Sonnet:      63.7 | 55.0 | 48.0 | 68.3 | -13.3 | -20.3
  Gemini 1.5 Pro (0801):  60.6 | 49.4 | 44.4 | 65.8 | -16.4 | -21.4
  Gemini 1.5 Pro (0523):  57.6 | 46.5 | 40.5 | 62.2 | -15.7 | -21.7
  GPT-4o mini:            55.3 | 39.9 | 35.2 | 59.4 | -19.5 | -24.2
  Qwen2-VL-72B:           59.3 | 49.2 | 43.3 | 64.5 | -15.3 | -21.2
  InternVL2-Llama3-76B:   55.0 | 41.9 | 38.0 | 58.3 | -16.4 | -20.3
  InternVL2-40B:          47.4 | 36.3 | 32.1 | 55.2 | -18.9 | -23.1
  LLaVA-OneVision-72B:    52.3 | 38.0 | 24.0 | 56.8 | -18.8 | -32.8
  Qwen2-VL-7B:            46.6 | 34.1 | 27.0 | 54.1 | -20.0 | -27.1
  Pixtral-12B:            47.5 | 33.4 | 25.0 | 52.5 | -19.1 | -27.5
  VILA-1.5-40B:           46.8 | 35.9 | 14.1 | 51.9 | -16.0 | -37.8
  Random Choice:          24.9 | 12.8 | 12.4 | 22.1 |  -9.3 |  -9.7
  Frequent Choice:        27.8 | 12.1 | 12.1 | 26.8 | -14.7 | -14.7
  Human Expert (Medium):  82.1 | 80.8 | 80.8 | 82.6 |  -1.8 |  -1.8
```
```text
Figure: derived overall MMMU-Pro drop (using paper's averaging rule):
        GPT-4o approx 17.2 (69.1 - avg(54.0,49.7)=51.85);
        Claude 3.5 Sonnet approx 16.8 (68.3 - avg(55.0,48.0)=51.5);
        VILA-1.5-40B approx 26.9 (51.9 - avg(35.9,14.1)=25.0)
Owner:  derived from MMMU-Pro Table 1 cells + the stated averaging rule; the
        16.8 and 26.9 endpoints are the paper's abstract range. Present as
        derived, not as a printed per-model column.
Scope:  MMMU (val) minus MMMU-Pro overall
```
```text
Figure: Claude 3.5 Sonnet MMMU (validation) 68.3% (0-shot chain-of-thought)
Owner:  Anthropic, Claude 3.5 Sonnet model card addendum, Table 1
Scope:  MMMU validation, maker's own reported figure
```
```text
Figure: Gemini 1.5 Pro 62.2% on MMMU; Gemini Ultra 59.4% (pass@1) / 62.4% (Maj@32)
Owner:  Google, Gemini 1.5 report and Gemini 1.0 report respectively
Scope:  MMMU validation, makers' own reported figures
```
```text
Figure: Qwen2-VL-72B MMMU val 64.5% (7B 54.1%, 2B 41.1%)
Owner:  Alibaba, Qwen2-VL technical report, main results table
Scope:  MMMU validation, maker's own reported figure
```
```text
Figure: GPT-4o MMMU 69.1%
Owner:  OpenAI (hello-gpt-4o page). NOT read on OpenAI's own page (bot-blocked);
        corroborated identically by the Anthropic addendum (cited to OpenAI), the
        Qwen2-VL report, and MMMU-Pro Table 1's MMMU (Val) column.
Scope:  MMMU validation, maker's reported figure
```
```text
Figure: text-only accuracy on MMMU with no image: GeminiPro 42.9%; Sphinx-X-MoE
        43.6% (17.9 points above its own LLM backbone)
Owner:  MMStar (Chen et al., 2024), Section 1 (independent secondary)
Scope:  MMMU samples answered without visual input
```

## Source assets

```text
Asset: MMMU-Pro, Figure 3, "Accuracy of text-only LLMs in different sets of MMMU
       questions."
Shows: How the two filtering steps drop text-only models' guessing accuracy,
       i.e. the size of the text-answerable slice being removed. This is the
       single clearest visual for the article's central claim.
Crop:  Keep the axis labels and the before/after sets; do not crop away the
       baseline set that makes the drop legible.
```
```text
Asset: MMMU-Pro, Figure 2, "Two MMMU questions that are answered correctly by a
       text-only LLM Llama-3-70B Instruct."
Shows: A concrete worked example of a question a language model answers without
       the image, by finding a textual shortcut. Ideal for the lesson's "worked
       example" requirement.
Crop:  Retain the full question text and options so the reader can see the
       shortcut; the image thumbnail can stay small.
```
```text
Asset: MMMU-Pro, Figure 4, "Sample questions from MMMU-Pro Vision" (question
       embedded in a screenshot, up to 10 options).
Shows: What the vision-only setting looks like, why it forces the model to read
       the image, and the ten-option format at once.
Crop:  Keep one full screenshot example legible; omit the multi-panel grid if
       space is tight.
```
```text
Asset: MMMU paper, Figure 2, "Sampled MMMU examples from each discipline," and
       Figure 95, "Distribution of image types in the MMMU dataset."
Shows: The heterogeneity of image types (charts, chemical structures, music
       sheets, medical scans) that the "sees like an expert" claim rests on.
Crop:  For Figure 2, retain enough distinct disciplines to convey variety; a
       four-to-six-panel crop suffices.
```
```text
Asset: MMMU-Pro Table 1 (per-model MMMU vs MMMU-Pro series), rendered as a
       committed chart-N.py bar or slope chart.
Shows: The gap between headline MMMU (Val) and the harder MMMU-Pro Vision score
       for named flagships, which is the article's "real case where the number
       misled." Full series preserved in the Numbers section above.
Crop:  Not an image crop; a chart the writer builds. Label axes; cite MMMU-Pro
       Table 1 as the source in the caption.
```
```text
Asset: MMMU paper, Figure 6, "A basic perceptual error, easy for humans but
       challenging for GPT-4V."
Shows: The counterpoint that MMMU does test perception, useful for the steelman
       paragraph so the piece is not read as a takedown.
Crop:  Keep the image and the model's wrong answer together.
```

## Discarded

```text
URL: https://openai.com/index/hello-gpt-4o/ — OpenAI's own GPT-4o page, the home
     of the 69.1% figure, returns HTTP 403 to every fetch route tried (WebFetch,
     browser-style curl) and the Wayback route is blocked from this environment.
     The figure is recorded under Numbers as OpenAI-owned but corroborated from
     three opened records rather than read on OpenAI's page. Not counted as a
     read source.
```
```text
URL: https://raw.githubusercontent.com/openai/simple-evals/main/README.md —
     OpenAI's own evals repo, opened to recover a GPT-4o MMMU number, but it
     reports MMLU/GPQA/MATH/HumanEval/DROP and not MMMU. No usable figure.
```
```text
URL: https://cdn.openai.com/gpt-4o-system-card.pdf — opened; the GPT-4o system
     card is safety-focused and contains no MMMU result. No usable figure.
```
```text
URL: artificialanalysis.ai / vals.ai MMMU-Pro leaderboards — surfaced in search
     as third-party aggregators. Not opened as evidence: the commission bars
     sourcing the in-circulation number to a leaderboard aggregator, and every
     figure the argument needs is already owned by a primary above.
```
