# evidence: the-instruments/helm (01)

The sources establish HELM's construction firsthand and, from HELM's own team, the choice-dependence at the center of the commission. The 2022 paper defines the 30-model, 42-scenario, seven-metric design, the standardized 5-shot run, and the head-to-head "win rate" the leaderboard aggregates (Figure 26). Three primary documents, all authored by CRFM, then admit the aggregate rank depends on choices: the HELM Lite announcement says a mean win rate "cannot be interpreted in isolation and depends on the full set of models in the comparison set"; the HELM Capabilities announcement says CRFM dropped mean win rate because it is "dependent on the set of models being compared" and "sensitive to small variations in scenario scores that invert ranks"; an independent analysis (Perlitz et al.) finds a HELM "leader may change by merely removing a low-ranked model." The angle is well supported, with one important correction: reweighting or dropping the robustness and fairness axes specifically does NOT reorder models much, because the paper finds accuracy, robustness, and fairness "extremely strongly correlated." The axes that do change the order are toxicity, bias, calibration, and efficiency — the ones HELM's aggregate underweights, omits, or that HELM Lite later dropped. The writer should build the choice-dependence on those axes, on scenario/model-set selection, and on HELM's own two changes of method, not on "drop robustness and the ranking scrambles."

## Sources

```text
URL:         https://arxiv.org/abs/2211.09110
Kind:        primary. The HELM paper itself (Liang et al.), published in TMLR 08/2023; it owns the benchmark's design and every reported result. Read into methods (§4 metrics, §7-8 adaptation) and results (§8, Figs 24-26).
Establishes: HELM evaluates 30 language models on all 42 scenarios; the 7 metrics and their definitions; the 5-shot standardized run; the per-metric head-to-head win rate (Fig 26); and the authors' explicit refusal to reduce a model to one number.
Paraphrase:  "We measure 7 metrics (accuracy, calibration, robustness, fairness, bias, toxicity, and efficiency) for each of 16 core scenarios when possible (87.5% of the time)." The benchmark spans 42 scenarios (16 core + 26 targeted). Models are adapted by 5-shot prompting with the in-context examples fixed across evaluation instances, re-run 3 times varying only which examples are sampled. Figure 26 reports "the fraction of head-to-head comparisons between the given model and all other models, across all scenarios, where the given model is higher along the metric"; efficiency is excluded from these comparisons. The paper assigns "a score matrix to each model" rather than a single score, and leaves aggregation to a single number "to future work," holding that "we do not believe there exists a universal aggregation that satisfies all preferences."
Locators:    Abstract; §1.1 (design principles, findings 1-12); §4.3-4.9 (metric definitions); §7-8.1 (5-shot adaptation, in-context examples); Fig 24-26 captions (pp. 48-51 of the TMLR PDF); §9/§10 aggregation stance (paragraph beginning "We leave the question of aggregating model performance to a single number").
Quote:       "We leave the question of aggregating model performance to a single number (or a single number per scenario, or per metric) to future work. We do not believe there exists a universal aggregation that satisfies all preferences, reflects all values, or captures all circumstances appropriately. However, we do believe single-number metrics, though reductive, are useful practical tools to simplify decision-making."
```

```text
URL:         https://crfm.stanford.edu/2023/12/19/helm-lite.html
Kind:        primary. CRFM's own announcement of HELM Lite; it owns the Lite ranking method and its definition of mean win rate.
Establishes: The exact definition of mean win rate as used on the leaderboard, its stated disadvantage (model-set dependence), and that HELM Lite dropped most of the seven metrics.
Paraphrase:  Averaging different scenario metrics is called "dubious semantically," so CRFM reports mean win rate instead: the fraction of times a model scores better than another model, averaged across scenarios. It works across metrics of different scales but "cannot be interpreted in isolation and depends on the full set of models in the comparison set." HELM Lite lists nine named scenarios (NarrativeQA, NaturalQuestions in open- and closed-book versions, OpenbookQA, MMLU, MATH, GSM8K, LegalBench, MedQA, WMT14), which CRFM's changelog counts as 10 scenarios by scoring NaturalQuestions' two versions separately; it uses 1 random seed instead of 3 and drops perturbations (robustness/fairness), calibration, and perplexity; it "focuses only on capabilities."
Locators:    Sections "HELM Lite v1.0.0" (structural simplifications), the scenario list, and the paragraph defining mean win rate.
Quote:       "Instead, we decide to report the mean win rate, which is the fraction of times a model obtains a better score than another model, averaged across scenarios. Mean win rate is semantically meaningful even if different scenario metrics have different scales or units, but has the disadvantage that a mean win rate cannot be interpreted in isolation and depends on the full set of models in the comparison set."
```

```text
URL:         https://crfm.stanford.edu/2025/03/20/helm-capabilities.html
Kind:        primary. CRFM's HELM Capabilities announcement; it owns the decision to abandon mean win rate.
Establishes: HELM Classic and HELM Lite ranked by mean win rate; CRFM later replaced it with a mean score because mean win rate is choice-dependent and rank-unstable.
Paraphrase:  The Capabilities leaderboard ranks models by a mean score that averages metrics across scenarios (with the WildBench 1-10 score rescaled to 0-1). This differs from HELM Classic and HELM Lite, which used mean win rate as the top-level aggregate. The change is because mean win rate is (1) dependent on the set of models being compared and (2) sensitive to small variations in scenario scores that invert ranks.
Locators:    Section "Top-level Aggregation."
Quote:       "The models are ranked based on the mean score, which aggregates metrics across scenarios with the WB score (1-10) rescaled to 0-1. Note that this is different from our previous approach in HELM Classic and HELM Lite, which is to use the mean win rate as the top-level aggregate score. This change is motivated by the fact that the mean win rate is 1) dependent on the set of models being compared, and 2) sensitive to small variations in scenario scores that invert ranks."
```

```text
URL:         https://crfm.stanford.edu/helm/
Kind:        primary. The live HELM leaderboard hub (CRFM); it owns the current set of published leaderboards and their headline columns. Page is JavaScript-rendered.
Establishes: HELM now hosts many separate leaderboards, each with its own ranking column: HELM Capabilities, HELM Lite, HELM Classic, HELM Safety, plus domain and modality variants (MedHELM, VHELM, HEIM, ToRR, Audio). The "one HELM number" a reader might quote is actually one of several, computed differently per board.
Paraphrase:  Distinct leaderboards live at /helm/capabilities/latest/, /helm/lite/latest/, /helm/classic/latest/, /helm/safety/latest/, and others, each reachable from this hub.
Locators:    Leaderboard navigation on the hub page; individual boards at the paths above.
Quote:       (none; rendered client-side)
```

```text
URL:         https://crfm-helm.readthedocs.io/en/latest/  (rank walk-through: https://github.com/stanford-crfm/helm/blob/v0.5.0/docs/get_helm_rank.md)
Kind:        primary. The HELM framework's own documentation (CRFM).
Establishes: How a model is placed on the leaderboard in practice, and that ranking is reproducible from released run stats; it also surfaces the framework's own pointer to Efficient-HELM.
Paraphrase:  "Get Your Model's Leaderboard Rank" instructs a user to download all prior HELM run stats and run their model through the same scenarios to obtain a comparable rank. It cites Perlitz et al. (Efficient Benchmarking) to note that running a fraction of examples per scenario still recovers the rank within a stated confidence interval (e.g. 10 examples/scenario gives a 95% CI of rank location of about +/-5 positions).
Locators:    docs/get_helm_rank.md, sections "Download HELM leaderboard results" and "Run Efficient-HELM" (table of examples-per-scenario vs. CI of rank location).
Quote:       (table) "10 examples per scenario -> CI 95% of Rank Location +/-5 -> compute saved x400."
```

```text
URL:         https://github.com/stanford-crfm/helm/blob/main/CHANGELOG.md
Kind:        primary. The HELM framework's own changelog (CRFM); it owns the release facts and dates.
Establishes: HELM Lite launched with 30 models and 10 scenarios; the mean win rate computation was later corrected; and the rank tutorial adopts the Efficient Benchmarking method.
Paraphrase:  The HELM Lite v1.0.0 entry records "Launched new HELM Lite leaderboard with 30 models and 10 scenarios." A later entry records "Fix incorrect handling of ties in win rate computation," i.e. the win rate number itself changed when the tie rule was fixed. Another entry adds a tutorial for computing a model's leaderboard rank using the method from Perlitz et al. (Efficient Benchmarking).
Locators:    HELM Lite v1.0.0 release entry; entry "Fix incorrect handling of ties in win rate computation (#3001, #2008)"; entry adding the rank tutorial (#1968, #1986, #1985).
Quote:       "Launched new HELM Lite leaderboard with 30 models and 10 scenarios." / "Fix incorrect handling of ties in win rate computation"
```

```text
URL:         https://arxiv.org/abs/2308.11696
Kind:        secondary (relative to HELM). Independent analysis of HELM by an IBM Research team (Perlitz, Bandel, Gera, Arviv, Ein-Dor, Shnarch, Slonim, Shmueli-Scheuer, Choshen), EMNLP 2023 Findings. Primary for its own DIoR measure, but here it reports on HELM from outside CRFM.
Establishes: Independent confirmation that HELM's ranking is fragile to benchmark-design choices, corroborating CRFM's own model-set-dependence admission.
Paraphrase:  Using HELM as the test case, the authors study the computation-reliability trade-off of benchmark design choices and introduce Decision Impact on Reliability (DIoR). They find that "a benchmark leader may change by merely removing a low-ranked model from the benchmark," and that a correct ranking can be recovered from a fraction of the evaluation examples.
Locators:    Abstract; the paper's "Benchmark Agreement Testing" and DIoR sections.
Quote:       "We find, for example, that a benchmark leader may change by merely removing a low-ranked model from the benchmark, and observe that a correct benchmark ranking can be obtained by considering only a fraction of the evaluation examples."
```

```text
URL:         https://crfm.stanford.edu/helm/classic/latest/
Kind:        primary. The live HELM Classic leaderboard (CRFM), the board that presents the original 2022 evaluation. JavaScript-rendered.
Establishes: That the multi-metric HELM Classic results are still published as a leaderboard headed by a mean win rate column (per the Capabilities announcement's description of Classic), the concrete object a "#1 on HELM" claim points at.
Paraphrase:  HELM Classic exposes per-scenario, per-metric results and orders models by a mean win rate across core scenarios; the underlying score matrix is browsable behind that headline number.
Locators:    "Core scenarios" group view; leaderboard column headed mean win rate.
Quote:       (none; rendered client-side; ranking method quoted from the Capabilities announcement above)
```

## Contradictions

- Against the loosest reading of the angle ("reweight or drop any axis and the order changes"): the paper finds accuracy, robustness, and fairness "extremely strong[ly] correlated" across all scenarios (Figure 25). CRFM acted on exactly this when building HELM Lite, dropping robustness and fairness perturbations "since robustness and fairness metrics ... were well correlated with accuracy (Figure 24 of the HELM Classic paper)." So dropping or down-weighting robustness/fairness barely reorders models. The axes that reorder are toxicity and bias (near-zero or divergent correlation with accuracy), calibration (scenario-dependent), and efficiency (excluded from the win rate entirely). The commission's example should name these axes, not robustness.
- The paper cautions this correlation is "a finding contingent on how we chose to measure robustness/fairness" (worst-case over mild perturbations), so the correlation is itself a choice, not a law. This limits how far the counterpoint above can be pushed.
- CRFM's stance is not that ranking is meaningless: the paper calls single-number metrics "reductive" yet "useful practical tools to simplify decision-making." The piece should not read HELM as disowning its own leaderboard; HELM built the leaderboard and defends it as a practical tool while warning against over-reading it.
- Direction-of-metric care: for calibration and efficiency, lower is better (ECE-10; inference time); for accuracy, robustness, fairness, higher is better. A win-rate "high" on calibration means low error. Do not describe a model as "winning on calibration" without stating the direction.

## Numbers

```text
Figure: 30 language models
Owner:  HELM paper (Liang et al. 2022 / TMLR 2023), abstract and §1.1
Scope:  all evaluated on all 42 scenarios; "prominent" open, limited-access, and closed models as of mid/late 2022
```

```text
Figure: 42 scenarios = 16 core + 26 targeted
Owner:  HELM paper, abstract and §1.1
Scope:  the 7 metrics are measured on the 16 core scenarios "when possible (87.5% of the time)"; the 26 targeted scenarios drive component evaluations (language, knowledge, reasoning, memorization, disinformation, bias, toxicity)
```

```text
Figure: 7 metrics (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency)
Owner:  HELM paper, §4.3-4.9
Scope:  per (model, scenario) cell of the score matrix; not all metrics apply to every scenario (e.g. toxicity/bias only where the model generates free text)
```

```text
Figure: 5 in-context examples (5-shot), fixed across instances, 3 random seeds
Owner:  HELM paper, §7-8.1 ("In-context examples")
Scope:  the single standardized adaptation used for the main comparison; HELM Lite later cut this to 1 seed
```

```text
Figure: text-davinci-002 wins its accuracy head-to-head comparisons more than 90% of the time
Owner:  HELM paper, §8 (Figure 26, accuracy subfigure)
Scope:  fraction of pairwise accuracy comparisons vs. all other models across the core scenarios; efficiency excluded from head-to-head
```

```text
Figure: TNLG v2 (530B) accuracy on NarrativeQA drops from 72.6% to 38.9% under robustness perturbations
Owner:  HELM paper, §1.1 finding 4
Scope:  standard vs. perturbed (typo-style) accuracy on one scenario; TNLG v2 is the third-most-accurate model on standard NarrativeQA
```

```text
Figure: accuracy-calibration relationship reverses across scenarios: OpenBookQA accuracy-calibration correlation > 0.8 (aligned); HellaSwag accuracy-calibration-error correlation > 0.85 (improving accuracy worsens calibration)
Owner:  HELM paper, §8 (discussion of Figures 24-25) and §1.1 finding 3
Scope:  across the 30 models, per scenario; two commonsense-QA scenarios that behave oppositely
```

```text
Figure: HELM Lite v1.0.0 = 30 models and 10 scenarios (nine named, NaturalQuestions scored in two versions), 1 random seed, ranked by mean win rate; robustness, fairness, calibration, and perplexity dropped
Owner:  CRFM, HELM Lite announcement (2023-12-19) and HELM CHANGELOG (v1.0.0 entry)
Scope:  the "capabilities-only" successor board; safety split into a separate benchmark
```

```text
Figure: rank recoverable to CI 95% of +/-5 positions using 10 examples per scenario (x400 compute saved)
Owner:  Perlitz et al. 2023 (Efficient Benchmarking), as reported in HELM's get_helm_rank doc
Scope:  HELM ranking as a function of examples per scenario; a measure of how much the rank is an artifact of sampling
```

## Limits

- The exact set of metrics feeding the HELM Classic leaderboard's headline mean win rate (accuracy only, or accuracy plus the other applicable metrics, across the core scenarios) is stated in the paper as a per-metric head-to-head (Figure 26 gives six separate rankings) and described by CRFM as a single "mean win rate as the top-level aggregate," but the two live boards (/helm/classic/, /helm/lite/) are JavaScript-rendered and I could not read the current column definition off the page itself. The writer should treat "the leaderboard's mean win rate" as the across-scenarios definition CRFM gives in the Lite announcement, and avoid asserting precisely which metrics enter the Classic headline column beyond what Figure 26 and the two announcements support.
- I did not obtain a live, dated snapshot of a specific "#1 on HELM" ordering from the rendered leaderboard (client-side rendering). The concrete reorder-under-different-choices case is therefore built from the paper's own Figure 26 (accuracy vs. toxicity/bias orderings) and from CRFM's and Perlitz's stated model-set sensitivity, not from a captured before/after leaderboard table. If the writer wants a named pair of models that swap under a metric change, Figure 26 supports it (e.g. T0pp (11B) is most toxic but among the least gender-biased; davinci (175B) among the most biased but among the less toxic), but the precise current-leaderboard swap is not captured.
- Everything the commission asked to define (model count, scenario count, the seven metric definitions, the 5-shot run, and mean win rate) is established firsthand and quoted.

## Source assets

```text
Asset: Figure 26, "Head-to-head win rate per each model" (HELM paper, ~p. 51 of the TMLR PDF; also live per-metric on the HELM Classic board).
Shows: Six side-by-side rankings of the same 30 models, one per metric (accuracy, calibration error, robustness, fairness, bias, toxicity). Accuracy, robustness, and fairness produce near-identical orders; toxicity and bias produce visibly different orders. This is the single clearest picture that the same models reorder when you change which axis you rank on.
Crop:  Keep at least the accuracy column beside the toxicity (or bias) column so the reader sees the same names in different positions. Retain the model labels and the 0.0-1.0 scale. Do not crop to a single column; the comparison is the point.
```

```text
Asset: Figure 24, "Accuracy vs. X" (HELM paper, ~p. 48), the six-panel scatter of accuracy against each other metric across all core scenarios and models.
Shows: Accuracy vs. robustness/fairness lie near a line (they track accuracy); accuracy vs. toxicity/bias/calibration scatter widely and vary by scenario. It is the evidence for the honest, narrower version of the angle.
Crop:  Preserve panel labels and axis labels; a two-panel crop (accuracy-vs-robustness beside accuracy-vs-toxicity) carries the contrast if the full six-panel is too dense.
```

```text
Asset: The HELM Capabilities "Top-level Aggregation" paragraph (https://crfm.stanford.edu/2025/03/20/helm-capabilities.html).
Shows: In CRFM's own words, that they abandoned mean win rate because it depends on the comparison set and small score changes invert ranks. Better as a pull-quote than a picture.
Crop:  (text) quote the two numbered reasons intact.
```

```text
Asset: The live HELM leaderboard hub/heatmap (https://crfm.stanford.edu/helm/classic/latest/), the browsable score matrix behind the headline number.
Shows: That "one HELM number" sits on top of a full grid of per-scenario, per-metric cells. Useful as a screenshot to make the "matrix reduced to a rank" concrete. Rendered client-side, so a capture would need a browser.
Crop:  Keep the mean win rate column adjacent to two or three per-metric columns so the reduction is visible.
```

## Discarded

```text
URL: https://ar5iv.labs.arxiv.org/html/2211.09110 — HTML mirror of the paper, truncated mid-Section 3; used only to confirm structure, superseded by the full PDF at arxiv.org/abs/2211.09110.
URL: https://prajnaaiwisdom.medium.com/...helm... — third-party Medium explainer; secondhand, no primary figure, not needed for context.
URL: https://ai-tldr.dev/learn/.../what-is-stanford-helm/ — SEO explainer; restates HELM's own framing without independent reporting.
URL: https://arxiv.org/pdf/2605.23628 ("How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness") — surfaced in search and directly on-topic (reweighting reorders leaderboards), but I did not open and verify it; its metadata looked off and the angle is already carried by CRFM's own admissions and Perlitz et al. Left out rather than cited unverified.
```
