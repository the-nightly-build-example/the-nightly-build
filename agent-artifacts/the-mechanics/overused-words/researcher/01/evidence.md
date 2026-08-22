# Evidence record: the-mechanics/overused-words (01)

The evidence supports the commission's causal chain with one sharp seam that must be preserved. The behavior is measured and firm: after late 2022 a specific set of style words rose abruptly in published text, quantified across two independent corpora (Kobak et al. on 14M PubMed abstracts; Liang et al. on machine-learning peer reviews). The settled cause is also firm: post-training with reinforcement learning from human feedback measurably narrows a model's output distribution and reduces diversity, shown directly by Kirk et al. against supervised fine-tuning and the base model. The open question is genuinely open and its leading hypothesis is weakly supported: the Nigerian/African-English annotator story originates as a journalist's speculation (Hern, Guardian), and the one peer-reviewed team that tested it empirically (Juzek & Ward) found their direct corpus test did not support it, while a separate model-surprisal test was only "consistent with" RLHF playing some role and behaved oddly for "delve" specifically. The consequence is well-sourced: word-frequency and stylometric detectors carry documented false-positive bias (Liang et al. 2023) and are defeatable by paraphrase (Sadasivan et al.). The record is thin in exactly one place the writer must flag: no source closes the open question, and the strongest empirical test of the annotator hypothesis is negative, not merely absent.

The proximate mechanism (a model emits a next-token probability distribution and a sampler draws from it) is not re-sourced here because the commission requires it to be linked, not re-taught. The library lessons that own it are confirmed below.

## Library lessons to link (confirmed via `nb history`, `NB_LIBRARY=/home/user/library-checkout`)

The writer links these at first use rather than re-teaching them.

```text
Path:  the-mechanics/autoregressive-generation   (2026-07-25)
Title: "The instant a model writes a token, it becomes fact"
Owns:  next-token / autoregressive generation — a model produces one token at a time and reads it back.

Path:  the-mechanics/sampling-temperature         (2026-07-21)
Title: "Two answers to one prompt diverge at a single draw"
Owns:  the next-token probability distribution and the sampler's draw; temperature reshaping the odds.
Note:  its own line — "The weights and the prompt fix a probability distribution over the next token,
       and a sampler's single draw from it is where two answers to one question come apart" — is the
       exact proximate-mechanism step (angle step 2). Link here, do not re-teach.

Path:  the-mechanics/formatting-defaults          (2026-08-14)
Title: "One line in the system prompt turns off the bullet points"
Owns:  post-training (a structure-rewarding stage) shaping output. Commission REQUIRES a Background link
       to this and forbids re-arguing "RLHF rewards format." This lesson extends the shared root cause
       from layout to word choice, then goes past it into distribution-narrowing.

Path:  the-evidence/instructgpt                    (2026-07-22)
Title: "A 1.3B model beat GPT-3 on the one metric OpenAI trained it to win"
Owns:  RLHF as the post-training recipe (the reward-model / preference-optimization stage).
Note:  RLHF is also touched in the-mechanics/sycophancy (reward model), the-evidence/deep-rl-from-human-
       preferences, and the-evidence/direct-preference-optimization. instructgpt is the RLHF lesson to link.
```

## Sources

```text
URL:         https://arxiv.org/abs/2406.07016
Kind:        primary — the authors own the corpus measurement; they ran the excess-vocabulary analysis firsthand.
Establishes: The behavior, measured. After LLMs appeared, specific style words rose abruptly in the frequency
             of published PubMed abstracts; the rise is used to estimate LLM-assisted writing prevalence.
Paraphrase:  Kobak, González-Márquez, Horvát, and Lause study vocabulary change in 14 million English PubMed
             abstracts, 2010-2024. They define, for each word, a 2024 counterfactual frequency q by extrapolating
             the pre-LLM trend, and compare it to the observed 2024 frequency p. The excess frequency ratio is
             r = p/q and the excess frequency gap is δ = p − q. Words with the largest r are low-baseline style
             words (delves, underscores, showcasing); words with the largest δ are common ones (potential,
             findings, crucial). From excess word usage they estimate at least 10% of 2024 abstracts were LLM-
             processed, up to ~30% in some sub-corpora. The abrupt shift exceeds the vocabulary footprint of the
             COVID pandemic.
Locators:    Abstract; Results (excess-word definitions and the marker-word panel, Fig. 2); Fig. 1 (frequency-
             over-time with counterfactual extrapolation); Fig. 3 (excess words per year by content vs style).
             Preprint arXiv:2406.07016v1, June 2024. Published as Science Advances 11(27), 2 July 2025.
Quote:       "We study vocabulary changes in 14 million PubMed abstracts from 2010-2024, and show how the
             appearance of LLMs led to an abrupt increase in the frequency of certain style words. Our analysis
             based on excess words usage suggests that at least 10% of 2024 abstracts were processed with LLMs.
             This lower bound differed across disciplines, countries, and journals, and was as high as 30% for
             some PubMed sub-corpora." (abstract, arXiv v1)
```

```text
URL:         https://arxiv.org/abs/2403.07183
Kind:        primary — the authors own this second-corpus measurement of the same behavior.
Establishes: The word-frequency shift is not an artifact of one corpus. A different genre (conference peer
             reviews) shows the same abrupt rise in specific adjectives after ChatGPT.
Paraphrase:  Weixin Liang et al. estimate the fraction of text LLM-modified in ICLR 2024, NeurIPS 2023, CoRL 2023,
             and EMNLP 2023 reviews. Certain adjectives spiked sharply in ICLR 2024 reviews relative to prior
             years: "commendable" ~9.8x, "meticulous" ~34.7x, "intricate" ~11.2x more likely to appear in a
             sentence. They estimate 6.5%-16.9% of review text could have been substantially LLM-modified.
Locators:    Abstract; main frequency-shift results and estimate. arXiv:2403.07183; ICML 2024.
Quote:       (figures per the paper's abstract and results tables; exact multipliers above.)
```

```text
URL:         https://arxiv.org/abs/2412.11385
Kind:        primary — Juzek & Ward own this analysis; they measure model-output word frequency firsthand and
             test the origin hypotheses themselves.
Establishes: (a) a primary measurement of word frequency in model output itself; (b) the direct empirical test
             of the annotator-dialect hypothesis, which did not support it; (c) suggestive-but-inconclusive
             evidence that RLHF (a between-model difference) is where the overuse enters.
Paraphrase:  Tom S. Juzek and Zina B. Ward (Florida State University) generate abstracts with ChatGPT-3.5 and
             measure occurrences-per-million (opm) of "focal" overused words in model output, finding them far
             above their opm in four training-data-proxy datasets — evidence against the pretraining-frequency
             explanation for these specific words. They enumerate seven candidate sources (initial training data;
             fine-tuning data; architecture; algorithm/tokenization; context priming; RLHF; other settings such
             as temperature). They test the annotator-dialect idea against the International Corpus of English
             (ICE) and report their initial analysis does not support it. A surprisal test finds Llama 2-Chat is
             far less "surprised" by AI-generated abstracts, which they read as consistent with a between-model
             (post-training) factor such as RLHF, but their human experiment was inconclusive and readers reacted
             to "delve" differently from other focal words. They call for a follow-up study.
Locators:    Abstract; Sec. 3 (seven hypotheses); Sec. 4 (training data + ICE/annotator test); Sec. 5 (architecture,
             algorithm, Llama surprisal); Sec. 6 (human experiment, inconclusive); Appendix B (opm comparison).
Quote:       "Our initial analysis of ICE does not support this hypothesis." (Sec. 4)
             "While the model testing is consistent with RLHF playing a role, our experimental results suggest
             that participants may be reacting differently to 'delve' than to other focal words." (abstract)
```

```text
URL:         https://arxiv.org/abs/2310.06452
Kind:        primary — the authors own the diversity measurement across base model, SFT, and RLHF.
Establishes: The settled cause. Post-training with RLHF measurably reduces output diversity relative to
             supervised fine-tuning — the distribution-narrowing / mode-collapse effect the lesson turns on.
Paraphrase:  Robert Kirk et al. compare base, supervised-fine-tuned, and RLHF models on generalisation and on
             output diversity (per-input diversity and across-input diversity, i.e. mode collapse), across
             syntactic, semantic, and other measures. RLHF generalises better to shifted inputs but significantly
             reduces output diversity, a tradeoff inherent to current fine-tuning. This is the concrete, quotable
             finding that post-training concentrates the output distribution.
Locators:    Abstract; diversity-metric results. arXiv:2310.06452; ICLR 2024.
Quote:       "RLHF significantly reduces output diversity compared to SFT across a variety of measures, implying
             a tradeoff in current LLM fine-tuning methods between generalisation and diversity."
```

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary — Ouyang et al. own the InstructGPT method; they describe the RLHF pipeline firsthand.
Establishes: RLHF (supervised fine-tuning, then reward-model + PPO optimization of human preference rankings)
             is the post-training recipe behind ChatGPT-style models — the stage whose narrowing the lesson names.
Paraphrase:  A model is fine-tuned on labeler demonstrations, then optimized by reinforcement learning against a
             reward model trained on human preference rankings. Gains in truthfulness and toxicity were real but
             partial, with only minimal regression on public NLP datasets. Cited only to name the recipe; the
             diversity-narrowing finding is carried by Kirk et al., not by this paper.
Locators:    Abstract; method (SFT -> reward model -> PPO). arXiv:2203.02155; NeurIPS 2022. Verified at
             abstract level only.
Quote:       "InstructGPT models show improvements in truthfulness and reductions in toxic output generation while
             having minimal performance regressions on public NLP datasets." (abstract)
```

```text
URL:         https://arxiv.org/abs/2304.02819
Kind:        primary — the authors own this evaluation of deployed detectors.
Establishes: The consequence. Word-frequency / stylometric AI detectors carry a documented false-positive bias;
             more "literary" wording reads as human, simpler wording reads as AI.
Paraphrase:  Weixin Liang et al. run several GPT detectors on non-native (TOEFL) and native (US 8th-grade) essays.
             Detectors misclassify more than half of non-native TOEFL essays as AI-generated while scoring native
             essays near-perfectly. Enriching non-native word choice cut misclassification; simplifying native
             writing raised it — the detectors track surface fluency, not authorship.
Locators:    Abstract; TOEFL vs 8th-grade results; word-substitution experiment. arXiv:2304.02819; Patterns (Cell
             Press) 4(7), 2023.
Quote:       "more than half of the non-native-authored TOEFL ... essays [are] incorrectly classified as
             'AI-generated,' while detectors exhibit near-perfect accuracy for US 8-th grade essays."
```

```text
URL:         https://arxiv.org/abs/2303.11156
Kind:        primary — the authors own the attack and the theoretical bound.
Establishes: Detectors are not only biased but gameable, and there is a distributional ceiling on detection.
Paraphrase:  Vinu Sankar Sadasivan et al. show a recursive paraphrasing attack that significantly lowers the
             detection rate of detectors and watermarking schemes while largely preserving text quality. They
             also prove a bound tying the best possible detector's AUROC to the total-variation distance between
             human and AI text distributions: as the distributions converge, reliable detection approaches
             chance. Supports "a distribution over training and tuning, not a watermark," and "can be prompted
             away."
Locators:    Abstract; recursive-paraphrasing experiments; TV-distance theorem. arXiv:2303.11156. A specific
             watermark drop (99.3% -> 9.7%) is reported in the paper's experiments; verified here at abstract
             level only, so the writer should cite the qualitative finding or confirm that figure in the body.
Quote:       "our recursive paraphrasing method can significantly reduce detection rates ... it only slightly
             degrades text quality in many cases" (abstract).
```

```text
URL:         https://www.theguardian.com/technology/2024/apr/16/techscape-ai-gadgest-humane-ai-pin-chatgpt
Kind:        secondary — a journalist's column that framed and popularized the hypothesis; it owns no measurement.
Establishes: The origin of the Nigerian/African-English annotator hypothesis, and its status as speculation.
Paraphrase:  Alex Hern (The Guardian, TechScape, 16 April 2024) proposes that because firms outsource RLHF
             annotation to low-wage, high-English-proficiency countries such as Nigeria, annotator preferences
             may push models toward Nigerian-register vocabulary like "delve," which he says is more common in
             Nigerian formal/business English. Offered as a theory, with no frequency study behind it. The
             article's own URL slug carries a typo ("gadgest"); the page is gated to automated fetch but this is
             the address where the source lives.
Locators:    The Guardian, TechScape newsletter, 16 April 2024.
Quote:       (recorded as the hypothesis's origin; the strength of its evidence is assessed under Contradictions.)
```

```text
URL:         https://simonwillison.net/2024/Apr/18/delve/
Kind:        secondary — a retelling of Hern's Guardian piece; adds framing, not new measurement. Counts with the
             Guardian item as one origin (two retellings of one origin count as one).
Establishes: How the hypothesis spread, and the informal "delve up 10-100x" claim as it circulated.
Paraphrase:  Simon Willison (18 April 2024) summarizes Hern's Guardian column for his readers, calls the theory
             "pretty solid," and repeats that PubMed abstracts now use "delve" "10 to 100 times more than a few
             years ago." The 10-100x figure here is informal secondhand framing; the primary, checked figure for
             "delve" is Kobak's r for "delves" (below).
Locators:    Post dated 2024-04-18; links Hern's Guardian article dated 2024-04-16.
Quote:       "delve" used "10 to 100 times more than a few years ago" (as relayed, not a primary measurement).
```

## Contradictions

The honest limits the commission asked for, plus what the search surfaced against the angle:

- Population, not instance. Kobak and Liang measure how often words appear across large corpora of *published* text, most of it human-written and only assisted by LLMs. A high excess frequency says the population shifted. It does not prove any single abstract, review, or sentence was machine-written. The word-frequency signal is correlational at the corpus level and cannot license a per-document verdict. This is the same fragility the detectors show.

- Base pretraining frequency also matters, and pulls against a clean "post-training did it" story for *general* word rank. Pretraining on web text sets the base rates every word starts from; post-training reshapes them. Juzek & Ward's finding cuts a specific way: for the *particular* focal words (delve, surpass), the training-data-frequency explanation is *not* supported — the words are overused in model output beyond their rate in training-data proxies — which is why the concentration has to come from later stages. Keep the distinction: pretraining sets the field of candidates; post-training concentrates the draw.

- The annotator hypothesis is contested and, on its one direct test, unsupported. Its origin is journalistic speculation (Hern), not a study. The only peer-reviewed empirical test located (Juzek & Ward's ICE-corpus analysis) did not support it. Their separate model-surprisal result is "consistent with RLHF playing a role" but does not isolate annotator dialect from any other between-model difference, and "delve" behaved unlike the other focal words in their human experiment. So the evidence for the *specific-word* origin is: one negative direct test, one weakly suggestive indirect test, and no positive confirmation. Label it a hypothesis, and state that its strongest empirical test came out against it. This is the seam the lesson must not blur: SETTLED that post-training concentrates the distribution (Kirk et al.); OPEN, and currently unconfirmed, *why these specific words*.

- Version drift in the headline prevalence figure. The June 2024 preprint says "at least 10%" of 2024 abstracts and "as high as 30%." The Science Advances (2 July 2025) publication revised these upward to about 13.5% and up to 40% as more 2024 data closed. Both are the same authors and method; the writer should cite one version explicitly and note it is a moving lower bound, not a contradiction between sources.

## Numbers

```text
Figure: r = 28.0  (excess frequency ratio for "delves", 2024)
Owner:  Kobak et al. (arXiv:2406.07016 / Science Advances 2025)
Scope:  observed 2024 frequency / pre-LLM counterfactual, across 14M PubMed abstracts. Read from the marker-word
        panel (Fig. 2); confirm the exact per-word value against the paper's figure/appendix before printing.

Figure: r = 10.9 ("underscores"); r = 10.2 ("showcasing")   [same source, scope, caveat as above]
Owner:  Kobak et al.

Figure: δ = 0.045 ("potential"); δ = 0.031 ("findings"); δ = 0.029 ("crucial")
Owner:  Kobak et al.
Scope:  excess frequency gap (absolute 2024 probability difference) for high-baseline words. Read from the same
        panel; confirm against the source figure/table.

Figure: at least 10% of 2024 PubMed abstracts LLM-processed (lower bound); as high as ~30% in sub-corpora
Owner:  Kobak et al., arXiv v1 (June 2024)
Scope:  fraction of 2024 English PubMed abstracts, from excess-word analysis. Published Science Advances 2025
        revises to ~13.5% and up to ~40%.

Figure: "commendable" ~9.8x; "meticulous" ~34.7x; "intricate" ~11.2x more likely per sentence
Owner:  Liang et al. (arXiv:2403.07183)
Scope:  ICLR 2024 peer reviews vs prior-year baseline. Estimated 6.5%-16.9% of review text substantially LLM-modified.

Figure: >50% of non-native TOEFL essays misclassified as AI-generated; near-perfect accuracy on US 8th-grade essays
Owner:  Liang et al. (arXiv:2304.02819, Patterns 2023)
Scope:  a set of GPT detectors run on TOEFL essays vs US 8th-grade essays.

Figure: RLHF significantly reduces output diversity vs SFT (per-input and across-input / mode collapse)
Owner:  Kirk et al. (arXiv:2310.06452)
Scope:  base vs SFT vs RLHF, across syntactic/semantic/other diversity measures. Directional finding; the paper's
        per-metric numbers can be pulled from its results tables if the writer wants a specific figure.
```

## Source assets

```text
Asset: Kobak et al., Figure 1 — frequency of selected words in PubMed abstracts, 2010-2024, with the pre-LLM
       counterfactual extrapolation drawn against the observed post-2022 jump.
Shows: the abrupt, dated break in a word's frequency the moment ChatGPT appears — the whole "measured, not a vibe"
       claim in one picture. Carries step 1 better than any prose restatement of the ratios.
Crop:  keep the vertical axis (frequency) labeled and the 2022/2023 break visible with the counterfactual line;
       keep at least one low-baseline style word (e.g. "delves") whose spike is unmistakable. Do not crop away the
       pre-2022 baseline, which is what makes the jump legible.

Asset: Kobak et al., Figure 2 — the marker-word panel ranking words by excess frequency ratio / gap.
Shows: which words carry the signal and how far each rose; the raw material for a most-over-represented-words table.
Crop:  if used as a table instead, take the top style words with their r values; retain units and the 2024 scope.

Asset: Liang et al. (2403.07183) — the adjective frequency-shift figure for ICLR 2024 reviews.
Shows: the same shift in a second, non-medical corpus (commendable/meticulous/intricate), which is the corroboration
       that the behavior is general.
Crop:  keep the multipliers and the year comparison; keep it visibly a different corpus from Kobak.

Asset: Kirk et al. (2310.06452) — the diversity-vs-generalisation results (base/SFT/RLHF).
Shows: the settled mechanism as data: RLHF's diversity drop against SFT. If the writer wants the settled claim to
       land on evidence rather than assertion, this is the figure.
Crop:  retain the RLHF-vs-SFT diversity comparison and the axis labels; the generalisation half is optional here.

Note: Charts in this paper are rendered from a committed chart-N.py per spec/charts.md, not lifted as images. These
      assets guide which measured series is worth rebuilding, not a screenshot to paste.
```

## Discarded

```text
https://www.emergentmind.com/papers/2406.07016 : third-party summary of Kobak; superseded by the arXiv primary.
https://www.aimodels.fyi/papers/arxiv/delving-into-chatgpt-usage-academic-writing-through : AI-generated paper
  summary; no independent standing.
https://pub.towardsai.net/why-does-chatgpt-use-delve-so-much-... : blog retelling of the delve hypothesis; the
  primary is Juzek & Ward (2412.11385) and the origin is Hern.
https://ampifire.com/blog/is-ai-detection-rigged/ : marketing blog; detector-bias claim is carried by Liang 2023.
https://www.fanaticalfuturist.com/2024/11/nigerian-ai-ese-not-english-... : secondhand retelling of the annotator
  hypothesis; adds no data, counts as the same origin.
https://businessday.ng/technology/article/online-uproar-over-nigerian-english-flagged-as-chatgpt-ish/ : reaction
  coverage, not evidence on the mechanism.
https://arxiv.org/abs/2406.08818 (Linguistic Bias in ChatGPT: dialect discrimination) : real and primary, but about
  the model's treatment of dialects, a different claim than why specific words are overused; out of scope here.
https://arxiv.org/html/2502.15666 (Almost AI, Almost Human) and https://arxiv.org/pdf/2412.05139 (Practical
  Examination of AI detectors) : additional detector-fragility evidence; not needed once Liang 2023 and Sadasivan
  cover the bias and gameability points. Held in reserve if the editor wants a second detector primary.
```
