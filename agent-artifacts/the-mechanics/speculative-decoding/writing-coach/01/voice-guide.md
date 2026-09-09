# Voice guide: the-mechanics / speculative-decoding

The press voice, applied to this one behavior. Short on purpose. The body speaks
to no one and never mentions the lesson; only the two bookends address the
reader.

## What this lesson sounds like

Explain it the way Matt Yglesias explains something he understands cold: plain
claims, concrete stakes, no fuss. The reader is smart and reads widely and has
never seen the inside of an inference stack. When a sentence has to choose
between sounding good and being understood, be understood.

Work backward from the behavior, one step at a time, the way The Mechanics does.
The behavior is concrete and checkable: the same open model, the same prompt, the
same text back, two to three times faster on one service, and the words arriving
in little bursts rather than a steady drip. Every step down names a real part of
the system and says what it does. Stop at the ground: a transformer scores many
positions in one pass, so checking a guess is cheap next to making one.

## The two terms this lesson owns

Define both in the sentence they first appear, in plain words, and then reuse
each name exactly:

- **token**: the small chunk of text a model reads and writes, often a word or a
  piece of one.
- **forward pass**: one sweep of the whole network over the sequence so far, the
  step that produces the next token. It is slow because it drags every weight in
  the model out of memory, not because the arithmetic is hard.

Two more names to keep steady once set: the small, fast **draft** model that
proposes, and the big **target** model that checks. Never swap in "the main
model", "the verifier", "the assistant" as variety. One name each.

## What to avoid

- No hype and no doom. The speedup is a real number a provider chooses. Show it
  and let it carry itself. No "revolutionary", "transformative", "game-changing"
  (the press bans these outright); no grand word before the argument earns it.
- Do not say speculative decoding "changes what the model says". It does not, and
  the whole lesson turns on that. State the guarantee plainly and cite the paper
  that proves it.
- Do not re-teach the neighbors. Prefill, first-token latency, why outputs vary
  under sampling: link the lesson in plain prose at first use, never as a
  numbered source, and move on.
- Skip the slop edges. No empty closer that grades the lesson, no "X is not Y, it
  is Z" unless a named misconception earns it, no "the catch is" punchline. The
  takeaway bookend lands the judgment; the body just teaches.
- Punctuation stays plain. Two thoughts are two sentences. Keep em-dashes to a
  couple at most across the piece; a period almost always wants the slot.
- Numbers get their real figure and a range the source supports (2x–3x, not
  "much faster"), and every one is tied to the source that measured it.

## The worked example is the spine

The reader should meet an actual short run: a handful of proposed tokens, most
accepted, one rejected, then the pause. Put it in a small table and walk it once.
Abstract claims about acceptance rates only land after the reader has watched one
run play out.
