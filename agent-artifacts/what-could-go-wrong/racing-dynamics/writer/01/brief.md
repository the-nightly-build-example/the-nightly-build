# Writer brief: what-could-go-wrong/racing-dynamics (round 01)

## Inputs (begin here; reread the voice guide before drafting)
- Commission: `../../commission.md`
- Editorial direction: `../../editorial-direction.md`
- Voice guide: `../../writing-coach/01/voice-guide.md`
- Evidence record: `../../researcher/01/evidence.md`  ← complete claim set (14 sources)
- Initialized article (edit in place):
  `/home/user/the-nightly-build/.nb-work/what-could-go-wrong/racing-dynamics/library/what-could-go-wrong/racing-dynamics.html`
- Template context: `.../racing-dynamics/.nb-context/` (read `furniture/engine.md`)

## Output
- Fill the article HTML.
- Write `writer/01/draft-handoff.md`.

## What to write
A What Could Go Wrong `lesson`: the argument at full strength first, then tested
against the record, then brought to the present, keeping the desk's neutrality
(no doom, no dismissal; leave the reader to decide). Teach three ideas:

1. **The model, at full strength (Armstrong, Bostrom & Shulman, 2016).** Walk
   the setup in plain words: several teams race to build the first powerful AI;
   each picks how much to invest in safety; cutting safety makes you faster;
   whoever is furthest ahead wins; the winner's system works with a probability
   equal to its safety and otherwise causes a disaster. Teach "Nash equilibrium"
   plainly (no one can do better by changing their own choice alone). The stark
   result: when being first matters far more than being safe, the equilibrium is
   to spend nothing on safety. Use the paper's own logic; a small worked case
   (e.g. as capability's importance goes to zero, equilibrium safety goes to
   zero) grounds it. The reader should believe a serious person holds this.
2. **The counterintuitive information result ("the curse of too much
   information").** The paper's signature finding: no team knowing anyone's
   capability is safest; everyone knowing everyone's is most dangerous. State
   the mechanism precisely from the evidence (under private information a team
   only cuts corners when it knows its own capability is low; under public
   information the leader cuts corners whenever the runner-up is close, which
   happens far more often). Mark honestly: the researcher found **no** technical
   rebuttal of this result on its own terms — present it as the model's claim and
   say that its robustness to relaxed assumptions is untested, not settled.
3. **Audit the assumptions against the record, then the present.** Take the
   three load-bearing assumptions and mark each holds / unproven / contradicted:
   - *A decisive, durable first-mover advantage.* This is the weak one. Every
     measured capability gap since 2023 has closed in months, not never (Epoch:
     US–China gap averages 7 months, range 4–14; open-vs-closed ~3–4 months;
     o1→DeepSeek-R1 about 4 months). Nothing shows a lead becoming a durable
     exclusive advantage. Say so plainly.
   - *Safety trades against speed under real competitive pressure.* Partly
     supported: OpenAI's own Preparedness Framework v2 names the "race to the
     bottom" scenario and pre-commits conditions (a primary admission of the
     incentive, not proof the field cuts safety). METR's on-record account of a
     three-week evaluation window for o3/o4-mini is independent, first-hand
     corroboration that evaluation time can be compressed around a release.
   - *Present-day: who presses this and what they want.* Proponents want
     coordination and if-then commitments (the 2024 Seoul Frontier AI Safety
     Commitments; Karnofsky's if-then proposal; the 2023 FLI pause letter's ask
     for a six-month pause). Dismissers reject the framing: Arbel & Tokson argue
     leads do not last (knowledge leaks, fast-follow), Scharre argues the
     "arms race" label is unwarranted while granting schedule pressure can
     degrade safety. Note where confidence outruns proof on both sides.

If space is tight, keep ideas 1–2 whole and compress idea 3's present-day survey
to the sharpest points.

## Decisions fixed for you (hold to the evidence)
- **Keep report, model-claim, and synthesis distinct.** The equilibria are
  if-then claims *within the model*; the Epoch gaps are reported facts; your
  weighing is synthesis. Do not let the model's conclusion read as a fact about
  the world.
- **The compressed-testing "days" claim is secondary and single-origin** (a
  Financial Times investigation the researcher could not open directly; ft.com
  blocked). If you use it, label it as reporting attributed to the FT and lean
  on METR's first-hand three weeks as the verified datapoint. Do not present
  "days" as established.
- **Name no company as an authority.** OpenAI's framework, the Seoul
  commitments, and the FLI letter are evidence of what those parties *said they
  would do* or *asked for*, not proof any claim is true or any signatory
  complied. Frame them that way.
- Karnofsky's affiliation at publication: visiting scholar, Carnegie Endowment
  for International Peace (he later joined a frontier developer's staff — do not
  present him as speaking for a company in this 2024 piece).

## Source handling
- Cite what the argument rests on, in first-citation order; you need not cite all
  14. Meet policy (min 8; primary ≥4; secondary ≥1). Kinds from the evidence:
  the paper (1), Bostrom (2), OpenAI Preparedness (3), GPT-4 system card (4),
  METR (5), Seoul commitments (6), FLI letter (7), Karnofsky (8), Epoch ×3
  (9–11), Arbel & Tokson (12) = **primary**; Scharre (13) is primary for his
  argument but **secondary** re any developer's conduct; the FT retelling (14) is
  **secondary**. Set `data-nb-kind` honestly; add `data-nb-locator` where the
  evidence supplies it.

## Constraints — banned terms are a hard gate here
- **"AI race" and "artificial intelligence race" are banned (max 0)** and the
  proof enforces it. Do NOT reproduce the FLI letter's wording that uses the
  phrase. Write "competitive pressure", "a development race", "racing to
  deploy", "a race to the bottom on safety" (this exact phrase is fine and is
  OpenAI's own), "the race to build the first powerful AI" (the word "race" is
  allowed; the banned strings are only "AI race"/"artificial intelligence
  race"). Also banned: **load-bearing 0, machinery 0**, leverage ≤1, em-dash ≤4,
  revolutionary/transformative/game-changing 0.
- Word band 1200–2200.
- nb-meta actual values: series what-could-go-wrong, slug racing-dynamics,
  template lesson, mode open, order null, date 2026-08-02,
  harness "claude-code-routine", model "claude-sonnet-5",
  tags ["coordination","competitive-pressure","ai-safety","governance"].

## Furniture
- Optional. The model's three information scenarios could be a small `nb-table`
  (scenario → who knows what → equilibrium safety in plain terms) if it aids the
  reader; keep it plain, cite it. The paper's Figure 1 (disaster probability vs
  capability-importance, 2 vs 5 teams, three info curves) is a strong source
  asset but its exact curve shapes are the evidence — prefer prose or a faithful
  small table over a freehand redraw; only capture the real figure with
  `nb asset` if clean. No external images. No article-authored scripts/styles.

## Bookends (write last)
- Background: link `what-could-go-wrong/intelligence-explosion` (the
  decisive-advantage/discontinuity assumption) and
  `the-levers/responsible-scaling-policies` (a live proposal proponents point
  to). Go deeper: beyond this paper (e.g. the open ORA copy of the paper).
  Relative links e.g. `../what-could-go-wrong/intelligence-explosion.html`,
  `../the-levers/responsible-scaling-policies.html`.

## Headline / dek / headings
- Headline: state the argument or the audit's sharpest finding with actors
  named; no colon-subtitle, no comma-triad, no unanswered question. Candidate
  territory: the model says competition drives safety to zero — and the one
  assumption it needs (a lasting lead) is the one the record has not shown.
- Do not echo the jailbreaks heading mold ("teaches a pattern, not a boundary")
  or comma-triad headings. Check recent deks; no banned dek molds.

## Original work
In `draft-handoff.md`, name the one visible act of original work: the
assumption-by-assumption audit marking each of the model's premises holds /
unproven / contradicted against the 2023–2026 record. It must be visible in the
article.

## Prove and hand off
Run to `BLOCK: 0`:
```
export PATH="$HOME/.local/bin:$PATH"
/home/user/the-nightly-build/nb check --series what-could-go-wrong \
  --repo /home/user/the-nightly-build --library /home/user/library-checkout \
  /home/user/the-nightly-build/.nb-work/what-could-go-wrong/racing-dynamics/library/what-could-go-wrong/racing-dynamics.html
```
Treat warnings as revision notes (watch the banned-term counts especially).
Write `draft-handoff.md`. Return `DONE writer <draft-handoff-path>` after
BLOCK: 0, or a REQUEST line if evidence/voice is missing.
