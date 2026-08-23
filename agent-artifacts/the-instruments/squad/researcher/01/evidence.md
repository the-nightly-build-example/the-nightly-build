# Evidence: the-instruments/squad (01)

The evidence supports the lesson's spine firmly and from primaries: how EM and F1
are computed (read from the official evaluation script and the SQuAD 1.0 paper),
SQuAD 1.0's scale and span-answer construction, exactly how the human number was
measured, the Jia & Liang adversarial collapse, and why SQuAD 2.0 was built. It
also forces one correction to the commission. The commission states that in
January 2018 Microsoft and Alibaba systems "crossed the reported human F1." The
primary leaderboard snapshot, the SQuAD 2.0 paper's own wording, and the Stanford
researcher's own announcement all show the crossing was on **exact match only**;
on F1 humans still led by about 2.6 points. This does not weaken the commissioned
angle (a number read as more than it was), it sharpens it, but the specific "human
F1" claim in the commission is wrong and must be rewritten to "human exact match."
The record is thin in only one place: the precise SQuAD 2.0 train/dev/test split
counts were not confirmed against the paper's own table and are left out; the
figure the lesson needs (53,775 unanswerable questions added) is verified.

## Sources

```text
URL:         https://aclanthology.org/D16-1264/
Kind:        primary — the paper that owns SQuAD 1.0's construction, its human
             baseline, and its EM/F1 definitions (Rajpurkar, Zhang, Lopyrev,
             Liang, EMNLP 2016). Read the published PDF directly.
Establishes: Dataset scale and construction; the two metrics; how human
             performance was measured and its exact values.
Paraphrase:  SQuAD 1.0 is 107,785 question-answer pairs on 536 Wikipedia
             articles, drawn from 23,215 paragraphs; every answer is a span of
             the passage, highlighted by a crowdworker. Two metrics score a
             prediction, both ignoring punctuation and the articles a/an/the.
             Exact match is the percentage of predictions matching any one
             ground-truth answer exactly. F1 treats prediction and ground truth
             as bags of tokens, takes the maximum F1 over all ground-truth
             answers for a question, then averages over questions (macro-average).
             Human performance was measured by collecting at least two extra
             answers per dev/test question (so each has at least three), then
             treating the second answer as the "human prediction" and scoring it
             against the remaining answers as ground truth — the same scoring a
             model gets, on one human's single answer, not a majority vote.
             Reported human test scores: 77.0 EM, 86.8 F1; dev: 80.3 EM, 90.5 F1.
             The logistic-regression model scored 40.4 EM / 51.0 F1 on test.
Locators:    Abstract; Sec. 2 intro (107,785 / 536); Sec. 3.1 (23,215 paragraphs,
             536 articles sampled from top 10,000 by PageRank); "Additional
             answers collection" (secondary-answer task); Sec. 6.1 "Model
             Evaluation" (metric definitions); Sec. 6.2 "Human Performance";
             Table 5 (dev/test EM/F1).
Quote:       "To evaluate human performance, we treat the second answer to each
             question as the human prediction, and keep the other answers as
             ground truth answers. The resulting human performance score on the
             test set is 77.0% for the exact match metric, and 86.8% for F1."
             And: "We take the maximum F1 over all of the ground truth answers
             for a given question, and then average over all of the questions."
```

```text
URL:         https://github.com/rajpurkar/SQuAD-explorer/blob/master/evaluate-v2.0.py
Kind:        primary — the official SQuAD evaluation script (Rajpurkar's repo);
             it owns the operational definition of EM and F1 the leaderboard runs.
             The blob page is anti-bot gated (403 to a bare client); the raw file
             served the code, read in full.
Establishes: The exact normalization and F1 computation, and how a no-answer
             question is scored.
Paraphrase:  normalize_answer lowercases, removes all string.punctuation
             characters, removes the whole-word articles a/an/the via regex, and
             collapses whitespace. compute_exact returns 1 only if the normalized
             gold and prediction strings are identical. compute_f1 tokenizes both
             normalized strings on whitespace, counts shared tokens with a Counter
             intersection, and returns the harmonic mean of token precision and
             recall; if either side is empty (a no-answer), F1 is 1 only if both
             are empty, else 0. get_raw_scores takes the max of compute_exact and
             of compute_f1 over all gold answers for the question. This is the
             machine form of the paper's prose definition.
Locators:    Functions normalize_answer, compute_exact, compute_f1, get_raw_scores.
Quote:       "def remove_articles(text): regex = re.compile(r'\b(a|an|the)\b',
             re.UNICODE)" and "# If either is no-answer, then F1 is 1 if they
             agree, 0 otherwise".
```

```text
URL:         https://aclanthology.org/D17-1215/
Kind:        primary — Jia & Liang, "Adversarial Examples for Evaluating Reading
             Comprehension Systems," EMNLP 2017. Owns the adversarial method and
             the measured drops. Read the published PDF directly.
Establishes: The distractor-sentence method and the exact F1 collapse it caused
             across published SQuAD systems, plus the human control.
Paraphrase:  The attack appends one sentence to the paragraph that does not change
             the correct answer or mislead a human. AddSent builds it: mutate the
             question (antonyms for nouns/adjectives, nearest GloVe neighbors for
             named entities and numbers), invent a fake answer of the right type,
             turn the two into a declarative sentence by ~50 parse rules, then have
             crowdworkers fix the grammar. AddAny instead runs local search over
             common words to minimize the model's F1, producing word salad. Across
             the sixteen tested models, average F1 fell from 75.4% to 36.4% under
             AddSent (the abstract rounds this to "an average of 75% ... to 36%").
             For the four models the authors attacked with every adversary
             (Match-LSTM and BiDAF, single and ensemble), AddSent drove average F1
             from 75.7% to 31.3%, and AddAny to 6.7%. In a human control on
             AddSent, human F1 fell only from 92.6 to 79.5 (a 13.1-point drop, much
             of it from AddSent picking the worst of up to five paragraph-question
             pairs); on the model-independent AddOneSent humans dropped just 3.4
             points. In 96.6% of model failures the model's predicted span sat
             inside the inserted sentence.
Locators:    Abstract; Sec. 1 (84.7% F1 state-of-the-art at the time; overstability);
             Sec. 4.2 "Main Experiments" (75.7->31.3; 75.4->36.4); Table 3 (all
             sixteen models); Sec. 4.3 "Human Evaluation" and Table 4 (92.6 / 79.5
             / 89.2); Sec. 4.4 "Analysis" (96.6%).
Quote:       "In this adversarial setting, the accuracy of sixteen published models
             drops from an average of 75% F1 score to 36%; when the adversary is
             allowed to add ungrammatical sequences of words, average accuracy on
             four models decreases further to 7%." And: "In 96.6% of model
             failures, the model predicted a span in the adversarial sentence."
```

```text
URL:         https://aclanthology.org/P18-2124/
Kind:        primary — Rajpurkar, Jia, Liang, "Know What You Don't Know:
             Unanswerable Questions for SQuAD," ACL 2018 (SQuAD 2.0). Owns the 2.0
             construction, its metric change, and its human number. Read the PDF.
Establishes: Why 2.0 exists, how many unanswerable questions were added, how the
             metric handles abstention, and the human and model scores. Also the
             authors' own account of the January-2018 crossing and of the 1.0
             human baseline's weakness.
Paraphrase:  2.0 adds 53,775 new unanswerable questions to SQuAD 1.1's questions;
             crowdworkers wrote each to look answerable, with a plausible wrong
             answer of the right type present in the paragraph. A model must now
             also decide when no answer is supported and abstain. Scoring: a
             no-answer question's gold answer is the empty string, so a prediction
             scores EM=F1=1 only if the model also returns no answer, and 0 for any
             span it emits; models abstain when their predicted unanswerable
             probability clears a threshold tuned on dev to maximize F1. Best model
             at publication (DocQA + ELMo): 63.4 EM / 66.3 F1 on test; human: 86.9
             EM / 89.5 F1; a 23.2-point F1 gap. The same architecture scored 85.8
             F1 on SQuAD 1.1, only 5.4 below humans there. The 2.0 human number
             used ~4.8 answers per question and a majority vote; the authors note
             the 1.0 human figure "evaluated a single human's performance" and so
             "likely underestimate[s] human accuracy." The intro states plainly
             that recent systems "surpass human-level exact match accuracy" on
             SQuAD, citing the type-matching heuristics of Weissenborn et al. and
             the distractor brittleness of Jia & Liang as the reasons 1.0's number
             overstated comprehension.
Locators:    Abstract; Sec. 1 (53,775; "surpass human-level exact match accuracy";
             85.8 F1 / 5.4 points); Sec. 4.2 "Human accuracy" (majority vote, 4.8
             answers, single-human underestimate note); Sec. 5.2 "Main results" and
             Table 3 (63.4/66.3, 86.9/89.5, 23.2); scoring rule ("any other
             response gets 0, for both exact match and F1").
Quote:       "Recent work has even produced systems that surpass human-level exact
             match accuracy on the Stanford Question Answering Dataset (SQuAD)."
             And: "We note that for the original SQuAD, Rajpurkar et al. (2016)
             evaluated a single human's performance; therefore, they likely
             underestimate human accuracy."
```

```text
URL:         https://ymcui.com/snapshot/SQuAD_Leaderboard_24th_January_2018.pdf
Kind:        primary — a dated snapshot of the official SQuAD 1.1 leaderboard as of
             24 January 2018, the artifact the "superhuman" coverage was reading.
             Recorded as the snapshot's own page because the live leaderboard
             (rajpurkar.github.io/SQuAD-explorer) no longer shows this state. Read
             the PDF directly.
Establishes: The exact human and machine EM/F1 standing at the moment of the
             crossing, and that the crossing was on exact match, not F1.
Paraphrase:  Human Performance (Stanford) on SQuAD 1.1: 82.304 EM, 91.221 F1.
             Ensembles above the human EM line by this date: Hybrid AoA Reader
             82.482 / 89.281 (rank 1; Joint Lab of HIT and iFLYTEK), Microsoft
             r-net+ 82.650 / 88.493, Alibaba SLQA+ 82.440 / 88.607, and r-net
             82.136 / 88.126. Every one of these beat the human EM (82.304) and
             every one sat below the human F1 (91.221); the best machine F1 on the
             board, 89.281, still trailed humans by about 1.9 F1, and the
             Microsoft/Alibaba entries trailed by about 2.6-2.7 F1.
Locators:    Leaderboard table, top rows; "Human Performance" row; ensemble entries
             with team labels (Alibaba iDST NLP, Microsoft, CMU).
Quote:       "Human Performance   82.304   91.221"; "SLQA+ (ensemble)   82.440
             88.607"; "r-net+ (ensemble)   82.650   88.493".
```

```text
URL:         https://arxiv.org/abs/1811.11934
Kind:        primary — Alibaba's own SLQA paper ("Multi-Granularity Hierarchical
             Attention Fusion Networks," Wang et al., ACL 2018). Owns Alibaba's
             claim about its leaderboard position.
Establishes: What the winning team actually claimed, which was narrower than the
             press framing.
Paraphrase:  The team states only that its model reached first place on the SQuAD
             leaderboard for single and ensemble models as of 12 January 2018. The
             abstract makes no claim of beating human performance and does not
             frame the result as superhuman.
Locators:    Abstract.
Quote:       "At the time of writing the paper (Jan. 12th 2018), our model achieves
             the first position on the SQuAD leaderboard for both single and
             ensemble models."
```

```text
URL:         https://arxiv.org/abs/1810.04805
Kind:        primary — Devlin, Chang, Lee, Toutanova, "BERT" (2018). Owns the later
             SQuAD scores that show the benchmark did eventually track real gains.
Establishes: That within the year, a model genuinely passed the human F1 line too,
             not just EM — context for the "did the number mislead?" balance.
Paraphrase:  BERT raised SQuAD 1.1 test F1 to 93.2, above the leaderboard human F1
             of 91.2, and set SQuAD 2.0 test F1 to 83.1. Read from the abstract;
             the per-metric human comparison and single/ensemble EM breakdown sit
             in the full paper, not confirmed here.
Locators:    Abstract.
Quote:       "SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute
             improvement) ... SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute
             improvement)."
```

```text
URL:         https://www.geekwire.com/2018/microsoft-alibaba-ai-programs-beat-humans-stanford-reading-test-1st-time/
Kind:        secondary — GeekWire news coverage (Jan 2018), reporting on the
             leaderboard event from outside the parties. Fetched through a reader
             proxy after the site returned 403 to a direct request; the address
             recorded is the article's own page.
Establishes: How the coverage framed the result, and that the qualification was
             available and dropped. Repetition, not proof: it supports that the
             "beat humans at reading comprehension" framing was made, not that it
             was accurate.
Paraphrase:  The headline reads "Microsoft and Alibaba AI programs beat humans in
             Stanford reading comprehension test for 1st time." The body gives the
             exact-match scores (Microsoft 82.6, Alibaba 82.4, human 82.3) and
             quotes Alibaba calling it "the first time that a machine has
             outperformed humans on such a test." The same article embeds the
             Stanford NLP announcement, which itself limits the claim to exact
             match and says humans still lead on F1.
Locators:    Headline; paragraph with "82.6 ... 82.4 ... 82.3"; embedded tweet.
Quote:       Headline: "Microsoft and Alibaba AI programs beat humans in Stanford
             reading comprehension test for 1st time." Embedded tweet: "the first
             model (SLQA+) to exceed human-level performance on @stanfordnlp
             SQuAD's EM metric! Next challenge: the F1 metric, where humans still
             lead by ~2.5 points!"
```

```text
URL:         https://techstartups.com/2018/01/15/artificial-intelligence-ai-systems-built-alibaba-microsoft-beat-humans-stanford-university-reading-test/
Kind:        secondary — trade-press coverage (15 Jan 2018), reporting the same
             event. Read directly.
Establishes: A second, independent retelling that names the metric as exact match
             and gives the dates.
Paraphrase:  Reports Alibaba reaching the human line on 11 January and Microsoft a
             day later, with EM scores 82.44 and 82.650 against the human 82.304,
             and reproduces the Stanford NLP note that the crossing was on the EM
             metric. Uses "beat humans" framing in headline and body.
Locators:    Headline and body; embedded Stanford NLP tweet.
Quote:       "the first model (SLQA+) to exceed human-level performance on
             ... SQuAD's EM metric!"
```

## Contradictions

- **The commission's "crossed the reported human F1" is false.** Three sources in
  a position to know say the January-2018 crossing was exact match, not F1: the
  24 Jan 2018 leaderboard snapshot (human 82.304 EM / 91.221 F1; every top
  ensemble above 82.3 EM and below 89.3 F1); the SQuAD 2.0 paper's own words
  ("surpass human-level exact match accuracy"); and the Stanford NLP announcement
  quoted in both news pieces ("SQuAD's EM metric! Next challenge: the F1 metric,
  where humans still lead by ~2.5 points"). On F1 humans led by about 2.6 points
  when the "superhuman" headlines ran. The angle survives and improves — the press
  read an EM result as general reading ability — but the writer must say EM, not F1.

- **The commission's account of how the 1.0 human number was computed is imprecise.**
  It says the answers were "majority-vote / multi-reference on the dev set." The
  SQuAD 1.0 paper computed its human EM/F1 by treating one crowdworker's second
  answer as the prediction and scoring it against the other answers — a single
  human answer, no vote. Majority vote over ~4.8 answers is how SQuAD **2.0**
  measured its human number, a different method in a different paper. Do not
  attribute 2.0's method to 1.0.

- **Defense that the human baseline is a floor, not a rigged ceiling.** The SQuAD
  2.0 authors themselves write that the 1.0 human number "evaluated a single
  human's performance" and "likely underestimate[s] human accuracy." That cuts
  both ways for the lesson: it concedes the human line was soft, which means
  "superhuman" claims measured against a low bar prove even less — but it also
  means the benchmark's designers were not hiding the baseline's weakness.

- **Later work suggests SQuAD did track real progress.** BERT (late 2018) reached
  93.2 F1 on SQuAD 1.1, genuinely above the 91.2 human F1, and 83.1 F1 on 2.0. So
  within a year machines cleared the F1 line too, and the harder 2.0 metric drove
  continued gains. A reader could argue the number was directionally right and
  only the early-2018 F1 framing was premature. The lesson should not imply SQuAD
  scores were meaningless; the documented failure is specific and dated.

- **The adversarial result has an internal caveat, stated by its authors.** Human
  F1 also dropped 13.1 points on AddSent, and Jia & Liang note "much of this
  decrease can be explained by mistakes unrelated to our adversarial sentences,"
  because AddSent reports the worst of up to five question-paragraph pairs. On the
  model-independent AddOneSent humans dropped only 3.4 points. The honest reading
  is that the gap between human and model brittleness is large but not as extreme
  as the headline 75->36 model number alone implies; do not overstate it.

## Numbers

```text
Figure: 107,785 question-answer pairs
Owner:  SQuAD 1.0 paper (aclanthology.org/D16-1264)
Scope:  Full SQuAD 1.0 dataset, 2016.
```
```text
Figure: 536 Wikipedia articles; 23,215 paragraphs
Owner:  SQuAD 1.0 paper
Scope:  Source passages for SQuAD 1.0 (articles sampled from top 10,000 by PageRank).
```
```text
Figure: Human 77.0 EM / 86.8 F1 (test); 80.3 EM / 90.5 F1 (dev)
Owner:  SQuAD 1.0 paper, Table 5
Scope:  SQuAD 1.0 test/dev; single second-answer scored against remaining references.
```
```text
Figure: Logistic regression 40.4 EM / 51.0 F1 (test)
Owner:  SQuAD 1.0 paper, Table 5
Scope:  SQuAD 1.0 test; best model in the original paper.
```
```text
Figure: Human 82.304 EM / 91.221 F1
Owner:  SQuAD 1.1 leaderboard snapshot, 24 Jan 2018 (ymcui.com)
Scope:  SQuAD 1.1 test; the human line the January-2018 systems were measured against.
```
```text
Figure: Alibaba SLQA+ (ensemble) 82.440 EM / 88.607 F1; Microsoft r-net+ (ensemble)
        82.650 EM / 88.493 F1; Hybrid AoA Reader (ensemble) 82.482 EM / 89.281 F1
Owner:  SQuAD 1.1 leaderboard snapshot, 24 Jan 2018
Scope:  SQuAD 1.1 test. All above human EM (82.304); all below human F1 (91.221).
```
```text
Figure: Sixteen models' average F1 fell 75.4 -> 36.4 under AddSent (abstract: ~75 -> 36)
Owner:  Jia & Liang 2017, Sec. 4.2 / Table 3
Scope:  1,000 sampled SQuAD 1.1 dev examples.
```
```text
Figure: Four models (Match-LSTM, BiDAF; single+ensemble) 75.7 -> 31.3 F1 (AddSent),
        -> 6.7 F1 (AddAny), -> 46.1 F1 (AddCommon)
Owner:  Jia & Liang 2017, Sec. 4.2 / Table 2
Scope:  1,000 sampled SQuAD 1.1 dev examples.
```
```text
Figure: Human F1 92.6 -> 79.5 (AddSent, -13.1); 89.2 (AddOneSent, -3.4)
Owner:  Jia & Liang 2017, Table 4
Scope:  Human control; majority vote of three crowdworkers per example.
```
```text
Figure: 96.6% of model failures placed the predicted span inside the added sentence
Owner:  Jia & Liang 2017, Sec. 4.4
Scope:  Adversarial (AddSent) failures.
```
```text
Figure: 53,775 unanswerable questions added
Owner:  SQuAD 2.0 paper (aclanthology.org/P18-2124), Sec. 1
Scope:  New negatives layered onto SQuAD 1.1 to build 2.0.
```
```text
Figure: Best model (DocQA + ELMo) 63.4 EM / 66.3 F1; Human 86.9 EM / 89.5 F1;
        23.2 F1 gap
Owner:  SQuAD 2.0 paper, Table 3
Scope:  SQuAD 2.0 test at publication. Same architecture scored 85.8 F1 on SQuAD 1.1.
```
```text
Figure: BERT 93.2 F1 (SQuAD 1.1 test); 83.1 F1 (SQuAD 2.0 test)
Owner:  BERT paper (arxiv.org/abs/1810.04805), abstract
Scope:  Late 2018; above the 91.2 human F1 on 1.1.
```

## Source assets

```text
Asset: SQuAD 1.0 paper, Table 5 (model and human EM/F1 on dev and test).
Shows: The whole gap the lesson turns on in one grid — logistic regression 51.0 F1
       against the human 86.8 F1, with EM and F1 side by side so a reader sees the
       two metrics are different numbers on the same predictions.
Crop:  Keep the Human row and the Logistic Regression row with both EM and F1
       columns and the Dev/Test labels. Omit the weaker baselines if space is tight.
```
```text
Asset: SQuAD 2.0 paper, Figure 1 (two crowd-written unanswerable questions with
       plausible-but-wrong answers, keywords highlighted).
Shows: Concretely why a span-picker fails 2.0 — the paragraph contains a phrase of
       the right type that is not the answer, so "pick the closest span" scores 0.
Crop:  Keep one full example: the paragraph, the question, and the marked plausible
       wrong answer. One example carries the point; both is optional.
```
```text
Asset: 24 Jan 2018 leaderboard snapshot (top rows with the Human Performance line).
Shows: The exact moment, as a reader would have seen it: several ensembles above the
       human EM line and all of them below the human F1 line, which is the whole
       "EM not F1" correction in one image.
Crop:  Retain the Human Performance row and the top few ensemble rows with both EM
       and F1 columns and team labels. Do not crop away the F1 column — it is the point.
```
```text
Asset: Jia & Liang 2017, Figure 1 (a paragraph with the appended adversarial
       sentence and the model's wrong prediction).
Shows: The attack in one picture — one added sentence sharing question words, and
       the model jumping its answer to it while the real answer is untouched.
Crop:  Keep the original passage, the inserted sentence (visually distinct), the
       question, and the model's shifted prediction.
```

## Discarded

```text
https://ar5iv.labs.arxiv.org/abs/1606.05250: HTML conversion failed ("Fatal error");
  replaced by the ACL Anthology PDF of the same paper, read directly.
https://www.thekurzweillibrary.com/deep-neural-network-models-score-higher-than-humans-in-reading-and-comprehension-test:
  404 at fetch time; the GeekWire and techstartups secondaries already cover the
  event, so not pursued further.
https://raw.githubusercontent.com/white127/SQUAD-2.0-bidaf/master/evaluate-v2.0.py:
  a third-party copy of the eval script used only to locate the functions; replaced
  by the official rajpurkar/SQuAD-explorer script, which is the citable primary.
```
