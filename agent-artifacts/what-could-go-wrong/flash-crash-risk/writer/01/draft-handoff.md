# Draft handoff: what-could-go-wrong / flash-crash-risk

## Status
Self-proof clean. `./nb check --series what-could-go-wrong`: BLOCK 0, WARN 0,
verdict PUBLISHABLE. Stamped words 2148 (band 1200-2200), sources 8 (5 primary,
3 secondary), reading 9 min.

## Headline and dek
- Title: "Automated trading crashed the market once, in 2010, with no AI involved"
- Dek (identical in dekline and nb-meta): "A rule-based sell order and a herd of
  high-frequency traders drove the 2010 Flash Crash, while the case that AI
  agents will cause the next one still rests on simulations."

## What the lesson teaches (the commission's short list, in order)
1. Orientation ("How automated selling can feed on itself"): the argument at full
   strength. Speed plus strategy sameness, correlated withdrawal, a feedback loop
   too fast for humans. Defines high-frequency trading and liquidity. Steelmans
   the worry via Kirilenko's "demand for immediacy" [1] and the IMF's speed/
   volatility framing [2]. Names the distinction from algorithmic-collusion and
   algorithmic-monoculture in prose (plain links), and both are linked again in
   Background. They are not re-argued.
2. "Inside the twenty minutes the market broke": the one demonstrated case, told
   from the primary record. Pre-2:30 stress [3]; the $4.1B / 75,000-contract Sell
   Algorithm targeting 9% of volume without regard to price [4]; the hot-potato
   (27,000 contracts in 14 seconds, ~49% of volume, ~200 net) [4]; E-mini -5%,
   SPY -6% in 4.5 min; indices already -4% then a further 5-6%; recovery by 3pm,
   close ~-3%; 20,000+ trades broken, penny-to-$100,000 stub prints [4]. Stat
   strip carries size/timing.
3. "The one real crash ran on rule-based code": the correction. The Sell
   Algorithm and the HFTs were rule-based, not ML/LLM [4][1]; Kirilenko: HFTs did
   not cause it but contributed by demanding immediacy [1]; Sarao's spoofing
   "contributed to" conditions per the CFTC, with the report's careful non-naming
   preserved [5]. All pre-modern-AI.
4. "The AI version of the worry lives in simulations": the analogy/guesswork
   side. Ross/So/Lo 2026 simulation (correlated behavior grows with capability;
   shared misinformation makes it a liability), flagged explicitly as an
   agent-based simulation, not a market [6]; BoE [7] and IMF [2] herding worries;
   no AI-caused crash on record.
5. "What would settle whether AI makes crashes worse": present-day. Who presses
   it (IMF, BoE, agent researchers) and what they want (recalibrated circuit
   breakers, margin review, agentic-AI oversight) [2][7]; existing tools from the
   SEC's post-2010 response [8]. The gap named both ways; the IMF's own two-sided
   case (AI could also reduce risk) [2]. Holds-up grid = demonstrated vs analogy.
   Body closes on the evidence question, not a verdict note.

Bookends written last, carry no citations. Takeaway lands the judgment (no
Verdict note in the body, per press/editorial.md).

## Sources note for the editor
- Numbered in order of first appearance (fixed a W-CITE-ORDER warn). Every source
  was opened and read; verbatim passages logged in researcher/01/evidence.md.
- Kirilenko is cited from the CFTC-hosted working-paper PDF (readable) rather than
  the Wiley DOI (bot wall); it is the same paper, Journal of Finance 2017.
- Sarao is sourced to the CFTC press release (readable); justice.gov sits behind
  a bot challenge and was not used.
- All eight URLs return a live response (none 404/410). Several government PDFs
  refuse a scripted curl with 403; the proof's link checker treats that as
  "restricted, not dead" and does not block (engine/nb/links.py).

## Deliberate calls / open items
- Did not assert the popular "998.5 points / ~$1 trillion" figure: it is not in
  any primary report I opened, which give the drop as percentages. Used the
  report's own percentages instead. If the editor wants the point/dollar anchor,
  it needs a secondary source added and verified.
- No chart (none earns a committed chart-N.py). Two furniture pieces only: a stat
  strip (crash size/timing) and a holds-up grid (demonstrated vs analogy).
- Two em-dashes budget unused (zero em-dashes in the piece). No banned terms.
