# Evidence: the-mechanics/clock-faces (01)

This record supports all four chain steps, but not evenly. Three steps rest on
primaries I read: the diffusion objective (DDPM, Ho et al. 2020), the 10:10
advertising convention (Karim et al. 2017), and the reading side (three
measured benchmarks: ClockBench, TickTockVQA, MeasureBench). MeasureBench also
supplies the strongest single number tying the two directions together: one
open model emits "10:10" for 72.88% of real clock photos it is asked to read.
The weak step is the generation behavior itself. I found no peer-reviewed,
measured study that systematically tests whether image *generators* render a
requested time; that step is carried by reputable demonstrations (Digital
Camera World; a documented 10-model test on a blog), which are secondary by the
brief's own rule. Two other gaps to flag: no source measures the time
distribution of clock images in an actual training corpus (the "overwhelmingly
10:10" claim about training data is inferred from the advertising convention,
not counted on LAION-scale data), and no source experimentally isolates "no
angle-to-time rule" as the cause of generation failure as opposed to plain
mode-collapse onto the dominant arrangement. The commission's angle survives,
but the settled/open line has moved: newer systems read clocks far better than
the 2025 launch numbers, and at least one 2026 image model largely overrides
the 10:10 prior on a requested time. Both are recorded below in full.

## Sources

```text
URL:         https://arxiv.org/abs/2006.11239
Kind:        primary — Ho, Jain & Abbeel own the definition of the diffusion
             training objective; this is the paper that introduced DDPMs.
Establishes: What a diffusion image generator is trained to do, in the authors'
             words: match the data distribution. Grounds step 1 (the model
             renders the most likely appearance, which is a real description of
             the objective, not a metaphor).
Paraphrase:  A diffusion model is a Markov chain that is trained, by variational
             inference, to turn noise into samples that match the training data.
             It is a latent-variable generative model; nothing in the objective
             rewards a per-image rule, only agreement with the data as a whole.
Locators:    Abstract (first sentence); Introduction, first paragraph.
Quote:       "A diffusion probabilistic model (which we will call a 'diffusion
             model' for brevity) is a parameterized Markov chain trained using
             variational inference to produce samples matching the data after
             finite time." Abstract: "We present high quality image synthesis
             results using diffusion probabilistic models, a class of latent
             variable models inspired by considerations from nonequilibrium
             thermodynamics."
```

```text
URL:         https://www.frontiersin.org/articles/10.3389/fpsyg.2017.01410/full
             (open-access mirror: https://pmc.ncbi.nlm.nih.gov/articles/PMC5572348/)
Kind:        primary — Karim, Lützenkirchen, Khedr & Khalil own the psychological
             experiment; primary to the smiling-face finding. For the
             convention's existence it is a primary statement by researchers who
             surveyed the practice, but they attribute the history to one press
             source (see Locators), so the dating is not their own measurement.
Establishes: That watch advertisements have commonly been set to 10:10 since the
             1950s, and why it persists (it reads as a smiling face and lifts
             the viewer's mood and buying intention). Grounds step 2 (the
             convention in the imagery) and explains the pull behind it.
Paraphrase:  Since the 1950s, ad watches are usually set at 10:10; in the 1920s
             and 1930s they were set at 8:20. Experiment 1 (n=46): 10:10 produced
             significantly more pleasure than 11:30 and 8:20, and significantly
             higher intention to buy than 11:30 (the 8:20 comparison for buying
             just missed significance, p=0.051). Experiment 2 (n=23): people
             rate 10:10 as strongly resembling a smiling face and 8:20 a sad
             face. The effect operates without the viewer being aware of it.
Locators:    Abstract; Introduction (history, citing Newman 2008, NYT, "Why Time
             Stands Still for Watchmakers"); Results, Experiments 1 and 2.
Quote:       "Intriguingly, since the 1950s in watch advertisements the time has
             commonly been set at 10:10."
```

```text
URL:         https://clockbench.ai/  (paper: https://clockbench.ai/ClockBench.pdf)
Kind:        primary — Alek Safar's benchmark owns its own measurement of
             analog-clock reading by frontier models.
Establishes: The reading side (step 4): reading an arbitrary analog clock is
             easy for humans and hard for models, though the gap has narrowed
             since launch. 180 clocks rendered from 36 base faces, 720 questions
             across four task types: reading the time, adding/subtracting time,
             rotating the hands, and shifting time zone.
Paraphrase:  Humans score 90.7% on the current leaderboard; the top model shown
             is at 66.7%, with 35 models listed trailing to about 3.9%. The
             benchmark's framing: a task trivial for humans that current frontier
             models struggle with. (Caution: the per-row model names and scores
             below the top line were read via a page-summarizer and I could not
             independently verify each row; the load-bearing figures are the
             human baseline and the single best-model score.)
Locators:    Leaderboard table and header text on clockbench.ai; methodology
             (four question types) on the same page.
Quote:       "whether models can read analog clocks — a task that is trivial for
             humans, but current frontier models struggle with."
```

```text
URL:         https://the-decoder.com/even-the-best-ai-models-cant-reliably-read-the-clock/
Kind:        secondary — Jonathan Kemper reporting on ClockBench at its launch;
             does not own the measurement.
Establishes: The launch-date state of the reading benchmark, which fixes one end
             of the "gap is closing" timeline. As of publication the best model
             read clocks at 13.3% against a 90%+ human baseline; humans missed by
             a median of ~3 minutes, the best model by a median of about an hour.
Paraphrase:  On 14 Sep 2025 the article reported human 89.1% vs best AI 13.3%
             (Gemini 2.5 Pro), with a named field (Gemini 2.5 Flash 10.5%, GPT-5
             8.4%, Claude Opus 4.1 5.6%, Claude Sonnet 4 4.2%, Grok 4 0.7%).
             These are much lower than the current clockbench.ai leaderboard,
             which is the evidence that newer models improved.
Locators:    Body; model table.
Quote:       (reported) humans "made a median error of just 3 minutes. The best
             AI model missed by a median of one hour."
```

```text
URL:         https://arxiv.org/abs/2603.08011
Kind:        primary — Choi, Lee, You & Lee own TickTockVQA and the Swap-DPO
             results; accepted to CVPR 2026 Findings.
Establishes: The reading side in real-world conditions (step 4), and the
             open/settled line: targeted training closes much of the gap. Base
             VLMs read real-world analog clocks near the floor; a preference-
             tuning method lifts them severalfold.
Paraphrase:  TickTockVQA holds 12,483 human-annotated real-world analog-clock
             images with hour/minute and AM/PM labels. Zero-shot full-time
             accuracy: Llama-3.2-11B 1.41%, Qwen2.5-VL-7B 6.04%, Gemma3-12B
             2.12%. After the authors' Swap-DPO fine-tuning: 46.22%, 23.06%,
             35.32% respectively. Swap-DPO specifically targets hour/minute hand
             swapping. This is direct evidence that the reading failure is
             trainable away, not a hard limit.
Locators:    Abstract; results tables (per-model before/after).
Quote:       "a full-time accuracy of 46.22% on TickTockVQA, representing an
             improvement of 44.81 percentage points over the zero-shot baseline."
```

```text
URL:         https://arxiv.org/abs/2510.26865
Kind:        primary — BAAI FlagEval Team (Fenfen Lin, Yesheng Liu, Haiyu Xu,
             Chen Yue, Zheqi He, et al.) own MeasureBench.
Establishes: The single strongest bridge between the two directions. When asked
             to READ a clock, models fall back on the trained 10:10 pose rather
             than measure the hands — the generative prior surfacing in the
             reading task. Also fixes how low overall instrument-reading accuracy
             is even for the best model.
Paraphrase:  MeasureBench tests VLMs on reading measurement instruments (analog
             clocks, gauges, rulers, thermometers, digital displays). Models
             frequently answer "10:10" regardless of the true time;
             Qwen2.5-VL-72B-Instruct outputs "10:10" for 72.88% of real-world
             clock images and 50.74% of synthetic ones. Best overall accuracy
             (Gemini-2.5-Pro) was 30.2% on real images, 26.3% on synthetic. The
             authors read the "10:10" default as mimicking the product-photo
             pose common in advertising — the same convention Karim et al.
             document.
Locators:    Analysis section on the "10:10" failure mode; results tables.
Quote:       "many models tend to answer '10:10' when reading clock times,
             regardless of the actual time shown in the image"; "Qwen2.5-VL-72B-
             Instruct outputs '10:10' for 72.88% of real-world clock images and
             50.74% of synthetic clock images."
```

```text
URL:         https://petapixel.com/2022/05/17/the-science-behind-why-watches-are-set-to-1010-in-advertising-photos/
Kind:        secondary — Jaron Schneider reporting the convention; repeats the
             Frontiers study and photographer practice, owns neither.
Establishes: Independent confirmation that 10:10 is standard product-photo
             practice, and the practical reason (logo visibility) that sits
             alongside the smiling-face effect. Useful context, not a new fact.
Paraphrase:  Photographers set watches to 10:10 mainly to frame the maker's logo
             (usually printed below 12) between the raised hands; before the
             1950s the norm was 8:20. Cites the Frontiers study for the smile
             effect. Example imagery uses Omega. (17 May 2022.)
Locators:    Body.
Quote:       "most photographers do this to best show the company logo."
```

```text
URL:         https://www.digitalcameraworld.com/tech/artificial-intelligence/why-are-ai-generated-images-of-clocks-always-set-to-10-past-10-i-think-i-know-the-answer
Kind:        secondary — Mike Harris, a documented demonstration and hypothesis,
             not a controlled study.
Establishes: The generation behavior (steps 1–3, observable side) and a useful
             nuance the flat "clocks are always 10:10" claim misses. Attributes
             the pattern to product-photography training data.
Paraphrase:  The author argues AI clock/watch images default to 10:10 because
             training data is dominated by product photography, "the vast
             majority of watch photography is product-based and therefore follows
             the 10:10 rule." In his own limited test with Adobe Firefly,
             *watches* came out predominantly at 10:10 but *wall clocks* came out
             at varied times — i.e., the prior is strongest for watches, weaker
             for clocks. (15 Jan 2025.)
Locators:    Body; the Firefly test paragraphs.
Quote:       "the vast majority of watch photography is product-based and
             therefore follows the 10:10 rule."
```

```text
URL:         http://polymath07.blogspot.com/2026/08/getting-clocks-right-ai-almost-there.html
Kind:        secondary — Polymath07, a documented systematic demonstration (ten
             image models, one fixed prompt); a reproducible test, not a measured
             study, so secondary by the brief's rule.
Establishes: Both the persistence of the 10:10 prior in 2026 image generators and
             the contradiction: a current model can largely override it. Direct
             evidence for step 3 (the missing time-to-angle rule) and its
             fraying.
Paraphrase:  Prompt to ten models: "A beige wall in a store selling clocks,
             showing four circular wall clocks, each reading exactly 3:27."
             Ideogram (P-Image) and Wan 2.7 produced 10:10; several others
             produced scattered or implausible times; Seedream 5.0 got minute
             hands right but hour hands near 3:57. Best was GPT Image 2 (graded
             A-): all four minute hands at :27, hour hands about six minutes
             early (~3:23). So the requested minute can now be hit and the hour
             hand approximately placed — the "no rule at all" story is becoming
             model-specific. (25 Aug 2026.) Individual model rows read via a
             page-summarizer; treat exact per-model wording as reported.
Locators:    Body; per-model results table.
Quote:       (author) clocks default to "10:10 (or sometimes 1:50)" because of
             abundant advertising training material.
```

## Contradictions

- **The reading gap is closing, fast.** ClockBench at launch (the-decoder, Sep
  2025): best model 13.3%. Current clockbench.ai leaderboard: top model ~66.7%
  against a 90.7% human baseline. TickTockVQA shows targeted preference tuning
  lifting a base model from 1.41% to 46.22%. The writer must not present clock
  reading as a fixed wall. It is a large but shrinking gap, and part of the
  shrinkage is deliberate training aimed at the exact failure.

- **At least one 2026 image generator largely overrides the 10:10 prior.**
  Polymath07's GPT Image 2 hit the requested minute (:27) on all four clocks and
  placed the hour hand within ~6 minutes, on a prompt asking for 3:27. This is
  the commission's predicted contradiction (newer systems doing better). What
  would settle whether the mechanism changed: knowing whether the gain comes
  from added clock-specific training data, a planning/tool step, or a different
  architecture. The demonstration cannot distinguish these; it only shows the
  output improved.

- **The prior is strongest for watches, not all clocks.** Digital Camera World's
  Firefly test produced varied times for wall clocks but 10:10 for watches. The
  commission's clean "ask for 3:15, get 10:10" is most reliable for watches and
  wristwatch-style faces. A careful lesson should say "watches and watch-like
  clocks" where it wants the strongest version.

- **No source contradicts the dataset-prior cause.** MeasureBench explicitly
  reads the "10:10" answer as mimicking the advertising pose, matching the
  commission. I found no primary attributing the behavior to a different cause
  (e.g., an architectural inability unrelated to data). The open question is not
  *whether* the dataset prior drives it but *how much* of the remaining failure
  is the prior versus a genuinely absent time-to-angle computation — no source
  isolates that experimentally.

## Numbers

```text
Figure: humans 90.7%, best model 66.7% (current leaderboard)
Owner:  ClockBench (clockbench.ai)
Scope:  720 questions over 180 clocks (36 base faces), four task types; % correct
```

```text
Figure: humans 89.1%, best model 13.3% (Gemini 2.5 Pro) at launch
Owner:  ClockBench, as reported by the-decoder, 14 Sep 2025
Scope:  same benchmark, launch snapshot; median human error ~3 min, best model ~1 hr
```

```text
Figure: "10:10" answered for 72.88% of real / 50.74% of synthetic clock images
Owner:  MeasureBench (arXiv 2510.26865), for Qwen2.5-VL-72B-Instruct
Scope:  reading task; share of clock images given the canned 10:10 answer
```

```text
Figure: best overall instrument-reading accuracy 30.2% real / 26.3% synthetic
Owner:  MeasureBench, for Gemini-2.5-Pro
Scope:  all instrument types, not clocks alone; % correct
```

```text
Figure: full-time reading accuracy 1.41% -> 46.22% (Llama-3.2-11B)
Owner:  TickTockVQA / Swap-DPO (arXiv 2603.08011)
Scope:  12,483 real-world clock images; zero-shot vs after preference tuning.
        Also Qwen2.5-VL-7B 6.04%->23.06%; Gemma3-12B 2.12%->35.32%.
```

```text
Figure: 10:10 the ad standard since the 1950s; 8:20 was the 1920s-30s norm
Owner:  Karim et al. 2017 (Frontiers in Psychology 8:1410)
Scope:  watch advertising practice; historical claim attributed to Newman 2008 (NYT)
```

```text
Figure: 10:10 vs 11:30 pleasure t45=3.817, p<0.001; buy intention t45=2.430, p<0.05
Owner:  Karim et al. 2017, Experiment 1 (n=46)
Scope:  the pull behind the convention, not the clock-reading behavior
```

```text
Figure: requested 3:27 -> GPT Image 2 minute hands :27, hour hands ~3:23
Owner:  Polymath07 blog demonstration, 25 Aug 2026
Scope:  one prompt, ten models; a demonstration, not a measured study
```

## Source assets

```text
Asset: ClockBench leaderboard table (clockbench.ai) — human row vs model rows
Shows: the size of the human-vs-model gap and its current top; the four task
       columns show reading is only one of the things tested
Crop:  must keep the human baseline row and the top model row together so the
       gap is legible; may omit the long tail below the top few rows
```

```text
Asset: MeasureBench "10:10" frequency figures/tables (arXiv 2510.26865)
Shows: the trained pose leaking into the reading task — a model answering 10:10
       most of the time regardless of the true face
Crop:  retain the Qwen 72.88% real / 50.74% synthetic figures and the model name;
       omit unrelated instrument types if cropping to the clock finding
```

```text
Asset: TickTockVQA before/after accuracy table (arXiv 2603.08011)
Shows: the reading failure is trainable away — small numbers becoming mid-range
       after targeted tuning
Crop:  keep both the zero-shot and post-tuning columns for the same models;
       a single column loses the whole point
```

```text
Asset: Karim et al. 2017 resemblance figure (10:10 smile vs 8:20 frown)
Shows: why the convention is sticky — the face the hands trace
Crop:  keep the 10:10 and 8:20 panels side by side
```

```text
Asset: Polymath07 grid of ten models' clocks for a requested 3:27
Shows: the spread from 10:10 (Ideogram, Wan) to nearly-right (GPT Image 2) in
       one frame — the behavior and its 2026 contradiction together
Crop:  keep at least one 10:10 failure beside the GPT Image 2 near-hit; the
       contrast is the asset. Attribute as a demonstration, not a measurement.
```

## Discarded

```text
URL: https://analyticsindiamag.com/ai-news-updates/its-disturbing-how-openais-dall%C2%B7e-flux-1-and-other-image-generators-cant-grasp-time-always-stuck-at-1010/
     — the page did not resolve to the clock article on fetch; it returned
     unrelated, rotated news items. I could not open the clock content at its own
     address, so I do not cite it. The same generation behavior is covered by
     Digital Camera World and the Polymath07 test, which did resolve.
```

```text
URL: https://clocks.brianmoore.com/
     — "AI World Clocks" tests whether models can WRITE HTML/CSS code to draw a
     clock at a given time, not whether a diffusion model renders pixels. It is a
     code-generation task, a different mechanism, and would mislead if cited for
     the diffusion prior. Noted here so the writer does not conflate it with the
     image-generation behavior.
```

```text
URL: https://www.yahoo.com/tech/why-ai-generated-images-clocks-101000445.html
     — syndication of the Digital Camera World piece (Mike Harris). Same content,
     not an independent source; cite Digital Camera World's own page instead.
```

```text
URL: watch-blog pages claiming Hamilton used 10:10 from 1926 and Rolex in the
     1940s (surfaced in search) — brand-and-date specifics that the primary
     (Karim et al.) does not make; Karim states "no specific brands" and dates
     only "since the 1950s," citing Newman 2008. Do not assert the Hamilton/Rolex
     dating; it is not in a source I could verify to a primary.
```
