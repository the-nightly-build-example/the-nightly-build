# writer brief: when-ai-breaks/bard-jwst-demo (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — house standard, paper
  voice, series prompt, lesson template identity
- commission.md (../../commission.md) — the incident, angle, boundaries, continuity
- voice-guide.md (../../writing-coach/01/voice-guide.md) — how this piece sounds
- evidence.md (../../researcher/01/evidence.md) — the verified claim set; your only
  source of facts
- the initialized article: ../../../../library/when-ai-breaks/bard-jwst-demo.html
  (edit in place; keep skeleton, engine assets, required labels)
- the effective template contract and furniture under ../../../../.nb-context/

Output: draft-handoff.md (this directory)

Proof: /home/user/the-nightly-build/nb check
  /home/user/the-nightly-build/.nb-work/when-ai-breaks/bard-jwst-demo/library/when-ai-breaks/bard-jwst-demo.html
  --series when-ai-breaks --library /home/user/library-checkout
  (iterate with --no-check-links; run nb stamp then the full check, links included,
  until BLOCK: 0)

Honor these decisions from the evidence and commission:

- The erroneous claim, verbatim as the evidence records it: "JWST took the very
  first pictures of a planet outside of our own solar system." It appeared in
  Google's own promotional GIF, posted to Twitter and embedded in the 6 February
  2023 announcement post. Quote it exactly.
- The correction, precisely: the first-ever direct image of an exoplanet was
  2M1207b (ESO's VLT/NACO, detected 2004, confirmed 2005); JWST's own first direct
  image was HIP 65426 b in 2022, and NASA states that was "not the first direct
  image of an exoplanet." Get both facts from the primary astronomy sources the
  evidence cites.
- Keep the market claim honest. Alphabet fell about 8% ($8.59 to a $99.05 close)
  on 8 February 2023, roughly $100 billion, up to ~9% intraday — report it as
  reported (secondary), and do NOT imply the demo alone caused it: the underwhelming
  Paris event (which proceeded that day) and Microsoft's ChatGPT-in-Bing launch the
  day before are in the same reporting. State the co-causes plainly.
- Sourcing note: some primary originals (the Pichai tweet; Reuters/The Verge/CNN
  at their own domains) were not readable firsthand; the verbatim error and Google's
  statement come from an independent outlet and a verbatim Reuters reprint. Cite the
  address where each source lives, as the evidence records it — do not cite a fetch
  endpoint.
- The mechanism: fluent, plausible generation with no built-in truth check —
  ordinary LLM behavior surfaced in a high-stakes ad, not a rare glitch. Hallucination
  and false confidence are taught (the-mechanics/hallucination,
  the-mechanics/false-confidence): link them in Background and teach only the
  minimum here. Close on where the same failure lives now in shipped products (e.g.
  AI search summaries stating wrong facts), from the evidence.
- Discuss Google/Alphabet as the operator, reported as fact; name no company as an
  authority.

Recent shapes to break (see commission): galactica is this desk's closest recent
piece and also a fabrication-in-a-demo story — do NOT echo its dek (", and Meta's
own paper had already measured...") or its trailing-clause headline ("..., and its
public demo lasted about two days"). Avoid the comma-triad dek. Vary the closing
present-day heading away from "Where X still Y."

This round's focus: tell the incident in dated order with names, land the exact
correction, keep the market causation honest, and make the fluent-confidence
mechanism concrete enough that the reader spots it in the AI answers they meet daily.
