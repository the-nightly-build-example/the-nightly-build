# Evidence: the-instruments/word-error-rate (01)

The record supports every question in the brief from primary documents. The
definition of Word Error Rate, its minimum-edit-distance alignment, and its
component counts are owned by the NIST sclite documentation, with the summed
formula and the ">100%" property owned by the Jurafsky & Martin ASR chapter; a
worked S/D/I micro-example is verified below by hand and by a Levenshtein
computation. The "human parity" case is read directly from Microsoft's 2016
paper (system 5.8%/11.0% versus a professional-transcriber baseline of
5.9%/11.3% on Switchboard/CallHome) and its 2017 update (5.1% on Switchboard).
IBM's Saon et al. paper is the primary that breaks the strong reading of parity:
with a more careful transcription protocol it measured the human CallHome rate
at 6.8%, not 11.3%. The evidence is thin in two places, both flagged in
Contradictions. First, the commission's phrase "a failure WER barely penalizes"
overstates what the Whisper paper supports: hallucinated words are scored as
insertions and substitutions and do raise WER on the segments where they occur.
The defensible claims are that a corpus-level WER averages those catastrophic
segments away, and that WER is meaning-blind, scoring a fluent fabrication the
same as an audible mishearing of equal length. Second, on the clean Switchboard
subset the parity claim held up under IBM's harder human baseline (Microsoft's
2017 system reached 5.1%, matching IBM's best human transcriber), so the angle
is strongest on CallHome and on cross-corpus generalization, not on Switchboard
alone.

## Sources

```text
URL:         https://arxiv.org/abs/1610.05256
Kind:        primary. Xiong et al. (Microsoft) are the authors of the human-parity
             claim and the party that ran both the ASR system and the human
             measurement. They own these numbers firsthand.
Establishes: Microsoft's automated system reached 5.8% WER on the Switchboard and
             11.0% on the CallHome portions of the NIST 2000 CTS test set, against
             a professional-transcriber baseline of 5.9% and 11.3%. Critically, it
             establishes HOW that human baseline was measured: an existing weekly
             commercial-vendor pipeline doing two-pass transcription (one pass from
             scratch, one listener correcting), given the same audio segments as
             the recognizer, with no multi-party adjudication.
Paraphrase:  The paper measures human error by slipping the NIST 2000 evaluation
             audio into a commercial transcription vendor's normal weekly work-list
             unannounced. The vendor does a first transcription pass and a second
             correction pass, nothing more elaborate. Scored with the NIST protocol,
             the result is 5.9% on Switchboard and 11.3% on CallHome. The authors
             note the two subsets differ almost by a factor of two, so no single
             "human error rate" number is appropriate, and that the old widely cited
             4% figure came from an unrecoverable personal communication. An error
             analysis finds the human and machine transcribers make broadly the
             same errors, dominated by short function words.
Locators:    Abstract; Sec. 1 (paras on the 4% figure and the 5.9%/11.3% finding);
             Sec. 2 "Human Performance" (the two-pass vendor pipeline description);
             Table 9 (literature + human comparison); Table 13 (S/D/I breakdown).
Quote:       "To measure human performance, we leveraged an existing pipeline in
             which Microsoft data is transcribed on a weekly basis. This pipeline
             uses a large commercial vendor to perform two-pass transcription."
             "Aside from the standard two-pass checking in place, we did not do a
             complex multi-party transcription and adjudication process."
             "The error rate on Switchboard is about 5.9%, and for CallHome 11.3%."
```

```text
URL:         https://arxiv.org/abs/1708.06073
Kind:        primary. Xiong et al. (Microsoft), the 2017 system update (Technical
             Report MSR-TR-2017-39). Owns the follow-up numbers and the concession.
Establishes: Microsoft's improved 2017 system reached 5.1% WER on the Switchboard
             portion (7.2% on CallHome in the results table), down from 5.8% in
             2016. It records Microsoft explicitly conceding, after IBM's result,
             that human performance is not a single point but a range set by the
             transcription effort spent.
Paraphrase:  Reviewing its own 2016 measurement, the paper describes the human
             baseline as produced by a vendor pipeline left "blind to the
             experiment," yielding 5.9% versus the system's 5.8%. It then
             characterizes the IBM/Appen study as "a more involved transcription
             process with more listening passes, a pool of transcribers, and access
             to the conversational context of each utterance, yielding a human error
             rate of 5.1%," and concludes that human performance "falls within a
             range depending on the level of effort expended." The 2017 system's
             5.1% Switchboard result is described as on par with the multi-
             transcriber human rate.
Locators:    Abstract; Sec. 1 (paras beginning "Given these developments" and "The
             IBM/Appen human transcription study"); Sec. 5.1 and Table 5 (final
             combined 5.1%/7.2%); closing para "Overall, we have reduced error rate."
Quote:       "Together with a prior study by LDC, we can conclude that human
             performance, unsurprisingly, falls within a range depending on the
             level of effort expended."
             "We note that this level of error is on par with the multi-transcriber
             error rate previously reported on the same task."
```

```text
URL:         https://arxiv.org/abs/1703.02136
Kind:        primary. Saon et al. (IBM), with Appen transcribers as co-authors.
             They ran their own independent human measurement and own its numbers
             and protocol firsthand. This is the paper that disputes parity.
Establishes: IBM's independent human measurement, using three independent
             transcribers plus a fourth senior transcriber doing quality control,
             put the best human transcriber at 5.1% on Switchboard and 6.8% on
             CallHome. IBM's own system reached 5.5%/10.3%. The CallHome human rate
             (6.8%) is far below Microsoft's (11.3%), so "human parity" was
             attainable on Switchboard but "a distant dream" on CallHome.
Paraphrase:  Prompted by the gap between Microsoft's 5.9% and the old 4% figure,
             IBM commissioned Appen (Sydney) to transcribe the same Hub5 2000 data.
             The protocol was three independent native-US-English transcribers whose
             work was quality-checked by a fourth senior transcriber, at roughly
             12-14x real time per first pass plus 1.7-2x for the check. The best
             transcriber after checking reached 5.1% on Switchboard and a
             "surprisingly low" 6.8% on CallHome. IBM attributes the large CallHome
             gap versus Microsoft to a much lower deletion rate in its careful human
             transcript. It also notes Switchboard is an easy test because 36 of 40
             test speakers appear in the training data, and that ASR degrades more
             than expert humans when moving from formal (Switchboard) to casual
             (CallHome) speech.
Locators:    Abstract; Sec. 1 (paras "In [1], the authors claim" and "The findings
             from this effort were doubly surprising"); Sec. 2 "Human transcription
             experiments"; Table 1 (per-transcriber raw and QC rates).
Quote:       "we performed an independent set of human performance measurements on
             two conversational tasks and found that human performance may be
             considerably better than what was earlier reported, giving the
             community a significantly harder goal to achieve."
             "the same transcriber achieved a surprisingly low 6.8% WER for CallHome
             (we were expecting a much higher number based on the 11.3% estimate)."
             "the very different estimates for the human error rate for CallHome
             (6.8% versus 11.3%) can be attributed to a much lower deletion rate for
             our best human transcript."
```

```text
URL:         https://github.com/usnistgov/SCTK/blob/master/doc/sclite.htm
Kind:        primary. NIST's Scoring Toolkit documentation. NIST defines and owns
             the reference scoring procedure the ASR field runs its numbers through;
             the parity papers above all cite "the NIST scoring protocol."
Establishes: The alignment procedure that produces the substitution, deletion, and
             insertion counts, and the per-component percentages over reference
             words. sclite aligns hypothesis to reference by dynamic-programming
             minimization of a Levenshtein distance with fixed operation weights.
Paraphrase:  sclite finds the alignment between reference and hypothesis by global
             minimization of a Levenshtein distance that weights correct words,
             insertions, deletions, and substitutions as 0, 3, 3, and 4. Errors are
             then tallied and reported as percentages of reference words: percent
             correct, substituted, inserted, and deleted. These weights are load-
             bearing: they are why the S/D/I split in the worked example below is
             deterministic rather than tie-dependent (see Numbers).
Locators:    Section "Dynamic Programming string alignment" (the 0/3/3/4 weights);
             the tallied-percentages block ("Percent of ... words = # ... words /
             # Reference words * 100").
Quote:       "The DP string alignment algorithm performs a global minimization of a
             Levenshtein distance function which weights the cost of correct words,
             insertions, deletions and substitutions as 0, 3, 3 and 4 respectively."
Access note: The document's own page (the GitHub blob above) loads in a browser but
             returns 403 to scripted requests through the proxy; the identical text
             was read from the raw file at
             https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm
```

```text
URL:         https://web.stanford.edu/~jurafsky/slp3/16.pdf
Kind:        secondary. Jurafsky & Martin, "Speech and Language Processing" (3rd ed.
             draft), Ch. 16, on the authors' Stanford site. A canonical textbook
             that teaches the standard definition rather than owning an original
             empirical claim; used here for the summed formula, the >100% property,
             and an independently published worked example.
Establishes: The full WER formula WER = 100 x (Insertions + Substitutions +
             Deletions) / (Total words in the correct transcript), the fact that WER
             can exceed 100% because it counts insertions, that the first step is a
             minimum-edit-distance alignment, and that sclite is the standard NIST
             scoring tool. Supplies a second, independently published worked example.
Paraphrase:  The chapter defines WER as one hundred times the sum of insertions,
             substitutions, and deletions divided by the number of words in the
             reference, and states plainly that because the numerator includes
             insertions the rate can be greater than 100%. It gives a CallHome
             alignment with six substitutions, three insertions, and one deletion
             over a 13-word reference, computing 76.9%. It notes systems normally
             normalize text before scoring.
Locators:    Sec. 16.6 "ASR Evaluation: Word Error Rate" (formula and the
             parenthetical ">100%" note; the CallHome worked example; the sclite and
             text-normalization paragraphs).
Quote:       "The word error rate (WER) is then defined as follows (note that because
             the equation includes insertions, the error rate can be greater than
             100%): Word Error Rate = 100 x (Insertions + Substitutions + Deletions)
             / (Total Words in Correct Transcript)."
```

```text
URL:         https://arxiv.org/abs/2212.04356
Kind:        primary. Radford et al. (OpenAI), the Whisper paper. Owns its own
             observations about WER as a metric and about the model's failure modes.
Establishes: Two blind spots of WER, stated by the model's own builders, plus the
             hallucination failure mode. (1) WER penalizes all string differences
             including innocuous formatting, so a transcript humans would judge
             correct can still score a large WER; the authors built a text normalizer
             that, on some datasets, drops WER by up to 50% by removing non-semantic
             differences. (2) Beyond mishearings, the model exhibits non-perceptual
             failures including repeat loops, dropping the first or last words of a
             segment, and "complete hallucination" where the output is a transcript
             unrelated to the audio, mostly in long-form transcription.
Paraphrase:  The evaluation section states that WER, built on string edit distance,
             penalizes every difference from the reference including transcript-style
             differences, so correct-sounding output can carry a large WER; the team
             addresses this with extensive pre-scoring text standardization and
             reports WER drops of up to 50% on some datasets from that step alone.
             Separately, the analysis section describes the model getting stuck in
             repeat loops, failing to transcribe the first or last few words, or
             producing a transcript "entirely unrelated to the actual audio," and
             calls these errors "decidedly non-human/perceptual."
Locators:    Sec. 3.2 "Evaluation Metrics" (WER penalizes innocuous differences; the
             up-to-50% normalization effect; Appendix C for the normalizer); Sec. 4.4
             "Improved decoding strategies" (repeat loops, dropped words, complete
             hallucination); Sec. 3.8/4.5 (long-form decoding); Fig. 5 (WER vs SNR).
Quote:       "WER, which is based on string edit distance, penalizes all differences
             between the model's output and the reference transcript including
             innocuous differences in transcript style. As a result, systems that
             output transcripts that would be judged as correct by humans can still
             have a large WER due to minor formatting differences."
             "problems such as getting stuck in repeat loops, not transcribing the
             first or last few words of an audio segment, or complete hallucination
             where the model will output a transcript entirely unrelated to the
             actual audio."
Access note: Read in full from the authors' hosted copy at
             https://cdn.openai.com/papers/whisper.pdf (identical text); the arXiv
             page above is the document's own canonical page and resolves.
```

```text
URL:         https://www.pnas.org/doi/10.1073/pnas.1915768117
Kind:        primary. Koenecke et al., "Racial disparities in automated speech
             recognition," PNAS 2020. Owns the disparity measurement firsthand.
Establishes: WER is not comparable across speaker populations. Five commercial ASR
             systems averaged 0.35 WER for Black speakers versus 0.19 for white
             speakers on matched conversational audio; the gap is roughly 2x for
             every system, and worst for Black men (0.41 versus 0.30 for white men).
             The cause is traced to the acoustic models, from insufficient Black-
             speaker training data.
Paraphrase:  The study ran matched interview audio (42 white, 73 Black speakers,
             ~19.8 hours) through ASR from Amazon, Apple, Google, IBM, and Microsoft.
             Every system showed a large racial gap: average WER 0.35 for Black
             speakers against 0.19 for white speakers, with per-system Black-speaker
             WER nearly double the white-speaker WER in every case (Microsoft, the
             best overall, 0.27 for Black speakers; Apple, the worst, 0.45). The
             authors trace the gap to the acoustic models and a shortage of Black-
             speaker training data.
Locators:    Abstract; Results (per-system paragraph beginning "For each of the five
             commercial ASR systems"; the 0.35/0.19 averages; the 0.41/0.30 Black-men
             figure); Fig. 1 (WER by race per company).
Quote:       "we found that all five ASR systems exhibited substantial racial
             disparities, with an average word error rate (WER) of 0.35 for black
             speakers compared with 0.19 for white speakers."
Access note: The PNAS DOI page (own page, open access) loads in a browser but
             returns 403 to the proxy; the identical text was read from the authors'
             hosted copy at https://5harad.com/papers/asr-disparities.pdf
```

```text
URL:         https://languagelog.ldc.upenn.edu/nll/?p=28894
Kind:        secondary. Mark Liberman (linguist, University of Pennsylvania /
             Linguistic Data Consortium) commenting on Microsoft's parity claim. He
             did not author the claim or the measurement; he reports on and assesses
             it from outside, which makes this a secondary source, though an expert
             one (the LDC publishes the Switchboard/CallHome corpora).
Establishes: A contemporaneous expert judgment that the parity result was a genuine
             milestone, and an early statement of the metric critique the commission
             turns on: that overall WER is too crude because errors differ in
             consequence.
Paraphrase:  Liberman treats Microsoft's result as an important, impressive
             milestone while noting that harder tasks remain and that evaluation
             should move past a single overall word error rate, since some errors
             matter more than others.
Locators:    Body of the post (the closing assessment paragraphs).
Quote:       "perhaps it's time to go beyond simple evaluation in terms of overall
             word error rate, since some errors are more consequential than others."
```

## Contradictions

- The strong reading of "human parity" does not generalize, but a narrow reading
  survives, and the record must keep both. IBM's careful protocol shows the human
  baseline is soft: on CallHome the human rate moves from 11.3% (Microsoft, single
  vendor pass) to 6.8% (IBM, three transcribers plus senior QC), so no machine had
  reached human parity on CallHome. Yet on the clean Switchboard subset the claim
  held up: Microsoft's 2017 system reached 5.1%, matching IBM's best human
  transcriber at 5.1%. The honest finding is that parity was real on one easy,
  train-contaminated subset (IBM notes 36 of 40 Switchboard test speakers appear in
  training) and did not hold on the harder subset or across corpora. This directly
  tests the commission's angle and should shape it: the lesson is corpus dependence
  and baseline softness, not that the whole result was hollow.

- Microsoft (the party with the most stake in the parity headline) itself conceded
  the range, writing that human performance "falls within a range depending on the
  level of effort expended." That concession is evidence FOR the commission's angle,
  from the least likely source, and it is stronger than any outside criticism.

- The commission's framing that hallucination is "a failure WER barely penalizes"
  overstates what the Whisper paper supports and should not be written as the paper's
  claim. Hallucinated words are scored as insertions and substitutions, so on the
  affected segment they raise WER, sometimes above 100%. What the primary evidence
  actually supports is narrower and still sharp: (a) a corpus-level or dataset-level
  WER averages catastrophic segments together with clean ones, so a strong headline
  WER can coexist with segments where the model invented text; and (b) WER is meaning-
  blind, scoring a fluent, plausible fabrication identically to an audible mishearing
  of the same length, so the number cannot flag which wrong output is dangerous. The
  writer should make the meaning-blindness and averaging points, not claim WER fails
  to count hallucinated words.

- Steelman that WER tracks meaning better than the commission assumes: Microsoft's
  error analysis found humans and its system make broadly the same errors, on the
  same short function words, on the same hard speakers, and that human judges could
  not reliably tell a human transcript from an ASR transcript of similar error rate.
  In this domain the machine's WER-counted errors were not systematically more
  meaning-destroying than a human's. The blind spots are real, but this is the case
  the article has to answer rather than ignore.

- Liberman, an authority positioned to be skeptical, called the result "an important
  and impressive milestone." The article should not treat the achievement as fake;
  the critique is about what the number can carry, not whether progress happened.

## Numbers

```text
Figure: 5.8% WER (Switchboard), 11.0% WER (CallHome)
Owner:  Microsoft, Xiong et al. 2016 (arXiv:1610.05256), automated system
Scope:  NIST 2000 CTS evaluation set, ~21,000 reference words per subset, NIST scoring
```
```text
Figure: 5.9% WER (Switchboard), 11.3% WER (CallHome)
Owner:  Microsoft, Xiong et al. 2016, professional-transcriber human baseline
Scope:  Same NIST 2000 subsets; single commercial-vendor two-pass transcription
```
```text
Figure: 5.1% WER (Switchboard), 7.2% WER (CallHome)
Owner:  Microsoft, Xiong et al. 2017 (arXiv:1708.06073), final combined system
Scope:  NIST 2000 CTS set; Table 5 final row; headline result is the 5.1% Switchboard
```
```text
Figure: 5.5% WER (Switchboard), 10.3% WER (CallHome)
Owner:  IBM, Saon et al. 2017 (arXiv:1703.02136), automated system
Scope:  Hub5 2000 (= NIST 2000 CTS) Switchboard/CallHome subsets
```
```text
Figure: 5.1% WER (Switchboard), 6.8% WER (CallHome) — best human transcriber after QC
Owner:  IBM, Saon et al. 2017, human baseline (Appen, 3 transcribers + senior QC)
Scope:  Same Hub5 2000 subsets. Per-transcriber Table 1 (raw / after-QC):
        T1 6.1/5.6 SWB, 8.7/7.8 CH; T2 5.3/5.1 SWB, 6.9/6.8 CH; T3 5.7/5.2 SWB, 8.0/7.6 CH.
        Compare Microsoft's reported human 5.9 SWB / 11.3 CH.
```
```text
Figure: Levenshtein operation weights 0 / 3 / 3 / 4 (correct / insertion / deletion / substitution)
Owner:  NIST sclite documentation
Scope:  The DP alignment cost model that fixes the S/D/I decomposition
```
```text
Figure: WER = (S + D + I) / N; can exceed 100% (numerator includes insertions)
Owner:  Jurafsky & Martin, SLP3 Ch. 16 (formula and >100% note); components owned by NIST sclite
Scope:  N = reference word count. J&M worked example: 6S + 3I + 1D over N=13 = 76.9% (CallHome)
```
```text
Figure: Verified worked micro-example (computed by hand and by Levenshtein alignment)
Owner:  This record, following the NIST/sclite 0/3/3/4 weighting
Scope:  REF: "the quick brown fox happily jumps"  (N = 6)
        HYP: "the slow  brown fox jumps   now"
        Alignment under sclite weights:
          the->the      correct
          quick->slow   substitution (S = 1)
          brown->brown  correct
          fox->fox      correct
          happily->()   deletion     (D = 1)
          jumps->jumps  correct
          ()->now       insertion    (I = 1)
        WER = (1 + 1 + 1) / 6 = 50%.
        Teaching subtlety verified in code: the error COUNT and WER (50%) are stable,
        but the S/D/I SPLIT is not tie-free under naive unit costs (an equal-cost
        alignment reads as 3 substitutions). NIST sclite's 0/3/3/4 weights make the
        intuitive 1S/1D/1I split the unique minimum, because one substitution plus one
        deletion plus one insertion (4+3+3 = 10) beats three substitutions (12).
        A >100% case: REF "hello" (N=1), HYP "hello there my friend" = 3 insertions,
        WER = 3/1 = 300%.
```
```text
Figure: 0.35 average WER (Black speakers) vs 0.19 (white speakers); Black men 0.41 vs 0.30
Owner:  Koenecke et al. 2020, PNAS
Scope:  5 commercial ASR systems; matched audio, 42 white + 73 Black speakers, ~19.8 hrs.
        Per system, Black-speaker WER: Microsoft 0.27 (best overall); Apple 0.45 (worst).
```
```text
Figure: WER falls by up to 50% on some datasets from pre-scoring text normalization
Owner:  Radford et al. 2022 (Whisper), Sec. 3.2
Scope:  Whisper's text normalizer removing non-semantic formatting differences before WER
```

## Source assets

```text
Asset: Table 13, Microsoft 2016 (arXiv:1610.05256) — WER broken into substitutions,
       insertions, deletions for human transcribers vs the ASR system, both subsets.
Shows: That the human and machine totals are close but composed differently — humans
       show a lower substitution rate and a higher deletion rate. Grounds the point
       that WER's single number hides the shape of the errors.
Crop:  Keep the S/I/D columns and the human-vs-system rows for both subsets. Omit the
       surrounding running text; the table stands alone.
```
```text
Asset: Table 1, IBM 2017 (arXiv:1703.02136) — WER on SWB and CH for each of the three
       transcribers before and after QC, with Microsoft's reported human WER as the
       last row.
Shows: The human baseline is a moving target: within-transcriber variation, the drop
       from QC, and the large CallHome gap (best human 6.8% vs Microsoft's 11.3%). This
       is the single clearest visual for the whole "parity" dispute.
Crop:  Keep all transcriber rows plus the "Human WER from [1]" row and both SWB and CH
       columns. Retaining the 11.3 vs 6.8 contrast is the point; do not crop it out.
```
```text
Asset: Figure 5, Whisper (arXiv:2212.04356) — WER on LibriSpeech test-clean as a
       function of signal-to-noise ratio, Whisper vs supervised baselines, under white
       noise and pub noise.
Shows: How WER degrades as noise rises, and that robustness differs sharply between
       models the headline clean-set WER would rank as similar. Owns the "noise" blind
       spot from the brief.
Crop:  Keep both noise-condition panels with axes labeled (SNR in dB vs WER%); the
       Whisper-vs-baseline separation is the message.
```
```text
Asset: Figure 1, Koenecke et al. 2020 (PNAS) — average WER for Black vs white speakers,
       per ASR company.
Shows: The racial gap is present in every commercial system, not one vendor's flaw.
       Owns the "accents/dialect not comparable across populations" blind spot.
Crop:  Keep all five companies and both speaker groups; the point is that every bar
       pair shows the gap.
```
```text
Asset: The Sec. 16.6 worked alignment (Jurafsky & Martin SLP3 Ch. 16) — a CallHome
       REF/HYP pair marked up with S, D, I labels under each token, computing 76.9%.
Shows: What min-edit-distance alignment looks like on real conversational speech, with
       the counts feeding the formula. A ready-made teaching visual for the mechanics.
Crop:  Keep the REF line, HYP line, the S/D/I eval line, and the arithmetic; nothing
       else is needed.
```

## Discarded

```text
URL: https://vatis.tech/blog/what-is-wer-in-speech-to-text-... — vendor blog; the
     definition it gives is owned by NIST sclite and J&M, which are cited instead.
URL: https://en.wikipedia.org/wiki/Word_error_rate — tertiary; the >100% property and
     formula are taken from J&M, which owns the pedagogical statement directly.
URL: https://techxplore.com/news/2016-10-microsoft-speech-... — press write-up of the
     Microsoft claim; the paper itself is read, so the coverage adds nothing.
URL: https://techxplore.com/news/2020-03-automated-speech-... — press write-up of
     Koenecke; superseded by reading the PNAS paper.
URL: https://www.researchgate.net/publication/319185175_... — mirror of the IBM paper;
     the arXiv version is the citable primary.
URL: https://smallest.ai / elevenlabs.io / decagon.ai / clari.com WER glossaries —
     SEO explainers; no primary standing and no figure the primaries do not own.
```
