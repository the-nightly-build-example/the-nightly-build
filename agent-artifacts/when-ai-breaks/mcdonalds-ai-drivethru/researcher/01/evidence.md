# evidence: when-ai-breaks/mcdonalds-ai-drivethru (01)

The record supports the commission's spine firmly: the corporate chronology
(Apprente acquired September 2019 -> folded into McD Tech Labs -> McD Tech Labs
sold to IBM, joint statement October 27, 2021 -> automated order taking (AOT)
tested at more than 100 US restaurants -> partnership ended, system shut off no
later than July 26, 2024) is anchored in McDonald's and IBM's own releases and in
consistent trade reporting. The wind-down memo from Mason Smoot, chief restaurant
officer for McDonald's USA, is quoted identically across four independent
outlets, and its "successes to date / voice ordering will be part of our
future" framing is on the record. The mechanism of why drive-thru ASR is hard is
anchored in the Whisper paper's measured collapse of accuracy under background
noise. The human-in-the-loop reality is documented at the highest evidentiary
level available, an SEC enforcement order, but it belongs to Presto Automation,
a competitor, not to McDonald's/IBM, and the record must not let the writer blur
the two.

Where the record is thin: no official measured accuracy for the McDonald's/IBM
system was ever published, so the widely-repeated "about 85 percent" figure is
reporting, not a company disclosure, and must be labelled as such. The specific
failure clips (bacon on ice cream, a runaway nugget order, an ice-cream order
that filled with ketchup and butter) are real and widely reproduced in mainstream
coverage, but they are user-posted videos without a stable, verifiable original
poster or restaurant, so they establish that such behavior was filmed and
circulated, not an audited failure rate. Nothing in the record contradicts the
commissioned angle; the one tension the editor should weigh is McDonald's "not a
failure, a partnership that ran its course" framing against the error record and
the sub-threshold accuracy, which the absence of published numbers leaves
unsettled.

## Sources

```text
URL:         https://www.prnewswire.com/news-releases/mcdonalds-to-acquire-apprente-an-early-stage-leader-in-voice-technology-300915075.html
Kind:        primary. McDonald's own press release, distributed verbatim over the
             PR Newswire wire. It owns the acquisition claim and the quotes. The
             document's home page, corporate.mcdonalds.com/.../acquires_apprente.html,
             returned HTTP 503 to every fetch attempt (gated, not dead); the wire
             copy carries McDonald's authored text unchanged.
Establishes: The September 10, 2019 agreement to acquire Apprente; Apprente as an
             early-stage voice/conversational-AI company (founded 2017, Mountain
             View, CA) built for multilingual, multi-accent, multi-item ordering;
             the creation of McD Tech Labs as a new internal group in McDonald's
             Global Technology, with the Apprente team as its founding members;
             the stated purpose of "faster, simpler and more accurate order taking
             at the Drive Thru," later mobile and kiosks.
Locators:    Headline; opening paragraphs; executive-quote block.
Quote:       Steve Easterbrook, President and CEO, McDonald's: "Building our
             technology infrastructure and digital capabilities are fundamental to
             our Velocity Growth Plan." Itamar Arel, Apprente co-founder and VP of
             McD Tech Labs, is quoted as joining McDonald's.
```

```text
URL:         https://newsroom.ibm.com/Joint-Statement-from-McDonalds-and-IBM
Kind:        primary. IBM's own newsroom, the joint statement authored by IBM and
             McDonald's. Owns the sale-and-partnership claim.
Establishes: Dated October 27, 2021. McDonald's sells McD Tech Labs to IBM; the
             team joins IBM's Cloud & Cognitive Software division; deal expected to
             close December 2021, subject to regulatory approval. Defines AOT
             (automated order taking) as AI/natural-language-processing technology
             to automate drive-thru ordering, to be scaled across languages,
             dialects and menu variations. Both parties assert testing "has shown
             substantial benefits."
Locators:    Full statement (short).
Quote:       "McDonald's development and testing of AOT technology in restaurants
             has shown substantial benefits to customers and the restaurant crew
             experience." "IBM's expertise in building customer care solutions with
             AI and natural language processing will help scale the AOT technology
             across markets and tackle integrations including additional languages,
             dialects and menu variations."
```

```text
URL:         https://www.sec.gov/files/litigation/admin/2025/33-11352.pdf
Kind:        primary. US Securities and Exchange Commission administrative
             cease-and-desist order (Release No. 33-11352), a government finding
             of fact. It owns the human-in-the-loop claim for Presto Automation.
             NOTE: this is a McDonald's COMPETITOR (Presto served Carl's Jr.,
             Hardee's, Del Taco, Checkers), NOT the McDonald's/IBM system. It
             documents the industry pattern of remote humans behind "AI" ordering;
             it is not evidence about McDonald's.
Establishes: From November 2021 to September 2022 Presto Voice ran on speech
             technology owned and operated by a third party ("Supplier A," i.e.
             Hi Auto). The original version converted the customer's spoken order
             to text and displayed it to off-site human agents Presto contracted,
             "including in the Philippines and India," who entered the order; it was
             "not capable" of completing orders on its own. Presto's own proprietary
             version, commercially deployed September 2022, "required a human agent
             to enter the orders approximately 70% of the time." Between October 21,
             2022 and May 1, 2023 Presto publicly claimed Presto Voice
             "eliminat[es] human order taking," which the SEC found false. Presto's
             disclosed "non-intervention"/"automated order completion" rates of 95%
             to 99% referred to orders completed without RESTAURANT-STAFF
             involvement, not without any human involvement, and were misleading.
             Settled January 14, 2025; cease-and-desist, no monetary penalty, citing
             cooperation. Violations of Securities Act 17(a)(2) and Exchange Act
             13(a).
Locators:    Summary para (order-taking at QSRs); paras 24-27 (human order taking,
             ~70%, Philippines/India, "eliminat[es] human order taking"); paras on
             "non-intervention"/"automated order completion" rate definitions and
             the 95%-99% claims; internal-message quotes on humans in the loop.
Quote:       "...required a human agent to enter the orders approximately 70% of the
             time." "Presto hired, trained, and supervised human order takers located
             abroad (primarily in the Philippines and India), who processed the vast
             majority of drive-thru orders..."
```

```text
URL:         https://cdn.openai.com/papers/whisper.pdf
Kind:        primary. The Whisper research paper (OpenAI). Owns the measured claim
             about ASR robustness under noise. Anchors the mechanism the lesson
             teaches; complements the library's existing the-evidence/whisper
             material.
Establishes: Title "Robust Speech Recognition via Large-Scale Weak Supervision"
             (Radford, Kim, Xu, Brockman, McLeavey, Sutskever, OpenAI, 2022).
             Section 3.7 "Robustness to Additive Noise" and Figure 5 show word error
             rate (WER) on LibriSpeech test-clean rising as signal-to-noise ratio
             (SNR) falls; even strong models degrade sharply once SNR drops below
             about 10 dB. This is the general primary for why recognition breaks
             down in the drive-thru's engine-and-traffic noise. The paper does not
             mention McDonald's; it is cited for the ASR mechanism only.
Locators:    Abstract; Section 3.7; Figure 5 (WER vs SNR).
Quote:       "This showcases Whisper's robustness to noise..." (context: WER still
             climbs steeply at low SNR, i.e. noise defeats even robust ASR).
```

```text
URL:         https://www.aljazeera.com/economy/2024/6/19/mcdonalds-scrap-ai-pilot-at-drive-through-outlets-after-order-mix-ups
Kind:        secondary. Al Jazeera reporting on the 2024 wind-down. Repeats the
             McDonald's statement; does not own it.
Establishes: McDonald's discontinued the IBM-built voice system deployed at about
             100 drive-thrus after viral videos of order errors; references TikTok
             clips of duplicate orders, wrong-vehicle pickups, and "ice cream with
             ketchup and butter." Carries McDonald's forward-looking statement.
Locators:    Body; closing statement.
Quote:       McDonald's: "our work with IBM has given us the confidence that a voice
             ordering solution for [drive-through] will be part of our restaurants'
             future," with a decision on a new solution promised by year-end 2024.
```

```text
URL:         https://www.biometricupdate.com/202406/mcdonalds-pauses-ai-voice-ordering-system-developed-with-ibm
Kind:        secondary. Reporting by Joel R. McConvey, June 25, 2024. Repeats the
             memo and adds chronology and cost context.
Establishes: Two-year IBM AOT test across ~100 drive-thrus, shutdown scheduled
             July 26, 2024. System "struggled with accuracy across different accents
             and dialects"; franchisees complained of high operating cost. Repeats
             the "voice ordering... part of our restaurants' future" line and the
             "informed decision... by the end of the year" line. Recaps Apprente
             (2019) -> McD Tech Labs -> IBM (2021). Notes McDonald's has faced
             Illinois BIPA suits over voice-data consent (context, not this lesson).
Locators:    Body.
Quote:       "make an informed decision on a future voice ordering solution by the
             end of the year."
```

```text
URL:         https://www.restaurantonline.co.uk/Article/2024/06/19/McDonald-s-ends-AI-drive-thru-trial-in-US-after-order-mistakes/
Kind:        secondary. UK trade reporting, June 19, 2024. Describes the specific
             failure clips.
Establishes: Three widely-circulated failures: bacon added to ice cream; a
             chicken-nugget order inflated to roughly 166 pounds' worth; and a
             TikTok titled "Fighting with McDonald's robot" in which a customer
             asking for vanilla ice cream and water received multiple ice creams,
             ketchup sachets and two portions of butter. Shut-off no later than
             July 26, 2024; more than 100 US restaurants; trial since 2021.
Locators:    Body (error list); details box.
Quote:       McDonald's: "While there have been successes to date, we feel there is
             an opportunity to explore voice ordering solutions more broadly."
```

```text
URL:         https://www.restaurantbusinessonline.com/technology/mcdonalds-ending-its-drive-thru-ai-test
Kind:        secondary that carries the primary. Restaurant Business obtained and
             quoted the internal email to franchisees; the memo is the primary the
             reporting quotes. Direct fetch returned HTTP 403 (site-level bot block,
             not org policy; the proxy reported no relay failure). The memo's wording
             and Mason Smoot's title are corroborated identically by Al Jazeera,
             Biometric Update, Restaurant Online and NBC News, so the quotes are
             treated as reliable; the exact email was not read firsthand.
Establishes: McDonald's ended the IBM AOT test with no expansion, per an email to
             franchisees sent the Thursday before the June 17-18, 2024 coverage.
             AOT shut off in all test restaurants no later than July 26, 2024.
             Author: Mason Smoot, chief restaurant officer, McDonald's USA.
Locators:    Body; quoted memo.
Quote:       Smoot: "while there have been successes to date, we feel there is an
             opportunity to explore voice ordering solutions more broadly," and the
             company will make "an informed decision on a future voice ordering
             solution by the end of the year."
```

```text
URL:         https://www.engadget.com/mcdonalds-ibm-ai-food-orders-131806578.html
Kind:        secondary. Engadget (Jon Fingas), on the 2021 IBM sale, later updated
             with an accuracy characterization. Source of the widely-repeated
             accuracy figure. Does NOT establish an official measured number.
Establishes: McDonald's tested the system at 10 Chicago restaurants in spring 2021.
             The article characterizes the system as "only about 85 percent accurate,
             necessitating human intervention for nearly a fifth of orders." This is
             reporting's characterization; neither McDonald's nor IBM published a
             measured order-accuracy figure. Treat 85% as reported, unowned.
Locators:    Body.
Quote:       "only about 85 percent accurate, necessitating human intervention for
             nearly a fifth of orders."
```

```text
URL:         https://www.restaurantdive.com/news/white-castle-soundhound-ai-voice-drive-thru-100-units-2024/689624/
Kind:        secondary. Restaurant Dive (Julie Littman), August 2, 2023. Peer-context
             for the closing section.
Establishes: White Castle expanding SoundHound voice AI to more than 100 US
             drive-thru lanes by end of 2024, many running 24/7. SoundHound claims a
             90% order-completion rate, orders processed within 60 seconds, and
             "complete end-to-end AI" without human assistance. Notes McDonald's
             low-80s accuracy fell below the ~95% threshold peers cite for adoption.
Locators:    Body; performance-claims list.
Quote:       SoundHound: "90% order completion rate."
```

```text
URL:         https://www.cnbc.com/2024/07/03/ai-drive-thru-ordering-mcdonalds-yum-wendys-test-tech.html
Kind:        secondary. CNBC survey of drive-thru voice AI across chains. Direct
             fetch returned HTTP 403 (site-level block); used for peer-context
             framing only, corroborated by the searches below. Wendy's/Google and
             Yum/Taco Bell figures are one-line context, not load-bearing.
Establishes: Peers pursuing voice AI after McDonald's exit: Wendy's FreshAI (built
             with Google Cloud), expanding from ~100 toward 500-600 locations by end
             of 2025; Yum Brands / Taco Bell scaling voice AI to hundreds of US
             stores. Context for "where the weakness lives today."
Locators:    Body (not read firsthand; blocked).
Quote:       None read firsthand.
```

### Failure videos as behavior artifacts

```text
Artifact:    User-posted drive-thru videos, most-cited: (a) bacon added to a
             soft-serve/ice-cream order; (b) a runaway chicken-nugget order (cited
             variously as ~260 nuggets or ~166 pounds' worth); (c) "Fighting with
             McDonald's robot," in which a request for vanilla ice cream and water
             filled with multiple ice creams, ketchup sachets and two portions of
             butter.
Kind:        primary artifacts of the behavior, with a provenance limit. Each shows
             the system's actual output on camera. But they are user-uploaded clips
             without a stable verifiable original poster, restaurant, or date, and
             the exact "260" figure appears mainly in secondary listicles. They
             establish that these mis-orders were filmed and widely circulated in
             mainstream coverage (Al Jazeera, Restaurant Online, ACS Information
             Age); they do not establish a measured failure rate.
Distinction: Widely-reproduced and mainstream-carried: bacon-on-ice-cream and the
             ketchup/butter/multiple-ice-cream clip. Commonly cited but
             origin-unverified: the precise "260 McNuggets" number. Do not present
             any single clip's exact figure as an audited McDonald's statistic.
```

## Contradictions

- McDonald's framing versus the error record. McDonald's calls the end a
  partnership that produced "successes to date," with "confidence" that voice
  ordering "will be part of our restaurants' future." The public record is a run
  of filmed mis-orders and reporting that the system plateaued in the low-80s
  percent, below the ~95% peers say is needed. What would settle it: an official
  measured accuracy figure over the pilot and the reason for ending (accuracy,
  franchisee cost, or a fixed-term partnership reaching its end). None was
  published, so the cause is genuinely undetermined; the honest reading is that
  the framing and the errors coexist without a public number to adjudicate them.
- The "about 85 percent" accuracy. Reported by Engadget and echoed as "low 80s"
  by Restaurant Dive, but attributable to no McDonald's or IBM disclosure. Record
  it as reported, and state plainly that measured accuracy was never published.
- Human-in-the-loop scope. The SEC-documented ~70% off-site human intervention is
  Presto, not McDonald's. McDonald's own human involvement was in-restaurant crew
  correcting roughly one order in five (the inverse of the reported ~85%). These
  are two different human-in-the-loop shapes and must not be merged.
- Number of restaurants. IBM/McDonald's and most reporting say "more than 100";
  a few sources round to "about 100." Use "more than 100."

## Numbers

```text
Figure: ~70% of orders required a human agent to enter them
Owner:  SEC order 33-11352 (Presto Automation), para 26
Scope:  Presto's proprietary Presto Voice, deployed from September 2022; off-site
        agents (Philippines/India). NOT McDonald's.
```

```text
Figure: "95% to 99%" automated-completion / >95% non-intervention rates (claimed)
Owner:  Presto public filings, as characterized by SEC order 33-11352
Scope:  Found misleading: measured only absence of restaurant-staff involvement,
        not absence of all human involvement.
```

```text
Figure: ~85% order accuracy / human intervention on ~1 in 5 orders (reported)
Owner:  Engadget reporting; NOT an official McDonald's/IBM figure
Scope:  Characterization of the McDonald's/IBM pilot. No measured accuracy was
        ever published by McDonald's or IBM. Use as reported, flag as unowned.
```

```text
Figure: more than 100 US restaurants
Owner:  IBM/McDonald's joint statement context and consistent trade reporting
Scope:  The AOT test footprint, 2021-2024.
```

```text
Figure: shut off no later than July 26, 2024
Owner:  Mason Smoot memo, via Restaurant Business / Biometric Update / Restaurant Online
Scope:  Removal of AOT from all test restaurants.
```

```text
Figure: WER rises steeply as SNR falls below ~10 dB
Owner:  Whisper paper, Figure 5 / Section 3.7
Scope:  LibriSpeech test-clean under additive noise; the general ASR mechanism.
```

```text
Figure: 90% order-completion rate (SoundHound, White Castle); Wendy's ~100 -> 500-600 by end 2025
Owner:  SoundHound via Restaurant Dive; Wendy's/Google via CNBC
Scope:  Peer context only.
```

## Source assets

```text
Asset: Whisper paper, Figure 5 (WER on LibriSpeech test-clean vs SNR).
Shows: Recognition accuracy collapsing as background noise rises, the exact
       mechanism that makes a drive-thru hostile to ASR.
Crop:  Keep both axes labelled (WER, SNR in dB) and the rising curve; omit the
       comparison-model legend clutter if space is tight, but keep the axis units.
```

```text
Asset: IBM/McDonald's joint statement, the "substantial benefits" sentence.
Shows: The operator's own optimistic framing at launch, to set against the later
       wind-down. A verifiable corporate-statement excerpt.
Crop:  The single sentence; retain attribution to the joint statement and its date.
```

```text
Asset: SEC order 33-11352, paragraph 26 ("...approximately 70% of the time" /
       "Philippines and India").
Shows: A government finding that a marketed "AI" drive-thru ran largely on remote
       humans, the human-in-the-loop reality in the plainest documentary form.
Crop:  Keep the sentence naming the ~70% figure and the agent locations; retain the
       release number so the reader can verify. Label clearly as Presto, not McDonald's.
```

```text
Asset: A still from a widely-reproduced failure clip (bacon-on-ice-cream, or the
       ketchup/butter/multiple-ice-cream "Fighting with McDonald's robot" clip).
Shows: The system's on-camera mis-order. Use only if provenance can be stated.
Crop:  If used, caption must say it is a user-posted clip of uncertain original
       source, not an audited example. No exact per-clip figure presented as fact.
```

## Discarded

```text
URL: https://corporate.mcdonalds.com/corpmcd/our-stories/article/acquires_apprente.html — the document's own home page, but HTTP 503 to every attempt; used the PR Newswire wire copy of the same McDonald's release instead.
URL: https://corporate.mcdonalds.com/corpmcd/our-stories/article/IBM-McD-Tech-Labs.html — HTTP 503; used the IBM newsroom copy of the same joint statement instead.
URL: https://www.cnbc.com/2024/06/17/mcdonalds-to-end-ibm-ai-drive-thru-test.html — HTTP 403 (site block); the story it broke is corroborated by Al Jazeera, Biometric Update and Restaurant Online, which were readable.
URL: https://www.theverge.com/2024/6/17/24180073/... — fetch blocked entirely; not needed once other outlets carried the same facts.
URL: https://apnews.com/article/mcdonalds-ai-drive-thru-ibm-... — fetch blocked; redundant with readable coverage.
URL: https://medium.com/@... (multiple) — self-published commentary, no independent reporting; rejected as non-authoritative.
URL: https://www.tiktok.com/discover/... — aggregation/discovery pages, not a single verifiable original clip; the failure-video artifact is recorded above with its provenance limit rather than pinned to these.
URL: https://presto.com/the-role-of-humans-in-a-voice-ai-drive-thru/ — Presto's own marketing on HITL; the SEC order is the authoritative primary for the same facts, so the vendor page is not cited.
```
