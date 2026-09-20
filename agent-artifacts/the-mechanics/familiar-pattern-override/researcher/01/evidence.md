# Evidence: the-mechanics/familiar-pattern-override (researcher 01)

The evidence firmly supports the causal chain the commission wants: a language
model predicts the most probable continuation; the canonical form of a famous
puzzle and its canonical solution are heavily overrepresented in training data;
and a lightly altered prompt that still looks like the canonical puzzle pulls
the model back to the canonical answer even though that answer is now wrong.
Nezhurina et al.'s Alice in Wonderland (AIW) paper gives a rigorously measured
demonstration with exact per-model accuracy figures. Mukhopadhyay et al.'s
PHANTOM RECALL gives a second demonstration built specifically from 25 famous
logic puzzles with 149 altered variants, naming the failure "phantom recall."
Razeghi et al. and McCoy et al. ground the mechanism with direct frequency- and
probability-sensitivity numbers. The open question is genuinely open in the
sources themselves, not just declared open by the commission: AIW's own authors
refuse to conclude "entire absence of reasoning," and reasoning-trained models
help in some tests (AIW's o1-preview, PHANTOM RECALL's "Thinking" mode) but
underperform their own base models in Jang et al.'s PuzzleTrivial test, which
uses the same Fibonacci-Rabbit/Tower-of-Hanoi-style trick. That last paper is
the strongest single piece of evidence against a simple "reasoning training
fixes it" reading, and the commission's angle should be adjusted to reflect it.

The evidence is thin in one specific place: no source directly measures
whether the effect is stronger on more-famous puzzles than on obscure ones.
The commission's closing claim ("works best on the most famous puzzles and
fades on obscure ones") is a reasonable inference from the frequency-effect
papers (Razeghi; McCoy) but is not itself tested by any puzzle study I read.
This is flagged again in Contradictions.

## Sources

```text
URL:         https://arxiv.org/abs/2406.02061
Kind:        primary — Nezhurina, Cipolina-Kun, Cherti, and Jitsev report their
             own experiments; they designed the AIW problem, ran the models,
             and own the accuracy figures.
Establishes: The core demonstration. Template: "Alice has N brothers and she
             also has M sisters. How many sisters does Alice's brother have?"
             (correct answer M+1). Across four number-substitution variations,
             most tested models score at or near zero; among the four models
             that cross a 0.3 correct-response-rate threshold, GPT-4o reaches
             p=0.649 and Claude 3 Opus p=0.431 (Llama-2 70B Chat p=0.3).
             Chain-of-thought prompting and multi-step re-evaluation do not
             fix it. On a harder variant, AIW+, GPT-4/4o and Claude 3 Opus
             fall below p=0.2, while o1-preview holds robust performance
             close to 1 across all AIW+ variations; o1-mini, despite being
             from the same "reasoning" model family, collapses toward 0.
             The paper explicitly declines to conclude "entire absence of
             reasoning," and separately reports that newer reasoning models
             DeepSeek-R1 and o1-mini still show strong fluctuations on later
             AIW versions.
Paraphrase:  Simple family-relationship arithmetic, restated with different
             numbers, causes most state-of-the-art models (including GPT-4
             and Claude 3 Opus) to fail far more often than the problem's
             difficulty would predict, and the few models that do well
             fluctuate wildly between near-perfect and near-zero on
             structurally identical variations.
Locators:    Abstract; Sec. 2 (problem template and variations, p.6-7);
             Sec. 3.1 ("Low correct response rates," p.7, gives the p=0.649 /
             p=0.431 / p=0.3 figures); Fig. 3 (main collapse chart); Sec. 3.2
             ("Harder problem versions," p.16-17, AIW+ and o1-preview/o1-mini
             results, Fig. 12); Sec. 1 introduction (p.2, the "we do not
             conclude entire absence of reasoning" hedge and the DeepSeek-R1/
             o1-mini fluctuation note).
Quote:       "We do not conclude entire absence of reasoning from the
             observations." (Introduction, p.2)
Quote:       "o1-preview is a clear exception and has robust performance
             close to 1 across all AIW+ variations." (Sec. 3.2, p.17)
```

```text
URL:         https://arxiv.org/abs/2510.11812
Kind:        primary — Mukhopadhyay, Baral, Mahajan, Harish, RRV, Parmar,
             Nakamura, and Baral (Arizona State) built the PHANTOM RECALL
             benchmark, ran all eleven models, and own the accuracy figures.
Establishes: The second demonstration, built directly on the commission's
             "trivially modified classic puzzle" template. 25 well-known logic
             puzzles were perturbed into 149 variants that "preserve reasoning
             structure but alter superficial details and solutions." One
             worked example given in full: the "man and his dog cross a river
             in the rain, only the man gets wet" riddle (canonical answer: the
             dog is bald / the river is frozen). Across 11 models, systems
             "approach perfect accuracy on base puzzles but drop sharply on
             perturbed variants, with errors dominated by phantom recall."
             Human-graded results on the 149-item set: o3 59.73% (89/149),
             Gemini 2.5 Pro 58.39% (87/149), Claude Sonnet 4 54.36% (81/149),
             Gemini 2.5 Flash 48.32% (72/149), Claude 3.5 Sonnet 46.31%
             (69/149), GPT-4o 29.53% (44/149). Open-source models scored (of
             149): Qwen 74 (49.7%), Phi 48 (32.2%), Llama 3.1 46 (30.9%),
             InternLM 40 (26.8%), Mistral 33 (22.1%). Separately, comparing
             each closed model's extended "Thinking" mode against its
             standard "Non-Thinking" mode on the same 149 puzzles: ChatGPT/o3
             59.73% vs. 29.53% (+30.2 points), Gemini 58.39% vs. 48.32%
             (+10.1 points), Claude 54.36% vs. 46.31% (+8.0 points). A
             separate prompting-based mitigation lifted open-source models by
             4.7 to 10.1 percentage points. The paper's own conclusion is that
             despite these gains, "phantom recall persists across all
             systems" and the improvements are "narrow and model-specific."
Paraphrase:  Models that solve the original version of a famous puzzle almost
             every time collapse on lightly altered versions of the same
             puzzle, reproducing the memorized canonical answer instead of the
             new one. Extended reasoning ("Thinking" mode) helps substantially
             for some models but the paper's authors do not read this as
             solving the problem.
Locators:    Abstract; Fig. 1 and Sec. 1 (river/dog worked example, p.1);
             Sec. 3.1 "Dataset Construction" (25 base puzzles, p.3); Sec. 6.1
             "Objective Evaluation" (open-source counts, p.6, Fig. 5);
             Appendix B "Metrics Results from Human Evaluations" (closed-model
             percentages and the Thinking-vs-Non-Thinking comparison, with
             per-model confusion matrices, Fig. 11-13); Sec. 6 error-
             mitigation results (percentage-point gains); Sec. 7 Conclusion
             (the "persists across all systems" / "narrow and model-specific"
             assessment).
Quote:       "Despite near-perfect accuracy on unmodified puzzles, models
             significantly underperform humans on perturbed ones, exhibiting
             both phantom recall and over-elaboration." (Abstract)
```

```text
URL:         https://arxiv.org/abs/2505.17225
Kind:        primary — Jang, Kim, Park, Ryu, and Yang built the ReasoningTrap
             diagnostic set (including its PuzzleTrivial component), ran the
             comparisons themselves, and own the finding.
Establishes: A third, independently designed demonstration of the same
             behaviour, and direct counter-evidence on the open question. Two
             worked examples given in full text: (1) a Fibonacci-Rabbit
             variant that states the starting rabbit pair is "permanently
             infertile" — a non-reasoning ("No think") model correctly
             concludes the population stays constant, while the paired
             reasoning ("Think") model dismisses the stated condition as
             "trivial," silently substitutes "temporarily infertile," and
             reverts to the canonical Fibonacci growth answer; (2) a puzzle
             prompt that states outright "this is NOT a Tower of Hanoi
             problem," which a reasoning model (the paper names Qwen3-32B and
             OpenAI o3 in the figure caption) treats as a typo and answers as
             standard Tower of Hanoi anyway. The paper names this failure
             "reasoning rigidity" and distinguishes it explicitly from prompt
             brittleness: "even when the conditions are fully understood, the
             model will override them in favor of familiar solution
             templates."
Paraphrase:  A model can state the altered condition back correctly and still
             answer as if the puzzle were unmodified. In the two worked
             examples given, the reasoning-trained sibling model does this
             where the base model does not — the opposite of what a simple
             "reasoning training fixes it" story would predict.
Locators:    Abstract; Sec. 1 Introduction (p.1-2, reasoning-rigidity
             definition and the "override in favor of familiar solution
             templates" quote); Fig. 1 and its caption (both worked examples,
             p.2); Sec. 3.2 "PuzzleTrivial" (construction and the Fibonacci
             example narrated in prose, p.4).
Caveat:      The paper's Tables 2 and 3 report numeric pass@1/p-pass@1 scores
             for each base-vs-reasoning model pair on PuzzleTrivial. The PDF's
             two-column table layout did not extract cleanly to plain text
             (rows from adjacent tables interleaved), so I could not verify
             individual cell values against a clean render and have not cited
             any specific number from those tables. Only the prose claims and
             the Figure 1 worked examples, which extracted unambiguously, are
             used above. The writer should not cite PuzzleTrivial percentages
             from this record; an editor or later research pass should pull
             the table from the rendered PDF or HTML, not the raw-text
             extraction, before using any of its numbers.
```

```text
URL:         https://arxiv.org/abs/2410.05229
Kind:        primary — Mirzadeh, Alizadeh, Shahrokhi, Tuzel, Bengio, and
             Farajtabar (Apple) built GSM-Symbolic and GSM-NoOp and own the
             results and interpretation.
Establishes: The mechanism claim in general form, stated as the paper's own
             conclusion, not a citation to someone else: LLM "reasoning" often
             tracks in-distribution pattern-matching against forms seen in
             training rather than formal reasoning, so performance degrades
             as a prompt departs further from the memorized form (changing
             names hurts less than changing numbers, which hurts less than
             adding an irrelevant clause). This paper's own flagship
             demonstration, GSM-NoOp (inserting a true but irrelevant clause
             into a math word problem, causing accuracy drops of up to 65
             points), is the added-distractor / irrelevant-context behaviour,
             not this commission's behaviour — the model here is misled by
             something new in the prompt, not reverted to an unmodified
             template. Cited here only for the general pattern-matching claim
             and the reasoning-limit position, not for the GSM-NoOp figure.
Paraphrase:  A model's apparent reasoning ability degrades in proportion to
             how far a restated problem departs from the form it saw most
             often in training, which the authors read as evidence of
             pattern matching rather than formal reasoning.
Locators:    Sec. 1 Introduction (p.1, "literature suggests... is
             probabilistic pattern-matching rather than formal reasoning");
             Sec. 4.2 "How fragile is mathematical reasoning..." (p.6, names-
             vs-numbers degradation); Sec. 6 Conclusion (p.10, "sophisticated
             pattern matching rather than true logical reasoning"); Sec. 4.4
             GSM-NoOp (p.7-8, the up-to-65-point figure — flagged as the
             neighboring behaviour, not cited as this article's own number).
Quote:       "Their reasoning is fragile and may be more akin to
             sophisticated pattern matching rather than true logical
             reasoning." (Sec. 6, p.10)
```

```text
URL:         https://arxiv.org/abs/2202.07206
Kind:        primary — Razeghi, Logan IV, Gardner, and Singh ran the
             correlation analysis themselves on GPT-family models against the
             (public) Pile pretraining corpus and own the frequency figures.
Establishes: The plain empirical link between "appears often in training
             data" and "model gets it right," which grounds the commission's
             "first cause" step. On few-shot numerical tasks, model accuracy
             on the top 10% most frequent terms in the pretraining data
             exceeds accuracy on the bottom 10% by more than 70 percentage
             points in some cases. Separately, GPT-3's largest model performs
             zero-shot 2-digit addition at 76.9% accuracy, a number the
             authors flag as possibly reflecting memorized overlap with
             training data rather than arithmetic competence.
Paraphrase:  How often a specific term or fact appeared in a model's training
             data predicts how well the model handles a task built from it,
             independent of the task's inherent difficulty — direct support
             for "the canonical puzzle and its canonical answer appear many
             times in training data, so the model assigns them a very high
             prior probability."
Locators:    Abstract; Sec. 1 Introduction (p.1, the 76.9% GPT-3 addition
             figure and the "more than 70% of average accuracy gap" figure).
Quote:       "Models are more accurate on instances whose terms are more
             prevalent, in some cases above 70% (absolute) more accurate on
             the top 10% frequent terms in comparison to the bottom 10%."
             (Abstract)
```

```text
URL:         https://arxiv.org/abs/2309.13638
Kind:        primary — McCoy, Yao, Friedman, Hardy, and Griffiths ran these
             probability-sensitivity experiments themselves and own the
             reported accuracy figures.
Establishes: The "next-token prediction favors the high-probability
             continuation" half of the mechanism, with concrete numbers
             (though from ciphers and word-reversal, not puzzles). Framing
             the task as one where the correct answer happens to be a
             high-probability English sentence versus a low-probability one:
             reversing a sequence of words, GPT-4 scores 97% accuracy when
             the correct output is high-probability text versus 53% when it
             is low-probability text, despite the task itself being fully
             deterministic either way. A parallel effect for input
             probability: encoding sentences in rot-13, GPT-4 scores 21% when
             the input is a high-probability sentence versus 11% when it is
             low-probability.
Paraphrase:  Even on tasks where there is exactly one correct answer, a
             model is far more likely to produce that answer when it happens
             to be the kind of text the model already assigns high
             probability to — direct, quantified support for "the model
             predicts the most probable continuation" as a general
             mechanism, independent of the puzzle domain.
Locators:    Table 1 (p.2-3, the output-probability and input-probability
             rows and the 97%/53% and 21%/11% figures); Sec. 1 Introduction
             (framing, "statistical next-word prediction system being used to
             solve [a task]").
Quote:       "LLMs achieve higher accuracy when the correct answer is
             high-probability text than when it is low-probability text,
             even when the task is deterministic." (Table 1)
```

```text
URL:         https://arxiv.org/abs/2308.03762
Kind:        primary — Arkoudas authored this position paper from his own
             qualitative testing of GPT-4 on 21 reasoning problems he
             designed; he owns the argument and the examples.
Establishes: An explicit statement of the "hard reasoning limit" side of the
             open question, argued from evidence, not merely asserted. Worked
             examples (graph coloring, an entropy-inequality problem) show
             GPT-4 restating a memorized fact correctly and then failing to
             apply its own stated fact to the very next step, which the
             author reads as evidence against "reasoning" in any operative
             sense, not merely a performance gap that more scale would close.
             None of Arkoudas's worked examples is a classic modified riddle
             in the commission's sense (they are original graph-theory and
             probability puzzles Arkoudas devised) — cited here for the
             general position, not as a demonstration of this specific
             behaviour.
Paraphrase:  One prominent researcher's explicit, evidence-argued position
             that GPT-4's failures reflect an absence of reasoning capacity,
             not a fixable performance gap.
Locators:    Abstract ("there are good reasons to be highly skeptical of
             GPT-4's ability to reason"; "GPT-4 at present is utterly
             incapable of reasoning"); Sec. 1.2 graph-coloring example (p.15,
             "It is clear that GPT-4 has memorized all this information but
             is unable to use it in a new setting"); Sec. 1.3.16 entropy
             example (p.43-44).
Quote:       "GPT-4 at present is utterly incapable of reasoning, in spite of
             its sporadic displays of ingenuity." (Abstract / p.2)
```

```text
URL:         https://arxiv.org/abs/2307.02477
Kind:        primary — Wu, Qiu, Ross, Akyürek, Chen, Wang, Kim, Andreas, and
             Kim designed and ran the counterfactual-task evaluations and own
             the figures.
Establishes: A general-purpose version of the same override mechanism outside
             the puzzle domain, useful for confirming the mechanism is not an
             artifact specific to riddles. Models perform well when a task
             matches the "default" convention they were trained on (base-10
             arithmetic, standard compass orientation, a standard musical
             key) and degrade when the same task is restated under an
             explicit but non-default convention, even though the underlying
             procedure is unchanged. One concrete, cleanly-extracted figure:
             for a spatial drawing-program task, the fraction of GPT-3.5
             outputs that are even parseable as a valid program drops from
             99% under the default coordinate convention to 62% (vertically
             flipped), 71% (90-degree rotation), or 75% (180-degree rotation)
             — the model keeps drawing as if the default convention still
             held.
Paraphrase:  Told explicitly that a task now runs under different rules than
             the ones it was trained on, a model frequently keeps applying
             the old, default rules — the same override pattern the
             commission describes for puzzles, demonstrated instead on
             arithmetic bases, spatial coordinates, and musical keys.
Locators:    Abstract; Sec. 2 (the base-9 arithmetic and rotated-coordinate
             "counterfactual condition" framework, p.2-3); footnote 11
             (p.19-20, the 99%/62%/71%/75% figures for the drawing-program
             task).
```

```text
URL:         https://www.open-thoughts.ai/blog/aiw
Kind:        secondary — this is the LAION/Open Thoughts team's own extension
             of the AIW methodology to additional models (o1, o1-preview,
             o1-mini, DeepSeek-R1, and several open "reasoning" models), which
             makes it partly firsthand for its own new data points, but it
             reports on and interprets someone else's original demonstration
             (Nezhurina et al.'s AIW problem) rather than owning the
             underlying claim. Treated as secondary for that reason.
Establishes: That the "reasoning training helps" pattern from the AIW paper
             generalizes only partially: o1 and o1-preview post the highest
             average accuracy of any models tested on AIW and its harder
             variants, and are also more consistent across variations than
             other reasoning models, but the post concludes that "open
             reasoning models... have a severe lack of robustness to the
             simple reasoning problems found in Alice in Wonderland," and
             that this gap is not visible in the standardized benchmarks used
             to market these models. I could not extract exact percentages
             from this page; its charts are rendered client-side and did not
             resolve to static text.
Paraphrase:  Independent replication broadly confirms the AIW paper's own
             finding — some reasoning models are much more robust, others are
             not — without settling whether reasoning training solves the
             underlying override.
Locators:    Section covering AIW Friends/Plus/Circle-Colleagues results
             (o1-family versus open reasoning models); no page or paragraph
             numbers on this page. Dated 2025-02-22 per the post's own byline.
```

## Contradictions

- **Whether reasoning training helps, hurts, or does neither — genuinely
  contested inside the primary sources, not just between "sides."** AIW finds
  o1-preview strongly robust on AIW+ while o1-mini (same lineage) collapses.
  PHANTOM RECALL finds every closed model's "Thinking" mode outperforms its
  own "Non-Thinking" mode on the identical 149-puzzle set (gains of 8 to 30
  points), yet the same paper's conclusion calls the effect "narrow and
  model-specific" and says phantom recall "persists across all systems."
  Jang et al.'s PuzzleTrivial set, built specifically to test this, finds the
  Fibonacci-Rabbit and Tower-of-Hanoi worked examples going the other way
  entirely: the reasoning-trained sibling model overrides the stated
  condition where the paired base model does not. No source in this record
  supports a clean "reasoning models have solved this" reading, and no source
  supports a clean "reasoning training never helps" reading either. The
  honest state of the evidence is genuinely mixed, model-by-model and
  puzzle-by-puzzle, and the commission's framing ("a prior-vs-reasoning
  tradeoff that scale and RL partly fix") should say model-and-task-dependent
  rather than implying a settled partial fix.
- **AIW's own authors do not endorse the strong "can't reason" reading.**
  Despite the paper's title invoking "complete reasoning breakdown," the text
  explicitly states "we do not conclude entire absence of reasoning from the
  observations" (p.2). A draft that cites AIW for the hard-limit position
  without this qualifier would overstate what the paper itself claims.
- **The "fades on obscure puzzles" claim is not directly tested anywhere in
  this record.** Razeghi and McCoy establish that frequency/probability in
  training predicts accuracy in general, which supports the claim by
  inference, but no source measures reversion rate as a function of a given
  puzzle's fame or frequency, holding the puzzle's alteration difficulty
  constant. This is the clearest evidentiary gap; see the note in the summary
  paragraph and flag it for the editor.
- **GSM-Symbolic's most-cited number is not evidence for this commission.**
  Its headline finding (up to 65-point accuracy drops on GSM-NoOp) is caused
  by adding an irrelevant true clause to an intact problem — the
  irrelevant-context/added-distractor behaviour the commission explicitly
  must stay distinct from, not a premise change causing reversion to a
  canonical answer. I have cited GSM-Symbolic only for its general
  pattern-matching claim, never for the GSM-NoOp figure, and the writer
  should do the same.

## Numbers

```text
Figure: GPT-4o correct response rate on AIW original, p=0.649 (averaged
        across STANDARD/THINKING/RESTRICTED prompts and variations 1-4)
Owner:  Nezhurina et al., AIW (arxiv.org/abs/2406.02061), Sec. 3.1
Scope:  One model, one problem template, 4 number-substitution variations,
        60 trials per variation; among the highest-scoring of ~20+ tested
        models.
```

```text
Figure: Claude 3 Opus correct response rate on AIW original, p=0.431
Owner:  Nezhurina et al., AIW, Sec. 3.1
Scope:  Same conditions as above. The paper notes only 4 of the tested models
        cross p=0.3 at all; most score close to 0.
```

```text
Figure: GPT-4/4o and Claude 3 Opus correct response rate on AIW+ (harder
        variant, 6 variations), below p=0.2
Owner:  Nezhurina et al., AIW, Sec. 3.2
Scope:  Same models, harder problem version requiring paternal/maternal-side
        cousin counting.
```

```text
Figure: o1-preview correct response rate on AIW+, close to 1 across all 6
        variations, with no fluctuation
Owner:  Nezhurina et al., AIW, Sec. 3.2, Fig. 12
Scope:  One reasoning-class model, same AIW+ variations. Contrast: o1-mini
        (same model family/lineage) collapses toward 0 on the same task.
```

```text
Figure: PHANTOM RECALL 149-puzzle accuracy (human-graded): o3 59.73%
        (89/149), Gemini 2.5 Pro 58.39% (87/149), Claude Sonnet 4 54.36%
        (81/149), Gemini 2.5 Flash 48.32% (72/149), Claude 3.5 Sonnet 46.31%
        (69/149), GPT-4o 29.53% (44/149)
Owner:  Mukhopadhyay et al., PHANTOM RECALL (arxiv.org/abs/2510.11812),
        Appendix B
Scope:  6 closed models, 149 perturbed variants of 25 well-known puzzles;
        denominator is the full perturbed set, not the base (unmodified)
        puzzles, on which the paper reports near-perfect accuracy without
        giving an exact percentage.
```

```text
Figure: Same 149-puzzle set, "Thinking" mode vs. "Non-Thinking" mode:
        ChatGPT/o3 +30.2 points (59.73% vs. 29.53%), Gemini +10.1 points
        (58.39% vs. 48.32%), Claude +8.0 points (54.36% vs. 46.31%)
Owner:  Mukhopadhyay et al., PHANTOM RECALL, Appendix B (Fig. 11-13)
Scope:  Same 3 closed models compared against themselves, same 149-item set.
        This is the primary quantitative evidence in this record for the
        "reasoning training partly fixes it" reading, though the paper's own
        conclusion frames the residual failure rate as still dominant.
```

```text
Figure: Open-source model accuracy on the same 149-puzzle set: Qwen 49.7%
        (74/149), Phi 32.2% (48/149), Llama 3.1 30.9% (46/149), InternLM
        26.8% (40/149), Mistral 22.1% (33/149); prompting-based mitigation
        raised these by 4.7 to 10.1 percentage points
Owner:  Mukhopadhyay et al., PHANTOM RECALL, Sec. 6.1 and Sec. 6 (mitigation)
Scope:  5 open-weight models, same 149-item set.
```

```text
Figure: Pretraining term frequency vs. accuracy gap: more than 70 percentage
        points between the top-10%-frequency and bottom-10%-frequency terms,
        in some tasks
Owner:  Razeghi et al. (arxiv.org/abs/2202.07206), Sec. 1
Scope:  GPT-family models (Pile-trained), several numerical-reasoning tasks;
        this is a correlational figure across terms within a task, not a
        single task's overall accuracy.
```

```text
Figure: GPT-3 (largest model) zero-shot 2-digit addition accuracy, 76.9%
Owner:  Razeghi et al., Sec. 1, citing Brown et al. 2020's own reported figure
Scope:  One arithmetic task, zero-shot; flagged by Razeghi et al. as possibly
        reflecting training-data overlap rather than arithmetic competence.
```

```text
Figure: GPT-4 word-reversal accuracy, 97% (high-probability output) vs. 53%
        (low-probability output); rot-13 encoding accuracy, 21%
        (high-probability input) vs. 11% (low-probability input)
Owner:  McCoy et al., Embers of Autoregression (arxiv.org/abs/2309.13638),
        Table 1
Scope:  Two deterministic tasks with a single correct answer each; the
        variable is only whether that correct answer/input happens to be
        high- or low-probability text, not puzzle content.
```

```text
Figure: GSM-NoOp accuracy drop, up to 65 percentage points, across all
        tested SOTA models
Owner:  Mirzadeh et al., GSM-Symbolic (arxiv.org/abs/2410.05229), Sec. 4.4
Scope:  Not this commission's behaviour — this is the irrelevant-context/
        added-distractor neighbor lesson's own number. Recorded here only so
        the writer does not mistake it for a familiar-pattern-override figure.
```

## Source assets

```text
Asset: Figure 3, "Collapse of SOTA LLMs on AIW problem" (Nezhurina et al.,
       arxiv.org/abs/2406.02061)
Shows: Bar chart of correct-response-rate by model with a same-figure inlay
       showing GPT-4's rate swinging from near-0 to near-1 across four
       variations of one unchanged problem structure.
Crop:  Whichever half best carries one point at a time — the bar chart for
       "most models fail," the inlay for "the same model wildly inconsistent
       on an unchanged problem" — should retain the axis labels and the
       per-variation color key; the inlay's point depends on seeing more than
       one variation's bar next to each other.
```

```text
Asset: Figure 12, AIW+ correct response rates (Nezhurina et al.)
Shows: o1-preview's flat, near-1 line against GPT-4/4o and Claude 3 Opus's
       collapse below 0.2, with o1-mini also shown collapsing despite sharing
       a lineage with o1-preview.
Crop:  Must keep at least o1-preview, one collapsed conventional model, and
       o1-mini together, or the point (reasoning training does not uniformly
       fix this, even within one vendor's own model family) is lost.
```

```text
Asset: Figure 5, open-source model accuracy on the Phantom Recall dataset
       (Mukhopadhyay et al., arxiv.org/abs/2510.11812)
Shows: Ranked bar chart of Qwen/Phi/Llama/InternLM/Mistral accuracy on the
       149 perturbed puzzles.
Crop:  None found beyond the full chart; it is already a single clean
       comparison.
```

```text
Asset: Figure 1, the river/dog worked-example puzzle, original vs.
       closed-ended transformed wording (Mukhopadhyay et al.)
Shows: The exact puzzle text used in the paper's own worked example, letting
       a reader see for themselves how small the "trap" wording is.
Crop:  The full puzzle text is short enough to quote directly rather than
       crop as an image; if used as an image, keep the full riddle text, not
       a partial sentence.
```

```text
Asset: Figure 1, the Fibonacci-Rabbit and Tower-of-Hanoi worked examples
       (Jang et al., arxiv.org/abs/2505.17225)
Shows: Side-by-side base-model vs. reasoning-model responses to the same
       altered prompt, with the reasoning model's silent substitution of
       "temporarily infertile" for the prompt's stated "permanently
       infertile" visible in its own words.
Crop:  Needs both the altered prompt and both models' answers together, since
       the point is specifically that the reasoning model's own words show it
       rewriting the condition rather than misreading it.
```

```text
Asset: Figure 1, multiplication accuracy vs. term frequency in pretraining
       data (Razeghi et al., arxiv.org/abs/2202.07206)
Shows: A scatter/line plot of GPT-J-6B's accuracy climbing with how often the
       relevant number appeared in its training data.
Crop:  None found; this chart's argument depends on the full frequency axis,
       not a cropped high or low end.
```

## Discarded

```text
URL: https://www.corrinlakeland.com/professional/2024/5/wolf-goat-cabbage-and-llms — read in full; a single-author blog post
     testing one modified river-crossing puzzle on ChatGPT with no
     quantitative data (only a qualitative "every LLM I tried failed" claim
     and one linked conversation transcript). PHANTOM RECALL and Jang et al.
     cover the same behaviour with actual measured numbers, so this added
     nothing a rigorous source didn't already establish.
```

```text
URL: https://marcodsn.me/altered-riddles — read in full (static HTML); the
     page describes a plausible-looking methodology ("pattern override
     rate," five alteration types) and names a surgeon-riddle example, but
     its leaderboard numbers are rendered client-side by JavaScript and did
     not resolve to static text I could verify. I could not confirm any
     specific figure from it, so nothing from this page is cited above.
```

```text
URL: https://ahmorse.medium.com/llms-and-reasoning-part-i-the-monty-hall-problem-f30b22c7ade7 — fetch returned HTTP 403.
     Per the sourcing standard a 403 is gated, not dead, but I could not
     obtain the article's content through any available browser-style
     request in this session, so I have not cited it and cannot confirm what
     it measured.
```

```text
URL: https://arxiv.org/abs/2302.08399 (Ullman, "Large Language Models Fail on
     Trivial Alterations to Theory-of-Mind Tasks") — read the abstract and
     summary in full; genuinely about the same shape of behaviour (a trivial
     alteration breaks a memorized-pattern response) but in a different task
     domain (belief-attribution/theory-of-mind vignettes, not classic
     riddles or puzzles with a single canonical numeric or logical answer).
     Excluded to keep the record on the commission's specific behaviour;
     flagged here in case the writer wants a theory-of-mind analogy.
```

```text
URL: https://arxiv.org/abs/2604.08571 (Golikov et al., "Robust Reasoning
     Benchmark") — read via fetch; tests AIME math problems under textual
     perturbation and attributes failures to a different mechanism
     ("Intra-Query Attention Dilution" across sequential problems), not to
     reversion toward a memorized canonical answer for an altered puzzle.
     Off-topic for this commission's mechanism; discarded rather than
     forced into the record.
```

```text
URL: https://arxiv.org/abs/2511.11810 (Højer, "On the Notion that Language
     Models Reason") — read via fetch; a theoretical/definitional position
     paper arguing LMs are not reasoners in any formal sense. Its position
     duplicates Arkoudas's (already cited) without adding puzzle-specific
     evidence or new figures, so including it would be padding rather than
     new interpretive weight.
```
