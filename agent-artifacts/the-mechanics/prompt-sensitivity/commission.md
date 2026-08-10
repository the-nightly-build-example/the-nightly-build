# Commission: the-mechanics/prompt-sensitivity

## The behavior
Ask a model the same thing two ways, or reformat a prompt that worked, and the answer changes or gets
worse: reorder the few-shot examples, swap a colon for a newline, capitalize differently, and the score
moves. This is the behavior anyone who has tried to get good output has seen, and this lesson works
backward to what produces it.

## Why this behavior, tonight
The reader has learned that a model turns words into vectors (the-mechanics/word-embeddings) and learns
from examples in the prompt (the-mechanics/in-context-learning). The missing piece is that the model
conditions on the exact tokens it is given, with no separate representation of "what the prompt means"
held apart from its surface form, so semantically equal prompts are not equal inputs. This lesson names
that mechanism and sets up later lessons on prompting.

## The chain to work backward (name a real part at each step, ground the example)
1. The behavior: the same request, reworded or reformatted, gives a different or worse answer, and the
   few-shot example order changes the result. Ground it in a measured case (a formatting change or an
   ordering change that moves accuracy a lot).
2. The model's input is the literal token sequence. There is no canonical meaning extracted and stored
   apart from the surface form; the model computes from the tokens themselves.
3. So a small surface change is a different point in the model's input space, and the output
   distribution shifts with it. Few-shot example order matters for the same reason: the sequence is part
   of the input.
4. This is measured, not folklore: reported spreads across trivially different formats are large, and no
   one can predict the best format in advance.
5. Ground: below the token-level conditioning and the model's learned sensitivities, nothing changes the
   answer. Mark settled versus open: that models are format- and order-sensitive is settled and measured;
   why a particular format helps, and whether the effect shrinks with scale or instruction-tuning, is
   open. No code: show format variants as inline data, never a runnable prompt harness.

## Template, form, and a hard constraint
Lesson template, body first, both bookends last. The-mechanics prompt says: No code.

## Reader and what to teach
Declared reader: smart, widely read, no codebase time. Assume algebra and probability. Link, do not
re-teach, word-embeddings and in-context-learning. Teach here, each once: that the model conditions on
the exact token sequence with no separate meaning representation; format sensitivity (trivial surface
changes move the output); order sensitivity of few-shot examples; why "semantically equivalent" prompts
are not equivalent inputs.

## Sources
Series policy: min 8 sources, primary >= 4, secondary >= 1. Primary the researcher must open: the format-
sensitivity paper (Sclar et al. 2023, "Quantifying Language Models' Sensitivity to Spurious Features in
Prompt Design" / FormatSpread); the few-shot ordering paper (Lu et al. 2022, "Fantastically Ordered
Prompts and Where to Find Them"); at least two more primaries measuring prompt/format/order sensitivity or
its interaction with scale and instruction-tuning. Secondary (a rigorous explainer) only for context.

## Production record
Harness: claude-code-routine. Model for every role: Claude Opus 4.8 ("capable" tier; no role carries a
`required` directive). Efforts follow policy: writing-coach low, researcher high, writer medium, editor high.
Recommended nb-meta tags: prompting, robustness, in-context-learning.

## Recent habits not to inherit
From the recent the-mechanics and house record, break these:
- Mechanics headline molds "can't tell X from Y" (word-order) and the "like any other token/word" tag
  (why-replies-stop), and the "A chatbot does X without Y" shape (retrieval, reading-images). Find this
  behavior's own surprise.
- The opener that quotes a tiny example, states the twist, then previews "First... Then... And last..."
  (word-order). State stakes without the enumerated tour.
- The takeaway that opens on the restated one-liner. Resolve what the opener set up.

## This round's focus
Keep strictly to the causal chain, marking settled versus open at each step. Ground the behavior in a
measured spread (formatting or ordering), not an anecdote, and keep "the model is genuinely worse" distinct
from "the surface form moved the score." No code.
