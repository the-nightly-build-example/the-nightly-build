# Evidence: the-mechanics/output-diversity (01)

The evidence supports the commissioned chain firsthand and with measured numbers.
Four separate primaries show that post-training (RLHF and preference optimization)
lowers output diversity relative to the base or SFT model: Kirk et al. show
per-input diversity dropping and across-input "mode collapse" appearing under
RLHF; Padmakumar and He measure InstructGPT (but not base GPT-3) raising the
similarity between different writers' essays and cutting lexical and content
diversity; Wu et al. measure aligned models collapsing book-review sentiment onto
the most-positive bin (5.9% for base Llama-2 versus 82.1% for Llama-2-chat and
100% for GPT-3.5/GPT-4); Mohammadi measures lower token-level entropy in an
aligned model than its base. The mechanism is anchored in a primary: the
InstructGPT objective maximizes a learned reward, which concentrates probability
on high-reward completions, and adds a KL penalty that leashes the policy to the
SFT model rather than being the thing that narrows the distribution. The
temperature point is directly supported: Mohammadi finds the aligned model's
"attractor states" persist even at temperature T = 1, and Wu et al. find raising
temperature and adding diversity prompts moves Llama-2-chat only from 82.1% to
58.1% positive. The record is thin in two honest places. First, Kirk et al.
report their diversity results as figures with broken y-axes, so the record
cannot quote an exact before/after number from that paper; the hard numbers come
from Padmakumar/He and Wu et al. Second, the recurring-name instance (Elara) is
documented in community and press sources, not measured in a controlled study,
and the strongest firsthand instance (a Hacker News thread) also shows the
phenomenon is inconsistent across model versions. The evidence does not undermine
the commissioned angle, but one primary (Shypula et al.) sharpens it: when
diversity is scored only among high-quality outputs, preference-tuned models come
out higher, so the honest claim is that alignment narrows lexical and syntactic
variety and concentrates modes, not that it reduces every measure of diversity.

## Sources

```text
URL:         https://arxiv.org/abs/2310.06452
Kind:        primary. Kirk, Mediratta, Nalmpantis, Luketina, Hambro, Grefenstette
             and Raileanu own this analysis; it is the study the commission names.
             Published as a conference paper at ICLR 2024.
Establishes: That RLHF substantially reduces per-input output diversity relative
             to SFT across syntactic (EAD) and semantic (Sentence-BERT) measures,
             and that a smaller across-input diversity drop constitutes the first
             rigorous demonstration of "mode collapse" from RLHF specifically.
             Also that raising the KL penalty coefficient lowered diversity further
             rather than restoring it (Appendix I).
Paraphrase:  The authors evaluate SFT, reward-model Best-of-N, and full RLHF (PPO
             with a KL penalty to the SFT model) on TL;DR summarization and
             AlpacaFarm instruction-following, across LLaMA-7B and OPT. They
             measure per-input diversity (variety among outputs for one input) and
             across-input diversity (variety of single outputs over many inputs)
             with three metrics: EAD (distinct n-grams, syntactic), Sentence-BERT
             cosine (semantic), and NLI (logical). RLHF has "much lower output
             diversity than SFT" on the first two per-input metrics; NLI shows no
             meaningful difference. Across-input differences are "much smaller" but
             present, which they read as across-input mode collapse. They report
             diversity only for summarization, finding no meaningful differences on
             the instruction-following task because their metrics assume short
             outputs. Increasing the KL coefficient dropped both performance and
             per-input diversity.
Locators:    Abstract; Section 6.2 "Diversity" (p.9); Figures 5-6; Section 6.3
             "The impact of the KL penalty"; Appendix I; Appendix J.4 (OPT).
Quote:       "RLHF substantially decreases the diversity of outputs sampled for a
             given input compared to SFT across a variety of measures." "We believe
             that this is the first rigorous empirical demonstration of
             across-input mode collapse emerging from RLHF training specifically."
```

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary. Ouyang et al. (OpenAI) own the InstructGPT method and its RL
             objective; this is the primary for the KL-regularized RLHF objective.
Establishes: The exact reinforcement-learning objective post-training optimizes,
             and what the KL penalty does. Reward maximization is the term that
             concentrates probability on high-reward completions; the KL penalty is
             a constraint that keeps the policy near the SFT model, not the source
             of narrowing.
Paraphrase:  In the RL stage (PPO) the policy is trained to maximize the learned
             reward model's score for its outputs, minus a per-token KL penalty
             measuring how far the RL policy has moved from the SFT policy, plus an
             optional pretraining-gradient term (the "PPO-ptx" variant). The KL
             penalty is added "to mitigate over-optimization of the reward model" -
             a leash against the policy drifting too far from SFT, not the
             mechanism that concentrates the distribution.
Locators:    Section 3.5 "Models", RL subsection; objective is Equation (2).
Quote:       "objective(phi) = E_{(x,y)~D_pi} [ r_theta(x,y) - beta * log( pi^RL(y|x)
             / pi^SFT(y|x) ) ] + gamma * E_{x~D_pretrain}[ log(pi^RL(x)) ]"
             "we add a per-token KL penalty from the SFT model at each token to
             mitigate over-optimization of the reward model."
```

```text
URL:         https://arxiv.org/abs/2309.05196
Kind:        primary. Padmakumar and He (NYU) own this controlled experiment;
             published at ICLR 2024. Measured before/after numbers.
Establishes: That co-writing with a feedback-tuned (RLHF) model, InstructGPT,
             raises the similarity between different authors' essays and lowers
             lexical and content diversity, while the base model GPT-3 does not -
             isolating post-training as the cause with matched model contribution.
Paraphrase:  38 Upwork writers wrote argumentative essays in three conditions:
             solo, with base GPT-3 (davinci), and with InstructGPT (text-davinci-
             003). GPT-3 and InstructGPT contributed similar amounts of text (about
             35% of characters), yet only the InstructGPT group's essays became
             more homogeneous and less diverse, by a statistically significant
             margin (p < 0.05). Corpus homogenization (average pairwise similarity,
             Rouge-L on key points; higher = more similar) rose from 0.1536 (solo)
             and 0.1578 (GPT-3) to 0.1660 (InstructGPT). InstructGPT essays had the
             lowest fraction of unique n-grams at every n and the fewest distinct
             key points at every clustering threshold. The authors attribute this
             to InstructGPT contributing less diverse text, and note it "echoes
             prior results showing reduced diversity after reinforcement learning."
Locators:    Abstract; Sections 3-5; Section 4.2 (homogenization scores); Table 3a
             (n-gram diversity), Table 3b (key-point diversity); Figure 2.
Quote:       "writing with InstructGPT (but not the GPT3) results in a statistically
             significant reduction in diversity." "The corpus homogenization scores
             ... are 0.1536 for Solo, 0.1578 for GPT3 and 0.1660 for InstructGPT."
```

```text
URL:         https://arxiv.org/abs/2407.02209
Kind:        primary. Wu, Black and Chandrasekaran own the measurement of
             "generative monoculture." Submitted July 2024. Measured before/after
             numbers, and the temperature test.
Establishes: That aligned models sharply narrow an output attribute relative to
             the human source data, and that raising temperature or prompting for
             diversity does not restore the range.
Paraphrase:  The authors define generative monoculture as the generated
             distribution being statistically narrower than the source
             distribution for a task attribute. For book reviews they measure the
             share of samples whose average sentiment lands in the most-positive
             bin (0.95, 1.00]. Human source reviews: 2.8%. Base (pretrained)
             Llama-2: 5.9%, close to the source. Vicuna-13b (SFT): 44.7%.
             Llama-2-chat (RLHF): 82.1%. GPT-3.5 and GPT-4: 100%. They note the
             base-to-chat gap is "consistent with findings suggesting RLHF reduces
             output diversity compared with SFT." They then test four
             diversity-raising interventions (higher temperature, top-p, temperature
             decay, diversity prompts); the best case moves Llama-2-chat only from
             82.1% to 58.1% (T = 1.2, p = 1.0), "still large."
Locators:    Abstract; Section 5 (results); the 5.9%/44.7%/82.1% figures on p.14;
             the 82.1%->58.1% temperature result adjacent; GPT-3.5/GPT-4 100% figure
             p.12; Section 6-7 (mitigations); Figure 4.
Quote:       "The PT LLM Llama-2 has 5.9% of samples with average sentiment values
             falling in the range of (0.95,1.00], which is much closer to the source
             percentage of 2.8% than 44.7% for Vicuna-13b and 82.1% for Llama-2-chat."
             "for both GPT-3.5 and GPT-4, 100% of the samples have average positivity
             falling in (0.95,1.00]."
```

```text
URL:         https://arxiv.org/abs/2406.05587
Kind:        primary. Behnam Mohammadi owns this experiment. Submitted June 2024
             (later at ICLR 2025). Firsthand for the entropy and temperature points.
Establishes: That the aligned model's next-token distributions are more peaked
             (lower Shannon entropy) than the base model's, and, crucially, that the
             aligned model's "attractor states" persist even at high temperature
             (T = 1), whereas the base model does not get trapped at low temperature.
             This is the direct primary for "temperature widens sampling within a
             narrowed distribution but does not restore range."
Paraphrase:  Comparing Llama-2-7b-text (base) and Llama-2-7b-chat (aligned), the
             base model has higher mean token-level Shannon entropy and the aligned
             model lower (entropy is bounded above by log2(5) ~ 2.32 bits over the
             top-5 tokens studied). The base model's per-token probability is spread
             across tokens; the aligned model's is concentrated on one or two,
             producing the same tokens repeatedly. The aligned model's completions
             cluster into a few "attractor states"; perturbing the prompt pulls the
             model back to a familiar completion. The author states these attractors
             are qualitatively different from low-temperature behavior because they
             appear even at T = 1. He restates the Llama-2/GPT KL objective
             R(a|s) = R_c(a|s) - beta * D_KL(pi || pi_0) and reports that Ouyang et
             al. found increasing the KL coefficient beta was insufficient to recover
             NLP performance, so mode collapse persisted despite PPO-ptx.
Locators:    Abstract; "Syntactic Diversity and Average LLM Entropy" (Experiment 3);
             "Attractor States and Model Creativity" (Discussion); the RLHF/KL
             subsection quoting the Llama-2/GPT objective.
Quote:       "We observe these attractors even at high temperatures (e.g., T = 1) for
             the aligned model, whereas we do not observe similar attractors at low
             temperatures for the base model." "the aligned model, with its low
             token-level entropy, is incapable of producing semantically diverse
             outputs."
```

```text
URL:         https://arxiv.org/abs/2504.12522
Kind:        primary. Shypula, Li, Zhang, Padmakumar, Yin and Bastani own this
             measurement. COLM 2025. Read specifically for contradictory evidence.
Establishes: That preference-tuned (RL) models score LOWER on conventional lexical
             and syntactic diversity but HIGHER on "effective semantic diversity"
             (diversity counted only among valid, high-quality outputs), because
             preference tuning raises the share of usable outputs enough to offset
             per-sample sameness.
Paraphrase:  The authors measure diversity among only high-quality generations. On
             base-versus-instruct comparisons the effect favors instruct models for
             semantic diversity (Cohen's D ~ 1.33-1.34, p < 0.001) while a separate
             metric column shows negative effect sizes (instruct lower), the
             direction consistent with reduced lexical/syntactic variety. Their
             stated conclusion is that preference-tuned models "generate greater
             effective semantic diversity than SFT or base models," which cuts
             against a flat claim that RLHF reduces all diversity, while conceding
             that on unadjusted metrics "preference-tuned models - particularly
             those trained via RL - often produce outputs with lower diversity."
Locators:    Abstract; Section 3.1 (effective semantic diversity definition);
             Table 2 (Wilcoxon p-values and Cohen's D by comparison); Figure 1.
Quote:       "preference-tuned models generate greater effective semantic diversity
             than SFT or base models."
```

```text
URL:         https://news.ycombinator.com/item?id=42093394
Kind:        secondary/community. This thread is the citable public instance of the
             recurring-name phenomenon and its discussion; individual comments are
             anecdote, not measurement.
Establishes: That the "always names the heroine Elara" observation is widely
             recognized, and, honestly, that it is inconsistent across model
             versions - which the record carries as a limit on the anecdote.
Paraphrase:  The submission, dated November 9, 2024, is titled "When you ask ChatGPT
             'Tell me a story' it's always is about a girl named Elara." Commenters
             both confirm and complicate it: some report Elara repeatedly, others
             get different defaults by model (one reports GPT-4o returning "Aldric",
             o1-preview "Elara", 4o-mini "Lila", legacy GPT-4 "Elinor"; others cite
             Luna, Lyra, Mila). Some attribute the sameness to ChatGPT's low default
             temperature, a lay explanation the deeper sources correct.
Locators:    Submission title and date; top-comment cluster reporting per-model
             name variation and the temperature hypothesis.
Quote:       Submission title: "When you ask ChatGPT 'Tell me a story' it's always
             is about a girl named Elara."
```

```text
URL:         https://www.today.com/parents/family/elara-name-of-the-year-ai-rcna250091
Kind:        secondary. TODAY reports naming expert Laura Wattenberg's observation;
             it documents the phenomenon rather than owning a measurement.
Establishes: That the recurring-name pattern is documented beyond a single thread:
             a naming authority names Elara the 2025 "Name of the Year" for its
             ubiquity in AI writing across genres, from science fiction to math
             workbooks.
Paraphrase:  Rachel Paula Abrahamson, writing December 19, 2025, reports Laura
             Wattenberg's finding that AI systems reach for the name Elara "no matter
             the context, no matter the genre," including mundane settings like
             "math workbooks about Elara's adventures in geometry." Wattenberg's
             explanation is that the name is smooth and vowel-forward and carries no
             real-world association, which makes it broadly appealing and therefore
             a name a model "trained to please users" gravitates to. That last link
             (people-pleasing training producing the convergence) is her hypothesis,
             not a measured mechanism.
Locators:    Byline and date; Wattenberg's "no matter the genre" and "math
             workbooks" observations; her phonetic and "no baggage" explanation.
Quote:       "The AIs love to create characters named Elara." "Because none of us
             have ever actually met a person named Elara, it has no baggage."
```

## Contradictions

- **Effective, quality-adjusted diversity can rise, not fall (Shypula et al.
  2504.12522).** The strongest challenge to the commission's angle. When diversity
  is counted only among high-quality outputs, preference-tuned models beat base and
  SFT models on semantic diversity (Cohen's D ~ 1.34, p < 0.001), because alignment
  raises the fraction of usable outputs. This does not refute the lesson: the same
  paper confirms lower lexical and syntactic diversity in aligned models. It forces
  a precise claim - alignment narrows word- and structure-level variety and
  concentrates modes, and whether that counts as "less diverse" depends on whether
  you weight by quality. The writer should not state that RLHF reduces diversity on
  every measure.

- **The KL penalty is a leash, not the narrowing force, and cranking it up made
  things worse (Kirk et al. 6.3/Appendix I; Ouyang et al. via Mohammadi).** The
  commission frames the "KL-regularized RLHF objective concentrating probability."
  Read precisely, the reward-maximization term concentrates probability on
  high-reward modes; the KL penalty constrains how far the policy leaves SFT. Kirk
  et al. found that raising the KL coefficient lowered per-input diversity further
  rather than recovering it, and Ouyang et al. found raising it insufficient to
  recover NLP performance. So the KL term is not the diversity-preserving dial one
  might expect, and attributing the narrowing to the KL penalty itself would
  overreach. This maps onto the commission's own "open question" about which
  pressure dominates.

- **The recurring-name phenomenon is real but inconsistent (Hacker News thread).**
  Different model versions return different default names, and some observers pin the
  sameness on low default temperature. The lesson's own sources answer the second
  point (Mohammadi's T = 1 attractors; Wu et al.'s temperature sweep), but the
  writer should present Elara as a well-documented tendency, not a universal
  constant, and should not claim every model always returns the same one name.

- **Kirk's collapse is scoped, not total.** Within Kirk et al., the diversity drop
  is large per-input, "much smaller" across-input, and absent on the NLI (logical)
  metric, and it did not show on the instruction-following task with their metrics.
  The clean "distribution narrows" story is best supported for syntactic and
  semantic per-input diversity.

## Numbers

```text
Figure: 2.8% of human source book reviews land in the most-positive sentiment bin (0.95, 1.00]
Owner:  Wu, Black, Chandrasekaran, "Generative Monoculture" (arXiv 2407.02209)
Scope:  Share of review samples by average sentiment; human source distribution; baseline for the model comparisons below
```

```text
Figure: 5.9% (base Llama-2), 44.7% (Vicuna-13b, SFT), 82.1% (Llama-2-chat, RLHF), 100% (GPT-3.5 and GPT-4) in bin (0.95, 1.00]
Owner:  Wu et al. (arXiv 2407.02209)
Scope:  Same most-positive sentiment bin; base vs SFT vs RLHF vs proprietary aligned models; book-review generation
```

```text
Figure: Diversity prompt + temperature move Llama-2-chat from 82.1% to 58.1% in the most-positive bin (T = 1.2, p = 1.0)
Owner:  Wu et al. (arXiv 2407.02209)
Scope:  Best-case mitigation among four diversity-raising methods; still far above the 5.9% base share - temperature does not restore range
```

```text
Figure: Corpus homogenization (Rouge-L on key points, higher = more similar): 0.1536 Solo, 0.1578 GPT-3, 0.1660 InstructGPT
Owner:  Padmakumar and He (arXiv 2309.05196)
Scope:  Pairwise essay similarity within a topic, averaged; 38 writers, 10 topics; InstructGPT higher at p < 0.05
```

```text
Figure: Fraction of unique n-grams (Solo / GPT-3 / InstructGPT): n=1 0.119/0.116/0.115; n=2 0.602/0.585/0.579; n=3 0.898/0.886/0.869; n=4 0.973/0.967/0.953; n=5 0.991/0.988/0.977
Owner:  Padmakumar and He (arXiv 2309.05196), Table 3a
Scope:  Lexical diversity of the essay corpus per group; InstructGPT lowest at every n
```

```text
Figure: Fraction of unique key points at clustering thresholds 0.5/0.6/0.7/0.8 (Solo / GPT-3 / InstructGPT): 0.982/0.971/0.950; 0.941/0.927/0.877; 0.792/0.779/0.738; 0.543/0.514/0.494
Owner:  Padmakumar and He (arXiv 2309.05196), Table 3b
Scope:  Content (idea-level) diversity by agglomerative clustering of key points; InstructGPT lowest at every threshold
```

```text
Figure: Base-vs-instruct effect on semantic diversity, Cohen's D ~ 1.33-1.34, p < 0.001 (instruct higher); a separate diversity column shows negative D (instruct lower)
Owner:  Shypula, Li, Zhang, Padmakumar, Yin, Bastani (arXiv 2504.12522), Table 2
Scope:  Effective semantic diversity among high-quality outputs vs an unadjusted lexical/syntactic measure; base vs instruction-tuned models. Contradiction evidence.
```

```text
Figure: Maximum possible token-level Shannon entropy ~ 2.32 bits (log2 of the top-5 tokens studied); aligned model mean entropy lower than base, base "hot", aligned "cold"
Owner:  Mohammadi (arXiv 2406.05587)
Scope:  Per-token entropy over generated completions; base Llama-2 vs aligned Llama-2-chat. NOTE: the paper's exact mean-entropy values (base and aligned, with SD) could not be extracted - they render as figures/glyphs the text layer drops, so only the direction and the 2.32-bit ceiling are quotable from this source.
```

## Source assets

```text
Asset: Wu et al. (2407.02209) Figure 4 - histograms of average review sentiment for human source vs Llama-2 base vs Llama-2-chat, showing the distribution piling onto the most-positive bin
Shows: The narrowing of the output distribution in one picture; the base model tracks the human spread while the aligned model spikes at the positive end
Crop:  Keep the x-axis sentiment range and the base-vs-aligned pair; a crop must retain the y-axis so the reader sees the pile-up, not just a shape
```

```text
Asset: Kirk et al. (2310.06452) Figure 5 - per-input diversity bars (EAD, Sent-BERT, NLI) for RLHF vs SFT on summarization
Shows: RLHF below SFT on the syntactic and semantic bars, and level on NLI
Crop:  The y-axes are broken for visualization; any use must keep the axis break visible or state it in the caption, or the drop will read as larger than it is
```

```text
Asset: Padmakumar and He (2309.05196) Figure 2 - boxplots of essay homogenization for Solo, GPT-3, InstructGPT across topics
Shows: The InstructGPT group sitting higher (more similar essays) than Solo and GPT-3
Crop:  Keep all three groups side by side; dropping Solo or GPT-3 removes the control that isolates post-training as the cause
```

```text
Asset: Mohammadi (2406.05587) token-probability figure - stacked per-token probability bars for a base-model vs aligned-model completion of the same prompt
Shows: The base model's probability spread across tokens versus the aligned model's mass on one or two, the visual root of low entropy
Crop:  Keep both completions on the same token axis; the contrast is the point, so neither model can be cropped out
```

```text
Asset: InstructGPT (2203.02155) Equation (2) - the RL objective with the per-token KL term
Shows: Exactly what post-training maximizes and where the KL leash sits; usable as a set-piece if the lesson shows the objective at all
Crop:  If reproduced, reproduce the whole objective (reward, KL penalty, pretraining term); a partial equation misstates the mechanism
```

```text
Asset: Shypula et al. (2504.12522) Figure 1 - illustration of effective semantic diversity (valid vs invalid generations, semantic duplicates) for base/SFT/instruct
Shows: Why counting only valid outputs flips the diversity verdict; the contradiction made visual
Crop:  Retain the valid/invalid distinction; without it the higher instruct score looks like a plain contradiction rather than a quality-adjusted one
```

## Discarded

```text
URL: https://namerology.com/2025/12/15/2025-name-of-the-year-is-elara-the-favorite-name-of-ai/ : the page is JavaScript-rendered and returned no readable text on fetch; the TODAY article covers the same expert (Wattenberg) and resolves cleanly, so it stands in
URL: https://ar5iv.labs.arxiv.org/html/2406.05587 and https://arxiv.org/html/2406.05587v1 : no HTML render exists (redirects to abstract / 404); used the PDF's text layer instead, with the entropy-value limitation noted
URL: https://www.alphaxiv.org/abs/2406.05587 : third-party summary, not the source's own page; used only to locate figures, not cited
```
