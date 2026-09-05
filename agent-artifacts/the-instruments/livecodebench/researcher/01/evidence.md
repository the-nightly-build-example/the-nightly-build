# Evidence record: the-instruments/livecodebench (01)

The evidence firmly supports the commissioned angle. The LiveCodeBench paper
(Jain et al., 2024) establishes firsthand who built the benchmark, from what
data, and by what procedure, including the moving-cutoff mechanism, the pass@1
metric, and the four scenarios named exactly. It also supplies, firsthand, the
contamination case study the article needs: DeepSeek's performance collapses on
LeetCode problems released after its training cutoff, and separately, a static
HumanEval score misled about a small model (DS-Ins-1.3B) that was overfit. The
official GitHub repository documents six dataset versions (v1 through v6) with
different date ranges and problem counts, and two vendor reports (DeepSeek-V3,
Qwen2.5-Coder) each cite a LiveCodeBench number tied to a *different* self-chosen
window, which is the concrete proof that two LiveCodeBench numbers are not
comparable. Where the record is thin: I could not fully extract DeepSeek-V3's
*chat*-model LiveCodeBench figure (the HTML render truncated before the instruct
table), so the verified DeepSeek score is from its base-model table. The angle is
not undermined; the strongest counter-evidence is that the moving cutoff is not a
perfect fix (an independent survey and the paper's own details both show this),
which the article should present as a real limit, not a refutation.

The paper read is v2 (revised 6 June 2024), which describes the 511-problem
release. The live benchmark has grown since; version facts below come from the
official repository, dated by their own release tags.

## Sources

```text
URL:         https://arxiv.org/abs/2403.07974
Kind:        primary. The paper that owns the benchmark's design, procedure, and
             every figure the article rests on. Authored by the team that built
             LiveCodeBench. (Read as the v2 PDF; cite the abstract page.)
Establishes: Who built it and when; the stated purpose (older benchmarks like
             HumanEval/MBPP are saturated and at risk of contamination); the data
             sources (LeetCode, AtCoder, CodeForces); the moving-cutoff
             procedure; pass@1; the four scenarios; the contamination case study;
             the HumanEval-overfitting case.
Paraphrase:  Authors: Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan,
             Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, Ion
             Stoica (UC Berkeley, MIT, Cornell per the leaderboard post below).
             Submitted 12 Mar 2024 (v1); revised 6 Jun 2024 (v2). The v2 release
             holds 511 problems from contests on the three platforms, released
             May 2023 to May 2024. The benchmark is built expressly so that a
             newer model can be scored only on problems released after its
             training cutoff, avoiding contamination. Four scenarios: code
             generation, self-repair, code execution, test output prediction.
             pass@1 for code generation is "the fraction of the problems for
             which the model was able to generate a program passing all tests"
             (Sec. 3.3). For code execution, a generation is correct if
             "assert f(input) == generated_output passes." The cutoff used for a
             model is its published training-cutoff date, "normalized to the
             release date if the training cutoff date is not published" (Sec.
             3.1). Problems are tagged with the contest date D as their release
             date. A "scrolling window" selects problems whose release date falls
             in a given time window. Contamination finding (Sec. 5.1): "We notice
             a stark drop in the performance of DS-Ins-33B model after Aug. 2023
             (right before its release date)"; the base model "DS-Base-33B ...
             dropping from Pass@1 ~60 in May problems to Pass@1 ~0 in September
             LeetCode problems"; "performance of the GPT-4-O model drops on
             problems released since November (its official cutoff date)";
             Codestral "achieves Pass@1 36.5 on problems released between May'23
             and Jan'24 and Pass@1 28.3 on problems since Feb'24." The drop
             "primarily occurs for the LeetCode problems only," while AtCoder
             performance is "relatively smooth across the months." For model
             comparisons the authors "only consider problems released since Sep
             2023" (349 problems) to sidestep DeepSeek contamination.
             HumanEval-overfitting finding (Sec. 5.2): using HumanEval+, models
             split into two clusters; some "perform well only on HumanEval+ but
             not as well on LiveCodeBench," which are "primarily ... the
             fine-tuned variants of open-access models." Worked case: "DS-Ins-1.3B
             which achieves 59.8% Pass@1 on HumanEval+ but only 26.3% on
             LCB-Easy." And "DS-Ins-33B is merely 4.3 point behind GPT-4-Turbo on
             HumanEval+ but 16.2 points (69%) on LCB code generation scenario."
             Correlation between HumanEval+ and LCB-Easy is "only a moderate
             correlation of 0.72." Cross-scenario pass@1 correlations are "over
             0.88 across all pairs," 0.98 for generation/self-repair, 0.96 for
             test-output/execution. Evaluated 18 base + 34 instruction-tuned
             models.
Locators:    Abstract; Sec. 1 & Fig. 1 (contamination motivation); Sec. 3.1-3.3
             (curation, cutoff, scenarios, pass@1); Table 1 (problem counts);
             Sec. 5.1 (contamination case); Sec. 5.2 & Fig. 5 (HumanEval
             overfitting).
Quote:       "for a new model and the corresponding cutoff date (normalized to
             the release date if the training cutoff date is not published), we
             can measure the performance of the model on benchmark problems
             released after the cutoff date." (Sec. 3.1)
```

```text
URL:         https://livecodebench.github.io/
Kind:        primary. The benchmark's own project site, authored by the team.
Establishes: The public statement of the contamination method and the four
             scenarios, in the authors' own words for a general reader.
Paraphrase:  States the benchmark "annotates problems with release dates, and
             thus allows evaluating models on problems released during a specific
             time period," so a newer model is tested "on problems released after
             D to measure its generalization on unseen problems," where D is the
             training cutoff. Names the four scenarios: code generation,
             self-repair, test output prediction, code execution. The site text
             read described "over three hundred" problems (an older snapshot than
             the 511-problem v2 paper and the current v6 repository), so the site
             is a poor source for the current count; use the repository for that.
Locators:    Landing page, "contamination" and "scenarios" sections.
Quote:       "LiveCodeBench annotates problems with release dates, and thus
             allows evaluating models on problems released during a specific time
             period."
```

```text
URL:         https://github.com/livecodebench/livecodebench
Kind:        primary. The official code repository and its README, owned by the
             benchmark team; the authority for the versioned releases.
Establishes: That "LiveCodeBench" is not one fixed set but a series of dated
             releases, each a different window and problem count -- the mechanical
             root of the "not comparable" problem. Also the exact scrolling
             flags.
Paraphrase:  Dataset versions: release_v1 = May 2023-Mar 2024, 400 problems;
             release_v2 = May 2023-May 2024, 511; release_v3 = May 2023-Jul 2024,
             612; release_v4 = May 2023-Sep 2024, 713; release_v5 = May 2023-Jan
             2025, 880; release_v6 = May 2023-Apr 2025, 1055. Default is
             release_latest. Evaluation over a window uses --start_date and
             --end_date flags in YYYY-MM-DD format; the paper's contamination-safe
             runs used --start_date 2023-09-01.
Locators:    README, "Versioning"/dataset-versions section and the run-flags
             section.
Quote:       "release_v6 ... problems released between May 2023 and Apr 2025
             containing 1055 problems."
```

```text
URL:         https://arxiv.org/abs/2412.19437
Kind:        primary, for the claim that a vendor report cites a LiveCodeBench
             number bound to a specific window. It is DeepSeek's own report of its
             own model; it is not an independent measurement of LiveCodeBench.
Establishes: That a widely cited launch report pairs a LiveCodeBench score with a
             date window and a shot count, so the score is meaningless stripped of
             them.
Paraphrase:  DeepSeek-V3 Technical Report (DeepSeek-AI, Dec 2024). In the base-
             model comparison table the coding row is labeled "LiveCodeBench-Base
             (0801-1101)" -- i.e. problems released 1 Aug to 1 Nov 2024 -- scored
             Pass@1, 3-shot. DeepSeek-V3 base: 19.4; DeepSeek-V2 base: 11.6;
             Qwen2.5 72B base: 12.9; LLaMA-3.1 405B base: 15.5. The window sits
             just after DeepSeek's own data collection, chosen so the problems
             post-date training. (I could not extract the chat/instruct table's
             LiveCodeBench figure; the HTML render truncated before it. The
             base-table figures above are what I verified.)
Locators:    Base-model evaluation table (Table 3 in the HTML render), coding row.
Quote:       "LiveCodeBench-Base (0801-1101)" with "DeepSeek-V3 ... 19.4"
             (Pass@1, 3-shot).
```

```text
URL:         https://qwenlm.github.io/blog/qwen2.5-coder-family/
Kind:        primary, for the claim that Qwen reported a LiveCodeBench figure on a
             window it chose. Alibaba's own launch post for its own models.
Establishes: A second vendor using a DIFFERENT window than DeepSeek, and stating
             plainly why -- direct proof that "the LiveCodeBench score" is really
             several different measurements sharing a name.
Paraphrase:  The Qwen2.5-Coder family post (released 12 Nov 2024) says its Instruct
             models were evaluated on LiveCodeBench questions from "2024.07 -
             2024.11," described as "the latest published questions that could not
             have leaked into the training set, reflecting the model's OOD
             capabilities." This window differs from DeepSeek's 0801-1101 window,
             though both claim contamination safety for their own model.
Locators:    Blog body, LiveCodeBench evaluation note.
Quote:       "2024.07 - 2024.11 ... the latest published questions that could not
             have leaked into the training set, reflecting the model's OOD
             capabilities."
```

```text
URL:         https://arxiv.org/abs/2107.03374
Kind:        primary. The paper that owns HumanEval; the source for what the older
             benchmark is and why it too tried to resist contamination.
Establishes: HumanEval's size and metric, and that its authors already knew
             training-set overlap was the threat -- so contamination is not a new
             worry LiveCodeBench invented, but one HumanEval addressed by hand-
             writing and LiveCodeBench addresses by dating.
Paraphrase:  "Evaluating Large Language Models Trained on Code" (Chen, Tworek, et
             al., 2021). HumanEval is "164 hand-written programming problems." The
             pass@k metric is the unbiased estimator 1 - C(n-c, k)/C(n, k) over n
             samples with c correct. The authors hand-wrote the problems precisely
             because of contamination risk.
Locators:    Abstract; Sec. 2 (HumanEval description and pass@k estimator).
Quote:       "It is important for these tasks to be hand-written, since our models
             are trained on a large fraction of GitHub, which already contains
             solutions to problems from a variety of sources."
```

```text
URL:         https://arxiv.org/abs/2502.17521
Kind:        secondary, and the one clearly independent source. A survey by
             authors unaffiliated with LiveCodeBench, classifying and critiquing
             contamination-resistant benchmarks from outside.
Establishes: That LiveCodeBench is a recognized instance of a general "temporal
             cutoff" strategy, and the documented limits of that strategy -- the
             evidence that most tests the commission's angle.
Paraphrase:  "Recent Advances in Large Language Model Benchmarks against Data
             Contamination: From Static to Dynamic Evaluation." Classifies
             LiveCodeBench under Dynamic Benchmarking -> Temporal Cutoff, alongside
             LiveBench, AntiLeak-Bench, AcademicEval, LiveAoPSBench, Forecastbench.
             States the limitations of the temporal-cutoff approach: it needs
             heavy ongoing human effort, and, critically, it "can still lead to
             data contamination, as these problems are likely to be reused in
             future competitions," and "verification is often overlooked in these
             live benchmarks."
Locators:    Sec. 4.4.1 "Temporal Cutoff" and its "Limitations" paragraph; Table 4
             (benchmark taxonomy).
Quote:       "Despite the popularity of temporal cutoffs, using recent information
             from competitions to evaluate LLMs can still lead to data
             contamination, as these problems are likely to be reused in future
             competitions."
```

```text
URL:         https://huggingface.co/blog/leaderboard-livecodebench
Kind:        primary. Co-authored by the LiveCodeBench team (Jain, Gu, Zhang, Li,
             Han, Yan) with Hugging Face (Clementine Fourrier); it is the authors
             explaining their own hosted leaderboard, not an independent review.
Establishes: The public "scrolling over time" leaderboard control that lets a
             reader re-score any model on any window -- the concrete tool that
             makes the date-window point actionable for the reader.
Paraphrase:  Describes the leaderboard's "scrolling over time" feature that "allows
             you to select problems within a specific time window," and restates
             the cutoff rule: "for new models with a training-cutoff date D, we can
             compute scores on problems released after D to measure their
             generalization on unseen problems." Does not give current counts or
             numeric scores in the portion read.
Locators:    Post body, "scrolling over time" and contamination sections.
Quote:       "for new models with a training-cutoff date D, we can compute scores
             on problems released after D to measure their generalization on
             unseen problems."
```

## Contradictions

The commission's angle -- the moving cutoff both fixes contamination and makes
two LiveCodeBench numbers hard to compare -- is supported, not contradicted. The
material that tests it is about how *clean* the fix is, and it should temper the
lesson rather than overturn it:

- **The moving cutoff is not a perfect decontaminant.** The independent survey
  (2502.17521, Sec. 4.4.1) states that temporal-cutoff benchmarks "can still lead
  to data contamination, as these problems are likely to be reused in future
  competitions," and that "verification is often overlooked in these live
  benchmarks." A window after a model's cutoff reduces contamination; it does not
  guarantee zero.

- **The cutoff itself is supplied by the model maker.** The paper (Sec. 3.1)
  normalizes the cutoff "to the release date if the training cutoff date is not
  published." The defense against contamination therefore rests on a date the
  vendor reports or that the authors guess -- the same party whose score is being
  protected. GPT-4-O's drop is measured against "its official cutoff date," a
  self-reported figure.

- **The contamination was platform-specific.** The paper (Sec. 5.1) finds the
  DeepSeek/GPT-4-O drop "primarily occurs for the LeetCode problems only," while
  AtCoder performance stayed "relatively smooth." So a window that is clean on one
  source platform need not be clean on another; the fix is uneven across the data.

- **The two vendor examples do not contradict each other, they illustrate the
  problem.** DeepSeek reports on 0801-1101 (Aug-Nov 2024); Qwen reports on
  2024.07-2024.11 (Jul-Nov 2024). Both call their window contamination-safe for
  their own model. The windows differ and the underlying dataset version differs,
  so the two "LiveCodeBench" numbers are not a like-for-like comparison -- exactly
  the commission's claim.

No source disputes the core facts of who built the benchmark, the platforms, the
scenarios, or the pass@1 definition.

## Numbers

```text
Figure: 511 problems (v2 release)
Owner:  LiveCodeBench paper (2403.07974), Table 1, "LCB (May-end)"
Scope:  All problems released May 2023 - May 2024, across the three platforms.
```

```text
Figure: platform split 267 / 235 / 9 (AtCoder / LeetCode / CodeForces)
Owner:  LiveCodeBench paper, Table 1
Scope:  Of the 511 v2 problems. Difficulty split: Easy 182, Medium 206, Hard 123.
        Average ~17 tests per problem.
```

```text
Figure: 349 problems
Owner:  LiveCodeBench paper, Table 1, "LCB (Sep-end)"
Scope:  Problems released Sep 2023 - May 2024. This is the contamination-safe
        subset the authors use for all model comparisons in Sec. 5.2, to exclude
        problems DeepSeek may have trained on.
```

```text
Figure: Pass@1 ~60 -> ~0
Owner:  LiveCodeBench paper, Sec. 5.1 (DS-Base-33B)
Scope:  Code generation on LeetCode problems, May 2023 problems vs September 2023
        problems. The collapse straddles DeepSeek's ~Sep 2023 release/cutoff.
```

```text
Figure: Codestral Pass@1 36.5 vs 28.3
Owner:  LiveCodeBench paper, Sec. 5.1
Scope:  36.5 on problems released May 2023 - Jan 2024; 28.3 on problems since Feb
        2024. Codestral released Feb 2024. Same model, two windows, ~8-point gap.
```

```text
Figure: DS-Ins-1.3B 59.8% vs 26.3%
Owner:  LiveCodeBench paper, Sec. 5.2 & Fig. 5
Scope:  59.8% Pass@1 on HumanEval+; 26.3% Pass@1 on LCB-Easy code generation.
        The worked case that a static HumanEval score misled about a small model.
```

```text
Figure: 4.3 points vs 16.2 points (69%)
Owner:  LiveCodeBench paper, Sec. 5.2
Scope:  DS-Ins-33B trails GPT-4-Turbo by 4.3 points on HumanEval+ but by 16.2
        points (69% relative) on LCB code generation (Sep 2023+ window). The gap
        HumanEval hid.
```

```text
Figure: correlation 0.72
Owner:  LiveCodeBench paper, Sec. 5.2
Scope:  Pearson-style correlation between models' HumanEval+ and LCB-Easy pass@1.
        "Only a moderate correlation," i.e. a HumanEval rank does not carry over.
```

```text
Figure: DeepSeek-V3 base 19.4 Pass@1
Owner:  DeepSeek-V3 Technical Report (2412.19437), base-model table
Scope:  LiveCodeBench-Base (0801-1101) = 1 Aug - 1 Nov 2024; 3-shot. Peers on the
        same row: DeepSeek-V2 11.6, Qwen2.5-72B base 12.9, LLaMA-3.1-405B base
        15.5. A score inseparable from its window, scenario, and shot count.
```

```text
Figure: dataset versions v1..v6 = 400, 511, 612, 713, 880, 1055 problems
Owner:  LiveCodeBench GitHub README
Scope:  v1 (to Mar 2024) 400; v2 (to May 2024) 511; v3 (to Jul 2024) 612; v4 (to
        Sep 2024) 713; v5 (to Jan 2025) 880; v6 (to Apr 2025) 1055. All start May
        2023. A "LiveCodeBench score" means nothing until the version is named.
```

```text
Figure: Qwen window 2024.07 - 2024.11
Owner:  Qwen2.5-Coder family blog
Scope:  The window Alibaba used to report its Instruct models' LiveCodeBench
        figures. Differs from DeepSeek's 0801-1101 window on the same benchmark.
```

## Source assets

```text
Asset: Figure 1, LiveCodeBench paper -- line charts of pass@1 by month for DeepSeek
       and GPT-4-O on LeetCode code generation and test output prediction, May
       2023 to Feb 2024, with each model's release/cutoff marked.
Shows: The contamination signal as a picture: performance is high on old months
       and falls off a cliff right at the model's cutoff. This is the single image
       that makes the whole lesson visible.
Crop:  Must keep the vertical drop and the cutoff marker aligned to a month on the
       x-axis. Do not crop away the axis labels or the release-date annotation;
       they are what make the drop mean "contamination" rather than "hard month."
```

```text
Asset: Figure 5, LiveCodeBench paper -- scatter plot, HumanEval+ pass@1 (x) vs
       LCB-Easy pass@1 (y), with a green cluster on the x=y line and a red cluster
       in the top-left (high HumanEval, low LiveCodeBench).
Shows: Overfitting to a static benchmark, as separation between two clouds of
       points. The red cluster is models a HumanEval number flattered.
Crop:  Must retain both clusters and the x=y reference line; the argument is the
       gap between the red cluster and that line. Omitting either cluster destroys
       the point.
```

```text
Asset: Table 1, LiveCodeBench paper -- problem counts by window, platform, and
       difficulty.
Shows: That the benchmark is a dated, sized collection, and that "Sep-end" (349)
       is a deliberate subset of "May-end" (511). Grounds the versioning point.
Crop:  If excerpted, keep the total-count column and the two window rows together;
       a single number lifted out reintroduces the very error the lesson warns
       against.
```

```text
Asset: LiveCodeBench GitHub README version list (v1..v6 with date ranges and
       counts).
Shows: Six things all called "LiveCodeBench," each a different window and size.
       The plainest evidence that a bare score is unanchored.
Crop:  Keep every version row with its date range and count intact; the list only
       argues when the reader sees the ranges change row to row.
```

```text
Asset: DeepSeek-V3 report base-model coding row -- header "LiveCodeBench-Base
       (0801-1101)" beside the Pass@1 3-shot column.
Shows: A real vendor score printed with its window and shot count attached, which
       is exactly how a careful figure should be reported.
Crop:  The header notation "(0801-1101)" and "3-shot" must stay attached to the
       number; the whole point is that they travel together.
```

## Discarded

```text
URL: https://benchlm.ai/benchmarks/liveCodeBench -- aggregator leaderboard with
     current-looking scores but no primary provenance for its numbers or window;
     not usable as a source that owns any claim.
URL: https://artificialanalysis.ai/evaluations/livecodebench -- third-party
     leaderboard; would be a candidate independent secondary for a live score, but
     I could not confirm its window/version labeling firsthand within scope, and
     the survey already serves the independent-secondary role. Not cited to avoid
     recording a figure I did not pin to a window.
URL: https://www.emergentmind.com/topics/livecodebench and .../humaneval-coding-benchmark
     -- machine-generated topic wikis; used only to orient, own no claim, not cited.
URL: https://www.codesota.com/benchmark/livecodebench -- marketing/aggregator page;
     no primary provenance; discarded.
URL: https://www.semanticscholar.org/paper/...afe0998d... -- index entry for the
     paper, not the paper; superseded by the arXiv page.
URL: https://arxiv.org/html/2412.19437v1 -- the chat/instruct evaluation table
     truncated in the HTML render, so DeepSeek-V3's chat-model LiveCodeBench figure
     is unresolved. The base-model figure (19.4, verified) is used instead. A
     writer wanting the chat number should pull it from the PDF's instruct table.
```
