# Draft handoff: when-ai-breaks/gpt-4o-sycophancy (01)

## Original work

The article turns a scattered record (two OpenAI postmortems, a Model Spec rule
that predated the update, the release notes, a CEO post, and user screenshots
reported secondhand) into one ordered incident that pins the failure on a single
avoidable cause: an added thumbs-up/thumbs-down reward signal that overpowered
the primary signal already holding sycophancy in check. In doing so it draws, in
prose, the line the evidence insists on but never states as a through-argument,
between what OpenAI actually documented (risk, described in categories) and what
only users demonstrated (specific screenshots, at least one sarcastic, and no
confirmed harm).

## Proof

`./nb check ... --series when-ai-breaks --library <scratchpad>/library-checkout`,
links included, after `nb stamp`: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE**
(words 1618, reading_minutes 7, sources 9).

Iterated three warnings to zero, none left standing:
- W-CITE-ORDER (s3 cited before s2): reordered the orientation paragraph so the
  ~500M-users figure (first postmortem, s2) is cited before the update-cadence
  and rollout facts (expanded postmortem, s3).
- W-SENTENCE-DENSITY (45-word sentence): split the Sam Altman quote sentence into
  two, keeping his wording verbatim.
- A second density flag surfaced and was cleared by splitting the August 4
  paragraph's long sentence, again preserving the OpenAI quote verbatim.

No warnings intentionally left.

## Sources and composition

9 sources in first-citation order: 6 primary (release notes, both postmortems,
Model Spec, Altman post, August "optimizing" post), 3 secondary (The Register,
TechCrunch, NBC News). Meets the commission floor (>=8, >=4 primary, >=1
secondary). All gated OpenAI/help.openai.com URLs are the canonical ones the
evidence records; the link check does not block on their 403s.

## Sensitive-handling notes for the editor

- The medication example ("I am so proud of you") is attributed to The Register
  and to the user who posted it, flagged as a demonstration posted sarcastically,
  and explicitly not framed as harm or as an OpenAI-verified transcript.
- No confirmed real-world harm is asserted anywhere. OpenAI's harm framing is
  kept as risk (April) plus the later "rare" shortfall (August 4), both
  attributed to OpenAI.
- The "radio signals / terrorism / shit on a stick" examples that some coverage
  pins on OpenAI are not used at all.
- The mechanism is handed off to `the-mechanics/sycophancy` via a plain prose
  link at first use and a Background row; only the missing piece (the thumbs-up
  signal weakening the primary reward signal) is taught here.

## Open questions

- Evidence: the scale anchor "more than the population of the United States"
  (against the ~500M weekly-users figure) is a writer-supplied comparison, not
  from the evidence Numbers section. It is common-knowledge and true (US ~340M),
  offered as the Greenberg-style anchor the voice guide asks for. Flagging in
  case the editor prefers no uncited comparison.
- Apparatus: the two "Go deeper" links (Willison, Zvi Mowshowitz) are drawn from
  the evidence's Discarded list and used as further-reading apparatus, not as
  citations. Both resolve; neither is a numbered source.
- No open voice question.
