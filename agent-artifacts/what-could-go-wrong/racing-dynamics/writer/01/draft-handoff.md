# Draft handoff: what-could-go-wrong/racing-dynamics (round 01)

## Original work

The one visible act of original work is the assumption-by-assumption audit
in the "first-mover-gap," "testing-time," and "if-then-commitments" sections:
each of the model's three load premises (a decisive, durable first-mover
advantage; safety trading directly against speed under real competitive
pressure; and the present-day stakes proponents and dismissers argue over)
is marked against the 2023–2026 record and named as weak, partial, or
contested, rather than left as an unweighed list. This is not something the
1985/2016 paper or any single cited source does on its own; it is the
piece's synthesis, held visibly apart from the model's if-then logic and
from the reported facts throughout.

## Files changed

- Article: `/home/user/the-nightly-build/.nb-work/what-could-go-wrong/racing-dynamics/library/what-could-go-wrong/racing-dynamics.html`
- No source assets or charts were used (per brief's "no external images" and
  "prefer prose or a faithful small table over a freehand redraw" guidance on
  the paper's Figure 1). A small `nb-table` renders the three information
  regimes instead, per the brief's optional-furniture suggestion. One bare
  `nb-math` equation (the no-information equilibrium, s = µ/(en), reduced to
  µ/2 for the two-team/enmity-1 worked case) grounds the "capability's
  importance → 0 ⇒ safety → 0" result the brief asked for.

## Proof result

Ran the exact command from the brief:

```
export PATH="$HOME/.local/bin:$PATH"
/home/user/the-nightly-build/nb check --series what-could-go-wrong \
  --repo /home/user/the-nightly-build --library /home/user/library-checkout \
  /home/user/the-nightly-build/.nb-work/what-could-go-wrong/racing-dynamics/library/what-could-go-wrong/racing-dynamics.html
```

Final result: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`. No warnings were
left unaddressed; the first pass came back with a high word count (2719) and
several dense, multi-clause sentences (up to 82 words), all fixed by
splitting sentences and trimming redundant clauses across every section
without cutting any required fact, quote, or citation. Final measured word
count is 2190 (in the 1200–2200 band), confirmed against nb-meta.

Also confirmed by direct search: 0 uses of "AI race" / "artificial
intelligence race" outside the Sources section (two source titles that
contain "AI Race" verbatim are in the exempt Sources list, per
`spec/editorial.md`'s counting rule); 0 uses of "transformative,"
"load-bearing," "machinery," "revolutionary," or "game-changing"; 0
em-dashes.

## Source policy

12 sources, first-citation order, all traceable to the evidence record:
the 2016 paper (primary, cited 6 times across the model-teaching sections),
two Epoch AI data insights (primary), Arbel & Tokson (primary), OpenAI's
Preparedness Framework (primary), METR (primary), the GPT-4 system card
(primary), Semafor's FT-derived reporting (secondary, labeled as such in
prose), the Seoul commitments (primary), Karnofsky (primary), the FLI letter
(primary), and Scharre (primary for his own argument). That is 11 primary +
1 secondary, meeting the policy floor (min 8, primary ≥ 4, secondary ≥ 1)
with margin. Bostrom's *Superintelligence* was deliberately not cited as a
numbered source (per the evidence record's own note that it restates, not
extends, source #1's model) but appears in the "Go deeper" band, which
carries no citation requirement.

## Decisions honored from the brief

- Kept report / model-claim / synthesis on separate footing throughout: the
  model's results are stated as "the paper states," equilibria are given as
  conditional (if µ is small, then...), Epoch's numbers are reported facts,
  and the audit language ("this is the assumption the record contradicts
  most directly," "confidence runs ahead of proof, on both sides") is
  flagged as the piece's own weighing.
- The FT "days" claim is explicitly labeled second-hand and single-origin,
  with METR's three weeks presented as the verified, named-source datapoint;
  the two are never conflated.
- No company is named as an authority: OpenAI's framework, the Seoul
  signatories, and the FLI letter are each framed as what that party said it
  would do or asked for, with an explicit disclaimer sentence in the same
  paragraph in two of the three cases.
- Karnofsky is identified as a visiting scholar at the Carnegie Endowment at
  the time of the 2024 piece, with no implication he spoke for a company.
- The information result (idea 2) is marked as the model's own claim with no
  on-record technical rebuttal found, its robustness outside the paper's
  exact setup stated as untested rather than settled.
- Headline and dek avoid the colon-subtitle, comma-triad, and "teaches a
  pattern, not a boundary" molds; section headings were checked against
  recent WCGW headings for shape variety (declarative single clauses, no
  repeated comma-and joins).

## Remaining questions

None outstanding. The one evidence gap the brief anticipated (no direct
technical critique of the information result's robustness) is stated
plainly in the "curse-of-information" section rather than papered over, per
the brief's explicit instruction; no further researcher input is needed to
close it, since the honest gap is itself the correct thing to teach.
