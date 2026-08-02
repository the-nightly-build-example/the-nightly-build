# Commission: what-could-go-wrong/racing-dynamics

## Assignment
A lesson on the argument that **competition to build powerful AI first will
push developers to skimp on safety.** The What Could Go Wrong desk teaches one
risk argument at a time, at full strength first, then tested against what real
systems and institutions actually do.

## Angle
Center the formal version: Armstrong, Bostrom & Shulman, **"Racing to the
precipice: a model of artificial intelligence development"** (*AI & Society*
31:201–206, 2016). A handful of teams race to build the first powerful AI; the
payoff is close to winner-take-all; safety work costs time; so each team is
pushed to cut safety to move faster, and in the model's equilibrium the field
ends up at more risk than any team would choose alone. Give its distinctive,
counterintuitive result its due: under the model, giving teams *more*
information about who is ahead can make the outcome *less* safe. Then draw the
sharp line the desk requires between what a working system has shown and what
is still analogy about systems that do not yet exist.

## Intended reader
House reader: smart, widely read, no codebase time. Teach on the spot: what a
simple game-theory "model" is and what an equilibrium means, in plain words, so
the reader can follow the argument's logic and see where its assumptions live.
Assume algebra and probability. Study how the field reasons about this; do not
join the worry or wave it off.

## Contribution this piece must make
A reader who finishes can (a) state the argument at full strength and name its
load-bearing assumptions (a decisive first-mover advantage; safety trades
against speed; few enough players to model); (b) separate what is demonstrated
(real competitive/schedule pressure among today's developers) from what is
assumed (a winner-take-all discontinuity that has not occurred); and (c) judge
where present-day confidence, doom or dismissal, outruns the evidence. The
visible original work is an assumption-by-assumption audit that marks each of
the model's premises "holds today," "unproven," or "contradicted so far," using
the record.

## Teach at most three ideas, completely
1. **The model, at full strength.** Walk the setup with the paper's own logic:
   teams, a near-winner-take-all prize, safety as a costly delay, and the
   conclusion that competition drives safety investment down. Use the paper's
   toy numbers or a faithful small worked example. The reader should believe a
   serious person could hold this before reading any objection.
2. **The counterintuitive information result.** The paper's signature finding:
   more mutual information about capabilities can worsen safety (a team that
   knows it is behind cuts more corners). State it precisely and show why it
   follows from the setup. Note what it assumes.
3. **Test it against reality, then bring it to now.** Which premises hold: is
   there a decisive first-mover advantage in AI so far, or has capability been
   incremental and fast-followed? Is safety-vs-speed a real observed tension?
   Cite the record on both. Then: who presses this argument today and what they
   want (coordination, compute/frontier governance, safety commitments — link
   the covered responsible-scaling-policies lesson), and where confidence
   outruns proof on either side. Mark analogy vs demonstration throughout.

If space is tight, keep ideas 1–2 whole and compress idea 3's present-day survey.

## Source obligations (what-could-go-wrong lesson)
- Minimum 8 sources; primary ≥ 4, secondary ≥ 1.
- Work from the originals: the 2016 paper (and Bostrom's *Superintelligence*
  treatment of race dynamics if used), read first-hand — never the commentary
  about them. A proponent's proposal document (e.g. a responsible-scaling / lab-
  safety commitment, or a coordination proposal) is a primary of what today's
  proponents want. An empirical primary on competitive/schedule pressure among
  developers (a developer's own on-record statement, or a safety-index report).
- **Name no company as an authority.** Report institutions and incentives; do
  not cite a lab as proof.

## Starting sources (researcher verifies and expands)
- Armstrong, Bostrom & Shulman, "Racing to the precipice," *AI & Society*
  (2016): open text at ORA Oxford
  (https://ora.ox.ac.uk/objects/uuid:d87d8e34-22d6-4597-ac31-041fcb63903f) or
  the FHI copy; DOI 10.1007/s00146-015-0590-y.
- Bostrom, *Superintelligence* (2014), the section on development races /
  collective action (for the fuller argument), if accessible first-hand.
- A present-day proponent primary: a responsible-scaling policy or a coordination
  proposal document stating what proponents want done.
- An empirical primary/serious secondary on competitive pressure and safety
  tradeoffs among current developers (on-record statement or a safety-index /
  governance report).

## Relevant prior coverage — link, do not re-teach
- `what-could-go-wrong/intelligence-explosion` — the discontinuity/decisive-
  advantage assumption this argument leans on; strong Background link and a
  place to point instead of re-teaching takeoff.
- `the-levers/responsible-scaling-policies` — a live proposal proponents point
  to; link when covering "what they want done."
- `what-could-go-wrong/instrumental-convergence` / `deceptive-alignment` — the
  "catastrophe if unsafe" end-state the model assumes; link, do not re-teach.

## Constraints and traps
- **The exact strings "AI race" and "artificial intelligence race" are banned
  (max 0).** Describe it as competitive pressure, a development race, an arms-
  race dynamic, racing to deploy — never the banned phrases. This is a hard
  constraint the proof enforces.
- "load-bearing" is banned (max 0) — name the specific assumption the argument
  needs. ("machinery" is also banned.)
- Do not let the piece become a governance/policy op-ed; it teaches an argument
  and audits its assumptions. Keep the desk's neutrality.

## Structures NOT to inherit (recent habits)
- Avoid comma-triad headings/deks; vary from recent WCGW shapes (jailbreaks:
  "Safety training teaches a pattern, not a boundary" — do not echo the
  "teaches a pattern, not a boundary" mold).

## Neighboring articles tonight (keep distinct)
alphago (Evidence), energy-per-query (Instruments), over-refusal (Mechanics),
microsoft-tay (When AI Breaks). over-refusal is a safety *mechanism*; this is a
safety *incentive argument*. Keep them clearly separate.

## Output paths
- Article: `.nb-work/what-could-go-wrong/racing-dynamics/library/what-could-go-wrong/racing-dynamics.html`
- Artifacts under the matching `agent-artifacts/what-could-go-wrong/racing-dynamics/`.

## Production
harness `claude-code-routine`; writer model `claude-sonnet-5`. Effort:
researcher/editor high, writer medium, coach low. Template `lesson`; mode
`open`; order null; date 2026-08-02.
Tags (nb-meta): coordination, competitive-pressure, ai-safety, governance.
