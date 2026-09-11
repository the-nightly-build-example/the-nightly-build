# Evidence: the-mechanics/hallucinated-packages (01)

The evidence strongly supports the lesson's spine. One peer-reviewed study (Spracklen
et al., USENIX Security 2025) owns the rates and the repeatability finding, with its
data and code published, and its headline numbers are corroborated by the authors' own
repository and by three independent secondary reports that quote the same figures. The
mechanism the lesson turns on is firmly sourced: hallinated package names are not random
noise but recur, and the paper measured exactly how often. The slopsquatting threat model
is well sourced from the security firms that named and popularized it, and there is one
documented real upload of a hallucinated name (huggingface-cli), but it was a harmless
proof-of-concept by a researcher, not a malicious attack.

The record is thin or contested in three places the writer must handle carefully. First,
the single "~20%" headline rate is an average dominated by older open-source models; the
commercial/open-source split is large (5.2% vs 21.7%), and a 2026 re-evaluation finds
frontier-model rates have compressed to roughly 4.6-6.1%. The scary round number is
already dated for the models most readers use. Second, no documented malicious
slopsquatting attack has been observed in the wild as of the sources' dates; the threat
is demonstrated-plausible, not realized. Third, the paper's empirical repeatability
finding is solid, but the deeper causal "why a given fake name is a stable attractor" is
better treated as synthesis built on the existing hallucination lesson than as a
mechanism this paper proves in depth. I read the Spracklen paper through the arXiv HTML
rendering (the USENIX and arXiv PDFs returned as binary/encoded and the USENIX
?login:-online page returned 403); figures cross-checked against the authors' GitHub
README and three secondary reports that quote them identically.

## Sources

```text
URL:         https://arxiv.org/abs/2406.10279
             (HTML read at https://arxiv.org/html/2406.10279v3 ; official publication
             at https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)
Kind:        primary. The paper owns the rates, the detection method, and the
             repeatability measurement firsthand. Peer-reviewed, USENIX Security 2025.
Establishes: How often code-generating LLMs name packages that do not exist, measured
             across 16 models and 576,000 code samples in Python and JavaScript; the
             commercial vs open-source split; and the central repeatability finding.
Paraphrase:  Authors: Joseph Spracklen, Raveen Wijewickrama, A H M Nazmus Sakib, Anindya
             Maiti, Bimal Viswanath, Murtuza Jadliwala (institutions: University of Texas
             at San Antonio, University of Oklahoma, Virginia Tech; per-author affiliation
             mapping not individually verified from the paper header). A "package
             hallucination" is detected mechanically: each package name the model emits in
             generated code is compared against a master list of real package names pulled
             from PyPI and npm as of 10 January 2024; a name not on the list is counted a
             hallucination. 16 models: 3 commercial (GPT-4, GPT-4 Turbo, GPT-3.5 Turbo) and
             13 open-source (CodeLlama variants, DeepSeek, Magicoder, WizardCoder, Mistral,
             Mixtral, OpenChat). 576,000 samples (19,200 per model) from two prompt sets:
             Stack Overflow questions (split recent-2023 vs all-time) and prompts the
             authors generated from the top-5,000 most-downloaded PyPI/npm package
             descriptions. Overall 19.7% of ~2.23 million generated package references were
             hallucinated; 205,474 unique non-existent names. Commercial models hallucinated
             5.2% on average, open-source 21.7% (GPT series ~4x less likely). Python
             hallucinated less than JavaScript (15.8% vs 21.3% on average). Repeatability
             (the lesson's core): 500 prompts that had each produced at least one
             hallucination were re-run 10 times each; 43% of hallucinated packages recurred
             in all 10 runs, 39% did not recur in any of the 10, and 58% recurred in more
             than one of the 10 runs. The authors frame recurrence as persistent and
             model-specific: each model tends to reproduce its own set of invented names
             rather than random one-off noise. Mitigations tested on a DeepSeek 6.7B
             baseline of 16.14%: RAG lowered it to 12.24%, self-refinement to 13.04%,
             fine-tuning to 2.66% (~85% reduction), an ensemble approach to 2.40%; model
             self-detection of its own hallucinations reached 89% precision/recall for
             GPT-4 Turbo, 82% for GPT-3.5, lower for open-source models; hallucination rate
             rose with sampling temperature.
Locators:    Abstract and RQ sections (detection method under the experimental setup;
             rates under the main results; repetition under the persistence/RQ3 section;
             mitigations under the mitigation section). Read via arXiv HTML v3.
Quote:       Detection: "we simply compare each package name to a master list of package
             names acquired from PyPI and npm, respectively (each list is as of 10 January,
             2024). If a package name is not on the master list, it is considered a
             hallucination." Split: "GPT series models were found to be 4 times less likely
             to generate hallucinated packages compared to open-source models, with a
             hallucination rate of 5.2% compared to 21.7%." Repetition: "43% of hallucinated
             packages were repeated in all 10 queries, while 39% did not repeat at all";
             "58% of the time, a hallucinated package is repeated more than once in 10
             iterations."
```

```text
URL:         https://github.com/Spracks/PackageHallucination
Kind:        primary. The authors' own code-and-data repository for the paper; it owns the
             reproduction artifacts and restates the headline figures.
Establishes: That the study's pipeline, prompt datasets, and mitigation implementations are
             public and reproducible; corroborates the headline numbers; and documents a
             deliberate withholding that matters to the threat model.
Paraphrase:  Contains the Python and JavaScript prompt datasets (LLM-generated and Stack
             Overflow categories), the end-to-end generate/extract/detect pipeline, and
             implementations of the RAG, self-detection, and fine-tuning mitigations, plus
             scripts to reproduce the paper's figures. README restates 16 models, 576,000
             samples, 19.7% hallucinated, 205,474 unique names, Python and JavaScript. The
             README states the authors will NOT publicly release the master list of
             hallucinated package names or detailed per-prompt results, citing supply-chain
             attack risk; access requires researcher verification.
Locators:    Repository README and top-level directory listing.
Quote:       None needed beyond the figures above.
```

```text
URL:         https://www.lasso.security/blog/ai-package-hallucinations
Kind:        primary. Bar Lanyado's own writeup of the research he conducted; it owns the
             huggingface-cli experiment and his own rate measurements.
Establishes: An earlier, independent demonstration of the same phenomenon, and the one
             documented case of a hallucinated package name actually being registered.
Paraphrase:  Bar Lanyado (research originally published via Vulcan Cyber; this writeup under
             Lasso Security). Tested four models across 47,803 developer "how-to" questions
             spanning five ecosystems (Python, Node.js, Go, .NET, Ruby). Per-model
             hallucination rates: GPT-4 24.2%, GPT-3.5-Turbo 22.2%, Gemini Pro (Bard) 64.5%,
             Cohere 29.1%. Repetitiveness test: 20 zero-shot hallucinations re-asked 100
             times each; cross-run consistency GPT-4 19.6%, Cohere 24.2%, Gemini 14%, GPT-3.5
             13.6%. Comparing across all four models, 215 hallucinated package names appeared
             in more than one model. The huggingface-cli case: models repeatedly recommended
             `huggingface-cli`, which does not exist (the real CLI installs via
             `pip install -U "huggingface_hub[cli]"`); Lanyado uploaded an EMPTY, HARMLESS
             package under that name as a proof of concept and it received more than 30,000
             authentic downloads in three months; Alibaba's GraphTranslator repository README
             referenced the fake package in its install instructions. Mitigating factors
             noted: Go lacks a central registry and .NET reserves prefixes (Microsoft,
             AWSSDK), raising the bar for registration.
Locators:    Blog body: rates table; "repetitiveness" section; huggingface-cli case study.
Quote:       "In three months the fake and empty package got more than 30k authentic
             downloads!" (wording matters because the package's harmlessness is load-bearing:
             it was a PoC, not an attack).
```

```text
URL:         https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks
Kind:        primary for Socket's own threat analysis and framing; secondary where it repeats
             the academic figures and the coining (it reports those from outside). Author:
             Sarah Gooding, Socket (security firm), 8 April 2025.
Establishes: The slopsquatting threat model as stated by a security firm that works the
             problem, and the attribution chain for the term.
Paraphrase:  Defines slopsquatting as registering a non-existent package name hallucinated by
             an LLM so that a developer guided by an AI assistant installs the attacker's
             package believing it real. Credits the term to Seth Larson (PSF
             Developer-in-Residence) and its popularization to Andrew Nesbitt (Ecosyste.ms).
             Threat model, step by step: LLM emits a plausible fake name embedded in otherwise
             working code; developers trust and copy it; attackers identify commonly
             hallucinated names and pre-register them on PyPI/npm; later installs pull the
             attacker's package. Repeats the study's 19.7%, 5.2% vs 21.7%, 58%, and 205,000+
             unique names. Reports no in-the-wild malicious instance and notes researchers
             deliberately avoided registering names themselves. Mitigation: dependency
             scanning before install.
Locators:    Post body: definition and attribution near the top; threat-model steps mid-post;
             study figures; mitigation near the end.
Quote:       Slopsquatting is registering "a non-existent package name hallucinated by an LLM,
             in hopes that someone, guided by an AI assistant, will copy-paste and install it
             without realizing it's fake."
```

```text
URL:         https://arxiv.org/abs/2605.17062
Kind:        primary. Aleksandr Churilov (independent researcher), "The Range Shrinks, the
             Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026
             Frontier-Model Cohort." Submitted 16 May 2026, last revised 9 August 2026 (v3).
             Read via the arXiv abstract page.
Establishes: That the headline rates are model-era-dependent and have fallen sharply on
             current frontier models, while the underlying registrable-name threat survives.
             This tempers the commission's scary figure without undermining the mechanism.
Paraphrase:  Re-ran a package-hallucination evaluation on a 2026 frontier cohort: Claude
             Sonnet 4.6, Claude Haiku 4.5, GPT-5.4-mini, Gemini 2.5 Pro, DeepSeek V3.2. Rates
             ranged from 4.62% (Claude Haiku 4.5) to 6.10% (GPT-5.4-mini), which the author
             frames as an order-of-magnitude compression of Spracklen's inter-model spread but
             not elimination. Identified 127 package names hallucinated identically across all
             five models, of which 53 remained registrable after existing registry defenses.
Locators:    Abstract.
Quote:       "an order-of-magnitude compression of the inter-model spread observed by
             Spracklen, but not a retirement of the threat." (Read from the abstract; I did
             not read the full method, so treat the 127/53 figures as abstract-level claims
             pending the body.)
```

```text
URL:         https://arxiv.org/abs/2606.13918
Kind:        primary. Lom M. Hillah, Jean-Marc Richard, Ryan Hasnaoui (NewCo Partners, Paris;
             Sorbonne Universite / CNRS / LIP6), "Bayesian-Calibrated Detection of
             Hallucinated Package Imports in AI-Assisted Code." Submitted 11 June 2026. Read
             via the arXiv abstract page.
Establishes: That mitigation is an active research area beyond the original paper, and that a
             plain registry check is not the end of the story: some registered names are still
             suspect. Useful for the "what reduces it / what is still open" part of the lesson.
Paraphrase:  Proposes a Bayesian calibration layer over registry checking that outputs a
             probability per detection rather than a binary flag, using PyPI metadata signals
             (package age, release count, author, summary) to catch suspicious names a strict
             registry check would wave through. Evaluated on 1,734 Python snippets across six
             models. Builds on, not contradicts, the registry-list detection approach.
Locators:    Abstract.
Quote:       None; abstract-level only.
```

```text
URL:         https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/
Kind:        secondary. Reports Lanyado's research from outside.
Establishes: Corroborates the huggingface-cli case and, importantly, carries Lanyado's direct
             statement on the absence of any observed malicious exploitation.
Paraphrase:  Identifies Lanyado as a security researcher at Lasso Security who previously
             published through Vulcan Cyber. Repeats the four-model rates (GPT-4 24.2%, GPT-3.5
             22.2%, Gemini 64.5%, Cohere 29.1%) and repetitiveness figures. States the
             huggingface-cli package received "more than 15,000 authentic downloads in the
             three months" (note: lower than the 30k in Lanyado's own later writeup; see
             Contradictions). Describes persistence as the key that turns a hallucination into
             a usable attack.
Locators:    Article body.
Quote:       Lanyado: "Besides our hallucinated package...I have yet to identify an exploit of
             this attack technique by malicious actors." (Load-bearing for the honest state of
             the threat.) "persistence - the repetition of the fake name - is the key to
             turning AI whimsy into a functional attack."
```

```text
URL:         https://www.csoonline.com/article/3961304/ai-hallucinations-lead-to-new-cyber-threat-slopsquatting.html
Kind:        secondary. Reports the Socket analysis and the academic study from outside.
Establishes: Independent corroboration of the coining attribution and the exact repeatability
             figures, and a clean statement that no in-the-wild case is documented.
Paraphrase:  Attributes "slopsquatting" to Seth Larson, "a security developer-in-residence at
             Python Software Foundation (PSF)." Repeats 16 models, 19.7% / 205,000, 5.2% vs
             21.7%, and states "43% of hallucinations reappeared every time in 10 successive
             re-runs, with 58% of them appearing in more than one run." States plainly that
             neither the Socket analysis nor the research paper mentioned any in-the-wild
             slopsquatting instances.
Locators:    Article body.
Quote:       "neither the Socket analysis nor the research paper mentioned any in-the-wild
             Slopsquatting instances."
```

```text
URL:         https://www.helpnetsecurity.com/2025/04/14/package-hallucination-slopsquatting-malicious-code/
Kind:        secondary. Reports the USENIX study from outside.
Establishes: Independent corroboration of the study's institutions and figures, and the
             developer-side mitigation advice.
Paraphrase:  Names the three institutions (University of Texas at San Antonio, University of
             Oklahoma, Virginia Tech). Repeats 16 models, 576,000 samples, ~20% hallucinated,
             and the 43%/39%/58% repetition figures. Says researchers issued recommendations
             for LLM creators to reduce hallucination; for developers, advises checking
             recommended packages before using the code. Contains no evidence of real-world
             attacks; describes the threat as potential.
Locators:    Article body.
Quote:       "43% of hallucinated packages were repeated in all 10 queries, while 39% did not
             repeat at all."
```

## Contradictions

- No documented malicious attack in the wild. Three sources agree the threat is
  demonstrated but not yet realized. Lanyado (The Register): "I have yet to identify an
  exploit of this attack technique by malicious actors." CSO: neither Socket nor the paper
  cited any in-the-wild instance. Help Net: the threat is potential, not actual. The only
  hallucinated name known to have been registered is Lanyado's own harmless huggingface-cli
  proof of concept. The writer must not imply a live attack campaign exists; the honest
  claim is that the ingredients are all present and one researcher proved the install step
  works.

- The headline rate is era- and model-dependent, and falling. The memorable "~20%" is an
  average pulled up by older open-source models (21.7%) against far lower commercial rates
  (5.2%). Churilov's 2026 re-evaluation puts frontier-model rates at roughly 4.6-6.1%. So
  the figure most likely to be quoted overstates what a reader using a current frontier
  assistant should expect. This does not undermine the lesson: the repeatability mechanism
  and the registrable-names threat both survive in the 2026 work (127 cross-model names, 53
  still registrable). The angle should lead with the mechanism, and treat the rate as a
  point-in-time, model-dependent number.

- huggingface-cli download count differs between sources. Lanyado's own Lasso writeup says
  "more than 30k authentic downloads" in three months; The Register (28 March 2024) says
  "more than 15,000" in the three months it had been available. Most likely a timing
  difference (the Register figure is earlier). The owner's figure is 30k; if the writer uses
  a single number, attribute it to Lanyado/Lasso and consider "tens of thousands."

- Two different "repeatability" measurements must not be conflated. Spracklen's 58%/43%/39%
  are WITHIN a single model: the same prompt re-run 10 times on one model, counting how often
  the same fake name comes back. Lanyado's 13.6-24.2% "repetitiveness" is a different test
  (20 hallucinations re-asked 100 times, per model), and his 215 figure is CROSS-model (a name
  appearing in more than one model). These measure related but distinct things. The lesson's
  core number is Spracklen's within-model recurrence.

- Mild arithmetic tension in the repetition figures, from rounding/framing. "39% did not
  repeat at all" plus "58% repeated more than once" leaves ~3% unaccounted (names that
  appeared in exactly two runs should sit inside the 58%). The three figures (43% all-ten,
  39% none, 58% more-than-once) are reported as separate readings of the same 500-prompt
  rerun set, not a partition that sums to 100. Report them as the paper states them; do not
  present them as a clean breakdown that adds up.

## Numbers

```text
Figure: 19.7% of recommended packages were hallucinated
Owner:  Spracklen et al. (USENIX Security 2025)
Scope:  ~2.23 million package references across 576,000 code samples, 16 models, Python+JS
```

```text
Figure: 5.2% (commercial models) vs 21.7% (open-source models)
Owner:  Spracklen et al.
Scope:  average hallucination rate per model group; GPT series ~4x less likely than open-source
```

```text
Figure: 205,474 unique hallucinated package names
Owner:  Spracklen et al. (repository README confirms)
Scope:  distinct non-existent names observed across the full run
```

```text
Figure: Python 15.8% vs JavaScript 21.3%
Owner:  Spracklen et al.
Scope:  average hallucination rate by language across models
```

```text
Figure: 58% recurred in more than one of 10 runs; 43% in all 10; 39% in none
Owner:  Spracklen et al. (repeatability / RQ)
Scope:  500 prompts that each produced >=1 hallucination, each re-run 10 times
```

```text
Figure: self-detection 89% (GPT-4 Turbo), 82% (GPT-3.5), lower for open-source
Owner:  Spracklen et al. (mitigation)
Scope:  precision/recall for a model flagging its own hallucinated package names
```

```text
Figure: DeepSeek 6.7B baseline 16.14% -> RAG 12.24%, self-refinement 13.04%,
        fine-tuning 2.66% (~85% cut), ensemble 2.40%
Owner:  Spracklen et al. (mitigation)
Scope:  one open-source model; mitigation effect on its hallucination rate
```

```text
Figure: GPT-4 24.2%, GPT-3.5 22.2%, Gemini/Bard 64.5%, Cohere 29.1%
Owner:  Lanyado (Lasso Security)
Scope:  47,803 developer "how-to" questions, 5 ecosystems; independent earlier study
```

```text
Figure: huggingface-cli: >30,000 downloads in 3 months (Lanyado); >15,000 (The Register)
Owner:  Lanyado / Lasso Security (30k); The Register (15k)
Scope:  one harmless PoC package; see Contradictions for the discrepancy
```

```text
Figure: 2026 frontier models 4.62% (Claude Haiku 4.5) to 6.10% (GPT-5.4-mini)
Owner:  Churilov (arXiv 2605.17062, 2026)
Scope:  5 frontier models; 127 names hallucinated across all 5, 53 still registrable
```

## Source assets

```text
Asset: Spracklen et al. per-model hallucination-rate table (16 models, commercial vs
       open-source, by language), in the main results section.
Shows: How wide the spread is and that the scary average is driven by specific open-source
       models. This is the single strongest visual for the rate story.
Crop:  Must retain the commercial/open-source grouping and the language columns. Note:
       house rules (spec/charts.md) require charts be rendered from a committed chart-N.py
       script, not lifted from the paper, so the writer should rebuild this as a chart from
       the figures in Numbers, not screenshot the table.
```

```text
Asset: Spracklen et al. repetition-distribution result (the 43% all-ten / 39% none / 58%
       more-than-once finding), in the persistence/RQ section.
Shows: That recurrence is the rule, not the exception - the load-bearing point of the lesson.
Crop:  Keep the denominator (500 reran prompts, 10 runs each) attached to the percentages.
```

```text
Asset: A built comparison of 2024 rates (5.2% / 21.7%) against 2026 frontier rates
       (4.6-6.1%) from Churilov.
Shows: The range compressing over two model generations while the registrable-name threat
       persists. Would have to be a writer-built chart (two sources), clearly dual-cited.
Crop:  n/a (constructed chart).
```

## Discarded

```text
URL: https://en.wikipedia.org/wiki/Slopsquatting - tertiary; useful as a map but every claim it makes is better sourced from the primaries above.
URL: https://www.usenix.org/publications/loginonline/we-have-package-you-comprehensive-analysis-package-hallucinations-code - returned HTTP 403; could not open, so not cited. Would be a primary (authors' own ;login: piece) if the orchestrator can reach it.
URL: https://www.usenix.org/system/files/usenixsecurity25-spracklen.pdf and https://arxiv.org/pdf/2406.10279 - the official PDFs; both returned as encoded/binary to the fetch tool. Content was read instead via the arXiv HTML rendering (v3) and cross-checked against the authors' GitHub README and three secondaries. The PDF is the canonical artifact; the arXiv abstract URL is recorded as the source's own page.
URL: https://www.infosecurity-magazine.com/news/ai-hallucinations-slopsquatting/ - secondary duplicate of the CSO/Help Net coverage; read far enough to confirm it repeats the same figures and adds no new interpretation.
URL: https://www.mend.io/blog/the-hallucinated-package-attack-slopsquatting/ and https://fossa.com/blog/... and https://www.aikido.dev/blog/... - vendor explainers that restate the primaries; no independent measurement, so not cited to avoid padding.
URL: https://sethmlarson.dev/slop-security-reports - Larson's own blog, but it is about AI-generated vulnerability reports ("slop security reports"), a different topic; it is not his definition of slopsquatting. The coining attribution therefore rests on the security-firm and press reporting above, which is consistent across sources.
```
