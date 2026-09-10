# Editorial review: what-could-go-wrong/automated-escalation (editor/01)

## Skeptic

Thesis: the machine-speed "flash war" fear has a real mechanistic core, but the
scenario it rests on has never been built, and the evidence offered as its proof
tests only what a language model does when told to play a country. The piece
stands on five claims, and I tried each.

1. **The speed/coupling "flash war" is Scharre's, not RAND's.** Held. The
   orientation attributes it to Scharre (s1), quotes his two questions verbatim,
   and never puts the speed argument in RAND's mouth. The first brief correction
   holds descriptor by descriptor.

2. **RAND's actual argument is strategic-stability erosion plus automation bias,
   and RAND dismisses the automated-launch nightmare.** Held. The "Hollywood
   nightmare" quote (p. 22), the "works just well enough to feed uncertainty"
   line, the trusted-adviser passage, the 1983 false-alarm stabilizing case, and
   the Perimetr "human in the loop" finding are all carried and matched to the
   evidence record's locators. RAND's balancing case is not omitted, which is what
   the record warned against.

3. **Deployed military AI is ISR/targeting decision-support with a human
   approving strikes; no nuclear-command automation exists.** Held. Maven is
   sourced to CSIS (s3, secondary, correctly labeled), the $480M→$795M figures and
   the ISR-not-launch line match the record, and the flash-crash analogy is marked
   where it strains.

4. **Wargame studies show LLMs escalate in simulation, rarely to nuclear use for
   safety-tuned models, driven by training not "AI as such," and the authors
   disclaim real-world inference.** Held, and this is the claim I pushed hardest,
   because it is the one the piece most wants. The Rivera Table 2 series I verified
   cell by cell against the evidence record: GPT-4 0.00% (0.00), Claude-2.0 0.00%
   (0.00), Llama-2-Chat 0.20% (0.40), GPT-3.5 0.21% (1.20), GPT-4-Base 7.08%
   (20.40). Exact. The ES weights (nuclear 60, violent 28), the "no statistically
   significant de-escalation" line, and the two limitation quotes ("illustrative
   proof-of-concept"; "particular methodology") match. The GPT-4-Base separation
   in the caption is preserved, so the 7% is not read as representative. The
   shown-vs-speculative line is sharp: the section closes by naming that the
   coupled machine-speed mechanism "has never been built."

5. **Present-day human-control pledges (2022 NPR, Nov 2024 Biden-Xi), with the
   2023 Political Declaration kept distinct as non-binding and non-nuclear.**
   Held. The second brief correction is clean: the Declaration sits in its own
   paragraph, is called "not a nuclear agreement" and "not binding" with the
   verbatim non-alteration quote, and the nuclear pledges are sourced separately
   (NPR via ACA s8; readout s9).

Breaks found and handled:

- **Payne quotations (s6) were not verbatim.** The draft printed `they "showed no
  impediment to nuclear escalation"` and `"never chose accommodation or withdrawal
  under pressure"` as quotations. I opened arXiv 2602.14740: the abstract reads
  "the nuclear taboo is no impediment to nuclear escalation by our models" and "no
  model ever chose accommodation or withdrawal even when under acute pressure."
  The quoted fragments as printed were reworded, so the quotation marks asserted
  words the source does not carry. Fixed by removing the false quotation marks and
  paraphrasing faithfully to the primary. The evidence record carries the same
  non-verbatim wording, so I have routed the record correction to the researcher
  so it does not propagate.

- **Lamparth (s5) "the same game."** The draft said the study "ran the same game
  past 214 national-security experts," which reads as Rivera's identical 8-nation
  game. The record has Lamparth as a distinct fictional US-China crisis wargame
  run past both experts and models. Recast to "put language models and 214
  national-security experts through one crisis wargame," which the quote and record
  support.

- **Dek and takeaway overstated the pledge scope.** Both said "every nuclear
  power has pledged." The evidence supports only the five NPT-recognized
  nuclear-weapon states (the body says so correctly); non-NPT nuclear-armed states
  are not covered. A quantity error in display text reaches every reader, so I
  corrected the dek (nb-meta and dekline) and the takeaway to "the five recognized
  nuclear powers."

- **"First time China joined" rode the wrong citation.** That clause is a
  reporting claim (per the record), but sat on s9, the White House readout, which
  does not carry it. Cut; the load-bearing joint affirmation and its verbatim quote
  stay on s9.

data-nb-kind audit: all twelve labels are correct. The nine primaries are
genuinely author-owned (Scharre's own words, RAND's report, the three study
teams, the readout, the Declaration text, Singer's and Panda-Reddie's own
arguments); the three secondaries (CSIS, ACA, Lieber) report or compile others'
work. No label hides a missing independent source.

Citation hrefs: opened all twelve as printed. Ten resolve (200). RAND (s2) and
the State Department Declaration (s10) return 403 to automated fetching; the
evidence record already documents both as bot-blocks that a human reader reaches,
and neither is a dead address. The Payne arXiv page (s6) resolves and its abstract
carries the qualitative findings the piece now states.

No unverified Payne 95%/76% figures appear anywhere. Only the qualitative findings
and the "21 games" count are used, as the brief required.

## Cut

Two direct cuts on this pass, both from middles, not the arc.

- The orientation section closed on "Whether the fear is grounded depends on what
  real systems do, and on the document usually cited as its origin." A signpost:
  it reports where the argument is about to go and does no reasoning, and the RAND
  section's own opener already makes the handoff. Deleted, not repaired.

- The Rivera paragraph carried "In the neutral scenario, GPT-4 and Claude-2.0 took
  no nuclear actions at all," which the table beneath it states in the two 0.00%
  rows. Deleted as duplication; the interpretive line about safety-tuned models
  keeps the point.

Slop pass: I ran the placeholder test across body, display text, and the prose
inside the note, the stat strip caption, and the table caption. The edges hold on
their own. The takeaway's last sentence, "Nothing loose in the world today
produces it," carries the thesis and stays. The two negative-parallelism
constructions I checked ("not AI holding a weapon or a launch order"; "a claim
about the future, not a fact about the present") each correct a misconception the
piece names, so both are earned. No borrowed phrasing from the voice-guide
exemplars, no prompt leakage from the commission or briefs, no house-formula dek
(the "worry, while the evidence rests on X" reversal is absent) and no
scaffolding-slot headings. Furniture earns its place: the note gives Scharre his
own words, the stat strip anchors the "use it or lose it" figures the prose cites,
and the table carries the model-variance result better than prose could. Nothing
reads as a stack of blocks.

## Reader

Read straight through as the paper's declared reader, then opened the handoff's
original-work sentence. Both answers survive. What the piece gives beyond its
sources is the separation the public debate fuses: the flash-war speed fear
(Scharre) and the wargame-escalation result (Rivera, Lamparth, Payne) are shown to
be different objects, so the evidence everyone cites tests only what a model
chooses when told to play a state, while the coupled machine-speed command
mechanism has never been built. No single source hands the reader that. The prose
sits closer to the voice-guide exemplars than to a median summary: it holds shown
and speculative apart sentence by sentence in Freedman's manner, and it lets real
figures carry the weight in Schlosser's, from the 3-5 warheads and ten-minute
flight to the Rivera table. The headline, reread as the largest claim, foregrounds
the vivid shown result and builds the caveat into its second clause ("their own
authors call a proof of concept"); it leans toward the dramatic where safety-tuned
models mostly did not reach nuclear use, but the caveat and the body's
qualification keep it honest rather than doom.

## Edits

- nb-meta dek: "every nuclear power has pledged" → "the five recognized nuclear powers have each pledged."
- Dekline: same correction as the nb-meta dek.
- Takeaway: "every nuclear power has pledged, on paper" → "the five recognized nuclear powers have pledged, on paper."
- Payne sentence (s6): removed the two non-verbatim quotations, replaced with faithful paraphrase ("no restraint against nuclear use held them back, and none chose accommodation or withdrawal even under acute pressure"); kept the "21 games" count and s6.
- Lamparth sentence (s5): "ran the same game past 214 national-security experts" → "put language models and 214 national-security experts through one crisis wargame."
- November 2024 sentence: cut "the first time China had joined such a statement" (reporting claim on the readout citation) and tightened to "the United States and China went further, jointly affirming" the verbatim quote on s9.
- Orientation close: deleted the signpost sentence "Whether the fear is grounded depends on what real systems do, and on the document usually cited as its origin."
- Rivera paragraph: deleted "In the neutral scenario, GPT-4 and Claude-2.0 took no nuclear actions at all" (duplicated by the table).
- Re-stamped after edits: words 2374, sources 12; proof BLOCK 0.

## Required work

- **researcher.** Correct the evidence record's Payne (source #6) entry: its two
  quoted phrases ("showed no impediment to nuclear escalation"; "never chose
  accommodation or withdrawal under pressure") are not verbatim to arXiv
  2602.14740, whose abstract reads "the nuclear taboo is no impediment to nuclear
  escalation by our models" and "no model ever chose accommodation or withdrawal
  even when under acute pressure." The article is already fixed; this keeps the
  error from reaching future reuse. Non-blocking.
- **researcher (low, optional).** The 2022 NPR human-in-the-loop quotation is
  load-bearing but sourced via ACA (s8, secondary). If a later round wants the
  exact NPR wording held as a direct quote, cite the 2022 Nuclear Posture Review
  primary. The writer brief permitted keeping it light, and it is one quote, so
  this is a note, not a blocker.
- **orchestrator.** W-LENGTH-HIGH stands at 2374 words against the 1200-2200 band,
  down from 2406. After the two middle cuts, the remaining overage is irreducible
  without dropping required content: the desk's full three-part arc, twelve
  required sources (~230 words of counted apparatus alone), both steelmen (Singer;
  Panda and Reddie), RAND's stabilizing case, and the Rivera table. Cutting to the
  band would mean removing a required source or a steelman, which the brief forbids
  and which would truncate the argument's arc. It is a WARN (PUBLISHABLE), not a
  blocker, consistent with the writer's handoff.

## Decision

approve. The two attribution corrections and the shown-vs-speculative line hold
descriptor by descriptor, the Rivera numbers verify exactly, and the fidelity
breaks I found (Payne quotations, Lamparth's "same game," the "every nuclear
power" overstatement, the misplaced China clause) are fixed in place; the only
standing warning is an irreducible length overage the brief treats as publishable.

Production record: reviewed as claude-opus-4-8 (Opus 4.8), effort=high.
