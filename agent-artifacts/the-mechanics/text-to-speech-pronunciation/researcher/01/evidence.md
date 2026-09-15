# Evidence: the-mechanics/text-to-speech-pronunciation (01)

The evidence supports the commission's core claim cleanly: in a classic
text-to-speech (TTS) system the pronunciation of each written word is decided in
a text-analysis front end (text normalization, then grapheme-to-phoneme
conversion, then homograph disambiguation) that runs before any audio sample
exists, and each step is a separately studied problem with its own published
error rates. Primary papers own every step: Sproat & Jaitly 2016 for
normalization, Rao et al. 2015 for G2P, Gorman et al. 2018 and Nicolis & Klimkov
2021 for homograph disambiguation (two independent owners of a ~99% figure on the
same public dataset), and van den Oord et al. 2016 (WaveNet) and Shen et al. 2018
(Tacotron 2) for what neural synthesis did and did not change. The two-failure
distinction the commission asks the writer to draw is well evidenced: a
normalization/G2P failure produces the wrong words or wrong phonemes for a written
form (the right sound was never generated), while a homograph failure produces a
real English word whose sound is right for some sense but wrong for this sentence.

The record is thin, and the angle is bounded, in three places the writer must
respect. First, the most vivid "read as the wrong words" errors (a currency read
as the wrong currency, a unit dropped) come from an experimental RNN in a
challenge paper, and that same paper shows deployed systems add a finite-state
filter precisely to stop those "silly" errors, so they evidence the mechanism and
the difficulty, not a bug a listener routinely hears. Second, the ~99% homograph
accuracy is measured on a balanced benchmark of 162 known homographs with the
homograph already located in the sentence, so it does not mean homographs are
solved in the wild. Third, "the error is almost always a front-end error" is a
classic-pipeline claim; end-to-end neural systems distribute pronunciation across
the network and add their own failure modes (skipped words, wrong-syllable stress)
that are not lexical front-end errors. None of the three overturns the angle, but
each bounds a sentence the writer might otherwise overstate.

## Sources

```text
URL:         https://arxiv.org/abs/1611.00068
Kind:        primary — Sproat & Jaitly (Google, Inc.) own the text-normalization
             experiment and its documented error output.
Establishes: (1) Text normalization is the front-end step that turns non-word
             written forms (numbers, measures, currency, dates) into the words a
             TTS voice should say, and the mapping is ambiguous. (2) A pure RNN
             trained on this task reaches high overall accuracy yet produces
             errors that "would convey completely the wrong message" — reading a
             written form as the wrong words. (3) Production-grade normalization
             pairs the RNN with a finite-state (FST) filter to suppress exactly
             these errors.
Paraphrase:  The paper releases a corpus of written text aligned to its
             normalized spoken form and trains several RNN architectures on it.
             English overall accuracy is 0.993 and the oracle accuracy (the
             correct answer is somewhere in the model's candidate set) is 0.998,
             yet the deep model still emits wrong-word normalizations. Table 4
             lists concrete failures. The authors argue the problem is not solved
             by feeding large annotated data to a general RNN, and show an
             FST-based filter recovers accuracy the RNN alone cannot.
Locators:    Abstract; Section 5 and Table 3 (accuracies, N=92,448 English test
             tokens); Table 4 (error triples); Section on the FST filter.
Quote:       Input "£900 million" — Correct "nine hundred million pounds" —
             Prediction "nine hundred million euros". Input "2 mA" — Correct
             "two milliamperes" — Prediction "two units". Input "82.55 mm" —
             Correct "eighty two point five five millimeters" — Prediction
             "eighty two one five five meters". Russian "16 ГБ" — Correct
             "sixteen gigabytes" — Prediction "sixteen hours" (Table 4). The
             authors add of the £900m/euros row: "In light of recent events, the
             final English example is rather amusing" (a 2016 Brexit aside).
```

```text
URL:         https://research.google.com/pubs/archive/43264.pdf
Kind:        primary — Rao, Peng, Sak, Beaufays (Google Inc.), ICASSP 2015. Owns
             the reported G2P error rates.
Establishes: (1) Grapheme-to-phoneme (G2P) conversion predicts a word's phoneme
             string from its spelling, and it is the fallback invoked whenever a
             word is not in the hand-built pronunciation dictionary — which is why
             names, loanwords, and new words rely on it. (2) English G2P is hard:
             even a strong neural model gets roughly a fifth to a quarter of
             held-out dictionary words wrong.
Paraphrase:  A pronunciation system is a static expert dictionary plus a G2P
             engine "to generate pronunciations" for words the dictionary lacks;
             the G2P "is invoked anytime a word is not in the static dictionary."
             English is called out as much harder to predict than a
             consistent-spelling language like Spanish. A deep bidirectional LSTM
             with CTC reaches 25.8% word error rate on the public CMUDict US
             English set; combined with a joint 5-gram model it reaches 21.3% WER,
             a 9% relative gain over the prior best of 23.4%.
Locators:    Abstract; Section 1 (dictionary + G2P framing, the "google → g u g @
             l" example); Table 1 (phoneme error rate, best 9.1%); Table 2 (WER
             comparison).
Quote:       "Grapheme-to-phoneme (G2P) models are key components in speech
             recognition and text-to-speech systems as they describe how words are
             pronounced." "A robust G2P is an essential piece ... it is invoked
             anytime a word is not in the static dictionary."
```

```text
URL:         https://aclanthology.org/L18-1215/
Kind:        primary — Gorman, Mazovetskiy, Nikolaev (Google), LREC 2018. Owns the
             homograph-accuracy figures and the Wikipedia Homograph Data set.
Establishes: (1) A homograph is one spelling with two or more pronunciations that
             depend on sense or part of speech; resolving it needs the surrounding
             sentence, and spelling alone cannot decide. (2) Named accuracy figures
             on a public benchmark: always guessing the most frequent pronunciation
             gets 85.0%; hand-written rules 89.3%; machine learning alone 95.4%;
             the hybrid (rules + ML) 99.0%. (3) The two hybrid systems run on all
             US English TTS traffic at Google.
Paraphrase:  The authors built a labelled set of 163 US-English homographs (two
             pronunciations each, two with three), ~100 Wikipedia sentences per
             homograph, three annotators per example, released as WikipediaHomograph-
             Data (Apache 2.0). Table 2 reports whole-set baselines: MLE 0.850
             micro-accuracy, embedded rules 0.869, server rules 0.893. Table 3
             (disjoint eval set) reports embedded rules 0.870, server rules 0.890,
             embedded ML 0.926, server ML 0.954, and both hybrid systems 0.990. The
             best (hybrid) systems achieve a 12.0% absolute / 92.3% relative error
             reduction over the worst (embedded rules-only). Morphosyntactic
             homographs (read, live, lives) are harder than lexical ones (bass).
Locators:    Abstract; §4.1 (163 homographs, ~100 sentences each); §5.1–5.2 and
             Tables 2–3 (figures); §5.3 (error analysis, the "present" case).
Quote:       "hybrid systems ... are significantly more accurate than either
             hand-written rules or machine learning alone." "All systems
             incorrectly predict the verb form [pɹɪˈzɛnt] in place of the
             noun/adjective [ˈpɹɛzənt] in sentences like 'Smith has played Trophy
             matches for the county from 1993 to present.'" Example pronunciations
             given: bass [beɪs] vs [bæs]; read_present [ɹiːd]; winds [wɪndz] vs
             [waɪndz]; use [juːst].
```

```text
URL:         https://www.isca-archive.org/ssw_2021/nicolis21_ssw.html
Kind:        primary — Nicolis & Klimkov (Amazon), SSW11 2021. Independent owner of
             a homograph figure on the same public dataset.
Establishes: A second, independent system reaches 0.991 accuracy on the English
             homographs of the same public dataset (Gorman et al. 2018) using only
             contextual word embeddings, with no rule system — corroborating the
             ~99% ceiling and confirming that reading the sentence context is what
             resolves the homograph.
Paraphrase:  "Per-case" classifiers (one per homograph) take contextual word
             embeddings (from pretrained language models such as BERT) as features
             and reach state-of-the-art 0.991 accuracy on the openly available
             dataset from Gorman et al., without additional rules. As few as 100
             sentences suffice to train a lightweight classifier when the two
             pronunciations are balanced; the authors add data for severely
             unbalanced homographs and show an 11% relative improvement there.
Locators:    Abstract; §1 (dataset [2] = Gorman et al.); the tear/tear definition.
Quote:       "achieve state-of-the-art accuracy of 0.991 on the English homographs
             on a publicly available dataset, without any additional rule system
             being necessary." Homograph defined via "tear (to separate or pull
             apart) and tear (a secretion from the eye)."
```

```text
URL:         https://arxiv.org/abs/1609.03499
Kind:        primary — van den Oord et al. (DeepMind), WaveNet, 2016. Owns the
             claim about what the neural back end replaced.
Establishes: WaveNet replaced the audio-generation back end (the vocoder), not the
             front end: for TTS it is "locally conditioned on linguistic features
             which were derived from input texts," with external models predicting
             phone durations and log-F0 from those same linguistic features. The
             classic front end (normalization, POS tagging, G2P) still runs
             upstream and still decides the phonemes.
Paraphrase:  The appendix lays out the standard two-part TTS pipeline: a
             text-analysis part (sentence/word segmentation, text normalization,
             POS tagging, G2P) that outputs a phoneme sequence with linguistic
             context, and a speech-synthesis part that turns that into a waveform.
             WaveNet is the second part. On naturalness (5-scale MOS) it scored
             4.21 for North American English versus 3.67 (LSTM parametric), 3.86
             (concatenative), and 4.55 for natural PCM speech — the gap to natural
             speech narrowing from 0.69 to 0.34.
Locators:    §3.2 and Table 1 (MOS); Appendix (TTS pipeline description);
             conditioning description ("locally conditioned on linguistic features
             ... derived from input texts").
Quote:       "WaveNets for the TTS task were locally conditioned on linguistic
             features which were derived from input texts." Pipeline: "text
             analysis part typically includes ... text normalization, part-of-speech
             (POS) tagging, and grapheme-to-phoneme (G2P) conversion. It takes a
             word sequence as input and outputs a phoneme sequence."
```

```text
URL:         https://arxiv.org/abs/1712.05884
Kind:        primary — Shen et al. (Google), "Natural TTS Synthesis by Conditioning
             WaveNet on Mel Spectrogram Predictions" (Tacotron 2), 2018. Owns the
             end-to-end naturalness figure and its documented error modes.
Establishes: (1) An end-to-end system maps characters straight to a spectrogram
             (then to audio), folding much of the front end into one network and
             raising naturalness to near-human: MOS 4.526 versus 4.582 for
             professional recorded speech. (2) It still mispronounces, and
             mispronunciation is the leading reason listeners prefer real speech.
             (3) It does not remove text normalization: the model is trained on
             already-normalized text ("16" written "sixteen"), so that step still
             happens upstream. (4) Its residual errors include non-lexical ones
             (skipped words, unnatural prosody) that are back-end/attention
             failures, not front-end pronunciation errors.
Paraphrase:  Tacotron 2 encodes characters, attends, and predicts mel spectrograms
             that a modified WaveNet turns into audio. On the internal test set it
             scores MOS 4.526 (ground truth 4.582); a side-by-side shows a small
             but significant preference for ground truth, and "occasional
             mispronunciation by our system is the primary reason for this
             preference." On a 100-sentence stress set (MOS 4.354) the manual error
             count was 0 sentences with repeated words, 6 with mispronunciations, 1
             with skipped words, and 23 with unnatural prosody. On out-of-domain
             news headlines it "sometimes runs into pronunciation difficulties,
             e.g., when handling names."
Locators:    Abstract (MOS 4.53 vs 4.58); §3.1 (trained on normalized text, "16"→
             "sixteen"); §3.2 and Table 1 (MOS ladder, error-mode counts, the names
             finding); §2 intro (WaveNet inputs "require ... elaborate text-analysis
             systems as well as a robust lexicon").
Quote:       "occasional mispronunciation by our system is the primary reason for
             this preference." "it sometimes runs into pronunciation difficulties,
             e.g., when handling names. This result points to a challenge for
             end-to-end approaches — they require training on data that cover
             intended usage."
```

```text
URL:         https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html
Kind:        primary — Amazon Web Services' own developer documentation for Amazon
             Polly. Owns the description of its own patch mechanism.
Establishes: A deployed neural TTS service ships a manual override: a custom
             pronunciation lexicon (a W3C PLS XML file) that maps a written form to
             a replacement spelling or an explicit phoneme string, "applied ... to
             the input text before the synthesis begins." This is concrete evidence
             for the commission's claim that vendors bolt lexicons and aliases onto
             neural systems to patch specific words the model gets wrong.
Paraphrase:  Lexicons "enable you to customize the pronunciation of words," applied
             before synthesis. The page gives worked cases: an alias mapping
             "g3t sm4rt" to "get smart" (the engine otherwise "reads the text
             literally"), and expanding the acronym "W3C" to "World Wide Web
             Consortium"; pronunciation can also be given "using a phonetic
             alphabet." Companion pages cover uploading and applying lexicons.
Locators:    "Managing lexicons" overview page; the bulleted examples.
Quote:       "a Text-to-Speech (TTS) engine reads the text literally, pronouncing
             the name exactly as it is spelled. This is where you can leverage
             lexicons ..." "This applies the specified lexicon to the input text
             before the synthesis begins."
```

```text
URL:         https://www.npr.org/sections/alltechconsidered/2015/10/05/446051309/hey-siri-what-did-you-say-why-computers-still-mispronounce-names
Kind:        secondary — NPR (Laura Sydell, All Tech Considered, 2015-10-05)
             reporting on the phenomenon from outside the system builders. Supplies
             real-world, named failures and an attributed expert explanation.
Establishes: Real, documented mispronunciations users hear from a shipping
             assistant (Siri), and a builder's plain account of why: the system
             consults a dictionary first and, for what the dictionary lacks,
             assembles words from recorded sound fragments rather than "full words."
Paraphrase:  The piece plays listener recordings against Siri's rendering of place
             names it mishandles: "Mobile, Ala." (the city, a homograph with the
             adjective mobile), "Des Moines" (silent final consonants), and "Rue
             Bourdeaux," a New Orleans street. Andrew Breen, research director for
             text to speech at Nuance Communications (which helped build Siri), says
             the dictionary is "the first port of call," but "text-to-speech systems
             don't draw from full words, and mispronunciations can ensue." Susan
             Bennett, the original Siri voice, describes recording nonsensical
             phrases so the system could assemble sounds.
Locators:    Body paragraphs quoting Breen; the listener-vs-Siri audio list (Mobile,
             Des Moines, Rue Bourdeaux); the Susan Bennett passage.
Quote:       "We have a dictionary, and that's the first port of call," Breen says.
             "But text-to-speech systems don't draw from full words, and
             mispronunciations can ensue."
```

## Contradictions

- **The vivid normalization errors are from a research model, not deployed TTS.**
  Sproat & Jaitly's £900m→"euros" and 2mA→"two units" come from an experimental
  pure-RNN normalizer, and the same paper's point is that production systems add an
  FST filter to prevent these "silly" errors. So they document the mechanism and
  the difficulty, not something a car navigation voice actually says. The everyday
  failures a reader has heard are better carried by the homograph cases
  (lead/read/bass/tear; Gorman's "present"; NPR's "Mobile, Ala.") and by neural-TTS
  name failures (Tacotron 2; NPR's "Des Moines").

- **~99% can read as "homographs are solved."** Gorman (0.990) and Nicolis &
  Klimkov (0.991) measure on a balanced set of 162–163 *known* homographs with the
  target word already located in the sentence. The wild is harder: the same paper's
  most-frequent-guess baseline is only 0.850 (so ~15% of these tokens genuinely need
  context), "present" is still missed by every system, and homographs outside the
  curated list, or in genuinely ambiguous sentences, are not covered by the figure.
  The number supports the "settled step, hard residue" framing; it does not support
  "systems almost never mispronounce homographs."

- **"Almost always a front-end error" is a classic-pipeline statement.** In
  end-to-end systems the front-end modules are not separate boxes, and Tacotron 2's
  own error audit shows non-lexical failures — 1 sentence with skipped words, 23
  with unnatural prosody (wrong-syllable emphasis, unnatural pitch) — that are
  back-end/attention artifacts, not a wrong choice of word or phoneme. The writer's
  two-failure split (normalization/G2P vs homograph) is a front-end taxonomy and
  should be presented as such, with these back-end errors named as a third, distinct
  kind rather than folded in.

- **G2P is shared with speech recognition.** Rao et al. (the G2P primary) frame G2P
  as key to "speech recognition and text-to-speech" both, and their CMUDict WER is a
  pronunciation-of-words metric independent of direction. This does not conflict with
  the TTS boundary — G2P is genuinely the same component used in both — but the
  writer must not import Rao's ASR framing; cite it only for the letters→phonemes
  step, which is what the front end does before synthesis.

## Numbers

```text
Figure: 0.993 overall accuracy (English RNN normalization); 0.998 oracle accuracy
Owner:  Sproat & Jaitly 2016
Scope:  N=92,448 English test tokens; "oracle" = correct answer present in the
        model's candidate lattice. High accuracy coexists with wrong-word errors.
```
```text
Figure: 25.8% word error rate (DBLSTM-CTC G2P); 21.3% with a joint 5-gram model
Owner:  Rao et al. 2015
Scope:  Public CMUDict US English held-out words; a word counts as an error if any
        phoneme is wrong. Prior best hybrid was 23.4%. Best phoneme error rate 9.1%.
```
```text
Figure: Homograph accuracy — MLE most-frequent 0.850; rules 0.893 (server) /
        0.869 (embedded); ML alone 0.954 / 0.926; hybrid 0.990
Owner:  Gorman et al. 2018 (micro-accuracy; Table 2 whole-set for baselines,
        Table 3 disjoint eval set for the rest)
Scope:  163 US-English homographs, ~100 Wikipedia sentences each; homograph token
        pre-located; best systems = 12.0% absolute / 92.3% relative error cut over
        worst.
```
```text
Figure: 0.991 homograph accuracy (contextual embeddings, no rules)
Owner:  Nicolis & Klimkov 2021
Scope:  English homographs of the same public dataset (Gorman et al. 2018);
        independent corroboration of the ~99% ceiling.
```
```text
Figure: Naturalness MOS — WaveNet 4.21; LSTM parametric 3.67; concatenative 3.86;
        natural speech 4.55 (North American English, 5-scale)
Owner:  van den Oord et al. 2016 (WaveNet), Table 1
Scope:  Subjective mean opinion score; back-end (vocoder) quality, front end held
        fixed and still supplying phonemes.
```
```text
Figure: MOS 4.526 (Tacotron 2) vs 4.582 (professional recording); on the 100-sentence
        stress set MOS 4.354 with 6/100 sentences containing mispronunciations,
        1 skipped words, 23 unnatural prosody
Owner:  Shen et al. 2018 (Tacotron 2), abstract and Table 1 / §3.2
Scope:  Internal 24.6-hour single-speaker US English set; end-to-end, trained on
        pre-normalized text. Mispronunciation is the top reason for the ground-truth
        preference; names are the named out-of-domain failure.
```

## Source assets

```text
Asset: Sproat & Jaitly 2016, Table 4 — the input / correct / prediction error rows
       (£900 million → "euros"; 2 mA → "two units"; 82.55 mm → "meters").
Shows: A written form emerging from the front end as the wrong spoken words, before
       any audio — the cleanest single before/after of a normalization failure.
Crop:  Retain the three columns (input, correct, prediction) for two or three English
       rows; omit the Russian rows and the training-step tables. Reproduce as a small
       plain comparison, not a full reprint.
```
```text
Asset: Gorman et al. 2018, the accuracy ladder in Tables 2–3 (0.850 → 0.893 → 0.954
       → 0.990) plus the "present" example sentence in §5.3.
Shows: How much of homograph resolution the most-frequent guess already covers and
       how much needs context, and a concrete sentence every system still gets wrong.
Crop:  If drawn as a chart, four bars (MLE, rules, ML, hybrid) with the axis labelled
       micro-accuracy and the Wikipedia Homograph Data denominator in the caption.
       The "present" case works as prose and needs no figure.
```
```text
Asset: Shen et al. 2018, the error-mode counts on the 100-sentence set (6
       mispronunciations, 1 skipped, 23 unnatural prosody, 0 repeated).
Shows: That even a near-human end-to-end system's residual errors are mostly prosody
       and pronunciation, and separates lexical mispronunciation from skip/repeat
       attention failures.
Crop:  Prose or a four-row list; no decorative chart. Keep the denominator (100
       sentences) attached to every count.
```
```text
Asset: WaveNet appendix, the two-part TTS pipeline description (text analysis →
       phoneme sequence → speech synthesis).
Shows: In the authors' own words, that normalization + POS + G2P sit in front of the
       neural audio model — the settled front-end/back-end split.
Crop:  Quote the sentence; no image.
```
None of the primaries offer a photograph or diagram worth lifting; the useful assets
are small numeric comparisons and two verbatim error examples.

## Library lessons to link in Background (not article-claim sources)

Surfaced via `nb history` against the library checkout, per the brief. These are
teaching the writer should link rather than re-teach; they do not source this
article's own claims.

- **the-mechanics/speech-to-text-hallucination** (2026-09-13, "Whisper answers
  silence with a sentence no one spoke"). The opposite direction — audio → text.
  The commission's boundary says link, don't re-teach the speech-recognition side.
  This is the primary Background link and the natural "we did the input side; this
  is the output side" pointer.
- **the-mechanics/text-in-images** (2026-08-25, "A generated image gets its letters
  wrong before the picture is ever drawn"). Strong structural parallel: an error
  fixed in an early text-handling stage *before* the output medium is produced, and
  a character-level fix. Good Background link for "the mistake is made before any
  audio exists." Note the mechanism differs (image tokenizer vs TTS front end); link
  it for the shape of the argument, not as the same component.
- **the-mechanics/counting-letters** (2026-08-28, "A model can spell strawberry and
  still miscount its letters"). Useful for the general idea that these systems
  manipulate written symbols, and a written form is not its sound or meaning.
  Caveat: that lesson is about the *language-model* tokenizer (byte-pair encoding),
  which is a different pipeline from the TTS front end — link it for the framing
  only, and do not imply TTS pronunciation runs on BPE tokens.
- **the-instruments/word-error-rate** (2026-08-28, "'Human parity' in speech
  recognition came down to how you count the humans"). Optional link if the writer
  uses the WER figure from Rao et al. Caveat: that lesson defines WER as transcript
  edit distance in speech recognition, whereas G2P WER counts a *word* wrong if any
  predicted phoneme is wrong. Different denominator; flag it if linked.

## Discarded

```text
https://arxiv.org/pdf/1611.00068: not a source but the same paper's PDF transport;
  recorded the abstract page (arxiv.org/abs/1611.00068) instead, per the URL rule.
https://elevenlabs.io/blog/...; https://murf.ai/blog/...; https://voice.ai/...:
  vendor marketing pages on "Siri text to speech," no primary mechanism or figure.
https://www.justanswer.com/...; https://colterreed.com/...: consumer how-to pages on
  fixing Alexa/Siri name pronunciation; the NPR piece documents the same phenomenon
  with named examples and an attributed expert, so these add nothing.
https://arxiv.org/html/2505.12973v1 (Fast, Not Fancy: Rethinking G2P): a newer G2P
  paper surfaced in search; Rao et al. 2015 already owns a clean, widely cited G2P
  WER, so this was not needed to meet the step or the floor.
```
