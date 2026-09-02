# Editorial review: the-evidence/constitutional-ai (editor/02)

This is a targeted re-read of the single sentence routed in editor/01. Round 01
approved everything else in the piece (the directional results, the three
tensions, the verbatim constitution principles, the "ad hoc" admission, the
Figure 4 asset, and every link), so this read confirms the one fix and checks
that it introduced nothing new. It does not relitigate the settled reads.

## Skeptic

The routed break was a false attribution: the present-day section quoted
Anthropic's Amanda Askell as saying the constitution is "addressed to Claude and
used at different stages in the model's training to shape its character," wording
that the TIME source (s6) presents as the reporters' own narration, with no
quotation marks and no attribution to Askell.

The corrected researcher/02 evidence settles the source reading firsthand: the
s6 Quote field now records the wording as TIME's own narration (Ostrovsky and
Perrigo), reached by two independent browser-shaped routes past the page's 406,
with the full sentence transcribed ("It is addressed to Claude and used at
different stages in the model's training to shape its character, instructing it
to be safe, ethical, compliant with Anthropic's guidelines, and helpful to the
user—in that order") and Askell's name confirmed absent from that sentence and
the one before it. A genuine, correctly marked Askell quote elsewhere in the
piece is recorded for contrast.

The article's reworded sentence now reads: "TIME's reporting on the update
describes the constitution as text addressed to Claude and used at different
stages in the model's training to shape its character." Checked against the
corrected evidence:

- The wording is attributed to TIME's reporting (source s6), not to Askell.
  Askell's name appears nowhere in the article now; a grep for it returns only
  the reworded description line, which no longer names her.
- It no longer presents as quoted speech: the quotation marks are gone and the
  sentence reads as reported description ("describes ... as text ...").
- The wording "addressed to Claude and used at different stages in the model's
  training to shape its character" matches the evidence's transcription
  verbatim, and the following sentence's ordering ("safety, then ethics, then
  Anthropic's own guidelines, then helpfulness, in that order") tracks the
  evidence's "safe, ethical, compliant with Anthropic's guidelines, and helpful
  to the user—in that order."
- The s1-s5 citations around this passage are untouched, and the change does not
  reach the sizing argument, which never depended on who spoke the words.

I opened the s6 href as the article prints it,
https://time.com/7354738/claude-constitution-ai-alignment/, with a
browser-shaped request: HTTP 200, no redirect away, landing on the source's own
TIME page. It resolves.

## Cut

Ran the slop and correctness pass over the reworded sentence and its paragraph,
since that is the only prose that changed. The sentence carries a fact — the
present-day description of the constitution and its source — and is grammatical
and clean: "TIME's reporting on the update describes the constitution as text
addressed to Claude and used at different stages in the model's training to
shape its character" is one main clause with a correctly hung participial
description, no dangling referent, no reflex punctuation. It is not a signpost
and survives the delete test: removing it loses the outside register the
present-day section spends its argument on. No borrowed phrasing, no prompt
leakage; "shape its character," which the next paragraph turns against the 2022
claim, is TIME's word carried in as reported description, not a planning label.
No new slop entered. Nothing to cut.

## Reader

Reading the present-day section straight through, the passage still delivers
what it did in round 01 — the drift from a preference-labeling result to a
document said to "shape character" — but now sourced honestly to the reporters
who describe that drift rather than put into the mouth of the person it is
supposedly coming from. The reader gets the outside-register point without being
misled about who said it. The prose sits where round 01 left it, closer to the
voice-guide exemplars than to a median summary. The fix improves the piece
without costing it anything.

## Edits

- None. The writer's reattribution is correct and complete; nothing was mine to
  edit in place, and the rest of the article stands as left in round 01.

## Required work

- None. The editor/01 researcher and writer items are both resolved: the
  evidence record's s6 entry is corrected, and the article reattributes the
  wording to TIME's reporting with the quotation marks removed.

## Decision

approve — the one routed misattribution is fixed: the wording is now attributed
to TIME's reporting (s6), not to Askell, no longer reads as quoted speech,
matches the corrected evidence verbatim, the s6 href resolves to its own page,
and the reworded sentence introduced no new slop.
