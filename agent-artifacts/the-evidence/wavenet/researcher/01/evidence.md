# Evidence: the-evidence/wavenet (researcher round 01)

The evidence supports the commissioned angle without needing to stretch it. The
2016 WaveNet paper (van den Oord et al., arXiv:1609.03499) earns its
naturalness claim on a narrow, specific measurement: a five-point MOS test on
100 held-out sentences from one female speaker, each rated by eight
crowdsourced listeners, run separately for North American English and
Mandarin, with WaveNet closing roughly half the gap to natural recordings and
falling clearly short of it (4.21 vs. 4.55 in English; 4.08 vs. 4.21-4.25 in
Mandarin). The paper itself says nothing about how slow generation is — no
real-time factor, no timing figure, only the observation that generation is
sequential. The concrete "how slow" numbers (172 timesteps/second on a P100,
versus 24,000 samples/second needed to be real time) come from the 2017
Parallel WaveNet paper, not the original. That paper also shows the
much-quoted post-distillation "near-human" MOS of 4.41 was measured on a new,
higher-fidelity 24 kHz/16-bit/65-hour corpus, not the original 16 kHz/8-bit
corpus the 4.21 figure came from — the two numbers are not on the same scale.
DeepMind's and Google's own deployment posts add at least two more MOS
readings (4.347/4.314/3.966/4.236 for four Assistant voices against a human
baseline of 4.667; 4.1 for Cloud Text-to-Speech against a differently stated
"over 70%" gap closure), each from its own listening test with its own human
baseline, which is itself direct, sourced proof that MOS figures do not
travel between tests.

Where the record is thin: the 2016 paper does not state how many hours of
TIMIT it used for the speech-recognition probe or give a baseline PER to
compare its 18.8 PER against, so that number can be reported but not put in
context from the paper alone. The Parallel WaveNet paper's deployment claims
(Google Assistant, TPU use) are stated in DeepMind's own blog posts rather
than in the peer-reviewed paper text itself, though the paper does state the
deployment fact plainly. I could not verify the original WaveNet paper's blog
announcement date to the day (found September 8, 2016, four days before the
v1 arXiv submission of September 12, 2016); I recommend citing only the month
and year rather than a specific day.

## Sources

```text
URL:         https://arxiv.org/abs/1609.03499 (paper text read via full-text
             rendering; PDF at https://arxiv.org/pdf/1609.03499)
Kind:        Primary — the authoring paper; it owns every claim about the
             model architecture, the datasets it used, the MOS methodology
             and results, and the TIMIT probe.
Establishes: The dilated-causal-convolution architecture; the exact datasets
             and hours per task; the MOS test design and numbers; the TIMIT
             phoneme-error-rate result; that the paper itself makes no
             real-time or generation-speed claim.
Paraphrase:  WaveNet is a fully probabilistic autoregressive model that
             predicts each raw audio sample from all previous samples,
             trained directly on waveforms rather than on hand-engineered
             vocoder features. Modeling raw waveforms was considered
             infeasible because they run at "at least 16,000 samples per
             second," and a causal convolutional network needs either huge
             filters or huge depth to see back far enough; dilated causal
             convolutions solve this by skipping inputs at an exponentially
             growing step size, so receptive field grows exponentially with
             depth instead of linearly. On text-to-speech, WaveNet was
             evaluated against the then-best LSTM-RNN statistical-parametric
             system and an HMM-driven unit-selection concatenative system, in
             both North American English (24.6 hours from one professional
             female speaker) and Mandarin Chinese (34.8 hours, one female
             speaker), both at 16 kHz. A separate multi-speaker experiment
             used 44 hours from 109 speakers (VCTK). Music generation used
             the ~200-hour MagnaTagATune dataset and a ~60-hour scraped
             YouTube piano dataset. A secondary speech-recognition experiment
             trained WaveNet as a discriminative model on TIMIT and reported
             18.8 phoneme error rate (PER), which the paper calls the best
             score for a model trained directly on raw audio on TIMIT — it
             does not report hours of TIMIT audio used or a specific prior
             PER to benchmark against. On generation cost, the only sentence
             in the paper is that "the predictions are sequential: after each
             sample is predicted, it is fed back into the network to predict
             the next sample" — no timing number, real-time factor, or
             discussion of deployability appears anywhere in the paper.
Locators:    Abstract; Section 2.1 (dilated causal convolutions, receptive
             field, and the "sequential" sentence); Section 3 experiments
             (dataset descriptions, hours, speaker counts); Table 1 (MOS
             results); the subjective-evaluation methodology paragraph
             preceding Table 1; the speech-recognition subsection reporting
             18.8 PER; Section 4 (limitations: receptive field of about 300
             ms in unconditional generation, occasional wrong-word stress
             when conditioned only on linguistic features, and lack of
             long-range coherence in music).
Quote:       "When generating with the model, the predictions are
             sequential: after each sample is predicted, it is fed back into
             the network to predict the next sample."
```

```text
URL:         https://arxiv.org/abs/1711.10433 (paper text read via full-text
             rendering; PDF at https://arxiv.org/pdf/1711.10433)
Kind:        Primary — the authoring follow-up paper, co-written by several
             of the original WaveNet authors plus new co-authors including
             Demis Hassabis; it owns the claims about the original model's
             measured generation speed, the distillation method, and the new
             MOS comparison.
Establishes: The concrete generation-speed figures for the original,
             un-distilled WaveNet; the distillation method (probability
             density distillation of an inverse-autoregressive-flow student
             from a WaveNet teacher); the MOS comparison on both the old and
             a new, higher-fidelity corpus; that the system was deployed by
             Google Assistant.
Paraphrase:  The original WaveNet's own optimized implementation reaches "172
             timesteps/second for a minibatch of size 1" on an Nvidia P100
             GPU — far short of the 24,000 samples/second the model actually
             needs to run in real time for 24 kHz audio, and the paper calls
             it "poorly suited to today's massively parallel computers" and
             "hard to deploy in a real-time production setting" for exactly
             that reason. Probability density distillation trains a parallel
             feed-forward inverse-autoregressive-flow "student" to match a
             pretrained autoregressive WaveNet "teacher," using a combination
             of a KL-divergence-based distillation loss with power, and later
             perceptual and contrastive loss terms, so the student can
             generate all samples of an utterance at once instead of one at a
             time. The distilled model reaches "over 500,000 timesteps/second
             with the same batch size of 1," which the paper calls "three
             orders of magnitude" faster than the teacher. Table 1 reports
             two separate blocks of results: the top three rows reproduce the
             2016 paper's English single-speaker numbers verbatim on the
             original 16 kHz, 8-bit mu-law, 25-hour corpus (citing the 2016
             paper as their source); the bottom three rows are new results on
             a different, upgraded 24 kHz, 16-bit linear-PCM, 65-hour
             single-speaker corpus, where autoregressive WaveNet and the
             distilled model score identically at 4.41 and both beat a
             24 kHz concatenative baseline at 4.19. Table 2 adds four English
             speakers and one Japanese speaker (9-65 hours of data each),
             with the distilled model beating parametric and concatenative
             baselines for every speaker. The paper states the resulting
             system "is deployed online by Google Assistant, including
             serving multiple English and Japanese voices."
Locators:    Abstract; Section 2 (motivation, "poorly suited to... parallel
             computers"); Section on inference speed reporting 172 and
             500,000+ timesteps/second on a P100 GPU; Table 1 and its
             surrounding text (dataset specs: "16kHz, 8-bit mu-law, 25h
             data" vs. "24kHz, 16-bit linear PCM, 65h data"); Table 2
             (multi-speaker MOS); Table 3 (ablation of loss terms);
             Conclusion (deployment statement).
Quote:       "Because WaveNet relies on sequential generation of one audio
             sample at a time, it is poorly suited to today's massively
             parallel computers, and therefore hard to deploy in a real-time
             production setting."
```

```text
URL:         https://deepmind.google/discover/blog/wavenet-a-generative-model-for-raw-audio/
Kind:        Primary — DeepMind's own first-party announcement of its own
             paper, published by the authoring lab. It restates the paper's
             own numbers rather than independently generating them, so it is
             not a second confirmation of the MOS figures, only a public
             restatement.
Establishes: How DeepMind itself chose to present the 2016 result publicly:
             the same Table 1 MOS numbers as the paper, framed as "reducing
             the gap with human performance by over 50%," with no generation
             speed or deployment claim at all.
Paraphrase:  The post reproduces the paper's English and Mandarin MOS figures
             exactly (WaveNet 4.21/4.08, concatenative 3.86/3.47, parametric
             3.67/3.79, human 4.55/4.21) and frames the result only as a
             quality improvement in listening tests, publishing audio samples
             rather than a deployable product. It explicitly flags the
             generation cost as a present-tense drawback rather than a solved
             problem: "Building up samples one step at a time like this is
             computationally expensive, but we have found it essential for
             generating complex, realistic-sounding audio." No claim of
             real-time capability or production use appears anywhere in the
             post.
Locators:    Body text and the two MOS comparison tables/charts embedded in
             the post (English and Mandarin); the paragraph on generation
             cost immediately following the architecture description.
Quote:       "Building up samples one step at a time like this is
             computationally expensive, but we have found it essential for
             generating complex, realistic-sounding audio."
```

```text
URL:         https://deepmind.google/discover/blog/wavenet-launches-in-the-google-assistant/
Kind:        Primary — DeepMind's own announcement of its own deployment,
             co-written by DeepMind and Google Assistant staff (byline:
             Aäron van den Oord and Tom Walters of DeepMind, Trevor Strohman
             of Google), dated October 4, 2017.
Establishes: The concrete production generation-speed figure; the specific
             per-voice MOS scores at launch; the human MOS baseline used in
             this specific evaluation; that this was the first product to
             run on Google's second-generation TPU.
Paraphrase:  The updated, distilled WaveNet generates "waveforms with 24,000
             samples a second" and "requires just 50 milliseconds to create
             one second of speech," a figure the post calls "1,000 times
             faster than the original model." It reports MOS scores for four
             specific launched voices: US English Voice I at 4.347, Voice II
             at 4.314, a third-party voice at 3.966, and the Japanese voice
             at 4.236 — "where even human speech is rated at just 4.667" in
             this test. All four beat the prior, non-WaveNet voices used
             before this launch. This is a different human MOS baseline
             (4.667) than either English human baseline in the 2016 paper's
             Table 1 (4.46 and 4.55), evidence that human-recording MOS is
             itself specific to the test it was measured in, not a fixed
             constant.
Locators:    Body paragraphs stating the 50ms/1,000x figures; the per-voice
             MOS list; the sentence naming the TPU.
Quote:       "the new US English voice I gets a mean-opinion-score (MOS) of
             4.347 on a scale of 1-5, where even human speech is rated at
             just 4.667"
```

```text
URL:         https://deepmind.google/discover/blog/high-fidelity-speech-synthesis-with-wavenet/
Kind:        Primary — DeepMind's own announcement of the Parallel WaveNet
             paper, dated November 22, 2017.
Establishes: DeepMind's own plain-language statement of the distillation
             method and the "more than 1000 times faster" headline figure;
             confirms the 4.667 human MOS baseline appears in more than one
             DeepMind post, not as a one-off number.
Paraphrase:  Describes probability density distillation as training a
             smaller "student" network to mimic a pretrained WaveNet
             "teacher," so the student can generate "the first and last word
             — and everything in between — at the same time" instead of
             sample by sample. Repeats that the production model is "more
             than 1000 times faster than the original" and repeats the 4.667
             human MOS figure from the Assistant launch post.
Locators:    The paragraphs describing teacher/student distillation; the
             sentence giving the 1000x figure; the sentence repeating the
             4.667 human baseline.
Quote:       "Note that even human speech is rated at just 4.667 on the MOS
             scale."
```

```text
URL:         https://cloud.google.com/blog/products/ai-machine-learning/introducing-cloud-text-to-speech-powered-by-deepmind-wavenet-technology
Kind:        Primary — Google's own first-party product announcement (Google
             Cloud), dated March 27, 2018, describing a different WaveNet
             deployment (a public API product) than the Assistant launch.
Establishes: A third, independently reported MOS figure and a differently
             stated gap-closure percentage for a different product and
             audience than either the original paper or the Assistant
             launch, reinforcing that MOS scores are specific to their own
             test and cannot be pooled across deployments.
Paraphrase:  Cloud Text-to-Speech's WaveNet voices scored "an average
             mean-opinion-score (MOS) of 4.1 on a scale of 1-5 — over 20%
             better than for standard voices and reducing the gap with human
             speech by over 70%." This 4.1 figure and "70%" gap-closure claim
             are neither the 2016 paper's 51%/69% gap-closure figures nor the
             per-voice Assistant scores from October 2017 (4.347/4.314/
             3.966/4.236); it is a fourth distinct MOS reading tied to its
             own test population and voice set. The post also repeats the
             1,000x speed and 50ms-per-second-of-speech figures.
Locators:    The MOS/quality paragraph; the speed paragraph; the paragraph
             describing WaveNet's history as "In late 2016, DeepMind
             introduced the first version of WaveNet."
Quote:       "people gave the new US English WaveNet voices an average
             mean-opinion-score (MOS) of 4.1 on a scale of 1-5 — over 20%
             better than for standard voices and reducing the gap with human
             speech by over 70%."
```

```text
URL:         https://www.engadget.com/2016-09-10-google-deepmind-ai-wavenet-text-to-speech.html
Kind:        Secondary — Engadget, an outlet with no authorship stake in
             WaveNet, reporting on the 2016 announcement from outside
             DeepMind. By Mariella Moon, published September 10, 2016.
Establishes: That contemporary press coverage, at least in this case, did
             not inflate the 2016 result into a "human-level" or
             "indistinguishable from human" claim; it accurately reported a
             gap-closing result and explicitly noted the technology was not
             yet deployable.
Paraphrase:  The article reports the "over 50 percent" gap-closure figure
             and that blind-test subjects rated WaveNet's output more human
             than the other systems, without claiming parity with human
             speech. It explicitly notes deployment was not imminent: "we're
             still far from using a WaveNet-powered app." This is one data
             point of accurate contemporary framing, not proof that all 2016
             coverage was this careful; it does not establish how the
             "human-level" shorthand entered later, looser retellings, which
             I could not trace to a specific originating article.
Locators:    Full short article body.
Quote:       "we're still far from using a WaveNet-powered app"
```

```text
URL:         https://arxiv.org/abs/2106.15561
Kind:        Secondary — an outside academic survey (Xu Tan, Tao Qin, Frank
             Soong, Tie-Yan Liu; Microsoft Research Asia; submitted June 29,
             2021), independent of DeepMind, cataloguing the neural
             text-to-speech field including WaveNet's successors.
Establishes: The present-day standing of the original 2016 architecture
             relative to later vocoder families, independent of DeepMind's
             own framing.
Paraphrase:  The survey names WaveNet as "the first neural-based vocoder,"
             autoregressive by design, and states plainly that "although
             WaveNet achieves good voice quality, it suffers from slow
             inference speed." It groups Parallel WaveNet under flow-based
             vocoders as the method that "leverages probability density
             distillation to marry the efficient sampling of [inverse
             autoregressive flow] with the efficient training of
             [autoregressive] modeling," and separately catalogues GAN-based
             vocoders (WaveGAN, GAN-TTS, MelGAN, Parallel WaveGAN, HiFi-GAN)
             and diffusion-based vocoders (DiffWave, WaveGrad, PriorGrad) as
             the families that came after and are used for fast synthesis
             today. This supports, from outside DeepMind, that the field
             moved past the original sequential architecture for production
             use, while crediting it as the origin point.
Locators:    Section 2.4 ("Vocoders"), subsections on autoregressive,
             flow-based, GAN-based, and diffusion-based vocoders.
Quote:       "Although WaveNet achieves good voice quality, it suffers from
             slow inference speed."
```

## Contradictions

- **The 2016 paper makes no generation-speed claim; the "famously slow"
  framing is entirely a later addition.** The 2016 paper's only sentence on
  generation is that it is "sequential" (Section 2.1); it gives no timing
  number, no real-time factor, and does not discuss deployability. All
  concrete numbers (172 timesteps/second original; 500,000+ timesteps/second
  distilled; 24,000 samples/second needed for real time; 1000x; 50
  milliseconds) come from the 2017 Parallel WaveNet paper and DeepMind's own
  2017 blog posts. A lesson that treats the speed problem as something "the
  paper reports" would be misattributing a follow-up's numbers to the
  original. I searched specifically for a speed or real-time statement
  anywhere in the 2016 paper's text and found none.

- **The widely repeated "near-human" 4.41 MOS is not on the same scale as the
  2016 paper's 4.21.** Table 1 of the Parallel WaveNet paper measures the
  distilled model's 4.41 on a new 24 kHz, 16-bit, 65-hour corpus, not the
  original 16 kHz, 8-bit, 24.6/25-hour corpus the 2016 paper's 4.21 came from.
  The improvement from 4.21 to 4.41 therefore reflects a change of recording
  quality and corpus as well as any change of method; the paper does not
  isolate how much of the gain is attributable to distillation alone versus
  the better underlying audio. I looked for a same-corpus, apples-to-apples
  comparison between the original architecture and the distilled one and did
  not find one in either paper.

- **The human MOS baseline itself moves between tests: 4.55/4.46 (2016
  English), 4.21/4.25 (2016 Mandarin), and 4.667 (2017 Assistant launch,
  repeated in the November 2017 blog).** None of these are the same
  recording set or rater pool, so none can be read as "the" ceiling for
  human speech on this scale. This directly supports the "MOS does not
  travel between tests" caution the commission asks the lesson to carry, and
  I verified it by reading the exact sentence in both 2017 DeepMind posts
  rather than relying on a summary.

- **Three different, non-reconcilable percentage/points figures describe
  "how much of the gap to human speech WaveNet closed":** the 2016 paper and
  2016 blog both say 51% (English) and 69% (Mandarin, from the 0.69-to-0.34
  and 0.42-to-0.13 point drops in Table 1's own English/Mandarin gaps); the
  Google Cloud Text-to-Speech post (2018) says "over 70%" without naming a
  language or citing the underlying point values. These are not
  contradictions about the same measurement — they are separate
  measurements on separate voices and products — but a lesson that quotes
  one figure as "the" gap-closure number without naming which test it comes
  from would flatten a real difference.

- I searched for a specific press piece that inflated the 2016 result to
  "indistinguishable from human speech" or a comparable overclaim, since the
  commission's angle assumes the memory of WaveNet outruns the paper. The one
  piece of contemporary coverage I read in full (Engadget, September 2016)
  did not do this — it accurately reported a gap-closing result and flagged
  that deployment was not imminent. I did not find a specific originating
  article for the looser "human-level" shorthand; it appears to be a drift
  that happened across many retellings over years rather than a traceable
  single overclaim, and the record should not assert a cause I could not
  verify.

## Numbers

```text
Figure: WaveNet MOS, North American English: 4.21 ± 0.081
Owner:  van den Oord et al. 2016 (arXiv:1609.03499), Table 1
Scope:  100 held-out sentences, one female speaker, 8 raters per stimulus,
        crowdsourced, headphone-failure ratings (~40%) excluded
```

```text
Figure: WaveNet MOS, Mandarin Chinese: 4.08 ± 0.085
Owner:  van den Oord et al. 2016, Table 1
Scope:  Same test design as above, Mandarin corpus (34.8 hours, one female
        speaker)
```

```text
Figure: Natural speech MOS, English: 4.46 ± 0.067 (8-bit mu-law), 4.55 ± 0.075
        (16-bit linear PCM)
Owner:  van den Oord et al. 2016, Table 1
Scope:  Same 100-sentence, 8-rater test as the WaveNet English score above
```

```text
Figure: Natural speech MOS, Mandarin: 4.25 ± 0.082 (8-bit mu-law), 4.21 ± 0.071
        (16-bit linear PCM)
Owner:  van den Oord et al. 2016, Table 1
Scope:  Same test design, Mandarin corpus; note the 16-bit reading is
        slightly lower than the 8-bit reading here, unlike in English —
        reported as-is, within the stated confidence intervals
```

```text
Figure: Parametric (LSTM-RNN) MOS: 3.67 ± 0.098 (English), 3.79 ± 0.084
        (Mandarin); Concatenative (HMM) MOS: 3.86 ± 0.137 (English),
        3.47 ± 0.108 (Mandarin)
Owner:  van den Oord et al. 2016, Table 1
Scope:  Same 100-sentence, 8-rater test as above; these are the "previous
        best" baselines WaveNet is measured against
```

```text
Figure: Gap-to-human closed by WaveNet: 51% (English, 0.69 points to 0.34),
        69% (Mandarin, 0.42 points to 0.13)
Owner:  van den Oord et al. 2016, Section 3.1 / Table 1 (percentages stated
        directly in the paper's text, computed from the 16-bit natural row)
Scope:  Same English/Mandarin single-speaker tests as above
```

```text
Figure: Speech-recognition result on TIMIT: 18.8 phoneme error rate (PER)
Owner:  van den Oord et al. 2016, speech-recognition subsection
Scope:  TIMIT dataset; hours of audio used and a specific prior-PER baseline
        are not stated in the paper — reported as a standalone figure, not a
        comparison, because the paper does not supply the comparison point
```

```text
Figure: Original WaveNet generation speed: 172 timesteps/second (minibatch
        size 1, Nvidia P100 GPU); real-time requirement: 24,000
        samples/second
Owner:  van den Oord et al. 2017, Parallel WaveNet (arXiv:1711.10433)
Scope:  DeepMind's own optimized implementation of the original
        autoregressive model, not the 2016 paper's own benchmark (the 2016
        paper gives no such figure)
```

```text
Figure: Distilled WaveNet generation speed: >500,000 timesteps/second (same
        batch size); "three orders of magnitude" speed-up; production
        figure "1,000 times faster than the original," 50 milliseconds to
        generate one second of speech, 24,000 samples/second output
Owner:  van den Oord et al. 2017 (speed figures); DeepMind blog, "WaveNet
        launches in the Google Assistant" (Oct. 4, 2017) and "High-fidelity
        speech synthesis with WaveNet" (Nov. 22, 2017) (the 1,000x/50ms
        production figures)
Scope:  Same P100 GPU benchmark for the raw timestep figures; the 50ms/1000x
        figures describe the deployed Assistant system specifically
```

```text
Figure: Distilled ("near-human") MOS on new corpus: 4.41 ± 0.069
        (autoregressive teacher) and 4.41 ± 0.078 (distilled student);
        24 kHz concatenative baseline on same corpus: 4.19 ± 0.097
Owner:  van den Oord et al. 2017, Table 1 (bottom block)
Scope:  A different corpus than the 2016 figures above: 24 kHz, 16-bit
        linear PCM, 65 hours, one female speaker — not directly comparable
        to the 4.21/3.86/3.67 figures from the 16 kHz/8-bit/25-hour corpus
        in the same table's top block
```

```text
Figure: Google Assistant launch voice MOS: US English Voice I 4.347, Voice
        II 4.314, third-party voice 3.966, Japanese voice 4.236; human
        baseline in this test 4.667
Owner:  DeepMind blog, "WaveNet launches in the Google Assistant" (Oct. 4,
        2017); human baseline repeated in "High-fidelity speech synthesis
        with WaveNet" (Nov. 22, 2017)
Scope:  Production Assistant voices at launch, a distinct test/rater pool
        from both the 2016 paper's tests and the Parallel WaveNet paper's
        Table 1/2 tests
```

```text
Figure: Cloud Text-to-Speech voice MOS: 4.1; described as "over 20% better
        than standard voices" and "reducing the gap with human speech by
        over 70%"
Owner:  Google Cloud blog, "Introducing Cloud Text-to-Speech powered by
        DeepMind WaveNet technology" (Mar. 27, 2018)
Scope:  Cloud Text-to-Speech US English WaveNet voices specifically; its own
        test population, not comparable point-for-point to the Assistant or
        2016 figures above
```

## Source assets

```text
Asset: Figure 3, "Visualization of a stack of dilated causal convolutional
       layers," arXiv:1609.03499 (van den Oord et al. 2016)
Shows: Four stacked convolutional layers with dilation 1, 2, 4, 8, making
       visible how each added layer lets a unit "see" exponentially further
       back in the input sequence without adding more layers per unit of
       receptive field than a normal causal convolution would need.
Crop:  Must keep all four layers and the dilation labels on each; the point
       is the shape of growth across layers, not any single layer.
```

```text
Asset: Table 1, arXiv:1609.03499, the MOS results table (English and
       Mandarin columns; parametric, concatenative, WaveNet, and two natural
       rows)
Shows: The full set of numbers a reader needs to see the size of the gap
       WaveNet closed and the size of the gap that remained, in both
       languages at once.
Crop:  Keep both language columns and both natural-speech rows (8-bit and
       16-bit); dropping either natural row would hide the discrepancy noted
       in Numbers above (the Mandarin 16-bit row scoring lower than 8-bit).
```

```text
Asset: Figure 5, arXiv:1609.03499, paired-preference bar charts (WaveNet(L)
       vs. WaveNet(L+F); baseline vs. WaveNet(L+F))
Shows: How much listeners preferred WaveNet conditioned on both linguistic
       features and fundamental frequency (F0) versus linguistic features
       alone, and versus the prior best baseline, as a forced-choice
       preference rather than an absolute MOS score.
Crop:  Only useful together with a definition of what "L" and "F"
       conditioning mean; do not crop out the axis/percentage labels.
```

None found for the Parallel WaveNet paper, the DeepMind blog posts, or the
Google Cloud post: I did not identify a static figure in any of those
sources — beyond the tables of numbers already listed above, which the
writer can render as a table rather than a chart — that would carry the
argument better than prose. The blog posts' audio-sample players are not
static visual assets.

## Discarded

```text
URL: https://arxiv.org/pdf/1609.03499 — opened directly as a PDF fetch; the
     PDF binary could not be parsed by the fetch tool into readable text, so
     I read the same paper via its full-text HTML rendering
     (ar5iv.labs.arxiv.org/html/1609.03499) instead and verified the
     underlying arxiv.org/abs page resolves and matches. Not a rejection of
     the source, only of that access route; the citation address recorded
     above is the paper's own arxiv.org page, not the ar5iv mirror.
```

```text
URL: https://arxiv.org/abs/1611.09482 ("Fast Wavenet Generation Algorithm,"
     Paine et al., Nov. 2016) — opened the abstract. This is an independent,
     non-DeepMind paper proposing a caching optimization for WaveNet
     inference; it is a plausible source for the "how slow" narrative but
     its abstract page did not surface a concrete timing figure, and the
     Parallel WaveNet paper already supplies an authoritative, DeepMind-owned
     number (172 timesteps/second) for the same claim. Not pursued further
     to avoid citing a number I had not verified.
```

```text
URL: https://en.wikipedia.org/wiki/WaveNet — surfaced repeatedly in search
     results as a summary of WaveNet's history and reception. Not opened as
     a citable source: it is a tertiary aggregation with no authorship stake
     and no claim it originates, and every figure on it traces back to
     sources already read directly above.
```

```text
URL: https://techcrunch.com/2017/10/04/googles-wavenet-machine-learning-based-speech-synthesis-comes-to-assistant/
     — surfaced in search results describing the same October 2017 Assistant
     launch already covered directly by DeepMind's own launch post. Not
     opened in full: it would be a second, weaker (secondary, non-owning)
     source for a fact already established by the primary announcement, and
     the source floor's secondary slot is already filled by a source (the
     neural-TTS survey) that changes the interpretation rather than
     repeating a fact already on record.
```
