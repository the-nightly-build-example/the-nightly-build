# Evidence record: the-mechanics/politeness-and-pressure (01)

The evidence supports the commission's two-part mechanism cleanly. The settled
half is well sourced: every study here treats tone, stakes, tips, and threats as
ordinary prompt text the model conditions on, and each finds that such text can
move the output. The unsettled half is where the strong sources converge. The
best-controlled tests on current models (Wharton Reports 1 and 3, and an
independent replication by Woolf) find no reliable average benefit from
politeness, tips, or threats, while the per-question effect is large in both
directions. The older studies that report big gains (EmotionPrompt's 115% on
BIG-Bench, Bsharat et al.'s tip and penalty principles) are real measurements
but run on older or smaller models and carry method choices that inflate the
headline number; they belong in Contradictions as the steelman, not as refutation.

Where the record is thin: several exact per-cell numbers in Yin et al. and the
per-model breakdowns in EmotionPrompt were read through a page-summarizing fetch,
not transcribed from a rendered table. I confirmed the load-bearing Yin figures
verbatim (GPT-3.5 on MMLU) and the qualitative GPT-4 / Llama-2 patterns verbatim;
the other cited cells are marked as summary-sourced and approximate. The Wharton
Report 1 PDF would not render to text; its figures come from the authors' own
Wharton write-up page, not the PDF body. Treat any single decimal below as
checkable-but-unconfirmed unless its locator says "verbatim."

## Sources

```text
URL:         https://aclanthology.org/2024.sicon-1.2/  (PDF: https://aclanthology.org/2024.sicon-1.2.pdf ; preprint: https://arxiv.org/abs/2402.14531)
Kind:        primary — Yin, Wang, Horio, Kawahara, Sekine own the politeness measurement; they built the scale and ran the models.
Establishes: That prompt politeness moves task performance, that the effect is model- and language-dependent, that the rudest phrasing usually hurts, and that maximum politeness is often not the peak.
Paraphrase:  The authors define an 8-level politeness scale (level 8 most polite, level 1 rudest) and apply it to summarization, language understanding (MMLU / C-Eval / JMMLU), and stereotypical-bias detection across English, Chinese, and Japanese, on GPT-3.5-Turbo, GPT-4, Llama-2-70B-chat (English), ChatGLM3-6B (Chinese), and Swallow-70B (Japanese). Impolite prompts often produce poor performance, but overly polite language does not guarantee the best outcome, and the optimal level differs by language.
Locators:    Abstract; Tables 4-6 (scale templates); Table 1 and Figure 3 (MMLU results). SICon 2024 (Second Workshop on Social Influence in Conversations), Miami, Nov 2024.
Quote:       "GPT-4's scores are variable but relatively stable. The highest score is achieved at level 4, and the lowest one is at level 3." / "Llama2-70B shows the most noticeable fluctuation, with scores nearly proportional to the politeness levels." / On GPT-3.5 MMLU: "GPT-3.5 achieved its highest score of 60.02 at politeness level 8 ... At level 3, a commendable score of 59.44 is maintained ... For the lowest politeness level 1, the score drops to 51.93, which is significantly lower than the other levels." (all verbatim from arXiv HTML)
```

```text
URL:         https://arxiv.org/abs/2307.11760  (HTML: https://arxiv.org/html/2307.11760v5)
Kind:        primary — Li et al. own the "EmotionPrompt" method and the reported gains.
Establishes: That appending an emotional-stakes sentence to a prompt (carrying no task information) changes output quality on their benchmarks; the claimed size of that change.
Paraphrase:  The authors add one of 11 fixed emotional-stimulus sentences (e.g. "This is very important to my career," "You'd better be sure," "Take pride in your work") to prompts and evaluate on 45 tasks across Flan-T5-Large, Vicuna, Llama 2, BLOOM, ChatGPT, and GPT-4. They report an 8.00% average relative improvement on Instruction Induction and 115% on BIG-Bench, plus a 10.9% average human-rated improvement across performance, truthfulness, and responsibility. They also document cases where the method made answers more overconfident or less comprehensive.
Locators:    Abstract; Table 4 (stimulus sentences EP01-EP11); Instruction Induction (24 tasks) and BIG-Bench (21 tasks) results tables; human study (106 participants, 30 questions, 1-5 scales); failure cases in Tables 19-20.
Quote:       Stimuli include "This is very important to my career"; "You'd better be sure"; "Take pride in your work"; "Believe in your abilities and strive for excellence."
```

```text
URL:         https://arxiv.org/abs/2312.16171  (HTML: https://arxiv.org/html/2312.16171v2)
Kind:        primary — Bsharat, Myrzakhan, Shen own the "26 principles" and their measured effect.
Establishes: That the tip/penalty/no-politeness tactics are named prompt "principles" with reported gains; that the reported gains grow with model scale.
Paraphrase:  The paper lists 26 prompting principles and tests them on LLaMA-1/2 (7B, 13B, 70B) and GPT-3.5/4 using their ATLAS benchmark. Principle 1 tells the user not to be polite ("no need to add phrases like 'please' ..."), Principle 6 is "I'm going to tip $xxx for a better solution!", and Principle 10 is "You will be penalized." Reported improvements rise with model size; the authors report large "boosting" (quality) and "correctness" gains, largest on GPT-4.
Locators:    Principles list (P1, P6, P10); results figures for boosting and correctness by model. Submitted Dec 26, 2023.
Quote:       P1: "If you prefer more concise answers, no need to be polite with LLM so there is no need to add phrases like 'please' ..." / P6: "Add 'I'm going to tip $xxx for a better solution!'" / P10: "Incorporate the following phrases: 'You will be penalized'."
```

```text
URL:         https://gail.wharton.upenn.edu/research-and-insights/techreport-threaten-or-tip/  (SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5375404)
Kind:        primary — Meincke, Mollick, Mollick, Shapiro own this controlled test of tips and threats.
Establishes: The strongest current-model evidence that tipping and threatening produce no reliable average performance gain, while per-question swings are large in both directions.
Paraphrase:  "Prompting Science Report 3: I'll pay you or I'll kill you — but will you care?" (Aug 2025) tests threat and tip prompts on Gemini 1.5 Flash, Gemini 2.0 Flash, GPT-4o, GPT-4o-mini, and o4-mini, against GPQA Diamond (198 questions) and 100 MMLU-Pro engineering questions, 25 trials per question per condition. Threats and tips give no meaningful overall improvement; only a handful of conditions reach significance, and per-question effects run from large gains to large losses.
Locators:    Report body; per-question effect ranges; trial counts (4,950 runs per prompt per model on GPQA; 2,500 on MMLU-Pro).
Quote:       Per-question effects: "Improvements: Up to 36 percentage points (GPQA) and 28 percentage points (MMLU-Pro); Decreases: Up to -28 percentage points (GPQA) and -35 percentage points (MMLU-Pro)" despite negligible average effect. A "your mother has cancer" plea moved only Gemini 2.0 Flash, by ~10 points.
```

```text
URL:         https://gail.wharton.upenn.edu/research-and-insights/tech-report-prompt-engineering-is-complicated-and-contingent/  (preprint: https://arxiv.org/abs/2503.04818 ; SSRN 5165270)
Kind:        primary — same Wharton team owns this test of politeness and formatting.
Establishes: That politeness has no reliable aggregate effect on a hard benchmark and that its per-question swing is very large; that removing formatting instructions does hurt.
Paraphrase:  "Prompting Science Report 1: Prompt Engineering is Complicated and Contingent" tests prompt variations on GPT-4o and GPT-4o-mini against GPQA Diamond with 100 repetitions per condition. Politeness ("Please" vs commanding phrasing) can shift a single question by up to ~60 points in either direction, but the differences wash out across the full set. Formatting changes, unlike politeness, showed a consistent direction (removing formatting hurt).
Locators:    Report body (politeness and formatting sections). arXiv 2503.04818.
Quote:       "Saying 'Please' versus 'I order' can dramatically shift performance by up to 60 percentage points in either direction, though these differences balance out across the full dataset." (from Wharton write-up; the arXiv PDF would not render to text for direct transcription)
```

```text
URL:         https://arxiv.org/abs/2510.04950  (PDF: https://arxiv.org/pdf/2510.04950)
Kind:        primary — a short-paper measurement that owns its result; used here as a direction-reversing data point.
Establishes: That on one current model, impolite prompts scored higher than polite ones — the opposite direction from Yin et al.
Paraphrase:  "Mind Your Tone: Investigating How Prompt Politeness Affects LLM Accuracy" (short paper) rewrites 50 base questions in mathematics, science, and history into 5 tone variants (Very Polite, Polite, Neutral, Rude, Very Rude), 250 prompts total, on ChatGPT-4o. Accuracy rose from 80.8% for Very Polite to 84.8% for Very Rude — rude beat polite, contradicting the earlier association of rudeness with worse outcomes.
Locators:    Abstract; results table. Small n (250 prompts, one model); short paper.
Quote:       "impolite prompts consistently outperformed polite ones, with accuracy ranging from 80.8% for Very Polite prompts to 84.8% for Very Rude prompts."
```

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary — Ouyang et al. own the InstructGPT / RLHF training method.
Establishes: The mechanism-step owner for post-training: models are fine-tuned on human preference rankings, so responsiveness to tone and stated stakes is a trained disposition, not raw pretraining. (Commission says link the taught lesson, not re-teach; this is the owning document for the one sentence of mechanism.)
Paraphrase:  GPT-3 is fine-tuned first on labeler demonstrations, then with reinforcement learning from human feedback using a dataset of labeler rankings of model outputs. Labelers ranked outputs by helpfulness, so the reward model encodes human preference for helpful, compliant answers.
Locators:    Abstract; method section.
Quote:       "we collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback."
```

```text
URL:         https://minimaxir.com/2024/02/chatgpt-tips-analysis/
Kind:        secondary — Max Woolf runs his own experiment, but on the viral claim he is reporting from outside the originating party and his own result is explicitly inconclusive. Used as independent-replication context for the anecdote.
Establishes: That an independent, quantified attempt to reproduce the "tip for better output" claim did not find a consistent effect; it also records the origin of the viral claim.
Paraphrase:  Woolf tests monetary tips ($100 to $100,000), non-monetary incentives (world peace, concert tickets), fines, and death threats on gpt-3.5-turbo-0125 (length control, MSE to a 200-character target) and gpt-4-0125-preview (GPT-4 rating output quality Yes/No). Most p-values stay high; no consistent pattern; the highest-quality output had neither tip nor threat. He calls the result "inconclusive" and says larger samples are needed.
Locators:    Experiment sections; conclusion. Feb 2024 post; traces the claim to a Dec 2023 viral tweet by "thebes."
Quote:       Bottom line "inconclusive"; "World Peace" was the strongest length effect, and "DEATH (CAPS)" outperformed a normal death threat — i.e. no coherent incentive gradient.
```

```text
URL:         https://www.techradar.com/computing/artificial-intelligence/new-chatgpt-prompt-goes-viral-with-sam-altmans-approval
Kind:        secondary — trade-press coverage of the viral anecdote; reports the claim, does not own or test it.
Establishes: Only that the "$200 tip" claim went viral and was widely repeated (folklore, not measurement). Supports "a claim was made," not "the claim is true."
Paraphrase:  Coverage of the December 2023 "thebes" tweet reporting that offering ChatGPT a tip (escalating to $200) appeared to improve a PyTorch code answer. This is the folklore the commission wants separated from controlled measurement.
Locators:    Article body.
Quote:       The originating user reported making "a shitpost about tipping chatgpt," then testing it and concluding "IT ACTUALLY WORKS WTF." One anecdote, one task, no controls.
```

## Contradictions

- **EmotionPrompt and Bsharat et al. report large positive effects; the
  controlled current-model studies do not.** EmotionPrompt's headline 115% on
  BIG-Bench and Bsharat et al.'s tip/penalty principles are the strongest
  evidence that a specific trick helps a lot. Two things blunt them against the
  commission's angle. (1) Models and vintage: both run mostly on 2023-era or
  small open models (Flan-T5, Vicuna, BLOOM, LLaMA-1/2, GPT-3.5); the null
  results (Wharton, Woolf) run on 2024-2025 models (GPT-4o, o4-mini, Gemini 2.0).
  The pattern across sources is that the effect shrinks as models get stronger —
  Yin et al. show GPT-4 nearly flat while Llama-2-70B swings widely. (2) Method:
  EmotionPrompt's 115% is a *relative* gain and the summary indicates it is drawn
  against a "max" aggregation, which inflates a headline versus an average;
  Bsharat et al.'s ATLAS uses human/GPT quality judgments rather than a fixed
  answer key. These are real measurements and must be steelmanned, but they do
  not establish reliable improvement on modern models.

- **Direction of the politeness effect is not consistent across studies.** Yin et
  al.: rude prompts usually hurt, polite usually helps (though not maximally).
  "Mind Your Tone": rude *beat* polite on ChatGPT-4o (84.8% vs 80.8%). Wharton
  Report 1: politeness had no reliable aggregate direction at all. This
  disagreement is itself the commission's point — the sign of the effect is not
  stable — but it means no source supports "being polite reliably helps."

- **No source found that a specific trick reliably and substantially helps on a
  current frontier model.** This was the search target for breaking the angle. The
  closest positives are older-model or aggregation-inflated (above). Recorded so
  the editor can see the angle was tested, not assumed.

## Numbers

```text
Figure: 8-level politeness scale (8 = most polite, 1 = rudest)
Owner:  Yin et al. 2024 (2402.14531), Tables 4-6
Scope:  Prompt templates per language (EN/ZH/JA); the independent variable, not a result.
```

```text
Figure: GPT-3.5 on MMLU (English) — 60.02 (level 8) / 59.44 (level 3) / 51.93 (level 1, rudest)
Owner:  Yin et al. 2024, Table 1 / Figure 3 (verbatim-confirmed)
Scope:  Accuracy on MMLU, GPT-3.5-Turbo; peak-to-rudest gap ~8.1 points; peak at most-polite but level 3 nearly ties it.
```

```text
Figure: GPT-4 on MMLU — "relatively stable," peak at level 4, lowest at level 3
Owner:  Yin et al. 2024 (verbatim-confirmed, qualitative; exact cells not transcribed)
Scope:  Accuracy, GPT-4; the strongest model showed the smallest politeness sensitivity.
```

```text
Figure: Llama-2-70B on MMLU — scores "nearly proportional to the politeness levels" (largest swing)
Owner:  Yin et al. 2024 (verbatim-confirmed, qualitative)
Scope:  Accuracy, Llama-2-70B-chat; smaller/open model, largest sensitivity to rudeness.
```

```text
Figure: EmotionPrompt — +8.00% relative (Instruction Induction), +115% relative (BIG-Bench), +10.9% human-rated
Owner:  Li et al. 2023 (2307.11760)
Scope:  8.00% averaged over 24 Instruction-Induction tasks; 115% is a relative gain drawn against a max aggregation over 21 BIG-Bench tasks (inflation caveat); 10.9% across performance/truthfulness/responsibility, 106 participants, ~30 questions, 1-5 scales. Models: Flan-T5, Vicuna, Llama 2, BLOOM, ChatGPT, GPT-4.
```

```text
Figure: Bsharat principles — P1 (no politeness), P6 ("I'm going to tip $xxx"), P10 ("You will be penalized"); gains rise with model scale
Owner:  Bsharat et al. 2023 (2312.16171)
Scope:  ATLAS benchmark; boosting and correctness reported largest on GPT-4 (summary-sourced: ~57.7% boosting / ~36.4% correctness on GPT-4 — treat as approximate, not table-transcribed). LLaMA-1/2 7B/13B/70B, GPT-3.5/4.
```

```text
Figure: Threats/tips — no meaningful average gain; per-question swing +36 to -28 pts (GPQA), +28 to -35 pts (MMLU-Pro)
Owner:  Meincke, Mollick, Mollick, Shapiro, Report 3, Aug 2025 (SSRN 5375404)
Scope:  GPQA Diamond (198 Qs) + 100 MMLU-Pro engineering Qs; 25 trials/question/condition; Gemini 1.5/2.0 Flash, GPT-4o, GPT-4o-mini, o4-mini. One plea moved only Gemini 2.0 Flash by ~10 pts.
```

```text
Figure: Politeness single-question swing up to ~60 pts either way, washes out in aggregate
Owner:  Meincke et al., Report 1 (2503.04818 / Wharton write-up)
Scope:  GPQA Diamond, GPT-4o and GPT-4o-mini, 100 repetitions/condition. Formatting removal hurt consistently; politeness did not have a reliable direction.
```

```text
Figure: Very Polite 80.8% vs Very Rude 84.8% accuracy
Owner:  "Mind Your Tone" 2025 (2510.04950)
Scope:  250 prompts (50 questions x 5 tones), ChatGPT-4o, math/science/history; rude beat polite. Small n, one model.
```

```text
Figure: Tipping/threat replication "inconclusive"; no coherent incentive gradient
Owner:  Max Woolf, Feb 2024 (secondary/independent)
Scope:  gpt-3.5-turbo-0125 (length-to-target MSE) and gpt-4-0125-preview (quality Yes/No); tips $100-$100,000, fines, death threats; most p-values non-significant.
```

## Source assets

```text
Asset: Yin et al., Figure 3 — per-level performance curves on MMLU (GPT-3.5, GPT-4, Llama-2-70B)
Shows: The core visual argument in one image: a steep curve for the smaller model, a nearly flat one for GPT-4, and a peak that is not at maximum politeness. Directly renders "the effect shrinks on stronger models."
Crop:  Must retain all three model curves and the level-1-to-8 x-axis and the score y-axis; do not crop to a single model, which would lose the flat-vs-steep contrast that is the point.
```

```text
Asset: Meincke et al. Report 3 — per-question effect distribution for threats/tips (histogram/scatter of gains and losses)
Shows: That the average is ~0 while individual questions move a lot in both directions — the "it does something, just not reliably the good thing" visual.
Crop:  Must retain the zero line and both tails (the +36 and -28 extremes); omitting a tail would misrepresent the symmetry.
```

```text
Asset: Li et al., Table 4 — the 11 EmotionPrompt stimulus sentences
Shows: The exact folklore phrasings ("This is very important to my career," "You'd better be sure") as fixed experimental strings, making concrete that the added text carries no task information.
Crop:  Keep the sentence list; the ID column (EP01-EP11) is optional.
```

```text
Asset: Bsharat et al. — principles list showing P1, P6, P10 verbatim
Shows: That "tip $xxx" and "you will be penalized" are literally codified prompt advice, grounding the folklore in a cited primary.
Crop:  Retain the three principle rows with their exact wording.
```

## Discarded

```text
URL: https://medium.com/@nathanbos/do-i-have-to-be-polite-to-my-llm-326b869a7230  — secondary blog summarizing Yin et al.; the primary is cited directly, so this adds nothing.
URL: https://ai-scholar.tech/en/articles/chatgpt/JMMLU  — secondary summary of the same Yin study; superseded by the primary.
URL: https://medium.com/aimonks/emotionprompt-elevating-ai-with-emotional-intelligence-baee341f521b  — promotional secondary summary of EmotionPrompt; primary read directly.
URL: https://www.windowscentral.com/software-apps/chatgpt-will-provide-more-detailed-and-accurate-responses-if-you-pretend-to-tip-it-according-to-a-new-study  — trade-press restating the tip claim; one more retelling of the same origin, not independent confirmation.
URL: https://twistedsifter.com/2024/02/... ("gave ChatGPT $100 to make money")  — unrelated stunt about earning money, not about tipping affecting output quality.
URL: https://arxiv.org/pdf/2605.30913 (Toxic HallucinAItions) and https://arxiv.org/html/2604.07369v1 (emotional intensity) and https://arxiv.org/html/2604.02236 (emotional framing)  — adjacent but not needed to meet the source policy; not opened past the search snippet, so not cited.
```
