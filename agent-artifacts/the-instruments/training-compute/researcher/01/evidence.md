# Evidence: the-instruments/training-compute (01)

The record supports the commission's core lesson firsthand. The two regulatory
thresholds are verified word-for-word in the owning legal texts: the EU AI Act
sets a presumption of systemic risk at training compute greater than 10^25 FLOP
(Article 51(2), Regulation (EU) 2024/1689), and US EO 14110 set reporting
triggers at 10^26 operations for AI models and 10^23 for models trained
primarily on biological sequence data (Section 4.2(b)(i)); EO 14110 was revoked
on 20 January 2025 by EO 14148, so its reporting trigger is no longer in force
as an executive requirement. The C = 6ND relation is verified in Kaplan et al.
2020 (which derives C ≈ 6N per token) and in Hoffmann et al. 2022 (Chinchilla),
which explicitly names "the common approximation C = 6DN (Kaplan et al., 2020)"
and shows it agrees with an exact operation count. Model-FLOPs-utilization (MFU)
is defined and measured in the PaLM paper (46.2%) and the Llama 3 paper (38-43%
BF16 MFU), bracketing the ~30-50% real-world range. The cleanest documentary
case is Llama 3.1 405B, whose disclosed 3.8×10^25 FLOP sits above the EU line
and below the EO line, and whose disclosed parameter and token counts reproduce
that figure via 6ND to two significant figures. The estimate-treated-as-fact
case is GPT-4, whose ~2.1×10^25 FLOP is an Epoch estimate, never disclosed by
OpenAI. The record's thinnest point is provenance transport, not content: the
two owning legal texts (EUR-Lex, Federal Register) are bot-gated to automated
fetches (HTTP 202 / proxy redirect), so their exact wording was read from
official mirrors (govinfo PDF for the EO; a verbatim reproduction for the EU
Act). The evidence does not undermine the commissioned angle; it confirms it.

## Sources

```text
URL:         https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
Kind:        primary — the EU AI Act itself (Regulation (EU) 2024/1689),
             Official Journal. It owns the 10^25 FLOP threshold.
Establishes: The systemic-risk classification and the 10^25 FLOP presumption.
Paraphrase:  Article 51(1): a general-purpose AI (GPAI) model is classified as
             one with systemic risk if it has high-impact capabilities, or a
             Commission decision finds equivalent capability per Annex XIII.
             Article 51(2): a GPAI model is *presumed* to have high-impact
             capabilities when the cumulative amount of computation used for its
             training, measured in floating point operations, is greater than
             10^25. Article 51(3): the Commission may amend the thresholds by
             delegated act. Recital 111 gives the rationale: cumulative training
             compute in FLOP is "one of the relevant approximations for model
             capabilities," so an initial threshold is set, to be adjusted over
             time for algorithmic and hardware progress. Article 3(67) defines a
             "floating-point operation" as any mathematical operation or
             assignment involving floating-point numbers.
Locators:    Article 51(1)-(3); Recital 111; Article 3(67).
Quote:       "A general-purpose AI model shall be presumed to have high impact
             capabilities ... when the cumulative amount of computation used for
             its training measured in floating point operations is greater than
             10^25."
Note:        EUR-Lex returns HTTP 202 with an empty body to automated fetches
             (bot challenge); it resolves normally in a browser. Exact wording
             above was verified against the verbatim reproduction at
             https://artificialintelligenceact.eu/article/51/ ,
             https://artificialintelligenceact.eu/recital/111/ , and
             https://artificialintelligenceact.eu/article/3/ (Future of Life
             Institute mirror), which matched the Official-Journal text.
```

```text
URL:         https://www.govinfo.gov/content/pkg/FR-2023-11-01/pdf/2023-24283.pdf
Kind:        primary — Executive Order 14110 as published in the Federal
             Register (88 FR 75191), the official government text.
Establishes: The US reporting thresholds in FLOP and the biological-model figure.
Paraphrase:  Section 4.2(b)(i): until technical conditions are defined, the
             Secretary of Commerce shall require reporting for any model trained
             using more than 10^26 integer or floating-point operations, or,
             for a model trained primarily on biological sequence data, more
             than 10^23 integer or floating-point operations. Section
             4.2(b)(ii): any computing cluster with machines in a single
             datacenter connected at over 100 Gbit/s and a theoretical maximum
             capacity of 10^20 operations per second for training AI. These are
             interim triggers, not a definition of capability.
Locators:    Section 4.2(b)(i) and 4.2(b)(ii); definition of "dual-use
             foundation model" at Section 3(k).
Quote:       "any model that was trained using a quantity of computing power
             greater than 10^26 integer or floating-point operations, or using
             primarily biological sequence data and using a quantity of
             computing power greater than 10^23 integer or floating-point
             operations".
Note:        federalregister.gov redirects automated fetches to a proxy host;
             the govinfo PDF above is the official primary and resolves cleanly.
```

```text
URL:         https://www.presidency.ucsb.edu/documents/executive-order-14148-initial-rescissions-harmful-executive-orders-and-actions
Kind:        primary content (text of EO 14148), hosted by the American
             Presidency Project archive.
Establishes: EO 14110's revocation and its date.
Paraphrase:  EO 14148, signed 20 January 2025, revokes a list of prior orders;
             entry (ggg) is EO 14110 of October 30, 2023 (Safe, Secure, and
             Trustworthy Development and Use of Artificial Intelligence). So the
             10^26 reporting trigger is no longer an active executive requirement
             after that date.
Locators:    Section 2, list entry (ggg).
Quote:       "Executive Order 14110 of October 30, 2023 (Safe, Secure, and
             Trustworthy Development and Use of Artificial Intelligence)."
```

```text
URL:         https://arxiv.org/abs/2001.08361
Kind:        primary — Kaplan et al. 2020, "Scaling Laws for Neural Language
             Models" (OpenAI/Johns Hopkins). It owns the 6ND compute estimate.
Establishes: The provenance and derivation of C ≈ 6ND.
Paraphrase:  N is the number of non-embedding parameters. A forward pass costs
             about 2N add-multiply operations per token (Table 1; the factor 2
             is the multiply-accumulate). The backward pass is about twice the
             forward pass, so the estimated non-embedding compute is C ≈ 6N
             floating-point operations per training token (Section 2.1). Over D
             tokens this is C = 6NBS = 6ND. The paper flags this as an estimate
             that omits context-dependent terms.
Locators:    Section 2.1 (Eq. 2.2 and the sentence defining C ≈ 6N per token);
             Table 1; Section 3 ("the factor of 6 accounts for the forward and
             backward passes").
Quote:       "Accounting for the backwards pass (approximately twice the compute
             as the forwards pass), we then define the estimated non-embedding
             compute as C ≈ 6N floating point operators per training token."
```

```text
URL:         https://arxiv.org/abs/2203.15556
Kind:        primary — Hoffmann et al. 2022, "Training Compute-Optimal Large
             Language Models" (Chinchilla, DeepMind). Cited as a *user* of 6ND.
Establishes: That the field uses C = 6ND and that it matches an exact count.
Paraphrase:  Appendix F counts FLOPs from the architecture using a factor of 2
             for multiply-accumulate and, "As in Kaplan et al. (2020)," a
             backward pass of twice the forward pass. The paper compares this
             exact count with "the common approximation C = 6DN (Kaplan et al.,
             2020)" in Table A4 and finds the differences "very small," not
             affecting its analysis. It attributes the approximation explicitly
             to Kaplan et al. 2020.
Locators:    Appendix F (FLOP counting) and Table A4; Section 1 cites Kaplan et
             al. 2020 for the parameter-performance power law.
Quote:       "We show a comparison between our calculation and that using the
             common approximation C = 6DN (Kaplan et al., 2020) where C is
             FLOPs, D is the number of training tokens, and N is the number of
             parameters ... We find the differences in FLOP calculation to be
             very small."
```

```text
URL:         https://arxiv.org/abs/2204.02311
Kind:        primary — Chowdhery et al. 2022, "PaLM: Scaling Language Modeling
             with Pathways" (Google). A training-systems primary that defines
             and reports MFU.
Establishes: The definition of model FLOPs utilization and a real MFU figure.
Paraphrase:  MFU is the ratio of observed throughput (tokens per second) to the
             theoretical maximum throughput of a system running at peak FLOP/s;
             it is implementation-independent, unlike hardware FLOPs utilization.
             Training PaLM 540B on 6144 TPU v4 chips achieved 46.2% MFU and
             57.8% hardware FLOPs utilization — high for the field, and reached
             only after specific compiler and parallelism optimizations.
Locators:    Section 1 (summary of 46.2% MFU / 57.8% HFU); Section 4 and the MFU
             definition paragraph.
Quote:       "model FLOPs utilization (MFU). This is the ratio of the observed
             throughput (tokens-per-second) relative to the theoretical maximum
             throughput of a system operating at peak FLOPs."
```

```text
URL:         https://arxiv.org/abs/2407.21783
Kind:        primary — Llama 3 team (Meta) 2024, "The Llama 3 Herd of Models".
             The lab's own disclosure of a real training-FLOP figure.
Establishes: A disclosed FLOP number, and a real MFU in the 30-50% band; the
             clean case that sits against both regulatory lines.
Paraphrase:  The flagship model (Llama 3.1 405B) is a dense transformer with
             405B parameters, pre-trained on 15.6T text tokens using 3.8×10^25
             FLOPs, "almost 50x more than the largest version of Llama 2." Table
             4 reports BF16 MFU of 43%, 41%, and 38% across three pre-training
             stages (430, 400, 380 TFLOP/s per GPU). Worked check: 6 × 405×10^9
             × 15.6×10^12 = 3.79×10^25, which reproduces the disclosed 3.8×10^25
             to two significant figures. Regulatory position: 3.8×10^25 is above
             the EU 10^25 systemic-risk line (~3.8x) and below the EO 10^26
             reporting line (~0.38x).
Locators:    Section 1 (Scale bullet: 3.8×10^25 FLOPs, 405B params, 15.6T
             tokens); Table 4 (per-stage BF16 MFU).
Quote:       "our flagship language model was pre-trained using 3.8 × 10^25
             FLOPs, almost 50x more than the largest version of Llama 2 ...
             pre-trained a flagship model with 405B trainable parameters on
             15.6T text tokens."
```

```text
URL:         https://epoch.ai/blog/estimating-training-compute
Kind:        primary — Epoch AI's own methodology writeup. Epoch owns its
             estimation procedure.
Establishes: The two estimation methods and their stated uncertainty.
Paraphrase:  Method 1 (counting operations): training_compute =
             ops_per_forward_pass × 3 × n_epochs × n_examples, where the 3 is the
             forward pass plus a 2:1 backward-to-forward ratio — the same factor
             behind 6ND. Epoch calls this a heuristic that "can be off depending
             on the exact architecture." Method 2 (hardware): training time ×
             number of cores × peak FLOP/s × utilization rate. Epoch assumes a
             utilization rate of 0.3 for large language models and 0.4 for other
             networks, and notes observed rates from 25% to 56%. When both
             methods are computable they "differ by no more than a factor of 1.7."
Locators:    "Method 1 / Method 2" sections; utilization-assumption and
             cross-check paragraphs.
Quote:       "0.3 for large language models, and a utilization rate of 0.4 for
             other networks"; the two methods "differ by no more than a factor
             of 1.7."
```

```text
URL:         https://arxiv.org/abs/2202.05924
Kind:        primary — Sevilla, Heim, Ho, Besiroglu, Hobbhahn, Villalobos 2022,
             "Compute Trends Across Three Eras of Machine Learning" (Epoch). The
             foundational paper behind Epoch's compute database.
Establishes: The estimation lineage and the wide error bars on older estimates.
Paraphrase:  Two methods are used to estimate training compute: counting
             operations from architecture, and estimating from hardware,
             training time, and a utilization rate. For the hardware method on
             older models with undisclosed details, the paper assumes a 10% GPU
             utilization rate and infers the GPU from publication year — a source
             of large uncertainty. Only the final training run is counted, not
             the experimentation that preceded it. Training compute has doubled
             roughly every 6 months since the early-2010s deep-learning era.
Locators:    Methodology / appendix on compute estimation; the two-method
             description and utilization assumptions.
Quote:       (methodology) estimates rest on "assumptions about ... utilization"
             and, for the GPU-time method on older models, a 10% utilization
             assumption.
```

```text
URL:         https://epoch.ai/data-insights/models-over-1e25-flop
Kind:        secondary — Epoch AI reporting on models it did not build; a
             third-party estimate, not a lab disclosure.
Establishes: The estimate-treated-as-fact case (GPT-4) and how many models
             cross the EU line.
Paraphrase:  As of June 2025, Epoch identified 33 publicly announced models from
             12 developers estimated to exceed the 10^25 FLOP EU threshold.
             GPT-4's training compute is given as approximately 2.1×10^25 FLOP —
             Epoch's own estimate from inferred training hardware and duration,
             not disclosed by OpenAI. The figure circulates widely as if it were
             a reported number.
Locators:    Headline count ("over 30 ... over the 10^25 FLOP ... threshold");
             GPT-4 entry ("Compute estimated using training hardware and training
             duration").
Quote:       "As of June 2025, we have identified over 30 publicly announced AI
             models from 12 different AI developers that we believe to be over
             the 10^25 FLOP training compute threshold."
```

```text
URL:         https://arxiv.org/abs/2407.05694
Kind:        secondary (commentary on the law) / primary for its own argument —
             Sara Hooker (Cohere) 2024, "On the Limitations of Compute
             Thresholds as a Governance Strategy." The against side of the debate.
Establishes: The case that a FLOP threshold is a poor risk proxy.
Paraphrase:  Hooker argues that compute thresholds "as currently implemented,
             are shortsighted and likely to fail to mitigate risk," because the
             relationship between compute and risk is highly uncertain and
             rapidly changing, and because thresholds overestimate our ability to
             predict which capabilities emerge at a given scale. Algorithmic
             progress lets smaller models match larger ones, decoupling
             capability from raw FLOP. She names both EO 14110 and the EU AI Act
             as adopting the approach. Affiliation (Cohere) confirmed via the
             companion policy primer at cohere.com; not stated in the abstract.
Locators:    Abstract; the section arguing compute-capability decoupling.
Quote:       compute thresholds "are shortsighted and likely to fail to mitigate
             risk."
```

```text
URL:         https://arxiv.org/abs/2405.10799
Kind:        secondary (analysis of the regulation) / primary for its own
             argument — Lennart Heim and Leonie Koessler 2024, "Training Compute
             Thresholds: Features and Functions in AI Regulation." The for side.
Establishes: The steelman defense of compute thresholds.
Paraphrase:  The authors argue training compute is "the most suitable metric" to
             flag GPAI models for oversight because it correlates with
             capabilities and risk, is quantifiable and knowable early in a
             model's lifecycle, and is externally verifiable. They concede that
             "training compute is an imperfect proxy for risk" and recommend it
             be used as an initial filter within a broader framework — paired
             with notification, model evaluations, and risk assessments — not in
             isolation. Author affiliations are not shown in the fetched abstract.
Locators:    Abstract; the strengths-and-limitations discussion.
Quote:       "training compute is an imperfect proxy for risk"; it is
             nonetheless described as an effective initial filter that is
             "quantifiable" and "measurable" early and "verifiable" externally.
```

## Contradictions

The record's central disagreement is whether a training-FLOP threshold is a
sound proxy for risk, and the two sides are both cited above.

- Against (Hooker, arxiv 2407.05694): the compute-to-risk relationship is
  uncertain and moving; algorithmic progress and better data let smaller,
  cheaper models reach the capabilities of larger ones, so a fixed FLOP line
  will misclassify systems in both directions, and thresholds overstate how well
  scale predicts which capabilities appear.
- For (Heim and Koessler, arxiv 2405.10799): no better early-warning metric
  exists — compute is measurable before a model is deployed, correlates with
  capability and risk, and is externally verifiable — but only as an initial
  filter inside a broader regime, and they explicitly grant it is "an imperfect
  proxy for risk."

The regulators encode both positions. The EU AI Act makes 10^25 FLOP a
*rebuttable presumption* (Article 51(2)) rather than a hard line, and Recital 111
calls compute only "one of the relevant approximations for model capabilities,"
to be revised over time — an acknowledgment inside the law that the proxy is
imperfect. This is the disagreement the commission asked to be filled, and it is
genuine, not manufactured.

A second, smaller tension: the commission's framing that the headline number is
"almost never measured" is correct for undisclosed models (GPT-4 circulates only
as Epoch's ~2.1×10^25 estimate), but Llama 3.1 405B is a counter-case where the
lab disclosed 3.8×10^25 FLOP directly. The honest lesson is that disclosure is
the exception, and even a disclosed figure is an accounting estimate (6ND or a
hardware count), not a metered quantity.

## Numbers

```text
Figure: 10^25 FLOP — EU AI Act systemic-risk presumption
Owner:  Regulation (EU) 2024/1689, Article 51(2)
Scope:  Cumulative computation used for training a general-purpose AI model,
        measured in floating point operations; rebuttable presumption.
```
```text
Figure: 10^26 integer or floating-point operations — US reporting trigger
Owner:  EO 14110, Section 4.2(b)(i)
Scope:  Total training compute for any model; interim trigger, revoked
        2025-01-20 by EO 14148.
```
```text
Figure: 10^23 integer or floating-point operations — biological-model trigger
Owner:  EO 14110, Section 4.2(b)(i)
Scope:  Training compute for a model trained primarily on biological sequence
        data; interim trigger, revoked with EO 14110.
```
```text
Figure: 10^20 operations per second — computing-cluster trigger
Owner:  EO 14110, Section 4.2(b)(ii)
Scope:  Theoretical maximum capacity of a co-located cluster (>100 Gbit/s
        interconnect) for training AI.
```
```text
Figure: C ≈ 6N FLOP per training token; total C = 6ND
Owner:  Kaplan et al. 2020, Section 2.1 (used in Hoffmann et al. 2022, Table A4)
Scope:  Dense transformers; N = non-embedding parameters, D = training tokens;
        6 = 2 (multiply-accumulate, forward) × 3 (backward ≈ 2× forward).
```
```text
Figure: 46.2% model FLOPs utilization (57.8% hardware FLOPs utilization)
Owner:  Chowdhery et al. 2022 (PaLM 540B), Section 1
Scope:  6144 TPU v4 chips; high-end, after optimization.
```
```text
Figure: 38%–43% BF16 model FLOPs utilization (380–430 TFLOP/s per GPU)
Owner:  Llama 3 team 2024, Table 4
Scope:  Three pre-training stages of Llama 3.1 405B on H100 GPUs.
```
```text
Figure: Epoch utilization assumptions 0.3 (LLMs) / 0.4 (other); observed 25%-56%
Owner:  Epoch AI, "Estimating training compute"
Scope:  Default utilization for the hardware method; the two methods agree
        within a factor of 1.7 when both are computable.
```
```text
Figure: 3.8×10^25 FLOP — disclosed training compute of Llama 3.1 405B
Owner:  Llama 3 team 2024, Section 1
Scope:  405B parameters, 15.6T tokens; above EU line, below EO line. 6ND check:
        6 × 405e9 × 15.6e12 = 3.79×10^25.
```
```text
Figure: ~2.1×10^25 FLOP — GPT-4 training compute (estimate, not disclosed)
Owner:  Epoch AI (third-party estimate from inferred hardware and duration)
Scope:  Above the EU 10^25 line; OpenAI has not published the figure.
```
```text
Figure: 33 models above 10^25 FLOP (as of June 2025)
Owner:  Epoch AI, "models over 1e25 FLOP"
Scope:  Publicly announced models from 12 developers; mostly Epoch estimates.
```

## Source assets

```text
Asset: Hoffmann et al. 2022 (Chinchilla), Table A4 — exact FLOP count vs the
       C = 6DN approximation, side by side.
Shows: That the analytic 6ND rule and a detailed operation count agree closely,
       so the "estimate" is a disciplined one for dense transformers.
Crop:  Keep both columns and the parameter/token axis; omit surrounding prose.
```
```text
Asset: Llama 3 2024, Table 4 — per-stage BF16 MFU (43%, 41%, 38%) and
       TFLOP/s per GPU (430, 400, 380).
Shows: Real utilization on a frontier run lands well below the hardware peak,
       which is why the hardware method needs an MFU assumption.
Crop:  Retain the MFU and TFLOP/s columns with stage labels; the parallelism
       columns (TP/CP/PP/DP) can be dropped for a lay reader.
```
```text
Asset: Kaplan et al. 2020, Table 1 — parameter and forward-pass compute counts
       (C_forward = 2N).
Shows: Where the factor of 2 (and thus 6) originates: multiply-accumulate in the
       forward pass, doubled for the backward pass.
Crop:  Keep the Total (Non-Embedding) row and the C_forward = 2N line.
```
```text
Asset: Epoch AI "models over 1e25 FLOP" — the chart/list of 33 models above the
       EU threshold.
Shows: How many current systems already cross the EU line, and that most entries
       are estimates rather than disclosures.
Crop:  Keep the threshold line and the model markers; a caption must note the
       figures are Epoch estimates.
```
```text
Asset: EO 14110, Section 4.2(b)(i)-(ii) — the threshold paragraph itself.
Shows: The exact statutory wording tying a capability class to a FLOP count.
Crop:  Quote the two clauses; no image needed.
```

## Discarded

```text
URL: https://en.wikipedia.org/wiki/Executive_Order_14110 — secondary; used only
     to locate the revocation date, then replaced by primary EO 14148 text and
     the govinfo EO 14110 PDF. Not cited as evidence.
URL: https://artificialintelligenceact.eu/article/51/ (and /recital/111/, /article/3/)
     — Future of Life Institute reproduction; faithful and used to verify exact
     EU wording, but the owning primary (EUR-Lex) is recorded instead. Kept as a
     verification aid, not the citation of record.
URL: https://cohere.com/research/papers/The-Limits-of-Thresholds.pdf — Cohere
     policy primer version of Hooker's argument; used only to confirm her
     affiliation. The arXiv paper is the source of record.
URL: https://arxiv.org/pdf/2502.00003 ("Defending Compute Thresholds Against
     Legal Loopholes") — on-topic but narrower (loophole engineering); not
     needed once Heim/Koessler carried the for side.
```
