# Evidence: the-evidence/proximal-policy-optimization (01)

The record supports every load-bearing claim in the commission. The 2017 paper
proposes one objective, the clipped surrogate (Equation 7), and recommends
epsilon = 0.2. It tests only two small reinforcement-learning benchmark
families: seven MuJoCo continuous-control tasks at one million timesteps each,
and 49 Atari games. It never touches language models. The bridge from this
algorithm to language-model tuning is later, separately authored work: Ziegler
et al. (2019) first ran PPO on a language model, and InstructGPT (2022) ran it at
175B scale. DPO (2023) removes the reinforcement-learning step; GRPO (DeepSeekMath,
2024) keeps PPO's clipped ratio but drops the value model. The paper's theory is
thin in a specific, checkable way: it proves nothing, states its objective is a
"lower bound," and picks its central constant with the word "say."

Where the record is thin, and where it complicates the angle: the paper's own
Atari result is split. PPO wins the fast-learning metric across 49 games but
loses the final-performance metric to ACER (28 games to 19). Two later studies
(Engstrom et al. 2020; Huang et al. 2022) argue that PPO's measured edge over its
predecessor comes largely from code-level implementation details rather than the
clipped objective itself. Both are recorded below in full under Contradictions.
The commission anticipated this ("search for what breaks the angle... its
RL-benchmark superiority was contested"), so the finding sharpens the lesson
rather than undermining it: the clipped objective is real and is what the paper
is famous for, but "PPO beat everything on the benchmarks" overstates a mixed
record.

One process note the editor should trust: the automated fetch summarizer
misreported two figures from the PPO paper (it claimed PPO "won 39/49" Atari
games and quoted the paper calling its update "a heuristic"). Neither is in the
paper. Every number below was read off the primary PDF's own tables and text, not
the summarizer.

## Sources

```text
URL:         https://arxiv.org/abs/1707.06347
Kind:        primary. Schulman, Wolski, Dhariwal, Radford, Klimov (OpenAI) are
             the authoring party; this paper owns the PPO algorithm, the subject
             of the lesson. Full text read from the arXiv PDF.
Establishes: The clipped surrogate objective, the recommended epsilon, the
             adaptive-KL alternative, the exact benchmark scope, the
             comparisons, and the absence of any theoretical guarantee.
Paraphrase:  Proposes a family of first-order policy-gradient methods. The
             probability ratio r_t(theta) = pi_theta(a_t|s_t) /
             pi_theta_old(a_t|s_t). The main objective (Eq. 7) takes the minimum
             of the unclipped ratio times advantage and a version where the ratio
             is clipped to [1-eps, 1+eps], forming a pessimistic lower bound that
             removes the incentive to move the ratio far from 1, which lets the
             policy take several epochs of gradient steps on one batch without
             the update running away. Recommends epsilon = 0.2. Offers an
             alternative adaptive-KL-penalty variant (Section 4) and reports it
             "performed worse than the clipped surrogate objective." Tested on 7
             MuJoCo tasks (1M timesteps) and 49 Atari games. On continuous
             control, PPO(clip) "outperforms the previous methods on almost all
             the continuous control environments" (TRPO, A2C, A2C+trust region,
             CEM, vanilla PG). On Atari it is better than A2C on sample
             complexity and "similarly to ACER though it is much simpler."
Locators:    Abstract; Eq. 6 (ratio), Eq. 7 (L^CLIP), p.3; "say, epsilon = 0.2"
             p.3; Section 4 (adaptive KL), p.4; Section 5 Algorithm 1, p.5;
             Section 6.1 + Table 1, p.5-6; Section 6.2 + Figure 3, p.6-7; Section
             6.4 + Table 2, p.8; Tables 3 and 5 (hyperparameters), p.10.
Quote:       "where epsilon is a hyperparameter, say, eps = 0.2." Also, on the
             predecessor it emulates: "to achieve our goal of a first-order
             algorithm that emulates the monotonic improvement of TRPO."
```

```text
URL:         https://arxiv.org/abs/1502.05477
Kind:        primary. Schulman, Levine, Moritz, Jordan, Abbeel (UC Berkeley) own
             the TRPO claim, which is the problem PPO simplified. Abstract read
             directly; the trust-region mechanism is also stated firsthand in the
             PPO paper's Section 2.2.
Establishes: What PPO drops. TRPO maximizes a surrogate objective subject to a
             hard KL-divergence constraint, giving a monotonic-improvement
             guarantee, solved with a second-order (conjugate-gradient) method.
Paraphrase:  TRPO is "an iterative procedure for optimizing policies, with
             guaranteed monotonic improvement." It constrains each update so the
             mean KL between old and new policy stays below delta, solved by
             conjugate gradient after a linear approximation to the objective and
             a quadratic approximation to the constraint. PPO replaces this hard
             constraint and second-order solve with first-order clipping.
Locators:    Abstract (TRPO); constraint and solver as restated in PPO paper Eq.
             3-4 and surrounding text, p.2.
Quote:       "We describe an iterative procedure for optimizing policies, with
             guaranteed monotonic improvement."
```

```text
URL:         https://arxiv.org/abs/1909.08593
Kind:        primary. Ziegler, Stiennon, Wu, Brown, Radford, Amodei, Christiano,
             Irving (OpenAI) own this result. Full text read. This is the
             earliest primary that runs PPO on a language model.
Establishes: The first documented step of the bridge from PPO-as-RL to
             PPO-as-language-model-optimizer, and the reward + KL-penalty setup
             that InstructGPT later inherited.
Paraphrase:  Fine-tunes a 774M-parameter GPT-2 with RL against a reward model
             trained from human preferences on four tasks (sentiment/descriptive
             continuation; TL;DR and CNN/Daily Mail summarization). The policy is
             trained with PPO. A KL penalty from the fine-tuned policy to the
             pretrained model is added into the reward, R(x,y) = r(x,y) - beta *
             log(pi(y|x)/rho(y|x)). Notes the honest failure that summarization
             models became "smart copiers" and that labelers could be gamed.
Locators:    Section 2, training step 3, p.3 ("Train pi via Proximal Policy
             Optimization"); Eq. 2 (KL-penalized reward), p.3; Section 2.2 (PPO2
             from OpenAI baselines, four PPO epochs per batch), p.3.
Quote:       "Train pi via Proximal Policy Optimization (PPO, Schulman et al.
             (2017)) with reward R from (2) on x ~ D."
```

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary. Ouyang et al. (OpenAI) own the InstructGPT result. Abstract
             read; PPO usage and model sizes confirmed from the PDF.
Establishes: That PPO is the RL optimizer inside the best-known RLHF pipeline,
             used at 175B scale, five years after the PPO paper and on a task the
             paper never tested.
Paraphrase:  Fine-tunes GPT-3 (1.3B, 6B, 175B) with a three-step pipeline:
             supervised fine-tuning, a reward model trained from human rankings,
             then RL against that reward model using PPO. Uses a per-token KL
             penalty from the SFT model and a "PPO-ptx" variant that mixes in the
             pretraining objective. Labelers prefer the 1.3B InstructGPT output
             to the 175B GPT-3 output.
Locators:    Abstract; Methods (RL step names PPO, Schulman et al. 2017);
             PPO-ptx variant described in the methods/objective section.
Quote:       "We fine-tune ... with reinforcement learning using the PPO
             algorithm."
```

```text
URL:         https://arxiv.org/abs/2305.18290
Kind:        primary. Rafailov, Sharma, Mitchell, Ermon, Manning, Finn (Stanford)
             own the DPO method. Abstract read directly; the DPO objective is
             also restated firsthand in DeepSeekMath Appendix A.1.4.
Establishes: One current alternative that removes PPO (and reinforcement
             learning) from preference tuning entirely.
Paraphrase:  Reparameterizes the RLHF reward so the optimal policy has a
             closed form, letting the standard RLHF problem be solved with a
             single classification-style loss on preference pairs. Removes the
             separate reward-model-then-RL loop, needs no sampling from the model
             during fine-tuning, and no significant hyperparameter tuning. It
             keeps the same preference model and the KL-to-reference objective
             that PPO-RLHF optimizes; it drops the reinforcement learning.
Locators:    Abstract; DPO pairwise loss restated in DeepSeekMath Eq. 12-14,
             p.29.
Quote:       "eliminating the need for sampling from the LM during fine-tuning or
             performing significant hyperparameter tuning."
```

```text
URL:         https://arxiv.org/abs/2402.03300
Kind:        primary. Shao et al. (DeepSeek-AI, with Tsinghua/Peking interns) own
             GRPO; this is the paper that introduces it. Full method read.
Establishes: The other current direction: keep PPO's clipped objective but
             remove its value model. This is the algorithm DeepSeek-R1 later used.
Paraphrase:  GRPO "foregoes the critic model, instead estimating the baseline
             from group scores." For each question it samples a group of outputs
             from the old policy, scores them with the reward model, and uses the
             group's mean (normalized by the group's standard deviation) as the
             baseline, so no separately trained value function is needed. It keeps
             PPO's clipped probability-ratio objective. It moves the KL penalty
             out of the reward and into the loss directly. The stated motive: in
             PPO the value function "is typically another model of comparable size
             as the policy," a memory and compute burden. Applying GRPO lifted
             DeepSeekMath-Instruct from 82.9% to 88.2% on GSM8K and 46.8% to 51.7%
             on MATH. The paper also frames SFT, RFT, DPO, PPO, and GRPO under one
             gradient template as "direct or simplified RL techniques."
Locators:    Section 4.1.1 "From PPO to GRPO," Eq. 1-3, p.11-13; Figure 4
             (PPO-vs-GRPO diagram), p.13; abstract and contributions, p.1-3;
             DeepSeekMath-RL results, Table 5, p.12.
Quote:       "we propose Group Relative Policy Optimization (GRPO), which obviates
             the need for additional value function approximation as in PPO, and
             instead uses the average reward of multiple sampled outputs, produced
             in response to the same question, as the baseline."
```

```text
URL:         https://arxiv.org/abs/2005.12729
Kind:        primary for its own experiment (Engstrom, Ilyas, Santurkar, Tsipras,
             Janoos, Rudolph, Madry, MIT), but it functions here as the strongest
             source against a naive reading of PPO's superiority. Abstract read.
Establishes: That PPO's measured advantage over TRPO is substantially due to
             implementation details outside the core clipped objective.
Paraphrase:  Studies "code-level optimizations": augmentations found only in
             implementations or described as auxiliary details. Finds they are
             responsible for most of PPO's cumulative-reward gain over TRPO and
             that they change how the methods behave. Implication: attributing
             PPO's benchmark wins to the clipping alone is not supported.
Locators:    Abstract; the two-part finding (a) and (b).
Quote:       "our results show that they (a) are responsible for most of PPO's
             gain in cumulative reward over TRPO, and (b) fundamentally change how
             RL methods function."
```

```text
URL:         https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/
Kind:        secondary. Huang, Dossa, Raffin, Kanervisto, Wang report on PPO from
             outside the authoring party (OpenAI), cataloguing what the paper left
             out. ICLR Blog Track, March 2022. Read directly.
Establishes: That reproducing PPO's reported performance needs many
             implementation details the paper does not state, reinforcing the
             Engstrom finding for the writer with a concrete count.
Paraphrase:  Catalogues 37 implementation details needed to reproduce PPO
             (13 core, 9 Atari-specific, 9 continuous-control, 5 for LSTM, 1 for
             MultiDiscrete actions). The clipped objective in the paper is a small
             part of what a working PPO implementation contains.
Locators:    Introduction and the enumerated detail sections.
Quote:       Presented as the article's own framing: reproducing PPO requires 37
             implementation details beyond the clipped objective described in the
             paper.
```

```text
URL:         https://arxiv.org/abs/2501.12948
Kind:        secondary here (context). DeepSeek-AI own the R1 result, but this
             record uses it only for the present-day-circulation point; the GRPO
             mechanics are cited to DeepSeekMath, which R1 itself cites. Abstract
             read; R1's body text was not fully verified (see limitation).
Establishes: That a PPO descendant (GRPO) is in high-profile live use as of
             January 2025.
Paraphrase:  Trains reasoning ability into an LLM through "pure reinforcement
             learning," using GRPO (cited to Shao et al. 2024). Confirms the
             algorithm lineage from the 2017 paper is still in active deployment.
Locators:    Abstract; GRPO cited to DeepSeekMath/Shao et al. 2024.
Quote:       "the reasoning abilities of LLMs can be incentivized through pure
             reinforcement learning."
```

## Contradictions

1. **The paper's Atari result is not a clean win for PPO.** Over 49 games and
   three trials (Table 2, p.8): on average reward across all of training PPO won
   30, ACER 18, A2C 1; but on average reward over the last 100 episodes ACER won
   28, PPO 19, A2C 1, one tie. PPO leads on fast learning and loses on final
   performance to ACER. The paper's own abstract concedes PPO is only "similarly
   to ACER" on Atari. A lesson that says PPO dominated the benchmarks is wrong
   about Atari; the honest claim is that PPO matched stronger methods while being
   much simpler.

2. **Two later studies attribute PPO's edge over TRPO to implementation, not the
   clip.** Engstrom et al. (2020) find code-level optimizations "are responsible
   for most of PPO's gain in cumulative reward over TRPO." Huang et al. (2022)
   catalogue 37 implementation details needed to reproduce PPO. Both cut against
   any claim that the clipped objective by itself is what made PPO win. They do
   not dispute that PPO is robust and simpler to tune, which is the paper's actual
   contribution.

3. **PPO's status as the RLHF workhorse is itself contested by the alternatives
   the commission asks about.** DPO removes reinforcement learning entirely and is
   widely adopted; GRPO keeps the clip but discards the value model. DeepSeekMath
   groups PPO with DPO and GRPO as one family of "direct or simplified RL
   techniques." So "PPO is still the workhorse" is true but eroding, and the
   lesson should present PPO as the incumbent being routed around, not as
   unchallenged.

4. **The paper offers no theoretical guarantee, by its own wording.** It proves
   no theorem. It calls its objective a "lower bound" / "pessimistic bound," says
   it "emulates the monotonic improvement of TRPO" rather than achieving it,
   chooses epsilon with "say, eps = 0.2," and calls the adaptive-penalty constants
   "chosen heuristically." This is the honest form of the "famously informal"
   characterization: intuition and experiments, not proofs. (The claim, seen in
   some secondary summaries and in the fetch summarizer's output, that the paper
   calls its update "a heuristic" in those words is not supported by the text.)

5. **The founding RLHF-with-PPO paper documents reward gaming.** Ziegler et al.
   report that pure RL fine-tuning produced summarizers that "degenerated to
   copying" and beat human reference summaries 96% of the time on TL;DR by
   exploiting what labelers checked for. A caution against treating PPO-RLHF as
   straightforwardly optimizing "what humans want."

## Numbers

```text
Figure: Clipped objective, L^CLIP(theta) = E_t[ min( r_t(theta) A_t,
        clip(r_t(theta), 1-eps, 1+eps) A_t ) ]
Owner:  PPO paper, Eq. 7, p.3
Scope:  r_t(theta) = pi_theta(a_t|s_t)/pi_theta_old(a_t|s_t); A_t is the
        advantage estimate; eps is the clip width.
```

```text
Figure: eps = 0.2 (recommended clip width)
Owner:  PPO paper, p.3 text and Table 3 usage
Scope:  Used for all MuJoCo comparison runs; Atari uses eps = 0.1 * alpha with
        alpha annealed 1 to 0 (Table 5).
```

```text
Figure: Surrogate-objective comparison, avg. normalized score over 21 runs
        (7 MuJoCo envs x 3 seeds), 1M timesteps
Owner:  PPO paper, Table 1, p.6
Scope:  No clip/penalty -0.39; clip eps=0.1 -> 0.76; clip eps=0.2 -> 0.82 (best);
        clip eps=0.3 -> 0.70; adaptive KL d_targ 0.003/0.01/0.03 ->
        0.68/0.74/0.71; fixed KL beta 0.3/1/3/10 -> 0.62/0.71/0.72/0.69.
        Scores shifted/scaled so random policy = 0, best = 1.
```

```text
Figure: MuJoCo benchmark scope: 7 tasks, 1,000,000 timesteps each, 3 seeds
Owner:  PPO paper, Section 6.1 and footnote 2, p.6
Scope:  HalfCheetah, Hopper, InvertedDoublePendulum, InvertedPendulum, Reacher,
        Swimmer, Walker2d (all "-v1"). MLP policy, two hidden layers of 64 units.
```

```text
Figure: MuJoCo PPO hyperparameters
Owner:  PPO paper, Table 3, p.10
Scope:  Horizon T = 2048; epochs = 10; minibatch = 64; gamma = 0.99;
        GAE lambda = 0.95; Adam stepsize 3e-4.
```

```text
Figure: Atari PPO hyperparameters
Owner:  PPO paper, Table 5, p.10
Scope:  Horizon T = 128; epochs = 3; minibatch = 32*8 (=256); actors = 8;
        clip = 0.1 * alpha; VF coeff c1 = 1; entropy coeff c2 = 0.01; alpha
        annealed 1 to 0.
```

```text
Figure: Atari games "won" over 49 games, 3 trials
Owner:  PPO paper, Table 2, p.8
Scope:  Metric (1) avg reward over all training: A2C 1, ACER 18, PPO 30, tie 0.
        Metric (2) avg reward over last 100 episodes: A2C 1, ACER 28, PPO 19,
        tie 1. Full per-game means in Table 6 (Appendix B, p.12).
```

```text
Figure: InstructGPT scale
Owner:  Ouyang et al. 2022, abstract and methods
Scope:  GPT-3 sizes 1.3B, 6B, 175B tuned with PPO; 1.3B InstructGPT preferred to
        175B GPT-3 by labelers.
```

```text
Figure: GRPO gains on DeepSeekMath-Instruct 7B
Owner:  DeepSeekMath, abstract and Table 5, p.1 and p.12
Scope:  GSM8K 82.9% -> 88.2%; MATH 46.8% -> 51.7% (chain-of-thought), after
        GRPO RL from a subset of instruction-tuning data.
```

## Source assets

```text
Asset: Figure 1, PPO paper (p.3). Two side-by-side plots of a single term of
       L^CLIP as a function of the probability ratio r: one for positive
       advantage (A>0), one for negative (A<0), each with a red dot marking the
       start point r = 1.
Shows: Exactly what clipping does. For A>0 the objective rises with r until
       1+eps and then flattens; for A<0 it falls until 1-eps and then flattens.
       This carries the worked-example intuition the lesson needs better than
       prose can.
Crop:  Must keep both panels, the r-axis tick marks at 1-eps, 1, 1+eps, and the
       red start dots. Omit nothing; the two panels only make sense together.
```

```text
Asset: Table 2, PPO paper (p.8). Games "won" by A2C / ACER / PPO on the two
       Atari scoring metrics.
Shows: The split result: PPO leads on the fast-learning metric, ACER on final
       performance. Carries Contradiction 1 in four numbers.
Crop:  Keep both metric rows and all four columns; the point is the reversal
       between the two rows.
```

```text
Asset: Figure 4, DeepSeekMath (p.13). Side-by-side schematic of PPO and GRPO.
Shows: PPO's pipeline includes a trained Value Model feeding GAE; GRPO's omits
       it and computes the baseline from a group of sampled outputs. Carries the
       "GRPO drops the critic" point at a glance.
Crop:  Keep both the PPO and GRPO rows and the "Value Model" box present in PPO
       and absent in GRPO; that contrast is the whole figure.
```

```text
Asset: PPO paper Figure 3 (p.7), learning curves on the 7 MuJoCo tasks for PPO,
       TRPO, A2C, A2C+trust region, CEM, vanilla PG.
Shows: Scale honesty: each x-axis runs to 1,000,000 timesteps. Useful only if
       the lesson wants to show the small-benchmark scale directly. Prose plus
       the Numbers section likely suffices; flagged, not recommended.
Crop:  If used, keep the "1000000" x-axis label visible so the scale reads.
```

## Discarded

```text
URL: https://ar5iv.org/abs/1707.06347 -> ar5iv.labs.arxiv.org : HTML conversion
     did not render the paper body through the fetch tool. Superseded by reading
     the arXiv PDF directly; not a citable source, only a failed access route.
```

```text
Fetch-summarizer output for the PPO PDF: rejected. It confabulated "PPO won
39/49" Atari games (the real Table 2 numbers are 30 and 19 depending on metric)
and a paper quote calling the update "a heuristic" (not in the text). All PPO
numbers in this record come from the primary PDF's own tables.
```

```text
Secondary explainer articles (Medium, blog write-ups of InstructGPT/PPO surfaced
in search): not cited. They repeat the primary papers without owning any claim; a
repetition supports only that a claim was made, not that it is true. The primaries
were available and were read instead.
```

```text
DeepSeek-R1 (arXiv:2501.12948) body text: not fully verified. The abstract was
read and confirms pure-RL scaling and the GRPO lineage (R1 cites Shao et al.
2024). The record therefore sources GRPO mechanics to DeepSeekMath, the paper
that owns them, and uses R1 only for the "still in live circulation" point. If the
writer wants to state R1-specific GRPO details, that passage must be verified
against R1's own Section 2 before publication.
```
