# Draft handoff: the-evidence/atari-dqn (01)

## Original work

This article sets the DQN paper's own operational numbers (human-level = 75% of
a single professional tester, cleared on 29 of 49 games, 23 at the tester's real
score, Montezuma's Revenge at 0) directly against the Extended Data Table 3
ablation, so the reader sees that the durable contribution was the two
stabilization tricks rather than a machine that understood the games, and can
tell the phrase "human-level control" apart from what the tables record.

The work is visible in the article's spine: it builds the naive
network-plus-Q-learning, shows the two named failures it hits, introduces
experience replay and the target network each as the removal of one failure, and
only then reports the "human-level" record beside the phrase.

## Proof result

`./nb check ... --series the-evidence --library /home/user/library-checkout`
(final pass, links included): **BLOCK: 0, PUBLISHABLE.**

One warning intentionally left:

- **W-LENGTH-HIGH (2305 words vs the 1200-2200 lesson band).** Trimmed from 2474
  to 2305 across two tightening passes (removed restatement, split dense
  sentences, cut the number-by-number ablation prose now carried by the table).
  The remaining overage is teaching, not fluff: three ideas each get a plain
  statement, a worked example, and their stakes, per the lesson template's
  "depth over coverage" and "never shrink an idea's explanation to make room."
  Further cuts would thin the value-based-RL worked example, the two-failure
  build, or the record-vs-phrase juxtaposition. Flagging for the editor's call.

No W-SENTENCE-DENSITY or link warnings remain. The byline was set to the stamped
10-minute read; nb-meta dek and the rendered dekline are byte-identical.

## Brief corrections, all honored

- Experience replay attributed to the 2013 precursor (arXiv:1312.5602); the
  separate/periodically-cloned target network attributed to the 2015 Nature
  addition. The ablation (Breakout 316.8 with both tricks on) is the table.
- 29 of 49 stated as the >=75% bar; 23 of 49 as the >=100% ("matched or beat the
  tester") bar, credited to NBC News. Thin baseline stated: one professional
  games tester, ~20 sessions of up to five minutes. Montezuma's Revenge = 0.
- Henderson et al. 2018 used only as evidence about the fragility of the deep-RL
  field DQN founded; the prose states plainly its tests were policy-gradient
  methods on simulated robot control, not DQN and not Atari.
- gradient descent linked to the-mechanics/gradient-descent at first use; no
  AlphaGo tree-search or self-play imported (DQN framed as value-based, no
  search, no model).

## Open questions for the editor

1. **Sutton & Barto source URL.** The evidence record's URL
   (`http://incompleteideas.net/book/the-book-2nd.html`) is http-only and its
   https endpoint serves a self-signed cert, so it fails the engine's
   absolute-https requirement and the link check. I substituted a clean-https
   copy of the same 2nd edition
   (`https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf`) and
   verified it contains Section 6.5 "Q-learning: Off-policy TD Control," Eq. 6.8,
   with the exact defining quote the researcher cited. Locator adjusted to
   "Sec. 6.5, Eq. 6.8" (edition/pagination-stable). Flagging the URL swap in case
   the desk prefers a different canonical host.

2. **Agent57 blog kind (s7).** The evidence marks the DeepMind Agent57 post a
   "first-party retrospective ... treat as corroboration, not an independent
   secondary." data-nb-kind offers only primary/secondary; I marked it primary
   (DeepMind owns the Agent57 result) and attributed it in prose as "DeepMind's
   own retrospective" so it never reads as independent confirmation. The
   independent secondary for the same point is MIT Technology Review (s6).
   Composition still clears the floor without s7 (4 primary / 2 secondary among
   the other six). Editor may reclassify if preferred.
