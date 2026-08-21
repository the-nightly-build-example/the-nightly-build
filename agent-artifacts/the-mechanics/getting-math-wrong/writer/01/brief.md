# writer brief: the-mechanics/getting-math-wrong (01)

Inputs:
- Editorial direction: ../../editorial-direction.md — house standard, paper voice, series prompt.
- Voice guide: ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages.
- Evidence record: ../../researcher/01/evidence.md — your complete claim set (add no facts it lacks).
- The initialized article: ../../../../library/the-mechanics/getting-math-wrong.html (edit; do not recreate the skeleton).
- Template context: ../../../../.nb-context/ — effective contract, furniture catalogs, runtime assets.

Output: ./draft-handoff.md (writer/01/draft-handoff.md)

Proof: run from repo root /home/user/the-nightly-build —
`./nb check .nb-work/the-mechanics/getting-math-wrong/library/the-mechanics/getting-math-wrong.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/b1bf3c94-3553-5519-8a12-b9ebb7eba930/scratchpad/library-checkout`
New slug; no `--revision`. Use `--no-check-links` while iterating; run it links-on until `BLOCK: 0`.

## Recent patterns to break (the-mechanics tics)

- Dek: avoid mechanism-as-subject + because/comma cause resolving on a flat
  limiting declarative ("is all the generator ever does").
- Headings: avoid imperative/second-person headings ("Ask for ten words, get a
  hundred"); subject-dropped past-participle headings ("Trained to run long...");
  and RETIRE the stock heading "What's settled, and what's still open." Mark
  settled vs open IN THE PROSE, not under a stock heading, and not by leaning on
  the word "unsettled."
- Opener: a concrete everyday demonstration is welcome, but avoid the exact
  second-person "Ask a model to..." frame.
- Closer: avoid the terse "The next time..." reframing kicker.
- Diction: avoid "one token at a time," "settled/unsettled/open" as a refrain,
  "honest" as a virtue word, "a weaker signal than it looks."
- Cross-series: no "By the end you will be able to..."; no "The next time..., ask"
  numbered-questions close.

## Decisions the inputs may not settle (from the researcher's report)

- **Scope the whole lesson to the raw, no-tool, no-scratchpad path.** Modern
  reasoning models and tool-wrapped products increasingly get large arithmetic
  right — but via the step-3 fixes (built-in chain-of-thought, code execution),
  NOT a new arithmetic unit. Say this so the piece is not falsified by a reader
  who watches a current product multiply correctly. The behavior you explain is
  the naked model with no scratchpad and no calculator.
- **Scope the tokenization cause.** "Numbers arrive in chunks, not clean digits"
  holds for OpenAI-style tokenizers (tiktoken caps digit runs at three, in both
  cl100k_base and o200k_base) but NOT single-digit-tokenizer models (Llama,
  Mistral, Gemma, PaLM). State the scope; do not claim it universally.
- **Keep step 4 (how the model implements addition) open.** The real-model
  interpretability is thin: two-digit operands on mid-size open models, and two
  studies disagree on framing (a trigonometric "Clock"/helix representation vs an
  unordered "bag of heuristics"). The fully reverse-engineered clean circuit is a
  modular-addition TOY (Nanda), not a chatbot doing multiplication — say so; do
  not present the toy as the explanation of real multiplication.
- **Worked anchor available:** 57,897 × 12,832 = 742,934,304 (true value, already
  recomputed). Accuracy-vs-digits: Faith and Fate (Dziri) reports GPT-4 zero-shot
  multiplication accuracy around 59%, 4%, and ~0% at 3-, 4-, and 5-digit. Use the
  evidence record's exact figures and scopes.
- Differentiate sharply from the published `the-mechanics/letter-counting`
  (characters hidden inside a token) — link it, do not repeat it. Link
  `the-mechanics/thinking-out-loud` and `.../tool-use` for the fixes.
