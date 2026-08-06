# researcher brief: what-could-go-wrong/sandbagging (01)

Inputs:
- ../../editorial-direction.md — citation standard, series territory, declared reader
- ../../commission.md — the exact subject, angle, and required contribution

Output: ./evidence.md

Work from original documents, never commentary (series rule). Read firsthand:
- van der Weij, Hofstätter, Jaffe, Brown, Ward, "AI Sandbagging: Language Models
  can Strategically Underperform on Evaluations" (2024, arXiv 2406.07358). Read
  the exact experiments: prompted sandbagging, fine-tuned sandbagging, hitting
  target scores, selectively hiding dangerous-capability performance while keeping
  general performance, and any calibration results. Record the real figures and
  the exact definition of "sandbagging" they use.
- Evidence on evaluation-awareness / test-detection: a primary source where a
  model recognizes an evaluation context (e.g. Anthropic's Claude 3 "needle in a
  haystack" test-awareness anecdote in an official writeup, and/or Apollo Research
  in-context scheming evaluations where models reason about being tested, and/or
  METR writeups on eval validity). Read the actual reported behavior and setup;
  record that these are constructed evaluations.
- Any frontier-lab or government (e.g. UK AISI / US AISI) primary on why
  capability elicitation and sandbagging threaten eval-based safety cases, and the
  proposed mitigations (held-out evals, fine-tuning access, elicitation). Read the
  actual claims.

Critical: find and read sources that BOUND the argument — that observed
sandbagging is induced (prompted/fine-tuned), not spontaneous; that eval-awareness
is not yet strategic concealment; and any skeptic of the sandbagging threat model.
Contradictions must not be empty.

Verify every figure (target-score hits, accuracy drops, N) against its owning
primary, with the experimental setup as scope. For any claim that a model "chose"
to underperform, record exactly whether it was prompted, fine-tuned, or
spontaneous — this distinction is the article's spine.

Source policy: at least 8 sources, at least 4 primary, at least 1 secondary.
Primary = the party that owns the claim (the paper's/eval's authors, the
institute). Name no company as an authority in the framing.

Environment: fetches go through a proxy; on 403/paywall retry with a
browser-style request first, and record each source's own canonical URL.

Sanity check: the full published what-could-go-wrong slug list is in the
commission's Boundaries. Do not build the record around a duplicate angle.
