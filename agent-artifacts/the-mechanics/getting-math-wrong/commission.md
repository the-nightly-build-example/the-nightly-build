# Commission: the-mechanics/getting-math-wrong

## Authorized work

Scheduled duty for 2026-08-21 returned `the-mechanics` as an open section. One of
five articles commissioned tonight, one per due series. Process this article only.
Slug verified new against the full published library (30 the-mechanics slugs).

## The behavior and the angle

The desk answers "how does it actually do that." The behavior: ask a chatbot to
multiply two large numbers (or add several multi-digit numbers) and it returns a
confident, wrong answer that looks about right. The lesson works backward from
that to what produces it, marking which steps are settled and which are open. No
code.

The chain to build (the writer orders and grounds it; this is the intended
spine):

1. A model does not compute; it predicts text. There is no arithmetic unit
   inside it. It produces the most probable next token given what it has seen,
   which for common, small sums is often the right digit and for large, rare ones
   is a plausible wrong one.
2. Numbers are tokenized in chunks, not clean digits, so the model does not
   receive place value the way a person reading the number does. (Differentiate
   from the published `the-mechanics/letter-counting`: that lesson is about not
   seeing the characters inside a token; this is about computing over numbers,
   a distinct failure with its own cause. Link it, do not repeat it.)
3. Generation runs left to right with no scratchpad, so a carry that a person
   would resolve by working right to left has nowhere to live. Writing the steps
   out (chain-of-thought) or calling a calculator (tool use) is what fixes it —
   link `the-mechanics/thinking-out-loud` and `the-mechanics/tool-use`.
4. What interpretability has found: models implement approximate, heuristic
   representations of number (not a carrying algorithm), and accuracy falls as
   digit count grows. Mark as settled: there is no exact arithmetic circuit and
   accuracy degrades with size; mark as open: exactly how models represent and
   combine numbers.

Ground the whole thing in one concrete, real failed calculation with the true
answer beside it. Keep the teaching to what the chain needs.

## Boundaries

- Slug new. Differentiate sharply from `the-mechanics/letter-counting`
  (characters hidden inside a token) and do not re-teach next-token prediction
  from zero if it can be introduced compactly. Link, don't rebuild:
  `the-mechanics/thinking-out-loud`, `.../tool-use`, `.../letter-counting`,
  `.../multilingual-gap` (tokenization).
- Tonight's neighbors (other series): the-evidence/direct-preference-optimization,
  the-instruments/big-bench-hard, what-could-go-wrong/unilateralists-curse,
  when-ai-breaks/arup-deepfake-fraud.

## Sources

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Leads:

- **Primary — a study of LLM arithmetic accuracy vs digit length**, showing
  accuracy falling as digits grow (e.g. work on integer multiplication/addition
  in transformers).
- **Primary — a tokenization source** on how multi-digit numbers are split (the
  tokenizer's number handling; the shift to single-digit tokenization in some
  newer models), owning the "no clean place value" claim.
- **Primary — interpretability of arithmetic in transformers**, e.g. the
  addition-circuit / Fourier-feature work (Nanda et al. on modular addition;
  Zhong et al. "clock and pizza"; or a 2024-2025 paper on how a model does
  addition), for what the model actually implements. Distinguish modular-toy
  results from real multi-digit arithmetic honestly.
- **Primary — a source showing scratchpad / chain-of-thought or a tool fixes it**
  (e.g. PAL / Program-Aided Language models, Gao et al. 2022, or a scratchpad
  arithmetic paper).
- **Secondary — reporting** on the "AI can't do math" phenomenon for the worked
  case.

Search for what breaks the angle: if newer models have largely solved multi-digit
arithmetic (single-digit tokenization, tool routing), record that and scope the
claim to where it still holds. Record contradictions.

## Furniture and charts

Lesson template. A chart earns its place if a trend is the point (accuracy vs
digit count) and the evidence supplies the verified series. Do not force one.
No Verdict block. No code (series rule).

## Production policy (from `nb production-policy`)

Profile `balanced`. writing-coach low, researcher high, writer medium, editor
high; model capable; none required. nb-meta `harness` "Claude Code", `model`
"capable". Runtime note as in the-evidence commission.

## Tags (writer to confirm)

arithmetic, tokenization, reasoning, tool-use, generation

## Recent patterns to break (five most recent the-mechanics pieces)

- Dek: avoid mechanism-as-subject + because/comma cause resolving on a flat
  limiting declarative ("can't take a word back," "is all the generator ever
  does").
- Headings: avoid imperative/second-person headings ("Ask for ten words, get a
  hundred," "You did not ask for a list"); subject-dropped past-participle
  headings ("Trained to run long..."); and above all RETIRE the stock heading
  "What's settled, and what's still open." Mark settled vs open IN THE PROSE, not
  under a stock heading, and not by leaning on the word "unsettled."
- Opener: a concrete everyday demonstration is welcome, but avoid the exact
  second-person "Ask a model to..." frame.
- Closer: avoid the terse "The next time..." reframing kicker.
- Diction to avoid: "one token at a time," "settled/unsettled/open" as a refrain,
  "honest" as a virtue word, "a weaker/shallower signal than it looks."
- Cross-series tics: no "By the end you will be able to..." promise; no "The next
  time..., ask..." numbered-questions close.
