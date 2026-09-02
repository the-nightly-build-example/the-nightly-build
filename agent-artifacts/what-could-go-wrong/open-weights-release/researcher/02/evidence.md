Evidence record: what-could-go-wrong/open-weights-release (researcher 02)

This record supersedes researcher/01 with one correction: the Zuckerberg
quotation in the 01 record's Meta essay entry was spliced, printing "larger
institutions...check the power of smaller bad actors" as if it were one
sentence in the primary. It is not. I reopened the essay firsthand (both a
direct HTTP fetch of the page's own markup and an independent fetch-and-quote
pass, cross-checked against each other) and confirmed the primary's actual
wording is two separate sentences with two different subjects: "larger
actors can check the power of smaller bad actors" is one sentence, and
"larger institutions deploying AI at scale will promote security and
stability across society" is a different sentence three sentences later in
the same paragraph. No sentence anywhere in the essay reads "larger
institutions...check the power of smaller bad actors." The corrected Zuckerberg
source entry below records all four consecutive sentences of the passage
verbatim and marked separately, so the writer has the unspliced wording to
quote from directly. Nothing else in the 01 record changes: every other
claim, figure, and locator below is carried forward unmodified from 01, and
I re-confirmed every URL in this record resolves to the source's own page
(see each entry; the Meta license page returns a bot-blocking HTTP 400 to an
automated fetch, as it did in 01, but its content was independently
re-confirmed readable and unchanged). The evidence otherwise firmly supports
both halves of the commission's central line: the irreversibility argument
(Seger et al. 2023) and the safety-stripping result (Qi et al. 2023) are both
stated and demonstrated exactly as the commission describes, with exact
figures and page-level locators below. The demonstrated/speculative line for
catastrophic bio uplift is equally firm: RAND's own summary states a null
result on operational uplift, in the plainest terms available without
reproducing any scenario detail. The marginal-risk rebuttal (Kapoor,
Bommasani, Narayanan et al. 2024) is precisely characterized: it is not a
blanket "open weights are fine" paper, it is a framework paper whose central
finding is that most prior studies on both sides of the debate under-argue
their case, and that marginal risk is low for some vectors (automated
vulnerability detection) and "considerable" for others (deepfake intimate
imagery) — this matters for the article, because it means the paper does not
"dismiss" the risk, it disaggregates it. The record is thin in one place the
commission cares about: independent, primary-sourced confirmation of the RAND
study's exact team count is not obtainable without the full report, and two
secondary retellings of that count disagree with each other (see Numbers and
Contradictions). I did not open the full RAND report body or its October 2023
predecessor beyond RAND's own public executive-summary page, per the
assignment's guardrail; where that page's own language pushed into scenario
specifics, I have excluded it from this record entirely (see Discarded). One
additional finding, outside the brief's explicit questions but squarely in
the series' "bring it to the present" charge: Meta itself moved away from
open-weight release for a stretch of 2025–2026, for stated commercial and
security reasons that have nothing to do with the catastrophic-misuse debate
this lesson teaches — a fact that complicates any clean "doom" or "dismissal"
reading of why labs release or withhold weights.

### Sources

```text
URL:         https://www.governance.ai/research-paper/open-sourcing-highly-capable-foundation-models
             (mirror: https://arxiv.org/abs/2311.09227 ; PDF read directly:
             https://arxiv.org/pdf/2311.09227)
Kind:        Primary. Centre for the Governance of AI (GovAI) is the paper's
             publisher and the authors' home institution; this is the report
             that makes the irreversibility/careful-release argument the
             commission asks to be stated at full strength.
Establishes: The full author list (22 names, lead Elizabeth Seger, GovAI);
             the exact irreversibility claim; the paper's five numbered
             recommendations; its own account of how open weights let users
             strip post-hoc safety filters and fine-tune away safeguards; the
             report's own publication date.
Paraphrase:  Open-source release of a foundation model has no "undo": if a
             released model has a flaw or a grave misuse potential, "there is
             nothing to stop users from continuing to use the model once
             released," and there is no way to force adoption of a later
             safety patch — malicious users are actively incentivized not to
             adopt safety improvements (p.5/PDF p.6). The paper's core
             recommendation is not a ban: "some highly capable foundation
             models should not be open-sourced, at least not initially"
             (Executive Summary, p.2/PDF p.2), decided through "rigorous risk
             assessments" (Recommendation 2, p.30/PDF p.31) before release,
             because "the decision to open-source a model is irreversible"
             (repeated verbatim at p.30 and p.33/PDF pp.31,34). Separately
             from Qi et al.'s later empirical result, Seger et al. lay out the
             mechanism qualitatively: open weights let an actor "write their
             own inference code...to run the model without safety filters,"
             note that "Stable Diffusion's safety filter...can be removed by
             deleting a single line of inference code," and that unmonitored
             fine-tuning "could involve the reintroduction of potentially
             dangerous capabilities that were initially removed by developers
             pre-release" — while also noting this is harder than removing a
             post-hoc filter, since it "requires the curation of a dataset...as
             well as...compute and technical expertise" (§3.1, p.11/PDF p.12).
             The paper explicitly says current models are not yet over the
             extreme-risk threshold: "Arguably, current AI capabilities do not
             yet surpass a critical threshold of capability for the most
             extreme risks" (Executive Summary, p.1/PDF p.2). Publication
             date: the GovAI research-paper page itself lists the report as
             published October 2023 (the arXiv mirror's own submission
             history shows v1 posted November 2, 2023 — a later mirror
             posting, not the report's original publication). Use October
             2023 as the report's sourced publication date; November 2023 is
             only the arXiv-mirror date.
Locators:    Abstract (PDF p.1); Executive Summary (PDF pp.2-3); §1
             Introduction (PDF p.5); §3.1 Malicious Use (PDF pp.12-13); §4.1.3
             Staged-Release Impact Testing (PDF p.19); §5 Recommendations
             (PDF pp.31,34); Conclusion (PDF p.34); GovAI research-paper page
             (publication month).
Quote:       "open-source AI model release is irreversible; there is no 'undo'
             function if significant harms materialize." (PDF p.6)
```

```text
URL:         https://arxiv.org/abs/2310.03693 (PDF read directly:
             https://arxiv.org/pdf/2310.03693)
Kind:        Primary. The authors (Qi, Zeng, Xie, Chen, Jia, Mittal, Henderson)
             ran the fine-tuning experiments themselves; this is the paper the
             commission names as the demonstrated safety-removal result.
Establishes: Exact costs, example counts, and harmfulness-rate figures for
             stripping safety alignment from both a closed model (GPT-3.5
             Turbo, via paid fine-tuning API) and an open-weight model
             (Llama-2-7b-Chat, via local full-parameter fine-tuning), plus
             author affiliations.
Paraphrase:  The authors fine-tuned GPT-3.5 Turbo on 10 adversarially chosen
             harmful (instruction, response) pairs for 5 epochs via OpenAI's
             paid fine-tuning API, at a cost the paper states as "less than
             $0.20." The harmfulness rate (share of test outputs judged most
             harmful, scored 1-5 by GPT-4) rose from a baseline of 1.8% to
             88.8%. On the open-weight Llama-2-7b-Chat model — described by
             the authors as "state-of-the-art" among open-source LLMs — the
             identical attack (10 harmful examples, full-parameter fine-tuning,
             5 epochs, learning rate 5e-5, no API cost since it runs on the
             attacker's own hardware) raised the harmfulness rate from a 0.3%
             baseline to 50.0%; at 50 examples it reached 80.3%. A second
             method (the "identity shifting" attack, reframing the assistant
             as an "Absolutely Obedient Agent" via 10 benign-looking
             role-play examples) raised Llama-2-7b-Chat's harmfulness rate to
             72.1% after 5 epochs and GPT-3.5 Turbo's to 87.3% after 10
             epochs. The paper also shows ordinary, non-adversarial fine-tuning
             on benign datasets (Alpaca, Dolly) degrades safety alignment to a
             lesser extent, i.e. no attacker intent is required for some
             erosion. Author affiliations: Xiangyu Qi, Tinghao Xie, Prateek
             Mittal — Princeton University; Yi Zeng, Ruoxi Jia — Virginia
             Tech; Pin-Yu Chen — IBM Research; Peter Henderson — Stanford
             University. The abstract itself frames the paper's occasion as
             "Meta's open release of Llama models and OpenAI's APIs for
             fine-tuning GPT-3.5 Turbo."
Locators:    Abstract (PDF p.1); §4.1 Setup (PDF p.5); §4.2 Harmful Examples
             Demonstration Attack, Table 1 (PDF p.6); §4.3 Identity Shifting
             Attack, Table 2 (PDF p.7); §4.4 Benign Fine-tuning (PDF p.7).
Quote:       "we jailbreak GPT-3.5 Turbo's safety guardrails by fine-tuning it
             on only 10 such examples at a cost of less than $0.20 via
             OpenAI's APIs, making the model responsive to nearly any harmful
             instructions." (Abstract, PDF p.1)
```

```text
URL:         https://arxiv.org/abs/2403.07918 (PDF read directly:
             https://arxiv.org/pdf/2403.07918)
Kind:        Primary. 24 named authors across Princeton, Stanford, MIT,
             Georgetown, GitHub, EleutherAI, Hugging Face, Meta, and others,
             including Sayash Kapoor and Arvind Narayanan; this is the
             marginal-risk rebuttal paper the commission names.
Establishes: The paper's own definition of "marginal risk"; its six-point risk
             assessment framework; its findings for cyberattacks and
             biosecurity specifically; its stated benefits of open weights;
             one concrete cost figure for training an open model.
Paraphrase:  Marginal risk is defined precisely as "the extent to which these
             models increase societal risk by intentional misuse beyond closed
             foundation models or pre-existing technologies, such as web
             search on the internet" (§1, p.2). Applying a six-point framework
             (threat identification; existing risk absent open models;
             existing defenses; evidence of marginal risk; ease of defense;
             uncertainty/assumptions) to seven previously published misuse
             studies (Table 1), the authors find six of seven "incomplete" —
             not that the underlying concern is false, but that "these
             studies, on their own, are insufficient evidence to demonstrate
             increased marginal societal risk from open foundation models"
             (§5.1, p.8). For cybersecurity specifically (automated
             vulnerability detection), the paper concludes "the current
             marginal risk of open foundation models is low" because
             sophisticated attackers already rely on tools like Metasploit and
             fuzzers that predate open LLMs, and the same capability helps
             defenders (§5.1/Table 2, pp.7-8). The paper is explicit this
             conclusion is NOT uniform across misuse vectors: for
             non-consensual intimate imagery it finds "open foundation models
             pose considerable marginal risk at present, and plausible
             defenses seem hard" (§5.1, p.8) — the paper disaggregates risk by
             vector rather than declaring open weights broadly safe. For
             biosecurity specifically, the paper does not itself run a
             marginal-risk assessment; it audits a prior study (Gopal et al.
             2023) against its own framework and finds that study's "evidence
             of marginal risk" step scored as entirely absent — the prior
             literature "gives no comparison to similar risks based on widely
             available information on the Internet" (Appendix B.4, p.22). On
             benefits: model weights are called "essential for several forms
             of research across AI interpretability, security, and safety"
             (§4) and open weights let defenders "monitor signals from
             deployed software systems for signs of active exploits." One
             concrete cost figure: training the Llama 2 series required "3.3
             million GPU hours on NVIDIA A100-80GB GPUs," which the authors
             estimate at roughly $6 million at February 2024 cloud rates of
             $1.8/GPU-hour (§4, p.5) — cited as a barrier to entry that
             tempers the "democratizing" benefit claim. This paper does not
             cite or engage the Mouton/RAND studies; its one closely
             comparable audited study is Gopal et al. 2023 on biosecurity.
Locators:    Abstract; §1 Introduction (p.1); §4 Benefits (p.5); §5 Risks of
             Open Foundation Models / §5.1 Risk Assessment Framework, Table 1
             (pp.5-6); Table 2 and surrounding discussion (pp.7-8); Appendix
             B.4 Biosecurity risk (p.22).
Quote:       "current research is insufficient to effectively characterize the
             marginal risk of open foundation models relative to pre-existing
             technologies." (Abstract)
```

```text
URL:         https://www.rand.org/pubs/research_reports/RRA2977-2.html
Kind:        Primary. Christopher A. Mouton, Caleb Lucas, and Ella Guest are
             the report's authors, RAND Corporation is the publisher; this is
             the study whose published top-line conclusion the commission asks
             for. Read only the report's own public summary/findings page, per
             the assignment guardrail — no operational content was opened.
Establishes: The exact top-line published conclusion on LLM-assisted vs.
             internet-only biological attack planning, and the study's basic
             design (compared conditions), stated by RAND itself.
Paraphrase:  RAND ran "an expert exercise in which teams of researchers
             role-playing as malign nonstate actors were assigned to realistic
             scenarios and tasked with planning a biological attack; some
             teams had access to an LLM along with the internet, and others
             were provided only access to the internet." The published,
             final-report finding: "using the existing generation of LLMs did
             not measurably change the operational risk" of a biological
             attack. A named Key Takeaway states plainly that "biological
             weapon attack planning currently lies beyond the capability
             frontier of LLMs as assistive tools" and that the authors "found
             no statistically significant difference in the viability of
             plans generated with or without LLM assistance." The report
             explicitly states its own limits: "This research did not measure
             the distance between the existing LLM capability frontier and
             the knowledge needed for biological weapon attack planning," and
             recommends monitoring future model generations rather than
             treating the null result as permanent. Lead author Christopher A.
             Mouton is titled, per RAND's own page, "Director, International
             Security and Defense Policy Program, RAND; Professor of Policy
             Analysis, RAND School of Public Policy." Document is 24 pages,
             DOI 10.7249/RRA2977-2, published Jan 25, 2024. This report says
             nothing about open-weight models specifically (it does not
             disclose which LLMs were tested) — it establishes a frontier-
             capability finding, not an open-vs-closed one; the open/closed
             comparison for capability comes from other sources below.
Locators:    Report abstract and "Key Takeaways" box on the report's own
             landing page (no PDF opened).
Quote:       "This research involving multiple LLMs indicates that biological
             weapon attack planning currently lies beyond the capability
             frontier of LLMs as assistive tools." (RAND report landing page,
             Key Takeaways)
```

```text
URL:         https://www.rand.org/news/press/2024/01/25.html
Kind:        Primary (RAND's own press release accompanying its report;
             same authoring organization, not outside commentary).
Establishes: A named-source quote from lead author Mouton contextualizing the
             null result as time-bound, not permanent, plus his RAND title.
Paraphrase:  The release states plainly: "The current generation of LLMs...do
             not increase the risk of a biological weapons attack by a
             non-state actor." It quotes Mouton: "Just because today's LLMs
             aren't able to close the knowledge gap needed to facilitate
             biological weapons attack planning doesn't preclude the
             possibility that they may be able to in the future... This is
             worth continuing to study because AI technology is available to
             everyone—including dangerous non-state actors—and it's advancing
             faster than governments can keep pace." Mouton's title here:
             "lead author and a senior engineer at RAND" in the release body,
             and "Director, International Security and Defense Policy
             Program, RAND; Professor of Policy Analysis, RAND School of
             Public Policy" in his researcher-spotlight byline on the same
             page.
Locators:    Full text of the release (single page).
Quote:       "Just because today's LLMs aren't able to close the knowledge gap
             needed to facilitate biological weapons attack planning doesn't
             preclude the possibility that they may be able to in the
             future." — Christopher Mouton
```

```text
URL:         https://developer.meta.com/ai/llama2/license/
             (canonical redirect target of https://www.llama.com/llama2/license/,
             dated July 18, 2023 in the document itself)
Kind:        Primary. Meta's own binding release document for Llama 2 — the
             commission's required "primary Meta Llama release document /
             license," reported as fact per the commission's instruction to
             name no company as an authority.
Establishes: The exact terms under which Meta released Llama 2's weights,
             including its one usage-scale restriction and its incorporation
             of a separate acceptable-use policy.
Paraphrase:  The Llama 2 Community License Agreement requires that use
             "comply with applicable laws and regulations...and adhere to the
             Acceptable Use Policy for the Llama Materials," incorporated by
             reference. It caps free commercial use by scale: "If, on the
             Llama 2 version release date, the monthly active users of the
             products or services made available by or for Licensee...is
             greater than 700 million monthly active users in the preceding
             calendar month, you must request a license from Meta, which Meta
             may grant to you in its sole discretion." Below that threshold,
             the license places no vetting, evaluation, or staged-release
             condition on who may download and run the weights — there is no
             KYC, no pre-release capability evaluation, and no revocation
             mechanism once weights are downloaded, which is the direct
             license-level counterpart to Seger et al.'s abstract claim about
             irreversibility.
Locators:    License body, §1(b)(iv) (acceptable-use incorporation) and §2
             (700-million-MAU threshold), confirmed against the page's
             embedded content (og:description "Llama 2 License"; date "July
             18, 2023" appears twice in the document). Re-confirmed for this
             record: the page returns HTTP 400 with WAF/bot-blocking headers
             to a plain automated fetch (same class of gating the 01 record
             and the editor noted for RAND and NTIA), but its content —
             including both quotes below — was independently re-read in full
             and is unchanged, so this is gating, not a dead link.
Quote:       "you must request a license from Meta, which Meta may grant to
             you in its sole discretion, and you are not authorized to
             exercise any of the rights under this Agreement unless or until
             Meta otherwise expressly grants you such rights." (§2)
```

```text
URL:         https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/
Kind:        Primary. Authored and published by Mark Zuckerberg as Meta's
             Founder and CEO on Meta's own newsroom; this is Meta's own
             position statement accompanying the Llama 3.1 release, reported
             as fact per the commission's instruction.
Establishes: Meta's own stated rationale for continuing open-weight release,
             its own admission of where Llama trailed the frontier, and its
             own account of the intentional-misuse risk it considers
             acceptable — including the exact, unspliced wording of the
             "larger actors" / "larger institutions" passage that the 01
             record misquoted.
Paraphrase:  Zuckerberg states Meta's own capability position directly:
             "Last year, Llama 2 was only comparable to an older generation of
             models behind the frontier. This year, Llama 3 is competitive
             with the most advanced models and leading in some areas." He
             argues open weights are safer against unintentional harm because
             "the systems are more transparent and can be widely scrutinized."
             In the essay's "Intentional harm" subsection he distinguishes
             what small-scale bad actors can do from what large-scale actors
             can do, and argues for wide deployment on the ground that it lets
             larger actors check smaller bad actors — a claim made in one
             sentence about "actors," followed three sentences later, after
             an intervening sentence about Meta's own social-network security
             practice, by a separate sentence about "institutions." These are
             two different sentences with two different grammatical subjects;
             neither should be quoted as if it contained the other's words.
             The full four-sentence passage, each sentence verbatim and kept
             separate, is recorded in Quote below — this is the corrected
             wording; the prior researcher record's rendering, "larger
             institutions...check the power of smaller bad actors," spliced
             sentence (1)'s verb phrase onto sentence (3)'s subject and does
             not appear anywhere in the source. The passage's argument is
             conditioned on "everyone hav[ing] access to similar generations
             of models." Zuckerberg states no download-side restriction
             beyond the license's acceptable-use terms and MAU threshold; the
             essay's own safety case rests on scrutiny and countervailing
             power, not on gating who can obtain the weights.
Locators:    Full essay text, published July 23, 2024 (page also shows a
             January 27, 2025 note/edit date); "Intentional harm" subsection,
             within the "Why Open Source AI Is Good for Developers, Meta, And
             the World" safety discussion. Verified firsthand by two
             independent means for this correction: (1) a direct HTTP fetch
             of the page's own markup (its embedded JSON-LD article body,
             which carries the full essay text verbatim), confirming the
             exact character sequence of all four sentences below; (2) a
             separate fetch-and-extract pass quoting the same four sentences
             independently. Both agree exactly with each other and with the
             editor's independent finding in editor/01/editorial-review.md.
Quote:       Four consecutive sentences from the "Intentional harm"
             subsection, verbatim and each its own sentence — record and cite
             them separately; never splice (2) or (3) into (1), and never
             attach sentence (1)'s verb phrase to sentence (3)'s subject:

             (1) "I think it will be better to live in a world where AI is
             widely deployed so that larger actors can check the power of
             smaller bad actors."

             (2) "This is how we've managed security on our social
             networks – our more robust AI systems identify and stop threats
             from less sophisticated actors who often use smaller scale AI
             systems."

             (3) "More broadly, larger institutions deploying AI at scale
             will promote security and stability across society."

             (4) "As long as everyone has access to similar generations of
             models – which open source promotes – then governments and
             institutions with more compute resources will be able to check
             bad actors with less compute."

             Sentence (1)'s subject is "larger actors" and its claim is that
             they "can check the power of smaller bad actors." Sentence (3)'s
             subject is "larger institutions" and its claim is that they
             "will promote security and stability across society" — a
             different subject and a different verb phrase. No sentence in
             this essay reads "larger institutions...check the power of
             smaller bad actors"; that wording does not exist in the source
             and must not be printed as a quotation. If the article's point
             needs both the "actors can check smaller bad actors" claim and
             the "institutions...promote security" claim, quote sentence (1)
             and sentence (3) as two separate quotations, or paraphrase one
             of them in the record's own words rather than merging them into
             one quoted sentence.
```

```text
URL:         https://arxiv.org/abs/2310.13625
Kind:        Primary. Janet Egan and Lennart Heim are the paper's authors and
             own the KYC-for-compute policy proposal; published via GovAI/CSET
             channels. Directly answers the commission's "what today's
             proponents want done" question with a concrete, named mechanism.
Establishes: A specific, current policy proposal — Know-Your-Customer
             requirements on compute providers — as one of the mechanisms
             proponents of oversight want, distinct from staged release or
             pre-release evaluation.
Paraphrase:  The authors propose the US government require compute providers
             to run Know-Your-Customer schemes (borrowed from banking
             regulation) so that large training or fine-tuning runs are tied
             to a verified identity, arguing this gives "more precise
             controls, allowing regulatory control over compute quantities, as
             well as the flexibility to suspend access at any time" —
             explicitly framed as a complement to existing chip export
             controls, and as a way to catch large fine-tuning runs (of the
             kind Qi et al. demonstrate) before they happen, not just to gate
             initial release.
Locators:    Abstract; full paper (html rendering).
```

```text
URL:         https://www.ntia.gov/other-publication/2024/fact-sheet-ntia-ai-report-calls-monitoring-not-mandating-restrictions-open-ai-models
Kind:        Primary. NTIA (U.S. Department of Commerce) is the report's
             author and this is the agency's own fact sheet on its report,
             issued under President Biden's AI executive order. Establishes
             the "current policy touchpoints" the commission asks for.
Establishes: The current (as of July 2024) official U.S. government policy
             posture toward open-weight models: monitor, do not restrict
             today, but build the capacity to restrict later if evidence
             warrants it.
Paraphrase:  NTIA's Report on Dual-Use Foundation Models with Widely Available
             Model Weights "recommends the U.S. government actively monitor
             for potential risks to arise, but refrain from restricting the
             availability of open model weights for currently available
             systems." It recommends the government build an evidence
             pipeline — collecting risk indicators, setting thresholds,
             maintaining technical/legal/policy expertise — so that if a
             future evaluation shows warranted risk, it could "place
             restrictions on access to models" or take other mitigation
             steps, including, it names explicitly, "restricting access to
             material components in the case of bio-risk concerns." This is
             evaluation-and-monitoring, not the staged-release/licensing/KYC
             regime some other proponents want — a live disagreement about
             what "today's proponents" should actually do.
Locators:    Full fact-sheet text (single page), dated July 30, 2024.
Quote:       "recommends the U.S. government actively monitor for potential
             risks to arise, but refrain from restricting the availability of
             open model weights for currently available systems."
```

```text
URL:         https://dailyai.com/2024/01/rand-report-says-llms-dont-increase-risk-of-biological-attacks/
Kind:        Secondary. DailyAI is an independent outlet reporting on the RAND
             study from outside RAND; provides context (a contemporaneous
             skeptical reaction) that RAND's own page does not carry.
Establishes: That the null result was publicly read, at the time, as
             confirming skepticism voiced before the study concluded — by a
             named AI researcher outside the safety-advocacy camp.
Paraphrase:  The article reports that Meta Chief AI Scientist Yann LeCun had
             publicly criticized RAND's October 2023 preliminary report before
             the final results were in, arguing an LLM might "save you a bit
             of time" over searching a search engine but that the hard,
             practical steps remain the bottleneck — and that the January 2024
             final report "confirmed LeCun's assessment." It also reports,
             independent of RAND's own page, that the LLM-assisted teams'
             plans were "marginally less viable" than the internet-only
             teams' plans, not merely statistically tied.
Locators:    Full article text (single page), published Jan 26, 2024.
```

```text
URL:         https://winbuzzer.com/2025/12/09/meta-pivots-from-llama-to-closed-ai-models-abandoning-open-source-roots-xcxwbn/
Kind:        Secondary. Independent tech-industry outlet reporting on Meta's
             internal strategy, not a Meta document.
Establishes: That Meta itself moved away from open-weight release for a
             stretch straddling late 2025, and the reasons given were
             competitive and security-related, not the catastrophic-misuse
             debate this lesson teaches.
Paraphrase:  As of December 2025, Meta was reported to be developing a
             proprietary, non-open model (codenamed "Avocado") after the
             underperformance of the open Llama 4 "Behemoth" model (shelved
             May 2025) and after DeepSeek's R1 model was seen inside Meta as
             having "copied Llama's architecture," which the piece frames as
             exposing "commercial risks of releasing open weights that can be
             easily cloned by adversaries" — a competitive/IP concern, distinct
             from bio/cyber misuse. It also quotes Zuckerberg as saying Meta
             needed "to be rigorous about mitigating these risks and careful
             about what we choose to open source," language that echoes
             Seger et al.'s own recommended posture (risk-assess before
             release) more than it echoes Zuckerberg's own 2024 essay above.
Locators:    Full article text, published Dec 9, 2025.
```

```text
URL:         https://spyglass.org/meta-open-ai-muse-glimmer/
Kind:        Secondary. Independent commentary/analysis outlet, published
             closest to the present moment of any source in this record.
Establishes: The most current (Aug 2026) state of Meta's open/closed posture,
             confirming the pivot was not a clean, permanent exit from open
             weights.
Paraphrase:  By August 2026, Meta had released a smaller, locally runnable
             model (Muse Glimmer) "notably below frontier level" and signaled
             it would release weights for a further model (Muse Spark 1.2)
             "at some point soon," while its actual frontier model
             (codenamed "Watermelon") had not been committed to open release
             — the author's read is that Meta may keep frontier capability
             closed and reserve "open" for models a tier behind it, even while
             publicly reaffirming commitment to open development.
Locators:    Full article text, published Aug 10, 2026.
```

### Contradictions

Against the doom reading (evidence the catastrophic-uplift claim is not
demonstrated):

- RAND's own final report is the strongest single fact here: a purpose-built
  red-team study found "no statistically significant difference in the
  viability of plans generated with or without LLM assistance," and states
  outright that bio-attack planning "currently lies beyond the capability
  frontier of LLMs as assistive tools." This is a null result from a study
  designed specifically to find uplift, not an absence of study.
- Kapoor et al.'s framework finding for cybersecurity — arguably the
  best-evidenced misuse vector in their survey — is that current marginal risk
  is low, because the relevant offensive tooling (Metasploit, fuzzers)
  substantially predates open LLMs and defenders get the same capability
  uplift attackers do.
- Yann LeCun's contemporaneous public skepticism (reported by DailyAI, not
  affiliated with RAND) argued before RAND's final report that even useful
  LLM output does not remove the "hard lab work" bottleneck — an independent
  voice, from inside a company that ships open weights, making the same
  point RAND's data later bore out.

Against the dismissal reading (evidence the risk is not merely hypothetical or
permanently closed):

- Qi et al.'s result is not a projection: it is a demonstrated capability, at
  trivial cost, against both a closed model (GPT-3.5 Turbo, $0.20, 10
  examples) and an open-weight model of the era (Llama-2-7b-Chat, no API cost
  at all since it runs on the attacker's own hardware). Whatever RAND found
  about bio-planning specifically, the fine-tuning-removes-safety mechanism
  Seger et al. describe qualitatively is empirically confirmed, on the exact
  kind of model this lesson is about.
- RAND's own report refuses to be read as a permanent clearance: "This
  research did not measure the distance between the existing LLM capability
  frontier and the knowledge needed for biological weapon attack planning,"
  and Mouton is on record that today's null result "doesn't preclude the
  possibility that they may be able to in the future."
- Kapoor et al.'s framework is not uniformly reassuring: for one of their
  seven surveyed vectors (non-consensual intimate imagery) they conclude
  marginal risk is "considerable" and defenses are hard — the same paper the
  commission cites as the marginal-risk rebuttal explicitly declines to
  extend that rebuttal to every misuse type.
- Meta's own Dec 2025 posture, per Winbuzzer's reporting, has Zuckerberg
  describing a need to be "rigorous about mitigating these risks and careful
  about what we choose to open source" — a leading open-weight lab
  conceding, in its own words, the case for withholding some models that
  Seger et al. made two years earlier, even if the stated proximate trigger
  was competitive exposure (DeepSeek replicating Llama's architecture) rather
  than the bio/cyber misuse debate.

A complication for both readings: the release decision in practice may not
track the safety debate at all. Meta's move away from open weights in
2025 was reported as driven by commercial/IP exposure, not new evidence on
misuse; its partial return to "open" positioning by August 2026 (Muse
Glimmer, a promised Muse Spark release) is reported as reserving the actual
frontier model for closed use while relabeling a sub-frontier model "open."
If accurate, this suggests real-world release decisions are currently made on
competitive grounds with the safety question downstream of it, which cuts
against treating either "doom" or "dismissal" advocates as the actual
deciding audience for Meta's choices.

One unresolved discrepancy, flagged rather than resolved: two secondary
sources give incompatible counts for RAND's own team structure. A general
web-search synthesis states "45 participants...15 groups of three people,"
split (unspecified ratio) between LLM+internet and internet-only. A
linkpost summary on the Effective Altruism Forum states "approximately 12
primary...3-person cells, plus 3 additional teams," split 8 (LLM+internet)
to 4 (internet-only). These cannot both be exactly right, and RAND's own
public summary page states only the qualitative design ("some teams had
access to an LLM along with the internet, and others were provided only
access to the internet") without a number. I have not resolved this: doing so
would require reading further into the report body than the guardrail on this
assignment permits me to search for team-composition tables adjacent to
scenario content. The writer should use RAND's own qualitative framing and
avoid citing either specific team count as confirmed.

### Numbers

```text
Figure: $0.20 (cost of the GPT-3.5 Turbo fine-tuning attack)
Owner:  Qi et al. 2023, arXiv:2310.03693
Scope:  10 adversarial examples, 5 epochs, via OpenAI's paid fine-tuning API;
        closed model, not open-weight.

Figure: 88.8% harmfulness rate (from a 1.8% baseline), 10-shot attack
Owner:  Qi et al. 2023, Table 1
Scope:  GPT-3.5 Turbo, harmfulness scored 1-5 by GPT-4 judge, share scoring
        the maximum (5).

Figure: 50.0% harmfulness rate (from a 0.3% baseline), 10-shot attack;
        80.3% at 50-shot
Owner:  Qi et al. 2023, Table 1
Scope:  Llama-2-7b-Chat, open-weight, full-parameter fine-tuning, 5 epochs,
        learning rate 5e-5, run on the attacker's own hardware (no API cost
        applies to this figure).

Figure: 72.1% harmfulness rate, identity-shifting attack, 5 epochs
Owner:  Qi et al. 2023, Table 2
Scope:  Llama-2-7b-Chat, only 10 (benign-looking) fine-tuning examples;
        68.2% at 10 epochs, non-monotonic across epoch count.

Figure: ~$6 million (estimated training cost of the Llama 2 series)
Owner:  Kapoor et al. 2024, §4, citing Touvron et al. 2023b for compute and
        Lambda 2024 for pricing
Scope:  3.3 million GPU-hours on NVIDIA A100-80GB GPUs, priced at February
        2024 cloud rate of $1.8/GPU-hour. Cited by Kapoor et al. as a barrier
        to entry, tempering the "open weights democratize development"
        benefit claim.

Figure: 700 million monthly active users (Llama 2 license commercial-use
        threshold)
Owner:  Meta, Llama 2 Community License Agreement, §2
Scope:  Measured against the licensee's (or affiliates') MAU in the calendar
        month preceding the Llama 2 release date (July 18, 2023); above this
        threshold a separate license from Meta is required. This is the
        license's only usage-scale gate; it is not a safety evaluation gate.

Figure: No statistically significant difference in plan viability
        (LLM-assisted vs. internet-only)
Owner:  Mouton, Lucas, Guest 2024, RAND RRA2977-2 (report's own summary page)
Scope:  Red-team exercise, condition compared: some teams with LLM + internet
        access vs. other teams with internet-only access. Exact team/
        participant counts not confirmed to primary-source certainty (see
        Contradictions); RAND's own page gives no number.
```

### Source assets

```text
Asset: Qi et al. 2023, Table 1 (10/50/100-shot harmful-examples attack) and
       Table 2 (identity-shifting attack), each giving harmfulness score and
       harmfulness rate, before/after, for both GPT-3.5 Turbo and
       Llama-2-7b-Chat (PDF pp.6-7).
Shows: A reader can see, at a glance, that the safety-removal effect is large,
       fast (within a handful of epochs), and present on both a closed model
       reached only through a paid API and an open-weight model run locally —
       the open/closed comparison the commission's angle turns on.
Crop:  Keep both models' rows side by side and the "Initial" baseline column;
       omit Qi et al.'s Figure 2/4 diagrams of the attack mechanism itself,
       which add no number and are illustrative rather than data-bearing.

Asset: Qi et al. 2023, Figure 3 — harmfulness rate vs. number of fine-tuning
       epochs (0/3/5/10) for the 100-shot attack, GPT-3.5 Turbo vs.
       Llama-2-7b-Chat (PDF p.6).
Shows: How few training passes are needed before the rate saturates — the
       "cheap and fast" part of the demonstrated result, as a trend rather
       than a single number.
Crop:  Retain both model lines and the epoch axis; the underlying chart data
       is in Table 1/2, so this asset is optional if space is tight.

Asset: Kapoor et al. 2024, Table 1 — the seven-vector, six-criterion
       traffic-light grid scoring how completely prior misuse studies (on
       spear-phishing, cybersecurity, disinformation, biosecurity, voice
       cloning, NCII, CSAM) address each element of the marginal-risk
       framework (PDF p.6).
Shows: Visually, that most prior "open models are dangerous" studies are
       incomplete by the authors' own framework — supports the "framework
       paper, not a blanket rebuttal" characterization in this record without
       requiring the reader to take the researcher's word for it.
Crop:  Keep all seven rows and six columns; the grid's value is the pattern
       across the full table, not any single cell.

None found for: Seger et al. 2023 (a policy/argument paper with no
       chart-worthy quantitative content); the RAND report (guardrail
       prohibits opening any chart that might sit near scenario content);
       the Meta license and Zuckerberg essay (prose documents, no data
       visuals); the NTIA fact sheet and Egan/Heim KYC paper (policy prose).
```

### Discarded

```text
URL: https://www.rand.org/pubs/research_reports/RRA2977-1.html — RAND's
     October 2023 preliminary report. Read its public executive-summary page
     only, then excluded entirely: that page's own "Key Takeaways" name
     specific pathogens and delivery-method categories from the study's
     fictional scenarios, which falls inside this assignment's guardrail
     against recording any operational CBRN detail, even at summary level.
     The January 2024 final report (RRA2977-2, used above) supersedes it for
     every claim this lesson needs and its own summary page stays entirely at
     the level of the top-line finding, so nothing was lost by dropping this
     one.

URL: https://cdn.governance.ai/Open-Sourcing_Highly_Capable_Foundation_Models_2023_GovAI.pdf
     — Same document as the GovAI/arXiv source used above. WebFetch could not
     extract readable text from this CDN copy specifically (returned as
     opaque binary/image stream to that tool); superseded by reading the
     arXiv-hosted PDF directly with a local PDF text extractor, which
     produced full, quotable text. Not a distinct finding, just a dead-end
     transport for a source already captured above.

URL: https://www.rand.org/pubs/articles/2024/red-teaming-the-risks-of-using-ai-in-biological-attacks.html
     — A RAND "article" restating the same report's findings in magazine
     form. Returned HTTP 403 to automated fetch tools and was not pursued
     further once the report's own landing page (used above) supplied the
     same top-line conclusion with a confirmed, resolving URL.

URL: General web-search synthesis claim ("45 participants...15 groups of
     three") and a linkpost summary claim ("~12 teams of three plus 3 more,
     split 8/4") for RAND's team structure — both read, both recorded above
     under Contradictions as an unresolved discrepancy rather than used as a
     confirmed figure, since they disagree with each other and neither is the
     primary report itself.
```
