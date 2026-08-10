# Evidence: the-instruments/alpacaeval (researcher/01)

The record supports the commission's angle directly. The construction of the win
rate is documented by the benchmark's own repository: a judge language model
compares a candidate's answers to a reference model's answers on 805 fixed
instructions and reports the fraction it prefers, a preference share and not an
accuracy. The length bias is measured firsthand by Dubois et al. (2024): the same
model's AlpacaEval 2.0 win rate moves from 22.9% to 64.3% purely by instructing it
to be more or less verbose, and length control cuts that swing to 41.9%–51.6% while
raising the metric's Spearman correlation with LMSYS Chatbot Arena from 0.94 to
0.98. The "how it is cited" claim is grounded in a real model report, the Zephyr
paper, which leads with an AlpacaEval win rate of 90.60% under version 1.0 against
text-davinci-003, a number that becomes 13.20% length-controlled against gpt4_turbo
on the version 2.0 leaderboard for the same model. That single model, read two
ways, carries the "comparable only under matched settings" point without argument.

The record is thin in one place worth flagging up front: the two primaries that
own the correlation figure disagree by a hundredth. The Dubois paper says the
uncontrolled correlation is 0.94; the tatsu-lab repository README says 0.93. Both
agree the controlled figure is 0.98. See Contradictions. A second soft spot: the
judge's agreement rate with human annotators is stated in the README's evaluators
table, but two automated reads of that table returned 68.1% and 69.2%, so I did not
pin the exact digit. The commission does not depend on it; the writer should reopen
the table before citing a precise value.

## Sources

```text
URL:         https://github.com/tatsu-lab/alpaca_eval/blob/main/README.md
Kind:        primary. The authoring repository of the AlpacaEval benchmark
             (tatsu-lab). It owns the definition of the metric and the identities
             of the default judge and reference models.
Establishes: How the win rate is computed and what it is. The metric is the
             fraction of the 805 instructions on which the automatic judge
             prefers the evaluated model's output over a reference model's
             output. It is a preference share, not a measure of correctness.
             Default judge/reference pairs: AlpacaEval 1.0 uses the annotator
             alpaca_eval_gpt4 with baseline text_davinci_003; AlpacaEval 2.0 uses
             the annotator weighted_alpaca_eval_gpt4_turbo with baseline
             gpt4_turbo. Length-controlled (LC) win rate is a debiased version
             that controls for output length.
Paraphrase:  The win rate measures the fraction of time the model's output is
             preferred over the reference's outputs (text-davinci-003 for
             AlpacaEval and gpt4_turbo for AlpacaEval 2.0). The evaluation set is
             the 805 examples from AlpacaEval. To compute the win rate the tool
             collects paired outputs and asks the automatic evaluator which it
             prefers. Length-controlled win rates are a debiased version of the
             win rates that control for the length of the outputs, and the README
             states they raise the correlation between AlpacaEval's leaderboard
             and Chatbot Arena from 0.93 to 0.98 Spearman.
Locators:    README sections on the metric, the evaluators, and length control.
Quote:       "the win rate measures the fraction of time the model's output is
             preferred over the reference's outputs"
```

```text
URL:         https://github.com/tatsu-lab/alpaca_eval/blob/main/src/alpaca_eval/leaderboards/data_AlpacaEval_2/weighted_alpaca_eval_gpt4_turbo_leaderboard.csv
Kind:        primary. The official AlpacaEval 2.0 leaderboard data file in the
             benchmark's own repository. It owns the published version 2.0 numbers
             for each model.
Establishes: The version-2.0 reading for zephyr-7b-beta, judged by
             weighted_alpaca_eval_gpt4_turbo against the gpt4_turbo baseline. This
             is the counterpart to the version-1.0 number the Zephyr paper reports.
Paraphrase:  For zephyr-7b-beta the file records a raw win rate of 10.99%, a
             length-controlled win rate of 13.20%, and an average output length of
             1,444. Columns include win_rate, avg_length, and
             length_controlled_winrate.
Locators:    Row for zephyr-7b-beta; header row names the columns.
Quote:       header: "win_rate,standard_error,n_wins,n_wins_base,n_draws,n_total,
             discrete_win_rate,mode,avg_length,length_controlled_winrate,
             lc_standard_error"
```

```text
URL:         https://arxiv.org/abs/2404.04475
Kind:        primary. Length-Controlled AlpacaEval (Dubois, Galambosi, Liang,
             Hashimoto), COLM 2024. It owns the measured length bias, the
             correction, and the correlation figures. Verified against the paper
             PDF, not coverage.
Establishes: The size of the length bias and the correction's effect. On
             AlpacaEval 2.0 the baseline model gpt4_1106_preview's own win rate
             swings from 22.9% to 64.3% purely by changing a verbosity
             instruction, which shows a model can move its number by verbosity
             alone. Length control shrinks that swing to 41.9%-51.6%. The
             normalized standard deviation across the three verbosity prompts
             falls from 25% to 10%. Length control raises the Spearman correlation
             with LMSYS Chatbot Arena from 0.94 to 0.98. The benchmark operates on
             a fixed set of 805 instructions; the current baseline and evaluator
             are both GPT-4 turbo (AlpacaEval 2.0).
Paraphrase:  The paper reports that varying the verbosity instruction in the
             prompt moves gpt4_1106_preview from 22.9% to 64.3%, and that after
             length control its win rates fluctuate only from 41.9% to 51.6%, with
             the normalized standard deviation across the three verbosity prompts
             dropping from 25% to 10%. It states that controlling for length
             increased the Spearman correlation with Chatbot Arena from 0.94 to
             0.98. It describes AlpacaEval as operating on a fixed set of 805
             instructions, with a GPT-4 turbo baseline and a GPT-4 turbo-based
             evaluator. The method fits a logistic/generalized linear regression
             predicting the annotator's preference from the model identity, the
             instruction, and the length difference, then reads off the preference
             at zero length difference.
Locators:    Abstract; Section 2 (background, 805 instructions, GPT-4 turbo
             baseline and evaluator); Section 4.1 (verbosity manipulation, 25% to
             10%); Section 4.2 (0.94 to 0.98); summary table on the results page
             (rows Win rate / Length-controlled / Length-normalized).
Quote:       "(gpt4_1106_preview) fluctuates from 22.9% to 64.3% by varying the
             verbosity instruction"
             "the normalized standard deviation across the three verbosity prompts
             decreases from 25% to 10% from the length control"
             "controlling for length increased the Spearman correlation with Chat
             Arena from 0.94 to 0.98"
```

```text
URL:         https://arxiv.org/abs/2403.04132
Kind:        primary. Chatbot Arena (Chiang, Zheng, Sheng, Angelopoulos, T. Li,
             D. Li, Zhang, Zhu, Jordan, Gonzalez, Stoica), 2024. It owns the
             human-preference ranking that the Dubois correlation is measured
             against.
Establishes: The reference the correlation validates against. Chatbot Arena ranks
             models from crowdsourced pairwise human votes using Bradley-Terry
             coefficients estimated by maximum likelihood, not raw Elo. As of the
             paper it had collected roughly 240K votes from over 90K users across
             more than 50 models.
Paraphrase:  The platform ranks models with the vector of Bradley-Terry
             coefficients estimated from pairwise human votes, and reports around
             240K votes from over 90K users over more than 50 models including
             GPT-4, Claude, Gemini, LLaMA, and Mistral. It notes the crowdsourced
             votes agree well with expert raters.
Locators:    Abstract; methodology section introducing Bradley-Terry coefficients;
             data-scale statement.
Quote:       "A standard score function in this setting is the vector of
             Bradley-Terry (BT) coefficients (Bradley & Terry, 1952)."
             "we have received around 240K votes from over 90K users"
```

```text
URL:         https://arxiv.org/abs/2310.16944
Kind:        primary. Zephyr: Direct Distillation of LM Alignment (Tunstall et
             al., 2023). A model report that quotes an AlpacaEval win rate as a
             headline result. Figures verified against the paper PDF (Table 1),
             which corrected an earlier misread.
Establishes: How the number is cited in practice, and under which settings.
             Zephyr-7B is reported at an AlpacaEval win rate of 90.60% (with a
             1.03 standard error) against the text-davinci-003 baseline. This is
             AlpacaEval 1.0: the paper states the metric is the pairwise win rate
             against text-davinci-003, scored by GPT-4, over 805 questions. The
             paper's own limitations name a judge failure mode: the GPT-4
             evaluator is biased toward models distilled from it and toward
             verbose but potentially incorrect responses.
Paraphrase:  Table 1 lists Zephyr 7B (dDPO) with an AlpacaEval win rate of 90.60
             and standard error 1.03. The evaluation section defines AlpacaEval as
             a single-turn benchmark of 805 questions where models are scored by
             GPT-4 and the final metric is the pairwise win rate against a baseline
             model, text-davinci-003. The conclusions section names the main
             limitation as the use of GPT-4 as the evaluator, which is known to be
             biased toward models distilled from it or toward verbose but
             potentially incorrect responses.
Locators:    Section 4.2 (AlpacaEval definition, 805 questions, text-davinci-003
             baseline); Table 1 (Zephyr 7B, 90.60 with 1.03 s.e.); Section 6
             (limitation on GPT-4 evaluator bias).
Quote:       "the final metric is the pairwise win-rate against a baseline model
             (text-davinci-003)"
             "the use of GPT-4 as an evaluator for the AlpacaEval and MT-Bench
             benchmarks, which is known to be biased towards models distilled from
             it, or those that produce verbose, but potentially incorrect
             responses"
             Table 1 row: "Zephyr 7B dDPO 7.34 90.60 1.03"
```

```text
URL:         https://huggingface.co/HuggingFaceH4/zephyr-7b-beta
Kind:        primary. The Zephyr-7B-beta model card, authored by the model's team
             (HuggingFaceH4). A model report in the form a reader is most likely to
             meet.
Establishes: That the model card, like the paper, cites the AlpacaEval 1.0 win
             rate of 90.60% and does not itself state a version-2.0 or
             length-controlled number. This matters for the version point: the
             card and the paper agree at 90.60% under 1.0, while the same model
             sits at 13.20% LC on the 2.0 leaderboard.
Paraphrase:  The card's performance table shows AlpacaEval (win rate %): 90.60. It
             does not mention AlpacaEval 2.0, length-controlled win rates, or the
             gpt4_turbo baseline.
Locators:    Performance/results table on the card.
Quote:       "AlpacaEval (win rate %): 90.60"
```

```text
URL:         https://arxiv.org/abs/2410.07137
Kind:        primary. Cheating Automatic LLM Benchmarks: Null Models Achieve High
             Win Rates (Zheng, Pang, Du, Liu, Jiang, Lin), 2024. It owns the
             null-model result. Included as a second documented failure mode of the
             automatic judge.
Establishes: That the automatic judge can be gamed by outputs that ignore the
             instruction, and that length control does not defend against this. A
             fixed, instruction-irrelevant "null" response reaches a raw win rate
             of 76.9% and a length-controlled win rate of 86.5% on AlpacaEval 2.0.
             The LC figure being higher than the raw figure shows length control is
             itself exploitable here.
Paraphrase:  The authors report that a null model outputting a single constant,
             instruction-irrelevant response achieves an 86.5% length-controlled
             win rate and a 76.9% raw win rate on AlpacaEval 2.0, and note that the
             LC win rates of their cheats are generally higher than the raw win
             rates because of their short length, so AlpacaEval 2.0 is not robust
             to a length cheat.
Locators:    Abstract and main results for AlpacaEval 2.0.
Quote:       "the LC win rates of our cheats are generally higher than the raw win
             rates because of their short length, which highlights that AlpacaEval
             2.0 is also not robust to length cheat"
```

```text
URL:         https://www.themoonlight.io/en/review/length-controlled-alpacaeval-a-simple-way-to-debias-automatic-evaluators
Kind:        secondary. A third-party summary site (Moonlight) reviewing the Dubois
             paper. It authored a summary, not the research. Used only as context
             for how the correlation figure is retold.
Establishes: That an independent retelling reports the correlation as 0.94 to
             0.98, matching the paper and not the repository README's 0.93. A
             repetition supports that the claim was made, not that it is true; the
             owning primary is the Dubois paper.
Paraphrase:  The review states that AlpacaEval-LC achieved a higher Spearman
             correlation (0.98) with Chatbot Arena than the original AlpacaEval
             (0.94).
Locators:    Review body, correlation summary.
Quote:       "AlpacaEval-LC achieved a higher Spearman correlation (0.98) with
             LMSYS's Chatbot Arena ... than the original AlpacaEval (0.94)"
```

## Contradictions

- Uncontrolled correlation, 0.94 versus 0.93. The Dubois paper states the
  uncontrolled AlpacaEval 2.0 win rate correlates with Chatbot Arena at 0.94
  (abstract, Section 4.2, and the paper's summary table). The tatsu-lab README, by
  the same group, states the improvement runs "from 0.93 to 0.98." Both agree the
  controlled figure is 0.98. The gap is a hundredth and both are primaries. The
  secondary review sides with the paper's 0.94. The paper is the document that
  performed and reports the regression, so it owns the figure; the writer should
  cite 0.94 to 0.98 and can note the README's 0.93 as the repository's rounding.

- Gameability figure, 25% versus 26%. Within the Dubois paper, the Section 4.1
  prose says the normalized standard deviation across the three verbosity prompts
  falls "from 25% to 10%," while the summary table lists the raw win rate's
  gameability at 26% (and length-controlled at 10%). This is a rounding difference
  inside one source. Cite "about a quarter, cut to a tenth" rather than a false
  precision, or cite the table's 26% to 10% explicitly.

- Same model, opposite-looking numbers. This is not a source error but the
  commission's whole point, recorded so the writer treats it as intended. Zephyr-7B
  reads 90.60% (AlpacaEval 1.0, GPT-4 judge, text-davinci-003 baseline, per its own
  paper) and 13.20% length-controlled / 10.99% raw (AlpacaEval 2.0,
  weighted_alpaca_eval_gpt4_turbo judge, gpt4_turbo baseline, per the leaderboard).
  Nothing about the model changed between the two readings; the reference model,
  the judge, and the length handling did. The high 1.0 number reflects a weak
  reference (text-davinci-003); the low 2.0 number reflects a strong reference
  (GPT-4 turbo).

- Judge-human agreement, unpinned. The README's evaluators table reports how often
  the default annotator agrees with human labels, but two automated reads returned
  68.1% and 69.2%. I could not confirm the exact digit and did not use it as a
  load-bearing figure. Not a disagreement between sources, a limit of my read.

## Numbers

```text
Figure: 805 instructions in the evaluation set
Owner:  AlpacaEval repository (tatsu-lab); also stated in Dubois et al. 2024
Scope:  The fixed instruction set, shared by AlpacaEval 1.0 and 2.0
```

```text
Figure: Win rate = fraction of 805 instructions on which the judge prefers the
        model's output over the reference's; a preference share, not an accuracy
Owner:  AlpacaEval repository (tatsu-lab)
Scope:  Per model, against one named reference under one named judge
```

```text
Figure: AlpacaEval 1.0 judge = alpaca_eval_gpt4; reference = text_davinci_003
Owner:  AlpacaEval repository (tatsu-lab)
Scope:  Default setting for version 1.0
```

```text
Figure: AlpacaEval 2.0 judge = weighted_alpaca_eval_gpt4_turbo;
        reference = gpt4_turbo (gpt4_1106_preview)
Owner:  AlpacaEval repository (tatsu-lab); Dubois et al. 2024
Scope:  Default setting for version 2.0
```

```text
Figure: Baseline gpt4_1106_preview raw win rate swings 22.9% to 64.3%
Owner:  Dubois et al. 2024, Section 4.1
Scope:  AlpacaEval 2.0; same model, three verbosity instructions
        (concise / standard / verbose)
```

```text
Figure: After length control the same swing is 41.9% to 51.6%
Owner:  Dubois et al. 2024, Section 4.1
Scope:  AlpacaEval 2.0; same three verbosity instructions
```

```text
Figure: Normalized standard deviation across the three verbosity prompts
        falls from 25% to 10% (prose); table lists 26% raw, 10% controlled
Owner:  Dubois et al. 2024, Section 4.1 and summary table
Scope:  AlpacaEval 2.0 gameability measure
```

```text
Figure: Spearman correlation with Chatbot Arena: 0.94 uncontrolled, 0.98 controlled
Owner:  Dubois et al. 2024 (abstract, Section 4.2). README states 0.93 to 0.98.
Scope:  AlpacaEval 2.0 leaderboard versus LMSYS Chatbot Arena rankings
```

```text
Figure: Null model on AlpacaEval 2.0: 86.5% length-controlled, 76.9% raw
Owner:  Zheng et al. 2024 (Cheating Automatic LLM Benchmarks)
Scope:  A single constant, instruction-irrelevant response; AlpacaEval 2.0
```

```text
Figure: Zephyr-7B AlpacaEval win rate 90.60% (standard error 1.03)
Owner:  Tunstall et al. 2023, Table 1; Zephyr-7B-beta model card
Scope:  AlpacaEval 1.0, GPT-4 judge, text-davinci-003 baseline, 805 questions
```

```text
Figure: zephyr-7b-beta AlpacaEval 2.0: 13.20% LC, 10.99% raw, avg length 1,444
Owner:  AlpacaEval 2.0 leaderboard (tatsu-lab)
Scope:  weighted_alpaca_eval_gpt4_turbo judge, gpt4_turbo baseline
```

```text
Figure: Chatbot Arena scale: ~240K votes, >90K users, >50 models; Bradley-Terry
        coefficients
Owner:  Chiang et al. 2024
Scope:  As of the paper; the human-preference reference for the correlation
```

## Source assets

```text
Asset: Dubois et al. 2024, Figure 1 (scatter of AlpacaEval win rate against
       Chatbot Arena rank, plotted for the raw and the length-controlled metric)
Shows: The correlation improving from 0.94 to 0.98 as points tighten toward the
       trend line after length control. It makes "raising correlation to near one"
       something a reader can see rather than take on faith.
Crop:  Must keep both panels or both series so the before/after is visible, the
       axis labels, and the correlation values. Do not crop to one panel.
```

```text
Asset: Dubois et al. 2024, the verbosity-manipulation result in Section 4.1
       (gpt4_1106_preview across concise/standard/verbose prompts, raw versus
       length-controlled win rates)
Shows: One model's number moving 22.9% to 64.3% on wording alone, then holding
       near 42%-52% after correction. This is the length bias in a single view.
Crop:  Must retain both the raw and the controlled rows so the collapse of the
       swing is legible; keep the verbosity-prompt labels.
```

```text
Asset: Dubois et al. 2024, summary table (rows Win rate / Length-controlled /
       Length-normalized against columns for Chatbot Arena correlation and
       gameability)
Shows: The 0.94 correlation and 26% gameability of the raw metric beside the 0.98
       and 10% of the controlled metric, in one comparison.
Crop:  Keep the header and at least the Win rate and Length-controlled rows.
```

```text
Asset: Tunstall et al. 2023, Table 1 (AlpacaEval win % column)
Shows: A real model report leading with an AlpacaEval win rate (Zephyr at 90.60),
       the version-1.0 number the article contrasts with the 2.0 leaderboard.
Crop:  Keep the column header "AlpacaEval (win %)" so the metric is unambiguous.
```

```text
Asset: AlpacaEval 2.0 leaderboard (https://tatsu-lab.github.io/alpaca_eval/)
Shows: The public leaderboard's two columns, length-controlled and raw win rate,
       side by side, where zephyr-7b-beta reads 13.20% and 10.99%.
Crop:  If used, retain both win-rate columns and the model name so the LC/raw gap
       is visible.
```

## Discarded

```text
URL: https://hyunyoung2.github.io/2024/07/20/alpacaEval2/ — secondary blog summary
     of the Dubois paper; adds no figure the paper does not own, and its numbers
     would need re-verification. Not needed once the paper was read directly.
URL: https://futureagi.com/glossary/alpacaeval/ — vendor glossary entry; generic,
     no primary figure, no citation value.
URL: https://llm-stats.com/benchmarks/alpacaeval-2.0 — third-party leaderboard
     mirror; the authoritative numbers live in the tatsu-lab repository, so this
     adds a transcription risk without benefit.
URL: https://www.emergentmind.com/topics/alpacaeval — aggregator topic page;
     surveyed for leads only, cites nothing firsthand.
URL: https://arxiv.org/pdf/2404.04475 — same document as the abstract page already
     recorded; the abs page is the reader-facing URL, the PDF was used only to
     verify figures.
```
