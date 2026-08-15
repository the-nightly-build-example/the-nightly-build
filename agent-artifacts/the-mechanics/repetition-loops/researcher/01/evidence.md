# Evidence: the-mechanics/repetition-loops (01)

The evidence supports the commissioned chain at every step except one, and the
one gap is the point the commission most wants marked as open. Holtzman et al.
own the two load-bearing claims: maximization decoding (greedy, beam) degenerates
into repetition where sampling methods do not, and the probability a model
assigns to a repeated phrase rises with each repetition (their Figure 4, a named
positive feedback loop). Xu et al. reproduce and quantify that rising-probability
curve on modern LMs, so the self-reinforcement claim rests on two independent
primaries, not one. The fixes each tie to a step and each has an owning primary:
top-k (Fan et al.), nucleus/top-p (Holtzman), the repetition penalty (Keskar et
al.), and two training-time methods (Welleck et al.'s unlikelihood, Xu et al.'s
DITTO). What is thin is the bottom of the chain. Why a trained model puts rising
probability on a continuation it just produced has no single settled account:
Welleck blames the likelihood objective, Fu et al. blame a structural trait of
language they call high inflow, and these are different explanations that do not
reduce to each other. Treat the self-reinforcement effect as measured fact and
its underlying cause as contested. One caution on the numbers: the papers measure
different models on different corpora with different repetition metrics, so the
figures below are directional across sources, exact only within each primary.

## Sources

```text
URL:         https://arxiv.org/abs/1904.09751
Kind:        primary. Owns the degeneration result and the self-reinforcement
             figure; published as a conference paper at ICLR 2020.
Establishes: (1) Maximization-based decoding (greedy, beam search) degenerates
             into bland, incoherent, repetitive text; sampling from the nucleus
             (top-p) does not. (2) The probability of a repeated phrase increases
             with each repetition, a positive feedback loop that holds for the
             vast majority of phrases tested. (3) A per-method repetition
             comparison (Table 1) on GPT-2 Large continuations.
Paraphrase:  Likelihood is a good training objective but a bad decoding
             objective. Searching for the most likely continuation drives the
             model into loops, because once a phrase repeats, the model raises
             the probability it will repeat again. Truncating the unreliable tail
             of the distribution and sampling (nucleus/top-p) restores
             human-like diversity and coherence.
Locators:    Abstract; Section 3 (maximization-based decoding); Figure 4 (the
             feedback-loop plot); Table 1 (decoding-method comparison).
Quote:       "The probability of a repeated phrase increases with each
             repetition, creating a positive feedback loop. We found this effect
             to hold for the vast majority of phrases we tested, regardless of
             phrase length or if the phrases were sampled randomly rather than
             taken from human text." (Figure 4 caption)
```

```text
URL:         https://arxiv.org/abs/1908.04319
Kind:        primary. Owns the training-side diagnosis and the unlikelihood
             objective; published at ICLR 2020. Authors: Sean Welleck, Ilia
             Kulikov, Stephen Roller, Emily Dinan, Kyunghyun Cho, Jason Weston
             (New York University; Facebook AI Research).
Establishes: (1) The likelihood objective itself, not only the decoding search,
             pushes probability mass onto sequences with repeats and frequent
             words. (2) Unlikelihood training lowers the probability of specified
             unwanted continuations during training and cuts repetition while
             holding perplexity.
Paraphrase:  Fixing repetition at decoding time treats a symptom. The model's
             token-level probabilities are themselves miscalibrated toward
             repeats, so even under sampling the token-repeat rate stays above
             human. Adding an unlikelihood term that penalizes repeated tokens
             and sequences during training moves those probabilities toward the
             human distribution.
Locators:    Abstract; results tables reporting seq-rep-4 and rep on Wikitext-103.
Quote:       "the likelihood objective itself is at fault, resulting in a model
             that assigns too much probability to sequences containing repeats
             and frequent words, unlike those from the human training
             distribution."
```

```text
URL:         https://arxiv.org/abs/2206.02369
Kind:        primary. Owns a measured self-reinforcement analysis on modern LMs
             and the DITTO training fix; published at NeurIPS 2022. Authors: Jin
             Xu, Xiaojiang Liu, Jianhao Yan, Deng Cai, Huayang Li, Jian Li.
Establishes: (1) Independent measurement that the probability of repeating a
             sentence rises almost monotonically with the number of prior
             repetitions, up to a ceiling. (2) The effect is stronger for
             sentences that already had a higher initial probability. (3) A
             single repetition in the context already raises the repeat
             probability in most cases (their IP1 metric exceeds 90% across
             corpora). (4) DITTO, a training method that teaches the model to
             decay repeat probability across repetitions.
Paraphrase:  Confirms Holtzman's feedback loop as a general, measurable property
             rather than an anecdote, and characterizes its shape: monotone rise,
             a ceiling, and dependence on the starting probability. Their fix
             manufactures pseudo-repetitive training data and penalizes the model
             for letting repeat probability climb.
Locators:    Analysis section on the self-reinforcement effect (the IP/TP metrics
             and the probability-vs-repetition-count plot); method section (DITTO).
Quote:       "The probability of repetition increases almost monotonically with
             the number of historical repetitions" (analysis section), and
             "sentences with higher initial probabilities usually have a stronger
             self-reinforcement effect."
```

```text
URL:         https://arxiv.org/abs/2012.14660
Kind:        primary. Owns a theoretical account of why repetition arises;
             published at AAAI 2021 (https://ojs.aaai.org/index.php/AAAI/article/view/17520).
             Authors: Zihao Fu, Wai Lam, Anthony Man-Cho So, Bei Shi.
Establishes: A Markov-model analysis with an Average Repetition Probability (ARP)
             and derived upper bounds, attributing repetition to a "high inflow
             problem": many words predict the same next word with high
             probability, so generation is easily pulled back to that word and
             loops.
Paraphrase:  Offers a cause located in the structure of language and its learned
             transition probabilities rather than in the training loss. If many
             predecessors funnel into one word (high inflow), the chain returns
             to it and repeats. Most existing fixes, in their framing, are
             implicitly minimizing an upper bound on ARP.
Locators:    Definition 2.3 (ARP); Theorem 1 and Corollaries 1.1 to 1.2
             (Section 2.2, the bounds and the inflow/outflow decomposition);
             Theorem 2 (Section 2.3, extension beyond the Markov case).
Quote:       Root cause stated as too many words "predicting the same word as the
             subsequent word with high probability," making it "easy to go back
             to that word and form repetitions."
```

```text
URL:         https://arxiv.org/abs/1909.05858
Kind:        primary. Owns the repetition-penalty decoding rule. Authors: Nitish
             Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong,
             Richard Socher (Salesforce Research). arXiv technical report, 2019.
Establishes: The penalized-sampling / repetition-penalty rule: discount the
             logits of already-generated tokens by a factor before the softmax,
             so previously used tokens are less likely to recur. Recommended
             factor near 1.2 with near-greedy sampling.
Paraphrase:  A decode-time fix aimed directly at the loop: divide the score of
             any token already in the generated set by theta before sampling.
             This lowers the odds of repeating used tokens without retraining.
Locators:    Section 4.1 (Sampling); the penalized-sampling equation with the
             indicator I(c) = theta if the token was already generated else 1.
Quote:       "We find that using a greedy sampling and theta approximately 1.2
             yields a good balance between truthful generation and lack of
             repetition."
```

```text
URL:         https://arxiv.org/abs/1805.04833
Kind:        primary. Owns the top-k random sampling decoding scheme in this
             lineage; published at ACL 2018. Authors: Angela Fan, Mike Lewis,
             Yann Dauphin (Facebook AI Research).
Establishes: Top-k random sampling (sample from the k most likely next tokens,
             k=10) as a decoding fix that beats beam search, which "tends to
             produce common phrases and repetitive text."
Paraphrase:  The earliest fix in the chain to trade maximization for restricted
             sampling. Beam search collapses to generic, repetitive output;
             sampling from a truncated top-k restores variety without admitting
             the long tail of implausible tokens.
Locators:    Section 5.4 (Generation), the top-k random sampling description.
Quote:       "We generate stories from our models using a top-k random sampling
             scheme... We randomly sample from the k=10 most likely candidates
             from this distribution." and beam search "tends to produce common
             phrases and repetitive text from the training set."
```

```text
URL:         https://huggingface.co/blog/how-to-generate
Kind:        secondary. Explanatory engineering write-up, not the owner of any
             mechanism claim. Author: Patrick von Platen (Hugging Face), 2020,
             updated 2023.
Establishes: Working-practitioner framing of the same behavior and fixes: greedy
             and beam search "start repeating"; top-k, top-p, and the no-repeat
             n-gram block are the standard counters. Useful for the concrete,
             reproducible transcript register the lesson wants.
Paraphrase:  Confirms the behavior is routine and shows the exact library knobs
             (no_repeat_ngram_size, top_k, top_p) a reader would meet. Repeats
             the primaries' claims; does not establish them.
Locators:    Sections on greedy search, beam search, and sampling.
Quote:       Repetition is "a very common problem in language generation in
             general and seems to be even more so in greedy and beam search."
```

```text
URL:         https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/
Kind:        secondary. Survey that catalogs and connects the decoding and
             training fixes. Author: Lilian Weng, 2021.
Establishes: A single map linking greedy/beam repetition to the four fixes
             (top-k, nucleus, penalized sampling, unlikelihood training) with the
             CTRL penalty and Welleck's method placed in context. Useful to check
             the lesson's fix-to-cause mapping against an independent synthesis.
Paraphrase:  Greedy search "tends to create repetitions of phrases, even for
             well-trained models"; decode-time methods (top-k, nucleus, penalized
             sampling) and training-time methods (unlikelihood) attack the same
             behavior from different points. Reports the primaries; owns nothing.
Locators:    Sections on decoding (penalized sampling) and on unlikelihood
             training.
Quote:       "Greedy search... tends to create repetitions of phrases, even for
             well-trained models."
```

## Contradictions

The primaries disagree about where repetition comes from, and this is the
decoding-cause-versus-training-cause split the commission asks to mark.

- **Decoding search vs. the training objective.** Holtzman frames degeneration
  as a property of maximization decoding: the same model, decoded by sampling
  from the nucleus, produces near-human repetition rates (Table 1: nucleus 0.36
  vs. human 0.28), which reads as a decoding problem with a decoding fix. Welleck
  argues the opposite emphasis: the likelihood objective itself miscalibrates the
  model's probabilities toward repeats, so decoding fixes mask a symptom while
  the token-level repeat rate stays above human even after the fix (their rep:
  0.627 baseline vs. 0.487 human). Both can hold at once, and the honest reading
  is that decoding controls whether the loop is entered while training controls
  the underlying bias. Neither claims a complete cure.

- **Objective vs. structure of language.** Fu et al. locate the cause in neither
  the search nor the loss but in the learned transition structure (high inflow),
  a trait they argue would produce repetition in a Markov generator regardless of
  objective. This is a third position, not a restatement of Welleck's.

- **The bottom step is genuinely open.** No source gives a single settled
  mechanism for why a trained transformer raises probability on its own recent
  output. Holtzman and Xu measure that it happens; Fu et al. and Welleck offer
  competing explanations for why. The lesson should present the measured effect
  as settled and the underlying cause as contested, and should not let any one
  paper's account stand in as the answer.

No source contradicts the core measured claims: that greedy/beam decoding loops
far more than sampling, and that repeat probability rises with each repetition.
Those are confirmed by two independent primaries each.

## Numbers

```text
Figure: 73.66% repetition (greedy), 28.94% (beam, b=16), 0.36% (nucleus p=0.95),
        0.28% (human), 0.22% (pure sampling), 0.28% (top-k=640)
Owner:  Holtzman et al. 2020, Table 1
Scope:  GPT-2 Large continuations of WebText prompts; the paper's Repetition
        metric (share of repeated content in a generation). The exact metric
        formula was not quotable from the parse and should be read off Section 4
        before the writer states a denominator; treat these as the paper's
        printed Repetition% figures.
```

```text
Figure: seq-rep-4: 0.442 (MLE baseline), 0.013 (unlikelihood token+seq),
        0.006 (human); token rep: 0.627 (MLE), 0.559 (unlikelihood), 0.487 (human)
Owner:  Welleck et al. 2020, results tables
Scope:  Transformer LM on Wikitext-103. seq-rep-4 is the fraction of duplicate
        4-grams at the sequence level; rep is the token-level repeat rate. The
        ~97% cut in seq-rep-4 is the headline reduction; the token-level rep gap
        to human narrows but does not close.
```

```text
Figure: repeat probability rises almost monotonically with repetition count to a
        ceiling; single-repetition trigger (IP1) exceeds 90% across corpora
Owner:  Xu et al. 2022
Scope:  Measured on neural LMs across several corpora. IP1 is the share of cases
        where one repetition in context raises the next-repeat probability.
        Confirms the shape of Holtzman's Figure 4 on modern models.
```

```text
Figure: repetition penalty theta approximately 1.2
Owner:  Keskar et al. 2019, Section 4.1
Scope:  Applied to the 1.63B-parameter CTRL model; the divisor on logits of
        already-generated tokens under near-greedy sampling.
```

```text
Figure: top-k with k = 10
Owner:  Fan et al. 2018, Section 5.4
Scope:  Story-generation model; the size of the truncated candidate set sampled
        from at each step.
```

## Source assets

```text
Asset: Holtzman et al. 2020, Figure 4 (the positive-feedback-loop plot: per-token
       probability of a repeated phrase against repetition number, rising curve).
Shows: The self-reinforcement claim in one image. This is the figure that carries
       step 3 of the chain better than any prose could.
Crop:  Must retain the rising-probability axis and the repetition-count axis and
       the label showing probability approaching its ceiling. Omit nothing that
       identifies the axes.
```

```text
Asset: Holtzman et al. 2020, Figure 1 (a concrete GPT-2 continuation under beam
       search visibly stuck repeating a phrase, beside human text).
Shows: The behavior itself, step 1, as a real transcript rather than a
       description. Good candidate for the opening concrete example.
Crop:  Keep the looped span intact so the repetition is legible; the prompt line
       can be trimmed if space demands, but the repeated phrase must survive.
```

```text
Asset: Holtzman et al. 2020, Table 1 (decoding methods vs. Repetition% and
       Self-BLEU).
Shows: Step 2 in one view: maximization rows (greedy 73.66, beam 28.94) against
       sampling rows (nucleus 0.36) and human (0.28). Makes the decoding contrast
       the surprise the headline could lead with.
Crop:  Retain the method column and the Repetition% column with the human row;
       other columns are optional context.
```

```text
Asset: Xu et al. 2022, the probability-vs-repetition-count figure.
Shows: Independent confirmation of Figure 4's shape on modern LMs, and the
       ceiling behavior. Useful if the lesson wants a second, newer witness.
Crop:  Keep both axes and the monotone curve; a multi-corpus panel can be reduced
       to one representative curve without loss.
```

```text
Asset: Welleck et al. 2020, results table (seq-rep-4 and rep across MLE,
       unlikelihood, human).
Shows: The training-side fix quantified, and that it narrows but does not close
       the token-level gap to human. Supports the "no complete cure" point.
Crop:  Retain the human, MLE-baseline, and unlikelihood rows for seq-rep-4 and
       rep; drop intermediate ablation rows.
```

```text
Asset: Keskar et al. 2019, Section 4.1 penalized-sampling equation.
Shows: The repetition penalty as an equation with the theta indicator. If the
       lesson shows any formula it is this one, but the commission says no code
       and the penalty is better stated in words; treat as reference, not a
       required visual.
Crop:  None recommended; prose statement preferred over reproducing the equation.
```

Fan et al. and the two secondaries: None found worth reproducing; their
contribution is textual.

## Discarded

```text
URL: https://arxiv.org/pdf/1904.09751 — PDF stream did not parse to text; used the
     ar5iv HTML rendering of the same paper (1904.09751) instead. Same document,
     readable route.
URL: https://openreview.net/pdf?id=sexfswCc7B — browser-verification wall blocked
     the fetch; the same paper reads cleanly at arxiv.org/abs/2206.02369, recorded
     as the source's own page.
URL: https://arxiv.org/pdf/2012.14660 — PDF stream did not parse; used the ar5iv
     HTML of the same paper. Not a rejection of the source, only of the transport.
URL: https://aclanthology.org/2025.naacl-short.41.pdf (Repetition Neurons) — a
     newer mechanistic-interpretability angle on repetition; read far enough to
     confirm it would support the "cause still open" boundary, but not needed to
     meet the policy and outside the confirmed chain. Left available if the writer
     wants a 2025 witness that the cause is still under active study.
URL: https://arxiv.org/abs/2310.14971 (Penalty Decoding) and
     https://arxiv.org/abs/2409.19877 (Contrastive Token Learning) — later
     decode-time and training tweaks; downstream of the chain, add nothing the
     owning primaries do not already establish.
```
