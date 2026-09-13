# Evidence: the-mechanics/speech-to-text-hallucination (01)

The evidence supports the commissioned angle firmly: Whisper's output stage is a
generative language model, and when the audio carries little or nothing to
transcribe it falls back on that model's language prior and emits a fluent,
confident sentence rather than a blank. Three independent kinds of source
converge on this. A peer-reviewed measuring study (Koenecke et al., FAccT 2024)
quantifies the behavior and its harms on real recordings. The model's own paper
(Radford et al.) states that the decoder is "an audio-conditional language model"
and lists "complete hallucination where the model will output a transcript
entirely unrelated to the actual audio" as a known failure mode, and OpenAI's own
model card names hallucination and recommends against decision-making use. A
mechanism paper (Frieske & Shi) shows the invented text is a distinct error type
from mis-hearing and can be induced by injecting noise. The deployment that gives
the behavior stakes is documented: an Associated Press investigation and the
vendor's own blog cover Nabla, a Whisper-based medical scribe used by 30,000-plus
clinicians that deletes the source audio by default.

The record is thin or contested in three places, all recorded in Contradictions.
First, exact rates vary by more than an order of magnitude across sources because
they measure different things (per-segment vs per-file, aphasia interviews vs
varied real-world audio) and different Whisper versions; there is no single
trustworthy "hallucination rate." Second, the flagship rate (1.4%) comes from
aphasic speech, a population chosen precisely because it has long pauses, so it
is not a general-population figure. Third, the trigger is low-information audio
broadly (silence, pauses, background noise, music), not strictly digital
silence, and it is a different failure from mis-hearing faint speech; the vendor
Nabla disputes that hallucination is a significant problem in its deployment.

## Sources

```text
URL:         https://facctconference.org/static/papers24/facct24-111.pdf
             (also arXiv: https://arxiv.org/abs/2402.08021)
Kind:        Primary. The authors ran the experiment and own the measurements;
             they are outside OpenAI, so this is primary for the hallucination
             data, not for Whisper's internals.
Establishes: The first large-scale external measurement of Whisper
             hallucination and its harm profile on real recordings.
Paraphrase:  The team ran 13,140 English audio segments (7,805 control, 5,335
             aphasia; ~40 hours of audio from 437 AphasiaBank speakers, ~10s per
             segment) through the default Whisper API in April/May 2023.
             Hallucinations were detected as multi-token differences between two
             runs with more tokens than the ground truth; 187 segments reliably
             hallucinated, yielding 312 hallucinated transcriptions. On average
             1.4% of transcriptions contained a hallucination. Of the 312, 38%
             contained at least one explicit harm: 19% perpetuation of violence,
             13% inaccurate associations, 8% false authority. Aphasia speakers
             hallucinated more than controls (1.7% vs 1.2%, p=0.019; 1.82% vs
             1.16% on a demographically matched subset of 6,046 segments,
             p=0.044). Files that hallucinated had higher "non-vocal" shares of
             duration (mean 42.4% aphasia-with, 40.6% aphasia-without, 16.2%
             control-with, 15.4% control-without); a logistic regression finds
             non-vocal duration share and number of words are the significant
             predictors of a hallucination. The authors hypothesize Whisper is
             "seeded by noise rather than speech" during pauses, and that its
             "over-reliance on OpenAI's language modeling advancements is what
             leads to hallucinations." Whisper was run at temperature 0 (least
             random) and still hallucinated non-deterministically. Retesting the
             187 segments in December 2023, after late-November Whisper updates,
             only 12/187 still hallucinated (9/92 aphasia files, 3/95 control).
             Google, Amazon, Microsoft, AssemblyAI and RevAI produced 0
             comparable hallucinations on the same 187 segments, so the authors
             call it "an OpenAI-specific concern." They note the "False
             Authority" hallucinations (YouTuber patter, "thank you for
             watching") are consistent with Whisper having been trained on over
             a million hours of YouTube audio.
Locators:    Abstract; §2.2-2.4 (data, method); §3 and Fig. 1a/1b (rates and
             harms); §3 (Dec 2023 retest, 12/187); §4.1 (competitors = 0;
             temperature 0; YouTube training); §4.2 and Fig. 3, Table 2
             (non-vocal duration); Table 1 p.4 (example transcriptions); §5
             (WER cannot capture this).
Quote:       "roughly 1% of audio transcriptions contained entire hallucinated
             phrases or sentences which did not exist in any form in the
             underlying audio... 38% of hallucinations include explicit harms."
             "longer pauses in spoken speech... could result in more
             hallucinations due to Whisper being seeded by noise rather than
             speech."
```

```text
URL:         https://arxiv.org/abs/2212.04356
             (PDF: https://cdn.openai.com/papers/whisper.pdf)
Kind:        Primary. OpenAI's own description of the model it built.
Establishes: The architecture (an audio encoder feeding an autoregressive text
             decoder that is a language model) and OpenAI's own acknowledgment
             of hallucination on non-speech and the decoding heuristics used to
             fight it.
Paraphrase:  Whisper is an off-the-shelf encoder-decoder Transformer. The
             encoder reads an 80-channel log-Mel spectrogram of the audio; the
             decoder predicts the transcript one token at a time and is
             explicitly described as "an audio-conditional language model,"
             trained to also condition on the preceding transcript text (50% of
             the time; Table 17). It is trained on 680,000 hours of audio
             (438,218 h, 65%, English), including no-speech segments (subsampled
             10x) to learn voice-activity detection, with a dedicated
             <|nospeech|> token. During development the model would "transcribe
             plausible but almost always incorrect guesses for the names of
             speakers" drawn from its language prior, fixed by fine-tuning on
             transcripts without speaker names (§2.4). The Limitations section
             names, among long-form failures, "complete hallucination where the
             model will output a transcript entirely unrelated to the actual
             audio," alongside repeat loops and dropped first/last words, calling
             these errors "decidedly non-human/perceptual." §4.5 gives the
             decoding heuristics that reduce this: beam search (5 beams),
             temperature fallback (start 0, raise by 0.2 to 1.0 when average log
             probability < -1 or gzip compression rate > 2.4), previous-text
             conditioning below temperature 0.5, a no-speech probability
             threshold of 0.6 combined with an average log-prob threshold of -1
             for VAD, and constraining the initial timestamp to 0-1s. Table 7
             shows each heuristic lowers long-form WER incrementally; the paper
             calls them "a workaround for the noisy predictions of the model" and
             says "more research would be needed."
Locators:    §2.2 (architecture), Fig. 1 (diagram, incl. "No speech -> null"),
             §2.3 ("audio-conditional language model", <|nospeech|>), §2.4
             (speaker-name hallucination), §4.5 and Table 7 (decoding
             heuristics), §6 Limitations ("complete hallucination"), Table 1
             (Large = 1550M params), Table 17 (50% prior-text rate).
Quote:       "complete hallucination where the model will output a transcript
             entirely unrelated to the actual audio." "Since our decoder is an
             audio-conditional language model, we also train it to condition on
             the history of text of the transcript."
```

```text
URL:         https://github.com/openai/whisper/blob/main/model-card.md
Kind:        Primary. Vendor (OpenAI) documentation of the shipped model.
Establishes: OpenAI states hallucination is a known behavior tied to language
             prediction, and warns against high-risk use.
Paraphrase:  The model card says "the predictions may include texts that are not
             actually spoken in the audio input (i.e. hallucination)" and
             attributes it to the model combining language prediction with
             transcription. It says the "sequence-to-sequence architecture of the
             model makes it prone to generating repetitive texts, which can be
             mitigated to some degree by beam search and temperature scheduling
             but not perfectly." It "recommend[s] against use in high-risk
             domains like decision-making contexts, where flaws in accuracy can
             lead to pronounced flaws in outcomes."
Locators:    "Performance and Limitations" section.
Quote:       "the predictions may include texts that are not actually spoken in
             the audio input (i.e. hallucination)."
```

```text
URL:         https://github.com/openai/whisper/discussions/928
Kind:        Primary artifact for the phenomenon. Posted by an outside user, so
             not authoritative on rates, but it displays the model's actual
             outputs and the community/maintainer explanation.
Establishes: Whisper invents specific recurring phrases over silence and closing
             music, seeded by subtitle training data.
Paraphrase:  Users report Whisper emitting subtitle-credit boilerplate during
             silent or non-speech sections, e.g. "Sous-titres realises par la
             communaute d'Amara.org" and its German/Spanish/Portuguese variants,
             plus "Thanks for watching!" and stray URLs. Contributors attribute
             this to training on video subtitles, where such credits appear at
             the end over silence, teaching the model to associate silence with
             those phrases; they point to the no_speech_prob output and VAD as
             partial fixes.
Locators:    Original post and top replies.
Quote:       "the model was obviously trained on subtitles and those specific
             subs typically show at the end of a video when there's nothing being
             said."
```

```text
URL:         https://github.com/openai/whisper/pull/1838
Kind:        Primary artifact. A merged change to the official Whisper repo.
Establishes: OpenAI's own mitigation confirms silence is a trigger and that the
             fix is a decoding-side workaround, not a model change.
Paraphrase:  The PR adds a `--hallucination_silence_threshold` parameter that,
             "when a possible hallucination is detected," skips silent periods
             longer than the threshold and reprocesses, plus `--clip_timestamps`
             to restrict inference to chosen regions. Hallucinations are flagged
             by anomalies (extreme word length/brevity or low probability) in the
             first 8 words of a segment. The rationale is that hallucinations
             often occur after silence, so removing the silence before
             re-inference improves the result. (Koenecke et al. cite this PR as a
             mitigation they did not use in their experiments.)
Locators:    PR title and description.
Quote:       "skip silent periods longer than this threshold (in seconds) when a
             possible hallucination is detected."
```

```text
URL:         https://arxiv.org/abs/2401.01572
Kind:        Primary. The authors (HKUST) design and run the experiment.
             Establishes the mechanism generally, not for Whisper specifically:
             the model is a small fairseq Transformer, not Whisper.
Establishes: That ASR "hallucination" is a distinct error type from mis-hearing,
             that it is fluent and semantically disconnected, that standard WER
             cannot detect it, and that it can be induced by noise.
Paraphrase:  Defines hallucination in ASR as output "semantically unrelated to
             the source utterance, yet still fluent and coherent," and separates
             it from phonetic errors (phonetically similar mis-hearings, which
             keep high semantic overlap) and oscillations (repetition loops).
             Shows WER, BLEU and CHRF2 cannot distinguish a hallucinatory model
             from a non-hallucinatory one with similar baseline WER. Induces
             hallucinations by injecting 1s of random noise (amplitude 0.5) at
             the start of an utterance; noise spread across the whole utterance
             instead produces ordinary phonetic errors. Finds two training-data
             routes: repeated mismatched target labels make the model copy those
             labels as hallucinations, while unique mismatched labels make it
             generate novel hallucinations not copied from the training set.
Locators:    Abstract; §1 (definitions); Table 1-2 (WER blindness; error-type
             examples); §3.4 and §4.4 (noise induction, start-of-utterance);
             §4.5 (training-data source).
Quote:       "commonly used metrics, such as word error rates, cannot
             differentiate between hallucinatory and non-hallucinatory models."
```

```text
URL:         https://www.ksl.com/article/51163476/ai-powered-transcription-tool-used-in-hospitals-invents-things-no-one-said-researchers-say
             (AP wire story by Garance Burke and Hilke Schellmann, Oct 26 2024;
             canonical origin is apnews.com, which is not reachable through this
             agent's fetch tools, so the identical AP text was read via this AP
             member reprint; the same wire copy also runs at tucson.com and
             columbian.com.)
Kind:        Secondary for the research figures it repeats (Koenecke); primary
             for its own reporting, i.e. the Nabla deployment facts and the
             developer interviews it conducted.
Establishes: The real-world deployment and its stakes: a Whisper-based medical
             scribe in wide clinical use that deletes the source audio.
Paraphrase:  Over 30,000 clinicians and 40 health systems, including the Mankato
             Clinic (Minnesota) and Children's Hospital Los Angeles, use a
             Whisper-based scribe from Nabla that was fine-tuned on medical
             language. "Nabla's tool erases the original audio for 'data safety
             reasons,'" per Nabla's Martin Raison, so the transcript cannot be
             checked against the recording. A University of Michigan researcher
             found hallucinations in 8 of 10 transcriptions; another developer
             found them in nearly all of 26,000 transcripts; the article also
             cites Koenecke's 187 hallucinations in more than 13,000 clear audio
             snippets and the ~40% harmful figure. OpenAI "recommended... against
             using Whisper in 'decision-making contexts.'" Developers said
             fabrications "tend to occur amid pauses, background sounds or music
             playing." Reported examples: Whisper adding "two other girls and one
             lady, um, which were Black" to a plain sentence, and inventing a
             medication, "hyperactivated antibiotics."
Locators:    Body paragraphs on Nabla, on the developer counts, on OpenAI's
             warning, and the two invented-text examples.
Quote:       "the fabrications tend to occur amid pauses, background sounds or
             music playing."
```

```text
URL:         https://www.nabla.com/blog/how-nabla-uses-whisper/
Kind:        Primary. Operator (Nabla) documentation of its own deployment.
Establishes: The operator's own account and its dispute with the AP framing;
             also the nuance in its audio policy.
Paraphrase:  Nabla says its model is based on Whisper "but contains many
             improvements specifically developed to suppress hallucinations,"
             and that hallucination "has never been reported as a significant
             issue" across 9 million processed encounters. It describes a
             safeguard in which each note is split into "atomic facts" checked by
             an LLM against the transcript and patient context, keeping only
             facts with "definitive proof," and it requires clinicians to review
             and edit notes before export. On audio: Nabla does not retain audio
             by default for privacy, but "let[s] clinicians opt into letting us
             store the audio for later review... only if authorized by their
             corporate policy and after obtaining patient consent." (This
             qualifies, without contradicting, the AP's "erases the original
             audio": deletion is the default, not an absolute.)
Locators:    Sections on Whisper basis, hallucination safeguards, clinician
             review, and audio retention.
Quote:       "hallucination has never been reported as a significant issue."
```

## Contradictions

**Is the invented text "from silence/nothing" or mis-heard faint speech?** The
sources agree it is a distinct failure from mis-hearing, but "from nothing" needs
care. Koenecke et al. tie hallucinations to longer "non-vocal" duration, but
their non-vocal measure is audio with "no (or only very weakly detected) human
speech," and control files that hallucinated still averaged ~16% non-vocal
share, so the trigger is pauses and weak/low-information signal inside otherwise
spoken utterances, not pure digital silence. Frieske & Shi induce hallucinations
by injecting random *noise*, not silence, and separate hallucination (fluent,
semantically disconnected, low cosine similarity) from phonetic error
(phonetically similar mis-hearing, high semantic overlap) — so mis-hearing faint
speech produces a *different* error, one that stays near the real words. The
Whisper paper likewise files "complete hallucination... entirely unrelated to the
actual audio" separately from "confusing similar-sounding words," and calls it
"non-human/perceptual." Net: the invention is best described as the decoder
running on little or nothing to condition on (silence, pauses, background noise,
music), which is broader than, and mechanistically distinct from, mis-hearing.

**How much do decoding rules and voice-activity detection fix it?** Substantially
but not fully, and the fixes are workarounds outside the model. The Whisper paper
shows beam search, temperature fallback, previous-text conditioning, a no-speech
probability threshold (0.6) and initial-timestamp constraints each lower
long-form WER (Table 7) but calls them "a workaround" needing "more research."
The model card says repetition is "mitigated to some degree... but not
perfectly." Koenecke et al. found late-November-2023 Whisper updates cut
reproducible hallucinations from 187/187 to 12/187 segments — a large reduction —
yet Whisper "still regularly and reproducibly hallucinates," and PR #1838 adds a
silence-skipping parameter precisely because the problem persists. So the
generative decoder's tendency is inherent; decoding and VAD reduce its rate
rather than remove it.

**Do vendors and studies disagree on rates?** Sharply. Koenecke reports 1.4% of
segments on aphasic interview audio. The AP's developer interviews report far
higher per-transcription rates (8 of 10; nearly all of 26,000) on varied
real-world audio with more pauses and music. Nabla says hallucination "has never
been reported as a significant issue" over 9 million encounters and claims
Whisper improvements to suppress it. These are not directly comparable — they
measure different units (segment vs file), different audio, and different Whisper
versions and pipelines — which is itself the finding: there is no single
general-purpose hallucination rate to quote. Separately, Koenecke found 0
comparable hallucinations in five competing services (Google, Amazon, Microsoft,
AssemblyAI, RevAI) on the same 187 segments, framing it as OpenAI/Whisper-specific
as of 2023-24; this is a single-study comparison and may not generalize to later
versions of those services.

**Does any of this undermine the commissioned angle?** No. The angle — a system
whose output stage is a language model emits fluent, plausible text even when the
input carries nothing to say — is directly supported by OpenAI's own paper and
model card and by the measuring and mechanism studies. The contradictions
qualify the *scope and rate*, not the mechanism.

## Numbers

```text
Figure: ~1.4% of transcriptions contained a hallucination (abstract rounds to "roughly 1%")
Owner:  Koenecke et al., FAccT 2024
Scope:  13,140 English audio segments (avg ~10s) from AphasiaBank, default Whisper API, April/May 2023; likely an undercount (only non-deterministic differences counted)
```

```text
Figure: 38% of hallucinated transcriptions contained >=1 explicit harm; 19% violence, 13% inaccurate associations, 8% false authority
Owner:  Koenecke et al., FAccT 2024
Scope:  312 hallucinated transcriptions from 187 reliably-hallucinating segments
```

```text
Figure: aphasia 1.7% vs control 1.2% hallucination rate (p=0.019); 1.82% vs 1.16% on matched subset (p=0.044)
Owner:  Koenecke et al., FAccT 2024
Scope:  5,335 aphasia vs 7,805 control segments; matched subset 6,046 segments
```

```text
Figure: 12 of 187 previously-hallucinating segments still hallucinated after late-Nov 2023 Whisper updates (9/92 aphasia files, 3/95 control)
Owner:  Koenecke et al., FAccT 2024
Scope:  Re-test December 2023 of the 187 segments identified in April/May 2023
```

```text
Figure: 0 comparable hallucinations from Google, Amazon, Microsoft, AssemblyAI, RevAI
Owner:  Koenecke et al., FAccT 2024
Scope:  Same 187 audio segments; tested April 2023 (Google), Dec 2023 (Google Chirp), Jan 2024 (others)
```

```text
Figure: mean non-vocal share of duration — aphasia+hallucination 42.4%, aphasia no-hallucination 40.6%, control+hallucination 16.2%, control no-hallucination 15.4%
Owner:  Koenecke et al., FAccT 2024 (Fig. 3, PyAnnote VAD)
Scope:  Per-segment; non-vocal = no or only weakly detected human speech
```

```text
Figure: hallucinations in 8 of 10 transcriptions (one researcher); nearly all of 26,000 transcripts (another developer)
Owner:  Associated Press (Burke & Schellmann), from developer interviews
Scope:  Single-developer counts on their own audio; not peer-reviewed; units differ from Koenecke's per-segment rate
```

```text
Figure: 30,000+ clinicians and 40 health systems use Nabla's Whisper-based scribe; 9 million encounters processed (Nabla's own count)
Owner:  Associated Press (deployment scale); Nabla blog (9M encounters)
Scope:  As of the AP report (Oct 2024) / Nabla blog
```

```text
Figure: Whisper trained on 680,000 hours of audio (438,218 h / 65% English); Large model = 1,550M parameters
Owner:  Radford et al. (Whisper paper), Table 1, Fig. 11
Scope:  Whisper model family / training set
```

```text
Figure: decoding thresholds — no-speech probability 0.6; average log-prob fallback -1; gzip compression rate fallback 2.4; beam 5; temperature 0->1.0 in 0.2 steps
Owner:  Radford et al. (Whisper paper), §4.5
Scope:  Long-form decoding heuristics
```

## Source assets

```text
Asset: Table 1 (p.4) in Koenecke et al. — ground-truth utterance beside the full
       Whisper transcription, with the hallucinated text in bold, across nine
       harm categories.
Shows: The behavior at a glance: a real short utterance and the fluent invented
       sentence appended to it (e.g. "...Thank you for watching!"; "...visit
       www.FEMA.gov"; a violent clause never spoken).
Crop:  Keep at least one ground-truth/transcription pair with its bolded
       hallucination and the harm label; a single row reads clearly. Omit the
       redacted-name and non-English rows if space is tight.
```

```text
Asset: Figure 1 (p.4) in Radford et al. (Whisper paper) — the architecture
       diagram: log-Mel spectrogram into the Transformer encoder, cross-attending
       into the decoder that predicts tokens, including the "No speech -> null"
       training example and the <|nospeech|> token.
Shows: The two-stage shape the lesson needs — audio encoder feeding an
       autoregressive text decoder — and that "no speech" is a trained-for case.
Crop:  The encoder-decoder core with the token stream is the useful part; the
       lower multitask-format legend can be dropped.
```

```text
Asset: Figure 1b / Figure 3 in Koenecke et al. — aphasia vs control hallucination
       rates (1.7% vs 1.2%) and the non-vocal-share density by subgroup.
Shows: That more non-vocal (silent/weak) audio goes with more hallucination.
Crop:  Fig. 1b is the simplest honest visual; Fig. 3 if the lesson wants the
       non-vocal-duration link. Label axes and note it is aphasic interview audio.
```

```text
Asset: Table 2 (p.3) in Frieske & Shi — side-by-side examples of a phonetic error,
       a hallucination, and an oscillation for the same reference.
Shows: Why a hallucination is not a mis-hearing: the phonetic error stays near the
       words, the hallucination is unrelated but fluent.
Crop:  Keep the three labeled columns for one reference row.
```

## Discarded

```text
URL: https://techxplore.com/news/2024-06-ai-speech-text-hallucinate-violent.html — secondary write-up of Koenecke; used the primary paper instead.
URL: https://fortune.com/2024/10/26/openai-transcription-tool-whisper-hallucination-rate... — secondary recap of the AP story; read the AP wire copy directly instead.
URL: https://futurism.com/the-byte/whisper-nabla-hospital-ai-details-patients — secondary recap; superseded by the AP report and Nabla's own blog.
URL: https://dl.acm.org/doi/10.1145/3630106.3658996 — ACM landing page for the same Koenecke paper; the open FAccT PDF and arXiv version carry the full text.
URL: apnews.com canonical article — origin of the AP story but unreachable through this agent's fetch tools; the identical AP wire text was verified via the KSL reprint recorded above.
```
