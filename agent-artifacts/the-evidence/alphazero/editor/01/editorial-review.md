# Editorial review: the-evidence/alphazero (editor/01)

## Skeptic

Thesis: AlphaZero's durable result is the general one (one algorithm learned
chess, shogi and Go from the rules alone), while the famous "beat Stockfish"
result is conditional, and the harsh conditions people cite belong to the 2017
preprint, not the 2018 Science paper that is the record. The piece stands on
four claims.

1. The generality claim: one network, no human games, no opening book, no
   handcrafted evaluation, learned three games to top level. Held. Both papers
   own it; the evidence records it as solid and uncontested. Training figures
   check against the Science record: chess ~9 h, Go ~13 days, 700,000 steps on
   batches of 4,096, first past Stockfish at 4 h and Elmo at 2 h, 5,000
   first-generation TPUs for self-play and 16 second-generation to train.

2. The two-match claim, which the round focus told me to push hardest. Held,
   and it is the article's strongest work. The flimsy conditions (100 games,
   one minute per move, Stockfish 8 on 64 threads with a 1 GB hash, no opening
   book, AlphaZero on 4 TPUs, result 28/72/0) are attributed to the December
   2017 preprint and cited to s2 throughout the two-matches section and the
   comparison table. The Science match is taught as the record: 1000 games at
   3 h + 15 s, Stockfish on 44 cores, a separate opening-book match and a
   latest-development-build match it also won, result 155/6/839, cited to s1. I
   checked every match figure and condition in the prose, the stat strip, and
   the table against the evidence Numbers section; all reconcile, including the
   per-colour split (black: won 2%, drew 97%) and the search-speed ratio (about
   60,000 vs 60 million positions a second, a thousandth). The table's W/D/L
   ordering is internally consistent with the evidence (155 wins, 839 draws, 6
   losses). No flimsy condition leaks onto the Science paper.

3. The surviving-caveat claim: even the Science match leaves the TPU-vs-CPU
   hardware unnormalized (DeepMind's own "not directly comparable", cited to
   s6), keeps Stockfish 8 as the opponent, and was DeepMind's in-house match.
   Held and correctly sourced. The endgame-tablebase point is stated as read
   from silence in a note labeled "Not stated in either paper", not asserted,
   which is what the round focus required.

4. The arc claim: independent replication came later (Leela won TCEC Season 15
   in May 2019, +14 =79 -7, cited s7/s8) and the ranking did not stay (Stockfish
   NNUE, at least +80 Elo, 2020, cited s9). Held; figures match the evidence.
   The durable finding is framed as convergence on neural-evaluation-plus-search,
   not permanent AlphaZero superiority, as the brief directed.

Display text: headline, dek, subheads, stat labels, and table caption all check
out as claims and as labels. "AlphaZero beat Stockfish twice, under different
rules each time" is the piece's spine, defended in full. The dek adds the two
papers and the 155-to-6 score without restating the headline; its "quotes X,
not Y" contrast corrects the exact misconception the article is about, so it is
earned rather than reflex.

data-nb-kind audit: five primary (s1 Science, s2 preprint, s3 Romstad's
statement carried by a Lichess repost, s6 DeepMind's own blog, s7 the Lc0
project site) and four secondary (s4/s5 chess.com reporting, s8/s9 Chess
Programming Wiki). The s3 primary label is defensible: the authority is
Romstad's own statement, and the repost only carries it. Floor cleared (9
sources, 5 primary, 1+ secondary).

Citations opened, each as printed. s2, s3, s4, s5, s6, s7, s8, s9 all resolve
and land on the source, and each carries the specific figure or quotation it is
cited for (verified the Romstad "apples to orangutans" and time-control lines,
the Nakamura/Kaufman opening-book reactions, the 155/6/839 and time-control
reporting, the TPU/Titan V line, the Lc0 self-description, the +14 =79 -7
superfinal record, and the +80 Elo NNUE line). s1 (science.org DOI) returns 403
behind the publisher paywall; it lands on the paper's own page, which the
evidence already flagged as gated, not dead, so it is the source itself, gated,
not a wrong endpoint.

Two figure discrepancies against the primary, both fixed directly (see Edits):
"16 more" TPUs implied a second batch of first-generation chips, but Science
records the 16 as second-generation; and "the strongest earlier version of
AlphaGo Zero" carried a superlative the evidence does not support (the Go
opponent is the 3-day version, and the 40-day version was stronger).

One soft point, checked and left: the article says Nakamura and Kaufman
"objected most to" the missing opening book. That is solid for Kaufman and
supported for Nakamura by the owning secondary's lead framing, though the same
source shows Nakamura also weighted the hardware handicap heavily. It is
context for the 2017 criticism, not a load-bearing claim, and it is fairly
sourced, so it stays.

## Cut

The prose is clean; the slop pass turned up no interchangeable sentences to
delete. I ran the placeholder test on every edge sentence and on the lines that
sound like the best in their paragraph ("The chess figure is more lopsided as a
headline than as a contest", "Two claims come out of AlphaZero, and they have
aged differently", "The method reproduced", "What lasted is a change in method
rather than a ranking"). Each carries a fact or a reasoning step the paragraph
then spends, so each survives. "What lasted is a change in method rather than a
ranking" uses negative parallelism, but the misconception it corrects (that
AlphaZero's legacy is that it out-ranks Stockfish) is the one the whole piece
names, so the contrast is earned.

One structural component failed and was removed: a "Verdict" note
(nb-note-strong) closed the last body section. The press editorial direction
forbids exactly this ("Do not close the body with a Verdict note, or any block
that restates the finding... a leftover, not a model to copy"), and the block
restated the judgment the takeaway bookend then lands. Every fact in it already
sits in the body and the holdsup component, so the cut loses nothing and removes
a stack-of-blocks ending (holdsup followed by verdict). No source was orphaned:
s1 and s9 remain cited elsewhere.

One grammar fix: "Two things the Science account leaves standing." was a verbless
fragment wedged between two full sentences; recast as a complete sentence.

Heading and dek shapes checked against the recent-pattern notes. Headings vary
(three noun phrases, one sequential clause), which answers the commission's ask
to break the all-full-sentence habit; the one clause heading ("The method
reproduced, then Stockfish caught up") is concrete and sequential, not the
abstract comma-and closer mold that was flagged. The dek is not the comma-and
mold and not a colon subtitle. No prompt leakage or borrowed voice-guide phrasing
found; the distinctive phrases in the draft are the article's own or attributed
quotations.

## Reader

Read straight through as the paper's reader, meeting AlphaZero for the first
time: what I have that the sources alone would not give me is a way to tell a
correct citation of AlphaZero from the common wrong one. I can now say which
match a quoted condition belongs to, why the Science match answered most of the
2017 complaints and what it still did not settle, and how the story ends with the
method spreading into Stockfish while the ranking reversed. The original-work
sentence claims exactly that separation and that split, and both survive the
read. The prose sits closer to the voice-guide exemplars than to a median
summary: it puts each match figure with its conditions in the same breath, gives
denominators, and lands a plain judgment without hedging or sneer. The headline,
read last as the largest claim, is carried by the body.

## Edits

- Removed the closing "Verdict" nb-note-strong block from the what-held-up
  section (press direction bans a Verdict close; it restated the takeaway).
- Recast the fragment "Two things the Science account leaves standing." as "The
  Science account leaves two things standing."
- Changed "16 more trained the network" to "16 second-generation TPUs trained
  the network" (Science records these 16 as second-generation, not more
  first-generation chips).
- Cut the unsupported superlative: "the strongest earlier version of AlphaGo
  Zero" became "an earlier version of AlphaGo Zero".

## Required work

- writer / orchestrator: re-run the proof and refresh the nb-meta stamp. The
  Verdict cut lowered the word count from the stamped 1802, so words and
  reading_minutes need restamping before the PR. This is the normal post-edit
  step, not a defect. (Structure re-checked with `nb check --no-check-links`:
  BLOCK 0, WARN 0.)

Optional, not blocking: if the writer can open the Science supplement (tables
S8-S9), the endgame-tablebase note could be upgraded from silence to a reported
fact. The article is correct as written without it.

## Decision

approve. Every central claim held against the evidence and every citation
resolves to its source; the two-match attribution the round focus centered on is
correct, and the remaining fixes were within the edit and made directly.
