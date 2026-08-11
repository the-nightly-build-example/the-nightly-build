# Evidence record: the-evidence/gpt-2

The evidence supports the commission's angle firsthand. The GPT-2 paper is a
technical report with no discussion of danger, misuse, release, or society
anywhere in its text: the "too dangerous" story lives entirely in OpenAI's
accompanying communications and the follow-up reports, not in the results
tables. The paper's own numbers are strong on zero-shot language modeling (state
of the art on 7 of 8 datasets) and, by its own repeated hedges, weak to random
on most downstream tasks. OpenAI's own November 2019 follow-up report says its
threat monitoring found "minimal evidence of misuse" and "did not find evidence
of GPT-2 direct misuse in publicly-accessible forums." All of that is
established from primaries read in full.

Two things are thinner and must not be overstated. First, the original February
14, 2019 announcement blog ("Better Language Models and Their Implications") is
egress-blocked from this session (openai.com returns 403 as a policy denial, not
a gated fetch; web.archive.org is also blocked). Its most-quoted sentence is
confirmed only through two independent secondaries, not read on OpenAI's own
page. Second, "too dangerous" is a genuinely contested attribution: OpenAI's
blog did not use those words (it wrote "concerns about malicious applications"),
but at least one major outlet (The Guardian) attributed the phrase to the
"creators," so the honest finding is that OpenAI invited the framing rather than
that the press invented it against them. The record flags both in
Contradictions.

## Sources

```text
URL:         https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
Kind:        Primary. This is the GPT-2 paper itself, hosted on OpenAI's own CDN
             (HTTP 200, read in full as text). It owns every claim about what the
             paper measured and how it hedged.
Establishes: Firsthand: author list and title; the four model sizes; WebText
             construction; the zero-shot language-modeling results and which were
             SOTA; the downstream-task numbers; and the paper's own hedges. Also
             establishes firsthand the absence of any danger/release/misuse
             language in the paper.
Paraphrase:  "Language Models are Unsupervised Multitask Learners," by Alec
             Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya
             Sutskever (OpenAI). Four models: 117M (12 layers, d_model 768), 345M
             (24, 1024), 762M (36, 1280), 1542M (48, 1600) parameters (Table 2).
             The largest, GPT-2 (1.5B), sets state of the art on 7 of 8 zero-shot
             language-modeling datasets but "still underfits WebText." WebText was
             built by scraping all outbound links from Reddit that received at
             least 3 karma, yielding ~45 million links, "slightly over 8 million
             documents for a total of 40 GB of text," with all Wikipedia removed
             and no links after Dec 2017. The strong results are on
             language-modeling perplexity/accuracy benchmarks. On downstream
             tasks the paper repeatedly says the result is weak: reading
             comprehension (CoQA) 55 F1 is "competitive with supervised baselines
             in a zero-shot setting," but summarization is "only rudimentary,"
             translation is far below unsupervised baselines, and question
             answering is "much, much, worse" than open-domain QA systems. The
             paper contains no section, sentence, or footnote about danger,
             misuse, malicious use, release strategy, or societal risk.
Locators:    Title/authors p.1; Abstract p.1; WebText section 2.1 p.3; Table 2
             (model sizes) p.4; Table 3 (zero-shot LM results) p.5; Winograd
             section 3.4 p.6; CoQA section 3.5 p.6; summarization Table 4 and
             section 3.6 p.6; translation section 3.7 p.7; QA section 3.8 and
             Table 5 p.7; Discussion/conclusion hedges p.8.
Quote:       "Our largest model, GPT-2, is a 1.5B parameter Transformer that
             achieves state of the art results on 7 out of 8 tested language
             modeling datasets in a zero-shot setting but still underfits
             WebText." (Abstract)
             "While suggestive as a research result, in terms of practical
             applications, the zero-shot performance of GPT-2 is still far from
             use-able." (Discussion)
             "There are undoubtedly many practical tasks where the performance of
             GPT-2 is still no better than random. Even on common tasks that we
             evaluated on, such as question answering and translation, language
             models only begin to outperform trivial baselines when they have
             sufficient capacity." (Discussion)
             "The performance of GPT-2 is still much, much, worse than the 30 to
             50% range of open domain question answering systems..." (section 3.8)
```

```text
URL:         https://arxiv.org/abs/1908.09203
Kind:        Primary for "what OpenAI said and did." OpenAI's own report ("OpenAI
             Report, November, 2019"), lead author an OpenAI staff member, read in
             full from the arXiv PDF (abstract page resolves HTTP 200). It is
             secondary for "whether the capability was actually dangerous," since
             OpenAI is an interested party judging its own release.
Establishes: Firsthand: the staged-release timeline and rationale, and OpenAI's
             own threat-monitoring findings.
Paraphrase:  "Release Strategies and the Social Impacts of Language Models," by
             Irene Solaiman, Miles Brundage, Jack Clark, Amanda Askell, Ariel
             Herbert-Voss, Jeff Wu, Alec Radford, Gretchen Krueger, Jong Wook Kim,
             Sarah Kreps, Miles McCain, Alex Newhouse, Jason Blazakis, Kris
             McGuffie, and Jasmine Wang (OpenAI, with co-authors at Harvard,
             Cornell, Politiwatch, and Middlebury's CTEC). OpenAI made four models
             (124 million to ~1.5 billion parameters) and released them in stages
             rather than at once "due to concerns about the larger models being
             misused": the 124M model in February 2019, 355M in May, 774M in
             August (with the first version of this report), and the full 1.5B in
             November. The report calls this a "delay of nine months." On misuse,
             OpenAI's own monitoring found little: "In addition to finding minimal
             evidence of misuse so far, several other factors contributed to our
             confidence in publishing our 774 million and 1.5 billion parameter
             models." Its threat monitoring "did not find evidence of GPT-2 direct
             misuse in publicly-accessible forums but we did see evidence of
             discussion of misuse," which had "declined by our mid-May release,"
             and found "no clear malicious code sharing or large-scale misuse, and
             only a small number of cases of explicit public plans for misuse." A
             separate detection line found synthetic text is fairly detectable
             (an OpenAI classifier detects 1.5B GPT-2 text with ~95% accuracy).
Locators:    Cover/date p.1; author block p.1; Executive summary paras. 2-3 p.1;
             Section 1 "Staged Release" p.2; Section 4.2 "Misuse: Actor
             Assessment" and "1.5 Billion Parameter Model: Threat Landscape" p.7;
             detection ~95% p.9 area; Section 5 recommendations p.16+.
Quote:       "In addition to finding minimal evidence of misuse so far..."
             (Executive summary)
             "Our threat monitoring did not find evidence of GPT-2 direct misuse
             in publicly-accessible forums but we did see evidence of discussion
             of misuse."
             "We also found no clear malicious code sharing or large-scale misuse,
             and only a small number of cases of explicit public plans for
             misuse."
             "While the landscape for possible misuse has changed since the time
             of our initial release, we have not seen any significant action
             toward misuse language models during this time."
```

```text
URL:         https://cdn.openai.com/GPT_2_August_Report.pdf
Kind:        Primary. The August 2019 first version of the same OpenAI report,
             released alongside the 774M model. This is the "six-month follow-up"
             document the commission names. Hosted on OpenAI's own CDN (HTTP 200,
             read in full).
Establishes: Firsthand: that by the six-month mark OpenAI already reported
             "minimal evidence of misuse" and released the 774M model on that
             basis. It corroborates the November findings at the earlier date, so
             the "no significant misuse found" conclusion is not a late revision.
Paraphrase:  "OpenAI Report, August, 2019," same title and lead authorship. It
             announces the 774M release and states that "In addition to finding
             minimal evidence of misuse, the positive social impact of beneficial
             uses... gave us confidence in publishing our 774 million parameter
             model." Its threat-monitoring language matches the November version:
             monitoring "did not find evidence of GPT-2 direct misuse in
             publicly-accessible forums."
Locators:    Cover/date p.1; executive summary p.1; staged-release and misuse
             passages ~p.1-2 and threat-monitoring section p.6-7 area.
Quote:       "In addition to finding minimal evidence of misuse, the positive
             social impact of beneficial uses... gave us confidence in publishing
             our 774 million parameter model."
```

```text
URL:         https://slate.com/technology/2019/02/openai-gpt2-text-generating-algorithm-ai-dangerous.html
Kind:        Secondary, independent. Contemporary reporting by Slate (Aaron Mak,
             February 22, 2019), a party outside OpenAI. Read via WebFetch (HTTP
             200). It is evidence of how the "too dangerous" framing traveled and
             of contemporary skepticism.
Establishes: Firsthand (as reporting): that the "too dangerous" phrasing was the
             outlet's own characterization, not a quote from OpenAI; and that
             independent researchers questioned both the novelty and the danger at
             the time.
Paraphrase:  The article, headlined "When Is Technology Too Dangerous to Release
             to the Public?", reports OpenAI withheld the full model citing
             "safety and security concerns" and that its blog "fretted that it
             could be used to generate false news articles, impersonate people
             online, and generally flood the internet with spam and vitriol." The
             "too dangerous to release" line is Slate's framing, not attributed to
             OpenAI as a quotation. It reports skepticism: Robert Frederking
             (Carnegie Mellon) said "It's not clear that there's any, like,
             stunningly new technique they [OpenAI] are using"; David Bau (MIT)
             said "One organization pausing one particular project isn't really
             going to change anything long term"; and it notes some accused OpenAI
             of "exaggerating the risks of its algorithm for media attention."
Locators:    Headline and byline at top; OpenAI's stated reasons in the opening
             sections; researcher quotes and the "exaggerating the risks"
             criticism in the body.
Quote:       Headline: "When Is Technology Too Dangerous to Release to the
             Public?" Frederking: "It's not clear that there's any, like,
             stunningly new technique they [OpenAI] are using."
```

```text
URL:         https://en.wikipedia.org/wiki/GPT-2
Kind:        Secondary/tertiary, independent of OpenAI. Read via WebFetch (HTTP
             200). Used for how the episode is summarized and cited now, the
             release timeline, the exact original-blog quotation, and named
             criticism. Its own claims are sourced to further primaries; treat it
             as pointing to those, not as itself owning them.
Establishes: That the most-quoted OpenAI sentence is "Due to our concerns about
             malicious applications of the technology, we are not releasing the
             trained model"; the staged timeline (Feb 14 announcement, 774M on
             Aug 20 2019, full 1.5B on Nov 5 2019); and named criticism of the
             danger framing.
Paraphrase:  Reproduces OpenAI's February 2019 line verbatim (above). Notes The
             Guardian's headline "New AI fake text generator may be too dangerous
             to release, say creators," which attributes the "too dangerous"
             concern to OpenAI itself. Records that Anima Anandkumar (then
             Caltech/Nvidia) called the stance "malicious BS" and said there was
             no evidence GPT-2 had the capabilities to pose the described threats.
             States that early concerns about widespread misuse "did not come to
             pass," and that OpenAI reported by November 2019 it had "seen no
             strong evidence of misuse so far."
Locators:    Release/controversy section of the article; the Guardian and
             Anandkumar references; the timeline in the infobox/history.
Quote:       OpenAI (Feb 2019, via Wikipedia): "Due to our concerns about
             malicious applications of the technology, we are not releasing the
             trained model."
             The Guardian headline (via Wikipedia): "New AI fake text generator
             may be too dangerous to release, say creators."
             Anandkumar (via Wikipedia): "malicious BS."
```

```text
URL:         https://techcrunch.com/2019/02/17/openai-text-generator-dangerous/
Kind:        Secondary, independent. Contemporary reporting by TechCrunch (Zack
             Whittaker, February 17, 2019). Read via WebFetch (HTTP 200). Evidence
             of the contemporary framing and of the "opposite of open" backlash.
Establishes: Firsthand (as reporting): a named OpenAI quote on the release
             tension, and that the immediate reaction split between "opposite of
             open" criticism and support.
Paraphrase:  Reports OpenAI cited potential abuses "generating fake news,
             impersonating people, or automating abusive or spam comments," and
             that "safety and security concerns will reduce our traditional
             publishing in the future." Quotes Jack Clark (OpenAI policy director)
             calling the release decision "a very tough balancing act," with the
             priority "not enabling malicious or abusive uses." Reports critics
             accused OpenAI of "closing off" its research and doing "the opposite
             of open," while some called it "a new bar for ethics." Notes Elon
             Musk said he had not been involved with OpenAI for over a year.
Locators:    Opening (OpenAI's stated concerns); Jack Clark quote mid-article;
             the "opposite of open" reaction and Musk note in the body.
Quote:       Jack Clark (OpenAI): the release decision is "a very tough balancing
             act"; the priority is "not enabling malicious or abusive uses."
             Critics: "the opposite of open."
```

```text
URL:         https://the-decoder.com/from-gpt-2-to-claude-mythos-the-return-of-ai-models-deemed-too-dangerous-to-release/
Kind:        Secondary, independent, recent. The Decoder (Maximilian Schreiner,
             April 8, 2026). Read via WebFetch (HTTP 200). Used only for how the
             GPT-2 "too dangerous" framing is invoked in retrospect and cited now.
Establishes: That the episode is now commonly read as a precedent whose feared
             harms did not materialize, and sometimes as marketing.
Paraphrase:  Characterizes the 2019 decision as controversial at the time — "some
             considered it wise precaution" while "others dismissed it as a PR
             stunt" — and states "the feared harms never materialized" by the time
             the full model shipped in November 2019. Quotes Simon Willison:
             "Saying 'our model is too dangerous to release' is a great way to
             build buzz." (The article's contrast with a later 2026 model is
             outside this lesson's scope and is not used here.)
Locators:    Historical-background section on GPT-2; Willison quote in the body.
Quote:       Simon Willison (via The Decoder): "Saying 'our model is too dangerous
             to release' is a great way to build buzz."
```

## Contradictions

- **"Too dangerous" attribution is genuinely contested.** OpenAI's blog wrote
  "concerns about malicious applications," not "too dangerous." The outlets split
  on whose phrase it was: Slate treats "too dangerous" as its own headline
  framing (not an OpenAI quote), while TechCrunch and The Guardian ("say
  creators") present the danger as OpenAI's stated characterization. So the clean
  version of the angle ("the press invented a phrase OpenAI never endorsed") is
  too strong. The defensible finding: OpenAI did not use the words, but its
  staged-release communications invited the framing, and reputable outlets
  attributed it back to OpenAI. By 2026 the same framing is often read as
  marketing (Simon Willison: "a great way to build buzz"). The writer must state
  this precisely.

- **"No misuse" overstates OpenAI's own finding.** OpenAI reported "minimal
  evidence of misuse," "no clear... large-scale misuse," and "only a small number
  of cases of explicit public plans for misuse" — plus "discussion of misuse" and
  awareness that "several governments have experimented with GPT-2." That is "no
  significant or large-scale misuse found," not "zero misuse." OpenAI also flags
  that nation-state actors are "more difficult to monitor," so its own claim is
  bounded, not absolute.

- **The angle's "far below simple baselines" is not uniform.** It holds for
  summarization (GPT-2 "just barely outperforms selecting 3 random sentences"),
  translation (5 BLEU vs 33.5 BLEU best unsupervised), and QA (4.1%; the smallest
  model does not beat a 1.0% most-common-answer baseline). But on reading
  comprehension the paper calls 55 F1 CoQA "competitive with supervised baselines
  in a zero-shot setting," and Winograd hit 70.7%. The honest claim is
  "task-dependent, and weak-to-rudimentary on most generative downstream tasks,"
  not "below simple baselines on all downstream tasks."

- **The release concern was about generation fluency, not benchmark scores.** The
  paper's downstream weakness and the release worry are not the same axis. The
  worry was that fluent synthetic prose (the "talking unicorns" sample) could mass
  produce plausible text; the weak benchmark numbers measure task accuracy. The
  writer should not use "it scored badly on QA" to rebut "its text was fluent."
  The gap the angle exploits is that fluency was never a measured danger, and the
  follow-up found the projected danger did not materialize — not that the model
  was incompetent at generating text.

- **The independent critique is opinion, sourced but thin.** The named critics
  (Anandkumar on danger; Frederking/Bau on novelty) are real and attributable, but
  the "OpenAI exaggerated for publicity" claim is a characterization, confirmed by
  two independent outlets (Slate, Wikipedia's cited critics) that may share a
  common origin. Present it as attributed criticism, not established fact.

## Numbers

```text
Figure: 117M / 345M / 762M / 1542M parameters (12 / 24 / 36 / 48 layers; d_model 768 / 1024 / 1280 / 1600)
Owner:  GPT-2 paper, Table 2
Scope:  The paper's four model variants. Note the release documents recount these
        as 124M / 355M / 774M / ~1.5B (1558M); the difference is a parameter-count
        convention, not different models. Cite the paper's figures for the paper
        and the report's for the release timeline; do not mix them silently.
```

```text
Figure: WebText: ~45 million outbound Reddit links (>=3 karma) -> "slightly over 8 million documents" -> 40 GB of text; Wikipedia removed; no links after Dec 2017
Owner:  GPT-2 paper, section 2.1
Scope:  The training corpus. 40 GB is text after de-duplication and cleaning.
```

```text
Figure: State of the art on 7 of 8 zero-shot language-modeling datasets (GPT-2 1542M)
Owner:  GPT-2 paper, Table 3 and Abstract
Scope:  Zero-shot, no fine-tuning. The one miss is the One Billion Word Benchmark
        (1BW): GPT-2 42.16 perplexity vs prior SOTA 21.8 (lower is better), which
        the paper attributes to 1BW's sentence-level shuffling.
```

```text
Figure: Zero-shot LM results, GPT-2 1542M vs prior SOTA (Table 3). LAMBADA perplexity 8.63 (SOTA 99.8); LAMBADA accuracy 63.24% (SOTA 59.23%); CBT common-noun 93.30% (SOTA 85.7%); CBT named-entity 89.05% (SOTA 82.3%); WikiText-2 ppl 18.34 (SOTA 39.14); Penn Treebank ppl 35.76 (SOTA 46.54); enwik8 0.93 BPB (SOTA 0.99); text8 0.98 BPC (SOTA 1.08); WikiText-103 ppl 17.48 (SOTA 18.3); 1BW ppl 42.16 (SOTA 21.8)
Owner:  GPT-2 paper, Table 3
Scope:  Zero-shot. Perplexity/BPB/BPC lower is better; accuracy higher is better.
        These are the "strong" numbers the fame overlooks.
```

```text
Figure: Winograd Schema Challenge 70.70% accuracy (improves SOTA by 7%); dataset is only 273 examples
Owner:  GPT-2 paper, section 3.4
Scope:  The paper itself flags the small size and recommends Trichelair et al.
        (2018) to contextualize the result.
```

```text
Figure: Reading comprehension (CoQA) 55 F1, matching or exceeding 3 of 4 baseline systems without the 127,000+ training pairs; supervised BERT SOTA ~89 F1 (= human)
Owner:  GPT-2 paper, section 3.5
Scope:  Zero-shot / greedy decoding on the CoQA dev set. The one downstream task
        the paper calls "competitive with supervised baselines."
```

```text
Figure: Summarization CNN/Daily Mail ROUGE (Table 4): GPT-2 TL;DR R-AVG 21.40 vs Random-3 20.98, Lede-3 31.55, Bottom-Up SOTA 32.75; GPT-2 no-hint 15.03
Owner:  GPT-2 paper, Table 4 / section 3.6
Scope:  "just barely outperforms selecting 3 random sentences"; "only rudimentary
        according to quantitative metrics."
```

```text
Figure: Translation WMT-14 English->French 5 BLEU; French->English 11.5 BLEU; best unsupervised MT 33.5 BLEU
Owner:  GPT-2 paper, section 3.7
Scope:  Zero-shot with in-context example pairs. Far below unsupervised baselines.
```

```text
Figure: Question answering (Natural Questions) 4.1% exact match; smallest model does not exceed a 1.0% most-common-answer baseline; 63.1% on the 1% of questions it is most confident in
Owner:  GPT-2 paper, section 3.8 and Table 5
Scope:  Zero-shot. "much, much, worse than the 30 to 50% range of open domain
        question answering systems."
```

```text
Figure: Staged release timeline — Feb 14 2019 announcement + 124M released; 355M May 2019; 774M Aug 20 2019 (+ first report); 1.5B Nov 5 2019; "delay of nine months"
Owner:  OpenAI report (Nov 2019, arXiv 1908.09203) for the timeline and "nine
        months"; Wikipedia for the Feb 14 / Aug 20 / Nov 5 calendar dates
Scope:  The full staged-release sequence. Feb withheld the full model, not
        everything: the 124M was released the same day.
```

```text
Figure: Synthetic-text detection ~95% accuracy (OpenAI classifier on 1.5B GPT-2 output)
Owner:  OpenAI report (Nov 2019), detection section
Scope:  Evidence cutting against the "dangerous" framing: the output was
        detectable. Detection is easier on longer / lower-temperature samples.
```

## Source assets

```text
Asset: Table 3, "Zero-shot results on many datasets" (GPT-2 paper, p.5)
Shows: The single clearest artifact of the angle — GPT-2's strong numbers are all
       on language-modeling benchmarks (perplexity, bits-per-byte, cloze
       accuracy), SOTA on 7 of 8, with 1BW the lone miss. A reader sees exactly
       what "measured" means.
Crop:  Must retain the SOTA row and the 1542M row and the column headers
       (dataset + metric type). Can omit the 117M/345M/762M rows if space forces
       it, but keeping them shows the log-linear scaling the paper claims.
```

```text
Asset: Table 4, summarization ROUGE (GPT-2 paper, p.6)
Shows: GPT-2 TL;DR sits between Random-3 and Lede-3 — the concrete backing for
       "just barely beats three random sentences." Good counterweight to any
       reader who assumes GPT-2 could already summarize.
Crop:  Retain the GPT-2 TL;DR, Random-3, and Lede-3 rows and the R-AVG column at
       minimum.
```

```text
Asset: Table 5, "30 most confident answers... on Natural Questions" (GPT-2 paper, p.7)
Shows: The texture of 4.1% QA accuracy: even among its most confident answers,
       GPT-2 is wrong on ordinary factoids (e.g. "Largest state in the us by land
       mass? -> California," marked wrong). Makes the weakness legible.
Crop:  A dozen rows including several marked wrong conveys it; keep the
       correct/probability columns.
```

```text
Asset: Figure 1, zero-shot task performance vs model size (GPT-2 paper, p.1)
Shows: The paper's own headline chart: performance rising with model size across
       Reading Comprehension, Translation, Summarization, Question Answering. Note
       the y-axes reach only modest absolute levels for the generative tasks,
       which visually restates the hedge.
Crop:  Keep axis labels and the task panels; the point is the modest ceilings,
       not decoration.
```

```text
Asset: The "talking unicorns" news-article sample (GPT-2 paper, Table 13 area / the model completions tables p.10+)
Shows: The fluent synthetic-text sample that drove the release worry. This is the
       capability the danger framing was about — generation quality — as distinct
       from the weak task benchmarks.
Crop:  A few sentences of the unicorn completion is enough; label it a
       cherry-picked / selected sample, which the paper's caption notes for the
       non-cherry-picked tables and OpenAI's blog notes for this one.
```

```text
Asset: OpenAI report staged-release timeline (Nov 2019 report, Section 1)
Shows: The four-step release sequence and "nine months" in OpenAI's own words —
       useful if the writer wants a plain timeline rather than prose.
Crop:  Prose, not a figure; quote the dated sentences.
```

## Discarded

```text
URL: https://openai.com/index/better-language-models/  — the Feb 14 2019 announcement blog, the primary that owns "Due to our concerns about malicious applications... we are not releasing the trained model." Egress-blocked (openai.com returns HTTP 403 as an organization policy denial, per the proxy status endpoint; not a gated fetch). Its wording is carried here only through two independent secondaries (Wikipedia's verbatim quotation and a WebSearch snippet of OpenAI's own page). Recorded as unresolved: the exact blog text was not read on its own page.
```

```text
URL: https://web.archive.org/... (Wayback copies of the Feb 2019 blog) — blocked from this session (WebFetch reports it cannot fetch web.archive.org; curl returns 403). Could not use to recover the blog primary.
```

```text
URL: https://www.theverge.com/2019/2/14/18224704/... — The Verge's Feb 14 2019 GPT-2 coverage (James Vincent), a strong candidate independent secondary. Blocked from this session (WebFetch cannot fetch theverge.com). Its skeptical framing is instead sourced through Slate, TechCrunch, and Wikipedia.
```

```text
URL: https://www.theguardian.com/technology/2019/feb/14/elon-musk-backed-ai-writes-convincing-news-fiction — The Guardian's Feb 14 2019 article, headlined "New AI fake text generator may be too dangerous to release, say creators," the clearest example of an outlet attributing "too dangerous" to OpenAI. Blocked from this session (WebFetch cannot fetch theguardian.com). Its headline and attribution are carried here only via Wikipedia's citation.
```

```text
URL: https://naokishibuya.github.io/... and https://medium.com/... GPT-2 retrospectives — personal blogs retelling the episode; not independent of OpenAI's own account and add nothing a primary does not. Not read beyond the search snippet; rejected as non-load-bearing.
```
