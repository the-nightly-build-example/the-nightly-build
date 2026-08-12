# editor review-brief: the-instruments/mmmu (01)

Inputs (read in the order your skill names):
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/writing-coach/01/voice-guide.md — read first.
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/editorial-direction.md — house standard, paper voice, lesson identity, series prompt.
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/commission.md — the assignment, its boundaries, the reader's situation.
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/writer/01/brief.md — the exact writer brief (to catch leakage and habits).
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/researcher/01/evidence.md — open when the first read calls for it.
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/writer/01/draft-handoff.md — original-work sentence, open only on the third read.
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/library/the-instruments/mmmu.html — the article to edit in place.
- template context under /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/.nb-context/.

Output: /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/editor/01/editorial-review.md

After any direct edits you make, the orchestrator runs `nb stamp` and `nb check`
before the PR; you do not run the proof. Route to the writer only what needs new
reporting or a redraft.

## Recent-pattern notes (catch formula against these; one article cannot show it)

Cross-desk house formulas this run is deliberately breaking — flag any that survived:
1. "Why this matters" opening on a nostalgic or second-person recall, or pivoting
   on "This lesson shows/teaches/takes apart...".
2. The opener closing on a "set the two things side by side" line.
3. "The takeaway" landing on a "So next time you [see/meet] a score..." portable
   rule.
4. "this desk" or any body self-reference; the body narrates no one.

the-instruments-specific molds: recent deks use "The score/number behind [popular
claim] is [deflating mechanical description]" and "A perfect X score means the
model [did a trivial thing]"; recent headings lean on "The X that Y"
relative-noun-phrases and the "noun, the appositive" comma mold. A dek or heading
built like those is a formula even if sharp.

## Round focus

Verify the piece teaches how the number is made and then what it can and cannot
support, and that these evidence-record boundaries survived:
- The claim is that a meaningful share of MMMU is answerable from text alone, not
  that most of the score is text. Vision adds roughly 22 points on top of the ~35%
  text-only ceiling. Flag any sentence that overstates this to "most of the score
  is text."
- The MMMU authors' defense (OCR/captions do not lift text-only models to parity;
  strong models still make basic perceptual errors) must be reported fairly where
  the text-answerable point is made.
- The "% answerable without the image" is triangulated across sources, not one
  reported figure; check it is attributed as such (including MMStar's direct
  measurement) and not stated as a precise single number the sources do not give.
- Any comparison of two models' numbers must hold scoring protocol constant
  (Maj@32 vs pass@1 is a protocol difference, not a capability gap). Check every
  head-to-head figure for mixed protocols.
Audit every data-nb-kind (a benchmark's authors are primary for its construction; a
lab is primary for "what it claimed" about its own model and secondary for whether
the score reflects multimodal reasoning). For any chart, check the series is one
protocol and the axes and source are honest. Confirm the three ordered reads, edit
directly what is yours, route only what needs reporting, and record every change.
