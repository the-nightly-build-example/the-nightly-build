# writer brief: when-ai-breaks/michigan-midas (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/michigan-midas/agent-artifacts/when-ai-breaks/michigan-midas/editorial-direction.md — house standard, press voice, series prompt, template identity
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/michigan-midas/agent-artifacts/when-ai-breaks/michigan-midas/commission.md — assignment, boundaries, required contribution, recent shapes/phrasing to break (esp. the Robodebt-echo warning)
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/michigan-midas/agent-artifacts/when-ai-breaks/michigan-midas/writing-coach/01/voice-guide.md — how this piece should sound, with exemplars
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/michigan-midas/agent-artifacts/when-ai-breaks/michigan-midas/researcher/01/evidence.md — the complete claim set
- Article to edit in place: /home/user/the-nightly-build/.nb-work/when-ai-breaks/michigan-midas/library/when-ai-breaks/michigan-midas.html
- Template context: /home/user/the-nightly-build/.nb-work/when-ai-breaks/michigan-midas/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/when-ai-breaks/michigan-midas/agent-artifacts/when-ai-breaks/michigan-midas/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/when-ai-breaks/michigan-midas/library/when-ai-breaks/michigan-midas.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/97d053c3-1b59-5f4b-8b78-5c56b444e4a1/scratchpad/library-checkout

This round's focus — the evidence record CORRECTS the commission on several
points. Follow the evidence, not the commission, and every figure must carry its
denominator, period, and owner or it will be wrong:
- There is NO single "the error rate," and the famous "93%" is not the state
  Auditor General's finding. 93% is the UIA's December 2016 review (20,965 of
  22,427 auto-adjudicated cases overturned). The UIA's fuller August 2017 review
  reports a DIFFERENT figure on a DIFFERENT denominator: 85% of 40,195 purely
  computer-decided findings reversed (plus 44% of 22,589 computer-flagged-then-
  investigated), across 49,910 people, $20.8M refunded. Do not write "the 2017
  review found 93%"; that conflates the two reviews and would be a headline-type
  error. Pick the figure whose denominator matches the sentence, and name the
  review and period.
- The undisputed teaching core (safe across all primaries): from October 2013 to
  August 2015 MiDAS decided fraud with no human examiner, on automated data
  mismatches and an income-averaging step, notifying claimants mainly through
  often-dormant online accounts, at a fourfold penalty, then collected via
  garnishment and tax-refund seizure.
- Vendors: "Fast Enterprises built MiDAS" is only half right. FAST built the
  platform; SAS built the fraud-detection engine (EFDS); CSG ran oversight. The
  vendor-versus-agency question has three parties. Be precise about who built
  what.
- Steelman the state's strongest counter: the 2023 Sixth Circuit gave agency
  supervisors qualified immunity after discovery, recharacterized the surviving
  claims as collection of benefits actually paid, and found the notice-and-appeal
  process more robust than alleged. Set that honestly against the Michigan
  Supreme Court's 2022 ruling (and the $20M settlement) that let claimants sue
  the state for damages. Present the strongest version of each side and say what
  evidence would settle it, per the beat.
- Robodebt is already published and shares the pattern but NOT the mechanism.
  MiDAS's data-mismatch fraud flags, multi-party build, dormant-account notice,
  and qualified-immunity ending are its own. Do not echo Robodebt's opener or its
  "the same bargain still runs" closer; link Robodebt (and the Dutch childcare
  scandal) in Background as the same design elsewhere.

Everything else per your skill. Fill nb-meta: date 2026-08-23, harness
`claude-code-routine`, model `claude-opus-4-8`, tags per the commission
(government, automation, unemployment, false-positives). Write the one-sentence
original-work statement in draft-handoff.md. Iterate with --no-check-links, then
run full `nb stamp` + `nb check` until `BLOCK: 0`, and do the display-text
self-test before handing off — the affected-count and error-rate figures in the
headline, dek, and subheads must each carry the right denominator and owner.
