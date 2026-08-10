# Evidence: the-evidence/emergent-abilities-mirage (01)

This record supports the commissioned angle closely, and the angle is balanced enough
that the evidence does not undermine it. Schaeffer, Miranda, and Koyejo (NeurIPS 2023)
own a precise, hedged claim: for the tasks and model outputs they analyze, a
nonlinear or discontinuous scoring metric can turn smooth improvement in a model's
per-token probability into an apparent sudden jump, and swapping to a linear or
continuous metric on the same runs shows gradual improvement. The paper states in its
own words that nothing in it should be read as claiming large models cannot display
emergence. Wei et al. (TMLR 2022) own the claim it rebuts, with an exact definition and
named examples. The disagreement is live and I could open both sides of it: Du et al.
(NeurIPS 2024) argue emergence survives continuous metrics when performance is plotted
against pre-training loss, and Jason Wei, the original author, argues the hard metrics
are the ones worth caring about. The record is strong on what each paper claims and on
the one figure where Schaeffer and Du use the *same* continuous metric (Brier Score) and
reach opposite conclusions. It is thinner in one place: I read Du's Appendix C (where they
say they reconcile their result with Schaeffer's) only through the main-text pointer to it,
not the appendix itself, and Schaeffer's own appendices were read only as summarized by
the figure list, not line by line.

## Sources

```text
URL:         https://arxiv.org/abs/2304.15004
Kind:        primary. Schaeffer, Miranda, and Koyejo author the mirage thesis; the paper
             owns the claim, the mathematical model, and all three empirical tests. Read
             via the arXiv full text and cross-checked against the abstract page.
Establishes: The paper's exact thesis, mechanism, scope, hedges, and the figures the
             argument rests on.
Paraphrase:  For a fixed task and model family, analyzing fixed model outputs, claimed
             emergent abilities can arise from the researcher's choice of metric rather
             than from a fundamental change in the model with scale. Nonlinear or
             discontinuous metrics (exact-string accuracy, multiple-choice grade) produce
             apparent sharp jumps; linear or continuous metrics (token edit distance,
             Brier score) show smooth, predictable improvement on the same runs. They
             back this with a simple mathematical model and three tests: three confirmed
             predictions on InstructGPT/GPT-3 arithmetic, a two-prediction meta-analysis
             of BIG-Bench, and an induced-emergence demonstration on vision networks.
Locators:    Abstract; Sec. 2 (Alternative Explanation); Sec. 3 (InstructGPT/GPT-3
             arithmetic); Sec. 4 (BIG-Bench meta-analysis); Sec. 5 (vision tasks);
             Sec. 7 (Discussion). Figures 2-8.
Quote:       Abstract: "for a particular task and model family, when analyzing fixed model
             outputs, emergent abilities appear due to the researcher's choice of metric
             rather than due to fundamental changes in model behavior with scale."
             Abstract close: "alleged emergent abilities evaporate with different metrics
             or with better statistics, and may not be a fundamental property of scaling
             AI models."
             Discussion (the scope hedge): "nothing in this paper should be interpreted as
             claiming that large language models cannot display emergent abilities."
```

```text
URL:         https://arxiv.org/abs/2206.07682
Kind:        primary. Wei et al. author the emergent-abilities framing that Schaeffer
             rebuts; this paper owns the definition and the headline examples. Published
             in Transactions on Machine Learning Research (TMLR), 2022. Read via arXiv
             full text and abstract page.
Establishes: The definition of an emergent ability and the specific tasks, model
             families, and scale thresholds that made the idea famous.
Paraphrase:  An emergent ability is one absent in smaller models and present in larger
             ones, so it cannot be predicted by extrapolating from smaller-model
             performance. Characterized as a phase-transition-like curve: near-random
             until a critical scale, then a jump to substantially above random. Shown
             across GPT-3, LaMDA, Gopher, Chinchilla, and PaLM, using accuracy, exact
             match, and BLEU as the scoring metrics. Also treats augmented-prompting
             emergence, e.g. chain-of-thought helping only above a scale threshold.
Locators:    Abstract; Sec. 2-3 (definition and few-shot examples); Sec. 4 (augmented
             prompting). Figure 2 is the eight-task panel.
Quote:       Abstract: "We consider an ability to be emergent if it is not present in
             smaller models but is present in larger models. Thus, emergent abilities
             cannot be predicted simply by extrapolating the performance of smaller
             models."
```

```text
URL:         https://arxiv.org/abs/2403.15796
Kind:        primary. Du, Zeng, Dong, and Tang author the loss-perspective defense of
             emergence and own that claim. Published at NeurIPS 2024. I read the NeurIPS
             2024 camera-ready PDF in full (30 pp.); the arXiv abstract page confirms the
             same abstract and resolves to the document's own page.
Establishes: The strongest later primary that argues emergence survives better
             measurement, and the point where it directly contradicts Schaeffer.
Paraphrase:  Plotting downstream performance against pre-training loss (not model size or
             compute), models of different sizes with the same loss show the same
             performance on 12 tasks. On MMLU, C-Eval, GSM8K, and GSM8K-Chinese,
             performance stays at random until pre-training loss falls below about 2.2,
             then climbs. Crucially, they re-score MMLU and C-Eval with two continuous
             metrics (CorrectChoiceProb and Brier Score) and report that the tipping point
             remains, so they argue a continuous metric does not remove the emergence.
             They pre-trained 30+ of their own models (300M-32B) and validate on LLaMA and
             Pythia. They redefine an emergent ability as one absent in higher-loss models
             and present in lower-loss models.
Locators:    Abstract; Sec. 2 (loss-vs-performance, Table 1 task list, Figures 1-3);
             Sec. 3.2 (Influence of Different Metrics, Figure 4, Eq. 2 for Brier Score);
             Sec. 4 (new definition, Eq. 3-5); Sec. 5 (Related Work). Appendix C is where
             they say they reconcile with Schaeffer, read here only via the main-text
             pointer.
Quote:       Sec. 3.2: "All three metrics -- accuracy, correct choice probability, and
             Brier Score -- show emergent performance improvements ... when the pre-training
             loss drops below a certain threshold."
             Sec. 3.2 close: "emergent abilities of language models occur when the
             pre-training loss reaches a certain tipping point, and continuous metrics
             cannot eliminate the observed tipping point."
             Sec. 5: "In this paper we prove the existence of emergent abilities from the
             perspective of pre-training loss, even with continuous metrics."
```

```text
URL:         https://www.jasonwei.net/blog/common-arguments-regarding-emergent-abilities
Kind:        primary for Wei's own rebuttal (he authors the position), but an informal
             self-published blog, not peer-reviewed empirical work. Cite it as "the
             original author's stated response," not as evidence a claim is true.
Establishes: How the author of the original emergence paper answers the metric critique.
Paraphrase:  Wei concedes that some tasks emergent under exact match improve smoothly
             under a soft metric. He argues this does not defeat the significance of
             emergence, because for many tasks the hard metric is the one we actually want:
             asked what 15 + 23 is, you want 38 and nothing else. He also points to
             BIG-Bench tasks that award partial credit where, he says, performance still
             rises sharply at the same threshold.
Locators:    The blog post's section on the metric argument.
Quote:       Paraphrased from the post: for a task like arithmetic you want the exact
             answer (his 15 + 23 = 38 example), so a partial-credit metric is not the goal.
             (I read this as reported prose, not a fixed pull-quote; the writer should
             quote the live page if exact wording is needed.)
```

```text
URL:         https://blog.neurips.cc/2023/12/11/announcing-the-neurips-2023-paper-awards/
Kind:        secondary. The NeurIPS program chairs report the award; they did not author
             the paper. Establishes why the document is famous, not what it says.
Establishes: The mirage paper won a NeurIPS 2023 award, listed under "Outstanding Main
             Track Papers."
Paraphrase:  NeurIPS 2023 named "Are Emergent Abilities of Large Language Models a Mirage?"
             an Outstanding Main Track Paper.
Locators:    The Outstanding Main Track Papers section of the awards announcement.
Quote:       Award category label: "Outstanding Main Track Papers."
```

```text
URL:         https://aihub.org/2024/04/25/are-emergent-abilities-of-large-language-models-a-mirage-interview-with-brando-miranda/
Kind:        secondary. An AIhub interview (Lucy Smith, April 25, 2024) reporting
             co-author Brando Miranda's own framing. The claims are his, but the source is
             reported interview, not the paper.
Establishes: The authors' plain-language statement of scope: the metric drives the jump,
             and they do not deny sharpness or emergence outright.
Paraphrase:  Miranda says the size of the jump depends heavily on the metric, that their
             mathematical model itself predicts sharpness, and that readers should not be
             surprised by sharp jumps when a metric only credits an exact-string match.
Locators:    The interview body.
Quote:       Miranda, on the mechanism: "the jump is a big function of the metric, i.e how
             you score the model's performance." On the caution: "don't be surprised if you
             see sharp jumps if your metric is only allowing credit if you get the exact
             string."
```

## Contradictions

- **Schaeffer vs. Du on the same continuous metric.** This is the center of the live
  disagreement, and it is not a difference of opinion but of result on different data.
  Schaeffer's Figure 6 takes tasks where the LaMDA family looks emergent under the
  discontinuous Multiple Choice Grade, re-scores them with the continuous Brier Score, and
  reports the emergence disappears into a smooth curve. Du's Figure 4 takes MMLU and C-Eval,
  re-scores with the same continuous Brier Score (plus CorrectChoiceProb), and reports the
  tipping point at pre-training loss ~2.2 remains. Same metric name, opposite conclusion,
  because they study different tasks and different model families. Both can be empirically
  correct at once, which is exactly why the question is unsettled. The writer must not let
  "a continuous metric removes emergence" read as settled.

- **Du's Brier Score result carries its own caveat.** Du note that a falling Brier Score
  does not always mean the task is being solved, because Brier Score also depends on the
  probability mass on wrong answers. They report that a context-free predictor giving uniform
  probability over four MMLU options scores 0.75, and that Brier performance is no better than
  random until the loss threshold. So their "continuous metric still shows emergence" claim
  rests on reading the Brier curve against that 0.75 random baseline, not on the curve simply
  being non-smooth. Record this honestly: it is a real qualification inside the defender's own
  paper.

- **Wei concedes the narrow point, disputes its weight.** Wei grants that some exact-match
  emergent tasks smooth out under a soft metric (agreeing with Schaeffer's narrow finding),
  then argues the hard metric is the one that matters for use. This is a disagreement about
  significance, not about the arithmetic-under-two-metrics fact, and should be framed that way.

- **The paper against a "debunked emergence" reading.** Schaeffer's own Discussion and
  Miranda's interview both cut against the popular use of the paper as having killed emergence.
  The paper explicitly does not claim emergence cannot happen; it claims that for the tasks and
  fixed outputs studied, claimed emergence can be a metric artifact. Any present-day framing that
  treats it as an outright debunking contradicts the paper itself.

## Numbers

```text
Figure: Per-token cross-entropy loss modeled as L_CE(N) = (N/c)^alpha, with c > 0 and alpha < 0
Owner:  Schaeffer et al. 2023, Sec. 2
Scope:  N is model parameters; a smooth power-law fall in per-token loss is the assumed input
        that the metric then transforms.
```

```text
Figure: Per-token probability of a correct token p = exp(-(N/c)^alpha); exact-match accuracy over
        L tokens is approximately p^L; token edit distance is approximately L*(1 - p)
Owner:  Schaeffer et al. 2023, Sec. 2
Scope:  L is the target length in tokens. Accuracy compounds geometrically with L (manufacturing a
        sharp jump); token edit distance stays roughly linear in p (staying smooth).
```

```text
Figure: At most 5 of 39 preferred BIG-Bench metrics ever show emergence
Owner:  Schaeffer et al. 2023, Sec. 4
Scope:  Population of Task-Metric-Model-Family triplets across BIG-Bench, hand-annotated.
```

```text
Figure: >92% of emergent abilities appear under one of two metrics: Multiple Choice Grade and
        Exact String Match
Owner:  Schaeffer et al. 2023, Sec. 4
Scope:  Same BIG-Bench triplet population. Multiple Choice Grade is discontinuous; Exact String
        Match is nonlinear.
```

```text
Figure: GPT-3 arithmetic tasks tested = 2-digit multiplication and 4-digit addition, 2-shot
Owner:  Schaeffer et al. 2023, Sec. 3
Scope:  InstructGPT/GPT-3 family; the tasks where accuracy shows apparent emergence and token
        edit distance shows smooth gains on the identical runs.
```

```text
Figure: Wei et al. emergence thresholds (illustrative) -- 3-digit arithmetic around GPT-3 13B;
        larger-digit arithmetic around GPT-3 175B; MMLU around Gopher scale; several BIG-Bench
        tasks emerging at PaLM 540B
Owner:  Wei et al. 2022
Scope:  Few-shot prompted accuracy plotted against training FLOPs / parameter count. Treat the
        specific scale figures as the paper's own illustrative anchors, not exact constants; the
        writer should read the exact axis values off Wei's Figure 2 before quoting a number.
```

```text
Figure: Du emergence threshold at pre-training loss ~2.2 on MMLU, C-Eval, GSM8K, GSM8K-Chinese
Owner:  Du et al. 2024, Sec. 2-3
Scope:  Their own 300M-32B models plus intermediate checkpoints; loss on a 4:1 English:Chinese
        corpus. Below ~2.2 the four "hard" tasks rise from random; the other 8 of 12 tasks rise
        from the start.
```

```text
Figure: Du best context-free Brier Score = 0.75 on four-option MMLU/C-Eval (the random baseline)
Owner:  Du et al. 2024, Sec. 3.2
Scope:  A uniform-probability predictor over four options. This is the baseline their Brier curve
        is read against; below it means better than random.
```

```text
Figure: Du scale = 30+ models pre-trained from scratch (300M, 540M, 1B, 1.5B, 3B, 6B, 32B),
        validated on LLaMA (7B-65B) and Pythia; 12 downstream datasets
Owner:  Du et al. 2024, Sec. 2
Scope:  Shows the size of the foundation under the defender's claim.
```

## Source assets

```text
Asset: Schaeffer et al. 2023, Figure 2 (six-panel schematic of the mechanism)
Shows: The whole argument in one image. Panels move from a smooth power-law fall in per-token
       loss and a smoothly rising per-token probability, to sharp emergent-looking curves under
       Accuracy and Multiple Choice Grade, to smooth curves under Token Edit Distance and Brier
       Score. This is the clearest single teaching aid for "smooth underneath, jump on top."
Crop:  Keep at least one nonlinear-metric panel beside one continuous-metric panel so the reader
       sees the same underlying trend read two ways. Do not crop to a single panel.
```

```text
Asset: Schaeffer et al. 2023, Figure 3 (GPT-3 arithmetic under two metrics)
Shows: Real model runs, not a schematic: apparent emergence under Accuracy (top) and smooth
       improvement under Token Edit Distance (bottom) on the identical GPT-3 outputs.
Crop:  Keep both rows; the contrast is the point. Retain axis labels and the metric names.
```

```text
Asset: Schaeffer et al. 2023, Figure 6 (LaMDA: Multiple Choice Grade vs Brier Score)
Shows: The specific case the writer needs for the contradiction: emergence under a discontinuous
       metric that vanishes under a continuous one. Pair it against Du Figure 4 to stage the debate.
Crop:  Keep both left (Multiple Choice Grade) and right (Brier Score).
```

```text
Asset: Du et al. 2024, Figure 4 (MMLU and C-Eval under Accuracy, CorrectChoiceProb, Brier Score)
Shows: The counter-result: on these tasks the tipping point near loss 2.2 persists under two
       continuous metrics. Set directly against Schaeffer Figure 6, this is the visual heart of
       the live disagreement.
Crop:  Keep the continuous-metric panels (CorrectChoiceProb, BrierScore), and keep the random-guess
       dashed line, which is what makes the Brier reading legible.
```

```text
Asset: Wei et al. 2022, Figure 2 (eight-task emergence panel)
Shows: The original picture of emergence: near-random accuracy across orders of magnitude of
       compute, then a jump. The eight tasks include modular arithmetic, IPA transliteration, word
       unscrambling, Persian QA, TruthfulQA, grounded mappings, multi-task NLU (MMLU), and word in
       context.
Crop:  If space forces a subset, keep two or three panels with visible near-random floors so the
       "flat then jump" shape reads. Keep the log-scale x-axis note.
```

```text
Asset: Du et al. 2024, Figure 1 (performance vs pre-training loss, 12 tasks)
Shows: The two families of tasks side by side: eight that rise smoothly from the start and four
       (MMLU, C-Eval, GSM8K, GSM8K-Chinese) that stay flat until loss ~2.2. Useful if the piece
       wants to show emergence is task-specific, not universal.
Crop:  If subsetting, keep at least one smooth task and one thresholded task with the random line.
```

## Discarded

```text
URL: https://arxiv.org/html/2304.15004v2 -- returned 404; used the ar5iv full-text render and the
     arXiv abstract page instead. Not a source problem, a routing one.
URL: https://ar5iv.labs.arxiv.org/html/2403.15796 -- only the abstract rendered for the Du paper;
     replaced by reading the NeurIPS 2024 camera-ready PDF in full. Recorded the arXiv abs page as
     the citable home, since it resolves and matches.
URL: https://proceedings.neurips.cc/paper_files/paper/2024/file/5f1eee2509599faeeb3570a887016a64-Paper-Conference.pdf
     -- this is the exact file I read for Du, but it is a direct PDF endpoint; the document's own
     landing page is the arXiv abs above, which is what the writer should cite.
```
