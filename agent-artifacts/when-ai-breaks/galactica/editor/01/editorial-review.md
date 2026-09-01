# Editorial review: when-ai-breaks/galactica (editor/01)

## Skeptic

Thesis: Galactica produced confident, authoritative-looking science, including
citations invented for real researchers, because it was a language model writing
the likely continuation rather than a checked fact; the science-styled surface
made those inventions read as results; the failure was foreseeable, since the
builders' own paper had measured the citation fabrication and warned against
production use; and the same weakness now lives in retrieval-backed research
assistants, better hidden. The piece states this and defends it in order.

The claims it stands on, and how each held:

- **Corpus, scale, release, and pause dates.** 106 billion tokens from 48 million
  papers/textbooks/lecture notes plus millions of compounds and proteins; largest
  model 120B; demo live at galactica.org on 15 Nov 2022; paper to arXiv the next
  day; demo paused 17 Nov 2022. All match the evidence Numbers section and s1. I
  opened arxiv.org/abs/2211.09085: title, first author Ross Taylor, and v1 stamp
  "Wed, 16 Nov 2022 18:06:33 UTC" confirmed. The one soft spot: the 15 Nov demo
  launch is cited to s1, which cleanly owns the "next day" arXiv fact but does not
  itself narrate the demo's launch date; the date is firmly corroborated across the
  record, so this is a citation-precision note, not a break. Left as is.

- **The launch-day fabrications.** False Schiff biography (sent to Maryland; he was
  at Stanford), transit-of-Venus dates with "the last known transit of Venus was in
  1882," and the invented Solomonov-Russell coin-flip paradox. I opened the NYU page
  (cs.nyu.edu/~davise/papers/ExperimentWithGalactica.html): dated 15 Nov 2022, Davis
  and Sundstrom, all three examples present, the 1882 line verbatim. Held.

- **The warning shipped on every output, and the fabrications went out under it.**
  The verbatim banner is shown in the note; the prose says the warning was accurate
  and the output still read as a settled reference. The lesson does not claim Meta
  gave no caution — the brief's central accuracy point. Held. (galactica.org is
  gated-not-dead; the printed address is the demo's own home.)

- **The self-measured citation fabrication (Table 26).** At 6.7B, singly-cited
  papers: 13.8% correct, and the model "invented the citation outright more than half
  the time" (54.5%); for papers cited 500+ times, 0.0% fabricated; ablation on 1,705
  methods. Every figure matches the evidence Numbers entry and the stat strip. The
  arithmetic and the direction (fabrication worst for obscure work, near-zero for
  popular) are correct and are the load-bearing engine of the mechanism section.
  Held. This is a primary self-measurement, correctly cited to s1 with locators.

- **Meta stood behind it as a research demo, not a defended product.** LeCun
  contemporaneously ("casually misusing it"), Pineau a year later ("research demo,"
  missing responsible-use guide, "the gap between the expectation... was too big").
  I opened venturebeat.com: Pineau quote, the "not misled" rationale, the missing
  responsible-use guide, and the 17 Nov takedown all confirmed. The steelman is set
  out ("That account is a real one, and the demo was labeled a demo") before it is
  weighed against the paper's own measurement and warning. Held.

- **The weakness lives now in retrieval-backed assistants.** Retrieval closes part
  of the gap but the model still writes the surrounding claims and can misdescribe a
  fetched source; the invented citation is harder to catch because most are right.
  This is the article's synthesis, sourced to s1 for the builders' named fix. Held.

Citations opened as printed. Reachable and landing on the source: s1 (arXiv), s2
(MIT Tech Review — confirmed to reproduce the LeCun launch line, the Black quote,
the content-filter text, and the "three days" framing, all used as secondary), s3
(NYU), s5 (Gary Marcus, 16 Nov 2022, the "pitch perfect and utterly bogus" line
present), s9 (VentureBeat). Gated-not-dead per the brief, printed address is the
source's own page: s4 (Black, x.com), s6 (galactica.org), s7 (Papers with Code,
x.com), s8 (LeCun, x.com). Internal cross-links (hallucination, microsoft-tay,
mata-v-avianca) all resolve in the library checkout. The LeCun launch quote is
correctly attributed to s2, where it is reproduced, not to LeCun's own undated
tweet — the right call.

Display text checked descriptor by descriptor: headline (invented citations for
real researchers; ~two days — both true and defended), dek, and all five subheads
carry only claims the body establishes. Names, titles, and affiliations (Taylor,
Davis/Sundstrom, Schiff, Black at Max Planck, Marcus, LeCun as Meta chief AI
scientist, Pineau as head of AI research) match the evidence. One quotation broke
fidelity: the Pineau line dropped the source's two internal commas, which also made
"was was" read as an error; restored to the evidence and the live VentureBeat
rendering. `data-nb-kind` labels are sound: the paper, NYU firsthand, Marcus's own
post, the three operator/promoter/critic posts, and the demo banner are primary;
MIT Tech Review and VentureBeat are secondary. Nine sources, seven primary.

## Cut

The piece is written close to the voice guide already — plain, concrete, level —
so the slop pass found little. One sentence failed the delete test: "The split is
the mechanism in miniature," opening the paragraph after the stat strip. Removing
it loses no fact and no reasoning step; the concrete sentences that follow ("The
model reproduced the references it had seen often and invented the ones it had
barely seen. Obscure work... is exactly where it failed") carry the whole point,
and the section heading already names the mechanism. Cut.

Edge sentences tested out of order held up: openers and closers of every paragraph,
section, and the article carry a fact or a step. The article's last line ("run on
the same weakness, and it is better hidden than it was in 2022") lands the present
weakness concretely rather than widening into a general warning, as the voice guide
asks. The two negative-parallelism constructions both survive because each corrects
a real, named alternative: "This was not Microsoft's Tay... No one had to attack
Galactica" (the commission's own contrast) and "the most likely text, not the true
one" (the mechanism itself). No dangling referents for a reader arriving cold.

Formula check against the recent-pattern notes: the opener avoids the "what X
switched off in <month>" / "X built Y to..." molds; the closer avoids the "same
task still routes to a person" note; the dek carries a figure but no date and is not
the comma triad; no section heading is a comma-and join, and the five headings read
as a reconstructable argument. No prompt leakage — the mechanism framing ("a system
built to sound like science produces fabrications that read like findings") is the
lesson's taught substance, in its own words, not a lifted planning label.
Punctuation is plain: no em-dashes, colons used properly. Grammar clean.

## Reader

What the piece gives beyond its sources: no single source sets the public
fabrications (NYU, Black) beside the builders' own measured citation-fabrication
rates (Table 26) and the demo's own printed warning, concludes that the failure was
quantified and foreseeable before release, and then carries that same weakness into
today's retrieval assistants where correct-most-of-the-time output hides the
invented citation. That synthesis is the article's, and it matches the writer's
original-work sentence in draft-handoff. Both answers survive. The prose sits closer
to the voice-guide exemplars (Willison's level plainness, Luu's flat statement of
what was counted) than to a median AI summary. The headline, read as the largest
claim, is true and defended.

## Edits

- Cut "The split is the mechanism in miniature." (mechanism section) — failed the
  delete test; the reasoning is carried by the sentences that follow.
- Restored the two internal commas in the Pineau quotation to match the evidence
  record and the live source: "The gap between the expectation, and where the
  research was, was too big." — quotation fidelity, and it removes the "was was"
  misread.

## Required work

None blocking. Notes for the record, no change required:
- researcher: the open evidence question (four reproduction-only sources) is
  resolved as gated-not-dead per this round's brief; no new evidence needed.
- writer: run a fresh proof. My two direct edits changed the body text (one cut
  sentence, one quote repunctuation), so the stamped word count and link/term
  counts should be re-verified before the orchestrator stamps.

## Decision

approve — the load-bearing figures, dates, quotations, and the warning/steelman
framing all hold against the evidence; I made two direct edits (a slop cut and a
quotation-fidelity fix) that need a fresh proof before stamping.
