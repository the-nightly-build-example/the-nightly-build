# Voice guide: the-mechanics/why-replies-stop (01)

Write as a teacher who already understands the whole chain and is walking the
reader down it without hurry or performance. The register is confident and
flat, not tentative. The reader is smart and reads widely; they have watched a
reply end cleanly and watched one snap off mid-word, and they want to know what
did that. You are not discovering the answer alongside them. You know it, and
you hand it over one plain part at a time.

Four moves carry this piece. They are how, not what.

**Deliver each step as a plain subject-verb sentence.** Every step of the
backward chain names a real part and states what that part does. The sentence
that delivers a step is the shortest one in its paragraph: the part is the
subject, the action is the verb, and nothing else rides along. The explanation
around it can breathe; the load-bearing sentence does not.

**State the trained fact flat.** The pivotal fact of this piece is a design
decision, not a mystery: the model learned, during training, to produce an
end-of-turn signal when a turn is complete. Write that the way you would state
where a valve sits. No wonder-words ("remarkably", "it turns out"), no hedge
("seems to", "sort of"), no drama. A trained-in behavior is as ordinary as a
physical part, and the sentence treats it that way. This flatness is the
article's signature and the thing the house default does not supply on its own.

**Keep the two causes on separate shelves.** A reply can end for two unrelated
reasons: the model itself produced its end-of-turn signal, or the program
running the model stopped it at a fixed limit. These are two different actors.
When the subject of your sentence moves from the model to the serving layer that
runs it, name the handoff in that sentence. Never let one sentence be vague
about which actor acted. The reader should be able to point at any stopped reply
and say which shelf it came from.

**Let the visible difference be the diagnostic.** The reader can tell the two
causes apart by looking: a turn that ends on a whole thought versus a word cut
in half. Render each cause by the fingerprint it leaves on the screen, with a
concrete before-and-after, never by an abstract label alone.

## Licenses

form: second-person worked prediction
move: CSET puts the reader in the model's position ("If you are given 'Mary had
  a little,' ... you'll very likely suggest 'lamb'") so the mechanism is felt
  before it is named.
bar:  the reader is doing the model's job for one concrete next-token choice,
  not being addressed as a spectator; at most twice in the piece; each use
  produces an actual prediction the sentence then uses.

form: one framing question that the next sentence answers
move: the backward-chain invites "so why did it stop there?"; a single posed
  question can mark the turn from behavior to cause.
bar:  at most one in the whole piece, phrased in the article's own nouns (the
  reply, the end-of-turn signal, the limit), and answered in the very next
  sentence. A second one is a tic; cut it. A question mark left unanswered is
  the Betteridge tell and fails.

form: open humor / wry aside
bar:  not licensed. The register stays plain. An arbitrary-looking detail is
  reported flat, not winked at.

## CSET (Georgetown), "The Surprising Power of Next Word Prediction: Large Language Models Explained, Part 1"
Source: https://cset.georgetown.edu/article/the-surprising-power-of-next-word-prediction-large-language-models-explained-part-1/
Craft:
- cadence: short declaratives that stack. Simple case first, then the
  complication built on top of it, one rung at a time.
- argument: generalizes from a single familiar prediction outward; each worked
  example earns the next claim rather than asserting it.
- evidence: concrete second-person scenarios do the proving; the reader
  supplies the answer and sees the mechanism from inside.
- stance: enthusiastic about capability, honest about the limits of
  understanding; commits where the mechanism is settled.
- notice: marks epistemic boundaries explicitly. States "LLMs work by adding
  and multiplying numbers" without qualification, but flags that experts
  "disagree fiercely" on whether models understand.
- diction: plain nouns, defined the moment they appear ("this long list of
  numbers is called a word embedding"), then reused exactly.
- reader: a smart non-specialist treated as a thoughtful observer, never talked
  down to, never assumed to hold jargon.
- the move the axes miss: it separates the settled mechanism from the open
  question in the same passage, and does not let the open question dilute the
  confidence of the settled part. That separation is the model for keeping the
  trained end-of-turn fact flat while staying honest about what is unresolved.

## Simon Willison, "Things we learned about LLMs in 2024"
Source: https://simonwillison.net/2024/Dec/31/llms-in-2024/
Craft:
- cadence: confident, unhedged declaratives built by accumulation, not by
  stacking subordinate clauses.
- argument: claims rest on observable facts, so they need no qualifier to stand.
- evidence: concrete particulars (specific numbers, specific systems) carry the
  point; nothing rests on speculation.
- stance: a knowledgeable peer, plainly committed, comfortable stating a fact
  without softening it.
- notice: isolates what the core model actually does from what the surrounding
  system does around it ("the actual model just saw text"), refusing to credit
  the model with work the infrastructure performed.
- diction: technical precision next to plain judgment, no ornament between them.
- reader: an interested reader who wants the real distinction, not a simplified
  one.
- the move the axes miss: the clean separation of the model from its harness is
  exactly the discipline this piece needs to keep the model's end-of-turn signal
  and the serving layer's fixed limit from blurring into one cause.

## Julia Evans, "How does gzip work?"
Source: https://jvns.ca/blog/2013/10/16/day-11-how-does-gzip-work/
Craft:
- cadence: short, propulsive sentences; momentum from brevity, not from length.
- argument: works down through a real system to concrete mechanism, structure
  before detail ("the basic idea", then the specifics).
- evidence: names exact things (specific bytes, real values) instead of gesturing
  at them; the concreteness is the teaching.
- stance: earnest, unpretentious, refuses false authority.
- notice: marks honestly what is arbitrary or unexplained rather than papering
  over it.
- diction: everyday words for technical things, no posturing.
- reader: a curious peer invited into the mechanism, not lectured.
- the move the axes miss: her honesty about a genuinely arbitrary detail is a
  useful contrast, not a template. Where gzip's "why four?!" is real mystery,
  this article's end-of-turn signal is a known design choice. Borrow her
  concreteness and her refusal to pad; do not borrow the puzzlement. A trained
  behavior gets stated flat, not wondered at.

## Self-test

A writer following only the house default would explain the mechanism
correctly, but would likely dramatize the trained end-of-turn behavior
("surprisingly, the model chooses to stop") and would let "the model" quietly
stand in for the whole running system. This guide forbids both: the trained fact
is stated as plainly as a physical part, and the model and the serving layer
stay two named actors the reader can tell apart by sight. That flatness and that
clean separation are what this article should sound like beyond the default.
