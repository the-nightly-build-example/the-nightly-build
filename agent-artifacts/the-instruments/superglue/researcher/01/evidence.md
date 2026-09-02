# Evidence: the-instruments/superglue (01)

The evidence supports the commission fully. The SuperGLUE paper (arXiv 1905.00537)
owns every construction detail: the eight tasks each carry their own metric, the
overall score is an equal-weight average of per-task scores (with two-metric tasks
averaged internally first, quoted verbatim below), and the 89.8 "human baseline" is
a measurement built from five Amazon Mechanical Turk workers per item after a short
training step, not a fixed human ceiling. The DeBERTa paper (2006.03654) and
Microsoft's 6 January 2021 announcement own the crossing: a single 1.5-billion-
parameter DeBERTa model scored 89.9 against the 89.8 human row. Contemporaneous
secondary coverage (VentureBeat, SyncedReview, both 6 January 2021) carried this to
the public as "AI surpasses humans," while the SuperGLUE co-author Sam Bowman and
the DeBERTa authors themselves said in the same window that the crossing did not
mean the problem was solved.

The record is thin in one place and carries one precision correction the writer
must respect. Thin: the live SuperGLUE leaderboard is a client-side React app; the
page and its API path both return only the HTML shell to every tool available here,
so the ranked table could not be rendered directly. The crossing is instead pinned
through the DeBERTa paper's own results table, Microsoft's reproduction of the
leaderboard as Figure 1 dated 6 January 2021, and two independent secondary reports.
Correction: "DeBERTa was the first to beat the human baseline" is not quite what the
primaries say. DeBERTa's own paper claims first only for a *single* model on
macro-average, and its own Table 5 lists Google's ensemble entry "T5 + Meena" at
90.2, already above 89.8. See Contradictions.

## Sources

```text
URL:         https://arxiv.org/abs/1905.00537
Kind:        primary. The SuperGLUE paper itself; it owns the task set, the metrics,
             the aggregation rule, and the human-baseline method and number.
Establishes: SuperGLUE is eight tasks, each with its own metric; the leaderboard
             number is their equal-weight average; the human baseline is 89.8,
             built from crowd workers under a stated protocol; the best baseline
             model at launch (BERT++) scored 71.5, an 18.3-point gap below humans.
Paraphrase:  Title "SuperGLUE: A Stickier Benchmark for General-Purpose Language
             Understanding Systems," by Alex Wang, Yada Pruksachatkun, Nikita
             Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and
             Samuel R. Bowman. v1 submitted 2 May 2019; v2 12 Jul 2019; v3 13 Feb
             2020. The abstract states SuperGLUE was built because GLUE performance
             "has recently surpassed the level of non-expert humans, suggesting
             limited headroom for further research." Table 1 (Section 3) lists the
             eight tasks and their metrics. Section 3.3 gives the averaging rule.
             Table 3 (Section 5.2) gives baseline and human scores per task and
             overall. Appendix C gives the human-annotation protocol.
Locators:    Abstract; Table 1, Section 3; Section 3.3; Table 3, Section 5.2;
             Appendix C.
Quote:       Aggregation (Section 3.3): "Lacking a fair criterion with which to
             weight the contributions of each task to the overall score, we opt for
             the simple approach of weighing each task equally, and for tasks with
             multiple metrics, first averaging those metrics to get a task score."
             Human protocol (Appendix C): "In the training phase, workers are
             provided with instructions on the task, linked to an FAQ page, and are
             asked to annotate up to 30 examples from the development set." "For
             each example, we collect annotations from five workers and take a
             majority vote to estimate human performance." "For both steps and all
             tasks, the average pay rate is $23.75/hr."
```

```text
URL:         https://arxiv.org/abs/2006.03654
Kind:        primary for the crossing claim, with a stake. The DeBERTa authors own
             their model's result and the "first time" framing; they are the
             authoring, self-interested party, so the framing is theirs to make and
             must be reported as their claim.
Establishes: A single 1.5-billion-parameter DeBERTa model scored 89.9 on SuperGLUE
             macro-average against the 89.8 human baseline; the DeBERTa ensemble
             scored 90.3; and the authors themselves cap what this means.
Paraphrase:  Title "DeBERTa: Decoding-enhanced BERT with Disentangled Attention," by
             Pengcheng He, Xiaodong Liu, Jianfeng Gao, Weizhu Chen. v1 5 Jun 2020;
             v2 3 Jan 2021; v3 11 Jan 2021 (later versions to Oct 2021). The
             SuperGLUE results table lists Human 89.8, T5 (11B) 89.3, T5 (11B) +
             Meena 90.2, DeBERTa single (1.5B, with SiFT) 89.9, DeBERTa ensemble
             90.3.
Locators:    Abstract; SuperGLUE results table (Table 5); discussion following it.
Quote:       "The significant performance boost makes the single DeBERTa model
             surpass the human performance on the SuperGLUE benchmark for the first
             time in terms of macro-average score (89.9 versus 89.8)." "Despite its
             promising results on SuperGLUE, the model is by no means reaching the
             human-level intelligence of NLU."
```

```text
URL:         https://www.microsoft.com/en-us/research/blog/microsoft-deberta-surpasses-human-performance-on-the-superglue-benchmark/
Kind:        primary for the public announcement and its date. The authoring
             organization owns when and how it announced the result; it is
             promotional, so treat its adjectives as the producer's, not as neutral
             fact. Do not cite it as an authority on what the score means.
Establishes: The crossing was announced publicly on 6 January 2021, reproducing the
             leaderboard as Figure 1 for that date; the single model surpassed the
             human baseline "for the first time" at 89.9 vs 89.8; the ensemble led
             at 90.3; the model was 48 Transformer layers, 1.5 billion parameters;
             it beat Google's 11-billion-parameter T5. The post also caps the claim.
Paraphrase:  Published 6 January 2021. States the single DeBERTa model surpassed
             human performance "for the first time in terms of macro-average score
             (89.9 versus 89.8)," the ensemble "sits atop the SuperGLUE benchmark
             rankings" at 90.3 versus 89.8, and the leaderboard is shown "as of
             January 6th, 2021."
Locators:    Body; Figure 1 caption.
Quote:       "Despite its promising results on SuperGLUE, the model is by no means
             reaching the human-level intelligence of NLU."
```

```text
URL:         https://arxiv.org/abs/1910.10683
Kind:        primary for T5's own SuperGLUE score. The T5 authors own the number
             their model reported.
Establishes: T5 (11 billion parameters) reported a SuperGLUE average of 89.3, below
             the 89.8 human baseline; it was the leaderboard leader before the
             January 2021 crossing.
Paraphrase:  Title "Exploring the Limits of Transfer Learning with a Unified
             Text-to-Text Transformer," by Colin Raffel, Noam Shazeer, Adam Roberts,
             Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter
             J. Liu. The 11B model reached state of the art on GLUE, SuperGLUE,
             SQuAD and CNN/Daily Mail; its SuperGLUE average was 89.3. The 89.3
             figure is corroborated by the DeBERTa paper's own comparison table.
Locators:    Results section ("Putting it all together"); confirmed against DeBERTa
             Table 5.
Quote:       (none load-bearing beyond the number)
```

```text
URL:         https://arxiv.org/abs/1804.07461
Kind:        primary for the predecessor benchmark. The GLUE authors (an overlapping
             team: Wang, Singh, Michael, Hill, Levy, Bowman) own GLUE's design and
             its macro-average recipe, which SuperGLUE reuses.
Establishes: GLUE is SuperGLUE's predecessor and uses the same equal-weight macro-
             average of per-task scores; SuperGLUE exists because GLUE saturated
             (models passed non-expert human level), which is the taught GLUE lesson
             this article links.
Paraphrase:  Title "GLUE: A Multi-Task Benchmark and Analysis Platform for Natural
             Language Understanding," arXiv 1804.07461 (April 2018). GLUE reports a
             macro-average of per-task scores to rank systems. The saturation link
             the writer should lean on is stated by the SuperGLUE abstract, not
             invented here: GLUE performance "has recently surpassed the level of
             non-expert humans."
Locators:    Benchmark/scoring description; corroborated by 1905.00537 abstract.
Quote:       (see 1905.00537 abstract for the saturation sentence)
```

```text
URL:         https://super.gluebenchmark.com/leaderboard
Kind:        the artifact the lesson examines: the public leaderboard where the
             single number sits beside the human row. Recorded as it lives.
Establishes: intended to confirm the crossing and rankings firsthand.
Paraphrase:  The live page is a client-side React application. Fetching the URL, and
             the candidate data path /api/leaderboard/submissions/public, both
             returned only the application HTML shell; the ranked table renders only
             after in-browser JavaScript executes, which the available tools cannot
             do. The leaderboard contents as of 6 January 2021 are therefore
             confirmed indirectly: through the DeBERTa paper's Table 5, Microsoft's
             reproduction of the leaderboard as Figure 1 for that date, and the two
             secondary reports below, which agree on Human 89.8, DeBERTa ensemble
             90.3, T5 + Meena 90.2, T5 89.3.
Locators:    Page root; /api/leaderboard/submissions/public.
Quote:       (unrenderable; see Contradictions and the resolution note above)
```

```text
URL:         https://venturebeat.com/business/ai-models-from-microsoft-and-google-already-surpass-human-performance-on-the-superglue-language-benchmark
Kind:        secondary. Trade-press reporting by Kyle Wiggers from outside the
             authoring labs, on the crossing.
Establishes: how the crossing reached the public ("surpass human performance"); that
             the launch gap was "nearly 20-point"; that two entries, not one, had
             crossed by 6 January 2021; and it carries a direct on-record caution
             from a SuperGLUE co-author.
Paraphrase:  Published 6 January 2021. Reports that two models had surpassed the
             human baselines and were the first to do so, and that the SuperGLUE
             gap was nearly 20 points at launch. Sam Bowman (NYU) is quoted on the
             benchmark's limits.
Locators:    Headline; body; Bowman quote.
Quote:       Headline: "AI models from Microsoft and Google already surpass human
             performance on the SuperGLUE language benchmark." Body: "two models --
             one from Microsoft called DeBERTa and a second from Google called T5 +
             Meena -- have surpassed the human baselines." "When SuperGLUE was
             introduced, there was a nearly 20-point gap between the best-performing
             model and human performance on the leaderboard." Bowman: "There's no
             reason to believe that SuperGLUE will be able to detect further
             progress in natural language processing, at least beyond a small
             remaining margin."
```

```text
URL:         https://syncedreview.com/2021/01/06/microsoft-deberta-tops-human-performance-on-superglue-nlu-benchmark/
Kind:        secondary. Trade-press reporting on the crossing, independent of the
             authoring labs.
Establishes: a second, independent instance of the "AI tops humans" framing reaching
             the public the same day, with no caveat in the article body.
Paraphrase:  Published 6 January 2021. Reports DeBERTa scored 89.9 versus the 89.8
             human baseline, scaled to 1.5 billion parameters, "substantially"
             outperforming Google's larger T5, and frames it as "for the first time,
             a new model surpassed human baseline performance." The article body
             carries no caveat; a critical note appears only in a reader comment.
Locators:    Headline; body.
Quote:       "for the first time, a new model surpassed human baseline performance on
             the challenging natural language understanding (NLU) benchmark."
```

## Contradictions

- **"First to beat the human baseline" is contested by the primaries themselves.**
  The commission names DeBERTa (January 2021) as the model that passed the human row.
  That is defensible only with the qualifier the DeBERTa authors themselves use.
  Their claim is that the *single* DeBERTa model surpassed the human baseline "for
  the first time in terms of macro-average score." Their own Table 5 lists Google's
  ensemble entry "T5 + Meena" at 90.2, already above the 89.8 human row, and
  VentureBeat's 6 January 2021 report names *two* models, DeBERTa and T5 + Meena, as
  having surpassed the human baselines. The precise, sourced statement is: DeBERTa
  was the first *single* model to cross the human macro-average (89.9 vs 89.8,
  announced 6 January 2021), while an ensemble entry had also crossed by then. The
  writer should not say flatly that DeBERTa "was the first to beat humans" without
  the single-model qualifier.

- **"AI beats humans" versus what the producers said in the same week.** The public
  framing (VentureBeat headline; SyncedReview) is that AI surpassed human language
  understanding. The people who made the number said the opposite at the same time:
  the DeBERTa authors ("by no means reaching the human-level intelligence of NLU")
  and the SuperGLUE co-author Bowman (the benchmark can no longer "detect further
  progress"). This is not a contradiction in the evidence; it is the gap between the
  measurement and its reception, which is the lesson's subject.

- **The "human" row is not a uniform human ceiling.** The per-task human scores in
  the SuperGLUE paper's Table 3 range from 80.0 (WiC) to 100.0 (COPA, WSC), and on
  MultiRC the human exact-match figure is 51.9. A single 89.8 label hides that the
  humans measured were untrained crowd workers whose own score swings by task and by
  metric. This supports the commission rather than undermining it.

## Numbers

```text
Figure: 89.8 (SuperGLUE overall, macro-average)
Owner:  SuperGLUE paper 1905.00537, Table 3
Scope:  Estimated human baseline across the eight non-diagnostic tasks; five
        Mechanical Turk workers per item, majority vote, after training on up to 30
        development examples.
```

```text
Figure: 71.5 (SuperGLUE overall)
Owner:  SuperGLUE paper 1905.00537, Table 3
Scope:  BERT++, the best baseline model at launch (May 2019); 18.3 points below the
        human baseline. Secondary coverage rounds this to a "nearly 20-point gap."
```

```text
Figure: 89.9 (SuperGLUE overall, macro-average)
Owner:  DeBERTa paper 2006.03654, Table 5; announced Microsoft blog 6 Jan 2021
Scope:  Single DeBERTa model, 1.5 billion parameters, 48 layers, with SiFT; first
        single model to cross the 89.8 human macro-average.
```

```text
Figure: 90.3 (SuperGLUE overall)
Owner:  DeBERTa paper 2006.03654, Table 5; Microsoft blog Figure 1 (6 Jan 2021)
Scope:  DeBERTa ensemble; top of the leaderboard as of 6 January 2021.
```

```text
Figure: 90.2 (SuperGLUE overall)
Owner:  DeBERTa paper 2006.03654, Table 5
Scope:  Google "T5 (11B) + Meena" ensemble entry; already above the 89.8 human row,
        which qualifies DeBERTa's "first" claim (see Contradictions).
```

```text
Figure: 89.3 (SuperGLUE overall)
Owner:  T5 paper 1910.10683 results; corroborated by DeBERTa Table 5
Scope:  T5, 11 billion parameters; the leaderboard leader before the January 2021
        crossing, still 0.5 below the human baseline.
```

```text
Figure: Eight tasks, each with its own metric
Owner:  SuperGLUE paper 1905.00537, Table 1
Scope:  BoolQ (accuracy); CB (accuracy / F1); COPA (accuracy); MultiRC (F1a / exact
        match); ReCoRD (F1 / exact match); RTE (accuracy); WiC (accuracy); WSC
        (accuracy). Two-metric tasks are averaged internally first, then all eight
        task scores are averaged with equal weight.
```

```text
Figure: Per-task human scores (Table 3)
Owner:  SuperGLUE paper 1905.00537, Table 3
Scope:  BoolQ 89.0; CB 95.8 / 98.9; COPA 100.0; MultiRC 81.8 F1a / 51.9 EM; ReCoRD
        91.7 F1 / 91.3 EM; RTE 93.6; WiC 80.0; WSC 100.0. Shows the 89.8 average
        hides a spread from 80.0 to 100.0 and a very low 51.9 on one metric.
```

```text
Figure: $23.75/hr; five workers per item; up to 30 training examples
Owner:  SuperGLUE paper 1905.00537, Appendix C
Scope:  The human-baseline annotation protocol; establishes the 89.8 row as a
        crowd-worker measurement, not an expert ceiling.
```

## Source assets

```text
Asset: SuperGLUE paper (1905.00537), Table 1 — the eight tasks with their metrics.
Shows: that "one number" averages scores measured in different units (accuracy, F1,
       exact match, and two-metric tasks), the core of the aggregation lesson.
Crop:  must retain the task column and the metric column together; may omit the
       example/size columns if present.
```

```text
Asset: SuperGLUE paper (1905.00537), Table 3 — the results table with per-task and
       overall scores for baselines and the human row.
Shows: the 89.8 human average sitting above 71.5 BERT++ at launch, and the per-task
       human spread (WiC 80.0 to COPA/WSC 100.0, MultiRC EM 51.9) that the single
       number conceals.
Crop:  must retain the Human row and the overall Average column; keep enough per-task
       columns to show the 80.0-to-100.0 spread. Do not crop to only the overall
       column, which would hide the point.
```

```text
Asset: Microsoft Research blog, Figure 1 — the SuperGLUE leaderboard "as of January
       6th, 2021," reproduced by the authoring org. (Equivalent data lives in the
       DeBERTa paper's Table 5.)
Shows: DeBERTa ensemble 90.3 and single 89.9 above the human 89.8 row, with T5 +
       Meena 90.2 also above it — the crossing and its qualifier in one image.
Crop:  must retain the human-baseline row and at least the DeBERTa and T5 + Meena
       rows with the overall column; keep the dateline. The blog is promotional, so
       caption it as the producer's reproduction, not a neutral leaderboard capture.
```

## Discarded

```text
URL: https://web.archive.org/web/2021*/https://super.gluebenchmark.com/leaderboard —
     archived leaderboard snapshots would confirm the live ranking, but web.archive.org
     is not fetchable through the available tools; recorded as an unmet check, not a
     rejection of the source.
```
