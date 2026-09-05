# Editorial review: what-could-go-wrong/automation-bias (editor/01)

## Skeptic

Thesis: automation bias, the tendency to defer to an automated system and stop
looking for evidence it is wrong, is one of the best-measured failure modes in
deployed aviation and clinical systems; it coexists with real net benefit, has an
equally documented opposite in algorithm aversion, and its present-day
chatbot/deskilling version outruns the evidence. So keeping a human in the loop
is a real but conditional safeguard, not the automatic fix its proponents assumed.

The claims it stands on, and how each held:

- **Bainbridge's mechanism (s1).** Automating routine work leaves the human two
  jobs, watching for the rare failure and taking over, and undermines both:
  reserved skill decays, vigilance lapses (~30 min, after Mackworth), and judging
  the machine that was built to out-judge you is an "impossible task." Reread
  against the paper: the two direct quotes ("formerly experienced operator..."
  and "impossible task") match the evidence record and the source. The evidence
  record does not carry Bainbridge's profession, so I checked the primary: the
  1983 Automatica byline reads "Department of Psychology, University College
  London," so "a psychologist writing about industrial process control" is
  supported, not introduced. Held.

- **The measured effect (s2).** NASA/Prinzel A' fell from .84 (variable
  reliability) to .70 (held constant). Figures and direction match the evidence
  record and the cited primary. The article correctly glosses A' as an index
  (0.5 chance, 1.0 perfect) so a reader does not read it as percent detected.
  Held.

- **Cummings' cases (s3).** Omission/commission definitions are Cummings' own
  (primary use). The 41% vs 3% omission and 65% commission figures are scoped
  in-text as a study "she summarizes," and the 2003 Patriot fratricide is
  attributed to "Cummings, drawing on the Army's own review." Both are the single
  retelling the evidence record flags; neither reaches the headline, dek, or a
  subhead as a bare figure. This is the review brief's central sourcing test and
  it passes. Held as scoped.

- **Net benefit (s4).** Goddard's 26 GPs over 520 decisions: 50.4% correct alone,
  58.3% with advice (+8), the advice pulling 13.1% wrong-to-right and pushing 5.2%
  right-to-wrong, that 5.2% being automation bias measured directly. Every figure
  matches the evidence record, the cited thesis, and the chart script. Held.

- **The opposite failure (s5).** Dietvorst's five studies: people shown an
  algorithm err abandon it even after watching it beat a human. Direction and
  framing match. Held.

- **The present-day evidence (s6, s7, s8).** Bo et al. LSAT 36%→46%, best team
  62%, bad-advice self-reliance below half; Perry et al. less-secure code with a
  false sense of security; Ibrahim's deskilling argument with its own concession
  that the direct evidence is thin. All match the record; the chatbot studies are
  explicitly marked narrow (single sittings, 2022–2024 models). Held.

Sourcing audit: Parasuraman & Riley 1997 and Skitka et al. 1999 are cited by no
one (correct); the use/misuse taxonomy is absent (correct); the present-day
framing is attributed only to Ibrahim, read firsthand. All eight `data-nb-kind`
labels are honest: s1–s7 primary for their own arguments/experiments, s8
secondary for a synthesis. Source floor met (7 primary + 1 secondary).

Citations: I opened all eight source hrefs plus both bookend external links as
printed. All resolve 200 except Dietvorst's publisher DOI (403, a gated APA page,
not dead). The internal Background link resolves to an existing library article,
and its descriptor ("pushed out teachers over a score they could not check")
matches that article's real title and dek.

Display text: headline, dek, and all five subheads verified descriptor by
descriptor against the owning primaries. No contested figure or retold case sits
in display text. The dek's tail ("measured in cockpits, clinics, and the first
studies...") is a three-item noun list inside one clause, not the banned
three-clause comma triad; its main clause is a genuine stance. It stands.

No claim broke. No fix needed routing.

## Cut

A dedicated slop pass, then the edges alone, then the delete test. Six sentences
or clauses failed and were cut or tightened directly; all were signposts,
self-grades, or body self-reference, none from thin reporting, so none routed.

- "The last irony is the sharpest." An evaluative signpost that announces a
  stakes the following sentences deliver; it also introduces "irony" with no
  setup. Cut; the paragraph now opens on the fact.
- "...which points at a fix the next section complicates." A forward signpost
  that narrates the article's own structure. Cut; the Goddard experience finding
  stands on its own.
- The pull quote ("Someone who over-trusts a machine will... walk away from one
  that beats them"). It restated the sentence immediately following it and again
  in the takeaway, near-verbatim, and its "will" overstated the body's more
  careful "can." Deliberate emphasis is valid, but a quote that duplicates the
  takeaway does not earn its place. Removed.
- "...here the ground has to be walked carefully, because..." Throat-clearing
  meta around a real point; tightened to state the point (the evidence is younger
  and thinner than the cockpit's) directly.
- "It is a serious worry with a serious pedigree." An empty assessment (subject,
  copula, grade) whose "pedigree" the prior clause already showed. Cut.
- "That is an honest statement of a gap, and it is the line this lesson has been
  drawing throughout." Body self-reference plus a self-grade; the concrete line
  is drawn by the two sentences that follow it. Cut.

The edges otherwise hold. The article's last sentence states the conclusion the
argument built (the deskilling claim runs ahead of measurement, which its own
proponents concede) and passes the slop test. No negative-parallelism reflex
survives unearned: each "not X, it is Y" corrects a misconception the piece names
(pure-loss framing, the human-in-loop-as-single-fix assumption). No borrowed
phrasing from the voice-guide exemplars; the piece's figures ("body count,"
"Bainbridge's decayed operator at the scale of everyone") are its own. No prompt
leakage: the commission's "shown vs extrapolated" idea is reported in the
article's own terms. Headings are varied in construction and written in the
argument's nouns; none match the recent-pattern molds (no "how X got its name"
opener, no forced "only in simulation" reversal). Grammar and punctuation are
clean.

## Reader

Read straight through as the paper's declared reader. What I have that the sources
alone would not give me: a single frame that treats over-trust and algorithm
aversion as one miscalibration of trust, governed by how reliable the aid is and
how the human is held to account, which turns the record's separately reported
studies into a test I can run on any "keep a human in the loop" claim. Opening the
draft-handoff original-work sentence, it claims exactly that, and the claim is
visible in the article: the aid's reliability is installed as the governing
variable in the Goddard section, algorithm aversion is folded into the same
variable, and the takeaway lands a conditional verdict no single study states. Both
answers survive, so the piece teaches rather than restating its sources. The prose
sits closer to the voice-guide exemplars than to a median summary: worked cases
carry the abstractions, the verdict holds two true claims at once without going
vague, and the shown/extrapolated line is drawn with the "say how far the evidence
reaches" discipline the guide asks for. The headline, reread as the largest claim,
is defended by the body.

## Visual evidence

One chart, Fig. 1, a from-zero waterfall of Goddard's data. I inspected the
committed `chart-1.py` and read the rendered PNG. The numbers (50.4 → +13.1 → −5.2
→ 58.3) match the script, the evidence record, and Goddard's abstract; the
arithmetic closes. The y-axis runs 0–70 from a true zero baseline and is labeled
"Correct prescriptions (% of 520 decisions)"; the four bars are labeled, the
green/red/blue coding reads correctly (help up, mislead down, totals as anchors),
and no legend is needed. Labels, scale, and visual implication are honest. No
correction for the writer.

## Edits

- Cut "The last irony is the sharpest." from the orientation section.
- Cut the trailing clause "which points at a fix the next section complicates";
  the Goddard experience sentence now ends at "the most."
- Removed the `nb-pull` pull-quote block from the opposite-failure section.
- Tightened "and here the ground has to be walked carefully, because the evidence
  is" to "where the evidence is" in the chatbot section.
- Cut "It is a serious worry with a serious pedigree." from the Ibrahim
  paragraph.
- Cut "That is an honest statement of a gap, and it is the line this lesson has
  been drawing throughout." from the Ibrahim paragraph.

## Required work

None. No researcher, writer, or orchestrator item blocks publication. The chart is
correct, no new reporting is needed, and no source asset needs requesting or
removing. Remaining steps are the orchestrator's routine stamp and check on the
edited article (word count will re-derive after the cuts and stays within the
1200–2200 band).

## Decision

approve. The argument is stated at full strength and correctly sourced, the
shown-versus-extrapolated line holds, the chart is honest, and the slop and
self-reference the draft carried have been cut directly; nothing left needs
reporting.
