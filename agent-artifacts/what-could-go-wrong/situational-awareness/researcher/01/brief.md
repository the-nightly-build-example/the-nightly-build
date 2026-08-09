# researcher brief: what-could-go-wrong/situational-awareness (01)

Inputs:
- `../../commission.md` — the assignment, the desk's full-strength-then-test
  shape, and the boundaries (sandbagging and deceptive alignment are their own
  lessons; the un-demonstrated exploitation must not be presented as shown).
- `../../editorial-direction.md` — citation standard, series territory, declared reader.

Output: `evidence.md` (this directory)

Focus and known risk surface (decisions the inputs do not settle):

- The argument's origin: find the primary write-up where situational awareness is
  set out as a dangerous-model ingredient (Ajeya Cotra's "Without specific
  countermeasures, the easiest path to transformative AI likely leads to AI
  takeover," or the specific section on situational awareness / "playing the
  training game"). Record what worried the author and the reasoning as its careful
  defender would put it. This is a primary for the *argument*.
- The measurement primaries: Berglund et al. 2023 ("Taken out of context: On
  measuring situational awareness in large language models," arXiv 2309.00667) —
  record exactly what was demonstrated (out-of-context reasoning: using a fact
  taught in training to change test-time behavior) and how bounded it is. Laine et
  al. 2024 ("Me, Myself, and AI: The Situational Awareness Dataset (SAD) for
  LLMs") — record the benchmark's structure, the frontier-model scores, the
  human/chance reference points, and the authors' own caveats. Give figures their
  denominators.
- The present-day position: find a frontier-safety framework or eval-lab document
  (e.g. an eval report or safety policy) that names situational / evaluation
  awareness as a capability that can invalidate evals and says what should be done
  about it. Record what it claims and what it does not; treat the lab as a party
  with a stake, not an authority.
- The sharp line the lesson turns on: search specifically for whether any
  documented case shows a model *using* situational awareness, unprompted, to game
  a real safety evaluation in deployment. Record the strongest thing found and,
  just as carefully, that the stronger versions are handed the goal or the setup
  (tie to the sandbagging and deceptive-alignment findings without re-arguing
  them). Contradictory evidence — that the awareness is shallower than claimed, or
  sharper — is the most valuable line here; find both directions.
- Recent (2024-2025) "evaluation awareness" findings where models verbalize they
  may be under test: record the source that owns each, and how strong it is.

Run-environment caveat: record each source's own resolving page (arXiv,
publisher, lab report page), never a fetch-proxy URL. Where a claim is an
accusation about a named lab's model, it needs two independent confirmations.
