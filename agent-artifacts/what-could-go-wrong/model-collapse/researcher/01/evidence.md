# Evidence: what-could-go-wrong/model-collapse (researcher 01)

The evidence firmly supports the commission's central line: recursive training that
*replaces* real data with a prior generation's synthetic output collapses models in
controlled experiments, with the tails of the distribution vanishing first, and this
is demonstrated (not merely argued) in both the 2023 precursor and the 2024 Nature
paper, in the authors' own words and numbers. The primary rebuttal is also strong:
Gerstgrasser et al. show, empirically across three model classes and theoretically in
a linear-regression framework, that *accumulating* data (keeping all prior real and
synthetic data and growing the pool) avoids collapse where replacement causes it. The
tension the commission wants is real and gets sharper than the commission's own framing:
it is not just "replacement collapses, accumulation is safe." Three complications
belong in the piece. First, Shumailov et al.'s own "10%-preserved" condition — a fixed
small retention of original data, not full accumulation — only slows collapse, it does
not avoid it; conflating that with Gerstgrasser's accumulation would overstate the
rebuttal. Second, Gerstgrasser et al.'s own paper flags a partial counter-example from
prior work (Martínez et al.) where accumulation still degraded a different architecture
quickly. Third, a later theoretical paper (Dohmatob et al., "Strong Model Collapse")
finds that in their regression setting, a synthetic fraction that stays fixed instead of
shrinking still collapses the model asymptotically — a different assumption about how
synthetic share evolves at scale than Gerstgrasser's setup implies, and the two papers
do not engage each other directly, which is itself worth stating plainly rather than
resolving for the reader. The evidence is thinnest on "who presses the worry today":
the strongest primary statement of the remedy (preserve human data, coordinate on
provenance) is in the original paper's own 2024 discussion section, not in a fresh 2026
statement; nothing more recent and equally authoritative turned up in the time
available. phi-1 is confirmed as a primary, on-topic instance of curated synthetic data
improving a model, which is the "live tension" the commission wants, though phi-1 is
about data quality/curation, not about model collapse directly — the paper never
mentions collapse.

## Sources

```text
URL:         https://www.nature.com/articles/s41586-024-07566-y
Kind:        Primary — the study's own report of its own experiments (model collapse
             in LLMs, VAEs, GMMs); owns the collapse claim and the OPT-125m/wikitext2
             results.
Establishes: The definition of model collapse, the early/late distinction, the
             OPT-125m fine-tuning experiment and its perplexity results, the authors'
             own discussion of remedies.
Paraphrase:  Shumailov, Shumaylov, Zhao, Papernot, Anderson and Gal report that
             indiscriminately training generative models on model-generated content
             causes "model collapse": a degenerative process in which later
             generations lose information about the tails of the training
             distribution first (early collapse), then converge toward a
             low-variance distribution that barely resembles the original (late
             collapse). They fine-tune OPT-125m on wikitext2 across nine
             generations, training each new generation on the previous
             generation's own output, and find perplexity against the real
             wikitext2 test set rises substantially when none of the original
             data is kept, and rises much less when 10% of the original data is
             retained at each step. They close by recommending that access to the
             original (human) data source be preserved and that the field
             coordinate on tracking the provenance of LLM-generated content on the
             web.
Locators:    "What is model collapse?" (definition, Definition 2.1); Fig. 1 and
             caption; "Model collapse in language models" and the two following
             sections (experiment description, results, Example 1, Ablation:
             Repetitions); Discussion, final two paragraphs (remedy).
Quote:       "Definition 2.1 (model collapse). Model collapse is a degenerative
             process affecting generations of learned generative models, in which
             the data they generate end up polluting the training set of the next
             generation. Being trained on polluted data, they then mis-perceive
             reality. ... We separate two special cases: early model collapse and
             late model collapse. In early model collapse, the model begins losing
             information about the tails of the distribution; in late model
             collapse, the model converges to a distribution that carries little
             resemblance to the original one, often with substantially reduced
             variance." — "To sustain learning over a long period of time, we need
             to make sure that access to the original data source is preserved and
             that further data not generated by LLMs remain available over time.
             ... One option is community-wide coordination to ensure that
             different parties involved in LLM creation and deployment share the
             information needed to resolve questions of provenance."
```

```text
URL:         https://arxiv.org/abs/2305.17493
Kind:        Primary — the 2023 precursor, same core authorship, owns the earlier
             version of the same experiments and definition.
Establishes: That "model collapse" as a named phenomenon and the OPT-125m/wikitext2
             LLM demonstration predate the Nature publication by over a year;
             records small wording differences from the final published definition.
Paraphrase:  The May 2023 arXiv paper (revised to v3, 14 Apr 2024) is the same
             research programme before Nature peer review: VAE, GMM and LLM
             experiments, the same "early/late model collapse" split, and the same
             OPT-125m fine-tuned-on-wikitext2 generational experiment with example
             outputs drifting toward a list of jackrabbit color-morphs by
             generation 9. The precursor's Definition 3.1 differs slightly in
             wording from the Nature paper's Definition 2.1: it says late collapse
             happens when "the model entangles different modes of the original
             distributions... often with very small variance," where the Nature
             version says "converges to a distribution that carries little
             resemblance to the original one, often with substantially reduced
             variance." The substance is the same; the exact sentence a writer
             quotes should match the paper it cites.
Locators:    Abstract; footnote 1 (name origin, and that "model dementia" was the
             original, later-renamed term); §3 "What is Model Collapse?",
             Definition 3.1; the boxed Example-1 output table (Gen 0, 1, 7, 9).
Quote:       "Definition 3.1 (Model Collapse). Model Collapse is a degenerative
             process affecting generations of learned generative models, where
             generated data end up polluting the training set of the next
             generation of models; being trained on polluted data, they then
             mis-perceive reality. We separate two special cases: early model
             collapse and late model collapse. In early model collapse the model
             begins losing information about the tails of the distribution; in
             the late model collapse model entangles different modes of the
             original distributions and converges to a distribution that carries
             little resemblance to the original one, often with very small
             variance."
```

```text
URL:         https://pmc.ncbi.nlm.nih.gov/articles/PMC11981929/
Kind:        Primary — the journal's official Author Correction to the Nature 2024
             paper, same authors.
Establishes: That a correction to the Nature paper exists (published 21 March
             2025), and exactly what it fixed.
Paraphrase:  The correction fixes a single notational error in the "Theoretical
             intuition" section: the text originally read "we consider αi = γi =
             0" where it should have read "we consider βi = γi = 0." It does not
             touch the empirical results, the definition, or any reported number.
             Worth knowing so the record is not surprised by it, not worth
             building any claim on.
Locators:    Full text of the correction notice (one paragraph).
```

```text
URL:         https://arxiv.org/abs/2404.01413
Kind:        Primary — owns its own accumulation-vs-replacement experiments and
             the linear-model theorem; the commission's central rebuttal source.
Establishes: That accumulating synthetic data alongside real data (rather than
             replacing real data with synthetic data) avoids model collapse,
             empirically across three model families and theoretically in a
             tractable linear-regression setting; states precisely what
             "accumulate" means operationally.
Paraphrase:  Gerstgrasser, Schaeffer, Dey, Rafailov, Pai, Sleight, Hughes, Korbak,
             Agrawal, Gromov, Roberts, Yang, Donoho and Koyejo (Stanford,
             Constellation, U. Maryland, MIT/Sequoia) confirm that replacing the
             original real data with each generation's synthetic data tends
             toward model collapse, matching Shumailov et al., then show that
             accumulating the successive generations of synthetic data alongside
             the original real data avoids it. "Accumulate" here means: at
             iteration n, concatenate the new synthetic dataset generated by
             model n-1 onto the full pool of the original real data plus every
             prior generation's synthetic data, and train model n on that whole
             (growing) pool; "replace" means training model n only on the newest
             synthetic dataset, discarding everything before it, holding total
             dataset size fixed. They test this on causal transformers (GPT-2 9M;
             Llama-2 12M/42M/126M) pretrained on TinyStories, on a GeoDiff
             diffusion model for molecular conformation, and on VAEs on CelebA
             faces, and find replacing degrades all three while accumulating
             holds error roughly flat (LM, VAE) or nearly flat (diffusion) across
             5-9 model-fitting iterations. In an analytically tractable linear
             framework building on Dohmatob et al.'s prior replace-regime result,
             they prove test error grows linearly with the number of iterations
             under replacement, but is bounded by a small constant independent of
             the number of iterations under accumulation, because each
             generation's added noise is diluted by a shrinking 1/i² weight as
             the pool grows. They flag one partial counter-example from the
             literature themselves (see Contradictions).
Locators:    Abstract; §1 Introduction, paragraph beginning "To that end...";
             §2.1 "Transformer-Based Causal Language Modeling" (Experiments,
             Results, Ablations); Fig. 2 and Fig. 3; §3 "Accumulating Data Avoids
             Model Collapse in Linear Models," Theorem 1, Theorem 2 and the
             surrounding discussion (pp. 8-10); §4 Discussion.
Quote:       "We confirm that replacing the original real data by each
             generation's synthetic data does indeed tend towards model collapse,
             then demonstrate that accumulating the successive generations of
             synthetic data alongside the original real data avoids model
             collapse; these results hold across a range of model sizes,
             architectures, and hyperparameters." — "Together, these results
             strongly suggest that the 'curse of recursion' may not be as dire as
             had been portrayed — provided we accumulate synthetic data alongside
             real data, rather than replacing real data by synthetic data only."
```

```text
URL:         https://arxiv.org/abs/2306.11644
Kind:        Primary — Microsoft Research's own report of its own model and
             training run; the commission's source for curated synthetic data
             that helped a model.
Establishes: A documented case where a mix that is mostly filtered-web plus a
             meaningful minority of LLM-synthesized training data produced a
             small model that matched or beat much larger code models on two
             benchmarks. Does not discuss or mention model collapse.
Paraphrase:  Gunasekar et al. (19 authors, Microsoft Research) introduce phi-1, a
             1.3-billion-parameter Transformer for Python code, trained on about
             7B tokens: roughly 6B tokens of "textbook quality" data filtered from
             web sources with a GPT-4-based classifier, plus about 1B tokens of
             textbooks and exercises synthetically generated by GPT-3.5, then
             fine-tuned on under 200M more tokens of textbook-exercise-like data.
             Despite being several orders of magnitude smaller than competing
             models in both parameters and training tokens, phi-1 reaches 50.6%
             pass@1 on HumanEval and 55.5% pass@1 on MBPP, ahead of models roughly
             an order of magnitude and more larger (e.g., StarCoder-Prompted,
             15.5B parameters/1T tokens, at 40.8%/49.5%), though still behind
             GPT-4's reported 67% on HumanEval. The authors' framing is explicitly
             about data quality changing the shape of scaling laws, not about
             synthetic data's safety; they note they omit some synthetic-data
             generation details "for proprietary reasons."
Locators:    Abstract; §1 Introduction, first two paragraphs; Table 1 (model
             comparison).
Quote:       "We introduce phi-1, a new large language model for code, with
             significantly smaller size than competing models: phi-1 is a
             Transformer-based model with 1.3B parameters, trained for 4 days on 8
             A100s, using a selection of 'textbook quality' data from the web (6B
             tokens) and synthetically generated textbooks and exercises with
             GPT-3.5 (1B tokens). Despite this small scale, phi-1 attains pass@1
             accuracy 50.6% on HumanEval and 55.5% on MBPP."
```

```text
URL:         https://arxiv.org/abs/2410.04840
Kind:        Primary — owns its own theoretical result and the language-model
             experiments that verify it.
Establishes: A complicating, later (Oct. 2024) theoretical result: in a
             high-dimensional linear-regression scaling-law setting, model
             collapse persists whenever the synthetic share of the training mix
             stays a fixed, non-vanishing fraction as the dataset grows — it does
             not require replacement, only a synthetic fraction that fails to
             shrink toward zero.
Paraphrase:  Dohmatob, Feng, Subramonian and Kempe (Meta AI/FAIR, NYU, UCLA)
             study supervised regression with a mixture of real and
             model-generated ("synthetic") training points and show that even a
             very small fixed fraction of synthetic data (their example: 1%)
             causes the scaling law to plateau: adding more data no longer
             improves test error once that fraction is fixed and non-vanishing.
             Larger models can worsen this in a tractable "random projections"
             approximation of a neural network, though beyond an (often very
             high) interpolation threshold, larger models can partially — not
             fully — offset it. The theoretical claims are checked empirically on
             language models and feed-forward image models. The abstract does not
             engage with or cite Gerstgrasser et al.'s accumulation result;
             the setups differ in an assumption that matters (see
             Contradictions).
Locators:    Abstract; Corollary 1 discussion (isotropic case: "the scaling law
             plateaus unless p2 → 0+"); §on model size and the interpolation
             threshold.
Quote:       "Within the scaling laws paradigm, which underpins the training of
             large neural networks like ChatGPT and Llama, we consider a
             supervised regression setting and establish the existence of a
             strong form of the model collapse phenomenon, a critical performance
             degradation due to synthetic data in the training corpus. Our
             results show that even the smallest fraction of synthetic data
             (e.g., as little as 1% of the total training dataset) can still
             lead to model collapse: larger and larger training sets do not
             enhance performance."
```

```text
URL:         https://arxiv.org/abs/2503.03150
Kind:        Primary — a position paper stating its own argument and evidence
             review, not a report on someone else's claim.
Establishes: The most articulate primary statement of the dismissive/skeptical
             reading available in this record: that "model collapse" research
             uses inconsistent definitions and that some of its most-cited
             scenarios rest on assumptions that do not match real deployment.
Paraphrase:  Schaeffer, Kazdan, Arulandu and Koyejo (submitted 5 Mar 2025) argue
             that research on model collapse spans at least eight distinct, at
             times conflicting, definitions of the term, which has made it hard
             to build a shared understanding of what is and is not shown. They
             argue certain predicted collapse scenarios rely on assumptions that
             poorly match real-world training conditions and that several
             prominent collapse scenarios are, in their reading, readily
             avoidable in practice. They argue this has drawn attention away from
             other, more immediately-plausible harms of the current trajectory of
             AI development. This is a direct, named challenge to how far the
             replacement-regime demonstrations should be read as predictive of
             real training pipelines — precisely the line the commission asks the
             piece to draw.
Locators:    Abstract.
```

```text
URL:         https://www.cs.ox.ac.uk/news/2356-full.html
Kind:        Secondary — University of Oxford Department of Computer Science's
             own press release about its faculty's paper; institutional
             reporting on the study, not the study itself. Carries one
             first-person quote from a co-author, which is primary for that
             sentence only.
Establishes: That the study's authors themselves, at publication, characterized
             the finding as significant and pointed to preserving human data and
             tracking provenance as the response — corroborating (not
             independently confirming) what the paper's own Discussion already
             says.
Paraphrase:  Published to coincide with the 25 July 2024 Nature publication, the
             piece quotes co-author Yarin Gal (Associate Professor, Oxford)
             directly, and reports the recommendation to preserve access to
             human-created data and establish clearer data provenance tracking.
             It attributes no claim to Gal that is not consistent with the paper
             itself.
Locators:    Full page (single press release).
Quote:       "Model collapse is the AI equivalent of a feedback loop gone wrong.
             The more models feed on their own output, the further they drift
             from reality. Model collapse threatens to create an AI echo
             chamber." — attributed to Yarin Gal.
```

```text
URL:         https://techxplore.com/news/2024-07-ai-collapse-llms.html
Kind:        Secondary — independent science-journalism outlet reporting on the
             Nature paper from outside the authoring team.
Establishes: Independent confirmation that the paper's headline finding and the
             filtering/human-data remedy were reported the same way by a party
             with no stake in the result.
Paraphrase:  Published 25 July 2024, the piece reports the OPT-125m generational
             drift example (architecture text degrading toward a list of
             jackrabbit color-morphs by the ninth generation) and paraphrases the
             authors as saying training on AI-generated data is not inherently
             impossible but that "the filtering of that data must be taken
             seriously," and that companies retaining access to human-generated
             content may hold a structural advantage. Contains no quote beyond
             that paraphrase.
Locators:    Full article (single news piece).
```

## Contradictions

- **Partial retention is not accumulation, and only slows collapse — it does not
  avoid it.** Shumailov et al.'s own "10% of original data preserved" condition
  keeps a small, fixed slice of the original real data at every generation and
  still shows perplexity rising over generations, just "only minor degradation"
  rather than the sharp rise seen with zero retention. This is a different
  operation from Gerstgrasser et al.'s "accumulate," which keeps the *entire*
  growing history of real and synthetic data, not a fixed 10% slice. A piece that
  states the demonstrated/extrapolated line needs to keep these three regimes
  (replace; fixed partial retention; full accumulation) distinct — collapsing the
  second into the third would overstate how easily the "curse" is broken.

- **The accumulation rebuttal names its own exception.** Gerstgrasser et al.
  write, of their own accumulation result: "we also note that Martínez et al.
  (2023a) found slightly contradictory evidence, specifically that a different
  architecture on a much smaller dataset exhibits fast performance deterioration
  even with accumulating data." They call understanding why "an interesting
  direction... for future research," not a solved question. (Read only in
  Gerstgrasser et al.'s own citation of it; the Martínez paper itself was not
  independently opened for this record and should not be cited beyond this
  attributed mention.)

- **A later theoretical result complicates, but does not straightforwardly
  refute, the accumulation finding.** Dohmatob et al. ("Strong Model Collapse,"
  Oct. 2024, five months after Gerstgrasser) show that in their regression
  setting, collapse persists whenever the synthetic share of the training mix is
  a fixed, non-vanishing fraction, even while the dataset keeps growing. This
  sounds like it targets accumulation directly, but the two papers make different
  assumptions about how the synthetic fraction evolves as more data arrives.
  Gerstgrasser et al.'s own theorem shows the *effective weight* of each
  generation's synthetic contribution shrinking as 1/i² under their specific
  accumulation scheme (new data added in equal-size chunks to an ever-larger
  pool) — i.e., their setup has the synthetic share falling over time, which is
  exactly the condition Dohmatob et al.'s result exempts from collapse ("unless
  p2 → 0+"). The two papers do not cite or engage each other on this point in the
  passages read for this record. This is a live, unresolved tension between two
  primary theoretical treatments, not a settled disagreement — the honest framing
  is "these two results are not obviously compatible or incompatible," not
  "accumulation is refuted."

- **A named, primary dismissive reading exists and should be steelmanned.**
  Schaeffer et al. argue the model-collapse literature is definitionally
  fragmented (they count at least eight distinct definitions in use) and that
  several prominent collapse scenarios "poorly match real-world conditions." This
  is a primary challenge to treating any single replacement-regime demonstration
  as predictive of internet-scale training, independent of the
  accumulation-vs-replacement question.

- **No contradiction found on the core demonstrated result.** No source read for
  this record disputes that full replacement collapses models in the settings
  Shumailov et al. and Gerstgrasser et al. both tested; the disagreement is about
  what that does and doesn't imply beyond those settings.

## Numbers

```text
Figure: 115 perplexity (zero-shot baseline) and 34 mean perplexity (fine-tuned on
        real wikitext2)
Owner:  Shumailov et al., Nature 2024
Scope:  OPT-125m causal language model, wikitext2 test set, "generation 0" (real
        data only), five independent runs
```

```text
Figure: perplexity rises by "20 to 28 perplexity points" over generations 1-9
        when no original data is preserved (five epochs)
Owner:  Shumailov et al., Nature 2024, Fig. 1b and accompanying text
Scope:  OPT-125m/wikitext2, full replacement each generation, five independent
        runs; read from the paper's own stated range, not re-derived from the
        chart
```

```text
Figure: "only minor degradation of performance" over generations 1-9 when 10% of
        original data is preserved (ten epochs)
Owner:  Shumailov et al., Nature 2024, Fig. 1c and accompanying text
Scope:  OPT-125m/wikitext2, fixed 10% original-data retention each generation,
        five independent runs; this is not the same operation as Gerstgrasser et
        al.'s "accumulate" (see Contradictions)
```

```text
Figure: enforcing a non-repeating penalty "causes the perplexity to double
        compared with the original"
Owner:  Shumailov et al., Nature 2024, "Ablation: Repetitions"
Scope:  Same LLM experiments, ablation condition only
```

```text
Figure: E_test(replace) = (sigma^2 * d / (T - d - 1)) * n  — grows linearly in
        the number of iterations n
Owner:  Gerstgrasser et al. 2024 (Theorem/Eq. 4, attributed to Dohmatob et al.
        2024a's prior result), extended by Gerstgrasser et al.
Scope:  Tractable linear-regression model-collapse framework; sigma^2 = label
        noise variance, d = input dimension, T = samples per iteration
```

```text
Figure: E_test(accumulate) <= (sigma^2 * d / (T - d - 1)) * (pi^2 / 6) — bounded
        by a constant, independent of n
Owner:  Gerstgrasser et al. 2024, Theorem 2 / Eq. 3
Scope:  Same linear-regression framework, accumulation condition
```

```text
Figure: cross-entropy test loss rises across 5 model-fitting iterations under
        "replace" (roughly 1.75-2.1 up to roughly 2.4-2.85, read from the chart,
        not a reported table) and stays roughly flat or falls slightly under
        "accumulate" (roughly 1.75-2.1 down toward roughly 1.6-1.85)
Owner:  Gerstgrasser et al. 2024, Fig. 2
Scope:  GPT-2 (9M) and Llama-2 (12M/42M/126M) pretrained on TinyStories,
        temperature = 1.0 sampling, five model-fitting iterations; approximate
        chart readings, preserve the figure itself for the writer rather than
        precise digits
```

```text
Figure: even a 1% synthetic-data fraction causes the scaling law to "plateau" —
        larger training sets stop improving performance
Owner:  Dohmatob et al. 2024 ("Strong Model Collapse"), abstract and Corollary 1
Scope:  High-dimensional linear regression / random-projection approximation of
        a neural network; verified empirically on language models and
        feed-forward image models in the same paper
```

```text
Figure: phi-1: 1.3B parameters, ~7B training tokens (6B web-filtered + 1B
        GPT-3.5-synthesized), 50.6% pass@1 HumanEval, 55.5% pass@1 MBPP
Owner:  Gunasekar et al. 2023 ("Textbooks Are All You Need"), Abstract and
        Table 1
Scope:  Single model, self-reported scores, compared in the same table against
        StarCoder-Prompted (15.5B params/1T tokens, 40.8%/49.5%) and GPT-4
        (67% HumanEval, no MBPP figure given)
```

## Source assets

```text
Asset: Fig. 1 (Shumailov et al., Nature 2024) — three-part figure: (a) the
       feedback-loop diagram ("Data0 -> Model0 -> Data1 -> Model1..." with the
       "probable events overestimated / improbable events underestimated" /
       "tails shrink over time" annotations); (b)-(c) side-by-side histograms of
       generated-data perplexity by generation, and line charts of test
       perplexity by generation, for the no-retention and 10%-retention
       conditions.
Shows: The mechanism (feedback loop) and the result (perplexity drift, tail
       thinning) in one image; the (b) vs (c) pairing is the paper's own visual
       argument for "some retained real data helps, but the LLM curve still
       climbs."
Crop:  Keep panel (a)'s loop diagram and at least one of the two perplexity line
       charts (b or c) together — the diagram explains what the line chart is
       measuring. Do not crop out the axis labels or the "Real" starting point on
       the line charts; that anchor is what makes the drift legible.
```

```text
Asset: Fig. 2 (Gerstgrasser et al. 2024) — "Replace Data" vs "Accumulate Data"
       schematic (top) paired directly with matching cross-entropy-by-iteration
       line charts (bottom), for four model architectures at once.
Shows: The single clearest visual statement of the commission's central
       distinction: same models, same task, only the data-handling rule differs,
       and the two outcomes diverge sharply.
Crop:  Keep the schematic and the chart together — the schematic is what makes
       "replace" vs "accumulate" concrete rather than abstract. If cropping to
       one pair, keep the legend identifying the four model architectures.
```

```text
Asset: Fig. 7 (Gerstgrasser et al. 2024) — the linear-regression numerical
       simulation, "Replace" (top) vs "Accumulate" (bottom), with theoretical
       prediction overlaid on numerical results, at three different per-iteration
       sample sizes T.
Shows: That the empirical LM/VAE/diffusion result and the closed-form theorem are
       the same phenomenon, not two separate claims — theory line and simulated
       points overlap.
Crop:  If used, keep at least one full column (one value of T) with both the
       "Replace" and "Accumulate" rows, so the reader sees the same iteration
       axis produce a diverging line versus a plateauing one.
```

```text
Asset: Table 1 (Gunasekar et al. 2023) — chronological table of code models by
       date, parameter count, training-token count, and HumanEval/MBPP pass@1.
Shows: phi-1's position at the bottom of the table next to StarCoder-Prompted
       (15.5B, ~12x phi-1's parameter count) and GPT-4, making the
       small-model/high-score claim checkable at a glance rather than asserted.
Crop:  If cropped, keep phi-1's row plus at least the two or three rows nearest
       it in score, and the column headers; dropping the header row turns the
       numbers back into unlabeled data.
```

## Discarded

```text
URL: https://www.nature.com/articles/d41586-024-03023-y — Nature News & Views
     piece "AI model collapse might be prevented by studying human language
     transmission" (Smith, Kirby, Guo & Griffiths, 17 Sept 2024). Fetch attempts
     resolved only the title and citation line; the article body did not load
     through any route tried (gated the same way as the two nature.com articles
     above, without an open-access mirror found). Not cited because the body was
     never read — bibliographic existence only, not its claims.
```

```text
URL: https://arxiv.org/abs/2601.09966 — "A Sustainable AI Economy Needs Data
     Deals That Work for Generators" (Jia, Oala, Xiong, Ge, Wang, Kang, Song;
     NeurIPS 2025 Position Paper Track, posted 16 Jan 2026). Opened and read the
     abstract and introduction. Rejected as a cited source for this record: its
     subject is economic inequity in data-licensing deals (missing provenance,
     bargaining power, price discovery) between data generators and model
     companies, not the mechanism of model collapse. It mentions the AI
     "feedback loop" only in passing as motivation and never analyzes tails,
     replacement, or accumulation. Using it here would be padding on the
     provenance keyword rather than evidence on the commissioned question.
```

## For the writer: neighbor slugs to link

Confirmed via `./nb history --library /home/user/library-checkout`:

```text
what-could-go-wrong/data-poisoning · "Poisoning's two strongest results were
  never run in the same experiment" — deliberate corruption of training data,
  the natural contrast to model collapse's accidental/systemic corruption.

the-mechanics/memorization · "A verbatim quote comes out of the weights, not a
  lookup" — how specific training sequences get pressed into weights; useful
  background for why losing distributional tails matters.

the-evidence/textbooks-are-all-you-need · "phi-1 matched code models 12x its
  size, but mostly on problems like its training set" — this library's own
  existing treatment of the phi-1 curated-synthetic-data case; do not re-teach
  phi-1's numbers in the new piece beyond what's needed, link instead.
```
