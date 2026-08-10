# writer brief: when-ai-breaks/robodebt (02)

Inputs:
- editorial-direction.md — house standard, this paper's voice, the when-ai-breaks prompt, template identity.
- writing-coach/01/voice-guide.md — how this lesson should sound, with exemplar passages.
- researcher/02/evidence.md — the UPDATED record (8 sources): researcher/01's six plus two new primaries. Use this,
  not researcher/01.
- writer/01/brief.md and writer/01/draft-handoff.md — your prior brief and handoff.
- The article you already drafted at library/when-ai-breaks/robodebt.html and its .nb-context/ contract.

Output: writer/02/draft-handoff.md

Proof: ./nb check .nb-work/when-ai-breaks/robodebt/library/when-ai-breaks/robodebt.html --series when-ai-breaks --library /home/user/library-checkout
(run from /home/user/the-nightly-build; --series is required in local mode; use --no-check-links while iterating, links included until BLOCK: 0)

This is a targeted revision to clear the source floor with real sourcing, not a rewrite. researcher/02 added two
primaries the article should now cite for substance it already carries or genuinely gains:
- Amato v Commonwealth (Federal Court consent order, Davies J, VID611/2019, 27 Nov 2019). It owns the concrete
  income-averaging worked example in the court's own numbers ($24,811 / 366 days = $67.79/day, x14 = $949.05
  apportioned fortnightly income, manufacturing a $2,924.28 debt), the "not validly made" / "no probative
  material" finding (the reversed burden, concretely), and the tax-refund garnish. Attribute the originating
  in-court finding to Amato, kept distinct from the Royal Commission's later systemic unlawfulness finding. Note
  the nuance the evidence flags: the Commonwealth conceded a real but much smaller debt was owed, so averaging
  invented the amount, not always the whole debt.
- Senate Community Affairs References Committee report ("Accountability and justice..."). It owns the committee
  majority's recommendation for a Royal Commission, the build cost versus projected savings (about $606 million
  spent against roughly $2 billion projected savings), and a first-hand no-override automation account. Attribute
  the Royal Commission recommendation as a committee-majority recommendation (there was a Government Senators'
  dissent; it was not adopted by the government of the day).

Integrate these by attributing claims to their true owning primary and, where the worked example strengthens the
lesson, use Amato's concrete figures. Preserve the settled work; keep every precision point from writer/01's brief
(averaging plus reversed burden, not automation alone; harm to the record with no death toll; the 2017 Ombudsman
report is not a finding of illegality). Do not independently expand the claim set beyond what researcher/02 opened.
Reach 8 sources with real citations (primary >= 4, secondary >= 1), rerun the full proof to BLOCK: 0 with no
W-SOURCES-MIN, and record in the handoff which claims the two new sources now anchor.
