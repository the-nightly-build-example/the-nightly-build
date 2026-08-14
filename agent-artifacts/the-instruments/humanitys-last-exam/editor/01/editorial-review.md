# Editorial review: the-instruments/humanitys-last-exam (editor/01)

## Skeptic

Thesis: an HLE score is manufactured to start near zero and climb fast, because
the set admits only questions the strongest current models already fail; that
construction, plus the gap between tool-assisted and no-tool runs, explains the
documented misreading of a 26% browsing run as "the frontier of human knowledge."

The claims it stands on, and how each held:

- **The adversarial filter (headline claim).** "Only admits questions today's
  models fail." Checked against the paper full text (s2): a multiple-choice
  question is kept only if frontier models average worse than random, an
  exact-match one only if the models cannot solve it; ~70,000 attempts yielded
  ~13,000 that stumped the models. Held. The headline is a claim the piece
  defends, not a scope label.
- **Near-zero by design, climbs fast.** Launch top 13.4% (o3-mini high), single
  digits below; current no-tool top gemini-3.1-pro-preview 46.44% as read
  2026-08-14. Both verified against Table 1 (s2) and the live Scale/CAIS board
  (s3, opened: methodology and top score confirmed). Held.
- **Tool/no-tool conflation is the misreading mechanism.** GPT-5 24.8% no-tool
  (with reasoning) vs 42.0% with tools; deep research 26.6% with browsing+Python
  vs the ~9% no-tool scores Fortune called a "nearly threefold jump" over.
  Verified against Vellum (s6) and Fortune (s7), both opened. Held.
- **The limit is the authors' own.** The paper's own caveat that a high score
  "would not alone suggest autonomous research capabilities or 'artificial
  general intelligence'" is quoted verbatim and confirmed in s2. Held. This is
  the counter-evidence that could have softened the angle; it instead supports
  it, exactly as the evidence record predicted.
- **Answer-key errors, given as a range.** FutureHouse 29±3.7% of audited
  text-only chem/bio answers conflict with the literature; the HLE team's own
  re-check ~18%. Verified against the FutureHouse page (s8), which carries both
  figures. Presented as 18–29% and bounded to the bio/chem slice. Held.

Sourcing audit (the round's sharpest risk). Every `data-nb-kind` was tested
against the primary/secondary rule and every `href` opened as printed:

- No figure is attributed as primary-to-OpenAI. The two OpenAI-owned figures ride
  their opened repeaters: GPT-5 24.8%/42.0% → Vellum (s6, correctly labeled
  **secondary**); deep research 26.6% → Fortune (s7). openai.com was 403 to the
  researcher, and citing an unopened page would violate "cite only what you read."
  The writer's call is correct.
- Fortune (s7) is labeled **primary**. This is defensible and matches the
  evidence record: the article is cited as the misreading artifact, and it owns
  its own framing and headline. Its use in the piece is as that artifact (the
  "frontier of human knowledge" headline and the "nearly threefold jump"), not as
  an independent owner of the 26.6% figure. The label hides no missing
  independent source, because the number is used to describe what Fortune did,
  not asserted as a standalone fact needing corroboration.
- s1–s5 (paper abstract, full text v11, official site, v1) and s8 (FutureHouse)
  are all first-party documents to the claims they carry: correctly primary.
- Source policy met: 8 sources, 7 primary + 1 secondary (commission floor: 8, ≥4
  primary, ≥1 secondary).
- Every href lands on the source itself. Fortune, the Scale/CAIS board,
  agi.safe.ai, Vellum, FutureHouse, arXiv v11, arXiv v1 all opened and confirmed.
  Bookend links (MMLU arXiv 2009.03300, lastexam.ai, Nature DOI, The Decoder) all
  resolve; the Nature DOI 302-redirects to the article's own page, which is
  correct DOI behavior.

Display text verified descriptor by descriptor. Headline, dek, five subheads,
the launch table (five rows, accuracy and calibration columns all matching s2),
both note quotes (verbatim), the FutureHouse figures, and the composition splits
(given as ranges, attributed to both owning primaries) are accurate to their
owners. No wrong label reaches the reader.

Decision on the writer's open question: the honest attribution **stands**. No
researcher pass is required, and inventing an OpenAI primary would be wrong.

No break found; no fix routed.

## Cut

Ran the slop pass sentence by sentence, then walked the edges alone, then the
delete test. The prose is clean and specific; no sentence failed the placeholder
test outright. Findings:

- Punctuation: one em-dash, inside the verbatim Fortune quote (not authored) — no
  change. Two prose semicolons. One (leaderboard sentence) joined two sequential
  thoughts and took the house default period; the other joins a genuine parallel
  clause pair (multiple-choice kept if… / short-answer kept if…) and is a
  justified use — left as is.
- Negative parallelism: three "not X" constructions, each correcting a
  misconception the piece names (a low score read as general knowledge; "frontier
  of human knowledge"; the limit as a critic's rather than the authors'). All
  earned; none is an invented strawman. Kept.
- Punchy pairs ("The questions did not change. The model's access did."; "Being
  wrong is one thing. Being wrong while sure is what the second column records.")
  survive the test because they turn on the specific nouns and carry the
  reasoning step. Kept.
- Edge sentences: the orientation closer ("How it is produced explains both
  halves…") leans toward a structural signpost but carries the piece's unifying
  claim (one mechanism produces both the floor and the climb), so it stays as a
  thesis line rather than scaffolding.
- No banned lexical tells (checked delve/underscore/highlight/testament/pivotal/
  robust/serves-as/vague-attribution families): none present.
- Recent-pattern check: the piece does not drift into the desk's "move the score
  from X% to Y% with a trivial change" formula; it tells HLE's own story (low by
  construction, fast rise, tool/no-tool conflation). Subheads vary in
  construction and read as argument steps. The dek is built in HLE's nouns and is
  a causal claim, not a demonstration stated as flat fact.
- Furniture: bookends, stat strip, launch table, two notes, and the chart are all
  documented components, each earning its place; no stack-of-blocks effect. No
  leakage from the brief or commission found.

## Reader

Read straight through as the paper's declared reader. What I have that the
sources alone would not give me: the ability to decode any HLE percentage with
two questions — were the tools on, and how much of the answer key is even right —
and a single dated chart that makes the tool/no-tool conflation visible as the
exact error Fortune made. That matches the draft-handoff's original-work
sentence (assembling the record's scattered no-tool and tool-assisted figures
into one picture and bounding the number against the authors' own scope and the
18–29% error range), and both answers survive. The prose sits close to the
voice-guide exemplars: plain declaratives, figures where they matter, the
misreading corrected without scoring points, in the Ritchie/Luu register the
guide sets. The headline, read as the largest claim, is one the piece defends.

## Edits

- Leaderboard sentence: replaced the semicolon with a period ("…answered 46.44%
  of the questions correctly. The board is live and rises over time."), the house
  default for two sequential thoughts.

## Required work

None.

## Decision

Approve. Sourcing holds under the primary/secondary test with no figure
mislabeled primary-to-OpenAI, every href lands on its source, display text and
the chart are honest, and the prose meets the slop and voice standards.
