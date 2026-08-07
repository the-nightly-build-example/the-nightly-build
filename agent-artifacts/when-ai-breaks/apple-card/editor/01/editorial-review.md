# Editorial review: when-ai-breaks/apple-card (editor/01)

## Skeptic

Thesis, stated from the draft alone: New York's DFS cleared Goldman Sachs of a
fair-lending violation in Apple Card underwriting, but "no violation found" is
not "proven fair" — a model blind to gender can still act on it through
correlated inputs (proxies), the one test DFS ran (comparing men and women with
similar credit characteristics) cannot by construction detect a bias that lives
inside those characteristics, and neither an applicant nor the public can obtain
the evidence (model features, regression specification, mediation analysis) that
would settle it. The load-bearing claims: (1) the documented 20x split on shared
finances; (2) DFS found no violation and the model did not use gender; (3) the
proxy mechanism; (4) the impossibility of proof; (5) the live-today framing via
CFPB Circular 2022-03.

I tried to break each and they held.

- **20x and dates.** Firsthand in the DFS report (s1, p.4), which the article
  cites rather than the gated tweet. The wife's firsthand claims (higher score,
  no explanation, "just the algorithm," limit raised after the tweets) are
  sourced to her own account on dhh.dk (s2), correctly labeled primary. No gated
  post is presented as a directly quoted primary; DHH's "black box" appears as
  paraphrase cited to DFS (whose own word it also is), never in quotes as his
  verbatim tweet. Wozniak's 10x is carried as his claim via Futurism (s3,
  secondary), never as a DFS finding. Goldman's denial is via AppleInsider (s4,
  secondary). All footings match the brief's caveats.
- **No violation / model didn't use gender.** Well supported by the report (s1)
  and the press release (s5). The nuance is held exactly: the piece never
  presents bias as proven and never reads as exonerating the opacity — it faults
  "the silence around" the model in the same calm register.
- **Proxy / impossibility argument (brief's judgment call #1).** Adequately
  hedged, and I do not require a second source to publish. The article never
  asserts bias occurred; it asserts unprovability. Its one empirical
  load-bearing fact — that DFS published no table, specification, or proxy
  analysis of the ~400,000-applicant study — is verifiable from the report's own
  absence and from DFS's own "does not prove otherwise" line (s1), not from
  O'Sullivan alone. The logical core (holding the characteristics equal holds an
  embedded proxy equal, so its effect disappears) is a reasoning step shown in
  the open, not a contested empirical claim that needs corroboration. O'Sullivan
  (s7) carries only the attributed expert opinion that such features are known
  to proxy for protected classes, and she is named as its holder. A second
  independent expert would strengthen the section but is not publication-
  blocking; if the orchestrator wants it, that is a researcher task (new
  evidence artifact), not a writer rewrite. Recorded, not required.
- **Attribution nuance (non-blocking).** The brief named "O'Sullivan / Patrick
  Hall of bnh.ai"; the article names only O'Sullivan, the piece's author. The
  "1970s-era test" characterization originates with Hall inside her article. This
  is acceptable — she makes the objection in her own voice and s7 links her
  piece correctly — but naming Hall for that phrase would be more precise. Not
  required.

Display text, descriptor by descriptor: the headline ("New York cleared the
Apple Card of bias without proving it fair") is a claim the piece defends,
subject-verb-surprise, no colon tell. Every subhead is a real step of the
argument in the piece's own nouns. The one display-text imprecision was in the
dek: "drew twenty times her Apple Card limit" misdescribes the fact — a limit is
offered/granted, and "drew" reads as borrowing. DFS's wording is "offered," and
the body already uses "offered." Fixed directly in both the dekline and the
nb-meta block. Every `data-nb-kind` is correct (s2 dhh.dk is properly primary as
the affected party's own account; the secondaries are correctly outside the
authoring party). Citation hrefs land on the sources themselves, and the figure's
`data-nb-url` resolves to the DFS PDF page carrying the panel.

## Cut

The piece is disciplined; there was little to remove. Two findings:

- **Redundant restatement (cut made).** The proxies section opens by
  establishing that "'The model does not use gender' answers the first charge. It
  does not touch the second." Its closing paragraph then ended on a near-verbatim
  restatement — "Clearing the first charge, disparate treatment, does not answer
  the second" — appended after the paragraph's real landing (the COMPAS
  fairness-definitions point). This both repeated the section's own opening and
  softened a paragraph that ends stronger on "both be right," which also hands
  off cleanly to the proof-problem section. Cut.
- **The two density warnings (brief's judgment call #2).** Both are controlled
  single-idea sentences using the colon for its proper job, and I concur with
  keeping them. The "three things: the list of features, the specification, and a
  mediation analysis" sentence is one introduced enumeration; splitting it would
  break the list that the next paragraph spends. The takeaway's "the reason the
  story does not end there is the proxy: ..." pairs the definition with its
  immediate consequence via the colon's payoff use. Neither is a run-on (no
  clause piled past the point of losing the thread); both are the licensed
  "long sentence in control."

Worst tell: none rising to a cut beyond the two above. The unreconciled pair in
"Cleared on bias, faulted on secrecy" restates the finding's two parts that the
prior paragraph also states, but that repetition is the licensed centerpiece move
(both poles documented and load-bearing, no "not X but Y" mold, no verdict
declared) and it clears the bar, so I protected it. The one "not X but Y" contrast
("not mainly about one card") is earned and within the one-or-two ceiling.

Furniture: the timeline carries the ordered trigger events, the "In plain
language" note carries the proxy definition (correct label per the note catalog),
and the figure is load-bearing evidence, not decoration. No component reads as
filler. Openers and closer clear the recent-pattern notes: the piece opens from
the affected user rather than the operator, and the closing heading ("Where the
black box sits today") varies the series-mandate phrasing rather than copying
"where the same weakness runs now."

## Reader

Read straight through as the paper's declared reader (smart, no time in a
codebase), what I have that the sources alone would not give me: the assembled
impossibility argument. The DFS report, the ECOA text, and O'Sullivan each hold a
piece; only the article puts them together into the specific, uncomfortable
conclusion that the one person with legal standing to complain is the one person
structurally barred from all three artifacts that could settle the question. That
matches the draft-handoff's original-work sentence, and both survive the read.
The prose sits closer to the voice-guide exemplars than to a median summary: it
delivers the anticlimax as the payoff, holds the accusation and the "no violation
found" at equal weight in adjacent unreconciled sentences, and stops at the proof
question to name the exact missing evidence and why it cannot be had — Ritchie's
disciplining of a viral number without scoring points on either side. The
headline, reread as the largest claim, is one the piece earns.

## Edits

- Dek (both the visible dekline and the nb-meta `dek`): "drew twenty times her
  Apple Card limit" → "was offered twenty times her Apple Card limit" (precision;
  aligns the verb with DFS's wording and the body).
- Proxies section: cut the closing sentence "Clearing the first charge,
  disparate treatment, does not answer the second." (redundant restatement of the
  section's own opening; strengthens the paragraph ending).
- Ran `nb stamp`: words 2087 → 2077, reading_minutes 9, sources 8.

## Required work

None blocking. Writer owns the re-proof after these direct cuts (run the brief's
`nb check ... ` to confirm BLOCK: 0 holds).

Optional, non-blocking, for the orchestrator to route only if desired:
- **researcher** — a second independent expert voice on the proxy point, to sit
  beside O'Sullivan/Hall. The argument is adequately hedged without it; this
  would be reinforcement, not a fix. Requires a new evidence artifact.

## Decision

approve — the nuance is held exactly, sourcing footings and display text are
sound, the asset earns its place, and the two remaining issues were surgical
(one dek precision fix, one redundant-sentence cut) with no blocking work left.
