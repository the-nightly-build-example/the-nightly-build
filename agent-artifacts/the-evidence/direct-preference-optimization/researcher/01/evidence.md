# Evidence: the-evidence/direct-preference-optimization (researcher 01)

The evidence firmly supports the paper's method claim and its measured results.
The DPO paper (Rafailov et al., NeurIPS 2023) does reparameterize the RLHF reward
so the optimal policy has a closed form, collapsing preference tuning into one
binary-cross-entropy loss on preferred/dispreferred pairs, with no separately
trained reward model and no PPO loop. Its three tasks, model sizes, and win-rate
numbers are verified firsthand against the paper's own figures and tables. What
the evidence supports only narrowly is the leap from those numbers to "DPO
replaced RLHF." The paper's "as good as or better than PPO" claim rests on small
models (774M-6B), GPT-4-as-judge win rates, and — for dialogue — a PPO baseline
the authors could not get to work at all, so they substituted Best-of-128 as a
"rough proxy." The present-day counter-evidence (Xu et al., ICML 2024) is equally
firsthand: on harder tasks PPO still wins by wide margins and DPO is provably
prone to favoring responses outside its preference data. The record is thin on
one thing only: a single independent secondary carries the "how it spread"
context; adoption itself is sourced to a primary model report (Zephyr).

## Sources

```text
URL:         https://arxiv.org/abs/2305.18290
Kind:        primary — the paper the lesson teaches; owns the DPO method and every
             DPO result. Authored by its inventors, who have a stake in the claim.
Establishes: DPO's method and results firsthand.
Paraphrase:  "Direct Preference Optimization: Your Language Model is Secretly a
             Reward Model," Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano
             Ermon, Christopher D. Manning, Chelsea Finn (Stanford; Mitchell and
             Sharma listed as equal contribution). Submitted arXiv 29 May 2023;
             v3 29 Jul 2024; published NeurIPS 2023. The paper introduces a new
             parameterization of the RLHF reward model that lets the optimal
             policy be written in closed form, so the standard RLHF objective is
             solved "with only a simple classification loss." The optimal policy
             is pi_r(y|x) = (1/Z(x)) pi_ref(y|x) exp(r(x,y)/beta) (Eq. 4); the
             reward is reparameterized as r(x,y) = beta log(pi_r/pi_ref) + beta
             log Z(x) (Eq. 5); substituting into a Bradley-Terry preference model
             cancels the intractable partition function Z(x) and yields the DPO
             loss (Eq. 7), a binary cross-entropy on the difference of implicit
             rewards for the preferred (y_w) and dispreferred (y_l) response. No
             separate reward model, no reinforcement-learning loop, no sampling
             from the policy during training. Three tasks: (1) controlled
             sentiment on IMDb movie-review prefixes, preference pairs labeled by
             a pretrained sentiment classifier, SFT/policy = GPT-2-large; (2)
             Reddit TL;DR summarization using the human preferences from Stiennon
             et al. 2022, 6B-parameter model; (3) single-turn dialogue on the
             Anthropic Helpful-Harmless set (~170k dialogues), Pythia-2.8B.
Locators:    Abstract; Section 4 (Eqs. 4, 5, 7); Section 6 and its Figures 2-3,
             Tables 1-2.
Quote:       "we introduce a new parameterization of the reward model in RLHF that
             enables extraction of the corresponding optimal policy in closed
             form, allowing us to solve the standard RLHF problem with only a
             simple classification loss."
Quote:       "fine-tuning with DPO exceeds PPO-based RLHF in ability to control
             sentiment of generations, and matches or improves response quality
             in summarization and single-turn dialogue while being substantially
             simpler to implement and train."
```

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary — owns the InstructGPT RLHF recipe DPO simplifies. Authored
             by OpenAI, the party that built and ran the pipeline.
Establishes: what RLHF's pipeline was, firsthand.
Paraphrase:  "Training language models to follow instructions with human
             feedback," Long Ouyang et al., OpenAI, 2022 (NeurIPS 2022). The
             three-step RLHF pipeline DPO removes two-thirds of: (1) supervised
             fine-tuning (SFT) on labeler demonstrations; (2) train a separate
             reward model on human rankings of model outputs; (3) optimize the
             policy against that reward model with PPO reinforcement learning,
             regularized toward the SFT model. Model sizes 1.3B, 6B, 175B.
             Headline: labelers prefer the 1.3B InstructGPT's outputs to the 175B
             GPT-3's, despite 100x fewer parameters. This is the concrete "reward
             model + PPO loop" that DPO's single classification loss replaces.
Locators:    Abstract; Section 3 (Methods, steps 1-3); Figure 2.
Quote:       "outputs from the 1.3B parameter InstructGPT model are preferred to
             outputs from the 175B GPT-3, despite having 100x fewer parameters."
```

```text
URL:         https://arxiv.org/abs/1706.03741
Kind:        primary — owns the preference-learning origin (learn a reward from
             human comparisons, then optimize it with RL). Authored by the
             OpenAI/DeepMind team that ran it.
Establishes: the reward-from-comparisons idea both RLHF and DPO inherit, firsthand.
Paraphrase:  "Deep reinforcement learning from human preferences," Paul F.
             Christiano and Dario Amodei (OpenAI); Jan Leike, Miljan Martic, Shane
             Legg (Google DeepMind); Tom B. Brown, 2017 (NeurIPS/NIPS 2017). A
             reward function is learned from non-expert human choices between
             pairs of short trajectory segments, then optimized by RL. Feedback
             was cheap: on the order of 700 human comparisons for MuJoCo
             locomotion and ~5,500 for Atari, i.e. feedback on under 1% of the
             agent's interactions, learning some novel behaviors from about an
             hour of human time. This is the "preferences from comparisons"
             ancestor of the pairwise data DPO trains on directly.
Locators:    Abstract; Section 1; experiments (MuJoCo/Atari query counts).
Quote:       "feedback on less than 1% of our agent's interactions with the
             environment."
```

```text
URL:         https://arxiv.org/abs/2404.10719
Kind:        primary — owns the DPO-vs-PPO counter-finding. Authored by the team
             that ran the comparison; carries the "does it still hold" angle.
Establishes: where PPO still beats DPO and why DPO is fragile, firsthand.
Paraphrase:  "Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study,"
             Shusheng Xu, Wei Fu, Jiaxuan Gao, Wenjie Ye, Weilin Liu, Zhiyu Mei,
             Guangju Wang, Chao Yu, Yi Wu (Tsinghua University; Shanghai Qi Zhi
             Institute; OpenPsi Inc.), ICML 2024. Theorem: the set of policies DPO
             can reach strictly contains PPO's, and DPO's loss can be minimized by
             a policy that puts high probability on out-of-distribution responses
             never seen in the preference data, because DPO has no on-policy KL
             constraint to hold it near the reference. Empirically, when the
             preference data is off the model's own distribution DPO degrades, and
             an added SFT step or iterative DPO narrows but does not close the gap.
             On hard benchmarks PPO wins outright: on CodeContests with
             CodeLlama-34B, PPO reaches 22.4% (10@1k), beating AlphaCode-41B's
             16.4%, versus DPO's 3.2%; on APPS PPO 44.4% vs DPO ~34% (pass@5); on
             SafeRLHF PPO's safety rate ~99.5% vs DPO ~95.8%; human raters
             preferred PPO to DPO 45% to 29% on HH-RLHF. The exact numbers should
             be re-read against the paper's own tables before print (fetched via
             the HTML mirror; treat the code figures as approximate pending a
             table check).
Locators:    Abstract; Section 4 (Theorem 4.1, OOD counter-example); Sections 5-6
             (SafeRLHF, HH-RLHF, APPS, CodeContests tables).
Quote:       "PPO is able to surpass other alignment methods in all cases and
             achieve state-of-the-art results in challenging code competitions."
```

```text
URL:         https://arxiv.org/abs/2310.16944
Kind:        primary — a model report that post-trains with DPO; owns its own
             adoption evidence. Authored by the team (Hugging Face) that built it.
Establishes: real open-model adoption of DPO, firsthand.
Paraphrase:  "Zephyr: Direct Distillation of LM Alignment," Lewis Tunstall,
             Edward Beeching, Nathan Lambert et al., Hugging Face, 2023. Starting
             from Mistral-7B, they apply distilled DPO (dDPO) on the UltraFeedback
             preference set (GPT-4-scored outputs, ~64k prompts), no human
             annotation and no sampling during fine-tuning. Zephyr-7B scores 7.34
             on MT-Bench, surpassing Llama2-Chat-70B (6.86), "the best open-access
             RLHF-based model" — a 7B DPO model beating a 70B PPO-RLHF model on
             that benchmark. Concrete evidence that DPO, not the RLHF pipeline,
             became the practical open-model recipe.
Locators:    Abstract; MT-Bench results table.
Quote:       "we apply distilled direct preference optimization (dDPO) to learn a
             chat model with significantly improved intent alignment... results on
             MT-Bench show that Zephyr-7B surpasses Llama2-Chat-70B, the best
             open-access RLHF-based model."
```

```text
URL:         https://cameronrwolfe.substack.com/p/direct-preference-optimization
Kind:        secondary — an explainer reporting on DPO's rise from outside the
             authoring parties. Its author neither wrote DPO nor built the models;
             it reports and interprets. Context only, per the citation standard.
Establishes: that DPO became a standard/default post-training method and the
             shape of the DPO-vs-PPO debate — as reported, not owned.
Paraphrase:  Cameron R. Wolfe, Ph.D., Senior Research Scientist at Netflix,
             "Direct Preference Optimization," published 28 Jul 2025. Characterizes
             DPO as a simpler alternative to RL-based alignment that "democratized"
             post-training and "become a standard post-training algorithm that is
             actively used by several popular LLMs," while noting that studies find
             a performance gap can persist between offline methods like DPO and
             online PPO-RLHF. Use for the spread-and-debate framing, not for any
             number.
Locators:    Introduction; sections on DPO vs RLHF and the DPO/PPO gap.
Quote:       "DPO... [has] allowed it to become a standard post-training algorithm."
```

## Contradictions

- The commission's "replaced RLHF" framing versus the DPO paper's own scope. The
  paper claims parity-or-better with PPO on three tasks at small scale
  (GPT-2-large, a 6B model, Pythia-2.8B), judged by GPT-4 win rates, not a general
  proof that DPO equals PPO. The strongest "DPO beats PPO" result (sentiment) uses
  a synthetic ground-truth reward, not human preference. Cite the paper's own
  words before writing "replaced."

- The DPO paper's dialogue comparison is not really a DPO-vs-PPO comparison. The
  authors report they were "unable to find a prompt or sampling temperature" at
  which their PPO model beat the base Pythia-2.8B, so they used Best-of-128 as "a
  rough proxy for PPO-level performance." On the paper's hardest task, the head-to-
  head against PPO is a substitution, not a measurement. This is internal to the
  primary and undercuts the broad "matches PPO" reading from inside the paper
  itself.

- DPO paper (2023) versus Xu et al. (2024) on whether DPO equals PPO. DPO reports
  win-rate parity or better on its three tasks; Xu et al. prove DPO can exploit
  out-of-distribution responses and show PPO winning by large margins on code
  (CodeContests 22.4% vs 3.2%) and leading on safety and human preference. Both
  are firsthand. They do not contradict on facts — they measure different tasks at
  different scales — but they contradict on the interpretation the commission must
  arbitrate. The honest present-day reading: DPO won adoption for its simplicity
  (Zephyr), yet PPO still leads where responses drift outside the preference data.

- Not every follow-up sides with Xu et al. The secondary notes DPO remains widely
  used and effective; several groups report DPO competitive with PPO when the
  preference data matches the model's distribution and tuning is careful. The gap
  is real but contested and task-dependent, not a settled "PPO wins."

## Numbers

```text
Figure: TL;DR summarization win rate vs human-written summaries, DPO ~61% at temp 0.0
Owner:  DPO paper (Rafailov et al.), Figure 2 right
Scope:  GPT-4 as judge; Reddit TL;DR test posts; 6B model; win rate against
        reference human summaries at sampling temperature 0.0
```

```text
Figure: TL;DR summarization win rate, PPO 57% at its best temperature (0.0)
Owner:  DPO paper, Figure 2 right / Section 6
Scope:  same GPT-4-judged TL;DR setup; PPO at its optimal sampling temperature
```

```text
Figure: Out-of-distribution (CNN/DailyMail) win rates — DPO 0.36 / PPO 0.26 at temp 0; DPO 0.31 / PPO 0.23 at temp 0.25
Owner:  DPO paper, Table 1
Scope:  models trained on Reddit TL;DR, evaluated on CNN/DailyMail news articles;
        GPT-4-judged win rate vs reference summaries
```

```text
Figure: Human preference for DPO over PPO summaries, 58%
Owner:  DPO paper, Table 2
Scope:  human raters, TL;DR summarization; validates GPT-4 as proxy (GPT-4 agrees
        with humans about as often as humans agree with each other)
```

```text
Figure: Model sizes — GPT-2-large (IMDb sentiment); 6B model (TL;DR); Pythia-2.8B (Anthropic HH)
Owner:  DPO paper, Section 6
Scope:  the full scale of the paper's evidence; all small by 2026 standards
```

```text
Figure: InstructGPT — 1.3B InstructGPT preferred over 175B GPT-3
Owner:  Ouyang et al. 2022, Abstract / Figure 2
Scope:  labeler preference on the OpenAI API prompt distribution; sizes 1.3B/6B/175B
```

```text
Figure: Christiano et al. — feedback on <1% of interactions; ~700 (MuJoCo) and ~5,500 (Atari) human comparisons
Owner:  Christiano et al. 2017, Abstract / experiments
Scope:  RL from human preferences on MuJoCo locomotion and Atari
```

```text
Figure: CodeContests 10@1k — PPO 22.4% vs DPO 3.2% (CodeLlama-34B); PPO > AlphaCode-41B (16.4%)
Owner:  Xu et al. 2024, results tables
Scope:  code-competition benchmark; re-verify exact cells against the paper's
        tables before print
```

```text
Figure: Safety rate — PPO ~99.5% vs DPO ~95.8% (SafeRLHF, Llama-2-7B); human win rate PPO 45% vs DPO 29% (HH-RLHF)
Owner:  Xu et al. 2024, results tables
Scope:  safety-alignment and helpfulness benchmarks; approximate pending table check
```

```text
Figure: Zephyr-7B MT-Bench 7.34 vs Llama2-Chat-70B 6.86
Owner:  Tunstall et al. 2023 (Zephyr), MT-Bench table
Scope:  MT-Bench chat benchmark; 7B DPO model vs 70B PPO-RLHF model
```

## Source assets

```text
Asset: DPO paper, Figure 2 (left: reward-vs-KL frontier for sentiment; right: TL;DR
       win-rate curves across sampling temperature for DPO vs PPO)
Shows: the two central comparisons in one figure — DPO's reward/KL frontier
       dominating PPO on sentiment, and DPO's summarization win rate exceeding
       PPO's best while staying flat as temperature rises (PPO's collapses)
Crop:  keep both axes and their labels and the DPO/PPO series legend; the
       temperature-robustness gap is the point, so do not crop to a single
       temperature
```

```text
Asset: DPO paper, Figure 3 left (GPT-4 win rates for Anthropic-HH dialogue, DPO vs
       Best-of-128, Preferred-completions, and other baselines)
Shows: DPO as the only efficient method beating the dataset's chosen responses on
       dialogue — but read against the caveat that no working PPO baseline appears
       here (Best-of-128 stands in for PPO)
Crop:  retain the baseline labels so the reader sees PPO is absent by proxy
```

```text
Asset: DPO paper, Table 1 (CNN/DailyMail out-of-distribution win rates, DPO vs PPO)
Shows: DPO holding a lead when the summarizer is moved to a new text distribution
Crop:  keep both temperature columns and both rows; four numbers, no trimming
```

```text
Asset: Xu et al. 2024, the CodeContests / APPS results table (PPO vs DPO vs
       DPO-Iter on code competitions)
Shows: the size of PPO's lead on hard reasoning tasks — the strongest single
       counter to "DPO equals PPO"
Crop:  keep the DPO, DPO-Iter, and PPO rows together so the gap and the partial
       recovery from iteration are both visible
```

```text
Asset: Zephyr paper, MT-Bench comparison table (Zephyr-7B vs Llama2-Chat-70B and
       other 7B models)
Shows: a DPO-trained 7B model outscoring a 70B PPO-RLHF model — adoption made
       concrete
Crop:  keep the parameter-count column beside the score so the 7B-beats-70B point
       lands
```

## Discarded

```text
https://arxiv.org/pdf/1706.03741 : same source as the Christiano abstract page; the
  PDF fetch returned unparsed binary, so affiliations and figures were read from
  the HTML mirror instead. Not a separate source — recorded only to note the
  transport, not the address.
https://www.superannotate.com/blog/direct-preference-optimization-dpo : surfaced in
  search as a DPO explainer; not opened. Redundant with the Cameron Wolfe secondary
  and vendor-marketing in origin; one independent secondary suffices.
https://medium.com/the-synaptic-stack/... and training.continuumlabs.ai/... :
  additional third-party DPO explainers surfaced in search, not opened; add no
  claim the primaries do not already own.
```
