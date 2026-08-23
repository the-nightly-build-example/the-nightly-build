# evidence: the-mechanics/false-confidence (01)

The evidence supports the mechanical spine of the commission well and complicates
two of its framing claims. Firmly sourced: the softmax at each step is a
distribution over the next token (settled architecture); calibration has a
precise, owned definition and a standard measure, ECE (Guo et al. 2017); a base
model's multiple-choice probabilities are well-calibrated and RLHF post-training
reduces that calibration (GPT-4 technical report, Figure 8); the stated confidence
a chat model prints is generated text, produced by the same next-token process,
not read off the logit distribution (Lin/Hilton/Evans, Tian et al.). Where the
evidence is thin or cuts against the commission: (1) the GPT-4 report gives **no
numeric ECE** for its Figure 8 — it shows two reliability plots and the words
"highly calibrated" versus calibration "reduced," nothing more, so the commission's
"actual numbers" worked example does not exist in the primary and must not be
invented; (2) the commission's claim that the softmax is "the only internal
quantity resembling confidence" is too strong — Kadavath et al. and Lin et al.
find additional latent uncertainty signals a model can be made to report; (3) the
claim that stated confidence "carries zero information about correctness" is
contradicted by Tian et al., who show that a numeric confidence explicitly asked
for is often *better* calibrated than the model's own token probabilities. The
honest spine survives; two absolute phrasings do not. Details and the exact
numbers below.

## Sources

```text
URL:         https://arxiv.org/abs/2303.08774
Kind:        primary. OpenAI authoring OpenAI's own model; it owns the GPT-4
             calibration result firsthand.
Establishes: The pre-trained (base) GPT-4 model is well-calibrated on a subset of
             MMLU, and RLHF/post-training reduces that calibration. Also that the
             report attributes exam capability to pre-training, not to RLHF.
Paraphrase:  In Section 5 (Limitations), the report states GPT-4 "can also be
             confidently wrong," that the pre-trained model is "highly calibrated
             (its predicted confidence in an answer generally matches the
             probability of being correct)," and that "after the post-training
             process, the calibration is reduced (Figure 8)." Figure 8 is a pair
             of reliability diagrams (base left, post-trained right) on an MMLU
             subset, x-axis = model confidence bins over the A/B/C/D choices,
             y-axis = accuracy in bin, dotted diagonal = perfect calibration. The
             report gives NO numeric ECE for either panel — the magnitude is only
             shown visually.
Locators:    Section 5 "Limitations"; Figure 8 and its caption.
Quote:       Caption: "Left: Calibration plot of the pre-trained GPT-4 model on a
             subset of the MMLU dataset. ... The dotted diagonal line represents
             perfect calibration. Right: Calibration plot of the post-trained
             GPT-4 model on the same subset of MMLU. The post-training hurts
             calibration significantly." Body: "the pre-trained model is highly
             calibrated ... However, after the post-training process, the
             calibration is reduced (Figure 8)."
```

```text
URL:         https://proceedings.mlr.press/v70/guo17a.html
Kind:        primary. Guo, Pleiss, Sun & Weinberger (ICML 2017) own the
             definition and the finding for modern nets.
Establishes: The formal definition of calibration, the reliability diagram, the
             ECE measure, and the empirical finding that modern deep networks are
             overconfident where older shallow ones were calibrated.
Paraphrase:  Perfect calibration: for a predictor h(X) = (Y-hat, P-hat), the
             fraction correct among predictions made at confidence p equals p, for
             all p. A reliability diagram plots accuracy as a function of
             confidence; a calibrated model traces the diagonal, and any deviation
             is miscalibration. ECE partitions predictions into M equal-width
             confidence bins and takes the sample-weighted average of
             |accuracy(bin) - confidence(bin)|. The headline finding: unlike
             networks "from a decade ago," modern networks "are no longer
             well-calibrated" — a 110-layer ResNet on CIFAR-100 has higher
             accuracy than a 5-layer LeNet but its average confidence sits well
             above its accuracy. Temperature scaling (dividing logits by a single
             learned T) largely fixes it post hoc.
Locators:    Abstract; Section 1 (Figure 1); Section 2 "Definitions" (Eq. 1 for
             perfect calibration; ECE Eq. 2 / bin definitions).
Quote:       Perfect calibration (Eq. 1): "P( Y-hat = Y | P-hat = p ) = p, for all
             p in [0,1]." Abstract: "we discover that modern neural networks,
             unlike those from a decade ago, are poorly calibrated." Section 1:
             "The average confidence of LeNet closely matches its accuracy, while
             the average confidence of the ResNet is substantially higher than its
             accuracy."
```

```text
URL:         https://arxiv.org/abs/2207.05221
Kind:        primary. Kadavath et al. 2022 (Anthropic) report firsthand
             experiments on their own language models.
Establishes: Large models are well-calibrated on multiple-choice / true-false
             *when the question is given in the right format*; models can
             self-evaluate P(True); models can be trained to output P(IK), the
             probability they know an answer, but P(IK) calibration does not
             transfer cleanly to new tasks. This is the primary for "models carry
             some internal signal of their own uncertainty," and for the strong
             format-dependence of that signal.
Paraphrase:  Calibration = "the probability it assigns to outcomes coincides with
             the frequency with which these outcomes actually occur." Larger models
             (up to 52B) are well-calibrated on diverse multiple-choice and T/F
             questions given visible lettered options; calibration improves with
             model size and from zero-shot to few-shot, and degrades under other
             formats (e.g. having to rewrite full answers, or a "none of the above"
             option). P(True): the model proposes an answer, then estimates the
             probability the answer is correct; this is reasonably calibrated and
             improves when the model first sees many of its own samples. P(IK): a
             value-head-trained probability of knowing the answer with no specific
             candidate answer shown; performs well in-distribution but is "poorly
             calibrated on ... other distributions," i.e. partial generalization.
             The models are Anthropic's own; the study probes the model's *own
             probabilities*, not verbalized text confidence.
Locators:    Abstract; Section 2 (calibration on MC); Section 3 (format effects,
             T/F); Section 4 (P(True)); Section 5 (P(IK), incl. 5.1 in-dist, 5.2
             cross-task, 5.3-5.4 context/hints).
Quote:       Abstract: "larger models are well-calibrated on diverse multiple
             choice and true/false questions when they are provided in the right
             format ... Models perform well at predicting P(IK) and partially
             generalize across tasks, though they struggle with calibration of
             P(IK) on new tasks."
```

```text
URL:         https://arxiv.org/abs/2205.14334
Kind:        primary. Lin, Hilton & Evans (Oxford/OpenAI, TMLR 2022) own the
             verbalized-uncertainty result.
Establishes: A distinction the commission's spine needs: a model can be trained to
             emit a confidence *in words/numbers as generated text*, "without use
             of model logits," and those verbal levels can be calibrated. This is
             the primary that verbalized confidence is a separate channel from the
             logit distribution, and evidence that latent uncertainty
             representations exist.
Paraphrase:  A GPT-3 model is finetuned to output both an answer and a confidence
             phrased in language ("90% confidence," "high confidence"); those
             levels map to well-calibrated probabilities and stay moderately
             calibrated under distribution shift. The verbalized channel is
             explicitly not read from logits. The authors argue the ability to
             generalize calibration rests on "pre-trained latent representations
             that correlate with epistemic uncertainty over its answers." Tested on
             their CalibratedMath arithmetic suite. This is a *finetuning* result on
             GPT-3, not a property of an off-the-shelf chat model.
Locators:    Abstract; Section 1; CalibratedMath task definition.
Quote:       Abstract: "a GPT-3 model can learn to express uncertainty about its
             own answers in natural language – without use of model logits. ...
             These levels map to probabilities that are well calibrated. ... GPT-3's
             ability to generalize calibration depends on pre-trained latent
             representations that correlate with epistemic uncertainty over its
             answers."
```

```text
URL:         https://aclanthology.org/2023.emnlp-main.330/
             (also https://arxiv.org/abs/2305.14975)
Kind:        primary. Tian et al. 2023 (Stanford/Harvard, EMNLP 2023) run the
             experiments they report.
Establishes: The central contradiction to the commission's "stated confidence
             carries zero information": for RLHF chat models (ChatGPT, GPT-4,
             Claude), a verbalized numeric confidence the model is *asked* for is
             typically better-calibrated than the model's own token probabilities,
             cutting ECE by roughly half. Also confirms the mechanism direction:
             pre-training yields well-calibrated conditional probabilities and RLHF
             degrades them.
Paraphrase:  "Unsupervised pre-training produces ... LMs whose conditional
             probabilities are remarkably well-calibrated," while RLHF-LMs "produce
             conditional probabilities that are very poorly calibrated" and
             overconfident. Across TriviaQA, SciQ, TruthfulQA, verbalized
             confidences "emitted as output tokens are typically better-calibrated
             than the model's conditional probabilities," often reducing ECE by a
             relative ~50%. The proposed mechanism for RLHF miscalibration: the RL
             objective pushes probability mass onto the single preferred answer
             rather than matching answer frequencies. The gain is uneven: largest
             on TruthfulQA (worst-calibrated), and Claude-1 verbalizes less well
             than the GPT family.
Locators:    Abstract; Section 1 (Figures 1-2, RLHF-worsens-calibration on
             Llama-2-70B; mechanism); Tables 1-4 (gpt-3.5, gpt-4, Claude-1,
             Claude-2 ECE by dataset).
Quote:       Abstract: "For RLHF-LMs such as ChatGPT, GPT-4, and Claude, we find
             that verbalized confidences emitted as output tokens are typically
             better-calibrated than the model's conditional probabilities on the
             TriviaQA, SciQ, and TruthfulQA benchmarks, often reducing the expected
             calibration error by a relative 50%."
```

```text
URL:         https://arxiv.org/abs/2306.13063
Kind:        primary. Xiong et al. 2023 (NUS et al., ICLR 2024) run the
             benchmark firsthand.
Establishes: The other side of the verbalized-confidence picture, and the reason
             the reader's everyday experience is of empty confidence: left to their
             default behavior, LLMs verbalize confidence overconfidently and cluster
             it in a high, narrow band, plausibly copying human phrasing.
Paraphrase:  Across five datasets and four LLMs, "LLMs, when verbalizing their
             confidence, tend to be overconfident, potentially imitating human
             patterns of expressing confidence." Calibration and failure-prediction
             improve as model capability scales; human-inspired prompts, sampling
             consistency, and aggregation reduce overconfidence, but no single
             method wins and all struggle on professional-knowledge tasks. Reconciles
             with Tian: the raw, un-elicited assertive tone is overconfident;
             structured elicitation is what recovers signal.
Locators:    Abstract; benchmark setup (verbalize / consistency / hybrid methods).
Quote:       Abstract: "LLMs, when verbalizing their confidence, tend to be
             overconfident, potentially imitating human patterns of expressing
             confidence."
```

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary. Ouyang et al. 2022 (OpenAI) own the InstructGPT/RLHF result.
Establishes: What the post-training step optimizes for — outputs human labelers
             prefer — which grounds the commission's step-2 claim that RLHF makes a
             model "helpful and confident-sounding." Owns the RLHF-on-preferences
             mechanism, not the calibration effect.
Paraphrase:  Models are aligned by collecting human rankings of outputs and
             fine-tuning with reinforcement learning from human feedback so the model
             produces the outputs labelers rank highest; labelers prefer the 1.3B
             InstructGPT to the 175B GPT-3. The training target is human preference /
             helpfulness, not truthfulness or calibrated uncertainty.
Locators:    Abstract; RLHF training procedure.
Quote:       (Abstract, paraphrased) rankings of model outputs are used "to further
             fine-tune this supervised model using reinforcement learning from human
             feedback"; the smaller InstructGPT model's outputs are preferred to the
             far larger GPT-3's.
```

```text
URL:         https://aclanthology.org/2024.naacl-long.366/
Kind:        secondary. Geng et al. 2024 (NAACL) survey others' work; they
             organize and report findings they did not themselves produce.
Establishes: Context and framing only — that confidence estimation / calibration
             in LLMs is an active, unsettled field with many competing methods, and
             that overconfidence after alignment is a recognized, general problem.
             Use for orientation, never as the owner of any specific figure.
Paraphrase:  A review of confidence-estimation and calibration methods for LLMs,
             written because "there has been no comprehensive overview to organize
             it." Frames LLM unreliability (factual errors) as the motivating
             problem and catalogs calibration techniques. Secondary throughout;
             every quantitative claim traces to a primary it cites.
Locators:    Abstract; survey taxonomy sections.
Quote:       Abstract: "There has been a lot of recent research aiming to address
             this, but there has been no comprehensive overview to organize it and
             to outline the main lessons learned."
```

## Contradictions

- **"Stated confidence carries zero information about correctness" is too
  absolute.** Tian et al. show that for RLHF chat models a *numeric confidence the
  model is asked to state* is typically better-calibrated than the model's own
  token probabilities, cutting ECE by ~half on three datasets. The generated-text
  confidence is not noise; when explicitly elicited it can out-inform the logits.
  The defensible version of the commission's claim is narrower: the model's default
  assertive *tone*, and an unsolicited "I'm 95% sure," is uninformative (Xiong et
  al.: default verbalized confidence is overconfident and human-mimicking), but a
  properly elicited verbalized probability is not.

- **"The softmax is the only internal quantity resembling confidence" is too
  absolute.** Kadavath et al. (P(True), P(IK)) and Lin et al. ("latent
  representations that correlate with epistemic uncertainty") both find internal
  uncertainty signals beyond the surface next-token distribution that a model can be
  trained to surface. The commission is right that the *printed words* are not read
  off the logits and that there is no verified truth-checking module; it overstates
  by calling the softmax the sole internal confidence signal.

- **RLHF need not destroy all usable confidence, and does not uniformly.** The GPT-4
  report shows degradation qualitatively; Tian shows the *conditional-probability*
  calibration is hurt but the information is recoverable by asking, and that base
  pre-training calibration is genuinely good. So "post-training flattens the honest
  uncertainty signal" is correct for the logit channel, but the signal is degraded,
  not erased — it can be partly recovered through verbalized elicitation and
  temperature scaling.

- **Verbalized-confidence gains are uneven, so do not overclaim the counter-story
  either.** In Tian's own tables the ECE improvement is large on TruthfulQA, small
  on TriviaQA where GPT-4's label probabilities are already near 0.074, and the
  selective-accuracy AUC does not always improve. Claude-1 verbalizes less well than
  the GPT family. The reader should get "sometimes recoverable when asked," not
  "verbalized confidence is reliable."

- **Why RLHF degrades calibration is not settled.** The GPT-4 report only reports
  that it does. Tian offers a hypothesis (the RL objective concentrates mass on the
  single preferred answer). This is a proposed mechanism from a third party, not a
  demonstrated cause owned by the model's makers; present it as a leading
  explanation, not established fact.

## Numbers

```text
Figure: GPT-4 base model — "highly calibrated" on an MMLU subset; post-RLHF —
        calibration "reduced." NO numeric ECE is given in the report.
Owner:  GPT-4 technical report, Figure 8 (Section 5).
Scope:  A subset of MMLU (4-way multiple choice, A/B/C/D). Magnitude shown only as
        two reliability diagrams; the report supplies no scalar. Do not cite a
        numeric GPT-4 ECE — none exists in the primary.
```

```text
Figure: ResNet (110-layer) on CIFAR-100 — top-1 error 30.6% (accuracy ~69.4%),
        with average confidence substantially above accuracy. LeNet (5-layer) —
        error 44.9% (accuracy ~55.1%), average confidence ≈ accuracy.
Owner:  Guo et al. 2017, Figure 1.
Scope:  CIFAR-100 test set; illustrative example of modern-net overconfidence. The
        confidence values are read from a plot; cite the error figures (printed) and
        the qualitative confidence-vs-accuracy gap, not a precise confidence decimal.
```

```text
Figure: Verbalized vs conditional-probability ECE, gpt-3.5-turbo (Tian Table 1):
        TriviaQA  Label prob. 0.078 -> Verb. 1S 0.024-0.025
        SciQ      Label prob. 0.219 -> Verb. 1S top-4 0.056 / Ling. 1S-opt 0.028
        TruthfulQA Label prob. 0.445 -> Verb. 1S top-4 0.198 / Ling. 1S-opt 0.082
Owner:  Tian et al. 2023, Table 1 (ECE column, lower is better).
Scope:  1000 sampled TriviaQA and SciQ validation questions; all 817 TruthfulQA
        validation questions. Correctness judged by GPT-4/GPT-3.5 equivalence check.
```

```text
Figure: Verbalized vs conditional-probability ECE, gpt-4 (Tian Table 2):
        TriviaQA  Label prob. 0.074 -> Verb. 1S 0.046-0.075 (little change)
        SciQ      Label prob. 0.216 -> Ling. 1S-opt 0.089
        TruthfulQA Label prob. 0.432 -> Ling. 1S-opt 0.139 (largest gain)
Owner:  Tian et al. 2023, Table 2.
Scope:  Same three datasets/splits. Shows the gain is dataset-dependent and largest
        where the model is worst-calibrated; TriviaQA barely moves.
```

```text
Figure: Headline effect size — verbalized confidence "often reduc[es] the expected
        calibration error by a relative 50%" vs the model's conditional probabilities.
Owner:  Tian et al. 2023, Abstract.
Scope:  RLHF-LMs (ChatGPT, GPT-4, Claude) over TriviaQA, SciQ, TruthfulQA. This
        abstract-owned relative figure is the safest single number for the article.
```

```text
Figure: ECE definition — sample-weighted mean of |accuracy(bin) - confidence(bin)|
        over M equal-width confidence bins.
Owner:  Guo et al. 2017, Section 2 (Eq. 2).
Scope:  General definition; the standard scalar the whole calibration literature,
        including the GPT-4 plot's implicit axis, is built on.
```

## Source assets

```text
Asset: GPT-4 technical report, Figure 8 — the two side-by-side reliability
       diagrams (base model left, post-RLHF model right) on an MMLU subset.
Shows: The whole worked example in one image: the base model's bars track the
       diagonal; the post-trained model's bars pull away from it. It carries the
       argument better than any prose restatement, and it is the correct asset
       precisely because the report gives no number to quote.
Crop:  Must keep both panels together (the comparison is the point), both axes, and
       the dotted diagonal. Do not crop to a single panel; a lone panel loses the
       before/after that is the finding.
```

```text
Asset: Guo et al. 2017, Figure 1 — LeNet vs ResNet confidence histograms (top) and
       reliability diagrams (bottom) on CIFAR-100.
Shows: What "overconfident" looks like: the ResNet's confidence mass piled near 1.0
       while its accuracy is lower, beside a well-calibrated shallow net. A clean
       visual anchor for the definition before GPT-4 is introduced.
Crop:  Keep at least the two bottom reliability diagrams with the diagonal and the
       error annotations; retain both networks for the contrast.
```

```text
Asset: Tian et al. 2023, Figure 1 — verbalized (blue) vs log-probability (orange)
       calibration bars for gpt-3.5-turbo on SciQ.
Shows: The contradiction in one frame: raw model probabilities overconfident,
       verbalized numeric confidence closer to the diagonal.
Crop:  Keep the paired panels and the diagonal; the comparison, not one bar chart,
       is the content.
```

## Discarded

```text
URL: https://ritvik19.medium.com/papers-explained-67-gpt-4-fc77069b613e — secondary
     blog summary of the GPT-4 report; superseded by reading the report directly.
URL: https://patrick-llgc.github.io/Learning-Deep-Learning/paper_notes/gpt4.html —
     third-party paper notes; not needed once the primary was read.
URL: https://github.com/vlgiitr/papers_we_read/.../Calibration_of_Neural_Nets.md —
     third-party summary of Guo et al.; the primary supplies the definitions.
URL: https://arxiv.org/pdf/2410.09724 (Taming Overconfidence, Reward Calibration in
     RLHF) — real and on-topic, but a proposed fix beyond this lesson's scope; would
     pull the piece toward remedies it does not need. Not cited.
URL: https://arxiv.org/pdf/2505.02151 (LLMs are overconfident and amplify human
     bias) — adjacent finding; Xiong et al. already carries the "verbalized
     overconfidence" point from a stronger, peer-reviewed primary.
```

Note on verification: two automated PDF reads of secondary origin returned figures
that did not survive checking against the primaries — a claimed GPT-4/Guo pair of
"74.5% / 81.7%" confidence-accuracy numbers, and a set of Tian Table 1 values — and
were discarded. The numbers recorded above are read from the primaries' own text and
tables (pdftotext of the source PDFs, Guo Figure 1 error annotations, Tian Tables
1-2). The single number a writer might most want, a GPT-4 base-vs-RLHF ECE, does not
exist in the report and was not substituted.
