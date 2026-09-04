# Evidence: the-instruments/attack-success-rate (01)

The evidence supports the full commissioned pipeline and both halves of the
lesson firsthand. Two benchmarks are recovered in concrete detail: HarmBench
(behavior set, a fine-tuned Llama-2-13B classifier validated at 93.19% agreement
with human labels, an ASR definition, and a standardized 512-token generation
window that alone moves ASR by up to 30%) and StrongREJECT (313 forbidden
prompts, a GPT-4-based rubric autograder scoring refusal/specificity/
convincingness, and a Spearman validation showing prior graders correlate with
human judgment as weakly as 0.157 or even negatively). The commission's four
teaching targets each have owned numbers: an ASR is defined only with an attack
and a judge attached (GCG transfer, HarmBench classifier); the same responses
score differently by judge (StrongREJECT's grader comparison, the past-tense
paper's 88/65/73 across three judges, and Gao 2026's judge precision/recall
spread); refusing more drives ASR to zero by construction (both benchmarks'
formulas); and a static low ASR expires (GCG reported 2.1% on Claude-2, while a
one-line past-tense rewrite took GPT-4o from 1% to 88%). The misled case is
concrete and current: Cisco's 100% ASR for DeepSeek R1 from 50 HarmBench prompts
under one algorithmic attack, repeated in trade press as a flat safety verdict
with no note of that scope. The record is thin in two places. The GCG paper's
AdvBench size is stated in prose as "500 each," while the widely reused released
files are commonly cited as 520 behaviors and 574 strings, which this record
could not confirm firsthand. And the over-refusal counterweight rests on one
primary (XSTest) plus the ASR formulas, because the commission routes
over-refusal to a separate published lesson; the writer must decide whether to
cite XSTest or only link that lesson.

## Sources

```text
URL:         https://arxiv.org/abs/2402.04249
Kind:        primary. Mazeika et al. own HarmBench, its behavior set, its
             classifier, and its ASR definition.
Establishes: The HarmBench pipeline firsthand. 510 unique harmful behaviors:
             200 standard, 100 copyright, 100 contextual, 110 multimodal, split
             100 validation / 410 test, across 7 semantic categories. A red
             teaming method turns behaviors into test cases; targets generate
             with greedy decoding at N=512 tokens; completions go to a
             classifier. The non-copyright classifier is a fine-tuned Llama 2
             13B chat model; copyright uses hashing. ASR is the fraction of
             test cases the classifier labels as exhibiting or attempting the
             behavior, where an errored attempt still counts. The paper reports
             the 512-token choice is unstandardized in prior work and can change
             ASR by up to 30%.
Paraphrase:  Attack success rate is the share of a fixed harmful-behavior set
             on which a classifier judges the model's generation a successful
             attempt, and the classifier and the generation length are part of
             the number.
Locators:    Sec. 3 (framework, ASR definition); Table 3 (classifier
             agreement); classifier and 512-token discussion in the evaluation
             pipeline section.
Quote:       "the choice of this parameter can change ASR by up to 30%."
```

```text
URL:         https://arxiv.org/abs/2402.10260
Kind:        primary. Souly et al. own StrongREJECT, its prompt set, its
             autograder, and its validation against human labels.
Establishes: The StrongREJECT pipeline and its judge-sensitivity analysis
             firsthand. The autograder gives three scores per response: a binary
             "refused" flag, a 1-5 specificity score, and a 1-5 convincingness
             score, combined as score = (1 - refused) x (specific + convincing)
             / 2, normalized to [0,1]. The original autograder prompts GPT-4;
             the paper also validates a fine-tuned open version. Validation
             ranks jailbreaks by human-judged effectiveness and correlates each
             automated grader against that ranking (Spearman): StrongREJECT
             fine-tuned 0.900, StrongREJECT rubric 0.846, HarmBench 0.819, PAIR
             0.249, GPT-4 Judge 0.157, string-matching -0.394. The paper's core
             finding: prior evaluators overstate jailbreak effectiveness because
             a jailbreak that raises an aligned model's willingness to answer
             tends to degrade the answer's quality, shown on the unaligned
             Dolphin model and on MMLU.
Paraphrase:  A response counts as a successful jailbreak only to the degree it
             is non-refusing, specific, and convincing, and most earlier graders
             that scored non-refusal alone rank jailbreaks far out of line with
             humans.
Locators:    Autograder rubric and formula in the method section; the grader
             correlation comparison figure/table; the willingness-vs-
             capabilities section (Dolphin, MMLU); Yong et al. discussion.
Quote:       "existing evaluation methods significantly overstate jailbreak
             effectiveness compared to human judgments and the StrongREJECT
             evaluator."
```

```text
URL:         https://github.com/alexandrasouly/strongreject
Kind:        primary. The StrongREJECT authors' own dataset and code
             repository.
Establishes: The live dataset counts, resolving a version discrepancy in
             secondary summaries. The full dataset is 313 forbidden prompts;
             the small subset is 60. Composition is roughly 70% novel prompts,
             10% from DAN, 10% from AdvBench, the rest from prior work and an
             OpenAI system card. The original autograder uses GPT-4 Turbo; the
             repo also ships a fine-tuned Gemma 2B autograder to run locally.
Paraphrase:  The maintained StrongREJECT dataset holds 313 prompts (60 in the
             small set), not the 346/50 some third-party summaries report.
Locators:    Repository README, dataset file descriptions
             (strongreject_dataset.csv, strongreject_small_dataset.csv).
Quote:       "the full dataset of 313 questions"
```

```text
URL:         https://arxiv.org/abs/2307.15043
Kind:        primary. Zou et al. own the GCG attack and its reported transfer
             rates.
Establishes: How an attack drives ASR, and the expiration point firsthand. GCG
             (Greedy Coordinate Gradient) optimizes an adversarial suffix by
             gradient-guided token substitution against open-weight models. Its
             AdvBench behaviors set is described in prose as 500 harmful
             behaviors and 500 harmful strings. Success on a behavior is "a
             reasonable attempt at executing the behavior," i.e. not a refusal,
             with manual verification for transfer results. A prompt optimized
             on an ensemble of Vicuna and Guanaco transfers to black-box models
             at: GPT-3.5 86.6%, GPT-4 46.9%, Claude-1 47.9%, Claude-2 2.1%,
             PaLM-2 66.0%. The paper attributes Claude-2's low rate to greater
             robustness.
Paraphrase:  The same fixed suffix produces wildly different success rates
             across models, and Claude-2's 2.1% is a low ASR against this one
             2023 attack, not a general safety score.
Locators:    Method section (GCG); Table 2 (transfer ASR); success-criterion
             discussion in the evaluation setup.
Quote:       "2.1" (Claude-2 transfer ASR, Table 2).
```

```text
URL:         https://arxiv.org/abs/2407.11969
Kind:        primary. Andriushchenko & Flammarion own the past-tense attack and
             its measured rates.
Establishes: A cheap attack defeating a low reported score, and judge
             sensitivity, firsthand. Using 100 harmful behaviors from
             JBB-Behaviors (JailbreakBench) and a GPT-4 judge, rewriting a
             request into the past tense over 20 attempts moves ASR from the
             direct-request baseline as: Llama-3 8B 0% -> 27%, Claude-3.5 Sonnet
             0% -> 53%, GPT-3.5 Turbo 0% -> 74%, Gemma-2 9B 0% -> 74%, Phi-3-Mini
             6% -> 82%, GPT-4o-mini 1% -> 83%, GPT-4o 1% -> 88%, R2D2 23% -> 98%.
             The same GPT-4o past-tense result is 88% under the GPT-4 judge, 65%
             under a Llama-3 70B judge, and 73% under a rule-based judge.
Paraphrase:  A one-line reformulation, no optimization, takes GPT-4o from
             refusing almost everything to complying most of the time, and which
             judge scores it changes the headline by more than 20 points.
Locators:    Table 1 (per-model before/after under GPT-4 judge); the
             three-judge comparison table for GPT-4o; setup (JBB-Behaviors,
             judges).
Quote:       "from 1% using direct requests to 88% using 20 past tense
             reformulation attempts."
```

```text
URL:         https://arxiv.org/abs/2606.25487
Kind:        primary. Gao owns this direct measurement of judge reliability.
Establishes: How much the judge alone moves ASR, firsthand. On 596
             human-labeled completions, the dedicated classifier
             HarmBench-Llama-2-13b-cls scores precision 0.835 / recall 0.974
             (it over-flags), while three LLM-as-judge models keep high
             precision but erratic recall: Qwen2.5-7B-Instruct 0.940 / 0.174,
             Phi-3.5-mini-instruct 0.810 / 0.648, Qwen2.5-3B-Instruct 0.889 /
             0.059. Benign framing wrappers that leave harmful text intact flip
             LLM judges 57%-100% of the time (a refusal-prefix alone 39%-88%),
             while the classifier resists at 3.4%; a white-box GCG attack on the
             classifier's weights flips 70% of confident true positives (21 of
             30). A human audit confirmed flipped responses still contained the
             harmful content.
Paraphrase:  The same responses graded by different judges give systematically
             different ASRs, and both judge families can be pushed off their
             verdicts without changing the harm in the text.
Locators:    Calibration table (precision/recall by judge); adversarial
             robustness section (wrapper flip rates, GCG-on-classifier);
             human-audit paragraph.
Quote:       "the choice of judge changes the answer."
```

```text
URL:         https://blogs.cisco.com/security/evaluating-security-risk-in-deepseek-and-other-frontier-reasoning-models
Kind:        primary. Cisco (Kassianik, Karbasi, and collaborators) own this
             widely cited ASR claim about DeepSeek R1.
Establishes: The misled case at its origin. On 50 uniformly sampled prompts
             from HarmBench, run through an automatic jailbreaking algorithm
             with automatic refusal detection plus human oversight at
             temperature 0, reported ASRs are: DeepSeek R1 100%, Llama-3.1-405B
             96%, GPT-4o 86%, Gemini-1.5-Pro 64%, Claude-3.5 Sonnet 36%,
             o1-preview 26%. The 100% means the model refused none of the 50
             tested prompts.
Paraphrase:  A single ASR from one 50-prompt sample under one attack and one
             judging setup became a flat "DeepSeek is unsafe" verdict.
Locators:    Results chart (per-model ASR); methodology paragraph (50 HarmBench
             prompts, algorithmic jailbreaking, refusal detection); conclusion.
Quote:       "DeepSeek R1 lacks robust guardrails, making it highly susceptible
             to algorithmic jailbreaking and potential misuse."
```

```text
URL:         https://arxiv.org/abs/2308.01263
Kind:        primary. Roettger et al. own XSTest and the exaggerated-safety
             measurement.
Establishes: The hidden cost the ASR number does not show. XSTest is 250
             hand-crafted safe prompts across 10 prompt types that a
             well-calibrated model should answer, paired with 200 unsafe
             contrast prompts. It measures exaggerated safety: refusing benign
             requests. This is the separate axis a low ASR can buy by refusing
             more, and the paper the lesson can point to for the over-refusal
             counterweight.
Paraphrase:  A model can drive ASR toward zero by refusing more, and whether
             that also refuses safe requests is measured by a different test,
             not by ASR.
Locators:    Abstract (250 safe + 200 unsafe contrast prompts, 10 types).
Quote:       "XSTest comprises 250 safe prompts across ten prompt types that
             well-calibrated models should not refuse to comply with, and 200
             unsafe prompts as contrasts."
```

```text
URL:         https://www.securityweek.com/deepseek-compared-to-chatgpt-gemini-in-ai-jailbreak-test/
Kind:        secondary. Eduard Kovacs reports Cisco's study; SecurityWeek did
             not run the test and does not own the numbers.
Establishes: How the ASR is cited in public. It repeats DeepSeek R1 100% and
             OpenAI o1 26%, with other models 36%-96%, and names HarmBench and
             the 50-prompt sample. It raises no methodological caveat about
             sample size, attack, or judge, and carries Cisco's "lacks robust
             guardrails" line as the finding.
Paraphrase:  Trade coverage forwards the 100% figure and the safety verdict
             while omitting that it rests on 50 prompts under one attack and one
             judging setup.
Locators:    Body paragraphs citing Cisco's ASRs and HarmBench.
Quote:       "DeepSeek R1 lacks robust guardrails, making it highly susceptible
             to algorithmic jailbreaking and potential misuse."
```

```text
URL:         https://the-decoder.com/researchers-uncover-an-all-too-easy-trick-to-bypass-llm-safeguards/
Kind:        secondary. Matthias Bastian reports the past-tense paper; The
             Decoder did not run the experiment.
Establishes: How a jailbreak ASR result reaches a general audience. It leads
             with GPT-4o going from 1% to 88% and reports 100% for some
             categories, and frames the result as evidence that SFT, RLHF, and
             adversarial training can be fragile and fail to generalize.
Paraphrase:  Public coverage treats the jump in ASR as proof that the safety
             training behind a low score is shallow.
Locators:    Article body (1%-to-88% figure, category rates, alignment
             framing); dated July 21, 2024.
Quote:       "the fact that such an obvious and easily exploitable flaw went
             undetected for so long is problematic."
```

## Contradictions

- StrongREJECT prompt count and autograder model differ across sources. The
  authors' repository states 313 prompts and a 60-prompt small subset, with the
  original autograder on GPT-4 Turbo and a newer fine-tuned Gemma 2B option.
  Some third-party summaries report 346 prompts and a 50-item subset, which
  matches an earlier description of the work. Resolution: cite the authors'
  maintained repository (313 / 60). The design and the validation are stable
  across versions; only the count and the exact grader model moved.

- GCG's AdvBench size. The paper's prose describes 500 harmful behaviors and 500
  harmful strings. The released dataset files are commonly cited as 520
  behaviors and 574 strings. This record confirmed only the paper's "500 each"
  firsthand and could not open the released files to confirm 520/574. The
  transfer ASRs do not depend on which count is correct.

- The direction in which ASR misleads is not one story. StrongREJECT shows prior
  graders overstate jailbreak success by counting mere non-refusal, so an ASR
  can be too high. Cisco and the past-tense paper show a low reported ASR
  understates a model's exposure to a cheap new attack, so an ASR can be too
  low. These are not in conflict; both are cases of the same number failing to
  carry a safety claim, and the lesson can use them as the two failure modes.
  Flagged so the editor can test the angle against both, rather than reading the
  commission's "misled people" as one direction.

- GCG's own success criterion versus StrongREJECT's critique. GCG counts "a
  reasonable attempt at executing the behavior," a non-refusal test that
  StrongREJECT later shows correlates with human judgment at string-matching
  levels. Recorded because the writer should not present GCG's transfer ASRs and
  StrongREJECT's grading standard as measuring the same thing.

## Numbers

```text
Figure: 510 unique harmful behaviors (200 standard, 100 copyright, 100
        contextual, 110 multimodal); 100 validation / 410 test
Owner:  HarmBench (arXiv:2402.04249)
Scope:  The full HarmBench behavior set; the counts a HarmBench ASR is over.
```

```text
Figure: HarmBench classifier human agreement 93.19% (vs GPT-4 88.37%, GPTFuzz
        75.42%, AdvBench refusal-classifier 69.93%, ChatGLM 64.29%)
Owner:  HarmBench (arXiv:2402.04249), Table 3
Scope:  Average agreement with human labels over the validation comparison;
        the classifier is a fine-tuned Llama 2 13B chat model.
```

```text
Figure: Generation length changes ASR by up to 30%; standardized at N=512
        tokens
Owner:  HarmBench (arXiv:2402.04249)
Scope:  Effect of the unstandardized token-count parameter on substring-match
        ASR in prior work.
```

```text
Figure: GCG on Llama 2 13B Chat = 30.2% ASR
Owner:  HarmBench (arXiv:2402.04249)
Scope:  HarmBench classifier as judge; one attack on one target; other methods
        (PAIR, TAP, few-shot) score far lower on the same model.
```

```text
Figure: StrongREJECT autograder score = (1 - refused) x (specific + convincing)
        / 2, normalized to [0,1]
Owner:  StrongREJECT (arXiv:2402.10260)
Scope:  Per-response grade; "refused" binary, specificity and convincingness on
        1-5 scales; original grader GPT-4 Turbo.
```

```text
Figure: Grader-vs-human Spearman: StrongREJECT fine-tuned 0.900, StrongREJECT
        rubric 0.846, HarmBench 0.819, PAIR 0.249, GPT-4 Judge 0.157,
        string-matching -0.394
Owner:  StrongREJECT (arXiv:2402.10260)
Scope:  Correlation of each automated grader with human rankings of jailbreak
        effectiveness; the core judge-sensitivity result.
```

```text
Figure: Yong et al. low-resource-language (Scots Gaelic) jailbreak reported 43%
        ASR on GPT-4; StrongREJECT finds the outputs vacuous, no actionable
        information
Owner:  Reported rate: Yong et al. 2023, as cited and re-scored in StrongREJECT
        (arXiv:2402.10260)
Scope:  A prior non-refusal ASR that overstated a jailbreak's real success.
```

```text
Figure: GCG ensemble transfer ASR: GPT-3.5 86.6%, GPT-4 46.9%, Claude-1 47.9%,
        Claude-2 2.1%, PaLM-2 66.0%
Owner:  GCG / Zou et al. (arXiv:2307.15043), Table 2
Scope:  One suffix optimized on Vicuna + Guanaco, transferred to black-box
        models; success = a reasonable non-refusing attempt, manually verified.
```

```text
Figure: Past-tense ASR, direct -> 20 reformulations (GPT-4 judge): GPT-4o
        1% -> 88%, GPT-4o-mini 1% -> 83%, Phi-3-Mini 6% -> 82%, Gemma-2 9B
        0% -> 74%, GPT-3.5 Turbo 0% -> 74%, Claude-3.5 Sonnet 0% -> 53%,
        Llama-3 8B 0% -> 27%, R2D2 23% -> 98%
Owner:  Andriushchenko & Flammarion (arXiv:2407.11969), Table 1
Scope:  100 JBB-Behaviors prompts; GPT-4 judge; a no-optimization rewrite
        attack.
```

```text
Figure: GPT-4o past-tense ASR by judge: GPT-4 judge 88%, Llama-3 70B judge 65%,
        rule-based judge 73%
Owner:  Andriushchenko & Flammarion (arXiv:2407.11969)
Scope:  Same responses (GPT-4o, 20 attempts), three judges; a direct
        judge-swing number.
```

```text
Figure: Judge precision / recall on 596 human-labeled completions:
        HarmBench-Llama-2-13b-cls 0.835 / 0.974; Qwen2.5-7B 0.940 / 0.174;
        Phi-3.5-mini 0.810 / 0.648; Qwen2.5-3B 0.889 / 0.059
Owner:  Gao (arXiv:2606.25487)
Scope:  Calibration of one classifier and three LLM judges against human labels.
```

```text
Figure: Benign-framing wrappers flip LLM judges 57%-100% (refusal-prefix alone
        39%-88%); classifier flip 3.4%; white-box GCG on classifier flips 70%
        (21/30)
Owner:  Gao (arXiv:2606.25487)
Scope:  Adversarial pressure on the judge, with harmful content left intact
        (human-audited).
```

```text
Figure: DeepSeek R1 ASR 100% on 50 HarmBench prompts; Llama-3.1-405B 96%,
        GPT-4o 86%, Gemini-1.5-Pro 64%, Claude-3.5 Sonnet 36%, o1-preview 26%
Owner:  Cisco (blogs.cisco.com, Jan 31 2025)
Scope:  50 uniformly sampled HarmBench prompts; automatic algorithmic jailbreak
        with refusal detection plus human oversight; temperature 0. The misled
        case's source number.
```

```text
Figure: XSTest = 250 safe prompts (10 types) + 200 unsafe contrast prompts
Owner:  Roettger et al. (arXiv:2308.01263)
Scope:  Measures exaggerated safety (over-refusal), the axis ASR does not show.
```

```text
Figure: Refusing everything yields ASR 0
Owner:  Definitional, from HarmBench (arXiv:2402.04249) and StrongREJECT
        (arXiv:2402.10260)
Scope:  HarmBench ASR counts only successful harmful completions, so a total
        refuser scores 0%; StrongREJECT's score multiplies by (1 - refused), so
        a refusal scores 0. Not a separate measurement; a consequence of both
        formulas.
```

## Source assets

```text
Asset: HarmBench Table 3 (classifier agreement rates with human labels, per
       classifier), arXiv:2402.04249
Shows: That the choice of judge is itself a number, and that the HarmBench
       classifier agrees with humans far more than refusal-string and GPT-4
       graders.
Crop:  Keep the classifier names and their agreement percentages; a chart
       rebuilt from these rows is honest only if it keeps every classifier, not
       just the winner.
```

```text
Asset: StrongREJECT grader-vs-human correlation comparison (Spearman by grader),
       arXiv:2402.10260
Shows: The spread from 0.900 down to -0.394 across graders on the same
       responses: the single clearest picture of judge sensitivity.
Crop:  Retain the full grader list including the negative string-matching bar;
       dropping the worst performers would flatter the field.
```

```text
Asset: Past-tense per-model before/after ASR (Table 1), arXiv:2407.11969
Shows: How far a no-optimization rewrite moves ASR, model by model, from a near-
       zero baseline.
Crop:  Keep the direct-request baseline beside each 20-attempt bar; the jump is
       the point, so the baseline cannot be omitted.
```

```text
Asset: Cisco per-model ASR chart (DeepSeek R1 100% beside o1-preview 26%),
       blogs.cisco.com
Shows: The headline comparison exactly as the public met it, from 50 prompts.
Crop:  A rebuilt chart must caption the 50-prompt, single-attack, single-judge
       scope; the original omits it and that omission is the lesson.
```

```text
Asset: Judge precision/recall table (classifier vs three LLM judges on 596
       labeled completions), arXiv:2606.25487
Shows: The two judge families failing in opposite directions: the classifier
       over-flags, LLM judges under-recall.
Crop:  Keep both precision and recall columns; recall alone or precision alone
       hides the trade.
```

## Discarded

```text
URL: https://arxiv.org/abs/2603.06594 ("A Coin Flip for Safety"): a second
     judge-reliability paper covering the same ground as Gao 2606.25487; not
     read in full and not needed once that source was verified. Available if the
     writer wants a corroborating judge-sensitivity source.
URL: https://huggingface.co/papers/2402.04249 and .../2402.10260: paper landing
     pages, useful only to locate the arXiv originals, which own the claims.
URL: https://www.emergentmind.com/topics/strongreject-framework: a third-party
     topic summary; superseded by the paper and the authors' repository, and the
     source of the 346/50 count this record set aside.
```
