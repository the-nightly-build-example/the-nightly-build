# Editorial review: the-mechanics/memorization (editor/01)

## Skeptic

Thesis: a word-for-word quote from a model is a specific token sequence that
next-token training fixed into the weights (memorization), not a file it opened
and not a sentence it invented; duplication and scale are the two settled drivers;
how much a model holds is definition-dependent and swings four orders of magnitude;
and the behavior is real but partial and, at its most dramatic, adversarially
provoked.

Load-bearing claims and how each held:

- **Verbatim strings sit in the weights, not an external store.** Stands on
  GPT-2's 604 confirmed memorized sequences recovered by prompting alone, some
  from a single training document (Carlini 2021, s2), and the NYT filing's
  GPT-4-vs-original exhibits (s1). Checked against the evidence record: 604 is the
  2021 owner's figure, correctly cited to s2, and the "appears in one document"
  detail matches the k-eidetic result. Held. The strongest claim I tried to break
  was "stored, not inferred"; the single-document recoveries retire the
  common-phrase objection, so it holds.

- **Duplication raises the odds, log-linearly, with no cliff.** Carlini 2023
  extractability-vs-copies (s3), Lee dedup >1% verbatim / C4 sentence >60,000x /
  ~10x drop after dedup (s4), and D'Souza & Mimno 72-of-240 poems (s5). Every
  figure matches the evidence Numbers block. Crucially the piece says "more copies,
  steadily more likely, with no single count past which memorization switches on"
  and never prints "the duplication threshold" the commission originally reached
  for. The Contradictions note is honored exactly. Held.

- **Scale raises memorization; the slope, not the level, is the finding.** +19
  points per 10x, R²=99.8%, 2-5x within a family (Carlini 2023, s3). The article
  attaches the caveat the evidence demands ("the slope is clean within one model
  family and grows more complicated across families, so it is the trend that is
  settled, not the exact number"), which is where a weaker draft would have printed
  the number as universal. Held.

- **"How much" is definition-dependent, four orders of magnitude.** 0.00000015%
  unprompted k-eidetic (GPT-2, ~40GB) vs ≥1% prompted-extractable (GPT-J 6B, The
  Pile 825GB). Each figure carries its counting rule in the prose and again in the
  three-row table, and the row definitions match the evidence (unprompted single-doc
  recovery; exact next-50 tokens from the true 50-token prefix; canonical poems by
  title). No bare percentage appears anywhere without its definition and scope. The
  0.00000015% figure is cited to s3, which is correct: the evidence Numbers block
  names the 2023 paper as the owner of that restated contrast, and the draft-handoff
  documents the choice. Held. This is the article's central discipline and it is
  clean.

- **The three neighbors.** Retrieval (s1, the same NYT filing's in-weights old
  articles at para 102 vs Bing fetching a post-April-2023-cutoff October 2023
  article at paras 108-114), hallucination (fabrication that matches no source),
  and the genuinely open memorization/generalization boundary. The in-weights vs
  Bing-fetched split is the concrete boundary demonstration and it lands in prose:
  identical-looking output, two different places the text lived. The retrieval,
  hallucination, and gradient-descent lessons are linked as Background and prior
  in-prose links, not re-taught, as required. Held.

- **Real but contested framing.** The Times presents near-verbatim output as
  reachable with minimal prompting (s1 para 98); OpenAI calls regurgitation a rare
  bug it is driving to zero and says the Times used long, manipulated prompts and
  cherry-picked (s9), while conceding duplication drives it. The piece states the
  agreement (duplication) and isolates the true dispute (whether an ordinary request
  trips it), which is the fair reading of the evidence. OpenAI's rebuttal is
  represented fairly, not knocked down. Held.

Display text, descriptor by descriptor: the headline commits to a claim the piece
defends and does not open with "A chatbot." The dek makes a world claim (the
mechanism) and adds the drivers the headline omits, rather than grading the
article's method. Every subhead is a step in the piece's own nouns; none is a
comma-and pair or a scaffolding slot. Named figures, models, parameter counts,
datasets, dates (December 2023 filing, April 2023 cutoff, October 2023 article),
and the $200 / >10,000 / >5% / 150x attack figures all check against the owning
primaries.

`data-nb-kind` audit: s1-s4 and s6-s7 primary (study authors or the plaintiff's
own filing and the authors' own writeup); s5, s8, s9 secondary (Cornell news
office, The Register, OpenAI's interested-party rebuttal). Labels are accurate. The
poem figure resting on a secondary (s5) is corroborative context, not a load-bearing
central claim, so the secondary is acceptable there. No discarded or fabricated
figure (the "33% at 50 vs 65% at 450" summarizer artifact, the unverified per-model
n-gram counts) appears anywhere.

No break survived the read. No claim required routing.

## Cut

The piece is tight; the earns-its-place test found little to remove. I cut one
mild self-reference in the orientation ("the specimen for this lesson" → "the
specimen"), where the voice guide already carries the specimen conceit and "for
this lesson" was filler narrating the piece.

Considered and kept: the pull quote repeats the body's core mechanical sentence
nearly verbatim, but that sentence (weights running next-token prediction, not a
file) is the single idea the lesson turns on, so the repetition reads as deliberate
emphasis, which the standard licenses. The two semicolons in the boundaries section
join tight corrective contrasts (retrieval vs memorization; hallucinated vs
memorized Moby-Dick), a licensed and controlled use, not run-ons. "It is worth
cashing the picture that wants to form here" is faintly meta, but the voice guide
explicitly licenses cashing the file metaphor, and a clean fix would cross into
rewriting, so it stays. "Copied across the crawled web thousands of times" is a soft
illustrative magnitude for the specimen, not a cited stat, but it is not
load-bearing (every quantified duplication claim beside it is sourced) and it earns
the concrete picture.

No prompt leakage. Comparing the authored text against the writer brief, the
required framings appear as reported mechanism, not copied instruction: the brief's
"more copies → steadily more likely" is reworded into the argument, "the duplication
threshold" is correctly absent, and there are no planning labels, selection rules,
or assignment-fulfilled claims. No banned-form tell recurs across headings, deks,
openers, or closers. Grammar and syntax are clean throughout, including display text
and furniture.

## Reader

Read straight through as the paper's smart, code-free reader, what I have that the
sources alone would not give me is a single continuous descent on one specimen
sentence that connects the surface behavior, the next-token training that drives the
loss on a repeated string to zero, the log-linear pull of duplication, the capacity
argument for scale, the definition-dependence of "how much," and the boundary with
retrieval and hallucination drawn from one filing. The sources are scattered papers
and a legal complaint; the synthesis into one mechanism story, plus the
definition-dependence insight and the in-weights-vs-fetched split read off a single
document, is real added value. The draft-handoff's original-work sentence claims
exactly this, and the article delivers it. The prose sits with the voice-guide
exemplars, not a median summary: it keeps one string alive across the descent,
cashes each "it's like a file" figure into literal mechanism and marks where the
figure breaks, and makes the invisible stored string felt through numbers tied back
to the specimen. Both reader answers survive; no redraft is needed.

## Edits

- Orientation: cut "for this lesson" from "So the specimen for this lesson is that
  returned sentence" (self-reference / filler).
- Ran `nb stamp` after the cut: words 2135, sources 9, reading 9 min (in the
  1200-2200 band).

## Required work

None. No publication-blocking issue remains.

## Decision

approve — every figure is tied to its definition, the drivers are framed as
log-linear rather than a threshold, the memorization/retrieval/hallucination
boundaries are clean, and OpenAI's rebuttal is represented fairly; the one open
furniture question (the NYT exhibit asset) does not earn its place, since the
boundary is fully carried in prose.
