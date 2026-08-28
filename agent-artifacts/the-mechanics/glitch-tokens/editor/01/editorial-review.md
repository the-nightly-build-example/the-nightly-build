# Editorial review: the-mechanics/glitch-tokens (editor/01)

## Skeptic

Thesis: a token like " SolidGoldMagikarp" breaks a model because the tokenizer's
vocabulary is a fixed artifact built before and from a different corpus than the
model's training, so a string can hold a vocabulary slot while its embedding was
barely trained and sits near random initialization; the failure belongs to a
tokenizer-and-model pairing rather than to a model name; under-training is the
main but not the only cause; detection is solved but the path from a dead
embedding to a specific wrong output is open.

Claims tested and how they held:

- **Original behavior on GPT-3 and ChatGPT, not GPT-2.** Held. The orientation
  reports the repeat-back failure on "a GPT-3 model" and on "GPT-3 and ChatGPT,"
  matching the record (davinci-instruct-beta and ChatGPT). Every "GPT-2" mention
  in the piece attaches to the *tokenizer* or to the corpus, never to the glitch:
  the not-just-rare section states outright that " SolidGoldMagikarp" verified
  under-trained in GPT-J and Phi-2 but not in GPT-2 itself, and the takeaway turns
  the misattribution into the reader's parting test. The brief's central precision
  demand is met; no sentence blames "GPT-2."

- **Under-training is the main but not sole cause.** Held. The where-it-runs-out
  section names the other classes from Land & Bartolo (intermediate-merge
  fragments, tokens unreachable under pre-tokenization, config mistakes) and calls
  the vocabulary-present-but-training-absent case "the cleanest and most common
  case, and it is not the whole catalogue." Not overclaimed.

- **Settled vs open, marked honestly.** Held. Settled: vocabulary built
  separately (s3, s4), near-random embedding for an untrained token (s6),
  detection solved with the 0.1-1%-of-vocabulary figure across 25 models and the
  Pile-aligned models running low (s7). Open: the path from a near-dead embedding
  to a *specific* output is left explicitly unexplained and not invented. The "In
  plain language" note correctly keeps the settled output-suppression mechanism
  distinct from the unexplained specific-output question.

- **Numbers.** 50,257 (s3), ~141 cluster (s1), 0.1-1% (s7), and every per-model
  table cell (GPT-J 200/999, Phi-2 103/999, GPT-2 XL 67/999, Pythia 14/993,
  GPT-NeoX 10/993) match the evidence record exactly. Table caption locator
  "Table 1" is correct.

Breaks found:

- **Wrong letter count (fixed directly).** The vocabulary-first section called
  " SolidGoldMagikarp" "eleven letters." The string has seventeen. Corrected to
  "seventeen" — verifiable arithmetic on the token string in the record, not a new
  fact.

- **StreamerBot origin contradicted by the primary (fixed directly, plus routed).**
  The where-it-came-from section grouped `PsyNetMessage` and `StreamerBot` as
  Rocket League tokens, following the evidence record. Opening the primary
  archaeology post (s5) as printed shows the post attributes `PsyNetMessage` to
  Rocket League but `StreamerBot` (as "TPPStreamerBot") to Twitch Plays Pokemon, a
  Reddit live-updater bot — a different origin. The primary governs, so I cut
  `StreamerBot` from the Rocket League clause; `PsyNetMessage` alone carries the
  software-origin example, and the sentence still makes its point. The record's
  own attribution is wrong and should be corrected (see Required work); the token
  string itself does not even appear in the record's reproduced cluster list.

Display text, descriptor by descriptor: headline ("The token a model can't repeat
back") and all four authored subheads are claims the body defends and carry no
comma-plus-"and" join. The dek ("... reached the model's vocabulary from a Reddit
counting forum and never reached its training") is a claim about the world, not a
grade of the piece, adds origin over the headline, and is none of the three banned
molds. Names and roles (Rumbelow, Watkins, Land, Bartolo) match the record.

Citations: every `data-nb-kind` is right (s1/s3/s4/s5/s6/s7 primary as owners of
their claims; s2 kith.org and s8 Wikipedia secondary). Counts clear policy: 8
sources, 6 primary, 2 secondary. I opened each external href as printed. The three
LessWrong post IDs resolve to posts I, II, and III correctly, the ACL page is the
right paper, and the OpenAI/GitHub links match the record; the two internal
Background/prose links (word-embeddings, letter-counting) resolve on the library
branch per the brief.

## Cut

Eight sentences carried slop or self-reference; I cut or recast each. Two were
body sentences that referred to the lesson or the reader, which this template
confines to the bookends: "getting it exactly right is the whole lesson" (also a
"whole X" punchline) became "the rest is a matter of making it exact," and the
"recall" aside pointing the reader back was dropped. Three were stakes-announcing
or signpost openers with no fact of their own: "it is the fact the whole puzzle
turns on" (the settled marker and the colon payoff stayed), the two-word "Here is
the gap," and "And here is the part that even the people who study these tokens
cannot yet close" (recast so the same "researchers can't close it" meaning leads
the real sentence). One throat-clearing lead-in to the required letter-counting
contrast, "It is worth marking how this sits against," became "This puzzle has a
mirror at."

The Evans wrong-guess rhythm (the "just a rare word" section states what rarity
would predict and why the evidence refuses it) and the Gawande settled/open moves
are earned, not slop, and stayed. The negative-parallelism instances that remain
("not a refusal and not an error message," "differ in kind, not degree," "the
detector settles it, not the spelling") each correct a misconception the piece
actually names, so they pass the earned-contrast test. No borrowed phrasing from
the voice guide's Evans/Travis/Gawande quotations appears in the draft. Headings
and edges show no formula against the recent-pattern notes: the headline is a
noun-phrase declarative distinct from letter-counting's "Why a model ..." frame,
and the letter-counting contrast is drawn explicitly as the reverse puzzle rather
than echoing it. No prompt leakage survives; the one method line ("work backward
from the wrong word to the one decision") is stated in the article's own nouns and
orients rather than restates the brief.

Furniture is load-bearing and not stacked: the definition note carries the
Land & Bartolo term, the stat strip holds the three thesis numbers (each cited in
prose), the table does the per-model pairing work a paragraph could not, and the
"In plain language" note separates the settled half of the mechanism from the open
half. No verdict block, as the press requires. I considered requesting the paper's
Figure 2 (indicator vs. training frequency) as a source asset, but the prose and
the table already let the reader test the pairing argument, so it is not needed.

## Reader

Read straight through, the reader ends able to say why a fluent model returns the
wrong string for one token and not for ordinary words, and able to hear the skipped
step when someone blames "GPT-2." That is more than any single source gives: the
LessWrong posts own the discovery and the archaeology, Land & Bartolo own the
measurement, and the GPT-2 paper owns the corpus, but the continuous backward chain
that ties them into one mechanism, and the settled/open line drawn across it, is the
article's own. The original-work sentence claims exactly that chain, and it
survives. The prose sits closer to the voice-guide exemplars than to a median
summary: it keeps one token in the room the whole way and kills the rare-word guess
with evidence rather than assertion.

## Edits

- Recast "getting it exactly right is the whole lesson" to "the rest is a matter of making it exact" (body self-reference to the lesson plus a "whole X" punchline).
- Corrected " SolidGoldMagikarp" from "eleven letters" to "seventeen letters" (wrong count; the string has 17 letters).
- Cut "and it is the fact the whole puzzle turns on" before the colon payoff (stakes-announcing); kept the "settled engineering" marker and the payoff.
- Cut "StreamerBot" from the Rocket League clause; the primary (s5) attributes it to Twitch Plays Pokemon, not Rocket League.
- Cut the signpost fragment "Here is the gap."
- Cut the reader-address aside "recall" from the GPT-3/ChatGPT sentence.
- Recast "And here is the part that even the people who study these tokens cannot yet close." to "Even the people who study these tokens cannot yet close the last step." (signpost opener).
- Recast "It is worth marking how this sits against a puzzle from the other end of the same series." to "This puzzle has a mirror at the other end of the same series." (throat-clearing).

Proof after edits: `./nb check ... --series the-mechanics --no-check-links` returns
BLOCK 0, WARN 0, PUBLISHABLE.

## Required work

- **researcher (non-blocking record hygiene):** Correct the evidence record's
  origin for `StreamerBot`. Primary s5 (SolidGoldMagikarp III) attributes it to
  Twitch Plays Pokemon (the "TPPStreamerBot" Reddit live-updater bot), not to
  Rocket League as the record's "e-commerce/game backends" line states. The article
  no longer depends on this — I removed the token — so this does not block
  publication; it prevents the error recurring and would let the writer optionally
  re-add `StreamerBot` with the correct origin.

## Decision

approve — the mechanism, its precision constraints, and the settled/open line all
hold against the record; the one factual break in a cited attribution (StreamerBot)
and the wrong letter count are corrected directly, leaving only a non-blocking
record fix for the researcher.
