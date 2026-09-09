# Voice guide: reading the ReAct paper

How this one lesson should sound. Short and usable. The house voice and the
lesson template already bind; this only says how to apply them to reading this
particular document.

## The register for this piece

Write like Matt Yglesias explaining something he understands well: plain claims,
concrete stakes, no fuss. The reader is smart, reads widely, and has never
touched a codebase. They have heard "AI agent" a hundred times and been told
"ReAct started it." Your job is to show them what the paper actually did, in
numbers they can check, so they can judge that claim themselves.

Teach, do not summarize. The reader should finish able to say what ReAct
proposed, what it scored, on what, and how far today's agent loops have moved
from it. Every paragraph earns its place by adding one checkable thing.

## Terms of art: define each on first use, in the same sentence

This paper sits on top of several ideas. Name each in plain words the first time
it appears, then keep the name fixed.

- The three moves ReAct interleaves: a **thought** (the model reasoning in
  words), an **action** (a command it emits, like a search), an **observation**
  (the text the environment sends back). Define them once, together, then reuse
  those exact three words everywhere.
- **Few-shot prompting**: showing the model a handful of worked examples in the
  prompt, without changing its weights. Contrast plainly with fine-tuning if you
  use that word.
- **Exact match** and **success rate**: say what each benchmark counts as a win
  before you quote a number against it.
- Chain-of-thought and tool-use are already taught. Link them (chain-of-thought
  in the-evidence, tool-use in the-mechanics) at first mention in prose. Do not
  re-teach either. This is a plain prose link, never a numbered source.

## What carries the lesson: the real numbers, honestly

The honest angle is that the paper credited with launching agents scored
unevenly, and on the very QA benchmark it is best known for its own
reasoning-and-search loop came in below plain chain-of-thought. State that with
the figures next to it (27.4 versus 29.4 exact match on HotpotQA), not as a
verdict the reader has to trust. Show where it clearly won (fact-checking, the
two interactive benchmarks, hallucination) with the same specificity. The paper
is neither a breakthrough nor a fraud, and the writing should let the numbers
set the weight.

Use one real worked trace (the paper's own Apple Remote HotpotQA example) so the
thought/action/observation loop is concrete before any number lands.

## What to avoid

- No hype, no doom. No "revolutionary", "transformative", "game-changing". A
  grand word appears only after the figure that earns it, and usually not then.
- Do not mirror this desk's tired headline mold. No "the paper credited with
  starting the X era never did Y". Find ReAct's own concrete surprise (the loss
  to chain-of-thought on its home benchmark) and state it straight.
- No negative parallelism as reflex ("not X but Y", "X rather than Y") unless a
  real, named misconception earns the contrast.
- Plainest punctuation. Two thoughts are two sentences. Keep em-dashes scarce.
- Do not let the abstract's headline gains ("34% and 10%") stand alone. They are
  the two interactive benchmarks only; the QA results are more mixed, and the
  lesson has to hold both at once.
- The body speaks to no one and never mentions the lesson. Only the two bookends
  address the reader.
