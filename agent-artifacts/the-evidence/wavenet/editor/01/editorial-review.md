# Editorial review: the-evidence/wavenet (editor/01)

## Skeptic

Thesis: the 2016 WaveNet paper is invoked today as shorthand for solved,
near-human, real-time speech synthesis, but the document itself supports a
narrower claim (a 4.21-of-5 listening-test score, closing roughly half a gap
to natural speech, with no generation-speed claim at all) and everything
people actually mean by "WaveNet" now (fast, deployed, near-human) comes from
later documents. Claims it stands on: (1) the 2016 paper makes no
generation-speed statement, only that generation is sequential; (2) its MOS
result is real but narrow (100 sentences, one speaker, one test, per
language) and does not establish human parity; (3) every speed figure (172,
24,000, 500,000+, 1000x, 50ms) belongs to the 2017 Parallel WaveNet paper and
DeepMind's 2017 blog posts; (4) the widely repeated 4.41 "near-human" score is
not on the same recording corpus as the 2016 paper's 4.21; (5) the durable
contribution is the raw-autoregressive approach, not the 2016 architecture's
speed.

I tried to break each claim against the primary text directly (fetched the
full-text renderings of both arXiv papers, both cited DeepMind blog posts, the
Google Cloud post, the Engadget piece, and the neural-TTS survey, not just the
evidence record). All five held up verbatim: the 2016 paper's only sentence on
generation is the "sequential... fed back into the network" line (§2.1); the
51%/69% gap-closure figures and the full MOS table matched Table 1 and §3.2
exactly; the 172/24,000/500,000+/"three orders of magnitude" figures and the
"poorly suited to today's massively parallel computers" quote matched
arXiv:1711.10433 verbatim; the 4.41 vs. 4.21 corpus mismatch (16kHz/8-bit/25h
vs. 24kHz/16-bit/65h) is exactly as reported; and the survey's "first
neural-based vocoder" / "suffers from slow inference speed" quotes matched
§2.4. No later speed or MOS figure was misattributed to the 2016 paper
anywhere in the draft, and no sentence asserted human parity — the closest,
the 4.41 "near-human" mention, is explicitly framed as a quoted claim the
piece then qualifies, not an assertion of its own.

Breaks found and fixed directly (the right source was already at hand in
every case):

- **Coincidental-number ambiguity, central to the round's focus.** The draft
  used "4.21" for two different measurements — WaveNet's own English score
  and, three sentences earlier, natural Mandarin speech's score — and then
  said "the 4.21 the 2016 paper actually measured is the safer number to
  repeat" without saying which one. Fixed by naming it explicitly:
  "WaveNet's own English score, 4.21."
- **A false causal claim.** The draft attributed WaveNet's generated-music
  drift to the ~300ms receptive-field limit. I reread the passage in full:
  that 300ms figure is stated in §3.1 for the *unconditional speech*
  experiment (the model loses track of a word after 2-3 phonemes), not the
  music experiment. The paper's music section (§3.3) uses a receptive field
  of *several seconds* and still lacks long-range coherence — an unrelated
  problem. This is exactly the kind of figure-crosses-context error the round
  is watching for, just inside the mechanism section rather than the speed
  section. Fixed by rewriting the sentence to describe what the 300ms limit
  actually does (unconditional speech losing the thread of a word), and
  removed the invented link to music, which was also introduced before music
  is mentioned as a task at all.
- **An uncited attribution.** The 51%/69% gap-closure figures were stated as
  "the 2016 paper reported" with no citation to source 1 anywhere in that
  sentence (only two citations to source 6, the Cloud TTS post, on either
  side of it). Added the missing citation.
- **A miscount.** "Three products, three tests, three different percentages"
  mischaracterized 51% and 69% as two different products; they are the same
  2016 paper's two languages. Only the Cloud TTS figure is a different
  product. Rewrote to state that correctly, and fixed "a third deployment"
  (only two deployments — Assistant and Cloud TTS — are named in the piece)
  to "a second deployment."
- **An unsupported technical specific.** "Google's then-new second-generation
  TPU" is not what the cited source says; the Assistant launch post calls it
  only "Google's latest TPU cloud infrastructure." Rewrote to match what the
  source actually states rather than a number the source doesn't give.
- **The evaluation-methodology claim, checked against the paper's Appendix
  B, not just the evidence record's summary.** The draft's dek and body said
  a natural recording was rated "by the same eight raters" / "the same panel"
  as WaveNet's output. The paper's Appendix B states each *stimulus* (one
  system's rendering of one sentence) was rated by eight subjects, that
  stimuli were "randomly chosen and presented for each subject," and that a
  subject could rate "up to 8" stimuli for English — a design that spreads
  many more than eight people across hundreds of stimuli, not one fixed panel
  hearing both the WaveNet and natural versions. This is a claim about the
  paper's own method that the paper does not support, sitting in the dek,
  where it reaches every reader. Fixed in the dek, the nb-meta JSON copy of
  the dek, and the two body sentences that repeated it, to describe what the
  method actually does (each stimulus rated by eight listeners; WaveNet and
  the natural recording scored "in the same test," not "by the same panel").

None of these broke the central claim or required new reporting — each was a
sentence the article could state correctly from the sources already cited, so
I fixed it rather than routing it.

## Cut

Delete-tested every paragraph edge and the article's own last sentence.

- Cut "Mandarin told a similar story at slightly different numbers" — pure
  signpost ahead of the table; the table already shows this, and the
  sentence added no fact of its own.
- Cut the body's one second-person imperative, "look first at what WaveNet
  actually predicts" — the lesson template reserves direct address for the
  two bookends; rewrote as a declarative transition.
- Rewrote the article's final sentence. The draft closed on "The next time
  'WaveNet' comes up as shorthand for solved speech, the question worth
  asking is which of these four documents... the claim is actually resting
  on" — a generic-moral construction ("next time you hear X, ask yourself
  Y") that `spec/editorial.md`'s Form section rules out ("skip the generic
  moral") and that fails the slop test once WaveNet/documents are swapped for
  placeholders. Replaced it with a concrete closing fact already established
  in the piece: the 2016 paper's own claim was "a score of 4.21, on one
  test, in one language, with no speed attached to it at all," which
  resolves the opener's promise (telling which document a WaveNet claim
  belongs to) without moralizing.
- Reworded the colon construction "One paper's two languages, plus a
  different product two years later: three different percentages..." — the
  clause before the colon didn't stand on its own, against the house
  punctuation standard. Split into two plain sentences.
- No em-dash, "leverage," or "load-bearing" overages (2 em-dashes present,
  under the max of 4); no press-banned terms (revolutionary, transformative,
  game-changing, AI race, machinery) appear anywhere.
- Checked every heading, the dek, and the closer against the commission's and
  brief's named recent habits (the "X beat Y on nine of twelve datasets" and
  reversal headline molds, the "Author-and-year's paper does X, and Y" dek
  shape, the "The [noun] that [verb]" heading mold, the comma-triad dek).
  None of the four headings, the dek, or the takeaway match any of them.
- No prompt leakage found: compared the draft's authored text against the
  commission, brief, and voice guide clause by clause; nothing reads as
  reworded instructions, and the commission's own framing ("the gap between
  what the paper measured and how the result is remembered") is reported as
  the article's finding, not repeated as a description of the assignment.
- Furniture check: the stat strip (172 / 24,000 / 500,000+) and the MOS table
  are both documented components, each cited in the prose immediately around
  it, and both do real work the surrounding paragraphs would otherwise have
  to carry in prose alone. No furniture without a purpose; no missed
  opportunity that would have made the piece clearer than the table and stat
  strip already do.

## Reader

Reading it straight through as the declared reader: what I have that the
sources alone would not give me is the sort — which of six-plus documents,
across three years, actually owns each of the numbers "WaveNet" gets credited
with — done once, so I no longer have to redo it myself across a paper, two
blog posts, and a product announcement. The original-work sentence in
`draft-handoff.md` claims exactly this ("it sorts every number and quote by
which of the six documents actually owns it... and builds the whole piece
around that sort"), and it holds up under the read; the sorting is real work,
not a restatement of any one source. The prose sits closer to the voice
guide's exemplars than to a median AI summary: it states figures and lets
them carry weight (Montgomery's habit), and the corrections found above were
precision failures inside an otherwise plainly-stated piece, not register
failures. Rereading the headline as the largest claim — "The 2016 WaveNet
paper never reports its own generation speed" — it is exactly true, and,
after the fixes above, no longer the piece's only exactly-true claim standing
next to a handful of looser ones underneath it.

## Edits

1. Fixed a dangling reference risk and disambiguated "WaveNet's own English
   score, 4.21" from the natural-Mandarin 4.21 mentioned two sentences
   earlier (present-day section).
2. Rewrote the false causal link between the 300ms receptive-field figure and
   generated music; the figure belongs to unconditional speech generation
   losing track of a word, not to music (mechanism section).
3. Added a missing inline citation to source 1 for the 51%/69% gap-closure
   figures (present-day section).
4. Corrected "Three products" to accurately describe one paper's two
   languages plus one later product, and "a third deployment" to "a second
   deployment" (present-day section).
5. Removed the unsourced "second-generation TPU" claim; rewrote to match what
   the cited source states (present-day section).
6. Rewrote the dek (both the nb-meta JSON copy and the rendered dekline),
   removing the unsupported "the same eight raters" / "the same panel" claim
   about the MOS methodology; replaced with "in the same test," which the
   paper's Appendix B supports.
7. Rewrote the two body sentences carrying the same "same panel" / "eight
   listeners rated 100 sentences" imprecision, to state that each stimulus
   (one system's rendering of one sentence) was rated by eight listeners
   (orientation section).
8. Cut the signpost sentence "Mandarin told a similar story at slightly
   different numbers."
9. Removed the body's one second-person imperative ("look first at..."),
   rewritten as a declarative transition (orientation section).
10. Rewrote the colon construction whose leading clause didn't stand alone
    ("One paper's two languages, plus a different product...") into two
    plain sentences (present-day section).
11. Rewrote the article's final sentence, cutting a generic-moral closer for
    a concrete, already-established fact (takeaway).

## Required work

None. No broken central claim, no missing evidence, and no source-policy
failure surfaced in this round; every issue found was fixable from sources
already cited and has been fixed directly.

## Decision

Approve. The thesis and its supporting claims hold against every primary
source I reread in full, the round's highest-risk attribution errors (no
later speed/MOS figure reading as the 2016 paper's, no implied human parity)
were already handled correctly in the draft and remain so, and the errors
this read surfaced — a coincidental-number ambiguity, a false causal claim
about music, an uncited figure, a miscounted "product," an unsupported
technical detail, and an inaccurate description of the MOS methodology's own
rater design — were all precision fixes reachable from sources already in
hand, made directly rather than routed.
