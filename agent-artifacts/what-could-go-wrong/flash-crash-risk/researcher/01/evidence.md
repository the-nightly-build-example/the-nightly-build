# Evidence: what-could-go-wrong / flash-crash-risk

Floor met: 8 sources, 5 primary, 3 secondary. Every URL below was opened and
returns a live response (checked 2026-09-09; the proof blocks only on 404/410 or
a domain that does not resolve). Several government PDFs refuse a scripted curl
(HTTP 403) but were read in full via the agent fetcher; each figure below is a
verbatim passage from the document itself. github.com not used (blocked here).

Neighbor distinction (kept out of the argument, linked in Background): this piece
is about speed plus strategy sameness producing sudden instability (crashes). It
is NOT algorithmic-collusion (pricing algorithms learning high prices) and NOT
algorithmic-monoculture (correlated decision/hiring errors).

---

## S1 — PRIMARY. U.S. CFTC & SEC · "Findings Regarding the Market Events of May 6, 2010" (Sept 30, 2010)
URL: https://www.sec.gov/news/studies/2010/marketevents-report.pdf
The official joint report. Supports the demonstrated case: size, timing,
recovery, trigger, and mechanism.

Verbatim:
- "That afternoon, major equity indices in both the futures and securities
  markets, each already down over 4% from their prior-day close, suddenly
  plummeted a further 5-6% in a matter of minutes before rebounding almost as
  quickly." ... "By the end of the day, major futures and equities indices
  'recovered' to close at losses of about 3% from the prior day."
- "At 2:32 p.m. ... a large fundamental trader (a mutual fund complex) initiated
  a sell program to sell a total of 75,000 E-Mini contracts (valued at
  approximately $4.1 billion) as a hedge to an existing equity position."
- "This large fundamental trader chose to execute this sell program via an
  automated execution algorithm ('Sell Algorithm') that was programmed to feed
  orders into the June 2010 E-Mini market to target an execution rate set to 9%
  of the trading volume calculated over the previous minute, but without regard
  to price or time."
- "on May 6, when markets were already under stress, the Sell Algorithm chosen
  by the large trader to only target trading volume, and neither price nor time,
  executed the sell program extremely rapidly in just 20 minutes."
- "In the four-and-one-half minutes from 2:41 p.m. through 2:45:27 p.m., prices
  of the E-Mini had fallen by more than 5% and prices of SPY suffered a decline
  of over 6%."
- Hot-potato / homogeneity mechanism: "HFTs began to quickly buy and then resell
  contracts to each other – generating a 'hot-potato' volume effect as the same
  positions were rapidly passed back and forth. Between 2:45:13 and 2:45:27,
  HFTs traded over 27,000 contracts, which accounted for about 49 percent of the
  total trading volume, while buying only about 200 additional contracts net."
- "At the same time, HFTs traded nearly 140,000 E-Mini contracts or over 33% of
  the total trading volume."
- Recovery: "By approximately 3:00 p.m., most securities had reverted back to
  trading at prices reflecting true consensus values."
- Broken trades / stub quotes: "over 20,000 trades (many based on
  retail-customer orders) across more than 300 separate securities ... were
  executed at prices 60% or more away from their 2:40 p.m. prices" ... "trades
  being executed at irrational prices as low as one penny or as high as
  $100,000. These trades occurred as a result of so-called stub quotes."
- Lesson (mechanism): "under stressed market conditions, the automated execution
  of a large sell order can trigger extreme price movements, especially if the
  automated execution algorithm does not take prices into account ... a
  liquidity crisis can develop if many market participants withdraw at the same
  time."
- Circuit breakers: staffs are considering "recalibrating the existing
  market-wide circuit breakers – none of which were triggered on May 6."

## S2 — PRIMARY. Kirilenko, Kyle, Samadi & Tuzun · "The Flash Crash: The Impact of High Frequency Trading on an Electronic Market" (working paper; published Journal of Finance 72(3):967–998, 2017)
URL: https://www.cftc.gov/sites/default/files/idc/groups/public/@economicanalysis/documents/file/oce_flashcrash0314.pdf
Peer-reviewed audit-trail analysis. Supports the careful attribution: HFTs did
not cause it, but their reaction deepened it.

Verbatim (abstract):
- "We show that High Frequency Traders (HFTs) did not cause the Flash Crash, but
  contributed to it by demanding immediacy ahead of other market participants."
- "A large enough sell order can lead to a liquidity-based crash accompanied by
  high trading volume and large price volatility – which is what occurred in the
  E-mini S&P 500 stock index futures contract on May 6, 2010, and then quickly
  spread to other markets."
- Policy: regulation should "encourage HFTs to provide immediacy, while
  discouraging them from demanding it ... a more diligent use of short-lived
  trading pauses."
Note: these were rule-based HFT strategies, not machine-learning or LLM agents.

## S3 — PRIMARY. U.S. CFTC · Press Release 7156-15, "CFTC Charges U.K. Resident Navinder Singh Sarao ... with Price Manipulation and Spoofing" (Apr 21, 2015)
URL: https://www.cftc.gov/PressRoom/PressReleases/7156-15
The spoofing prosecution. Supports the "contributed to" nuance without
overclaiming Sarao caused the crash.

Verbatim:
- Charges: "unlawfully manipulating, attempting to manipulate, and spoofing —
  all with regard to the E-mini S&P 500 near month futures contract."
- "Defendants utilized the Layering Algorithm continuously, for over two hours,
  immediately prior to the precipitous drop in the E-mini S&P price, applying
  close to $200 million worth of persistent downward pressure."
- "Defendants' manipulative activities contributed to an extreme E-mini S&P
  order book imbalance that contributed to market conditions that led to the
  Flash Crash."
Note: the 2010 joint report did not name Sarao; this later action added a
spoofer's layering as a contributing factor. Also rule-based automation.

## S4 — PRIMARY (research). Ross, So, De Simone, Pozniak & Lo · "Why Better Models Can Create Riskier Systems: Evidence from LLM Agents in Financial Markets" (arXiv 2609.04373, submitted Sept 3, 2026)
URL: https://arxiv.org/abs/2609.04373
The AI-agent side. Explicitly a simulation, not a market event. Andrew W. Lo
(MIT) among authors.

Verbatim:
- "We show that improving individual model capability can degrade rather than
  improve system-level outcomes."
- "frontier LLMs exhibit significantly correlated behavior that increases with
  capability."
- "when agents share a common misinformation environment, the same correlated
  behavior becomes a liability."
- Thesis: "improving individual models does not necessarily produce better
  system-level outcomes."
Method: "an agent-based simulation with LLM traders of varying general-purpose
capability." NOT a recorded real-market event.

## S5 — SECONDARY (regulatory review). Bank of England · "Financial Stability in Focus: Artificial intelligence in the financial system" (2025)
URL: https://www.bankofengland.co.uk/-/media/boe/files/financial-stability-in-focus/2025/financial-stability-in-focus-artificial-intelligence-in-the-financial-system.pdf
Present-day argument from a central bank.

Verbatim:
- "AI-driven trading and investment strategies could increase the tendency for
  market participants to take correlated positions ... [from] similar model
  designs across the market. Herding and market concentration was the top risk
  cited in recent IMF outreach when stakeholders were asked about risks that
  could result from wider adoption of generative AI in capital markets."
- "Advanced AI models could rationally exploit profit-making opportunities in a
  destabilising way or engage in other adverse behaviours."
- Defines "agentic AI (that is, systems which can take autonomous action to
  achieve specified goals ...)"; notes "risks around herding in markets,
  potentially leading to procyclical fire-sales, are not new."

## S6 — SECONDARY (regulatory review). IMF · Global Financial Stability Report, Oct 2024, Ch.3 "Advances in Artificial Intelligence: Implications for Capital Market Activities"
URL: https://www.imf.org/-/media/Files/Publications/GFSR/2024/October/English/ch3.ashx
Present-day argument, and it steelmans the other side too.

Verbatim:
- Both sides: "AI may actually reduce financial stability risks by enabling
  superior risk management, deepening market liquidity, and improving market
  monitoring ... At the same time, new risks may arise: Increased market speed
  and volatility under stress, especially if trading strategies of AI models all
  respond to a shock in a similar manner or shut down in response to an
  unforeseen event."
- Names the failure mode: "liquidity, excess volatility, and flash crashes —
  arising from fast-paced decision making and ineffectiveness of guardrails."
- "Automated trading algorithms have helped markets move faster and digest large
  trades more efficiently in major asset classes such as US equities."
- "Participants in the IMF outreach cited potential herding and market
  concentration as a key financial stability risk."
- Policy ask: "Undertake the calibration of circuit breakers and a review of
  margining practices in light of potentially rapid AI-driven price moves."

## S7 — SECONDARY (regulatory review). U.S. SEC · Press Release 2012-107, "SEC Approves Proposals to Address Extraordinary Volatility in Individual Stocks and Broader Stock Market" (June 1, 2012)
URL: https://www.sec.gov/newsroom/press-releases/2012-2012-107htm
The concrete policy response to 2010: what "circuit breakers" the argument's
present-day proponents want recalibrated already exist.

Verbatim:
- Limit up-limit down "prevents trades in individual exchange-listed stocks from
  occurring outside of a specified price band."
- Updated market-wide circuit breakers "when triggered, halt trading in all
  exchange-listed securities throughout the U.S. markets."
- "The market-wide circuit breakers were not triggered during the severe market
  disruption of May 6, 2010, which led the exchanges and FINRA, in consultation
  with SEC staff, to assess whether the circuit breakers needed to be updated in
  light of today's market structure."

## S8 — PRIMARY. U.S. CFTC & SEC · "Preliminary Findings Regarding the Market Events of May 6, 2010" (May 18, 2010)
URL: https://www.sec.gov/sec-cftc-prelimreport.pdf
Contemporaneous primary. Establishes the market was already falling before 2:30.

Verbatim:
- "between 9:30 a.m. and 2:00 p.m., the Dow Jones Industrial Average (DJIA)
  declined 161 points to 10,712 (-1.5%)."
- Short-sale detail: "short sales accounted for approximately 70% of executions
  against stub quotes between 2:45 p.m. and 2:50 p.m., and approximately 90% of
  executions against stub quotes between 2:50 p.m. and 2:55 p.m."

---

## Unsourceable / avoided
- The oft-quoted "998.5 points / ~$1 trillion" Dow figure appears in the primary
  reports only as percentages (indices already down >4%, then a further 5-6%; by
  2 p.m. the DJIA was down 1.5% to 10,712). The lesson therefore uses the
  report's own percentage figures, not a point/dollar figure I could not confirm
  in a primary I opened.
- github.com blocked (egress 403): no GitHub URLs used.
- SSRN, Wiley, justice.gov, and several news sites sit behind bot challenges and
  could not be read; the CFTC-hosted Kirilenko working paper and the CFTC Sarao
  release were used in their place, and both were read in full.
