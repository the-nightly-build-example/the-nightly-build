# writer brief: when-ai-breaks/ai-overviews (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-overviews/agent-artifacts/when-ai-breaks/ai-overviews/editorial-direction.md — house standard, paper voice, series prompt
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-overviews/agent-artifacts/when-ai-breaks/ai-overviews/commission.md — incident, structure, mechanism, boundaries, source floor
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-overviews/agent-artifacts/when-ai-breaks/ai-overviews/writing-coach/01/voice-guide.md — the craft standard (forward-told, deadpan-flat on the absurd facts)
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-overviews/agent-artifacts/when-ai-breaks/ai-overviews/researcher/01/evidence.md — the complete, verified claim set
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-overviews/library/when-ai-breaks/ai-overviews.html — the initialized article to edit in place
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-overviews/.nb-context/ — the effective template contract and runtime assets

Output: /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-overviews/agent-artifacts/when-ai-breaks/ai-overviews/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-overviews/library/when-ai-breaks/ai-overviews.html --series when-ai-breaks --library /home/user/library-checkout
(iterate with --no-check-links; final pass with links, until BLOCK: 0)

nb-meta to fill: date 2026-08-05, harness claude-code-routine, model claude-opus-4-8. Run nb stamp for the counts.

This round's focus — the evidence record complicates the commission's angle;
engage the counter-account rather than asserting the thesis unopposed (the house
standard requires steelmanning opposing views on a contested point):
- Google's own framing is that AI Overviews "misinterpreted language on
  webpages" and that hallucination is "an inherent feature" (Reid; Pichai). That
  pulls against a pure "faithful retrieval of a real source, no trust model"
  thesis. Put Google's account in at full strength, then weigh it.
- Use the two confirmed examples for two distinct jobs. Glue-on-pizza is the
  clean case where the system restated a real Reddit joke accurately — that is
  the "no trust model" demonstration. Eat-a-rock is a data-void case: per the
  postmortem the Onion satire surfaced via a republished copy on a software
  firm's site because it was nearly the only match. Do not describe rocks as a
  direct Onion retrieval.
- Use ONLY the confirmed-real examples (glue, rocks). Do NOT use the discarded
  faked screenshots (dogs in cars, smoking in pregnancy, depression / Golden Gate
  Bridge) — Google says they never appeared.
- Do not cite a Reddit URL for the glue joke: it could not be resolved to a live
  page. Attribute the joke's existence to the secondary reporting and Google's
  acknowledgment, as the evidence record does.
- The Verge / Pichai page is live but fetch-blocked; the evidence record records
  it at its own address with corroboration. Cite it at that address.

Distinguish this incident from the desk's air-canada-chatbot and mata-v-avianca
(both hallucination/invention). This one is retrieval surfacing a real source.
