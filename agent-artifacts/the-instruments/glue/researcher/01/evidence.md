# Evidence: the-instruments/glue (01)

The record supports the commission's core spine firmly. GLUE (Wang et al. 2018)
is nine English NLU tasks scored as an unweighted macro-average of per-task
metrics; the human baseline of 87.1 was not in the original paper but was
measured separately by Nangia and Bowman (2019) using non-expert crowdworkers.
SuperGLUE (Wang et al. 2019) exists explicitly because GLUE performance "surpassed
the level of non-expert humans," and its own human baseline is 89.8. The surpass
events are verified to the day from dated primary snapshots: Microsoft's MT-DNN
passed the GLUE human estimate (87.6 vs 87.1) on June 6, 2019, and DeBERTa passed
the SuperGLUE human baseline (single 89.9, ensemble 90.3 vs 89.8) on January 6,
2021. The "shortcut, not comprehension" claim is well sourced: hypothesis-only
NLI classifiers hit ~67% (SNLI) and ~53% (MultiNLI); a cues-only baseline hits
59.6% on COPA (a SuperGLUE task). The record is thinnest on two points. First,
the commission's round timings are slightly off: GLUE's human number was
surpassed ~13 months after the benchmark launched (not "within a year" from
launch in the tidy sense), and critically the human baseline itself was only
published in late May 2019 and beaten within about two weeks. SuperGLUE's took
~20 months (not "~18"). Second, the strongest counter to the commission's own
"misled people" frame comes from the benchmark and model authors themselves:
they never claimed "solved understanding," and the DeBERTa team explicitly wrote
their record-topping model is "by no means reaching the human-level intelligence
of NLU." The hype was mostly downstream of the labs, not from them. That does not
undermine the angle, but the writer must locate the "misleading" in reception and
headline shorthand, not in the authors' claims.

## Sources

```text
URL:         https://arxiv.org/abs/1804.07461
Kind:        primary — the benchmark's own authors (Wang, Singh, Michael, Hill,
             Levy, Bowman); owns the definition of GLUE, its tasks, and its scoring.
Establishes: The nine GLUE tasks and their metrics; that the overall GLUE score
             is an unweighted macro-average across the nine tasks, with
             two-metric tasks averaged internally first; the hand-built diagnostic
             set. This version does NOT contain a human baseline number.
Paraphrase:  GLUE bundles nine existing English sentence/sentence-pair tasks
             (single-sentence: CoLA, SST-2; similarity/paraphrase: MRPC, STS-B,
             QQP; inference: MNLI, QNLI, RTE, WNLI) into one leaderboard. Each
             task keeps its native metric (accuracy, F1, Matthews correlation,
             or Pearson/Spearman). A model's headline number is the simple
             average of the per-task scores. A separate hand-curated diagnostic
             set (Lexical Semantics, Predicate-Argument Structure, Logic,
             Knowledge) is for analysis, not the leaderboard number.
Locators:    Abstract; tasks table (Sec. 2 / Table 1); scoring description; Sec.
             on the diagnostic dataset. Submission history: v1 20 Apr 2018,
             v2 18 Sep 2018, v3 22 Feb 2019.
Quote:       "For tasks with multiple metrics ... we use an unweighted average of
             the metrics as the score for the task when computing the overall
             macro-average."
```

```text
URL:         https://arxiv.org/abs/1905.00537
Kind:        primary — same core author group (Wang et al.); owns SuperGLUE's
             design, its human baseline, and the stated reason GLUE was retired.
Establishes: That GLUE was retired because model performance passed non-expert
             humans; the eight SuperGLUE tasks; SuperGLUE human baseline 89.8;
             the benchmark authors' own report that GLUE SOTA (88.4, XLNet /
             Yang et al. 2019) passed the 87.1 human number "as of early July
             2019"; SuperGLUE's equal-weight aggregation.
Paraphrase:  One year after GLUE, its single-number metric had been saturated:
             the top system had passed the non-expert human level, leaving little
             headroom. SuperGLUE keeps the same averaging recipe but swaps in
             eight harder tasks (BoolQ, CB, COPA, MultiRC, ReCoRD, RTE, WiC, WSC)
             and publishes a human baseline of 89.8, with per-task human numbers
             ranging from 80.0 (WSC) to 100.0 (COPA). The authors state that the
             GLUE SOTA of 88.4 (XLNet) exceeded the 87.1 human number by 1.3
             points by early July 2019.
Locators:    Abstract; Introduction (GLUE-surpassed framing and the "88.4 vs 87.1"
             sentence); tasks table with human-performance column; scoring
             section. Submission history: v1 2 May 2019, v2 12 Jul 2019,
             v3 13 Feb 2020.
Quote:       "performance on the benchmark has recently surpassed the level of
             non-expert humans, suggesting limited headroom for further research."
             And: "the current state of the art GLUE Score as of early July 2019
             (88.4 from Yang et al., 2019) surpasses human performance (87.1 from
             Nangia and Bowman, 2019) by 1.3 points."
```

```text
URL:         https://arxiv.org/abs/1905.10425
Kind:        primary — Nangia and Bowman; this paper owns the GLUE human baseline
             number the leaderboard uses.
Establishes: The GLUE human baseline is 87.1 (macro-average), measured with
             non-expert annotators given brief instructions and a small number of
             examples; humans beat the state of the art on six of the nine tasks
             at the time.
Paraphrase:  The GLUE "human baseline" is not an intrinsic ceiling; it is a
             conservative estimate produced by hiring non-expert crowd annotators,
             training each on short instructions and roughly twenty examples, and
             scoring their majority answers on the same test sets. Their average
             is 87.1. The paper frames headroom above the then-current model SOTA
             as real but shrinking fast.
Locators:    Abstract; per-task human results table. Title: "Human vs. Muppet: A
             Conservative Estimate of Human Performance on the GLUE Benchmark."
             Submission history: v1 24 May 2019, v2 28 May 2019, v3 1 Jun 2019.
Quote:       "these annotators robustly outperform the state of the art on six of
             the nine GLUE tasks and achieve an average score of 87.1."
Note:        The "SOTA ~83.9 at time of writing" figure appears in the paper's
             framing but was read via the abstract page; treat the firm figure
             here as the 87.1 human average, which the abstract states directly.
```

```text
URL:         https://arxiv.org/abs/1803.02324
Kind:        primary — Gururangan, Swayamdipta, Levy, Schwartz, Bowman, Smith;
             owns the hypothesis-only artifact finding for NLI (the data behind
             GLUE's MNLI/QNLI/RTE-style tasks).
Establishes: The core annotation-artifact result: a text classifier reading only
             the hypothesis (never the premise) labels ~67% of SNLI and ~53% of
             MultiNLI correctly, far above chance for a 3-class task (~33%).
Paraphrase:  Crowd-written NLI datasets leak the answer into the hypothesis alone.
             A model that never sees the premise still classifies most examples,
             because writers reuse tells: negation words track contradiction,
             vague/general hypotheses track entailment. So a high NLI score can
             reflect these surface regularities rather than reasoning about the
             premise-hypothesis relation. This is the plain meaning of
             "annotation artifact": a statistical shortcut left in the data by how
             it was collected, unrelated to the ability the task means to measure.
Locators:    Abstract (headline 67% / 53% figures stated there); results tables
             for the hypothesis-only baselines; analysis of negation/vagueness.
             Submission: v1 6 Mar 2018, v2 16 Apr 2018 (NAACL 2018).
Quote:       "a simple text categorization model can correctly classify the
             hypothesis alone in about 67% of SNLI ... and 53% of MultiNLI ...
             Our findings suggest that the success of natural language inference
             models to date has been overestimated."
```

```text
URL:         https://arxiv.org/abs/1911.00225
Kind:        primary — Kavumba, Inoue, Heinzerling, Singh, Reisert, Inui; owns the
             superficial-cue finding for COPA, a SuperGLUE task.
Establishes: SuperGLUE-specific artifact evidence. A cues-only baseline (choosing
             the answer from token cues in the alternatives alone) reaches 59.6%
             (+/-2.3) on COPA vs 50% chance; BERT-large drops from 76.5% on
             original COPA to 74.5% on Balanced COPA (cues neutralized), while
             RoBERTa-large is stable (87.7% -> 89.0%).
Paraphrase:  COPA (pick the more plausible cause/effect) carries single-token
             giveaways. A model using only those cues beats chance by ~10 points.
             When the cues are balanced away, BERT loses ground, showing it had
             leaned on them; RoBERTa does not, showing artifact-reliance is
             model-specific, not universal. Same shortcut pattern as GLUE-era NLI,
             now demonstrated inside SuperGLUE.
Locators:    Abstract; cues-only baseline result; BERT/RoBERTa original-vs-balanced
             results tables. Title: "When Choosing Plausible Alternatives, Clever
             Hans can be Clever." Submission: 1 Nov 2019.
Quote:       cues-only 59.6% (+/-2.3); BERT-large 76.5% -> 74.5%; RoBERTa-large
             87.7% -> 89.0% (original COPA -> Balanced COPA).
```

```text
URL:         https://learn.microsoft.com/en-us/archive/blogs/stevengu/microsoft-achieves-human-performance-estimate-on-glue-benchmark
Kind:        primary — Microsoft's own announcement; owns the MT-DNN result and
             carries a dated leaderboard snapshot.
Establishes: The date GLUE's human estimate was first passed: June 6, 2019,
             MT-DNN at 87.6 vs the 87.1 human estimate. A concrete worked example
             of aggregation hiding a weak task: on WNLI, prior SOTA including BERT
             could barely beat the majority-vote baseline of 65.1 (human 95.9),
             and MT-DNN only reached near-human overall after a special method
             lifted WNLI to 89.0.
Paraphrase:  Microsoft reports MT-DNN passing the GLUE human estimate on a
             specific date, attributing the human number to Nangia and Bowman
             (1905.10425). The blog is explicit that the last barrier was one
             task, WNLI, where models had scored no better than always guessing
             the majority class, and that fixing that single task is what carried
             the average over the human line. This is the exact mechanism the
             lesson needs: a nine-task average can sit at human level while a
             model is at chance on one of the nine.
Locators:    Body paragraph ("surpassed the estimate for human performance ...
             (87.6 vs. 87.1) on June 6, 2019"); WNLI paragraphs; embedded dated
             leaderboard image (June 6, 2019). ms.date: 2019-06-20.
Quote:       "finally surpassed the estimate for human performance ... on the
             overall average score on GLUE (87.6 vs. 87.1) on June 6, 2019." And:
             "previous state-of-the-art ML models can hardly outperform the naive
             baseline of majority voting (scored at 65.1) [on WNLI], including
             BERT."
Note:        Canonical archived URL after 301 from the old blogs.msdn.microsoft.com
             address. Author byline "Guggs" (Steven Gu), Microsoft.
```

```text
URL:         https://www.microsoft.com/en-us/research/blog/microsoft-deberta-surpasses-human-performance-on-the-superglue-benchmark/
Kind:        primary — Microsoft's own announcement; owns the DeBERTa result and
             carries the authors' own caveat.
Establishes: The date SuperGLUE's human baseline was passed: January 6, 2021,
             single DeBERTa 89.9 and ensemble 90.3 vs the 89.8 human baseline; and
             the authors' explicit disclaimer that this is not human-level
             understanding.
Paraphrase:  DeBERTa (1.5B-parameter, 48-layer variant) topped the SuperGLUE
             leaderboard, the single model passing the human baseline "for the
             first time." The same post states plainly that beating the benchmark
             does not mean the model understands language as a human does, and
             notes humans still generalize compositionally from few examples in
             ways the model cannot. This is the strongest in-record evidence that
             the "machines understand language" reading was never the builders'
             claim.
Locators:    Body (scores 89.9 / 90.3 vs 89.8; "for the first time"); caveat
             paragraph near the close. Published January 6, 2021.
Quote:       "the single DeBERTa model surpass[es] the human performance on
             SuperGLUE for the first time." Caveat: "Despite its promising results
             on SuperGLUE, the model is by no means reaching the human-level
             intelligence of NLU."
```

```text
URL:         https://aclanthology.org/2020.acl-main.463/
Kind:        primary — Bender and Koller, ACL 2020 position paper; owns the
             argument that benchmark success is not evidence of understanding.
Establishes: The steelmanned critique the commission needs: a system trained only
             on linguistic form has, in principle, no path to meaning, so passing
             form-based NLU benchmarks does not show comprehension.
Paraphrase:  The "octopus" position paper argues that models trained purely on
             text form cannot thereby acquire meaning, and warns against the hype
             that reads benchmark wins as "understanding." It is the primary to
             cite (not commentary) for "saturation is not comprehension," and it
             names the hype directly as a failure of scientific framing.
Locators:    Abstract; thesis statement. Title: "Climbing towards NLU: On Meaning,
             Form, and Understanding in the Age of Data." Proceedings of ACL 2020.
Quote:       "we argue that a system trained only on form has a priori no way to
             learn meaning." And: "these successes sometimes lead to hype in which
             these models are being described as 'understanding' language or
             capturing 'meaning'."
Note:        Authors are Bender and Koller (not "Koehler").
```

```text
URL:         https://gilbane.com/2021/01/microsoft-announces-deberta-surpasses-human-performance-on-superglue/
Kind:        secondary — The Gilbane Advisor, a third-party industry outlet
             reporting on Microsoft's DeBERTa announcement; no stake in the result.
Establishes: How the surpass was received and framed outside the lab: as passing
             a specific benchmark's macro-average, dated Jan 6, 2021, not as
             general human-level comprehension. Useful as the calibrated end of the
             reception spectrum.
Paraphrase:  A trade outlet repeats the 89.9 / 90.3 vs 89.8 scores and the "for
             the first time" framing, but narrows the claim to the macro-average
             on this benchmark and does not assert human-like comprehension. A
             repetition supports that the claim was made and circulated, not that
             it is true.
Locators:    Dateline January 6, 2021; scores and framing in body.
Quote:       "the single DeBERTa model surpass[es] the human performance on
             SuperGLUE for the first time in terms of macro-average score."
```

## Contradictions

- The commission's own "misled people" frame vs. the authors' claims. The
  benchmark builders did not claim understanding was solved; they treated
  saturation as a signal to raise the bar and built SuperGLUE (1905.00537). The
  DeBERTa team, sitting atop SuperGLUE, wrote their model is "by no means
  reaching the human-level intelligence of NLU"
  (microsoft.com DeBERTa blog). The "AI understands language now" reading lives in
  headlines and public reception, not in the primaries. The writer should place
  the misleading there, not in the authors' mouths, or the angle will misattribute.

- Commission timings vs. verified dates. Commission says GLUE's baseline was
  passed "within about a year" and SuperGLUE's "within ~18 months." Verified:
  GLUE launched April/May 2018 (paper v1 20 Apr 2018; MT-DNN blog says "since its
  release in early 2018") and its human estimate (87.1) was passed 6 Jun 2019 by
  MT-DNN, ~13-14 months after launch. SuperGLUE launched 2 May 2019 and its human
  baseline (89.8) was passed 6 Jan 2021, ~20 months later. Use the exact dates.

- A sharper fact the round numbers hide: GLUE's human baseline (Nangia and Bowman)
  was only published ~24-28 May 2019 and was passed within about two weeks
  (MT-DNN, 6 Jun 2019; XLNet 88.4 by early July per 1905.00537). The human number
  and its defeat are nearly simultaneous. This strengthens the lesson (the "human
  baseline" was a late, thin, conservative estimate, not a long-standing ceiling),
  but it contradicts any telling where models slowly closed a durable human gap.

- Artifact reliance is model-specific, not universal. Kavumba et al. (1911.00225)
  show BERT leans on COPA cues but RoBERTa does not (it improves on Balanced COPA).
  So "the tasks contain shortcuts" is firm; "every high scorer is exploiting
  shortcuts" is not. The honest claim is that a high score is consistent with
  shortcut exploitation and does not by itself rule it out.

## Numbers

```text
Figure: GLUE overall score = unweighted macro-average of 9 per-task scores
Owner:  Wang et al. 2018 (1804.07461)
Scope:  Two-metric tasks (MRPC acc/F1, QQP acc/F1, STS-B Pearson/Spearman)
        averaged internally first, then averaged across all 9 tasks equally.
```

```text
Figure: 9 GLUE tasks and metrics
Owner:  Wang et al. 2018 (1804.07461)
Scope:  CoLA (Matthews corr; ~8.5k train), SST-2 (acc; ~67k), MRPC (acc/F1;
        ~3.7k), STS-B (Pearson/Spearman; ~7k), QQP (acc/F1; ~364k), MNLI (acc;
        ~393k), QNLI (acc; ~105k), RTE (acc; ~2.5k), WNLI (acc; ~634).
```

```text
Figure: GLUE human baseline = 87.1 (macro-average)
Owner:  Nangia & Bowman 2019 (1905.10425)
Scope:  Non-expert crowd annotators, brief instructions + small example set,
        scored on the GLUE test sets; humans beat then-SOTA on 6 of 9 tasks.
```

```text
Figure: GLUE human baseline first surpassed = 87.6 vs 87.1, on 2019-06-06
Owner:  Microsoft MT-DNN blog (learn.microsoft.com archive)
Scope:  MT-DNN ensemble, overall GLUE macro-average; corroborated by 1905.00537
        (XLNet 88.4 by "early July 2019").
```

```text
Figure: WNLI as the aggregation-hiding example = prior SOTA incl. BERT ~65.1
        (majority-vote baseline) vs human 95.9; MT-DNN lifted WNLI to 89.0
Owner:  Microsoft MT-DNN blog
Scope:  WNLI test accuracy, one of the 9 GLUE tasks; a model at the chance/
        majority floor on this task while near-human on the 9-task average.
```

```text
Figure: SuperGLUE human baseline = 89.8 (per-task range 80.0 WSC to 100.0 COPA)
Owner:  Wang et al. 2019 (1905.00537)
Scope:  8-task equal-weight average; two-metric tasks averaged first.
```

```text
Figure: SuperGLUE human baseline surpassed = single 89.9 / ensemble 90.3 vs 89.8,
        on 2021-01-06
Owner:  Microsoft DeBERTa blog
Scope:  SuperGLUE macro-average; DeBERTa 1.5B / 48-layer variant.
```

```text
Figure: NLI hypothesis-only baseline = ~67% (SNLI), ~53% (MultiNLI); chance ~33%
Owner:  Gururangan et al. 2018 (1803.02324)
Scope:  3-class NLI; classifier reads hypothesis only, premise withheld.
```

```text
Figure: COPA cues-only baseline = 59.6% (+/-2.3); chance 50%. BERT-large 76.5%
        -> 74.5% (original -> Balanced COPA); RoBERTa-large 87.7% -> 89.0%
Owner:  Kavumba et al. 2019 (1911.00225)
Scope:  COPA (a SuperGLUE task); binary choice.
```

## Source assets

```text
Asset: GLUE tasks table (Table 1, 1804.07461) listing each task, its metric,
       and dataset sizes.
Shows: That "the GLUE score" is one average over nine different tasks measured in
       four different units (accuracy, F1, Matthews corr, Pearson/Spearman) — the
       heart of the "what got averaged" lesson.
Crop:  Keep the task-name, metric, and size columns; a crop can drop domain/source
       columns without losing the point.
```

```text
Asset: Dated GLUE leaderboard snapshot, June 6, 2019 (image embedded in the MT-DNN
       blog).
Shows: The exact moment MT-DNN's 87.6 sits above the 87.1 human row — a primary,
       dated record of the surpass, with the human baseline visible as a
       leaderboard entry.
Crop:  Retain the top rows including the "Human Baselines" row and the date; omit
       lower-ranked entries.
```

```text
Asset: SuperGLUE tasks table with human-performance column (1905.00537).
Shows: The 89.8 average and its per-task spread (80.0 WSC to 100.0 COPA),
       demonstrating how uneven human scores are folded into one number.
Crop:  Keep task names, metric, and the human column; the model-baseline columns
       are optional.
```

```text
Asset: SuperGLUE leaderboard figure, January 6, 2021 (DeBERTa blog).
Shows: DeBERTa above the human baseline row — the dated primary record of the
       second surpass.
Crop:  Keep the human-baseline row and DeBERTa rows and the date.
```

```text
Asset: COPA original-vs-Balanced results (Kavumba et al. 2019).
Shows: BERT losing ground when cues are removed while RoBERTa holds — a compact
       picture of artifact reliance being real but model-specific.
Crop:  Keep the BERT and RoBERTa rows for original vs Balanced COPA and the
       cues-only baseline row.
```

## Discarded

```text
URL: https://syncedreview.com/2021/01/06/microsoft-deberta-tops-human-performance-on-superglue-nlu-benchmark/
     403 Forbidden on fetch; could not read firsthand, so not cited. The Gilbane
     Advisor covers the same event and was readable, so it serves as the secondary.
```

```text
URL: https://arxiv.org/pdf/2103.06312 (AI Index 2021 report PDF)
     Exceeded fetch size limit; could not read the relevant section firsthand.
     Not needed: the surpass dates are established by dated primary snapshots
     (MT-DNN and DeBERTa blogs) and the SuperGLUE paper's own reporting.
```

```text
URL: https://www.windowscentral.com/microsofts-neural-language-model-surpasses-human-performance-superglue-test
     Article body not retrievable (page returned only nav/signup chrome). Not
     cited; would only have duplicated the reception point the Gilbane secondary
     already carries.
```

```text
URL: https://hai.stanford.edu/ai-index/2021-ai-index-report
     Landing page only; no benchmark-timeline detail in the retrievable content.
     Not cited.
```
