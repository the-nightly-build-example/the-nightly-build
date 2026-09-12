# Evidence record: the-mechanics/lost-in-the-middle (01)

The evidence supports the commissioned behavior firmly. Liu et al. (2023), the
governing primary, measured a U-shaped accuracy curve by position of the relevant
document on two tasks, found it in extended-context models, and showed the worst
(middle) case can fall below answering with no documents at all. Its numbers are
verified here against the paper's own tables. The claim that a larger context
window does not fix the effect is directly supported: within a shared window an
extended model's curve is nearly superimposed on the base model's. The mechanism
is where the evidence is genuinely open, and the primaries disagree in emphasis
rather than in fact. Liu's own analysis rules out instruction tuning as the
necessary cause and declines to name a single mechanism; Hsieh et al. (2024)
attribute the accuracy dip to a U-shaped attention bias that is present even when
document content is shuffled; Xiao et al. (2023) explain the primacy half through
softmax normalization and causal visibility. Positional encoding is where a
writer is most likely to overreach: RoPE's documented long-term decay predicts
recency, not a middle dip, so attributing lost-in-the-middle to "positional
encoding decay" alone skips a step the primaries do not support. The record's
main thinness is the persistence question. No source here re-runs Liu's exact
position-of-answer QA protocol on a 2024-2025 frontier model (GPT-4o, Claude 3,
Gemini 1.5); persistence in current models is supported by proxy through RULER,
NoLiMa, and Levy et al., which use different protocols. That gap is recorded
below and is the writer's to state plainly, not paper over.

The evidence does not undermine the commissioned angle. It supports every load-
bearing claim (real, reproducible, not cured by a bigger window, mechanism
unsettled) and adds one caution the angle must absorb: the effect size varies
sharply by model even within Liu's own 2023 data. GPT-3.5-Turbo drops 22 points
across 20 documents; Claude-1.3 moves about 4 points across the same span. "Models
are lost in the middle" overstates the flatter cases.

## Sources

```text
URL:         https://arxiv.org/abs/2307.03172
Kind:        primary — owns the lost-in-the-middle finding; controlled experiments
             the authors designed, ran, and measured. Published in TACL vol. 12
             (2024), pp. 157-173; ACL Anthology 2024.tacl-1.9. arXiv v3, 20 Nov 2023.
Establishes: The U-shaped accuracy-by-position curve on multi-document QA and on
             key-value retrieval; its presence in extended-context models; the
             middle case falling below closed-book; the saturation of a retriever-
             reader pipeline past ~20 documents. Firsthand measurement.
Paraphrase:  Nelson F. Liu (Stanford), Kevin Lin (UC Berkeley), John Hewitt
             (Stanford), Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni (all
             Samaya AI), and Percy Liang (Stanford) placed one answer-bearing
             Wikipedia chunk among k-1 relevant-but-wrong distractor chunks drawn
             from NaturalQuestions-Open (2,655 queries), and varied only the
             position of the answer-bearing chunk. Accuracy is highest when that
             chunk sits first or last and lowest in the middle. The same shape
             appears in a synthetic key-value task using random UUIDs, which strips
             out language semantics and still shows the dip. GPT-3.5-Turbo's multi-
             document QA accuracy can drop by more than 20 points, and in the 20-
             and 30-document settings its worst (middle) accuracy is below its
             closed-book accuracy of 56.1%. Where an input fits both a base and an
             extended-context model, the two curves are nearly identical, so the
             extended window does not confer better use of position.
Locators:    §2.3 and Table 1 (closed-book/oracle); Figure 5 and Appendix G Tables
             5-7 (multi-document QA by position); §3 and Figure 7 (key-value); §5
             and Figure 11 (retriever-reader saturation); footnote 6 and Appendix D
             (GPT-4 subset). Author affiliations on the title page.
Quote:       "we see a distinctive U-shaped performance curve—models are often much
             better at using relevant information that occurs at the very beginning
             (primacy bias) and very end of contexts (recency bias), and suffer
             degraded performance when forced to use information within the middle."
             And on the window: "extended-context models are not necessarily better
             than their non-extended counterparts at using their input context."
```

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary — owns the positional-encoding design it introduces. Vaswani
             et al., NeurIPS/NIPS 2017; arXiv 12 Jun 2017.
Establishes: Why a transformer needs position information at all, and how it enters
             the model. Firsthand: this is the paper that added positional encodings.
Paraphrase:  The transformer has no recurrence and no convolution, so on its own it
             treats a sequence as a set and cannot tell order. To give it order, the
             authors add a positional encoding vector to each token's input embedding
             at the bottom of the stack. Their scheme uses sine and cosine functions
             of different frequencies. This is the base fact the article needs to say
             position is injected, not innate, before it links the-mechanics/attention.
             Modern LLMs use a different scheme (see RoPE, next entry); the article
             should not imply GPT or LLaMA use these sinusoids.
Locators:    §3.5 "Positional Encoding".
Quote:       "Since our model contains no recurrence and no convolution, in order for
             the model to make use of the order of the sequence, we must inject some
             information about the relative or absolute position of the tokens... we
             add 'positional encodings' to the input embeddings at the bottoms of the
             encoder and decoder stacks."
```

```text
URL:         https://arxiv.org/abs/2104.09864
Kind:        primary — owns Rotary Position Embedding (RoPE). Su, Lu, Pan, Murtadha,
             Wen, Liu; Neurocomputing (2024); arXiv 20 Apr 2021, v5 8 Nov 2023.
Establishes: The positional-encoding scheme GPT-3.5 and LLaMA-family models actually
             use, and its "long-term decay" property. Firsthand design claim.
Paraphrase:  RoPE encodes a token's absolute position by rotating its query and key
             vectors by an angle proportional to position, with the result that the
             attention score between two tokens depends on their relative distance.
             The authors report a decay: the inter-token dependency weakens as the
             relative distance between two tokens grows. This matters as a caution.
             Decay-with-distance predicts that far-apart tokens attend less, which
             favors nearby (recent) tokens; it does not by itself produce a dip
             specifically in the middle with recovery at the far start. Using RoPE
             decay as the sole cause of lost-in-the-middle would be an interpretation
             the paper does not make.
Locators:    Abstract; §3.3 (relative position formulation) and §3.4.3 (long-term
             decay) in the full paper.
Quote:       RoPE "encodes the absolute position with a rotation matrix and meanwhile
             incorporates the explicit relative position dependency in self-attention
             formulation," with "decaying inter-token dependency with increasing
             relative distances."
```

```text
URL:         https://arxiv.org/abs/2309.17453
Kind:        primary — owns the "attention sink" finding. Xiao (MIT), Tian, Chen,
             Lewis (Meta AI), Han; with CMU/NVIDIA affiliations; ICLR 2024; arXiv 29
             Sep 2023, v3 12 Dec 2023.
Establishes: A firsthand, measured account of how attention distributes over a long
             input: models dump large attention on the first tokens regardless of
             meaning, and this is tied to softmax and to causal visibility. Supports
             the primacy half of the U mechanistically.
Paraphrase:  The authors observe that a surprisingly large share of attention lands
             on the initial tokens even though those tokens carry no special meaning,
             a pattern they name an attention sink. Their explanation is structural.
             Softmax forces the attention weights over the visible tokens to sum to
             one, so when no token is a strong match the model still has to put that
             weight somewhere, and the earliest tokens become the dumping ground.
             Because attention is causal, the first tokens are visible to every later
             token, which makes them the natural place for that surplus. This is an
             interpretation the authors argue for and support with attention maps, not
             a proof that it causes the QA dip Liu measured.
Locators:    §3 "Why do LLMs attend to initial tokens?" (attention-sink definition,
             softmax argument, causal-visibility argument); Figure 2 (attention maps).
Quote:       "A surprisingly large amount of attention score is allocated to the
             initial tokens, irrespective of their relevance." And: "initial tokens
             are visible to all subsequent tokens... As a result, initial tokens are
             more easily trained to serve as attention sinks."
```

```text
URL:         https://arxiv.org/abs/2406.16008
Kind:        primary — owns the positional-attention-bias mechanism claim and the
             calibration mitigation. Hsieh, Chuang, Li, Wang, Le, Kumar, Glass,
             Ratner, Lee, Krishna, Pfister (MIT and Google Cloud AI); Findings of ACL
             2024 (2024.findings-acl.890); arXiv 23 Jun 2024.
Establishes: Firsthand measurement that the attention a model pays to a document is
             U-shaped in that document's position and is present when the documents
             are shuffled, i.e. independent of content. Firsthand mitigation result.
Paraphrase:  The authors measure attention allocated to each document as a function
             of its slot in a long input and find the same U shape as the accuracy
             curve: documents at the start and end receive more attention, those in
             the middle less. The shape holds after the documents are randomly
             reordered, which the authors read as evidence that the bias attaches to
             position, not to what the document says. They model attention to a
             document as a sum of a relevance term and a position-bias term plus
             noise, then calibrate by subtracting an estimate of the bias, and report
             gains in long-context document ranking and in retrieval-augmented
             generation, and that the calibration stacks on top of reordering methods.
             The U-shaped-attention finding is firm; the exact percentage gains below
             are the paper's reported figures, taken from its tables via the paper's
             own text and not re-derived here.
Locators:    §3 and Figure 4 (U-shaped attention, shuffle-invariance); §4 (relevance
             + bias decomposition and calibration); §5 and Tables 4-5 (mitigation
             results). Models analyzed: Vicuna-7B-v1.5-16k and Tulu-2-7B, both LLaMA-
             family (RoPE).
Quote:       Reported: the U-shaped attention "pattern persists even after randomly
             shuffling document order, suggesting that this bias does not depend on
             the documents' actual content."
```

```text
URL:         https://arxiv.org/abs/2404.06654
Kind:        primary — owns the RULER benchmark and its measurements. C.-P. Hsieh,
             Sun, Kriman, Acharya, Rekesh, Jia, Zhang, Ginsburg (NVIDIA); COLM 2024;
             arXiv 9 Apr 2024.
Establishes: Firsthand later evidence that a passing needle-in-a-haystack score does
             not mean a model uses its full window, and that claimed context lengths
             overstate effective ones.
Paraphrase:  The authors build synthetic long-context tasks (harder retrieval, multi-
             hop tracing, aggregation, QA) at controlled lengths. Models that score
             near-perfect on the plain needle-in-a-haystack retrieval test still lose
             large amounts of accuracy on the harder tasks as the input grows. Of the
             long-context models tested, all claim 32K tokens or more, but only about
             half hold satisfactory performance out to 32K. This bounds the "bigger
             window" story from a different angle than Liu: the advertised length is
             not the usable length. It measures length degradation, not the position-
             of-answer curve specifically.
Locators:    Abstract; §4 results and the per-length effective-context table/heatmap.
Quote:       "While these models all claim context sizes of 32K tokens or greater,
             only half of them can maintain satisfactory performance at the length of
             32K." And: "Despite achieving nearly perfect accuracy in the vanilla NIAH
             test, almost all models exhibit large performance drops as the context
             length increases."
```

```text
URL:         https://arxiv.org/abs/2502.05167
Kind:        primary — owns the NoLiMa benchmark and its measurements. Modarressi,
             Deilamsalehy, Dernoncourt, Bui, Rossi, Yoon, Schütze (Adobe Research and
             LMU Munich); ICML 2025 (PMLR v267); arXiv 7 Feb 2025, v2 26 Mar 2025.
Establishes: Firsthand later evidence that current frontier models lose long-context
             accuracy as length grows once the answer is not a literal lexical match.
Paraphrase:  The authors extend the needle-in-a-haystack test so the question and the
             buried fact share little surface wording, forcing the model to make a
             latent association rather than match a string. Under this test, models
             that are near-perfect on short inputs fall off sharply with length: at
             32K tokens, ten of the evaluated models drop below half of their short-
             context baseline. GPT-4o, one of the more robust, falls from a 99.3%
             short baseline to 69.7% at 32K. The authors attribute the fall to the
             attention mechanism having a harder time in long inputs when it cannot
             lean on a literal match. This is length-and-retrieval degradation in
             2024-2025 models; it is the closest source here to Liu's setting but does
             not itself trace the position-of-answer U curve.
Locators:    Abstract and results tables (per-length scores; GPT-4o line; count of
             models below 50% at 32K).
Quote:       Reported: "performance degrades significantly as context length
             increases," and at 32K "11 models drop below 50% of their strong short-
             length baselines" (GPT-4o: 99.3% baseline to 69.7% at 32K).
```

```text
URL:         https://arxiv.org/abs/2402.14848
Kind:        primary — owns the FLenQA dataset and the length-isolation result. Levy,
             Jacoby, Goldberg (Bar-Ilan University and Allen Institute for AI); ACL
             2024 (2024.acl-long.818); arXiv 22 Feb 2024.
Establishes: Firsthand later evidence that reasoning accuracy falls as input length
             grows, well before a model's technical maximum, with length isolated as
             the only changing variable.
Paraphrase:  The authors hold the reasoning task fixed and pad the input to different
             lengths with irrelevant text, so length is the only thing that changes.
             Accuracy drops as the padding grows, and the drop starts far short of the
             models' maximum input length. This supports the commission's "not fixed
             by a bigger window" claim through a mechanism-agnostic route: more tokens
             hurt even when the task and the relevant content are unchanged. It does
             not isolate position within the input, so it complements rather than
             replicates Liu.
Locators:    Abstract; FLenQA construction section; length-degradation results.
Quote:       Reported: a "significant degradation in LLMs' reasoning performance at
             much shorter input lengths than their technical maximum."
```

```text
URL:         https://reference.langchain.com/python/langchain-community/document_transformers/long_context_reorder/LongContextReorder
Kind:        secondary — reports and responds to Liu's finding from outside the
             authoring party; it is framework documentation, not a measurement.
Establishes: That the finding reached mainstream retrieval tooling as a shipped
             mitigation, which grounds the article's closer about where the weakness
             lives for the reader. It does not establish the effect; it cites Liu for
             that.
Paraphrase:  LangChain ships a LongContextReorder document transformer whose stated
             purpose is to counter lost-in-the-middle by reordering retrieved
             documents so the most relevant sit at the start and end and the least
             relevant fall in the middle. Its class docstring cites the Liu paper
             (arXiv 2307.03172) directly. This is a retelling of Liu's result plus an
             engineering response, useful for the RAG closer, not independent
             confirmation of the effect.
Locators:    LongContextReorder class docstring on the reference page.
Quote:       "Reorder long context. Lost in the middle: Performance degrades when
             models must access relevant information in the middle of long contexts."
```

## Contradictions

- **Effect size is not uniform across models, in Liu's own data.** GPT-3.5-Turbo
  drops from 75.8% (answer first) to 53.8% (answer in the middle) across 20
  documents, a 22-point U. Claude-1.3 over the same 20 documents runs 59.9% /
  55.9% / 56.8% / 57.2% / 60.1%, a shallow dip of about 4 points, and Claude-1.3
  (100K) tracks it. In the 20-document setting MPT-30B-Instruct is nearly flat
  (53.7% to 56.3%). So the headline behavior is strong for GPT-3.5 and mild for
  Claude even in 2023. A writer must report the effect at the size the primary
  measured and name the model, not generalize the steep curve to all models.
  (Owner: Liu et al., Appendix G Tables 5-7.)

- **Secondary coverage inflates the drop to "more than 30%".** The primary says
  GPT-3.5-Turbo's accuracy "can drop by more than 20%", and the largest position
  gap in its tables is about 22-23 points (20-doc GPT-3.5-Turbo 75.8 to 53.8; 30-
  doc GPT-3.5-Turbo-16K 73.4 to 50.5). The ">30%" figure that appears in some
  write-ups is not in Liu. Use the primary's number. (Owner: Liu et al., §2.3.)

- **The mechanism is contested in emphasis among the primaries.** Liu explicitly
  declines to name one cause and rules out instruction tuning as necessary: the
  base model MPT-30B, before any instruction tuning, already shows the U, and the
  effect appears across positional-encoding schemes (ALiBi in MPT, RoPE in
  LongChat). Hsieh et al. locate the accuracy dip in a relevance-independent U-
  shaped attention bias. Xiao et al. explain the primacy half through softmax plus
  causal visibility. None of these is refuted by another; they name different
  layers of the same system, and the article should present them as candidate
  mechanisms, marking the exact cause as open. (Owners: Liu §4; Hsieh §3-4; Xiao
  §3.)

- **RoPE decay does not, on its own, predict a middle dip.** RoPE's documented
  property is decay of inter-token dependency with distance, which favors nearby
  tokens (recency). It does not by itself explain the primacy half or the recovery
  at the far start. Any claim that "positional encoding decay causes lost-in-the-
  middle" is an interpretation the RoPE paper does not make and that Liu's cross-
  scheme observation cuts against. (Owners: Su et al.; Liu §4.)

- **How much newer models and mitigations reduce the effect is unsettled and
  partly favorable.** Frontier models are near-perfect on simple needle-in-a-
  haystack retrieval, which reads like a fix. RULER shows that score is
  superficial: the same models degrade on harder long-context tasks and often fail
  before their claimed 32K. NoLiMa shows current models (GPT-4o included) fall
  with length once the answer is not a literal match. Even GPT-4, in Liu's own
  Appendix D subset, shows the same trend at higher absolute accuracy. The
  mitigations reduce but do not remove the effect: Liu's query-aware
  contextualization fixes key-value retrieval almost completely yet barely moves
  multi-document QA; instruction tuning narrows the base model's worst-case gap
  from about 10 points to about 4 but keeps the U; Hsieh's calibration and simple
  reordering help without erasing the bias. (Owners: RULER abstract/§4; NoLiMa;
  Liu §2.3, §4.2, §4.3, Appendix D; Hsieh §5.)

## Numbers

```text
Figure: GPT-3.5-Turbo multi-doc QA, 20 documents: 75.8% (index 0) / 57.2% (4) /
        53.8% (9, middle, worst) / 55.4% (14) / 63.2% (19, last)
Owner:  Liu et al. 2023, Appendix G Table 6
Scope:  NaturalQuestions-Open, 2,655 queries; accuracy = correct answer appears in
        output; one gold doc among 19 distractors; ~4K tokens
```

```text
Figure: GPT-3.5-Turbo-16K multi-doc QA, 30 documents: 73.4% (index 0) / 50.5% (9,
        worst) / 63.7% (index 29, last)
Owner:  Liu et al. 2023, Appendix G Table 7
Scope:  Same task; one gold doc among 29 distractors; ~6K tokens
```

```text
Figure: Claude-1.3 multi-doc QA, 20 documents: 59.9 / 55.9 / 56.8 / 57.2 / 60.1%
        (dip ~4 points) — the flat-curve counterexample
Owner:  Liu et al. 2023, Appendix G Table 6
Scope:  Same 20-document task
```

```text
Figure: Closed-book vs oracle accuracy (multi-doc QA). GPT-3.5-Turbo 56.1% /
        88.3%; GPT-3.5-Turbo-16K 56.0% / 88.6%; Claude-1.3 48.3% / 76.1%;
        LongChat-13B-16K 35.0% / 83.4%; MPT-30B-Instruct 31.5% / 81.9%
Owner:  Liu et al. 2023, Table 1
Scope:  Closed-book = no documents; oracle = only the single answer document. The
        20- and 30-document middle case for GPT-3.5-Turbo falls below its 56.1%
        closed-book score.
```

```text
Figure: Key-value retrieval worst case, GPT-3.5-Turbo-16K at 300 pairs (~16K
        tokens): 45.6% without query-aware contextualization, ~100% with it;
        Claude-1.3 near-perfect across all positions
Owner:  Liu et al. 2023, §3.2 and §4.2, Figure 7
Scope:  Synthetic UUID key-value task; 500 examples per setting; 75 / 140 / 300 pairs
```

```text
Figure: Instruction tuning narrows but keeps the U: MPT-30B base worst-case gap
        ~10 points, MPT-30B-Instruct ~4 points; both U-shaped
Owner:  Liu et al. 2023, §4.3, Figure 10
Scope:  20-document multi-doc QA; base vs instruction-tuned same architecture
```

```text
Figure: Encoder-decoder within training length is nearly flat: Flan-UL2 shows 1.9%
        absolute best-to-worst difference within its 2048-token training window;
        it develops the U only on inputs longer than that window
Owner:  Liu et al. 2023, §4.1, Figure 8
Scope:  Multi-doc QA; Flan-UL2 and Flan-T5-XXL
```

```text
Figure: Retriever-reader saturation: past 20 retrieved documents, reader accuracy
        gains ~1.5% (GPT-3.5-Turbo) and ~1% (Claude-1.3) while context and cost
        keep rising; reader accuracy saturates well before retriever recall does
Owner:  Liu et al. 2023, §5, Figure 11
Scope:  Open-domain QA on NaturalQuestions-Open; Contriever (MS-MARCO) retriever
```

```text
Figure: Effective vs claimed context (later work): all tested models claim >=32K,
        only about half hold performance to 32K on RULER's harder tasks
Owner:  Hsieh et al. 2024 (RULER), abstract/§4
Scope:  Synthetic tasks at controlled lengths; 4 task families, 13 tasks
```

```text
Figure: Frontier degradation with length (later work): at 32K, ten models fall
        below 50% of their short-context baseline; GPT-4o 99.3% -> 69.7%
Owner:  Modarressi et al. 2025 (NoLiMa)
Scope:  Needle-in-a-haystack with minimal lexical overlap between question and needle
```

## Source assets

```text
Asset: Liu et al. 2023, Figure 5 — multi-document QA accuracy vs position of the
       answer document, one U-shaped line per model, at 10 / 20 / 30 documents
Shows: The whole behavior in one image: high at the ends, low in the middle, and
       the extended-context line sitting on top of the base line
Crop:  Keep the y-axis (accuracy) and the x-axis position labels and the model
       legend; the 20-document panel alone carries the point if space is tight
```

```text
Asset: Liu et al. 2023, Table 1 — closed-book and oracle accuracy per model
Shows: The two reference points a reader needs to judge the middle dip: no
       documents (56.1% for GPT-3.5-Turbo) and the single right document (88.3%)
Crop:  Keep model rows and both columns; retain the exact percentages
```

```text
Asset: Liu et al. 2023, Figure 11 — retriever recall and reader accuracy vs number
       of retrieved documents
Shows: Reader accuracy flattening while retriever recall keeps climbing, the RAG
       point for the closer
Crop:  Keep both curves and the x-axis document count; retain axis labels
```

```text
Asset: Hsieh et al. 2024, Figure 4 — attention weight by document position, U-shaped
Shows: The attention side of the effect: the model's attention itself favors the
       ends over the middle, and holds that shape when documents are shuffled
Crop:  Keep the position axis and the attention-weight axis; if the paper shows
       shuffled vs ordered side by side, keep both to make the content-independence
       visible
```

```text
Asset: Xiao et al. 2023, Figure 2 — per-layer attention maps concentrating on the
       first tokens
Shows: The attention sink, the concrete picture behind the primacy half of the U
Crop:  Keep enough layers to show the sink is not a single-layer artifact; retain
       the token-index axis so the concentration at index 0 is legible
```

## Discarded

```text
URL: https://python.langchain.com/docs/how_to/long_context_reorder/ — the how-to
     content moved; the URL now 308-redirects to a generic overview page, so a
     reader who clicks it does not reach the material. Replaced by the stable
     LangChain API reference page for the class, which resolves without redirect
     and carries the same finding and citation.
```

```text
URL: https://www.getmaxim.ai/articles/solving-the-lost-in-the-middle-problem-...
     — vendor marketing blog; restates the finding without adding measured
     evidence and is a weaker secondary than the LangChain reference. Not needed.
```

```text
URL: Medium and dev.to write-ups of the Liu paper (e.g. medium.com/@carolzhu/...,
     dev.to "The Lost in the Middle Problem") — retellings of the primary with no
     independent measurement; a retelling supports only that the claim was made.
     The primary itself is cited instead.
```

```text
URL: https://arxiv.org/html/2603.10123 ("Lost in the Middle at Birth: An Exact
     Theory of Transformer Position Bias") — surfaced in search with a 2026 date;
     not read or verified, and a theory claim of this weight should be checked in
     full before use. Left out rather than cited unread. Flagged for a later
     invocation if the article wants a theoretical mechanism source.
```

## Unresolved for the orchestrator

- No source here replicates Liu's position-of-answer QA curve on a 2024-2025
  frontier model (GPT-4o, Claude 3/3.5, Gemini 1.5). Persistence in current models
  rests on proxy evidence (RULER, NoLiMa, Levy, and Liu's own GPT-4 subset). If the
  article needs to assert the specific U-shape in a named current model, that
  evidence is missing and a further brief should commission it. Owner of the gap:
  none yet published in what was searched; the writer should hedge the persistence
  claim to what these proxies support.
- The exact calibration percentage gains in Hsieh et al. (2024) were read from the
  paper's text rather than re-derived from its full tables. The load-bearing claim
  (U-shaped, content-independent attention bias) is verified; if the writer quotes a
  specific gain figure, the owning table should be reopened first.
