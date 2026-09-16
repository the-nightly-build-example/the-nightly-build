# Evidence: the-instruments/mean-opinion-score (researcher 01)

The evidence fully supports all five teaching ideas in the commission, including a documented,
controlled, peer-reviewed case of idea 4: a research team re-rated the *identical* audio stimuli
from three Blizzard Challenge 2013 systems in a new listening test eight years later and watched
their Mean Opinion Scores collapse by roughly a full point apiece, purely from test context, while
system rankings held. That paper (Le Maguer, King & Harte, Interspeech 2022) is the strongest single
source for the lesson's original claim and carries an explicit, quotable verdict: "MOS is not
absolute." It is reinforced by the standard itself: ITU-T P.800.2 states in its own words that "it is
not meaningful to directly compare MOS values produced from separate experiments" without explicit
test design for that purpose. A second, independently useful pattern emerged unplanned: five
different papers, evaluating largely the same public dataset (LJSpeech) or closely comparable
corpora, reported five different MOS values for the *human ground-truth recordings themselves*
(4.32 to 4.74), which is a ready-made, fully sourced chart showing that even the "known-good" anchor
of a MOS test is not fixed. The evidence is thin in one place: I could not open the 2024 journal
extension of the Blizzard replication study (paywalled at two hosts), though I did read in full the
2022 conference paper by the same authors reporting the same core experiment, which covers the
material the commission needs. I also did not independently open the VITS paper to check its own
claim of near-human MOS; I have that claim only at second hand, from a paper that contests it.

## Sources

```text
URL:         https://www.itu.int/rec/T-REC-P.800-199608-I/en
Kind:        primary — ITU-T's own recommendation defining ACR, MOS, and the standard listening-test procedure.
Establishes: The ACR opinion scale's exact labels and numeric values; the definition of MOS as an
             arithmetic mean of these votes; the listening-test procedure (source recordings, speech
             material, listener eligibility, session length, statistical treatment) that P.808 later
             adapts for crowdsourcing; also defines DCR (DMOS) and CCR (CMOS) as the comparison-based
             alternatives the commission's idea 5 needs.
Paraphrase:  Annex B.4.5: "Quality of the speech / Score: Excellent 5, Good 4, Fair 3, Poor 2, Bad 1.
             The quantity evaluated from the scores (mean listening-quality opinion score, or simply
             mean opinion score) is represented by the symbol MOS." Annex B.3-B.4 requires reference
             conditions "so that experiments made in different laboratories or at a different time in
             the same laboratory can be sensibly compared," implying that without them they cannot be.
             Session length: "no session should last for more than 20 minutes and in no case should a
             session exceed 45 minutes" (B.3).
Locators:    §6.2 (recommended method); Annex B (Listening tests — ACR), specifically B.1 (source
             recordings), B.4.4 (listeners), B.4.5 (opinion scales — the ACR table), B.4.7 (statistical
             analysis); Annex D (DCR/DMOS); Annex E (CCR/CMOS).
Quote:       "Excellent = 5; Good = 4; Fair = 3; Poor = 2; Bad = 1 ... The arithmetic mean of any
             collection of these opinion scores is called the mean conversation-opinion score" (§A.4.2.1,
             mirrored for listening tests in B.4.5 as plain "MOS").
```

```text
URL:         https://www.itu.int/rec/T-REC-P.800.2-201305-S/en
Kind:        primary — ITU-T's own recommendation on interpreting and reporting MOS.
Establishes: The explicit, standards-body statement that MOS is not a portable absolute value, the
             mechanism (rater pool, presentation, other conditions in the same test, audio "context")
             by which it moves, and the minimum information (votes, mean, standard deviation, number
             of subjects, test plan) that must travel with any reported MOS.
Paraphrase:  §7 lists concrete factors that move a MOS for the same condition: playback equipment,
             presentation level, acoustic environment, subject profile, cross-cultural scale use,
             speech material, language, and — critically — "the quality of the other conditions in the
             experiment" and the audio bandwidth "context" of the whole test. It gives a worked
             illustration: the same G.729 codec condition can score above or below 3.9 depending on
             whether the other conditions in its test batch are worse or better than it, and a G.711
             condition scores above 4.0 in a narrow-band test but only 3.5–3.7 in a wideband one.
Locators:    §5 (introductory definition of MOS as the average of "votes" for a "condition"); §7
             (Interpreting MOS values, the source of the comparability warning); §9 (statistical
             analysis: CI, vote count, standard deviation required); §11 and Table 1 (mandatory/
             recommended fields for reporting subjective MOS — methodology, test plan, condition
             information, number of votes, subject profile, language, talker count/gender).
Quote:       "One of the most important consequences of the considerations described above is that it
             is not meaningful to directly compare MOS values produced from separate experiments,
             unless those experiments were explicitly designed to be compared, and even then the data
             should be statistically analysed to ensure that such a comparison is valid." (§7)
```

```text
URL:         https://www.itu.int/rec/T-REC-P.808-202106-I/en
Kind:        primary — ITU-T's own recommendation defining the crowdsourced listening-test procedure.
Establishes: How most current TTS MOS figures are actually produced: the qualification/training/rating
             job workflow, listener eligibility and screening (hearing test, environment check, headphone
             validation), reliability checks (gold-standard and "trapping" questions), the minimum
             number of raters per stimulus for an ACR crowdsourcing test, and an explicit statement that
             crowdsourced results are not interchangeable with lab results.
Paraphrase:  §1 (Scope): crowdsourcing methods are "complementary to" P.800/P.835 lab methods, not a
             replacement, and "the results from crowdsourcing-based methods can be expected to deviate
             to a certain extent from those of laboratory testing." §6.3.1.3: "In an ACR crowdsourcing
             experiment, each stimulus should be assessed at least by 8 individuals and each circuit
             condition with 96 votes." §6.3.5 sets listener eligibility: normal hearing (≤25 dB loss up
             to 8 kHz), native or native-level fluency, not involved in related work, no other subjective
             test in the prior 7 days (2 weeks for a listening test), never heard the same sentence lists
             before; recommends age/gender-balanced sampling. Annex A reproduces the ACR scale from
             P.800 unchanged (Excellent 5 … Bad 1), adapted for a screen-based rating widget.
Locators:    §1 (Scope); §6.1-6.4 (database structure, experiment design, listening test procedure,
             data analysis); §6.3.1.3 (rating-job minimum votes); §6.3.5 (listener eligibility);
             §6.3.8 (reliability check mechanisms — gold standard and trapping questions); §6.4.3
             (reporting requirements, additive to P.800.2); Annex A (adapted ACR opinion scale).
Quote:       "Crowdsourcing-based methods are not expected to replace laboratory testing, as there are
             fundamental differences between both methods regarding their conception, the participants
             and their motivation, as well as technical and environmental factors ... the results from
             crowdsourcing-based methods can be expected to deviate to a certain extent from those of
             laboratory testing." (§1)
```

```text
URL:         https://arxiv.org/abs/1712.05884
Kind:        primary — the paper that owns the Tacotron 2 MOS figure widely cited as "matches human
             recordings."
Establishes: The exact MOS, its comparison to a ground-truth figure from the same test, and the test's
             own setup (samples, raters, scale, rater service).
Paraphrase:  100 fixed sentences were held out from the training set of a single professional female
             speaker's 24.6-hour internal corpus. Generated audio was rated by "a human rating service
             similar to Amazon's Mechanical Turk" with "at least 8 raters" per sample, 1-5 scale in
             0.5-point steps, 95% CIs from the t-distribution. Table 1 reports MOS for six systems in
             the same test batch, side by side with ground truth, which the paper leans on directly:
             "results in an MOS comparable to that of the ground truth audio." A separate side-by-side
             test on the same 100 items found a small but statistically significant listener preference
             for the ground truth over Tacotron 2 (mean score -0.270 ± 0.155 on a -3..+3 scale),
             something the headline MOS comparison alone does not show.
Locators:    Abstract; §3.2 Evaluation; Table 1 (MOS by system); the paragraph and Fig. 2 describing the
             side-by-side comparison against ground truth.
Quote:       "Our model achieves a mean opinion score (MOS) of 4.53 comparable to a MOS of 4.58 for
             professionally recorded speech." (Abstract) Table 1: Tacotron 2 (this paper) 4.526 ± 0.066;
             Ground truth 4.582 ± 0.053.
```

```text
URL:         https://www.isca-archive.org/interspeech_2017/rosenberg17_interspeech.html
Kind:        primary — peer-reviewed study (Interspeech 2017) that owns its own bias measurements from
             46 real MOS listening tests.
Establishes: How much within-test variance a MOS conceals, from two identifiable sources (rater and
             sentence/utterance), and that ordinary t-tests on MOS are statistically inappropriate.
Paraphrase:  Across 46 Amazon Mechanical Turk TTS listening tests run 2015-2017 (5-point Bad..Excellent
             ACR scale each), the average standard deviation of individual raters' mean scores was
             0.484 MOS points; the average spread between the most lenient and harshest rater's mean was
             2.31 points (min 1.7, max 3.2) on the 1-5 scale. Two large in-person (non-AMT) tests run by
             IBM employees showed similarly large spreads (2.75 and 3.0), so the effect is not specific
             to crowd platforms. Utterance-level bias was smaller but still substantial: average spread
             1.47, std dev 0.33. The paper argues MOS is ordinal, not interval, so paired non-parametric
             tests (Mann-Whitney U with rank normalization) should replace t-tests, and shows that
             correcting for rater/utterance bias changes the measured statistical significance of system
             differences in most of the 46 tests.
Locators:    Abstract; §3 (non-parametric tests); §4 (sources of bias — participant, utterance); §7
             (measuring bias, the 0.484 / 2.31 / 1.47 figures); §8 (impact on 46 tests' significance).
Quote:       "we find that on average the mean difference between the highest and lowest scoring rater
             is over 2 MOS points (on a 5 point scale)." (Abstract)
```

```text
URL:         https://arxiv.org/abs/1910.10909
Kind:        primary — the paper that owns the ESPnet-TTS 2020 MOS table, including its Tacotron 2 figure.
Establishes: A LJSpeech MOS figure for a retrained Tacotron 2 and a same-test ground-truth figure, with
             full test setup.
Paraphrase:  100 sentences randomly held from the LJSpeech test split; evaluated on Amazon Mechanical
             Turk by 101 US-based subjects, each rating at least 20 samples on the standard 1-5 ACR
             scale (5 excellent .. 1 bad). Table 5 reports MOS with 95% CI for six systems (two
             retrained Tacotron 2 variants, two Transformer TTS variants, and two other open-source
             toolkits' pretrained models) plus ground truth.
Locators:    §4.1 (experimental condition — dataset split, six trained models); §4.3 (subjective
             evaluation — AMT, 101 subjects, scale); Table 5 (MOS with 95% CI).
Quote:       Table 5: "Groundtruth 4.46 ± 0.05 ... Tacotron2.v3 4.20 ± 0.06."
```

```text
URL:         https://arxiv.org/abs/2205.15439
Kind:        primary — the paper that owns the StyleTTS 2022 MOS table, including its Tacotron 2 + HiFi-GAN
             figure, and that explicitly discusses why its own numbers differ from other papers' claims.
Establishes: A third, later LJSpeech MOS figure attached to the name "Tacotron 2," a same-test
             ground-truth figure, full test setup, and a direct, first-hand explanation of why its VITS
             score disagrees with VITS's own reported near-human-parity result.
Paraphrase:  100 LJSpeech test-set sentences; Amazon Mechanical Turk, native English speakers based in
             the US; MUSHRA-like design (models presented together, hidden, alongside ground truth as a
             reference/anchor, unlike a plain one-at-a-time MOS test); 10 raters per set, 1-5 scale in
             0.5 increments; raters who did not rank ground truth in the top two among all models on a
             set were dropped (46 of 50 qualified). Table I: Ground Truth 4.32 ± 0.04; Tacotron 2 +
             HiFi-GAN 3.01 ± 0.06; FastSpeech 2 + HiFi-GAN 2.97 ± 0.06; VITS 3.78 ± 0.06; StyleTTS +
             HiFi-GAN 4.01 ± 0.05. The authors explicitly flag that their VITS score is much lower than
             VITS's own reported "close to ground truth" result and attribute the gap to the evaluation
             method itself (anchored MUSHRA-style vs. plain unanchored MOS), not to a difference in the
             audio.
Locators:    §III-A (Datasets); §III-C (Evaluations — AMT protocol, rater qualification); Table I
             (LJSpeech MOS); §IV-A (Model Performance, the paragraph on the VITS discrepancy).
Quote:       "We do note that our evaluation results differ from those reported in the baseline models,
             particularly for VITS. The VITS model has been reported to yield results very close to the
             ground truth ... However, in our evaluation, VITS was found not to reach ground truth
             levels of performance. The primary factor leading to this discrepancy is the difference in
             evaluation methods ... The use of a reference point in our MUSHRA-like evaluation provides
             an anchor for rating, particularly the ground truth as the reference, which potentially
             lowers the scores of other models." (§IV-A)
```

```text
URL:         https://arxiv.org/abs/2205.04421
Kind:        primary — the paper that makes the commissioned "human-level quality"/"human parity" claim
             for TTS and defines its own statistical test for it.
Establishes: The exact wording and statistical basis of a "human parity" claim, two separate same-paper
             MOS readings for "human recordings" on the same public dataset, and the paper's own
             admission that its parity claim depended on which human recordings were allowed to count
             as the reference.
Paraphrase:  Defines "human-level quality" as "no statistically significant difference between the
             quality scores of the speech generated by a TTS system and the quality scores of the
             corresponding human recordings on a test set" (Definition 1), tested via 7-point CMOS
             (-3..+3) with a Wilcoxon signed-rank test, guideline: >20 native-speaker judges, ≥50 test
             utterances. On LJSpeech, two separate listening tests are reported: Table 1 (judging four
             prior systems against "Human Recordings," 50 utterances, 20 judges) gives Human Recordings
             MOS 4.52 ± 0.11; Table 2/3 (the paper's own headline comparison, same claimed protocol: 50
             utterances, 20 judges) gives Human Recordings MOS 4.58 ± 0.13, and NaturalSpeech 4.56 ±
             0.13, CMOS -0.01, Wilcoxon p = 0.6902 (paper reports this as p >> 0.05, i.e. not
             significant) — the paper's basis for claiming "human-level quality." Footnote 4 states
             judges were told to exclude LJSpeech recordings with "strange rhythm ups and downs" from
             the human-recordings side of the comparison to keep that baseline's quality good, and that
             without this exclusion NaturalSpeech would have scored +0.09 CMOS *better* than the
             (unfiltered) human recordings.
Locators:    §2.1 (Definition 1, human-level quality); §2.2 (judgement guideline, 20 judges/50
             utterances/CMOS/Wilcoxon); Table 1 (Judgement of Previous TTS Systems — Human Recordings
             4.52 ± 0.11); §4.2, Table 2 and Table 3 (Comparison with Human Recordings — Human
             Recordings 4.58 ± 0.13, NaturalSpeech 4.56 ± 0.13, CMOS -0.01, p = 0.6902), and footnote 4.
Quote:       "Note that some human recordings in LJSpeech dataset may contain strange rhythm ups and
             downs that affect the rating score. To ensure the human recordings used for evaluation are
             of good quality, we let judges to exclude the recordings with strange rhythms from
             evaluation. Otherwise, our NaturalSpeech will achieve better CMOS than human recordings. In
             a CMOS test without excluding bad recordings, NaturalSpeech achieves +0.09 CMOS better than
             recordings." (footnote 4)
```

```text
URL:         https://arxiv.org/abs/2305.10608
Kind:        primary for its own "range-equalizing bias" experiment; secondary (but independently
             checked against the primaries above) for its remark on Tacotron 2's declining reported MOS.
Establishes: A controlled demonstration that narrowing the range of system quality in a test changes
             the MOS of systems that never changed, including how far scores can move (up to 1.28
             points), and a widely quotable observation connecting three published "Tacotron 2" MOS
             figures across years, with an explicit warning against treating that connection as a valid
             comparison.
Paraphrase:  Using the public BVCC dataset (187 TTS/voice-conversion systems, including natural speech,
             all originally rated together in one large test with 8 ratings/sample), the authors re-ran
             new listening tests that "zoom in" on progressively smaller, higher-quality subsets (50%,
             25%, 12%, 6% of the systems, keeping only the top-rated half each time), with 200 new
             listeners total. As the range narrows, statistically significant pairwise differences
             increase sharply (2 significant pairs among the top-11 systems in the original 100% test,
             vs 25 in the 6%-zoom retest), and low-ranked systems in the narrow tests lose real score:
             the largest single drop was 1.28 MOS points for a system that had never itself changed. The
             authors separately note, as an aside illustrating the same bias: Tacotron 2's own paper
             reported MOS 4.53 in 2018 "with quality close to that of natural human speech"; a 2020
             ESPnet-TTS study reported 4.20 for a retrained Tacotron 2; a 2022 study (StyleTTS) reported
             3.01 for a Tacotron 2 + HiFi-GAN baseline — and immediately caution that this sequence is
             not a valid direct comparison because listeners, sentences, training data, vocoders and
             even the rating-scale increment differed each time.
Locators:    Abstract; §3.2 (new listening test design — BVCC, zoom levels, listener counts in Table 1);
             §4.1-4.2 (score distributions and emergence of significant differences, Table 2); §4.4 and
             Table 4 (largest score drops, the 1.28-point figure); §5 Conclusions (the Tacotron 2
             paragraph).
Quote:       "Of course, it's not at all valid to make direct comparisons between MOS tests with
             completely different listeners, test sentences, training data, configurations, vocoders,
             and even rating scale increments. However, this general decrease in MOS indicates the
             possibility of range-equalizing bias, and that an unintentional 'zooming in' may be taking
             place as speech synthesis technology improves." (§5)
```

```text
URL:         https://www.isca-archive.org/interspeech_2022/lemaguer22_interspeech.html
Kind:        primary — peer-reviewed study (Interspeech 2022) that owns the controlled replication
             experiment. This is the strongest documented case found for the commission's required
             cross-test MOS-misled-people instance.
Establishes: A same-stimuli, controlled measurement of how much MOS can move purely from test context —
             the identical recordings of three historical TTS systems, re-rated eight years later, drop
             about a full MOS point each while their relative ranking survives; and an explicit,
             citable verdict that MOS is not an absolute score and should not be pooled across tests,
             including for training automatic MOS predictors.
Paraphrase:  The authors took the exact audio submitted by three top-tier Blizzard Challenge 2013
             systems (labelled K, N, C, representing the hybrid, HMM and unit-selection synthesis
             families) plus the original natural-voice recordings, and re-ran the same sentences in a
             new 2021 online listening test (Prolific, 59-60 usable native English listeners) alongside
             four newly trained modern neural systems (Tacotron/FastPitch × WaveNet/Parallel WaveGAN).
             The 2013 lab test (in-person, University of Edinburgh) had rated: system K mean MOS 3.81,
             system N 3.22, system C 2.88, natural voice ("A") 4.74. The identical audio, re-rated in
             2021 alongside the modern systems: K 2.62, N 2.00, C 1.96 — drops of 1.19, 1.22 and 0.92
             MOS points respectively for stimuli that had not changed at all. The downsampled natural
             voice ("A-16," same speaker/content, only bandwidth reduced) scored 4.39, a smaller but
             present drop the authors attribute mainly to test context rather than the bandwidth change,
             since downsampling itself did not significantly affect the rating in a companion check.
             Despite the collapse in absolute scores, pairwise significance testing (Wilcoxon
             signed-rank with Bonferroni correction) shows system K still rated significantly more
             natural than N and C, which the 2021 data no longer distinguishes from each other: the
             scores were "compressed," not reordered.
Locators:    Abstract; §2.1.1 (selected historical systems); §2.3 (recruitment/evaluation protocol);
             §3.2 and Table 1 (MOS by system, original vs. extension, with mean/median/std/n); §3.4 "How
             reliable is MOS?" (the point-drop analysis and the paper's conclusions).
Quote:       "Exactly the same stimuli were presented to listeners in both listening tests, yet the MOS
             scores given by listeners to each and every one of these systems dropped by a full point.
             ... The fact remains that MOS is not absolute. Researchers should never report an isolated
             MOS out of context and must be cautious about their conclusions when using this metric. ...
             It is certainly not valid to simply pool MOS obtained from multiple listening tests, to
             form a training set for a MOS prediction model." (§3.4)
```

## Contradictions

- The commission's premise — a "human parity" MOS comparison that misled people — is best matched not
  by a single false public claim but by a chain of self-undermining evidence inside the strongest
  parity paper itself. NaturalSpeech (Tan et al. 2022) reports "no statistically significant
  difference from human recordings" (CMOS -0.01, p ≈ 0.69) and calls this "human-level quality," but
  its own footnote 4 discloses that judges were instructed to drop poor-quality human recordings from
  the reference set to obtain that result, and that without the exclusion the system would have scored
  *better* than the (unfiltered) human baseline by +0.09 CMOS. A claim of parity with "human
  recordings" turns out to depend on which human recordings were allowed to count — the opposite of an
  absolute, portable finding.
- ITU-T P.800.2 states plainly that MOS values from separate experiments should not be compared "unless
  those experiments were explicitly designed to be compared, and even then the data should be
  statistically analysed to ensure that such a comparison is valid" (§7). Every "human parity" or
  progress-over-time narrative built from separately published MOS figures — including the sequence
  the reader is likely to encounter in marketing or press coverage ("System X scored 4.5, near human
  quality") — violates this on its face, because the comparison was never designed as one experiment.
- The two "Human Recordings" figures inside the NaturalSpeech paper itself disagree: 4.52 ± 0.11 (Table
  1, in a test batched with four prior systems) versus 4.58 ± 0.13 (Table 2, in the paper's headline
  test batched only with NaturalSpeech). The paper does not state outright that these were two
  separate listening-test administrations rather than one test reported twice with different subsets
  selected for each table; the differing means, sample sizes implied by the differing CIs, and the
  separate section/table framing make two administrations the more likely reading, but I record this
  as inferred, not confirmed by an explicit methods statement, and flag it for the writer/editor to
  weigh accordingly.
- Cooper & Yamagishi's observation that a system called "Tacotron 2" scored 4.53, then 4.20, then 3.01
  across three papers (2018, 2020, 2022) is frequently reusable as "proof the system's quality
  declined," but the authors explicitly say the opposite: the comparison is not valid, because the
  three tests differ in listeners, sentences, training data, vocoder, and even the scale's rating
  increment. The teaching point is that this looks like a real trend and is not one — which is itself
  the lesson's idea 4, made concrete without needing a villain.
- The StyleTTS paper's own account of why its VITS score (3.78, well below VITS's own reported
  near-ground-truth result) differs from VITS's published claim is a first-hand admission that
  evaluation *method* (anchored MUSHRA-style vs. plain MOS) moves scores independent of audio quality.
  I was not able to open the VITS paper itself to read its original claim in its own words, so this
  contradiction is recorded from one side only — the side disputing the claim — and should be presented
  as such, not as a confirmed two-sided contradiction.
- Rosenberg & Ramabhadran document large *within-test* variance (rater-to-rater spread up to 2.3 MOS
  points; utterance-to-utterance spread up to 1.47) that is a different mechanism from the *cross-test*
  range-equalizing/context bias documented by Le Maguer et al. and Cooper & Yamagishi. Both erode
  confidence in a MOS figure, but for different reasons, and should not be collapsed into one
  explanation in the lesson.

## Numbers

```text
Figure: ACR opinion scale — Excellent=5, Good=4, Fair=3, Poor=2, Bad=1
Owner:  ITU-T P.800 (1996), Annex B.4.5, reused verbatim by ITU-T P.808 (2021), Annex A.1
Scope:  The scale definition itself, not a measurement; applies to every MOS figure below
```

```text
Figure: minimum 8 raters per stimulus, 96 votes per condition, in an ACR crowdsourcing test
Owner:  ITU-T P.808 (2021), §6.3.1.3
Scope:  Recommended minimum for a single crowdsourced ACR listening test; several TTS papers below meet
        or exceed the per-stimulus minimum (Tacotron 2: "at least 8 raters"; ESPnet-TTS: ~20 raters per
        sample from 101 subjects) but none report the full 96-vote-per-condition figure explicitly
```

```text
Figure: rater-to-rater MOS spread, mean 2.31 points (range 1.7-3.2), across 46 TTS listening tests
Owner:  Rosenberg & Ramabhadran, Interspeech 2017, §7
Scope:  46 AMT-run TTS listening tests, Oct 2015-Feb 2017, IBM Watson; 5-point ACR scale; within-test
        (not cross-test) variance
```

```text
Figure: Tacotron 2 MOS 4.526 ± 0.066; ground truth (same test) 4.582 ± 0.053
Owner:  Shen et al. (Tacotron 2), ICASSP 2018, Table 1
Scope:  100 held-out sentences, internal 24.6-hour single-professional-female-speaker corpus (not
        LJSpeech), ≥8 raters/sample, 95% CI via t-distribution
```

```text
Figure: ESPnet-TTS Tacotron2.v3 MOS 4.20 ± 0.06; ground truth (same test) 4.46 ± 0.05
Owner:  Hayashi et al. (ESPnet-TTS), ICASSP 2020, Table 5
Scope:  LJSpeech, 100 sentences, 101 AMT US-based subjects rating ≥20 samples each, 95% CI
```

```text
Figure: NaturalSpeech-context Human Recordings MOS 4.52 ± 0.11
Owner:  Tan et al. (NaturalSpeech), 2022, Table 1
Scope:  LJSpeech, 50 utterances, 20 judges; test batched with FastSpeech 2, Glow-TTS, Grad-TTS, VITS
```

```text
Figure: NaturalSpeech-headline Human Recordings MOS 4.58 ± 0.13; NaturalSpeech MOS 4.56 ± 0.13; CMOS -0.01 (p=0.6902)
Owner:  Tan et al. (NaturalSpeech), 2022, Table 2 and Table 3
Scope:  LJSpeech, 50 utterances, 20 judges; test batched only with NaturalSpeech; ground-truth
        recordings with "strange rhythm ups and downs" excluded from the reference set per footnote 4
```

```text
Figure: StyleTTS-context Ground Truth MOS 4.32 ± 0.04; Tacotron 2 + HiFi-GAN MOS 3.01 ± 0.06
Owner:  Li, Han & Mesgarani (StyleTTS), 2022, Table I
Scope:  LJSpeech, 100 samples, 46 of 50 qualified AMT native-English raters (10 raters/set),
        MUSHRA-like hidden-reference design (not plain unanchored MOS)
```

```text
Figure: Blizzard 2013 natural voice MOS 4.74 (original, in-person) vs 4.39 (2021 downsampled re-test)
Owner:  Le Maguer, King & Harte, Interspeech 2022, Table 1
Scope:  Same speaker/content; "A" = original 2013 44.1 kHz condition (180 votes, novel sentences only);
        "A-16" = 16 kHz downsampled version rated in the 2021 online Prolific re-test (118 votes)
```

```text
Figure: same-stimuli MOS drop for historical Blizzard 2013 systems, 2013 vs 2021 re-test
Owner:  Le Maguer, King & Harte, Interspeech 2022, Table 1
Scope:  System K: 3.81 -> 2.62 (n=347 -> 236 votes); System N: 3.22 -> 2.00 (387 -> 236); System C:
        2.88 -> 1.96 (380 -> 236). Identical audio stimuli in both tests; the only manipulated variable
        is which other systems (2013 historical peers vs 2021 modern neural systems) shared the test.
```

```text
Figure: largest range-equalizing score drop, 1.28 MOS points, for a system whose audio never changed
Owner:  Cooper & Yamagishi, Interspeech 2023, Table 4
Scope:  BVCC dataset system BC2011-G, comparing its rating in the original 187-system test to a
        retest containing only the top 11 (6%) highest-rated systems
```

```text
Figure: number of statistically significant pairwise differences among the same top-11 systems: 2 (in the
        original 187-system test) vs 25 (in the 6%-zoom retest of just those 11 systems)
Owner:  Cooper & Yamagishi, Interspeech 2023, Table 2
Scope:  Same 11 systems' scores, re-analyzed under two different test-range conditions
```

**Preserved series — ground-truth ("human recordings") MOS across studies, for a possible chart:**

```text
4.74  Blizzard 2013 original lab test, 44.1 kHz, novel sentences only, n=180 (Le Maguer et al. 2022, Table 1)
4.58  Tacotron 2 paper's internal corpus, 100 sentences, >=8 raters (Shen et al. 2018, Table 1)
4.58  NaturalSpeech headline test, LJSpeech, 50 utts/20 judges, "strange rhythm" recordings excluded (Tan et al. 2022, Table 2)
4.52  NaturalSpeech judgement test, LJSpeech, 50 utts/20 judges (Tan et al. 2022, Table 1)
4.46  ESPnet-TTS test, LJSpeech, 100 sentences/101 AMT raters (Hayashi et al. 2020, Table 5)
4.39  Blizzard 2013 extension re-test, 16 kHz downsampled, online Prolific (Le Maguer et al. 2022, Table 1)
4.32  StyleTTS test, LJSpeech, 100 samples/46 AMT raters, MUSHRA-like anchored design (Li et al. 2022, Table I)
```

## Source assets

```text
Asset: ITU-T P.808 (2021), Figure 1 — workflow diagram of Qualification job -> Training job -> Rating
       job, with a "re-training" feedback loop
Shows: The actual pipeline behind a crowdsourced MOS test, which the reader has never seen; makes idea 2
       (where the number comes from, step by step) concrete without prose
Crop:  Keep all three boxes and the re-training arrow; it is small and self-contained
```

```text
Asset: Le Maguer, King & Harte (2022), Figure 1 — boxplot of MOS by system, yellow (2013 original) vs
       green (2021 re-test, suffix "-E"), same three historical systems shown twice
Shows: The same audio's score collapsing visually, side by side, when the surrounding systems change;
       this is the single clearest visual argument for idea 4 in any source read
Crop:  This is the paper's own figure and cannot be reproduced verbatim per house chart policy (charts
       must be rendered from our own committed chart-N.py); however, the underlying numbers are in the
       paper's Table 1 (system, mean, median, std, n) and are fully reproducible as our own chart —
       see the "same-stimuli MOS drop" figures above
```

```text
Asset: the seven ground-truth MOS figures compiled above under "Preserved series"
Shows: That the number attached to real human recordings — the ostensibly fixed anchor of any MOS test
       — itself ranges from 4.32 to 4.74 depending on which paper, dataset, and test ran it
Crop:  If charted, split or clearly label the two points from a different, non-public corpus (Shen et
       al.'s internal 24.6-hour corpus) from the five points that are all LJSpeech, so the chart does
       not imply they are the same recordings under test; caption should name each paper/year, since the
       number alone invites exactly the naive comparison the lesson warns against
```

```text
Asset: NaturalSpeech (2022), Table 1 vs Table 2/3 — two "Human Recordings" MOS rows in one paper
Shows: A same-paper, same-dataset illustration that the reference value moves depending on what else was
       in the test batch, without needing a second paper to make the point
Crop:  Present both rows together with their exact CIs; do not average them, since they come from
       differently composed test batches (see Contradictions)
```

## Discarded

```text
URL: https://www.sciencedirect.com/science/article/abs/pii/S0885230823000967 (Le Maguer, King & Harte,
     "The limits of the Mean Opinion Score for speech synthesis evaluation," Computer Speech & Language
     84, 2024) — gated, not dead: returned HTTP 403. Also tried the University of Edinburgh Research
     Explorer's linked accepted-manuscript PDF (research.ed.ac.uk/files/398883062/2023_csl_mos.pdf),
     which also returned HTTP 403. This is the journal-length extension of the Interspeech 2022 paper by
     the same authors that I did read in full (see Sources); an AI-search summary (not independently
     verified by me) suggests the journal version adds a fourth replication experiment and the phrase
     "MOS is a relative score," consistent with the conference paper's own conclusion. I could not verify
     any number from this specific version and did not cite any of its content as read.
```

```text
URL: (VITS paper, Kim, Kong & Son, "Conditional variational autoencoder with adversarial learning for
     end-to-end text-to-speech," ICML 2021) — not opened. Its claim of a MOS "very close to ground
     truth" is quoted only secondhand, inside the StyleTTS paper that disputes it (see Sources and
     Contradictions). I did not verify VITS's own reported figure or test setup against the original.
```

```text
URL: openreview.net/forum?id=omwBmLXjPi (an OpenReview listing for the Le Maguer et al. CSL 2024 paper)
     — rejected: page served only a browser verification / login screen, no paper content.
```
