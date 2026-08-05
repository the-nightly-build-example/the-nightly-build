# Draft handoff: what-could-go-wrong/mesa-optimization (01)

## Original work (one sentence)

The article makes the goal-misgeneralization authors' own disclaimers of
mesa-optimization the hinge of the lesson, and places the never-identified
inner optimizer between the two interpretability findings the record holds
apart (traced arithmetic as a scattered "bag of heuristics"; learned Sokoban
planning that serves its intended goal), so the reader can sort any claim about
this risk onto a demonstrated-versus-argued line the evidence record states
only piece by piece.

Where it is visible: sections "The part that has been shown" and "The part no
one has caught," and the takeaway that resolves the opener on which side of that
line a given claim sits.

## Proof result

`./nb check ... --series what-could-go-wrong --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** words 2090,
reading_minutes 9, sources 9 (7 primary, 2 secondary). No warnings left
standing.

## Verbatim quotes verified this session

All quotations were checked character-for-character before printing, since the
evidence record flagged every non-Meinke quote as captured through a rendered
fetch:

- Langosco et al. (s2): "goal misgeneralization can occur without
  mesa-optimization"; "these are in fact two distinct behaviors"; "our work
  does not demonstrate or address mesa-optimization" — verified against
  ar5iv 2105.14111.
- Shah et al. (s3): "a learned model implements a search algorithm with an
  explicitly represented objective"; "We do not make this assumption" —
  verified against ar5iv 2210.01790.
- Nikankin et al. (s4): "neither robust algorithms nor memorization"; "bag of
  heuristics" — verified against the arXiv 2410.21272 abstract.
- Greenblatt et al. (s8): "selectively complying with its training objective in
  training to prevent modification of its behavior out of training"; "did not
  instruct the model to fake alignment or give it any explicit goal" — verified
  against the arXiv 2412.14093 abstract.
- Meinke et al. (s7): the system-prompt line ("Nothing else matters. Make sure
  you achieve YOUR goal at all cost.") and the open-question caveat ("without
  in-context learning remains an open question not addressed by this study") —
  used as recorded; the evidence record states these were extracted verbatim
  from the PDF. Not independently re-fetched this session.

## Desk-rule compliance notes

- No company is named as an authority. Every claim is attributed to named
  authors/papers; model names (frontier models, a production model) appear only
  as experimental subjects, never as a lab's word.
- Ngo et al. and Turner both cited off the paper's own framing; Ngo paraphrased
  (not quoted) since that wording was a flagged rendered fetch and no quotation
  was needed.
- goal-misgeneralization, deceptive-alignment, and reward-hacking are plain
  prose links, not numbered sources, per the press's "link, don't re-teach"
  rule. The scheming primaries (Meinke, Greenblatt) are cited only for the
  spontaneous-versus-handed point this lesson needs, not to re-run the
  deceptive-alignment lesson.

## Open questions

None blocking. Two judgment calls the editor may want to weigh:

1. The pull quote ("A wrong learned goal is not yet a mesa-optimizer") repeats a
   sentence that also runs in the adjacent prose. That is the intended
   pull-quote usage (promote a sentence from the body), and the sentence is the
   article's central move, so it is deliberate emphasis rather than duplication
   to cut.
2. The two paired headings "The part that has been shown" / "The part no one has
   caught" use a deliberate parallel to make the demonstrated/argued line
   structural; the other three headings vary in shape. Kept as craft, not as a
   stamped cadence.
