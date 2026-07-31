# Editorial review 01 — editor — the-evidence/the-bitter-lesson

## Skeptic

Skeptic: thesis "Sutton's own worked examples carried more hand-built human
structure than his four sentences report, the essay itself is a ~1,100-word
historical induction over four cases with no data of its own (weaker, on that
axis, than the measured scaling evidence and the human-designed systems the
field kept building), and its narrow claim about hand-coded heuristics losing
to search/learning still holds"; tested 11 claims against the evidence record
(essay date/byline/word count, Sutton's 2019 dual affiliation, the four Sutton
quotes, Deep Blue's 1997 score/speed and grandmaster-tuned evaluation
function, AlphaGo 2016's supervised-training quote and win figures, AlphaGo
Zero's training-day figures and its date relative to the essay, Kaplan's and
Chinchilla's abstract figures and the Gopher/MMLU comparison, the
Transformer's BLEU/training-time figures, InstructGPT's 100x-parameter
figure, Brooks's quotes and response date, Wikipedia's citation-count claim);
broke: (1) "AlphaGo Zero, published five months before Sutton's essay" —
AlphaGo Zero (Nature, Oct 2017) predates the essay (13 Mar 2019) by roughly
seventeen months, not five; recomputing the arithmetic against the two dates
in the evidence record and the general record catches this. (2) The
Transformer paragraph attached "reached in 3.5 days on 8 GPUs" to the 28.4
BLEU English-German result; the evidence record's verbatim abstract ties that
training-time figure to the separate 41.8 BLEU English-French result, not the
one actually cited in the sentence — a denominator/owning-claim mismatch. (3)
Source 11 (Rodney Brooks, "A Better Lesson") carries `data-nb-kind="primary"`
in the Sources list, but as the article actually uses it — quoted only to
rebut Sutton's essay, never to source its own independent finding — it is the
critique, and the review brief's explicit audit standard for this piece is
"the essay and the scaling papers are primary; a critique is secondary." All
other claims and every named person's title/date/quote checked verbatim
against the record and held.

## Cut

Cut: 4 sentences/clauses (all removed the two factual errors above plus two
self-reference violations, none required new prose); worst tell: a body
sentence read "without telling **the reader** which of two systems... the
sentence is about" — a direct hit on the floor's ban on ever mentioning a
reader in body prose. A neighboring paragraph opened with "**Set** the
essay's evidence against what the field built to test the same question
later" (a pure signpost, deleted along with a full sentence describing what
was about to happen) and named the newsroom directly ("Two papers **this
course** has already covered") — the same self-reference the floor bans under
"this dossier." No stock revelation frames, no reused recent-piece openers,
no colon-subtitle headline, no formulaic dek mold, banned-terms budget clean
(`leverage` 1/1 in Sutton's own quoted phrase, em-dash 0, all zero-budget
terms absent).

## Reader

Reader: this gives me the size of the foundation under a slogan I keep
hearing cited as settled — Sutton's own examples audited against the primary
record each system left (Deep Blue's grandmaster-tuned evaluation function,
AlphaGo 2016's human-game training data), set against the measured scaling
evidence that came after (Kaplan corrected by Chinchilla) and the
hand-designed systems the field built anyway (the Transformer, InstructGPT) —
a three-way comparison no single cited source makes, matching the draft
handoff's original-work sentence. Neither a takedown nor an endorsement: the
"What holds up" panel credits Sutton's narrower claim (hand-coded heuristics
losing to search and learning, AlphaGo Zero's knowledge-free result) as
plainly as the "What to be careful about" panel names where the citation
overruns the text. Prose reads close to the voice-guide exemplars — flat
opening claim, no hedge-padding, concrete numbers throughout — not a median
AI summary.

## Direct edits made

1. `AlphaGo Zero, published five months before Sutton's essay` → `AlphaGo
   Zero, published before Sutton's essay` (removed a wrong, uncomputed date
   gap; ~17 months, not 5).
2. `results while training faster: 28.4 BLEU on one 2014 English-German
   benchmark, more than 2 points above the prior best including model
   ensembles, reached in 3.5 days on 8 GPUs` → `results: 28.4 BLEU on one
   2014 English-German benchmark, more than 2 points above the prior best
   including model ensembles` (removed a training-time figure misattributed
   from the paper's separate English-French result).
3. `without telling the reader which of two systems` → `without telling
   which of two systems` (removed the body's only reader-address, banned by
   the house floor).
4. `Set the essay's evidence against what the field built to test the same
   question later. Sutton's argument...` → `Sutton's argument...`, and `Two
   papers this course has already covered, both filed` → `Two papers, both
   filed` (removed a signpost sentence and a self-reference to the
   newsroom/course).

All four are pure deletions or word-removals; no new prose was written.
Re-ran the proof after each batch: `BLOCK: 0 / WARN: 0 / verdict:
PUBLISHABLE`, unchanged from before the cuts — the word-count delta from
these cuts (~34 words off the declared 2,198) stayed inside whatever
tolerance `nb check` allows, so `W-SELF-COUNT` did not fire and no
`nb-meta` sync is required from these cuts specifically.

## Required work by owner

- **Writer:** change source 11's `data-nb-kind` from `"primary"` to
  `"secondary"` in the Sources list (`<li id="s11">`) — Rodney Brooks's "A
  Better Lesson" is used throughout this piece purely as a critique of
  Sutton's essay (the primary document), never as an independent finding of
  its own, and the review brief's audit standard for this piece calls for
  exactly that label. This is a markup/attribute change outside the editor's
  authority to make directly. Rerun the full proof after the change; the
  series floor (min 6 sources, primary ≥ 3, secondary ≥ 1) still clears
  comfortably either way (8 primary / 3 secondary after the fix).

## Decision

REQUEST writer — one markup fix required (source 11's `data-nb-kind`), plus
a fresh proof run after it. No redraft of prose is needed: the skeptic,
cut, and reader tests otherwise passed clean, and the four editorial cuts
already made hold under a clean proof.
