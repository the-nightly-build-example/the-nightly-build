# Evidence record: what-could-go-wrong/algorithmic-collusion (01)

The record supports the lesson's spine cleanly. The worry has a named origin and a
precise statement (Ezrachi and Stucke, defended in their own 2020 paper). Two
simulation results are documented from their own papers: Q-learning agents reaching
supra-competitive prices with punishment strategies (Calvano, Calzolari, Denicolò,
Pastorello), and LLM pricing agents doing the same and swinging on prompt wording
(Fish, Gonczarowski, Shorrer). A third simulation extends the behavior to market
division under modern LLMs (Lin, Ojha, Cai, Chen). The one real-world enforcement
action, DOJ v. RealPage, is documented as a shared-data, common-algorithm scheme
among competing landlords, which is a different mechanism from autonomously learned
collusion and must not be blurred into it. The skeptical case is documented from a
primary that re-examined the Calvano code (den Boer, Meylahn, Schinkel) and a
critical review (Dorner). A regulator synthesis (OECD 2023) supplies the present
state: concern is live, remedies are debated, and no autonomous-collusion case
exists.

Where the record is thin, and the writer must respect it: every demonstrated result
is a simulation in a simplified market. There is no documented case of independent
pricing algorithms learning to collude in a real market. The extrapolation to
open markets at scale is argued (Ezrachi and Stucke) but not shown. The further
extrapolation to agents coordinating against human oversight in safety settings is
conjecture with no pricing-literature evidence behind it, and is flagged as such in
Contradictions. The Calvano and CPI documents read are the April-2019 working paper
and the authors' 2020 summary; page numbers for the published AER article are taken
from the working paper the FTC hosts, and the den Boer critique quotes the AER page
numbers directly. The Fish paper has been revised repeatedly since 2024; the version
read (arXiv, current) runs its main duopoly on GPT-4 (0613) and adds later-model
robustness, so cite it as a living paper, not a fixed 2024 result.

## Sources

```text
URL:         https://ora.ox.ac.uk/objects/uuid:fde32e64-30b0-41b8-9477-de4cc716d902
Kind:        primary. Ezrachi and Stucke own the argument; this is their own paper
             stating and defending it. Full text hosted at the same Oxford record
             (file m4ccfcc7d271be9b6a42f5ca60b02e26f), which is the copy read.
Establishes: The argument at full strength and its origin. Ariel Ezrachi (Slaughter
             and May Professor of Competition Law, University of Oxford) and Maurice
             E. Stucke (Professor of Law, University of Tennessee) first laid out the
             worry across four scenarios and their 2016 book "Virtual Competition:
             The Promise and Perils of the Algorithm-Driven Economy" (Harvard
             University Press). This 2020 paper restates the four scenarios, defends
             the two contested ones against skeptics, and argues the law-theory gap.
Paraphrase:  They name four ways algorithms can produce collusion: Messenger
             (algorithms carry out a human cartel), Hub and Spoke (competitors use a
             common third-party algorithm), Predictable Agent ("Tacit Collusion on
             Steroids", firms unilaterally use algorithms intending to sustain
             conscious parallelism), and the fourth, "Artificial Intelligence, God
             View, and the Digital Eye", where machines reach the anticompetitive
             outcome on their own. They report broad agreement on the first two and
             active debate on the last two. Their core legal claim: tacit collusion
             without a provable agreement escapes Article 101 TFEU and Sherman Act
             Section 1, because those need a "meeting of the minds".
Locators:    Abstract; introduction (four scenarios, "In 2016 we provided further
             context... in our book, Virtual Competition"); the paragraph naming the
             third and fourth scenarios; the "escape antitrust scrutiny" paragraph.
Quote:       "In the fourth scenario, we predicted that, in the future, algorithms
             may arrive at this anticompetitive outcome on their own."
Quote:       "Some economists, however, downplay algorithmic tacit collusion as
             unlikely, if not impossible. 'Keep calm and carry on' they argue."
```

```text
URL:         https://www.aeaweb.org/articles?id=10.1257/aer.20190623
Kind:        primary. The four authors own the demonstrated result. Published as
             Calvano, Calzolari, Denicolò, Pastorello (2020), American Economic
             Review 110(10): 3267-97. The full text read is the authors' April 2019
             working paper (SSRN 3304991), hosted openly by the FTC at
             https://www.ftc.gov/system/files/documents/public_events/1494697/calzolaricalvanodenicolopastorello.pdf
Establishes: The central demonstrated-in-simulation result. Emilio Calvano
             (University of Bologna), Giacomo Calzolari (European University
             Institute), Vincenzo Denicolò (University of Bologna), and Sergio
             Pastorello (University of Bologna) ran Q-learning pricing algorithms in
             a repeated Bertrand duopoly and found they consistently learned
             supra-competitive prices without communicating and without being told to
             collude. This is a computer simulation, not a field study.
Paraphrase:  Two Q-learning agents, each seeing only past prices, repeatedly set
             prices in a logit-demand oligopoly. They converge to prices above the
             one-shot Bertrand-Nash level, sustained by reward-punishment strategies:
             an undercut is followed by a finite punishment phase and then a gradual
             return to the pre-deviation price. The authors call this the first clear
             documentation of collusive strategies (not just outcomes) among
             autonomous pricing algorithms. They stress the strategies are learned by
             trial and error, with no design, communication, or prior knowledge, and
             they note no antitrust case had been brought against autonomously
             colluding algorithms.
Locators:    Abstract; introduction (p. 3268, "learn to collude tacitly", "no one has
             brought an antitrust case"); results, average profit gain Δ definition
             (eq. 9) and Figure 2; deviation-and-punishment section (p. 3282,
             one-period deviation experiment).
Quote:       "We find that the algorithms consistently learn to charge
             supra-competitive prices, without communicating with one another. The
             high prices are sustained by classical collusive strategies with a finite
             phase of punishment followed by a gradual return to cooperation."
Quote:       "Clearly, the exogenous deviation gets punished. The punishment is not as
             harsh as it could be... and it is only temporary."
```

```text
URL:         https://www.competitionpolicyinternational.com/wp-content/uploads/2020/07/4-Algorithmic-Collusion-A-Real-Problem-for-Competition-Policy-By-Emilio-Calvano-Giacomo-Calzolari-Vincenzo-Denicol%C3%B2-Sergio-Pastorello.pdf
Kind:        primary. The same four authors summarizing their own study for a policy
             audience (CPI Antitrust Chronicle, July 2020). They own the claims; the
             outlet is a trade journal.
Establishes: The authors' own plain-language statement of what they showed and its
             legal stakes, and useful framing of the prior literature (Klein 2018).
Paraphrase:  They recap that reinforcement-learning algorithms learned supra-
             competitive prices in their experiments, place the finding against
             earlier work (Klein's homogeneous-goods Q-learning reaching roughly
             midway between competitive and monopoly profit), and state the legal
             difficulty: in most countries, including the US and Europe, tacit
             collusion in practice is not treated as illegal, for reasons they list
             (it is seen as hard to achieve, hard to detect, and hard to remedy).
Locators:    Sections on the modelling literature (Klein "roughly mid-way"); the
             legal-treatment paragraph ("tacit collusion in practice is not regarded
             as illegal").
Quote:       "in most countries (including the U.S. and Europe) tacit collusion in
             practice is not regarded as illegal."
```

```text
URL:         https://arxiv.org/abs/2404.00806
Kind:        primary. Fish, Gonczarowski, Shorrer own this demonstrated result.
Establishes: The second demonstrated-in-simulation result, updated to large language
             models. Sara Fish, Yannai A. Gonczarowski, and Ran I. Shorrer show LLM
             pricing agents reaching supra-competitive prices, and that small prompt
             changes move the degree of pricing sharply. A simulation, in a simple
             fixed-horizon Bertrand setting.
Paraphrase:  LLM agents set prices over 300 periods in a repeated logit Bertrand
             duopoly, each seeing all prices and its own demand. They reach
             supra-competitive prices and profits quickly and without being told to
             collude. Two prompt prefixes differing only in emphasis produce very
             different pricing: the prompt stressing long-run profit (P1) yields much
             higher prices, sometimes near monopoly, than the prompt mentioning
             undercutting and quantity sold (P2). Text-log analysis attributes part of
             the gap to price-war avoidance; an implantation test that inserts
             price-war-concern sentences raises subsequent prices. The main duopoly
             runs use GPT-4 (0613); later revisions add robustness on newer models.
             The authors shut off all communication except through price.
Locators:    Abstract; Sections 2-3 (setup, prompt prefixes P1/P2, price results vs
             Bertrand-Nash); Section 4 (price-war analysis, implantation, Table 1
             reward-punishment coefficient); Section 6 (limitations).
Quote:       "In oligopoly settings, LLM-based pricing agents quickly and
             autonomously reach supracompetitive prices and profits. Variation in
             seemingly innocuous phrases in LLM instructions ('prompts') substantially
             influence the degree of supracompetitive pricing."
Quote:       "our economic environment is simple and does not capture many real-world
             complexities, and we focus on one fixed time horizon."
```

```text
URL:         https://arxiv.org/abs/2410.00031
Kind:        primary. Lin, Ojha, Cai, Chen own this demonstrated result.
Establishes: That the simulated behavior extends past single-good pricing to market
             division, under current-generation LLMs. Ryan Y. Lin, Siddhartha M.
             Ojha, Kevin Cai, and Maxwell F. Chen (California Institute of Technology)
             find LLM agents in a multi-commodity Cournot game can each monopolize
             specific commodities, dividing the market, without explicit instruction
             or direct communication. A simulation.
Paraphrase:  In an infinite-horizon multi-commodity Cournot competition, paired LLM
             agents (same model against itself) adjust quantities and allocation so
             that each firm dominates particular commodities, raising profit at
             consumer expense. Models run include OpenAI o4-mini, GPT-4.1 and
             GPT-4.1-mini, DeepSeek-V3, Anthropic Claude-3.7-Sonnet, and Google
             Gemini-1.5 Pro. The authors note limits, including context windows
             affecting decision retention, and frame the market as a simplified
             design choice.
Locators:    Abstract; Section on model setup (six models listed); simulation-design
             paragraph (infinite-horizon choice); limitations paragraph.
Quote:       "Our findings demonstrate that LLMs can effectively monopolize specific
             commodities by dynamically adjusting their pricing and resource
             allocation strategies."
```

```text
URL:         https://papers.tinbergen.nl/22067.pdf
Kind:        primary. den Boer, Meylahn, Schinkel re-examine the Calvano algorithm
             and own their critique. Tinbergen Institute Discussion Paper 2022-067/VII
             (Dec 2022); later published as "Artificial Collusion" in Management
             Science (2024), doi:10.1287/mnsc.2024.08557.
Establishes: The credible deflationary case, from inside the code. Arnoud V. den Boer
             and Maarten Pieter Schinkel (University of Amsterdam) with Janusz M.
             Meylahn (University of Twente) argue the Calvano result does not show a
             practical cartel threat.
Paraphrase:  Their objections: (1) timescale. Learning takes hundreds of thousands to
             millions of periods, beyond any horizon that matters to a firm's profit,
             so the collusive equilibrium is reached on a timescale "almost irrelevant
             from the firm's point of view". (2) Fragile setup. The result assumes two
             competitors committed to the same Q-learning algorithm, same
             hyperparameters and action space, started at the same moment;
             synchronization in particular is hard to relax. (3) Not robust to
             alternatives. Against a simple different algorithm (Exp3), Q-learning
             performs worse, so a profit-seeking firm would not commit to it. (4)
             Averaged evidence. The punishment figure is an average and cannot show
             that most individual runs actually punish. They argue existing simple
             algorithms do not meet the conditions for a real threat, and set out what
             a genuinely dangerous colluding algorithm would require.
Locators:    Abstract ("no immediate reason for alarm"); convergence-timescale
             section (quoting AER pp. 3269, 3276); Section 5 (Exp3 comparison);
             critique of the deviation figure (AER p. 3282); Section 6 (what is
             needed).
Quote:       "A detailed analysis of the inner workings of this algorithm reveals that
             there is no immediate reason for alarm. We set out what is needed to
             demonstrate the existence of a colluding price algorithm that does form a
             threat to competition."
```

```text
URL:         https://www.justice.gov/atr/case/us-and-plaintiff-states-v-realpage-inc
Kind:        primary. The US Department of Justice owns these allegations. Case page.
             The documents read are the DOJ settlement press release
             (https://www.justice.gov/opa/pr/justice-department-requires-realpage-end-sharing-competitively-sensitive-information-and)
             and the Proposed Final Judgment PDF (justice.gov/opa/media/1419406/dl,
             filed 24 Nov 2025).
Establishes: The real-world adjacent case, kept distinct from autonomous learning.
             DOJ and eight states sued RealPage on 23 Aug 2024 for a shared-data,
             common-algorithm scheme: competing landlords fed nonpublic,
             competitively sensitive rental data into RealPage's revenue-management
             software, which returned aligned price recommendations. This is
             coordination through a common tool and shared private data, not
             independent algorithms autonomously converging on high prices.
Paraphrase:  Under licensing agreements, competing landlords supplied RealPage daily
             nonpublic data (renewals, terms, prices). The software used that pooled
             rival data to recommend rents, with an "Auto Accept" feature that
             implements the recommendation within set parameters. DOJ alleges this
             suppressed independent pricing and aligned rents. The complaint pleads
             Sherman Act Sections 1 and 2. A proposed settlement (Nov 2025) bars the
             sharing of competitively sensitive nonpublic information and constrains
             the pricing tool.
Locators:    Settlement press release (RealPage "relied on nonpublic, competitively
             sensitive information shared by landlords to set rental prices");
             Proposed Final Judgment, Recitals and Definitions (Sherman Sections 1 and
             2; "Auto Accept"; "Competitively Sensitive Information"; "Nonpublic
             Data").
Quote:       "The Complaint states claims upon which relief may be granted against
             Defendant under Sections 1 and 2 of the Sherman Act (15 U.S.C. §§ 1, 2)."
Quote:       "RealPage's revenue management software has relied on nonpublic,
             competitively sensitive information shared by landlords to set rental
             prices."
```

```text
URL:         https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/05/algorithmic-competition_2be02d00/cb3b2075-en.pdf
Kind:        primary. The OECD Secretariat owns this policy synthesis. "Algorithmic
             Competition", OECD Competition Policy Roundtable Background Note (2023),
             DAF/COMP(2023)3.
Establishes: The present regulator position and the state of real-world evidence.
             The OECD treats autonomous self-learning collusion as a live concern but
             records that no such case has been seen, and separates the mechanisms and
             remedies.
Paraphrase:  The note revisits the 2017 "Algorithms and Collusion" work. It names the
             threat of autonomous self-learning algorithms reaching collusive outcomes
             without being programmed to, and treats it as an ongoing enforcer
             concern. It distinguishes coordinated conduct where there is an explicit
             agreement or a common software provider (a hub-and-spoke setting) from
             autonomous tacit collusion, and states that, as far as the Secretariat is
             aware, there have been no autonomous tacit collusion cases. It surveys
             remedies authorities can consider and how they might investigate
             algorithms directly.
Locators:    Executive summary (autonomous self-learning threat); Section 3.1
             (algorithmic coordinated conduct, three mechanisms; "there have not been
             any autonomous tacit collusion cases"); Chapter 4 (investigating
             algorithms, remedies).
Quote:       "the threat posed by autonomous self-learning algorithms... that have the
             potential to reach collusive outcomes without being explicitly programmed
             to do so."
Quote:       "As far as the Secretariat is aware, there have not been any autonomous
             tacit collusion cases."
```

```text
URL:         https://arxiv.org/pdf/2110.04740
Kind:        secondary. Dorner reviews and weighs the literature from outside the
             authoring parties. "Algorithmic collusion: A critical review", Florian E.
             Dorner (Institute of Science, Technology and Policy, ETH Zurich).
Establishes: A synthesized skeptical reading, from a computer-science vantage, of
             whether the simulation evidence transfers to real markets.
Paraphrase:  The review argues the antitrust literature overestimates how far recent
             machine-learning progress applies to the coordination problem real
             cartels face, and that the models supporting learned collusion use simple
             market simulations and simple algorithms that avoid the hard problems of
             real-world learning. It concludes it is likely too early to change
             antitrust law to handle self-learning algorithms colluding in real
             markets, while hub-and-spoke arrangements through centralized pricing
             algorithms may already warrant action. It cites Schwalbe's conclusion
             that algorithmic collusion currently looks far harder to achieve than
             legal scholars assume.
Locators:    Abstract; introduction; the "strong evidence... in real markets"
             discussion; the cooperative-AI passage (DeepMind researchers).
Quote:       "it is likely too early to adapt antitrust law to be able to deal with
             self-learning algorithms colluding in real markets, [while] other forms
             of algorithmic collusion, such as hub-and-spoke arrangements facilitated
             by centralized pricing algorithms might already warrant legislative
             action."
```

## Contradictions

- The central dispute is whether the Calvano simulation implies a real-market
  threat. Calvano et al. call it the first clear documentation of learned collusive
  strategies. den Boer, Meylahn, Schinkel, examining the same algorithm, find "no
  immediate reason for alarm" because the learning timescale is irrelevant to a firm,
  the setup requires committed, synchronized, identical algorithms, and Q-learning is
  beaten by a simple alternative. Dorner reaches the same deflationary conclusion from
  the literature. The writer should present both from their primaries and not resolve
  it as settled.

- Ezrachi and Stucke argue the fourth scenario, machines colluding on their own in
  real markets, is a real forward risk. Every demonstrated result behind it is a
  simulation. There is no field case: the OECD note records no autonomous tacit
  collusion case, and Calvano et al. note none had been brought. The demonstrated and
  the extrapolated must stay visibly separate.

- The RealPage case cuts against blurring the categories. It is a shared-data,
  common-algorithm coordination case pleaded under Sherman Sections 1 and 2, not a
  case of independent algorithms learning to collude. It shows the mechanism the OECD
  and Dorner say is the near-term concern (hub-and-spoke via a common tool), not the
  autonomous scenario. Using RealPage as proof of autonomous collusion would be an
  error the evidence does not support.

- The safety-relevant extrapolation in the commission, agents coordinating against
  human oversight, has no support in the pricing literature read. No source here
  studies agents colluding to evade a human overseer. The Lin et al. and Fish et al.
  results are market simulations about profit, not oversight. Treat that extension as
  conjecture with no primary behind it, or cut it. Flagged as unverifiable from this
  record.

- Prompt sensitivity in Fish et al. cuts two ways. It shows LLM pricing is not
  robustly collusive: wording moves it from near-competitive to near-monopoly. That
  both raises the concern (innocuous phrasing can induce it) and undercuts it (the
  behavior is fragile and instruction-dependent), and the writer should present both
  readings.

## Numbers

```text
Figure: Average profit gain Δ = (π − πN)/(πM − πN); Δ=0 is Bertrand-Nash competitive,
        Δ=1 is monopoly. Baseline duopoly Δ ranges 70%-90% across the learning-rate
        and exploration grid; ≈85% at the grid mid-point (α=0.125, β=1e-5).
Owner:  Calvano, Calzolari, Denicolò, Pastorello (working paper / AER 2020).
Scope:  Mean over 1,000 independent sessions per cell; two ex-ante symmetric agents,
        logit-demand repeated Bertrand duopoly; standard error of Δ typically < 1 pt.
```

```text
Figure: Convergence takes ~400,000 to several million periods; ~850,000 at the grid
        mid-point.
Owner:  Calvano et al.
Scope:  Periods of the repeated game to convergence; the den Boer critique rests on
        this being far beyond any economically relevant horizon.
```

```text
Figure: With an outside demand shock / three-firm and uncertainty extensions, Δ falls
        to about 56%, rising to ~62% with more persistence (ρ=99.99%).
Owner:  Calvano et al. (robustness sections).
Scope:  Still well above the competitive benchmark; shows the result is not confined
        to the frictionless baseline.
```

```text
Figure: Earlier Q-learning baseline (Klein) reached profit "roughly mid-way" between
        competitive and monopoly, i.e. average profit gain ≈50%.
Owner:  Klein (2018), as reported by Calvano et al. and the CPI summary.
Scope:  Homogeneous-goods, Maskin-Tirole staggered-pricing model; context for how the
        result grew with a larger action set. Cite as reported-via, not read firsthand.
```

```text
Figure: LLM prompt effect: prompt P1 (long-run-profit emphasis) yields significantly
        higher prices than P2, sometimes near monopoly; main duopoly on GPT-4 (0613),
        300 periods.
Owner:  Fish, Gonczarowski, Shorrer.
Scope:  Repeated logit Bertrand duopoly; direction and significance are the load-
        bearing facts, not any single price level (which shifts across paper versions).
```

```text
Figure: Autonomous-collusion enforcement cases to date: zero.
Owner:  OECD (2023); consistent with Calvano et al.'s 2019 statement that no case had
        been brought.
Scope:  Real-world antitrust cases of independent algorithms autonomously colluding.
        RealPage is a shared-data case, not this category.
```

```text
Figure: In 2015, more than a third of vendors in a sample of 1,600+ best-selling
        Amazon items had automated pricing.
Owner:  Chen et al. (2016), as reported by Calvano et al.
Scope:  Context on real adoption of algorithmic pricing. Cite as reported-via; a dated
        figure the writer should present as of 2015, not as current.
```

## Source assets

```text
Asset: Calvano et al., Figure 2 (the working paper's heat-map of Δ over the α, β grid).
Shows: That supra-competitive outcomes are common across learning/exploration
       settings, not a knife-edge, with Δ mostly in the 70%-90% band.
Crop:  Must keep the color scale and both axis labels (α, β) and the Δ legend; a crop
       that drops the scale turns evidence into decoration.
```

```text
Asset: Calvano et al., deviation-and-punishment figure (p. 3282 area): prices (top) and
       profits (bottom) for τ periods after a one-period deviation.
Shows: The reward-punishment mechanism directly, an undercut, a temporary dip, a
       gradual return, which is the heart of the "learned strategy, not just outcome"
       claim.
Crop:  Must retain the pre-deviation baseline, the deviation period, and the recovery
       tail; cropping to the dip alone hides the "temporary and gradual" point den Boer
       disputes.
```

```text
Asset: Fish, Gonczarowski, Shorrer, Figure 2 (price series under P1 vs P2 against the
       Bertrand-Nash line).
Shows: Both prompts run above the competitive line and P1 runs far higher, making the
       prompt-sensitivity and supra-competitive facts visible at once.
Crop:  Must keep the Bertrand-Nash reference line and the P1/P2 distinction; without
       the reference line "high price" has no meaning.
```

```text
Asset: OECD (2023), the taxonomy of algorithmic coordinated-conduct mechanisms in
       Section 3.1.
Shows: The line between hub-and-spoke / common-software coordination and autonomous
       tacit collusion, the exact distinction the lesson must hold (and RealPage sits
       on the near side of).
Crop:  None found as a single strong graphic; the value is the categorical text, better
       used as prose than as an image.
```

## Discarded

```text
URL: https://www.aeaweb.org/articles/pdf/doi/10.1257/aer.20190623 — gated AER full
     text; returns the landing page only. Used the FTC-hosted working paper for the
     text and the AER landing page as the canonical citation.
URL: https://papers.ssrn.com/sol3/Delivery.cfm/4213600.pdf?abstractid=4213600 — SSRN
     anti-bot page, not the PDF. Read the den Boer paper via the Tinbergen host instead.
URL: https://ir.law.utk.edu/cgi/viewcontent.cgi?article=1042&context=book_chapters —
     403 Forbidden. Used the Ezrachi and Stucke 2020 Oxford paper for their own words.
URL: https://www.justice.gov/opa/pr/justice-department-sues-realpage-algorithmic-pricing-scheme-harms-millions-american — original Aug 2024 press release returned empty
     on fetch; used the DOJ case page, the settlement release, and the Proposed Final
     Judgment, which carry the same allegations.
URL: Various law-firm client alerts (Wilson Sonsini, Cooley, Fenwick, Freshfields,
     Holland & Knight) on RealPage — secondary commentary; went to the DOJ documents
     they summarize.
URL: https://marginalrevolution.com/... on Fish et al. — blog commentary; went to the
     arXiv paper.
```
