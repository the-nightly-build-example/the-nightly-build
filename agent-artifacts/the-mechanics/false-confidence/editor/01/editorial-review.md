# Editorial review: the-mechanics/false-confidence (editor/01)

## Skeptic

Thesis: a model carries two quantities a user hears as one confidence — the
probability it computes over the next token, which in a base model tracks how
often it is right, and the confidence it types in words, which is generated text
and was never a reading of that probability. Post-training (RLHF) degrades the
honest token-probability calibration, so the default assured tone and the
unsolicited "I'm 95% sure" carry little; a number the model is deliberately
asked for can do better, unevenly.

The claims it stands on, and how each held:

- **A wrong answer arrives in the same tone as a right one, and the model admits
  it.** GPT-4's report is cited for "can be confidently wrong in its
  predictions." Opened s1; the report carries this in Section 5. Holds.
- **Calibration has a precise owned definition, and accuracy does not imply
  it.** Guo et al. (s2) own the definition, the reliability diagram, ECE, and the
  LeNet-vs-ResNet finding. Opened s2. The article's numbers check against the
  evidence record: ResNet erred on ~31% (30.6%), LeNet ~45% (44.9%), a 110-layer
  net on a 100-way task (CIFAR-100). Arithmetic and direction correct. Holds.
- **A base model is well-calibrated; post-training reduces it.** Kadavath (s3,
  opened) supports base-model calibration "in the right format"; the GPT-4 report
  (s1) supplies the pre-trained-vs-post-trained comparison. The note blockquote
  attributed to the report — "The pre-trained model is highly calibrated.
  However, after the post-training process, the calibration is reduced." — I
  checked against the primary's exact wording ("Interestingly, the pre-trained
  model is highly calibrated (...). However, after the post-training process, the
  calibration is reduced (Figure 8)."). The article's trim of the opening adverb
  and the parenthetical gloss is faithful; the retained words are verbatim and
  the meaning is unchanged. No routing needed. Holds.
- **RLHF optimizes human preference, not truth or calibration.** Ouyang (s4,
  opened) owns the mechanism and the 1.3B-preferred-over-175B figure the article
  uses. Holds.
- **Why RLHF degrades calibration is open, not shown.** The article attributes
  the probability-mass hypothesis to Tian (s5) and marks it "a plausible reading
  of the cause, not a demonstrated one." Matches the evidence record's
  instruction to present it as a leading explanation. Holds, correctly flagged.
- **The printed confidence is generated text, not a reading of the logits, and
  is not the only internal uncertainty signal.** Lin (s6) and Kadavath (s3)
  support the trainable P(IK) / verbalized-in-words channels; both opened. The
  article states the softmax "is not the only trace of uncertainty inside the
  model," naming P(IK) and latent representations. Holds.

The two narrowings I was told to break hardest on both hold in defensible form.
(1) Not "zero information": the article confines the uninformative claim to the
default tone and the unsolicited number (Xiong, s7, opened), and states plainly
that an explicitly elicited numeric confidence is often better calibrated than
the token probabilities (Tian, ~50% relative ECE cut), then immediately marks
the recovery "real and uneven" — large on the misleading set, negligible on
plain trivia. (2) Not "the only internal signal": stated explicitly, as above. I
could not break either by rereading the cited sources against them.

Display text audited descriptor by descriptor. Headline "Post-training makes a
model less able to tell when it's wrong" is comparative, not absolute, and is the
settled Figure-8/Tian finding; subject-verb-surprise, no colon mold, no question
hedge. Dek adds the second strand (the two quantities) without restating the
headline and is a two-clause "A, and B", not the banned comma triad. Four
subheads each name a step in the piece's own nouns and reconstruct the argument
in order. No wrong label found in display text.

data-nb-kind audit: 7 primary (s1-s7) + 1 secondary (s8). Every primary is the
firsthand owner of the claim it carries; s8 (Geng) is a genuine survey and is
used only for the "open problem, no settled winner" framing — correct secondary
use. No mislabels. Every citation href (s1-s8) opened as printed; all eight land
on the source itself, titles and authors matching. The figure's data-nb-url
(page 12 of the report PDF) is provenance for the asset, correct.

No broken claim, no miscitation, no missing evidence for anything the argument
rests on. Nothing routed from this read.

## Cut

Two direct cuts, both slop rather than thin reporting:

- The "Why this matters" opener promised the volunteered number "is the least
  informative confidence of all" — an unearned superlative that also ranked it
  below the bare tone, which the body and the takeaway do not support (they group
  tone and unbidden number together as telling you "almost nothing," with elicited
  numbers doing better). Rewrote to "tells you little more than the steady tone
  does," which aligns the opener with its own resolution and with the body.
- "The honest summary is that post-training degrades the useful signal..." — the
  "honest summary is that" frame is self-grading, an accounting of the argument
  rather than a step in it. Deleted the frame and left the synthesis, which
  carries real content (degraded not erased; recoverable sometimes) and stands on
  its own.

The rest survived the sentence-by-sentence pass and the edge pass. The two "not
X" constructions in the orientation section correct real, named neighbor
behaviors (hallucination, sycophancy, both linked), so they are earned contrasts,
not invented strawmen. Semicolons at three section edges each join tightly bound
parallel clauses and each carries a specific finding under the slop test. No
prompt leakage: the reader's situation is reworded, not lifted, and the only
self-reference is in the two bookends, where the template allows it. No borrowed
phrasing from the voice guide's Karpathy/Olah/Nielsen quotations. Furniture is
restrained and each piece earns its place: one equation (the formal calibration
ideal the section teaches, cashed out in its caption), one source asset (the
worked before/after), one note (the report's own words). Reads as a continuous
lesson, not a stack of blocks. No component added or removed.

Recent-pattern checks all clear: the piece opens on one concrete case (ask it two
questions, hear one voice), not a specimen table; the closer is in this lesson's
nouns ("the default tone is not the reading it appears to be"), not a "the X is
where the Y runs out" twist; the dek avoids all three banned molds.

## Reader

Read straight through as the paper's declared reader, I come away able to
separate the token probability a model computes from the confidence it types,
to say why post-training makes the computed one overconfident, and to know that
the volunteered "95% sure" is close to worthless while a number I deliberately
ask for can sometimes beat it. That is more than any one source gives: the record
holds these as scattered, partly conflicting findings, and the piece orders them
into one retraceable behavior-to-cause chain. Opening the draft-handoff's
original-work sentence, it claims exactly this assembly-into-one-spine, and the
article delivers it. Both answers survive, so the piece teaches rather than
restates. The prose sits closer to the voice-guide exemplars than a median
summary: concrete worked cases (the gauge, the A/B/C/D choice, 70 percent, the
bars below the diagonal), settled and open marked apart, one idea carried through
each step.

## Edits

- Opener: "...the reassuring number a chatbot volunteers is the least
  informative confidence of all." -> "...the reassuring number a chatbot
  volunteers on its own tells you little more than the steady tone does."
  (removed unearned superlative; aligned opener with the takeaway and body).
- Stated-confidence close: deleted the self-grading frame "The honest summary is
  that" and recast the sentence as a plain synthesis ("Post-training degrades the
  useful signal rather than erasing it, and some of it can be recovered by asking
  in the right way, sometimes.").

## Required work

None blocking. The article is publishable as edited.

- Non-blocking, owner researcher (record integrity only): the evidence record
  (researcher/01/evidence.md) states GPT-4 Figure 8 gives "NO numeric ECE" and
  the magnitude is "only shown visually." That is factually wrong about the
  primary — Figure 8 prints ECE: 0.007 (pre-train) and ECE: 0.074 (ppo), and the
  committed asset-1.png faithfully reproduces those annotations. The writer
  already flagged this in draft-handoff.md. It does not block this article: the
  prose is qualitative, the two real numbers are already before every reader in
  the source's own figure, and the worked example teaches the point without them,
  so per the round brief I am not opening a researcher round to move them into
  prose. The correction matters only for the record's reuse by future articles;
  routing it there is the orchestrator's call.

## Decision

approve — both narrowings hold in defensible form, every citation resolves to its
source, the asset is a faithful crop, and the two remaining slop touches were
fixed in place; no publication-blocking work remains.
