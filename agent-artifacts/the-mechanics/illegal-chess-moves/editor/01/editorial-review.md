# Editorial review: the-mechanics/illegal-chess-moves (editor/01)

## Skeptic

Thesis: a chatbot's illegal chess move is neither a failed rules-check nor a
random guess; the model is handed the game as move-notation text and predicts the
next move, with no board it tests the move against, so legality is only as good as
the learned next-token statistics, and those statistics vary from near-perfect
(gpt-3.5-turbo-instruct) to hopeless (the chat models).

Claims it stands on, and how each held:

1. **No external board is checked (settled).** Stated cleanly in "There is no
   board, only the moves as text": no separate board the model sets up and checks
   a move against, board knowledge lives in the next-token statistics, marked
   settled engineering. This is the load-bearing step and it holds across every
   experiment in the record. Confirmed as written.

2. **Small transcript-trained models build a readable internal board (settled,
   for those models only).** Held against the sources. Li et al. (nonlinear probe,
   "emergent nonlinear internal representation of the board state") and Nanda et
   al. (linear under a mine/yours encoding, ~99.6% by layer 7, causal edits) both
   check out against the papers and Nanda's companion post, which I opened. The
   original-nonlinear / later-linear correction is reported in order, as the record
   asks. Karvonen's chess result (50M-param, ~16M games, >99.6% legal, 99.2% of
   squares over 10,000 games, unique by move ten) matches both the paper and his
   blog. Yuan and Søgaard's seven-model unsupervised recovery checks out. The scope
   limit is honest: the "Open question" note states plainly that none of this has
   been run on a large chat model, and calls that the biggest gap. This framing is
   accurate and is the honest version the brief demanded.

3. **The late-game collapse is a weak/chat-model property, not a law (settled that
   it is weak-model-only; the cause of the gap is open).** The refutation holds.
   Yedidia's chat-model decay (illegal by ~move 14; ~move 20-30 with the game-score
   prompt) is verified. Acher's roughly-constant illegal rate across game length is
   verified on her post ("the hypothesis that GPT has more and more difficulties
   once a game progresses was not confirmed"). Dynomight's late-game and
   never-before-seen-position observations are verified. The piece explicitly
   refuses to state compounding as universal. Held.

4. **Legality is a property of prompt-plus-model (settled); the size of the
   model-to-model gap has no settled cause (open).** The harness-dependence
   (Acher's 16% of games vs Karvonen's ≤5/8,205, same model) is stated plainly and
   both numbers verify. The Elo-1800 pretraining-filter explanation is correctly
   held at arm's length as "not confirmed against any primary OpenAI document." Held.

5. **The engine is the contrast, not the subject.** AlphaZero/Stockfish appears
   only to show what having the rules and a board buys. The AlphaZero quote ("given
   no domain knowledge except the game rules") is verified. Kept as contrast. Held.

Display text, descriptor by descriptor. The headline ("gpt-3.5-turbo-instruct
plays legal chess; the chatbots don't") names its actors and states a finding the
piece defends; both halves are true. The dek adds the mechanism without restating
the headline. Every subhead is a real step in the piece's own nouns, and the five
of them reconstruct the argument in order. No scaffolding headings.

Two display-text failures found and fixed:

- **David Barry's rating label (fixed).** The draft called him "an 1800-rated
  human" (his FIDE classical rating) attached to a *blitz* match. I opened the
  source: "I am rated 1800 FIDE, 1900 Lichess blitz," and the +380-Elo margin the
  match produces is computed against his 1900 blitz rating. Labeling a blitz result
  with the classical figure understates the opponent and misleads. Corrected to "a
  player rated 1900 at blitz" in both the body sentence and the stat strip. This
  uses the figure the source states for the exact context of the cited result; no
  fact was invented and the claim is unchanged.

- **Source 10 title (fixed).** The draft printed "Yuan & Søgaard · Do Language
  Models Induce the Othello Board Layout?" That is not the paper's title. arXiv
  2503.04421, the huggingface and Semantic Scholar records, and the abstract page
  all give "Revisiting the Othello World Model Hypothesis." A citation whose display
  text names a title the source does not carry is a sourcing failure a reader cannot
  catch. Corrected to the real title.

Citations: I opened all printed hrefs. Every link resolves and lands on the
document its entry describes. One precision failure found and fixed:

- **Source 1 pointed to the wrong Dynomight post for two claims (fixed).** Source 1
  is `dynomight.net/chess/`. That page owns "no other LLM is remotely close" and
  the list of competing theories, both verified there. But two claims the draft
  cited to it — that the strong model plays legal moves deep into the late game and
  in never-before-seen positions, and that prompting lifted gpt-4o to ~1540 Elo —
  live only on the follow-up post `dynomight.net/more-chess/`, which I opened and
  verified ("gpt-3.5-turbo-instruct rarely suggests illegal moves, even in the late
  game"; "completely new board states that have never existed in any game before in
  history"; ~1540 vs the original 1750). A reader clicking source 1 lands on a page
  that does not contain those claims. I added the follow-up as source 14 (primary,
  Dynomight, verified read) and repointed those two citations to it. The theories
  and the "no other LLM" quote still cite source 1 correctly.

`data-nb-kind` audit: twelve primaries and one secondary before my edit, thirteen
primaries and one secondary after adding source 14. Willison is correctly the lone
secondary and is used only for the context claim the piece already flags as
unverified. The internal-board claim rests on three independent groups (Li, Nanda,
Karvonen, plus Yuan and Søgaard); the strength and compounding claims each rest on
multiple independent runs. No wrong-label sourcing found.

## Cut

I made a dedicated slop pass over every sentence, including display text and the
prose inside the stat strip, table caption, and the "Open question" note, then
walked the edges alone, then read the piece cold against the dangling-referent
rule, then ran the delete test.

Six sentences or clauses failed and were cut or reworked:

- "This is the step everything else rests on." — a signpost that reports where the
  argument stands and states no fact. Cut; the claim it introduced carries itself.
- "That is the floor this lesson has walked down to." — signpost plus body
  self-reference. Cut.
- "It helps to see what the model lacks by looking at a system that cannot make
  this mistake." — method-narration opening the engine section. Cut; the section
  heading and "built the opposite way" carry the contrast.
- "Start with what the model is given." — an imperative that narrates the method
  and addresses the reader in the body. Folded away; the paragraph now opens on the
  fact ("The model is not shown a chessboard").
- "and this is where the tidy story fails" — a signpost clause. Cut; the sentences
  that follow show the failure.
- "There is a tidy story about when the illegal moves appear, and it is half
  right." — reworked to "A tidy story explains when the illegal moves appear." The
  cut half repeated the construction of the orientation edge ("That is the
  reputation, and it is only half true"): two "half true / half right" pivots in
  one piece is an internal formula, and the reworked line lets the two paragraphs
  do the correcting.

Body self-reference in the "Open question" note (the lesson template allows only
the two bookends to address the reader or name themselves, which the review brief
underlined). Three phrases broke it and were rewritten to state the same facts
without naming the lesson or the reader: "the models whose illegal moves started
this lesson" became "the models people actually play against"; "the most important
thing this lesson cannot tell you" became "the biggest gap in the evidence"; "the
chatbot on your screen" became "the chat model people actually use."

Edges, out of order: the article's last sentence ("For one model the statistics
are good enough that legality comes almost for free. For the others they are not,
and a bishop slides through a pawn.") carries the conclusion the argument built and
lands on the opening image. It stays. The bookends survive the delete test because
the template hands them the reader-facing work, and each sentence in them belongs
to this lesson's particulars.

Formula check against the recent-pattern notes: the piece avoids "Ask <system> for
<X> and it <does Y>," avoids the "an image generator <does X>" dek shape, and does
not reuse "a model has no <X> to reach for." Headings are varied in build; none
joins two clauses with a comma and "and." Prompt-leakage check against the
commission and briefs: the bookends describe the lesson's method in the piece's own
terms, which the template permits; no planning labels, selection rules, or
assignment-fulfilled claims leaked into the body. No borrowed phrasing from the
voice-guide exemplars (Heaton, Shirriff, Ciechanowski) appears.

Grammar and punctuation: clean after the edits. No new em-dashes introduced (the
note rewrite uses appositive commas). The dek's colon and the headline's semicolon
are borderline against the plainest-mark default but each joins a genuinely tight
pair, and the proof already cleared the counted tells; I left both.

Furniture: the stat strip, the single table, and the "Open question" note each do
real work — orientation, the legality gradient at a glance, and the honest limit —
and none reads as a stacked block. No component added or removed; the note's prose
was corrected in place.

## Reader

Read straight through as the paper's declared reader, I come away with something no
single source gives me: one illegal move resolved into a causal chain nobody
assembles in one place — no external board (settled), a readable internal board in
small transcript-trained models but untested in chat models (settled/open), a
late-game collapse that is a weak-model trait and not a law, and legality pinned to
the quality of learned statistics with the rules-holding engine as the floor. The
draft-handoff's original-work sentence claims exactly that assembly, and it
survives: the piece synthesizes rather than restates. The prose sits closer to the
voice-guide exemplars than to a median summary — concrete mechanism, real figures
doing the scaling, and the settled-versus-open line drawn in the open rather than
hedged. The headline, read last as the largest claim, is one the body earns.

## Edits

- Corrected David Barry's rating label from "an 1800-rated human" to "a player
  rated 1900 at blitz" in the orientation paragraph (the cited result is a blitz
  match; 1900 is his blitz rating and the Elo margin is computed against it).
- Corrected the same label in the stat strip to "a player rated 1900 at blitz, in
  a 10-game match."
- Cut the signpost "This is the step everything else rests on."
- Cut the method-narration opener "Start with what the model is given.", opening
  the paragraph on "The model is not shown a chessboard."
- Rewrote the "Open question" note's three body self-references to remove all
  reference to the lesson and the reader.
- Reworked the compounding opener to "A tidy story explains when the illegal moves
  appear." (removed the repeated "half right" construction).
- Cut the signpost clause "and this is where the tidy story fails."
- Cut the method-narration opener "It helps to see what the model lacks by looking
  at a system that cannot make this mistake." in the engine section.
- Cut the signpost/self-reference "That is the floor this lesson has walked down
  to." in the engine section.
- Corrected source 10's display title to "Revisiting the Othello World Model
  Hypothesis (2025)."
- Added source 14 (Dynomight, "OK, I can partly explain the LLM chess weirdness
  now," dynomight.net/more-chess/, primary, verified) and repointed the late-game /
  novel-position citation and the gpt-4o ~1540 citation from source 1 to it.

## Required work

- **orchestrator:** re-stamp and re-check. My edits changed the body text (a net
  reduction of several sentences) and added one source, so nb-meta `sources` (13 →
  14) and `words` need recomputing. The new source URL
  `https://dynomight.net/more-chess/` resolves (I fetched it), so the link check
  should stay at BLOCK 0. No other owner has outstanding work.
- **researcher:** none. The one open item (whether a large chat model holds a board
  representation) is the article's honestly marked open question, not an evidence
  gap.
- **writer:** none. The citation and label repairs were within editorial reach and
  are done; no new reporting or redraft is required.

## Decision

approve — the two rebuilt framings are honest and correctly marked settled/open,
the Barry label and the two citation faults were fixable in place and are fixed,
and nothing publication-blocking remains beyond the orchestrator's re-stamp for the
changed text and the added source.
