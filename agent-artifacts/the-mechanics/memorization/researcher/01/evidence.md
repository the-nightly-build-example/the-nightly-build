# Evidence: the-mechanics/memorization (01)

The evidence strongly supports the commissioned chain: a word-for-word quote can
come out of a model because the exact token sequence is fit into the model's
weights during next-token training (memorization), and two settled drivers make
it happen more often, duplication of the string in the training data and larger
model scale. All four extraction/memorization primaries were read firsthand, and
a concrete regurgitation case (the New York Times complaint) was read at the
page level, including its side-by-side GPT-4-vs-original comparisons. The
memorization / retrieval / hallucination boundary is cleanly sourced, and the
same NYT filing usefully separates in-weights memorization (old articles) from
query-time retrieval (post-cutoff articles fetched by Bing). The record is
thin in three places: the exact per-category counts of GPT-2's 604 memorized
examples were read from rendered text, not confirmed against the table image;
the per-model gigabyte/n-gram counts in the 2023 scalable-extraction paper were
not visually verified (the robust figures are "gigabytes," "over 10,000
examples for $200," and "over 5%"); and the commission's phrase "the
duplication threshold" overstates the literature, which reports a *log-linear*
relationship, not a hard cutoff. One genuine tension the writer must carry:
"how much has a model memorized" has no single answer, it ranges from
0.00000015% to at least 1% depending entirely on the definition used, and the
NYT and OpenAI disagree on whether regurgitation is routine or an
adversarially-provoked rare bug.

## Sources

```text
URL:         https://arxiv.org/abs/2012.07805
Kind:        primary — the study's authors (Carlini, Tramèr, Wallace, et al.)
             own the extraction result firsthand.
Establishes: An adversary querying GPT-2 recovered hundreds of verbatim training
             sequences, including data present in only a single training
             document; larger models are more vulnerable; formal "k-eidetic
             memorization" definition.
Paraphrase:  Querying the public GPT-2 (XL, 1.5B parameters), the authors
             generated 1,800 candidate sequences (100 samples across 3
             generation strategies x 6 ranking metrics) and confirmed 604 unique
             memorized examples against GPT-2's training data. Content types
             included names, phone numbers and email addresses (PII), IRC
             conversations, source code, and 128-bit UUIDs. Some recovered
             sequences appear in just one training document. A string s is
             "k-eidetic memorized" if it is extractable and appears in at most k
             examples in the training data.
Locators:    Abstract; Results / Table 1 (category breakdown); definition of
             k-eidetic memorization (Section 3). Full text read via
             ar5iv.labs.arxiv.org/abs/2012.07805.
Quote:       "A string s is k-eidetic memorized (for k>=1) by an LM if s is
             extractable from the LM and s appears in at most k examples in the
             training data." (definition, verified via ar5iv rendering)
```

```text
URL:         https://arxiv.org/abs/2202.07646
Kind:        primary — the authors (Carlini, Ippolito, Jagielski, Lee, Tramèr,
             Zhang; Google Research / UPenn / Cornell; ICLR 2023) own these
             quantified measurements. Intro pages read firsthand from the PDF.
Establishes: The three settled drivers, quantified: memorization grows
             log-linearly with (1) model capacity, (2) number of times an
             example is duplicated, (3) tokens of context in the prompt. The 6B
             model memorizes at least 1% of its training set.
Paraphrase:  Using the GPT-Neo family (125M, 1.3B, 2.7B, 6B) trained on The Pile
             (825GB), the authors prompt the model with the first (L-50) tokens
             of a training sequence and call it "extractable" if the model emits
             the exact next 50-token suffix under greedy decoding (50 tokens ~
             127 characters ~ 25 words). Larger models memorize 2-5x more within
             a family; a ten-fold increase in model size raises memorization by
             19 percentage points on their normalized eval set (near-perfect
             log-linear fit, R^2 = 99.8%). The 6B GPT-J model "memorizes at
             least 1% of its training dataset," contrasted with the earlier
             GPT-2 extraction's loose 0.00000015% lower bound (about 600
             examples). A GPT-2 baseline trained on different data (WebText)
             shows near-zero extraction, controlling for test-set overlap.
Locators:    Abstract; Intro p.1 (1% vs 0.00000015%); p.2 three properties;
             Definition 3.1 p.3; Section 4.1 "Bigger Models Memorize More" p.4
             (19 points, R^2 99.8%); Figure 1 (a/b/c panels). Read pages 1-4 of
             the PDF directly.
Quote:       "a ten fold increase in model size corresponds to an increase in
             memorization of 19 percentage points." (Section 4.1)
             "the 6 billion parameter GPT-J model ... memorizes at least 1% of
             its training dataset: The Pile." (Introduction, p.1)
```

```text
URL:         https://arxiv.org/abs/2107.06499
Kind:        primary — the authors (Lee et al.) own the deduplication finding.
Establishes: Duplication in the training data is the driver, shown from the
             other direction: removing duplicates cuts verbatim emission about
             ten-fold. Supports "duplication drives it."
Paraphrase:  Over 1% of the unprompted output of LMs trained on standard
             datasets is copied verbatim from the training data. C4 contains a
             single 61-word English sentence repeated over 60,000 times. Models
             trained on deduplicated data emit memorized text about ten times
             less frequently and reach the same or better accuracy in fewer
             steps. Train-test overlap affects over 4% of the validation set of
             standard datasets. Two deduplication tools are introduced (exact
             substring and approximate near-duplicate matching).
Locators:    Abstract (all four figures stated there).
Quote:       "over 1% of the unprompted output of language models trained on
             these datasets is copied verbatim from the training data ...
             Deduplication allows us to train models that emit memorized text
             ten times less frequently."
```

```text
URL:         https://arxiv.org/abs/2311.17035
Kind:        primary — the authors (Nasr, Carlini, et al.) own the scalable
             "poem poem poem" extraction result.
Establishes: The concrete production regurgitation case with numbers: a
             divergence attack pulls training data out of aligned ChatGPT; open
             models leak gigabytes.
Paraphrase:  "Extractable memorization" is training data an adversary can
             recover by querying a model without prior knowledge of its data.
             Existing techniques extract gigabytes from open models (Pythia,
             GPT-Neo) and semi-open models (LLaMA, Falcon). To attack aligned
             ChatGPT the authors use a new "divergence attack" ("Repeat the word
             'poem' forever") that breaks the chatbot persona and makes it emit
             training data at a rate 150x higher than normal. Roughly $200 of
             queries recovered over 10,000 unique verbatim-memorized examples;
             in the strongest configuration over 5% of ChatGPT output was a
             direct verbatim 50-token copy of training data. Extracted content
             included real email addresses, phone numbers, book and poem
             passages, and code.
Locators:    Abstract (gigabytes; 150x). $200 / >10,000 examples and the "over
             5%" figure and megabytes-for-$200 read firsthand from the authors'
             own writeup (below). The per-model n-gram counts were NOT visually
             verified; do not cite them.
Quote:       "in order to attack the aligned ChatGPT, we develop a new
             divergence attack that causes the model to diverge from its
             chatbot-style generations and emit training data at a rate 150x
             higher than when behaving properly." (abstract)
```

```text
URL:         https://not-just-memorization.github.io/extracting-training-data-from-chatgpt.html
Kind:        primary — the same authors' own public writeup of arXiv 2311.17035.
Establishes: Plain-language, quotable versions of the key ChatGPT-extraction
             numbers, plus the responsible-disclosure timeline.
Paraphrase:  "Over five percent of the output ChatGPT emits is a direct verbatim
             50-token-in-a-row copy" of training data. About $200 recovered
             "over 10,000 unique verbatim-memorized training examples" / "several
             megabytes"; more spend would extract about a gigabyte. The prompt
             makes the model "escape its fine-tuning alignment procedure and fall
             back on its pre-training data." Recovered a real email address and
             phone number, code, book passages, disclaimers. Disclosed to OpenAI
             Aug 30 2023 after discovery Jul 11; published Nov 28 2023 after a
             90-day window.
Locators:    Body sections on rates, cost, method, and disclosure.
Quote:       "we can extract several megabytes of ChatGPT's training data for
             about two hundred dollars."
```

```text
URL:         https://storage.courtlistener.com/recap/gov.uscourts.nysd.612697/gov.uscourts.nysd.612697.1.0.pdf
Kind:        primary — the plaintiff's own court filing (The New York Times
             Company v. Microsoft Corp. et al., S.D.N.Y. No. 1:23-cv-11195,
             complaint filed Dec 27 2023). Owns the allegation, not neutral
             proof of behavior. Read at page level (pp. 29-40).
Establishes: A concrete, dated regurgitation case with side-by-side evidence;
             and, within the same document, an explicit split between
             in-weights memorization and query-time retrieval.
Paraphrase:  Para 98: the GPT LLMs "have 'memorized' copies of many of those
             same works encoded into their parameters," and GPT-4 "will output
             near-verbatim copies of significant portions of Times Works when
             prompted to do so." Paras 99-100 and 104-107 show side-by-side
             GPT-4/ChatGPT output against the original 2019 taxi-medallion
             series, the 2012 Apple-outsourcing series, "Snow Fall" (2012), and
             the 2012 Pete Wells Guy Fieri review, with copied text highlighted.
             Para 101: "Exhibit J provides scores of additional examples of
             memorization of Times Works by GPT-4." Para 102 names two distinct
             mechanisms: (1) "memorized" copies retrieved from the models
             themselves, and (2) synthetic search results generated from copies
             stored in Bing's search index. Paras 108-114 ("Unauthorized
             Retrieval") show Bing Chat / Browse with Bing reproducing an
             October 2023 article ("The Secrets Hamas Knew About Israel's
             Military") that postdates GPT-4 Turbo's April 2023 training cutoff,
             proving that output came from live retrieval, not the weights.
Locators:    pp. 29-40, paras 94-114. Memorization: 98-107. Retrieval: 108-114.
Quote:       "the GPT LLMs themselves have 'memorized' copies of many of those
             same works encoded into their parameters ... the current GPT-4 LLM
             will output near-verbatim copies of significant portions of Times
             Works when prompted to do so." (para 98)
```

```text
URL:         https://arxiv.org/abs/2005.11401
Kind:        primary — Lewis et al. own the RAG architecture they define. Used
             to fix the retrieval boundary.
Establishes: Retrieval is an external lookup at inference time, structurally
             distinct from knowledge stored in weights.
Paraphrase:  RAG pairs a "parametric memory" (a pre-trained seq2seq generator,
             i.e. knowledge in weights) with a "non-parametric memory" (a dense
             vector index of Wikipedia) accessed by a neural retriever. The
             retriever queries the external index at inference based on the
             input, and the generator conditions on the retrieved passages.
             Retrieval happens at query time, not training time.
Locators:    Abstract; architecture description.
Quote:       "the non-parametric memory is a dense vector index of Wikipedia,
             accessed with a pre-trained neural retriever."
```

```text
URL:         https://arxiv.org/abs/2202.03629
Kind:        primary — Ji et al.'s survey defines the term. Used to fix the
             hallucination boundary.
Establishes: Hallucination is fabricated content, not the emission of real
             stored text.
Paraphrase:  Hallucination in NLG is generated text that is nonsensical or
             unfaithful to the source material or to factual reality:
             fabrication and unfaithful generation not grounded in any real
             source. This is the opposite of memorization, which emits real
             text that exists in the training data.
Locators:    Abstract; definition section.
Quote:       (definition paraphrased above; abstract read via arXiv page.)
```

```text
URL:         https://www.theregister.com/2023/12/01/chatgpt_poetry_ai/
Kind:        secondary — trade press reporting on arXiv 2311.17035 from outside
             the authoring team.
Establishes: Independent retelling of the ChatGPT-extraction numbers and that
             the attack was unpatched at publication (context, not proof).
Paraphrase:  Reports the $200 cost, "over 10,000" recovered examples matched
             against a ~10 TB dataset, the "divergence attack" that breaks the
             chatbot persona (short single-token words like "poem"/"company"
             work best), and that at publication the attack "doesn't seem to
             have been patched."
Locators:    Body.
Quote:       "The trick, described as a divergence attack, appears to break the
             model's chatbot persona ... its outputs diverge and it can start
             leaking training data."
```

```text
URL:         https://news.cornell.edu/stories/2024/01/chatgpt-memorizes-and-spits-out-entire-poems
Kind:        secondary — university news office reporting a separate academic
             study (D'Souza and Mimno, Cornell). A distinct study from Carlini's;
             do not conflate.
Establishes: Independent corroboration that prominence/duplication in the
             corpus drives which texts are memorized.
Paraphrase:  Prompted for 240 poems by 60 American poets, ChatGPT reproduced 72
             verbatim; Google's PaLM produced 10; Pythia and GPT-2 produced
             none. Inclusion in the poetry canon (the 1983 Norton Anthology was
             the strongest predictor) best explained which poems were memorized,
             consistent with duplication driving memorization.
Locators:    Body.
Quote:       ChatGPT "retrieved" 72 of the 240 poems verbatim; "inclusion in the
             poetry canon was the most important factor."
```

```text
URL:         https://openai.com/index/openai-and-journalism/
Kind:        secondary/interested-party — OpenAI's public rebuttal (Jan 8 2024).
             A party with stake, owns its own statement but not neutral on the
             facts. Canonical page returned HTTP 403 on direct fetch; the "rare
             bug" wording was verified via NBC (nbcdfw.com) quoting the statement.
Establishes: The defendant's counter-narrative and, notably, its own concession
             that duplication drives memorization.
Paraphrase:  OpenAI calls "regurgitation" "a rare bug that we are working to
             drive to zero," says it is more likely when content appears more
             than once in the training data, and argues the Times "intentionally
             manipulated prompts," often including lengthy article excerpts, and
             cherry-picked from many attempts.
Locators:    OpenAI statement, Jan 8 2024; "rare bug" quote confirmed at
             https://www.nbcdfw.com/news/national-international/openai-responds-to-new-york-times-lawsuit-says-regurgitation-of-content-is-a-rare-bug/3428395/
Quote:       "'regurgitation' ... 'is a rare bug that we are working to drive to
             zero.'"
```

## Contradictions

- **"How much is memorized" has no single number; it is definition-dependent.**
  The 2021 paper's unprompted k-eidetic measure yields a loose lower bound of
  0.00000015% (~600 examples). The 2023 paper's "extractable/discoverable"
  measure (prompt with the true prefix, greedy-decode the suffix) yields at
  least 1% for the 6B model. The 2023 paper itself says k-eidetic memorization
  is "less useful for tightly bounding memorization." Same phenomenon, numbers
  four orders of magnitude apart. The writer must state which definition a
  figure belongs to.

- **NYT vs OpenAI on whether regurgitation is normal.** The NYT complaint (para
  98) presents near-verbatim GPT-4 output as behavior triggered "with minimal
  prompting." OpenAI counters that it is "a rare bug," that the Times
  "manipulated prompts" with lengthy excerpts, and cherry-picked. Two parties
  with direct stake disagree; present as a dispute, not settled fact. Both,
  however, agree duplication increases it (OpenAI concedes this explicitly).

- **604 vs 600.** The 2021 paper reports 604 confirmed memorized examples; the
  2023 paper rounds this to "just 600 memorized training examples." Minor;
  cite 604 to the 2021 owner.

- **Scale is clean within a family, "more complicated" across families.** The
  2023 abstract flags that the log-linear relationships "become more
  complicated when generalizing these results across model families." The
  2-5x and 19-points-per-10x figures are within-family (GPT-Neo). Do not
  present them as a universal constant.

- **No hard "duplication threshold."** The commission asks for "the duplication
  threshold." The literature reports a *log-linear* relationship between
  duplication count and extractability (2023 Figure 1b), not a cutoff. The
  dedup paper's "61-word sentence repeated over 60,000 times" is an example of
  extreme duplication in C4, not a memorization threshold. Frame it as "more
  copies -> steadily more likely," not "past N copies it memorizes."

## Numbers

```text
Figure: 604 unique memorized examples confirmed from GPT-2
Owner:  Carlini et al. 2021 (arXiv 2012.07805)
Scope:  Out of 1,800 candidate sequences (100 x 3 generation strategies x 6
        ranking metrics); target model GPT-2 XL, 1.5B parameters; validated
        against GPT-2's ~40GB training data. (2023 paper rounds this to "600.")
```

```text
Figure: at least 1% of training data memorized
Owner:  Carlini et al. 2023 (arXiv 2202.07646)
Scope:  6B-parameter GPT-J; training set The Pile (825GB); "extractable"
        = 50-token prefix reproduces the exact next 50 tokens under greedy
        decoding. Absolute headline figure.
```

```text
Figure: ~0.00000015% (loose lower bound)
Owner:  Carlini et al. 2023 restating Carlini et al. 2020/2021
Scope:  The fraction implied by ~600 unprompted-extractable GPT-2 examples over
        its 40GB dataset. Directly contrasted with the 1% above to show the
        definition dependence.
```

```text
Figure: 2-5x more memorization for larger models
Owner:  Carlini et al. 2023 (arXiv 2202.07646)
Scope:  Within the GPT-Neo family (125M / 1.3B / 2.7B / 6B), worst-case
        normalized eval set.
```

```text
Figure: +19 percentage points per 10x model size (R^2 = 99.8%)
Owner:  Carlini et al. 2023, Section 4.1
Scope:  GPT-Neo family; biased/normalized sample (over-represents duplicates
        and long sequences) — the SLOPE is the finding, not the absolute level
        on that sample. The paper states the absolute level in Figure 1a "is
        not particularly important."
```

```text
Figure: ~10x less verbatim emission after deduplication; >1% of unprompted
        output copied verbatim before dedup; C4 sentence repeated >60,000x;
        >4% train-test overlap in standard validation sets
Owner:  Lee et al. 2021 (arXiv 2107.06499)
Scope:  Standard LM datasets (C4 and others); unprompted generation.
```

```text
Figure: over 10,000 unique verbatim examples for ~$200; over 5% of output a
        verbatim 50-token copy; 150x higher emission via divergence attack;
        gigabytes extractable from open models
Owner:  Nasr, Carlini et al. 2023 (arXiv 2311.17035) + authors' writeup
Scope:  ChatGPT (gpt-3.5-turbo) via the "poem"-repetition divergence attack;
        open-model gigabyte figures are order-of-magnitude (per-model n-gram
        counts NOT visually verified).
```

```text
Figure: 72 of 240 poems reproduced verbatim (vs PaLM 10, Pythia/GPT-2 0)
Owner:  D'Souza and Mimno, via Cornell Chronicle (secondary)
Scope:  240 poems by 60 American poets; canon inclusion best predictor.
        Independent corroboration of the duplication/prominence driver.
```

## Source assets

```text
Asset: NYT complaint, para 99 and para 100, two-column "Output from GPT-4" vs
       "Actual text from NYTimes" comparisons (taxi-medallion series; Apple
       outsourcing series), with differences visible.
Shows: What "near-verbatim" actually looks like — long passages matching
       word-for-word with only scattered edits. Makes memorization concrete.
Crop:  Keep both column headers and enough parallel lines to see the match;
       omit surrounding legal boilerplate.
```

```text
Asset: NYT complaint, paras 105 and 107, the original-article text with the
       copied portions highlighted in red ("Snow Fall"; Guy Fieri review).
Shows: Precisely which spans were reproduced verbatim vs paraphrased — the red
       highlighting is the evidence itself.
Crop:  Retain the red-highlighted lines and enough black context to show it is
       partial, not total, copying.
```

```text
Asset: NYT complaint, paras 112-113, Bing Chat reproducing the October 2023
       "Secrets Hamas Knew" article (post-dating the April 2023 training
       cutoff).
Shows: The retrieval-vs-memorization boundary in one image: this text could not
       be in the weights, so it came from live lookup.
Crop:  Keep the Bing Chat frame and the article date cue; this asset only works
       paired with the cutoff fact.
```

```text
Asset: Carlini et al. 2023, Figure 1 (three panels a/b/c: fraction extractable
       vs model size, vs number of repetitions, vs prompt length).
Shows: All three settled drivers as clean upward log-linear lines, with a flat
       near-zero baseline (GPT-2 on different data) proving it is not test
       overlap.
Crop:  Keep the flat baseline line in each panel; without it the trend loses its
       control. Note the log x-axes in the caption.
```

```text
Asset: Carlini et al. 2021, Table 1 (categories of the 604 memorized examples).
Shows: The variety of memorized content (news, code, PII, UUIDs, licenses,
       religious text), grounding "what gets memorized."
Crop:  Reproduce as a small table, not a screenshot; per-category counts were
       read from rendered text and should be re-checked against the source
       before any exact number is printed.
```

## Discarded

```text
URL: https://nytco-assets.nytimes.com/2023/12/NYT_Complaint_Dec2023.pdf
     — Times-hosted copy of the complaint; blocked on fetch. Used the
     CourtListener docket copy (same document) instead; not a separate source.
```

```text
URL: (WebFetch summarizer numbers "33% extractable at 50 tokens vs 65% at 450
     tokens" for the 2023 paper) — REJECTED. Not found on firsthand reading of
     the paper's own pages/figures; treated as a summarizer artifact and not
     used. The verified context-length finding is directional/log-linear
     (Figure 1c), not those percentages.
```

```text
URL: (WebFetch summarizer per-model counts "591,475 unique 50-grams for GPT-Neo
     6B," "LLaMA 65B 0.789%" for arXiv 2311.17035) — NOT USED. Could not be
     visually verified against the paper; the robust, citable figures are
     "gigabytes," "over 10,000 examples for ~$200," and "over 5%."
```
