# Evidence: the-mechanics/hedging (01)

The evidence supports the commission's three-step chain, but the strongest link
is the middle one. For the reward-model step there is a first-party admission
that names the exact cause the commission proposes: InstructGPT's own paper says
its labelers were told to reward epistemic humility, that labelers therefore
rewarded hedging, and that the reward model picked this up (Ouyang et al. 2022,
sections 4.3 and 5.3). That single source ties the observed behavior to the
mechanism better than anything else here. The safety-and-design step is
documented directly in the policy documents that own it: OpenAI's Model Spec
ranks a hedged right answer above no answer and far above a confident wrong one,
and Anthropic states it wants "professional reticence" on hot-button topics. The
base-model step is the thinnest: no source I found measures a base model
completing toward hedged prose on advice-shaped prompts, so that step is
presented as reasoning the reader can follow, anchored only by the finding that
base models are well-calibrated (they are not hedging from ignorance). The
evidence also contains a genuine tension the editor must weigh: on scored
factual benchmarks the same training pipeline is documented pushing the opposite
way, toward confident guessing, and frontier models in 2026 hedge very little on
several measures. Quantitative hedging rates exist but come from one narrow
domain (human-rights prompts), so no source supports a general "assistants hedge
X% of the time" figure.

## Sources

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary. OpenAI's own paper on InstructGPT; it owns both the RLHF
             method and the first-hand observation of the model's hedging.
Establishes: (a) how the reward model is built from labeler rankings of model
             outputs; (b) that InstructGPT over-hedges even when a clear answer
             exists; (c) the authors' own explanation that this traces to
             labelers being instructed to reward epistemic humility.
Paraphrase:  Labelers rank between 4 and 9 responses per prompt, producing all
             pairwise comparisons, and the reward model is trained on those
             comparisons. In qualitative results the authors report the model
             can hedge on questions that have a clear answer. In limitations
             they attribute this to a labeler instruction to reward epistemic
             humility, which the reward model then learns.
Locators:    Sec 3.5 (Reward modeling); Sec 4.3 (Qualitative results); Sec 5.3
             (Limitations), under "InstructGPT still makes simple mistakes."
Quote:       "the model can overly hedge; when given a simple question, it can
             sometimes say that there is no one answer to the question and give
             multiple possible answers, even when there is one fairly clear
             answer from the context" (4.3). "we instruct labelers to reward
             epistemic humility; thus, they may tend to reward outputs that
             hedge, and this gets picked up by our reward model" (5.3).
```

```text
URL:         https://arxiv.org/abs/2210.10760
Kind:        primary. Gao, Schulman, Hilton (OpenAI); it owns the measurement of
             reward-model overoptimization.
Establishes: The reward model is an imperfect proxy, and optimizing it too hard
             degrades true quality (Goodhart). As optimization increases, the
             gold-standard score first rises, then falls.
Paraphrase:  A learned reward model stands in for human judgment. Pushing a
             policy to maximize that proxy raises the true objective up to a
             point and then lowers it. This is the general shape of why chasing
             a rater-derived signal drifts a model away from what raters
             actually wanted.
Locators:    Abstract and Introduction.
Quote:       "Because the reward model is an imperfect proxy, optimizing its
             value too much can hinder ground truth performance, in accordance
             with Goodhart's law."
```

```text
URL:         https://arxiv.org/abs/2303.08774
Kind:        primary. OpenAI's GPT-4 Technical Report; it owns the calibration
             measurement on its own model.
Establishes: The pre-trained model is well-calibrated; post-training (RLHF)
             reduces calibration on MMLU. This is documented as a plot, not a
             single error figure.
Paraphrase:  Before RLHF the model's stated confidence tracks its accuracy.
             After RLHF that match degrades. The report shows two calibration
             plots (pre- vs post-training) and states the loss plainly.
Locators:    Sec 5 (Limitations), Figure 8 and its caption.
Quote:       "the pre-trained model is highly calibrated ... However, after the
             post-training process, the calibration is reduced." Figure 8
             caption: "The post-training hurts calibration significantly."
```

```text
URL:         https://arxiv.org/abs/2305.14975
Kind:        primary. "Just Ask for Calibration" (Tian et al. 2023, EMNLP); it
             owns the measurement of RLHF-model miscalibration and the
             verbalized-confidence result.
Establishes: RLHF-tuned models produce badly calibrated internal probabilities;
             asking them to state confidence in words is better calibrated,
             cutting expected calibration error by about half on three
             benchmarks.
Paraphrase:  RL finetuning concentrates probability on the preferred answer, so
             the model's token-level confidence no longer reflects how likely it
             is right. Confidence spoken as words is closer to the truth.
Locators:    Abstract and results on TriviaQA, SciQ, TruthfulQA.
Quote:       "RLHF-LMs produce conditional probabilities that are very poorly
             calibrated." Verbalized confidences "often reducing the expected
             calibration error by a relative 50%."
```

```text
URL:         https://arxiv.org/abs/2207.05221
Kind:        primary. Kadavath et al. 2022 (Anthropic), "Language Models
             (Mostly) Know What They Know"; owns the base-model calibration
             finding.
Establishes: Large pretrained models are well-calibrated on multiple-choice and
             true/false questions given the right format, and RL finetuning
             tends to collapse those predictions (partly recoverable by
             temperature scaling). Supports that hedging is not simple ignorance
             and that finetuning, not pretraining, distorts stated confidence.
Paraphrase:  The base model's probabilities line up with its accuracy when the
             question is posed as a choice. RL finetuning collapses the
             distribution onto the chosen answer, breaking that alignment.
Locators:    Calibration sections (multiple-choice and true/false); discussion
             of RLHF policies appearing miscalibrated.
Quote:       "our largest models tend to produce a well-calibrated probability
             distribution among the available options." On tuned policies:
             "RL finetuning tends to collapse language model predictions."
```

```text
URL:         https://model-spec.openai.com/2025-12-18.html
Kind:        primary. OpenAI Model Spec (current at publication date); it owns
             the design choice, not a report of one.
Establishes: Hedging is partly a deliberate target. The spec ranks answer types
             and places a hedged right answer above no answer and far above a
             confident wrong answer, tells the model to express uncertainty, and
             tells it to present multiple viewpoints and assume an objective
             point of view on contested topics.
Paraphrase:  The written policy prefers a hedge to a wrong commitment and asks
             for even-handed treatment of contested questions. This makes
             hedging the rational output under the stated reward, not an
             accident, on questions the policy treats as contested or uncertain.
Locators:    "Seek the truth together" > "Be honest and transparent" (the
             ranking; "Express uncertainty"); "Seek the truth together" >
             "Don't have an agenda" ("Assume an objective point of view").
Quote:       "confident right answer > hedged right answer > no answer > hedged
             wrong answer > confident wrong answer."
Note:        The same ranking appears in the archived 2024-05-08 spec
             (https://cdn.openai.com/spec/model-spec-2024-05-08.html), so this
             is a stable, not new, policy.
```

```text
URL:         https://www.anthropic.com/news/political-even-handedness
Kind:        primary. Anthropic's own statement; it owns both the policy and the
             even-handedness measurement of its models.
Establishes: Deliberate non-commitment on contested political topics is a stated
             design goal, and Anthropic measures how evenly its models treat
             opposing views. Refusing to engage and one-sided persuasion are
             penalized; balanced engagement is rewarded.
Paraphrase:  Anthropic says it wants Claude to avoid unsolicited political
             opinions and to give balanced information on political questions,
             and it scores models on treating opposing views with equal depth.
Locators:    Body text on the even-handedness goal and scores; description of
             what the automated evaluation rewards and penalizes.
Quote:       Design: Claude should "provide information or discuss different
             perspectives without expressing personal opinions or taking sides"
             and "err on the side of providing balanced information on political
             questions." Scoring penalizes a model that argues one side in
             detail while giving the other "only bullet points."
```

```text
URL:         https://arxiv.org/abs/2502.19463
Kind:        primary. "Hedging and Non-Affirmation: Quantifying LLM Alignment on
             Questions of Human Rights" (2025); it owns the measured hedging
             rates.
Establishes: A concrete, quantified definition of hedging and per-model rates,
             in one narrow domain. Provides the article's only measured hedging
             figures; also shows hedging depends on the group in the prompt.
Paraphrase:  The study defines hedging as a response that avoids a yes/no
             commitment by referencing an opposing view, then scores seven
             models on human-rights prompts built from the Universal Declaration
             of Human Rights across 205 identities. Rates vary widely by model.
Locators:    Definition of hedging (three sub-categories A/B/C); results tables
             of hedging and non-affirmation rates by model; method (UDHR
             Articles 2-21, 205 identities, 4,738 prompts per model, 7 models).
Quote:       Hedging is when "the response avoids fully committing to a singular
             yes/no view by referencing an opposing point of view."
```

```text
URL:         https://arxiv.org/abs/2509.04664
Kind:        primary. Kalai, Nachum, Vempala, Zhang (OpenAI 2025), "Why Language
             Models Hallucinate"; owns the argument about evaluation incentives.
Establishes: A countervailing pressure. On scored tasks, training and evaluation
             reward confident guessing over admitting uncertainty, because a
             model that guesses scores better than one that abstains. This runs
             opposite to the hedging pressure and shows the direction of the
             bias depends on the task.
Paraphrase:  Where benchmarks grade answers as right or wrong with no credit for
             "I don't know," the optimum is to guess confidently, not to hedge.
             The hedging story and the hallucination story are the same
             optimization pointed at different reward signals.
Locators:    Abstract; argument that models are optimized as test-takers.
Quote:       "language models hallucinate because the training and evaluation
             procedures reward guessing over acknowledging uncertainty" and
             "language models are optimized to be good test-takers, and guessing
             when uncertain improves test performance."
```

```text
URL:         https://arxiv.org/abs/2310.13548
Kind:        primary. Sharma et al. 2023 (Anthropic), "Towards Understanding
             Sycophancy in Language Models"; owns the sycophancy measurement.
Establishes: The boundary the commission requires. Sycophancy is caving to user
             pressure (matching the user's stated belief); it is a distinct
             failure from non-commitment, though both arise from preference
             optimization. Human raters and preference models sometimes prefer a
             convincing sycophantic answer over a correct one.
Paraphrase:  Preference optimization can reward agreeing with the user over
             being right. That is a different mechanism from refusing to commit:
             sycophancy needs a user position to bend toward; hedging appears
             before any pushback.
Locators:    Abstract; sections on human/PM preference for sycophantic answers.
Quote:       "both humans and preference models (PMs) prefer convincingly-written
             sycophantic responses over correct ones a non-negligible fraction
             of the time."
```

```text
URL:         https://www.interconnects.ai/p/openai-rlhf-model-spec
Kind:        secondary. Nathan Lambert (Interconnects), an RLHF researcher,
             analyzing OpenAI's Model Spec from outside OpenAI.
Establishes: Context and interpretation: that the answer-type ranking is an
             intentional hierarchy in which hedging is the second-best outcome,
             and that reducing diverse views to one answer is a structural
             tension the spec is trying to manage, not a bug a patch removes.
Paraphrase:  A knowledgeable outside reading confirms the ranking is deliberate
             and frames the neutrality requirement as hard by design. Use for
             framing, not for any load-bearing figure.
Locators:    Discussion of the answer-type ranking and "Assume an objective
             point of view."
Quote:       None needed; the primary Model Spec carries the wording.
```

```text
URL:         https://www.lesswrong.com/posts/vBDupg8iPqgdwhFzz/demands-are-all-you-need-prompt-imperativeness-drastically
Kind:        secondary, low weight. A self-published, non-peer-reviewed student
             study (author "fluxxrider," via the Lumiere program). It owns its
             own measurement but has not been reviewed, and the models tested are
             small ("mini"/"flash"/"haiku" tiers).
Establishes: Direction only, not a citable number: hedging on subjective
             questions collapses under demanding/imperative prompt phrasing,
             while factual questions hedge little regardless. Supports that the
             hedge is a controllable default, consistent with a withheld-stance
             reading, not fixed ignorance.
Paraphrase:  Rephrasing a request as a demand sharply cut measured hedging on
             subjective prompts across three small models; objective prompts
             showed a floor effect. Treat as suggestive, not as evidence of a
             rate.
Locators:    Results on subjective vs objective questions; effect-size
             discussion.
Quote:       Reported drop on subjective questions from 2.38 to 0.43 (its own
             hedging scale), "Cohen's d = 2.67," n=900. Do not carry these
             numbers into the article as authoritative.
```

## Contradictions

The commission's framing is that the model "withholds a stance it is capable of
taking" even when "the question admits" an answer. Four findings complicate that
and the editor should weigh them.

1. Opposite pressure on scored tasks. Kalai et al. (2509.04664) document the same
   training pipeline pushing toward confident guessing, not hedging, wherever a
   benchmark grades answers right/wrong with no credit for abstention. So the
   direction of the bias is task-dependent: hedging dominates on open-ended,
   advice-shaped, or contested prompts; overconfident guessing dominates on
   closed factual questions. A blanket "assistants hedge" claim is too broad.
   The lesson should scope the behavior to the prompt types where it actually
   appears.

2. Frontier models in 2026 hedge little on some measures. In the human-rights
   study (2502.19463) Claude Sonnet 4 hedged on 2.4% of identities; Anthropic's
   even-handedness scores sit at 94-97% for top models. The student study finds
   hedging on subjective prompts nearly vanishes under a demanding prompt. Labs
   have actively engineered hedging down, so the "it depends" default is weaker
   and more prompt-sensitive than the framing implies. The behavior is real but
   not uniform.

3. Hedging is sometimes correct design, not a failure. The Model Spec ranks a
   hedged right answer above no answer and far above a confident wrong one, and
   Anthropic's "professional reticence" on hot-button topics is intentional. On
   a genuinely contested normative question there may be no single correct stance
   to withhold. The defensible target for the lesson is the overshoot InstructGPT
   4.3 names, hedging on questions with "one fairly clear answer," not all
   non-commitment. The angle holds if it distinguishes the two; it overstates if
   it treats every hedge as a suppressed stance.

4. No source decomposes the three steps. Nothing I found measures how much of a
   given hedge comes from base-rate completion versus reward-model preference
   versus safety tuning. The commission already marks this as open; the evidence
   confirms it is open. Any sentence assigning a share to one step would be
   unsupported.

## Numbers

```text
Figure: hedged right answer > no answer > hedged wrong answer, in OpenAI's
        preference ranking of answer types
Owner:  OpenAI Model Spec (2025-12-18)
Scope:  A design ranking, not a measured rate. Applies to how the policy wants
        the model to trade confidence against correctness.
```

```text
Figure: reward model trained on all pairwise comparisons from K responses,
        K between 4 and 9 per prompt
Owner:  Ouyang et al. 2022 (InstructGPT), Sec 3.5
Scope:  Reward-model training setup; not a rate of hedging.
```

```text
Figure: verbalized confidence cuts expected calibration error by a relative ~50%
Owner:  Tian et al. 2023 (2305.14975)
Scope:  On TriviaQA, SciQ, TruthfulQA, for RLHF models including ChatGPT/GPT-4;
        relative reduction versus the model's own conditional probabilities.
```

```text
Figure: post-training reduces calibration on MMLU (shown as a plot, no ECE value)
Owner:  OpenAI GPT-4 Technical Report, Fig 8
Scope:  A subset of MMLU; pre-training vs post-training GPT-4. There is no single
        numeric error to quote; describe the two plots or the stated direction.
```

```text
Figure: hedging rate 2.4% (Claude Sonnet 4) to 28.6% (Gemini 2.5 Pro)
Owner:  Hedging and Non-Affirmation (2502.19463)
Scope:  Share of 205 identities on which each model hedged, over human-rights
        prompts from UDHR Articles 2-21; 4,738 prompts per model, 7 models.
        Domain-specific; not a general hedging rate.
```

```text
Figure: non-affirmation rate 2.4% (Gemini 2.5 Pro) to 27.7% (Mistral-7B)
Owner:  Hedging and Non-Affirmation (2502.19463)
Scope:  Same study and denominator as above. Non-affirmation is scored
        separately from hedging.
```

```text
Figure: political even-handedness: Claude Opus 4.1 95%, Claude Sonnet 4.5 94%;
        Gemini 2.5 Pro 97%, Grok 4 96%, GPT-5 89%, Llama 4 66%
Owner:  Anthropic, "political even-handedness"
Scope:  Anthropic's own automated even-handedness evaluation across many
        political stances. A vendor-run benchmark; read as such.
```

## Source assets

```text
Asset: GPT-4 Technical Report, Figure 8, the two side-by-side calibration plots
       (pre-trained vs post-trained GPT-4 on an MMLU subset), with the dashed
       perfect-calibration diagonal.
Shows: RLHF bends stated confidence off the diagonal, so the same model that was
       calibrated before tuning is no longer calibrated after. This carries the
       "tuning distorts confidence" point better than prose.
Crop:  Must keep both panels, the diagonal reference line, and both axis labels
       (confidence vs accuracy). Do not crop to one panel; the comparison is the
       evidence.
```

```text
Asset: Gao et al. (2210.10760) overoptimization curve, the gold-reward score
       plotted against optimization distance (it rises, peaks, then falls).
Shows: The Goodhart shape: chasing the proxy reward helps, then hurts. Grounds
       why optimizing a rater-derived signal drifts a model past what raters
       wanted.
Crop:  Keep the peak and the descending tail; a crop that omits the downturn
       loses the whole point. Keep the axis labels (gold reward vs KL /
       optimization).
```

```text
Asset: The Model Spec answer-type ranking line itself
       ("confident right answer > ... > confident wrong answer").
Shows: The deliberate preference ordering in the policy's own words. Works as a
       pull-quote or a simple ordered strip, not a chart.
Crop:  Reproduce the full ordering; a partial ranking misstates the policy.
```

```text
Asset: Per-model hedging rates from 2502.19463 and the even-handedness scores
       from Anthropic.
Shows: How much models differ. Best rendered as the article's own honest chart
       from the reported numbers, not lifted from either source, and captioned
       with the narrow domain (human-rights prompts; vendor evaluation).
Crop:  None. Build from the figures in Numbers, label the domain in the caption.
```

## Discarded

```text
URL: https://arxiv.org/abs/2505.12843 (Bias Fitting to Mitigate Length Bias):
     length bias is a real reward-model artifact but a different one; the lesson
     is about non-commitment, not verbosity. Available if the writer wants to
     note that reward models also reward length.
URL: https://www.globalwitness.org/en/campaigns/digital-threats/greenwashing-and-bothsidesism-in-ai-chatbot-answers-about-fossil-fuels-role-in-climate-change/
     relevant false-balance example, but the page returned 403 through the proxy
     and I could not read the passage, so I will not cite it. Recorded here as a
     lead, not evidence; the even-handedness and hallucination primaries already
     carry the false-balance tension.
URL: https://openai.com/index/why-language-models-hallucinate/ : the blog
     landing page 403'd; the underlying paper (2509.04664) is readable and cited
     instead. Same content, citable home.
URL: https://en.wikipedia.org/wiki/False_balance : encyclopedic background on
     bothsidesism, not needed once the primaries define the behavior.
```
