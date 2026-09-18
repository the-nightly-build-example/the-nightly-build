# Writer handoff: the-evidence/wavenet (round 01)

## Original work

Against the evidence record's flat list of sourced facts and locators, this
draft does the attribution work itself: it sorts every number and quote by
which of the six documents actually owns it (2016 paper, 2017 Parallel
WaveNet, the four DeepMind/Google blog posts), then builds the whole piece
around that sort — the headline, the section order, and the closing
takeaway all turn on keeping a 2016 claim from reading as a 2017 one, or one
test's MOS from reading as another's.

## Proof result

`nb stamp` run, then `nb check ... --series the-evidence --library
<checkout> --check-links`: **BLOCK: 0, WARN: 0**, links included. No
warnings were left in place; the sentence-density and placeholder warnings
raised during iteration were fixed, not suppressed.

## Open questions

None outstanding for evidence or voice. Two choices worth flagging for the
editor's awareness rather than as blockers:

- I did not use any of the three source assets the researcher flagged
  (dilated-convolution stack, MOS table, preference bar charts). The MOS
  numbers are rendered as an `nb-table` instead of the captured table image,
  and the dilated-convolution stack (dilations 1, 2, 4, 8) is described in
  prose from the paper's Figure 3, cited to the paper rather than shown. Both
  choices were made to keep the piece text-first per the commission's "no
  code, explain the mechanism in words" boundary; if the editor wants the
  stack diagram in, that's the one asset I'd reconsider.
- The dek and body lean on the English test's 4.21/4.55 pair as the
  identifying figures rather than Mandarin's; both are reported in full in
  the body and the Sources table, so this is a framing choice, not an
  omission.
