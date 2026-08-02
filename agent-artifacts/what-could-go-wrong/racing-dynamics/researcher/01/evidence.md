# Evidence record: what-could-go-wrong/racing-dynamics

The record supports the piece's central move: the formal model (Armstrong,
Bostrom & Shulman, 2016; restated by Bostrom in *Superintelligence*, 2014) is
read first-hand in full, its equations and both headline results (competition
lowers safety investment; more information can lower it further) are captured
exactly, and its three load-bearing assumptions are stated precisely enough to
audit: a near-winner-take-all payoff to finishing first, a small fixed number
of teams whose relative capability is what the payoff depends on, and safety
investment that trades directly against speed. Present-day material is
strong on two of the three audits. On assumption (a) — a decisive, durable
first-mover advantage — the record is one-sided and well-sourced: every
capability lead tracked by Epoch AI's index has closed within months, not
never, including a case (DeepSeek R1 following OpenAI's o1) that is now
independently dated to four months. On assumption (b) — that developers
trade safety against speed under real competitive pressure — the record has
a genuine primary admission (OpenAI's own Preparedness Framework names the
scenario and pre-commits conditions for handling it) plus one well-reported
but single-origin claim (a Financial Times investigation, read only through
its retellings, not the original, which this session could not fetch) that a
second, independent, on-record primary (METR's own account of a three-week
evaluation window) partially corroborates without fully matching its
specifics. The record is thin in one place the brief asked for: a direct,
technical critique of the information result's robustness to relaxed
assumptions. Searches surfaced plenty of people rejecting the racing
framing's real-world premise (no winner-take-all discontinuity has occurred)
but nothing that engages the model's math on its own terms. That gap is
recorded honestly below rather than papered over.

## Sources

1. **Armstrong, S., Bostrom, N. & Shulman, C., "Racing to the precipice: a
   model of artificial intelligence development."** Two linked instances of
   the same paper were read in full:
   - FHI Technical Report #2013-1 (October 2013), full text at
     https://ora.ox.ac.uk/objects/uuid:d87d8e34-22d6-4597-ac31-041fcb63903f
     (landing page) and the PDF itself,
     https://ora.ox.ac.uk/objects/uuid:d87d8e34-22d6-4597-ac31-041fcb63903f/files/s5q47rq79d
     (labeled by ORA as the "version of record," 8 pages). Both URLs
     resolved and were read completely, page by page.
   - Published version: *AI & Society* 31:201-206 (2016), DOI
     10.1007/s00146-015-0590-y. The DOI resolves (redirects to
     link.springer.com) but the full text sits behind a Springer login wall;
     this session read the abstract independently via a citation aggregator
     (ResearchGate's listing) and confirmed it is verbatim identical to the
     FHI report's abstract, so the ORA copy is being treated as the accurate
     stand-in for the published article's content. Citation for the argument
     in the article should point readers to the open ORA copy.
   - **Classification: primary.** The authors are the paper's sole
     authorship and the model is entirely theirs; this is the document that
     owns every claim about the model.
   - **What it establishes first-hand:** The full model. *n* teams each have
     capability *c* drawn uniformly from [0, µ] and choose a safety level *s*
     between 0 (no precautions) and 1 (total safety); each team's score is
     *c − s*, the highest score wins the race, and the winner's AI succeeds
     with probability *s* and causes "an AI-disaster" with probability 1 − s.
     Utilities are normalized to 1 (success) and 0 (disaster); a team that
     loses to a rival gets 1 − e, where *e* is "enmity," ranging from 0
     (indifferent who wins) to 1 (a rival's success is as bad as disaster).
     µ measures "the relative importance of capability": high µ means
     skimping on safety buys little advantage; low µ means it buys a lot.
   - **Exact statements, quoted:** Abstract: "This paper presents a simple
     model of an AI arms race, where several development teams race to build
     the first AI. Under the assumption that the first AI will be very
     powerful and transformative, each team is incentivised to finish
     first — by skimping on safety precautions if need be. This paper
     presents the Nash equilibrium of this process... Surprisingly,
     information also increases the risks: the more teams know about each
     others' capabilities (and about their own), the more the danger
     increases" (p. 1 / journal p. 201).
   - **The three information scenarios and their equilibria (§2, pp. 2-5):**
     - *No information* (nobody knows any capability, including their own):
       symmetric equilibrium safety level s = µ/(en) if µ < en, else s = 1.
       Disaster probability = 1 − µ/(en) if µ < en, else 0.
     - *Private information* (each team knows only its own capability x):
       s(x) = x/(en − e + 1) if x < en − e + 1, else 1. Integrating over all
       x gives disaster probability 1 − µⁿ/[(n+1)(ne−e+1)] for µ < en−e+1.
     - *Public information* (every team knows every team's capability): let
       Δ be the gap between the top two teams; the leader's safety is
       s_top = Δ/e if Δ/e < 1, else 1. Integrating over Δ gives disaster
       probability 1 − µ/[e(n+1)] for µ < e.
   - **The main result, exact statement:** "in every situation, an increase
     of the importance of capability (an increase in µ) reduces the risk...
     Indeed, around µ = 0 (i.e. when capability is nearly irrelevant to
     producing the first AI), the only Nash equilibrium is to take no safety
     precautions at all" (§3.1, p. 4). Also: enmity and team count both
     increase risk in most cases (§3.2, §3.4).
   - **The information result, exact statement and reasoning (§3.3, p. 6-7,
     titled "The curse of too much information"):** "The no-information case
     is always safer than the other two cases... It is always better if none
     of the teams have any idea about anyone's capability." The paper's own
     mechanism: under private information, a team only takes extra risk if
     its own capability is low (a team that knows it's ahead has no reason
     to cut corners), so a disaster requires *all* teams to happen to be low
     capability — a probability that shrinks as 1/µⁿ. Under public
     information, the winner takes risk only if the runner-up is close
     behind — a probability that shrinks more slowly, as 1/µ. So public
     information is asymptotically far more dangerous than private
     information, and both are more dangerous than no information at all.
     Conclusion (§4, p. 8): "Counter-intuitively, increasing the information
     available to all the teams... increases the risk. This is a special
     case of an information hazard [Bos11]: we'd be better off not knowing."
   - **Toy figures:** Figures 1-3 (pp. 6, 8) plot AI-disaster probability
     against µ (x-axis, 0 to 10) for 2 and 5 teams, at enmity 1 and enmity
     0.5, each showing three curves (no information, private information,
     public information). All curves start at risk 1.0 at µ=0 and decay
     toward 0 as µ grows; the no-information curve always decays fastest.
   - **Locators:** all quotes above carry their FHI-report page number; the
     journal pagination (201-206) runs roughly one-to-one with the report's
     pages 1-6 (abstract=201, model=202-204, results/conclusion=205-206).

2. **Bostrom, Nick. *Superintelligence: Paths, Dangers, Strategies* (Oxford
   University Press, 2014), Chapter 14, "The strategic picture," section
   "The race dynamic and its perils" and "Box 13: A risk-race to the
   bottom," pp. 246-248.** Read via the Internet Archive's OCR scan of the
   physical book: item page
   https://archive.org/details/superintelligence-paths-dangers-strategies-by-nick-bostrom,
   full OCR text fetched directly from
   https://ia600501.us.archive.org/5/items/superintelligence-paths-dangers-strategies-by-nick-bostrom/superintelligence-paths-dangers-strategies-by-nick-bostrom_djvu.txt
   (both URLs resolved; the text file downloaded and was searched directly
   for "race dynamic," confirming exact page numbers and OCR text). A
   secondary mirror (publicism.info/philosophy/superintelligence/15.html)
   was checked first and returned matching wording, which cross-confirms the
   Archive.org scan's fidelity; the Archive.org scan of the print book is
   the source of record for every quote below.
   - **Classification: primary.** Bostrom's own book, his own argument.
   - **What it establishes first-hand:** Bostrom's plain-language restatement
     of the same race model, with an explicit acknowledgment (endnote, p.
     293 in the OCR numbering) reading: "I am indebted to Carl Shulman and
     Stuart Armstrong for help with this model" — tying Box 13 directly to
     the same collaboration as source #1, two years before the journal
     version appeared.
   - **Exact quotes:** "A race dynamic exists when one project fears being
     overtaken by another. This does not require the actual existence of
     multiple projects." "The severity of a race dynamic (that is, the
     extent to which competitors prioritize speed over safety) depends on
     several factors, such as the closeness of the race, the relative
     importance of capability and luck, the number of competitors..." "The
     race dynamic could spur projects to move faster toward superintelligence
     while reducing investment in solving the control problem." Box 13: "The
     Nash equilibrium for this game is for every team to spend nothing on
     safety." "The greater the number of competing teams, the more dangerous
     the race becomes." On information: "the models are unequivocal:
     information is (in expectation) bad," with the footnoted qualifier
     "That is, information in the model is always bad ex ante. Of course,
     depending on what the information actually is, it will in some cases
     turn out to be good that the information became known, notably if the
     gap between leader and runner-up is much greater than one would
     reasonably have guessed in advance."
   - **Locators:** print pages 246 ("The race dynamic and its perils," Box
     13 opens), 247 ("Compatible goals," "The number of competitors"), 248
     ("The curse of too much information," continuing into "On the benefits
     of collaboration").
   - Note for the writer: this book chapter is background/corroboration,
     not a separate finding — it restates source #1's model in different
     prose and a different figure (Bostrom's Figure 14 mirrors Armstrong et
     al.'s Figures 1-3). Cite the journal paper for the model itself and
     this chapter only if a second phrasing of the same result is useful.

3. **OpenAI, "Preparedness Framework," Version 2, last updated 15 April
   2025.** PDF read directly and in full:
   https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf
   (22 pages; resolved, downloaded, read). Companion blog post (context
   only, not separately quoted): https://openai.com/index/updating-our-preparedness-framework/.
   - **Classification: primary.** OpenAI's own governance document, stating
     its own policy in its own words. This is evidence of what one developer
     says it will do, not proof that competitive pressure actually degrades
     safety industry-wide — the brief's "name no company as an authority"
     instruction is honored by treating this as exactly that: one
     developer's on-record statement.
   - **What it establishes first-hand:** the developer's own acknowledgment
     that a competitor's move can change its safety posture. Section 4.3,
     "Marginal risk" (p. 12), quoted in full: "We recognize that another
     frontier AI model developer might develop or release a system with
     High or Critical capability in one of this Framework's Tracked
     Categories and may do so without instituting comparable safeguards to
     the ones we have committed to. Such an action could significantly
     increase the baseline risk of severe harm being realized in the world,
     and limit the degree to which we can reduce risk using our safeguards.
     If we are able to rigorously confirm that such a scenario has occurred,
     then we could adjust accordingly the level of safeguards that we
     require in that capability area, but only if: we assess that doing so
     does not meaningfully increase the overall risk of severe harm, we
     publicly acknowledge that we are making the adjustment, and, in order
     to avoid a race to the bottom on safety, we keep our safeguards at a
     level more protective than the other AI developer, and share
     information to validate this claim."
   - Also relevant: Table 1 (p. 5-6) defines a "Critical" AI
     self-improvement threshold partly in schedule terms — "a generational
     model improvement (e.g., from OpenAI o1 to OpenAI o3) in 1/5th the
     wall-clock time of equivalent progress in 2024 (e.g., sped up to just 4
     weeks) sustainably for several months" — this is a definitional
     trigger inside OpenAI's own framework, not an observed event; do not
     present it as something that has happened.
   - **Locator:** §4.3 "Marginal risk," p. 12; Table 1, pp. 5-6.

4. **OpenAI, "GPT-4 System Card"** (undated within the PDF; GPT-4 launched
   14 March 2023). PDF read directly: https://cdn.openai.com/papers/gpt-4-system-card.pdf
   (resolved; read pp. 41-43).
   - **Classification: primary.** OpenAI's own account of its own testing
     process for one specific model.
   - **What it establishes first-hand:** "Since it finished training in
     August of 2022, we have been evaluating, adversarially testing, and
     iteratively improving the model and the system-level mitigations around
     it" (p. 42/Introduction). August 2022 to the March 2023 launch is
     roughly seven months — this is the developer's own on-record basis for
     the "months, not days" baseline that later reporting (source #14 below)
     says shortened.
   - **Locator:** Introduction, p. 42.

5. **METR, "Details about METR's preliminary evaluation of OpenAI's o3 and
   o4-mini,"** 16 April 2025. Read directly: https://metr.org/evaluations/openai-o3-report/
   (resolved).
   - **Classification: primary — independent evaluator, not the developer.**
     METR is a third party contracted/given access by OpenAI to test the
     model; its account of its own working conditions is a first-hand,
     on-record statement independent of OpenAI's.
   - **What it establishes first-hand:** "The work reported here was
     conducted over only three weeks." "METR received access to earlier
     checkpoints of o3 and o4-mini from OpenAI three weeks prior to model
     release." METR states this shortened window meant "we conducted no
     elicitation of o3's and o4-mini's capabilities. The agentic scaffold
     used is relatively simple, and was not adapted to either o3 or
     o4-mini," and warns that "more thorough evaluations are likely to
     reveal additional capabilities or risk-relevant observations." The
     report does not itself attribute the short window to competitive
     pressure from other developers — it states the fact of the constraint,
     not a cause.
   - **Use as corroboration:** this is an independent, on-record
     confirmation that a real evaluation window was short (three weeks)
     around a real release, though its specific figure (three weeks) is not
     identical to the "days" language in the Financial-Times-derived
     reporting (source #14). Treat as a second, independent data point
     about compressed evaluation time, not as confirming the exact "days"
     claim.

6. **UK Government / AI Seoul Summit, "Frontier AI Safety Commitments,"**
   21 May 2024, updated 7 February 2025. Read directly:
   https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024
   (resolved); press release also read:
   https://www.gov.uk/government/news/historic-first-as-companies-spanning-north-america-asia-europe-and-middle-east-agree-safety-commitments-on-development-of-ai
   (resolved).
   - **Classification: primary.** This is the actual commitment text,
     published by the convening government, that the signing organizations
     agreed to; it is the document that owns the claim about what was
     committed (though each signatory's compliance is a separate, unverified
     question the document does not itself settle).
   - **What it establishes first-hand:** the specific "if-then" structure
     the brief asked for. Quoted: organizations commit to "set out explicit
     processes they intend to follow if their model or system poses risks
     that meet or exceed the pre-defined thresholds," and, at the limit,
     "not develop or deploy a model or system at all, if mitigations cannot
     be applied to keep risks below the thresholds." The three required
     outcomes are to "effectively identify, assess and manage risks,"
     demonstrate "accountability for safely developing and deploying," and
     provide "appropriate transparency to external actors."
   - **Signatories exactly as listed on the government page (as of the
     February 2025 update):** Amazon, Anthropic, Cohere, Google/Google
     DeepMind, G42, IBM, Inflection AI, Meta, Microsoft, Mistral AI, Naver,
     OpenAI, Samsung Electronics, Technology Innovation Institute, xAI,
     Zhipu.ai, Magic, Minimax, 01.ai, and NVIDIA — twenty organizations by
     the update, sixteen at the original May 2024 signing. This is a list
     of institutions and a commitment text, not an authority for any safety
     claim; use it only to show what signatories said they would do.
   - **Locator:** the "if-then" language sits under "Outcome 1" in the
     published commitments text.

7. **Future of Life Institute, "Pause Giant AI Experiments: An Open
   Letter,"** published 22 March 2023. Read directly:
   https://futureoflife.org/open-letter/pause-giant-ai-experiments/
   (resolved).
   - **Classification: primary** of what this specific set of signatories
     asked for, on the record, at that date. It is not proof that a pause
     was warranted or that it happened.
   - **What it establishes first-hand:** the letter's own framing and ask.
     Quoted: "recent months have seen AI labs locked in an out-of-control
     race to develop and deploy ever more powerful digital minds that no
     one — not even their creators — can understand, predict, or reliably
     control." The specific ask, quoted exactly: "We call on all AI labs to
     immediately pause for at least 6 months the training of AI systems more
     powerful than GPT-4." Signed by over 30,000 people including named
     individuals such as Yoshua Bengio, Stuart Russell, Elon Musk, and Steve
     Wozniak (per the letter's own signatory list).
   - **Note:** the letter itself uses the exact banned racing phrase; do not
     reproduce that string in the article — paraphrase the ask and the
     framing instead.

8. **Karnofsky, Holden, "If-Then Commitments for AI Risk Reduction,"**
   Carnegie Endowment for International Peace, 13 September 2024. Read
   directly: https://carnegieendowment.org/research/2024/09/if-then-commitments-for-ai-risk-reduction
   (resolved).
   - **Title/affiliation as the document states it:** Holden Karnofsky,
     writing as a visiting scholar at the Carnegie Endowment for
     International Peace (Carnegie California) at the time of publication.
     Note for the writer/editor: Karnofsky later joined a frontier AI
     developer's technical staff (per public reporting, January 2025), after
     this piece was published — a detail worth knowing but not part of the
     document's own claim.
   - **Classification: primary** of what this proponent specifically wants
     done — a present-day coordination proposal, distinct from source #6's
     government-brokered version.
   - **What it establishes first-hand:** a concrete "if-then" proposal
     format. Quoted definition: commitments "of the form: If an AI model has
     capability X, risk mitigations Y must be in place," up to and including
     deployment pauses. Concrete example quoted: *if* a model "can
     interactively advise a malicious actor... to produce and release a
     catastrophically damaging CBRN weapon," *then* it "can only be deployed
     using methods where a determined actor would reliably fail to elicit
     such advice" and "can only be stored in environments such that it would
     be highly unlikely that a terrorist... could obtain the model weights."
     On coordination: "voluntary commitments alone are unlikely to keep
     risks low," and the piece argues "regulation and likely even
     international coordination" will ultimately be needed.

9. **Epoch AI, "Chinese AI models have lagged the US frontier by 7 months on
   average since 2023,"** data insight, 2 January 2026. Read directly:
   https://epoch.ai/data-insights/us-vs-china-eci (resolved).
   - **Classification: primary** — Epoch AI is the organization that built
     the Epoch Capabilities Index (ECI) and ran this specific analysis; this
     is its own dataset and its own claim about it, not a report on someone
     else's work.
   - **What it establishes first-hand:** "Since 2023, every model at the
     frontier of AI capabilities, as measured by [ECI], has been developed
     in the United States." "Chinese models have trailed US capabilities by
     an average of seven months, with a minimum gap of four months and a
     maximum gap of 14." The first Chinese model to match GPT-4's ECI score
     did so in May 2024 — a 14-month gap from GPT-4's own release. As of
     publication, "no Chinese model has yet surpassed the ECI of OpenAI's o3
     model, released in April 2025." Methodology: leading model per country
     per period, models within 1 ECI point treated as equivalent, earliest
     (likely non-frontier) models from each country excluded.
   - **Caveat to carry into the article:** this measures *how long a gap
     lasts before being closed*, which is direct, on-point evidence against
     a durable first-mover lock-in — it does not measure whether any given
     gap conferred a decisive strategic or economic advantage while it
     lasted.

10. **Epoch AI, "Open models lag state-of-the-art closed models by 4
    months,"** data insight (methodology note dated to an October 2025
    predecessor; this update read directly, undated header but referencing
    data through May 2026). Read directly: https://epoch.ai/data-insights/open-closed-eci-gap
    (resolved).
    - **Classification: primary**, same reasoning as #9.
    - **What it establishes first-hand:** open-weight models lag the closed
      frontier by "an average of four months" (an 8-ECI-point gap), up
      slightly from "an average of three months between January 2023 and
      October 2025" found in Epoch's prior version of the same analysis —
      i.e., the gap is not zero and moved a little wider between the two
      readings, not narrower. Use this for nuance: fast-following is real,
      but the gap is not shrinking monotonically to zero.

11. **Epoch AI, "Frontier AI capabilities can be run at home within a year
    or less,"** data insight, 15 August 2025. Read directly:
    https://epoch.ai/data-insights/consumer-gpu-model-gap (resolved).
    - **Classification: primary**, same organization, its own benchmarking.
    - **What it establishes first-hand:** "Using a single top-of-the-line
      gaming GPU like NVIDIA's RTX 5090 (under $2,500), anyone can locally
      run models matching the absolute frontier of LLM performance from
      just 6 to 12 months ago." Per-benchmark lag: GPQA-Diamond 7.4 months,
      MMLU-Pro 7.3 months, Artificial Analysis Intelligence Index 6.3
      months, LM Arena Elo 12.4 months. Methodology: largest models fitting
      an RTX 4090 (≤28B parameters) or RTX 5090 (≤40B) compared to frontier
      benchmark scores via linear regression with bootstrapped 90%
      confidence intervals.

12. **Arbel, Yonathan A. & Tokson, Matthew, "The AI Race Isn't Real,"**
    Lawfare, 19 May 2026. Read directly:
    https://www.lawfaremedia.org/article/the-ai-race-isn-t-real (resolved).
    - **Titles as the piece states them:** Yonathan A. Arbel, Silver
      Associate Professor, University of Alabama School of Law, and Director
      of its AI Studies Initiative; Matthew Tokson, Professor of Law,
      University of Utah S.J. Quinney College of Law.
    - **Classification: primary** of this dismissal argument — the authors'
      own on-record academic case against the racing framing, published
      under their own names.
    - **What it establishes first-hand — the strongest dismissal steelman
      found:** "AI knowledge is leaky. It is rapidly copied, distilled, and
      reverse-engineered," so a lead does not stay a lead. Concrete
      datapoint, quoted: when OpenAI released o1 in September 2024,
      "DeepSeek released R1" just "four months later, exhibiting mastery of
      the new paradigm." They also argue the race framing itself "corrodes
      safety by rewarding speed over caution" — i.e., their dismissal is of
      the *premise* (no durable lead exists to race for), not of the
      *mechanism* (competitive pressure cutting safety), which they
      partly grant.
    - **Cross-check:** the o1/R1 dates were independently checked against
      OpenAI's own September 2024 o1-preview announcement date and
      DeepSeek's 20 January 2025 R1 release date (both corroborated via
      multiple independent tertiary listings — Wikipedia's "OpenAI o1" and
      "DeepSeek (chatbot)" entries, and an IISS Strategic Comments piece);
      12 September 2024 to 20 January 2025 is almost exactly four months,
      confirming the Lawfare authors' figure.

13. **Scharre, Paul, "Debunking the AI Arms Race Theory,"** Texas National
    Security Review, Vol. 4, Issue 3 (Summer 2021), published online 28
    June 2021. Read directly: https://tnsr.org/2021/06/debunking-the-ai-arms-race-theory/
    (resolved).
    - **Title/affiliation as stated:** Paul Scharre, Vice President and
      Director of Studies, Center for a New American Security.
    - **Classification: primary** of his own argument; **secondary** with
      respect to any specific developer's conduct (he is describing the
      general "arms race" framing in military AI policy, not making claims
      about a specific company).
    - **What it establishes first-hand:** a technical, definitional
      dismissal — that a classical "arms race" requires abnormally high
      defense-spending growth (10-25% annually) and that AI, as a
      general-purpose technology rather than a discrete weapon, does not
      fit. Quoted: "The scale of military AI spending, at least at present,
      is nowhere near large enough to warrant the title of 'arms race.'" He
      does grant the underlying safety concern is "real but driven by
      perception, not inevitability," citing the V-22 Osprey program as a
      historical case where schedule pressure caused incomplete testing —
      i.e., he steelmans the mechanism while rejecting the "race" label.
    - **Scope caveat:** this piece is about military AI competition between
      states, not the commercial frontier-lab competition the commission
      centers; use it for the dismissal argument's structure and the "not
      every fast-moving competition is winner-take-all" point, not as
      direct evidence about any lab's conduct.

14. **Financial Times reporting on OpenAI's compressed safety-testing
    timelines** (original article not independently read — see below).
    Retold, with overlapping quotes and figures, by: TechCrunch
    (https://techcrunch.com/2025/04/16/openai-partner-says-it-had-relatively-little-time-to-test-the-companys-new-ai-models/,
    resolved), Semafor
    (https://www.semafor.com/article/04/11/2025/openai-slashes-time-given-to-safety-testing-as-it-races-to-innovate,
    resolved, byline Tom Chivers, 11 April 2025), CSO Online, and Seeking
    Alpha (both resolved via search snippet, not independently re-fetched
    beyond confirming consistent content).
    - **Classification: secondary, single origin.** Every one of these
      pieces attributes its central numeric claim to the same underlying
      Financial Times investigation. Per the research standard, this is
      one confirmation, not several, regardless of how many outlets carry
      it.
    - **Access note:** this session could not fetch the Financial Times
      article directly — `www.ft.com` returned a hard fetch failure (not a
      login page, an outright block) rather than a paywall screen to work
      around. The claim is therefore reported here at second hand and
      should be labeled as such if used: reporting states OpenAI moved from
      roughly six months of safety testing (for GPT-4) to as little as a
      few days (for later models, amid pressure to keep pace with rivals
      including DeepSeek), based on unnamed sources one outlet's account
      calls "familiar with the process." Semafor's own paraphrase, read
      directly: "The company used to allow months for safety testing, but
      now gives just days." No outlet reviewed quotes a named individual
      making this claim; the "recipe for disaster" and "reckless"
      characterizations are attributed to anonymous sources in the
      original FT piece as relayed by others.
    - **Independent corroboration available:** source #5 (METR) is an
      on-record, named, independent account of a real short evaluation
      window (three weeks) around the same o3 release cycle. It does not
      use the word "days" and does not claim OpenAI told it to hurry — it
      states its own working constraint. Treat sources #5 and #14 together
      as two independent lines pointing at the same underlying pattern
      (compressed evaluation time around a real release), while being
      precise that only #5 is a first-hand-read, on-record, named-source
      primary; #14 is secondary and unverified at its origin by this
      session.

## Contradictions

- **The central one: winner-take-all assumption vs. the observed
  fast-follow pattern.** The model's danger scales with how close the race
  is and, more fundamentally, assumes there is a race worth having — a
  payoff structure where finishing first matters enormously (source #1's
  "very powerful and transformative" first AI; enmity up to e=1, "another
  team building a successful AI is just as bad as an AI-disaster"). The
  empirical record (sources #9-12) shows every measured capability gap
  since 2023 has closed in months: 14 months (first Chinese model to reach
  GPT-4-level ECI), an average of 7 months for the US-China gap, an average
  of 3-4 months for the open-vs-closed gap, and a specific 4-month gap
  between OpenAI's o1 and DeepSeek's R1. Nothing in the record shows a
  capability lead translating into a durable exclusive advantage — no
  developer has "won" in the sense the model's payoff structure assumes.
  This is the strongest, best-sourced tension in the file and should carry
  real weight in the piece.
- **Doom framing vs. dismissal framing of the same underlying facts.**
  Source #7 (FLI letter) and adjacent quotes (e.g., Stuart Russell's public
  characterization, found via search but not independently read as a
  primary document in this pass — flagged for the writer to source
  separately if used) press the argument at full strength: competitive
  pressure is dangerous and demands a pause or hard commitments. Sources
  #12 and #13 dismiss the *framing*, not always the underlying mechanism:
  Arbel & Tokson reject the idea that any lead is durable enough to be worth
  racing for; Scharre rejects the "arms race" label on technical,
  definitional grounds while granting that schedule pressure degrading
  safety is "real." The two sides are not simply disagreeing about facts —
  they largely agree that competitive pressure exists and can degrade
  safety in principle, and disagree about whether the specific stakes
  (a decisive, winner-take-all prize) that make the model's danger acute
  are actually in play.
- **Whether "more information reduces safety" survives outside the model's
  own assumptions: record is thin, flagged rather than filled.** Multiple
  searches for a direct technical critique of the information result
  (whether it depends on the continuous-capability, one-shot,
  simultaneous-choice setup, and whether it would reverse under a
  dynamic/repeated-game version) did not surface one. The closest adjacent
  material — a 2021 PLoS One paper extending a related race model (Han et
  al.'s "DSAIR," cited by name in the paper reviewed) — cites Armstrong et
  al. as foundational and builds a variant model but does not test the
  fragility of the information result specifically; it was read and is
  listed under Discarded. This absence should be stated plainly in the
  article rather than implied to be settled: the paper's own authors flag
  the model as deliberately simple ("the simple model is enough to gain
  useful insights"), and no on-record technical rebuttal of the information
  result specifically was found.

## Numbers

- **Model equations (all from source #1, §2, pp. 2-5):**
  - No information: safety s = µ/(en) for µ < en, else s = 1. Disaster
    probability = 1 − µ/(en) for µ < en, else 0.
  - Private information: s(x) = x/(en−e+1) for x < en−e+1, else 1.
    Integrated disaster probability = 1 − µⁿ/[(n+1)(ne−e+1)] for
    µ < en−e+1.
  - Public information: leader's safety s_top = Δ/e for Δ/e < 1, else 1
    (Δ = capability gap between top two teams). Integrated disaster
    probability = 1 − µ/[e(n+1)] for µ < e.
  - Asymptotic comparison (§3.3): private-information danger shrinks as
    1/µⁿ; public-information danger shrinks only as 1/µ — the paper's exact
    account of why more information is worse, and why the effect gets more
    pronounced with more teams (n).
- **Capability-gap timing (fast-follow evidence):**
  - GPT-4 released 14 March 2023 (source #4, own system card, training
    finished August 2022, ~7 months internal testing before launch).
  - First Chinese model to match GPT-4's Epoch Capabilities Index score:
    May 2024 — a 14-month gap (source #9).
  - US-China ECI gap since 2023: average 7 months, range 4-14 months
    (source #9).
  - Open-weight vs. closed frontier ECI gap: ~3 months (Jan 2023-Oct 2025
    reading) widening slightly to ~4 months (through May 2026 reading)
    (source #10).
  - Consumer-GPU-runnable models vs. frontier: 6.3 to 12.4 months lag
    depending on benchmark (source #11).
  - OpenAI o1-preview released 12 September 2024; DeepSeek R1 released 20
    January 2025 — a gap of about 4 months and 8 days, matching source
    #12's "four months later" (cross-checked against independent tertiary
    listings, not just the Lawfare piece itself).
  - On specific benchmarks at release, DeepSeek R1 was reported (via
    aggregator sites, not independently verified against a primary DeepSeek
    technical report in this pass) at 79.8% on AIME 2024 vs. o1's 79.2%,
    and 97.3% on MATH-500 vs. o1's 96.4% — near-parity, not a lasting gap.
    Flag this pair as tertiary-sourced if used; a primary DeepSeek technical
    report would strengthen it.
- **Testing-timeline figures (competitive/schedule pressure on safety):**
  - GPT-4: ~7 months of "evaluating, adversarially testing, and iteratively
    improving" before launch (source #4, primary, first-hand).
  - o3/o4-mini: METR's own evaluation window was three weeks (source #5,
    primary, first-hand, on-record, independent of OpenAI).
  - Secondary, single-origin reporting (source #14) puts some testing
    windows at "just days" — not independently confirmed by this session
    beyond the METR figure above, which is a different (and less dramatic)
    number for a related but not identical claim.
  - OpenAI's own definitional example of an "AI self-improvement" Critical
    capability threshold includes "sped up to just 4 weeks" as a
    hypothetical trigger, not an observed event (source #3, Table 1) — do
    not conflate with the testing-timeline figures above.

## Source assets

- **Figure 1 (a and b), Armstrong, Bostrom & Shulman (2013/2016), p. 6 of
  the FHI report / p. 205 of the journal article.** Two side-by-side line
  charts (2 teams; 5 teams), each plotting AI-disaster probability (y-axis,
  0 to 1) against "relative importance of capability" µ (x-axis, 0 to 10),
  with three curves per chart (no information — solid; private information
  — dashed; public information — dotted), all at enmity e=1. This is the
  single image that could carry the paper's two headline results in one
  look: the downward slope of all three curves shows "more capability
  matters, less danger," and the consistent ordering of the three curves
  (solid lowest, dotted highest) shows the information result — that more
  information is more dangerous — holding at both team counts. A crop must
  keep both panels (2 teams and 5 teams) side by side to preserve the "more
  teams is worse" comparison, keep the axis labels and the three-curve
  legend intact, and should not be relabeled or redrawn — reproduce or
  closely rebuild it from the described data rather than freehand a
  version, since the exact curve shapes are the evidence.
- No other source in this record carries a comparable visual argument;
  Bostrom's Figure 14 (source #2) is the same data restated and is
  redundant with the above. None found beyond this.

## Discarded

- ResearchGate listing page for the journal article — returned a 503
  error on direct fetch; abstract text was instead confirmed via a
  different route (a citation aggregator's cached listing) that matched
  the FHI report's abstract verbatim, so the underlying claim (ORA copy =
  published content) stands, but this specific URL is not usable as a
  citation.
- EA Forum post reviewing "Racing to the Precipice" (part of a paper-review
  sequence) — returned HTTP 403 on fetch; a search for its content
  surfaced only a restatement of the paper's own abstract, no independent
  critique, so nothing was gained even had it loaded.
- Han et al.-derived DSAIR extension paper (PLoS One, 26 January 2021, PMC
  7837463) — read in full via fetch; cites Armstrong et al. as foundational
  and extends the model with positive/negative incentive structures, but
  does not critique or stress-test the information result specifically, so
  it does not fill the "Contradictions" gap on that point. Kept out of the
  numbered Sources list because it contributes no direct quote or figure
  used in the piece.
- OpenAI's "Introducing OpenAI o1-preview" announcement page — returned
  HTTP 403 on direct fetch; the September 2024 release date was instead
  confirmed via independent tertiary listings (Wikipedia's "OpenAI o1"
  entry, cross-checked against the Lawfare piece's own dating), which
  agreed, so the date is usable but not from a first-hand read of OpenAI's
  own announcement.
- Financial Times original article (multiple candidate URLs) — direct
  fetch of ft.com was blocked outright by the fetch tool, not merely
  paywalled; see source #14 above for how this was handled (used only via
  secondary retellings, clearly flagged as such, not treated as
  independently verified).
- Future of Life Institute "AI Safety Index" (Winter 2025, Summer 2025) —
  identified via search as a serious governance/grading report scoring
  developers on safety practices, potentially useful empirical texture on
  "does competitive pressure show up as worse safety scores," but not
  opened and read in this pass given the source count was already well
  covered without it; flagged here in case the writer wants a governance
  index for additional texture rather than as evidence already verified.
