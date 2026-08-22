# Evidence record: the-evidence/whisper (01)

The commissioned angle holds and is earned from the primary documents. The
Whisper paper states its own claim as robustness, not lowest error: its best
zero-shot model posts an unremarkable 2.5 word error rate on LibriSpeech
test-clean, ties a supervised model there, and beats that same model by an
average 55.2% relative error reduction across twelve other datasets. The scale
figures the lesson depends on (680,000 hours total; 117,000 across 96 other
languages; 125,000 of translation) are stated verbatim in the paper. The
paper, in Section 6, names "complete hallucination where the model will output
a transcript entirely unrelated to the actual audio" as a known failure mode,
and OpenAI's own model card both warns of hallucination and recommends against
use "in high-risk domains like decision-making contexts." The present-day
failure is documented by a peer-reviewed measurement (Koenecke et al., FAccT
2024: 1.4% of transcriptions hallucinated, 38% of those carrying explicit
harm) and by the AP investigation (medical deployment through Nabla). Two
things are thin and flagged below: the ~438,000-hour English figure is a
subtraction the paper never prints, and the one clean controlled hallucination
rate (1.4%) was measured on aphasic speech, a population the same study shows
is disproportionately affected, so it cannot be reported as Whisper's general
rate. Contradictions are real and recorded: clean-benchmark accuracy favors
specialized supervised models, and the severity of hallucination varies by
more than an order of magnitude across the sources depending on the audio.

Library check (targeted `nb history`): zero-shot evaluation is already taught
in `the-evidence/gpt-2` ("the model sees the task described in its input and
nothing else, no examples and no fine-tuning") and used again in
`the-evidence/gpt-3-few-shot`; Background can link rather than re-teach. Word
error rate is *used* as a number in `the-evidence/knowledge-distillation`
(10.7% vs 10.9%) but never defined there, so it is new teaching here.

## Sources

```text
URL:         https://arxiv.org/abs/2212.04356
Kind:        primary. The paper owns every claim about Whisper's data, method,
             and measured results; authored by the model's builders (OpenAI).
Establishes: The dataset scale and composition, the model family, the zero-shot
             robustness result, the text-normalizer caveat on WER comparisons,
             and the paper's own acknowledgment of hallucination as a failure mode.
Paraphrase:  680,000 hours of labeled audio scraped from the internet, trained
             as one encoder-decoder Transformer to do multilingual recognition,
             translation, language ID, and voice-activity detection, evaluated
             zero-shot on datasets it never trained on. Machine-generated (ASR)
             transcripts were filtered out by heuristic to avoid learning
             "transcript-ese." On LibriSpeech clean the model is ordinary; its
             edge is holding up on out-of-distribution audio.
Locators:    Abstract; Section 1 (pp. 1-2); Section 2.1 Data (pp. 2-3); Table 1
             architecture (p. 5); Section 3.1 Zero-shot Evaluation (p. 5);
             Figure 2 and Table 2 robustness (p. 6); Section 6 Limitations (p. 14).
Quote:       "When scaled to 680,000 hours of multilingual and multitask
             supervision, the resulting models generalize well to standard
             benchmarks and are often competitive with prior fully supervised
             results but in a zero-shot transfer setting without the need for any
             fine-tuning. When compared to humans, the models approach their
             accuracy and robustness." (Abstract)
Quote:       "In order to avoid learning 'transcript-ese', we developed many
             heuristics to detect and remove machine-generated transcripts from
             the training dataset." (Section 2.1)
Quote:       "problems such as getting stuck in repeat loops, not transcribing
             the first or last few words of an audio segment, or complete
             hallucination where the model will output a transcript entirely
             unrelated to the actual audio." (Section 6, "Improved decoding
             strategies," p. 14)
Quote:       "Although the best zero-shot Whisper model has a relatively
             unremarkable LibriSpeech clean-test WER of 2.5, which is roughly the
             performance of modern supervised baseline or the mid-2019 state of
             the art, zero-shot Whisper models have very different robustness
             properties than supervised LibriSpeech models and out-perform all
             benchmarked LibriSpeech models by large amounts on other datasets."
             (Section 3.2, p. 6)
```

```text
URL:         https://github.com/openai/whisper/blob/main/model-card.md
Kind:        primary. OpenAI's own release document for the model; owns the
             maker's stated intended use and warnings.
Establishes: That OpenAI itself warned, at release, of hallucination and against
             high-risk decision-making use, which is the exact deployment later
             reported. Also that the maker acknowledges uneven performance across
             languages, accents, and demographic groups.
Paraphrase:  The card tells users to run their own evaluations before deploying,
             warns that output may contain text not present in the audio, and
             names the mechanism as the model combining next-word prediction with
             transcription. It recommends against high-risk decision-making use.
Locators:    Sections "Performance and Limitations" and "Broader Implications".
Quote:       "the predictions may include texts that are not actually spoken in
             the audio input (i.e. hallucination). We hypothesize that this
             happens because ... the models combine trying to predict the next
             word in audio with trying to transcribe the audio itself."
Quote:       "We recommend against using Whisper models to transcribe recordings
             of individuals taken without their consent ... we caution against
             using Whisper models in higher-risk domains like decision-making
             contexts, where flaws in accuracy can lead to pronounced flaws in
             outcomes."
```

```text
URL:         https://facctconference.org/static/papers24/facct24-111.pdf
Kind:        primary. The peer-reviewed study owns its own measurement; authors
             ran the audio through Whisper and coded the results firsthand.
             Published at ACM FAccT 2024. (Also at arxiv.org/abs/2402.08021.)
Establishes: A controlled, quantified hallucination rate and a harm taxonomy,
             plus the finding that hallucination tracks non-vocal (silence)
             duration. This is the independent measurement the commission asked
             for, separate from the AP interviews.
Paraphrase:  Koenecke, Choi, Mei, Schellmann, and Sloane segmented ~40 hours of
             AphasiaBank audio (23 of them from speakers with aphasia) into
             13,140 utterance-length segments and ran them through the default
             Whisper API in April and May 2023. 1.4% of transcriptions contained
             an entire hallucinated phrase or sentence absent from the audio. Of
             those hallucinations, 38% carried explicit harm: 19% perpetuation of
             violence, 13% inaccurate associations, 8% false authority.
             Hallucination occurred disproportionately for speakers with longer
             non-vocal stretches, a symptom of aphasia.
Locators:    Abstract; Section 2.1-2.3 (data and API experiments); Section 2.5
             and Section 3 (categorization, results).
Quote:       "we find that roughly 1% of audio transcriptions contained entire
             hallucinated phrases or sentences which did not exist in any form in
             the underlying audio ... 38% of hallucinations include explicit
             harms such as perpetuating violence, making up inaccurate
             associations, or implying false authority." (Abstract)
Quote:       "hallucinations disproportionately occur for individuals who speak
             with longer shares of non-vocal durations—a common symptom of
             aphasia." (Abstract)
```

```text
URL:         https://www.openslr.org/12
Kind:        primary. The corpus's own distribution page; owns the size figure.
Establishes: A concrete, named ~1,000-hour supervised English corpus the reader
             can scale the 680,000-hour figure against, and the reference set on
             which Whisper's own "unremarkable 2.5" number is measured.
Paraphrase:  LibriSpeech is about 1,000 hours of 16 kHz read English speech
             aligned from LibriVox public-domain audiobooks. Its labeled training
             subsets are 100 + 360 + 500 = 960 hours.
Locators:    Page header and "About" description; subset table.
Quote:       "LibriSpeech is a corpus of approximately 1000 hours of 16kHz read
             English speech."
```

```text
URL:         https://web.stanford.edu/~jurafsky/slp3/16.pdf
Kind:        authoritative reference (primary for the definition). Jurafsky &
             Martin, Speech and Language Processing (3rd ed. draft), the standard
             text; owns the field-standard statement of the metric.
Establishes: The definition of word error rate and a worked example, so the
             lesson can teach the term rather than assert it. Also the standard
             practice of text normalization before scoring, which is why
             Whisper's cross-model comparisons specify "after applying our text
             normalizer."
Paraphrase:  Word error rate aligns the recognizer's output to a reference
             transcript by minimum edit distance, counts substitutions,
             insertions, and deletions, and divides their sum by the number of
             words in the reference; because insertions are included it can
             exceed 100%.
Locators:    Chapter 16 (Automatic Speech Recognition and Text-to-Speech),
             Section 16.6 "ASR Evaluation: Word Error Rate."
Quote:       "Word Error Rate = 100 x (Insertions + Substitutions + Deletions) /
             Total Words in Correct Transcript"
Quote:       Worked example (CallHome): six substitutions, three insertions, one
             deletion against a 13-word reference gives "Word Error Rate = 100 x
             (6+3+1)/13 = 76.9%".
```

```text
URL:         https://apnews.com/article/ai-artificial-intelligence-health-business-90020cdf5fa16c79ca2e5b6c4c9bbb14
Kind:        secondary. The AP reports on a failure it did not itself own or
             measure; it interviews the engineers and researchers who did. By
             Garance Burke and Hilke Schellmann, October 26, 2024.
Establishes: The present-day deployment and its stakes: Whisper-based
             transcription used at scale in medicine, with the original audio
             sometimes destroyed. Supplies independent field observations of
             hallucination separate from the Koenecke study.
Paraphrase:  OpenAI markets Whisper as near "human level robustness and
             accuracy." A University of Michigan researcher found hallucinations
             in eight of every ten public-meeting transcriptions he inspected; a
             machine-learning engineer in about half of 100+ hours; a developer
             in nearly all of 26,000 transcripts. Over 30,000 clinicians and 40
             health systems use Nabla's Whisper-based medical tool, which has
             transcribed an estimated 7 million visits and erases the original
             audio for "data safety reasons," leaving no recording to check the
             transcript against. AP discloses it has a licensing deal with OpenAI.
Locators:    Lede; "The full extent of the problem"; the Nabla passage.
Quote:       "Tech behemoth OpenAI has touted its artificial intelligence-powered
             transcription tool Whisper as having near 'human level robustness and
             accuracy.' But Whisper has a major flaw: It is prone to making up
             chunks of text or even entire sentences."
Quote:       "It's impossible to compare Nabla's AI-generated transcript to the
             original recording because Nabla's tool erases the original audio for
             'data safety reasons,' Raison said."
```

A repetition supports that a claim was made, not that it is true. The AP field
figures (8 of 10; nearly all of 26,000) are uncontrolled counts by individual
practitioners on their own audio, not measured rates on a defined sample; the
one measured rate is Koenecke's 1.4%, and it is on aphasic speech.

## Contradictions

- **Clean-benchmark accuracy favors specialized supervised models, by the
  paper's own admission.** Whisper's best LibriSpeech test-clean WER of 2.5 is
  "roughly the performance of modern supervised baseline or the mid-2019 state
  of the art" (paper, Section 3.2). In Table 2 the comparison supervised model
  (wav2vec2.0 Large, no language model) and Whisper Large V2 tie at 2.7 on
  LibriSpeech Clean. So Whisper is not "the most accurate transcriber" on the
  in-distribution benchmark, which is the whole reason the paper argues for
  measuring robustness instead. This confirms the commission's angle rather than
  undercutting it, but it contradicts the popular reading of Whisper as simply
  the best.

- **The severity of hallucination is genuinely disputed and depends on the
  audio.** Koenecke measures 1.4% on clean, short, utterance-length segments,
  but explicitly finds the rate rises with non-vocal (silence) duration and is
  concentrated in the aphasia group. AP's practitioners report far higher
  incidence (half of 100+ hours; eight of ten meetings; nearly all of 26,000),
  on messier, longer, real-world audio. Both can be true: hallucination is rare
  on clean short clips and common on long or silence-heavy audio. The lesson
  must not present any single number as Whisper's hallucination rate.

- **The paper measured average WER robustness, not verbatim reliability on an
  individual utterance.** Robustness in the paper is average performance across
  distributions (Section 3.2), a claim about aggregate error. Verbatim medical
  and legal transcription needs the opposite: no invented span in any single
  record. The paper's own robustness result and the deployment failure are not
  in contradiction; they measure different things, and today's usage relies on a
  guarantee the paper never made.

- **OpenAI's marketing and OpenAI's model card disagree.** The card recommends
  against high-risk decision-making use; the product is marketed as near human
  robustness and accuracy and has been deployed into exactly such use. Both are
  OpenAI primary sources.

## Numbers

```text
Figure: 680,000 hours of labeled audio (total training set)
Owner:  Whisper paper (Abstract; Section 2.1; Section 4.2)
Scope:  Full multilingual, multitask training corpus scraped from the internet.
```

```text
Figure: 117,000 hours covering 96 other (non-English) languages
Owner:  Whisper paper (Section 1, p. 2)
Scope:  Subset of the 680,000 hours; non-English speech recognition.
```

```text
Figure: 125,000 hours of X->English translation data
Owner:  Whisper paper (Section 1, p. 2)
Scope:  Subset of the 680,000 hours; translation task.
```

```text
Figure: ~438,000 hours English transcription  [DERIVED, not stated]
Owner:  Not printed in the paper. 680,000 - 117,000 - 125,000 = 438,000.
Scope:  English recognition remainder. Present as an inference, not a quote. The
        paper separately states 65% of training compute is spent on the English
        recognition task (Section 4.3), which is a different quantity.
```

```text
Figure: 5,140 hours (SpeechStew, 7 pre-existing datasets combined)
Owner:  Whisper paper (Section 1, p. 1), citing Chan et al. 2021
Scope:  Largest prior combined high-quality supervised set named in the paper;
        the honest "before" number for the scale jump.
```

```text
Figure: "1,000 or so hours typical of an academic supervised dataset"
Owner:  Whisper paper (Section 1, p. 2)
Scope:  The paper's own scale anchor for a single gold-standard corpus.
```

```text
Figure: ~1,000 hours (LibriSpeech), labeled subsets 100+360+500 = 960 hours
Owner:  openslr.org/12
Scope:  A concrete named corpus for the reader to scale 680,000 against.
```

```text
Figure: Model sizes: Tiny 39M, Base 74M, Small 244M, Medium 769M, Large 1550M
Owner:  Whisper paper (Table 1, p. 5)
Scope:  Parameter counts of the released family.
```

```text
Figure: LibriSpeech test-clean WER: best zero-shot Whisper 2.5; Large V2 2.7;
        smallest 39M model 6.7
Owner:  Whisper paper (Section 3.2, p. 6; Table 2)
Scope:  In-distribution reference benchmark, WER after the paper's text normalizer.
```

```text
Figure: 55.2% average relative error reduction (Whisper Large V2 vs wav2vec2.0
        Large, no LM), across 13 non-LibriSpeech / out-of-distribution datasets;
        average WER 12.8 (Whisper) vs 29.3 (wav2vec2.0), tie at 2.7 on LibriSpeech
Owner:  Whisper paper (Table 2, p. 6)
Scope:  Two models matched on LibriSpeech; the gap opens off-distribution. This
        table is the quantitative heart of the robustness claim.
```

```text
Figure: 1.4% of transcriptions contained a hallucination
Owner:  Koenecke et al., FAccT 2024 (Section 3)
Scope:  13,140 utterance-length AphasiaBank segments, default Whisper API,
        April-May 2023. Aphasic + control speech; rate rises with non-vocal time.
```

```text
Figure: 38% of hallucinations carried explicit harm (19% violence, 13%
        inaccurate associations, 8% false authority)
Owner:  Koenecke et al., FAccT 2024 (Section 2.5, Section 3)
Scope:  Denominator is the hallucinated transcriptions, not all transcriptions.
```

```text
Figure: 187 hallucinations in 13,000+ clear audio snippets
Owner:  AP (Oct 26, 2024), reporting the Koenecke study
Scope:  Same study as above; AP's phrasing. 1.4% of 13,140 is ~184; treat 1.4%
        as the primary figure and 187 as the AP retelling of it.
```

```text
Figure: 30,000+ clinicians, 40 health systems, ~7 million visits (Nabla)
Owner:  AP (Oct 26, 2024), attributed to Nabla's CTO Martin Raison
Scope:  Deployment scale of one Whisper-based medical product; company-supplied.
```

## Source assets

```text
Asset: Figure 2, "Zero-shot Whisper models close the gap to human robustness"
       (Whisper paper, p. 6). Scatter of WER on LibriSpeech dev-clean (x) vs
       average WER on Common Voice/CHiME-6/TED-LIUM (y), with supervised
       LibriSpeech models, zero-shot Whisper models, a human point, and the
       y=x ideal-robustness line.
Shows: The core claim in one picture: supervised models sit on the clean axis
       but rise steeply off-distribution (brittle), while Whisper's points hug
       the ideal line and reach the human's confidence interval. A reader sees
       "robustness" as distance from the diagonal, not a single score.
Crop:  Must retain both axis labels, the y=x line, and the three series legend
       (supervised, Whisper, human). Do not crop away the human point or the
       diagonal; they are the comparison.
```

```text
Asset: Table 2, "Detailed comparison of effective robustness across various
       datasets" (Whisper paper, p. 6). Per-dataset WER for wav2vec2.0 Large vs
       Whisper Large V2, with relative error reduction, ending in the 55.2%
       average and the LibriSpeech-Clean tie at 2.7.
Shows: The same finding as numbers: two models identical on LibriSpeech, then a
       50-75% gap on Artie, Common Voice, CHiME-6, and the rest. Good for a small
       excerpt table (LibriSpeech Clean + two or three hard datasets + Average).
Crop:  If excerpted, keep the LibriSpeech-Clean tie row so the "same on clean,
       far apart off-clean" contrast survives; keep the Average row.
```

```text
Asset: Whisper multitask-format diagram (Figure 1, Whisper paper, p. 4) showing
       the token sequence (language tag, task tag, timestamps, transcript) and
       the <|nospeech|> branch.
Shows: Why the model can emit text through silence: it is a decoder always
       predicting the next token, with "no speech" as just one predictable token
       among many. Useful only if the lesson teaches the always-emit mechanism.
Crop:  Keep the "No speech" branch visible; that branch is the point.
```

Koenecke et al. also carry example figures pairing "#Ground truth" audio with
the hallucinated Whisper output (the AP lede image is one such example). Named
here in case the writer wants a concrete before/after; verify licensing before
reproducing.

## Discarded

```text
URL: https://techcrunch.com/2024/10/26/openais-whisper-transcription-tool-has-hallucination-issues-researchers-say/ — Reports on the same AP investigation; a retelling of one origin, so it adds no independent confirmation. Used only to recover the correct AP URL.
URL: https://www.columbian.com/... and other AP wire syndications — Verbatim reprints of the AP story (same origin); returned 403/404 and add nothing the AP page does not.
URL: https://apnews.com/article/...90020cdf5f7c278031bd2fce1c19b3c4 — Wrong slug from an early search; returns "Page unavailable." Correct slug ends ...90020cdf5fa16c79ca2e5b6c4c9bbb14 and resolves.
URL: https://www.alphaxiv.org/abs/2212.04356, https://hackmd.io/@nbswords/BkXJKSEZxx, https://www.emergentmind.com/papers/2212.04356 — Third-party summaries of the Whisper paper; the paper itself was read directly, so summaries are unnecessary and non-authoritative.
URL: https://huggingface.co/openai/whisper-large-v3 — A later model release (v3), not the September 2022 paper or its models; out of scope for a lesson on the 2022 document.
```
