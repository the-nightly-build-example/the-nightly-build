# writer brief: what-could-go-wrong/normal-accidents (01)

Inputs:
- `.nb-work/what-could-go-wrong/normal-accidents/agent-artifacts/what-could-go-wrong/normal-accidents/editorial-direction.md` — house standard, paper voice, series prompt
- `.nb-work/what-could-go-wrong/normal-accidents/agent-artifacts/what-could-go-wrong/normal-accidents/writing-coach/01/voice-guide.md` — how this piece should sound; read before drafting
- `.nb-work/what-could-go-wrong/normal-accidents/agent-artifacts/what-could-go-wrong/normal-accidents/researcher/01/evidence.md` — the complete claim set; use the Numbers section exactly
- `.nb-work/what-could-go-wrong/normal-accidents/agent-artifacts/what-could-go-wrong/normal-accidents/commission.md` — assignment, boundaries, habits to break
- Article to edit in place: `.nb-work/what-could-go-wrong/normal-accidents/library/what-could-go-wrong/normal-accidents.html`
- Template context: `.nb-work/what-could-go-wrong/normal-accidents/.nb-context/`

Output: `.nb-work/what-could-go-wrong/normal-accidents/agent-artifacts/what-could-go-wrong/normal-accidents/writer/01/draft-handoff.md`

Proof (run with links, until BLOCK: 0):
`./nb check .nb-work/what-could-go-wrong/normal-accidents/library/what-could-go-wrong/normal-accidents.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/fb9d317b-0db5-5e4f-9677-1de8446e916f/scratchpad/library-checkout`

This round's exactness (the evidence forces these):
- Sourcing caveat: Perrow's book could not be read firsthand. The record recovers
  his definitions and page numbers through his 2011 Bulletin of the Atomic
  Scientists article and Andrew Hopkins' 1999 verbatim quotations. Attribute
  Perrow's exact wording and page numbers as the evidence record does (through
  those reproductions); do not imply a first-hand reading of the book's pages.
- Draw the sharp line the desk requires. The demonstrated case is the 2010 Flash
  Crash (the CFTC/SEC staff report): tightly coupled automation cascading faster
  than humans could intervene. The present-day proponents (Maas 2018; Bianchi,
  Cercas Curry, Hovy 2023) concede that tight coupling among AI systems is mostly
  potential, not yet built, and disclaim near-term catastrophe. Let them draw the
  shown-versus-analogy line themselves.
- Bound the argument honestly, because two findings cut against a maximalist read:
  (1) Perrow drew his theory narrowly and classed Bhopal, Chernobyl, Challenger,
  and the Exxon Valdez as ordinary component-failure accidents outside
  normal-accident theory, so do not stretch "normal accident" to AI-failure-in-
  general. (2) The theory's terms lack an independent measure: Perrow reclassified
  air traffic control and carrier decks as linear and loosely coupled exactly
  where High Reliability Organization researchers held them up as complex, tightly
  coupled systems run safely. Name that untestability as the gap where confidence
  outruns proof.
- Steelman the HRO objection with the record's figures (air traffic control:
  75M+ handoffs a year with no midair collision under positive radar control;
  carriers: 16,000+ arrested landings without a deck accident), each with the
  hedge the record attaches, before weighing it.
- Link, do not re-teach: what-could-go-wrong/flash-crash-risk (the shown instance)
  and what-could-go-wrong/algorithmic-monoculture (a related mechanism). Do not
  drift into misalignment framings; the point is that well-behaved parts still
  produce system accidents.
- Recent habits to break: no "What <Person> saw in <place>" opener heading; no dek
  built as "the strongest evidence is a single <X>" or "borrows its <thing> from
  <source> that never mentions <Y>", and no bare "dates to <year>" tail; no
  two-sentence terse-rebuttal headline; no comma-triad dek.
- Set nb-meta `harness` to `claude-code`, `model` to the model you run as, date
  2026-09-17. Keep nb-meta `dek` identical to the rendered dekline.
