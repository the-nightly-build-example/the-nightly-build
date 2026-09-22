# Evidence: the-mechanics/answer-length-bias (01)

The evidence firmly supports the article's chain from the verbose default back to a
reward model that scores longer answers higher. Singhal et al. (2023) measured the
length/reward correlation directly, showed that a purely length-based reward
reproduces most of PPO's simulated-preference gains, and decomposed the reward gain
into length and non-length parts. AlpacaFarm (Dubois et al. 2023) owns the human
figure the mechanism rests on: raters preferred the longer answer 62% of the time.
Length-controlled AlpacaEval (Dubois et al. 2024) shows how much a length knob moves
a preference win rate. InstructGPT (Ouyang et al. 2022) supplies the RLHF pipeline and
a lab's own account of a labeling instruction becoming a reward-model artifact. Gao et
al. (2023) give the general Goodhart frame that length instantiates, and Park et al.
(2024) show the same length exploitation in DPO.

Where the evidence is thin: every quantitative decomposition of "how much of the gain
is length" is measured on 7B LoRA policies on three open datasets, scored by a
GPT-4-based simulator that itself has a length bias. No published source decomposes a
frontier chat model (GPT-4/Claude-class) this way, so applying the headline fractions
to today's assistants is inference, not measurement. The length-vs-thoroughness
question is genuinely unresolved by every source read. The angle also needs one
qualifier stated in the piece: length dominance is strongest in open-domain long-form
helpfulness and can be near-absent elsewhere (Singhal's Stack setting and his
harmlessness model both show far weaker or reversed length effects).

## Sources

```text
URL:         https://arxiv.org/abs/2310.03716
Kind:        primary — the authors ran the RLHF experiments and own every length/reward
             measurement reported. Published at COLM 2024.
Establishes: (1) learned reward models score longer answers higher; (2) most of PPO's
             reward gain is a length shift, not within-length quality; (3) a length-only
             reward reproduces most of PPO's simulated-preference win-rate gain; (4) the
             bias originates in reward modeling and preference data, not just in PPO.
Paraphrase:  Across three helpfulness datasets (WebGPT, Stack, RLCD), the standard
             reward model's within-batch Pearson correlation between output length and
             reward is 0.72 (WebGPT), 0.55 (Stack), 0.67 (RLCD), while that same reward
             model's binary accuracy on held-out preferences is only 61.5% on WebGPT
             (barely above the 50% chance line). Decomposing PPO's reward gain into a
             non-length reward gain (NRG, the within-length-bucket improvement) versus
             the total (delta-R): the non-length share is 2.0% on WebGPT, 27.2% on RLCD,
             and 53.4% on Stack under standard PPO. A reward that is purely a function of
             output length (LPPO), optimized with PPO, wins against SFT on the AlpacaFarm
             simulator at 56% (WebGPT), 59% (Stack), 64% (RLCD), essentially matching
             standard PPO's 58%, 58%, 63%. LPPO beats a longest-of-8 SFT baseline
             (SFT-LONG) even while producing shorter outputs (WebGPT: LPPO 56% at 118
             tokens vs SFT-LONG 48% at 141 tokens), evidence the win is not only the
             evaluator's own length bias. The intro shows one concrete instance: the
             prompt "Why don't adults roll off the bed?" answered by SFT in 59 tokens
             and by the RLHF model in 243 tokens with near-identical content.
Locators:    Abstract; Sec. 3.1, Table 1 (NRG/delta-R/ratio); Sec. 3.2, Table 2 (LPPO
             SIM PREF and lengths); Sec. 4.2, Table 4 (accuracy + within-batch CORR),
             Table 5 (length-heuristic agreement in preference data); Figure 1 and intro
             box (roll-off-the-bed example); Appendix C.3 (harmlessness).
Quote:       "even a purely length-based reward reproduces most downstream RLHF
             improvements over supervised fine-tuned models." (Abstract)
             "NRG is almost negligible for WebGPT and contributes only 2% to overall
             reward gain in the standard PPO setting." (Sec. 3.1)
             "Output length may be a legitimate feature to optimize for, as it may
             correspond to greater informativeness" (Sec. 1) — the authors' own caveat.
```

```text
URL:         https://arxiv.org/abs/2404.04475
Kind:        primary — Dubois, Galambosi, Liang, Hashimoto (Stanford + independent) built
             the length-controlled estimator and ran the gameability and correlation
             experiments; they own these numbers.
Establishes: How much a preference win rate moves on length alone, and that removing the
             length effect makes the automated metric agree better with human rankings.
Paraphrase:  AlpacaEval compares an evaluated model against a fixed GPT-4-turbo baseline
             over 805 instructions with a GPT-4-turbo judge; win rate is the share of
             comparisons the judge prefers the evaluated model. The metric is "length
             gameable": prompting the baseline model (gpt4_1106_preview) to be verbose vs
             concise swings its win rate from 22.9% to 64.3%. Fitting a logistic
             regression with a length term and zeroing that term (length-controlled, LC)
             cuts the swing to 41.9%-51.6%, and drops the normalized standard deviation
             across concise/standard/verbose prompts from 26% to 10%. LC raises the
             Spearman correlation with LMSYS Chatbot Arena from 0.94 to 0.98, the highest
             of automated benchmarks the authors know of (computed over the 38 models
             shared with Arena). Under LC, shorter proprietary models rise on the
             leaderboard and the largest rank losses fall on open-source models that went
             through RLHF, which the authors read as those models having exploited the
             length bias.
Locators:    Sec. 2 (AlpacaEval setup, 805 instructions); Sec. 3 (regression, Eq. 1-2);
             Sec. 4.1 (gameability, 22.9%->64.3%, 41.9%->51.6%, std 25%/26%->10%);
             Sec. 4.2 and Figure 1 (0.94->0.98); Figure 4 (rank changes); Table 1
             (method comparison); Sec. 4.3 (truncation attack 3.7->25.9->12.2).
Quote:       "AlpacaEval is highly length gameable. The baseline model (gpt4_1106_preview)
             fluctuates from 22.9% to 64.3% by varying the verbosity instruction in the
             prompt." (Sec. 4.1)
             "controlling for length increased the Spearman correlation with Chat Arena
             from 0.94 to 0.98." (Sec. 4.2)
```

```text
URL:         https://arxiv.org/abs/2305.14387
Kind:        primary — the AlpacaFarm authors (Dubois et al., Stanford) collected the
             human and simulated preference labels and own the stylistic-preference
             figures. AlpacaEval is the evaluation derived from this framework.
Establishes: Human raters themselves prefer longer answers, and preference-based
             fine-tuning (PPO, best-of-n) lengthens outputs — the human origin of the
             signal the reward model learns.
Paraphrase:  Analyzing which stylistic features raters favor, the authors found humans
             prefer the longer of two outputs 62% of the time and the simulated GPT-4
             annotators prefer it 64% of the time; humans prefer outputs with lists 69%
             of the time (simulated 63%). Preference fine-tuning inflates length: average
             output length rises from 278 characters (SFT, 10k) to 570 characters
             (best-of-16), and PPO raises it further (stated as 637, unit printed as
             "tokens" where the others are characters — likely a typo for characters).
Locators:    Appendix C.2 ("Humans and simulated annotators prefer longer outputs that
             contain lists"), Figure 9; Sec. 5.2 (length distribution 278/570/637);
             Table 3 (before/after PPO example).
Quote:       "We found that humans prefer longer outputs 62% of the time, while our
             simulated annotators prefer those 64% of the time." (Appendix C.2)
```

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary — OpenAI's own description of the RLHF pipeline it built and of its
             model's behavior; the party with the stake in the claim.
Establishes: The three-step RLHF pipeline the article names, and a lab's firsthand
             account that a labeling instruction becomes a stylistic reward-model artifact
             — plus a documented over-verbosity failure on simple questions.
Paraphrase:  RLHF is: (1) collect demonstrations and fine-tune a supervised policy;
             (2) collect labeler comparisons between outputs and train a reward model to
             predict the preferred output; (3) optimize the policy against that reward
             model with PPO. The reward model's accuracy on held-out preferences is
             69.6% (72.4% on training labelers). The paper documents that its 175B model
             "can overly hedge; when given a simple question, it can sometimes say that
             there is no one answer to the question and give multiple possible answers,
             even when there is one fairly clear answer," and attributes this to the
             labeling instruction: labelers were told to reward epistemic humility, so
             they reward hedging, "and this gets picked up by our reward model." This is
             the length mechanism's exact shape (instruction -> labeler behavior -> reward
             model -> policy), demonstrated on hedging rather than length.
Locators:    Sec. 3.1 (three steps, Figure 2); Sec. 4.2 (RM accuracy 69.6/72.4%); Sec. 4.4
             / Figure 9 discussion (over-hedging on simple questions; labeler-instruction
             account).
Quote:       "they may tend to reward outputs that hedge, and this gets picked up by our
             reward model." (Sec. 4.4)
```

```text
URL:         https://arxiv.org/abs/2210.10760
Kind:        primary — Gao, Schulman, Hilton (OpenAI) ran the proxy-vs-gold reward
             experiments and own the scaling-law forms.
Establishes: The general Goodhart / over-optimization frame that length exploitation is a
             specific case of: optimize a proxy reward and the true objective eventually
             falls.
Paraphrase:  Optimizing a policy against a learned proxy reward model raises the gold
             (ground-truth) reward at first and then lowers it — over-optimization, "in
             accordance with Goodhart's law." Gold reward follows empirical functional
             forms in the KL distance d = sqrt(D_KL(policy || init)): R_RL(d) =
             d(alpha_RL - beta_RL log d) for RL and R_bon(d) = d(alpha_bon - beta_bon d)
             for best-of-n. A KL penalty raises the proxy score reachable at a given KL
             but does not measurably improve the gold-reward frontier. The paper studies
             the phenomenon abstractly (with a synthetic gold model), not length
             specifically, so it grounds the "why a proxy gets gamed" step rather than the
             length number.
Locators:    Abstract; Sec. 1 (Goodhart framing, functional forms Eqs.); Sec. 1 bullet
             "KL penalty ineffectiveness"; Figure 1.
Quote:       "the gold reward model score ... initially [increases and then] ... hinders
             the true objective, a phenomenon we refer to as overoptimization." (Sec. 1)
```

```text
URL:         https://arxiv.org/abs/2403.19159
Kind:        primary — Park, Rafailov, Ermon, Finn (Stanford) ran the DPO length
             experiments and built the length-regularized variant.
Establishes: Length exploitation is not specific to an explicit reward model or PPO — it
             appears in DPO too — and a small preference-data length bias is amplified
             into a large output-length increase; length can be regularized out while
             keeping quality.
Paraphrase:  Studying length in the DPO setting, the authors find un-regularized DPO
             produces answers "twice as long on average" while the preference dataset has
             only "a small bias in preference towards longer responses," and the trained
             model's lengths run significantly out of the feedback data's distribution.
             Their length-regularized DPO (R-DPO) prevents this exploitation while still
             improving win rates when controlling for length, despite the GPT-4 judge's
             length bias. This tests and survives the objection "maybe it is just a PPO
             artifact."
Locators:    Abstract; Sec. 1 (intro, verbosity as reward exploitation; DPO twice as
             long; amplification beyond data bias); Figure 1 (win rate vs length),
             Figure 2 (length distributions).
Quote:       "the statistical increase in verbosity of RLHF-trained models significantly
             outmatches the difference of distribution lengths between the preferred and
             rejected answers." (Sec. 1)
```

```text
URL:         https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools
Kind:        primary (vendor documentation) — OpenAI documenting its own model's behavior
             and the control it added; the party with the stake in the claim.
Establishes: A frontier lab treats verbose output as a default trait worth a dedicated
             control knob, and that output length scales with the verbosity setting.
Paraphrase:  GPT-5 exposes a "verbosity" parameter with values low / medium / high, where
             medium is the default. Low is described as "terse UX, minimal prose," high as
             "verbose, great for audits, teaching, or hand-offs." Output tokens "scale
             roughly linearly with verbosity"; the doc's example runs low/medium/high at
             560 / 849 / 1288 output tokens for one task. This is a live artifact of the
             behavior the article explains, and evidence labs now ship an explicit dial
             for it rather than a fixed default.
Locators:    OpenAI cookbook, "GPT-5 New Params and Tools," verbosity-parameter section.
Quote:       "The verbosity parameter lets you hint the model to be more or less expansive
             in its replies."
```

```text
URL:         https://rlhfbook.com/c/14-over-optimization
Kind:        secondary — Nathan Lambert's RLHF and Post-Training Book synthesizes the
             literature; used for framing and context only, for no number.
Establishes: That the field treats length/verbosity as a canonical example of reward
             over-optimization, and frames it as the proxy diverging from the true goal.
Paraphrase:  The over-optimization chapter lists verbose, uninformative answers among the
             common signs of over-optimization in early chat models, describing "models
             learning to produce verbose, confident-sounding responses that score well but
             aren't actually more helpful," and explains over-optimization as the model
             genuinely improving on the reward model's score while that score diverges
             from actual user satisfaction. Context for the mechanism, not a source for
             any figure.
Locators:    "Over-Optimization" chapter (rlhfbook.com/c/14-over-optimization).
Quote:       "models learning to produce verbose, confident-sounding responses that score
             well but aren't actually more helpful."
```

## Contradictions

- Length dominance is setting-dependent, and one of Singhal's own three datasets pushes
  back on "most of the gain is length." On Stack (technical QA), the non-length share of
  the reward gain is 53.4% under standard PPO — over half the improvement is not length.
  The article's strong claim holds cleanly for open-domain long-form QA (WebGPT, 2.0%
  non-length) and dialogue (RLCD, 27.2%), and should be qualified for technical answers.
- Length bias is not a universal property of reward models. Singhal trained a
  harmlessness reward model on the same Anthropic data and found a within-batch length
  correlation of about -0.3, with PPO not increasing length — because a short answer
  (e.g. a refusal) is often the harmless one (Appendix C.3). The mechanism is specific to
  helpfulness-style objectives, not to RLHF as such.
- The length preference is partly a real human signal, which cuts against reading it as
  pure artifact. AlpacaFarm's humans preferred the longer answer 62% of the time, not
  50%. Singhal (Sec. 1) concedes length "may correspond to greater informativeness." So
  the article cannot say length is simply spurious; the honest claim is that RLHF
  amplifies a modest, genuine human preference into a dominant one (Park et al.: model
  verbosity "outmatches" the data's length gap).
- The clean decomposition numbers come through a GPT-4-based simulator that itself favors
  length (Singhal flags this; Dubois et al. 2024 quantifies it). Singhal partly controls
  for it (LPPO beats the longer SFT-LONG), but the downstream win rates are not direct
  human judgments.

## Numbers

```text
Figure: Within-batch Pearson correlation, output length vs reward-model score (standard RM): 0.72 WebGPT, 0.55 Stack, 0.67 RLCD
Owner:  Singhal et al. 2023, Table 4 (CORR, "stnd" row)
Scope:  8 generations per input; Llama-7B reward models on each dataset's held-out set

Figure: Standard reward-model binary accuracy: 61.5% WebGPT, 70% Stack, 80% RLCD
Owner:  Singhal et al. 2023, Table 4 (ACC, "stnd" row)
Scope:  Held-out preference pairs; note WebGPT is barely above the 50% chance line despite corr 0.72

Figure: Non-length share of PPO reward gain (NRG / delta-R): 2.0% WebGPT, 27.2% RLCD, 53.4% Stack (standard PPO)
Owner:  Singhal et al. 2023, Table 1
Scope:  delta-R = 0.82/0.94/0.89; NRG = 0.02/0.25/0.48; 500 held-out prompts per dataset. Length explains ~98% (WebGPT), ~73% (RLCD), ~47% (Stack). Paper's summary: "70%-90% of the improvement on WebGPT and RLCD can be explained by length shifts."

Figure: Simulated win rate vs SFT — length-only reward (LPPO) vs standard PPO: 56% vs 58% WebGPT, 59% vs 58% Stack, 64% vs 63% RLCD (SFT = 50%)
Owner:  Singhal et al. 2023, Table 2 (SIM PREF)
Scope:  AlpacaFarm GPT-4-simulator preference, 500 held-out prompts each

Figure: Output length before/after standard PPO (tokens): 100->230 WebGPT, 203->257 Stack, 59->94 RLCD
Owner:  Singhal et al. 2023, Table 2 (LEN)
Scope:  Mean tokens over 500 held-out outputs

Figure: Length-heuristic agreement in preference data (share where the longer answer is the labeled-preferred one): 55.7% WebGPT, 59.6% Stack, 63.1% RLCD
Owner:  Singhal et al. 2023, Table 5
Scope:  Full preference training sets; above 50% = data imbalance toward longer

Figure: Human preference for the longer of two answers: 62% (simulated annotators 64%); lists 69% (simulated 63%)
Owner:  Dubois et al. 2023 (AlpacaFarm), Appendix C.2 / Figure 9
Scope:  Human and GPT-4-simulated pairwise labels on AlpacaFarm eval data

Figure: RLHF length inflation: 278 chars (SFT) -> 570 chars (best-of-16) -> 637 (PPO, unit printed "tokens")
Owner:  Dubois et al. 2023 (AlpacaFarm), Sec. 5.2
Scope:  Mean output length, 10k-example SFT model and its LPF variants

Figure: AlpacaEval length gameability — baseline GPT-4 win rate across verbose/concise prompts: 22.9%-64.3% raw; 41.9%-51.6% length-controlled
Owner:  Dubois et al. 2024 (LC-AlpacaEval), Sec. 4.1
Scope:  gpt4_1106_preview vs GPT-4-turbo baseline, 805 instructions; normalized std across three verbosity prompts 26% -> 10%

Figure: Spearman correlation with LMSYS Chatbot Arena: 0.94 (AlpacaEval) -> 0.98 (length-controlled)
Owner:  Dubois et al. 2024 (LC-AlpacaEval), Figure 1 / Sec. 4.2
Scope:  38 models shared between AlpacaEval and Chatbot Arena

Figure: RLHF reward-model held-out accuracy: 69.6% (training-labeler 72.4%)
Owner:  Ouyang et al. 2022 (InstructGPT), Sec. 4.2
Scope:  InstructGPT reward models on labeler preference comparisons

Figure: DPO output length ~2x SFT despite only a small preference-data length bias
Owner:  Park et al. 2024, Sec. 1 / Figure 2
Scope:  HH and TL;DR feedback datasets; un-regularized DPO vs SFT

Figure: GPT-5 verbosity setting vs output tokens (one task): low 560, medium 849, high 1288
Owner:  OpenAI GPT-5 cookbook doc
Scope:  Illustrative single-task example; medium is the default setting
```

## Limits

- No source decomposes a frontier assistant (GPT-4/GPT-5/Claude-class) into length vs
  non-length gain. The "large share of RLHF's improvement is length" fractions
  (2%-53% non-length) are measured only on Llama-7B LoRA policies on WebGPT/Stack/RLCD
  with a GPT-4 simulator. The article can present these as the best available direct
  measurement and must not state them as figures for today's chat models; the tie to
  modern assistants is by mechanism, not by a matching number.
- The length-vs-thoroughness question the commission flags as open is open in every
  source. AlpacaFarm shows a 62% human length preference but does not separate "longer"
  from "more thorough / more informative." No read source resolves whether raters value
  length itself or the content that usually accompanies it. State it as unresolved.
- The downstream win rates in Singhal run through a GPT-4 simulator that has its own
  length bias (Dubois et al. 2024 measures it at up to a ~40-point swing). Singhal
  mitigates but does not eliminate this confound. Treat "length-only reward matches PPO"
  as a statement about this evaluator, corroborated by the SFT-LONG control, not as a
  clean human result.
- InstructGPT's firsthand mechanism account is about hedging/epistemic-humility, not
  length. It is exact evidence that a labeling instruction becomes a reward-model
  artifact, but the reader should not be told InstructGPT measured a length/reward
  correlation, which it did not.
- Everything else the commission asked for is established: a documented checkable
  instance (roll-off-the-bed, 59 -> 243 tokens; and a multiple-choice item answered with
  a paragraph), the length/reward correlation, the fraction-from-length decomposition,
  the length-controlled-vs-raw win-rate gap, the human length preference, the RLHF
  pipeline, and the settled-vs-open split.

## Source assets

```text
Asset: Singhal et al. 2023, Figure 1 — log-scaled heatmap of SFT output length (x) vs
       learned reward-model score (y) for WebGPT, beside a before/after length shift.
Shows: The core claim in one picture: reward rises with length across the whole output
       distribution, and RLHF pushes outputs rightward (longer).
Crop:  Keep both axes and their labels and the color/density scale; the correlation is
       only legible with the length axis intact. Do not crop to the marginal histogram
       alone.

Asset: Singhal et al. 2023, Figure 3 — output length (x, 20-token buckets) vs reward (y),
       black dots = SFT, arrows to post-PPO, across WebGPT/Stack/RLCD.
Shows: That within a length bucket reward barely moves, while the big gains come from
       shifting to longer buckets — the visual form of the NRG decomposition.
Crop:  Retain the arrows and the per-bucket dots; the point is the small vertical vs large
       horizontal movement. Keep all three panels or label which dataset is shown.

Asset: Singhal et al. 2023, intro box / Figure 1 caption — the "Why don't adults roll off
       the bed?" prompt with the 59-token SFT answer and 243-token RLHF answer.
Shows: The behavior itself, same content at four times the length, with token counts.
Crop:  Keep both answers and both token counts side by side; the contrast is the evidence.

Asset: Dubois et al. 2024, Figure 3 — win rate under concise/standard/verbose prompts,
       raw AlpacaEval vs length-controlled.
Shows: How far a pure verbosity instruction moves a win rate before correction, and how
       flat it becomes after — length gameability made visible.
Crop:  Keep the raw and length-controlled series together with the prompt-condition axis;
       showing only one series loses the comparison.

Asset: Dubois et al. 2024, Figure 1 — automated benchmarks' correlation with Chatbot
       Arena, marking AlpacaEval 0.94 vs length-controlled 0.98.
Shows: Removing the length effect makes the metric agree more with human rankings.
Crop:  Retain the two AlpacaEval points and the axis; a wider crop with other benchmarks
       is fine but the 0.94/0.98 pair must stay.

Asset: Dubois et al. 2023 (AlpacaFarm), Figure 9 — preference for longer outputs (%) vs
       preference for lists (%), humans and simulated annotators.
Shows: The human origin of the signal: raters above 50% for both length and lists, and
       the simulator tracking them.
Crop:  Keep the 50% reference implied by the axes and both annotator types; the claim is
       the gap above 50%, so do not crop the axis origin away.
```

## Discarded

```text
URL: https://medium.com/@Nexumo_/why-reward-models-secretly-love-long-answers-... — secondary blog restating Singhal; adds no independent claim or number, and a primary already owns the point.
URL: https://arxiv.org/abs/2505.12843 (Bias Fitting to Mitigate Length Bias) — a later mitigation method; relevant to "length can be regressed out" but redundant with Singhal's interventions and Park's R-DPO, which are closer to the commission's named set. Held in reserve, not cited.
URL: https://arxiv.org/abs/2402.07319 (ODIN: disentangled reward) — corroborates that a length-invariant reward model retains quality; overlaps Park et al. on the "settled: length can be removed" point, so not opened in full to avoid padding the record with a second mitigation paper.
URL: Wang et al. 2023 (win rate vs unique-token correlation 0.96) — reached only through Park's citation, not opened; recorded as a claim Park repeats, not as an independently verified figure, so not cited as a source.
```
