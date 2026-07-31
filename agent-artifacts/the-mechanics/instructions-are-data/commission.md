# Commission — the-mechanics / instructions-are-data

Date: 2026-07-31 (UTC) · Mode: open · Template: lesson · Section: Working Knowledge

## The behavior

Anyone who uses AI has seen it: a chatbot follows an instruction buried in a pasted
document, a webpage, or an email it was asked to summarize — sometimes an
instruction the user never intended it to obey. The mirror image is the "jailbreak,"
where added text talks the model out of its own rules, and the "system prompt" that
is supposed to set those rules in the first place. The Mechanics-desk question:
**how does the model decide what to obey, and why can text from a document override
what the user or the operator told it?**

## The angle

Work backward from the behavior to the ground truth, step by step, each step a real
part of the system, no code:

1. **The model sees one flat stream of tokens.** The operator's system prompt, the
   user's message, and any retrieved or pasted content are concatenated into a
   single sequence and fed to the model together. The "roles" (system / user /
   assistant) are marked by ordinary special tokens in a chat template (e.g. ChatML-
   style markers); those markers are themselves just tokens in the same stream, not
   a protected channel. Show a concrete assembled prompt so the reader sees the
   concatenation.
2. **There is no architectural boundary between instruction and data.** Attention
   (already taught) lets every token attend to every earlier token; nothing in the
   architecture stamps some tokens "trusted commands" and others "inert data." Being
   *later* in the stream or wearing a *system* marker gives text no enforced
   authority — only whatever statistical priority training gave it.
3. **Instruction-following is learned, not enforced.** A base model just continues
   text. The obedience users rely on comes from post-training (instruction tuning
   and RLHF — link `the-evidence/instructgpt`): the model was rewarded for treating
   certain spans as commands. That is a *tendency*, not a guarantee, so a
   sufficiently instruction-shaped span anywhere in the context can capture it. This
   is why **prompt injection** (Simon Willison named it, Sept 2022) and indirect
   injection through retrieved content (Greshake et al. 2023) work, and why, as of
   2026, there is no robust general fix.

Mark clearly which steps are **settled engineering** (flat token stream; no
privileged channel; obedience is a trained behavior) and which are **open**
(defending against injection; the reason no reliable instruction/data separation
exists yet is an active problem, not a solved one).

## Required contribution (the article's own work)

Reduce three phenomena users treat as separate — hidden system prompts, jailbreaks,
and prompt injection — to one mechanism: a single undifferentiated context in which
"which text is a command" is a learned statistical judgment, not an enforced
boundary. The reader should leave able to predict where a model can be steered by
text it was only meant to read, and to see why "just tell it to ignore instructions
in the document" cannot fully work.

## Source obligations

From `nb source-policy --series the-mechanics`: **min 8 sources; primary ≥ 4,
secondary ≥ 1.**

- **Primary:** a chat-template / special-token spec showing role markers are tokens
  (e.g. OpenAI ChatML documentation, or a HuggingFace chat-template / tokenizer
  doc, or Llama/Mistral prompt-format docs — read the actual format). InstructGPT
  (Ouyang et al. 2022, already in course) for "obedience is trained." Simon
  Willison's original prompt-injection posts (`simonwillison.net`, Sept 2022 and
  follow-ups — he is the primary source for the concept and term). Greshake et al.
  2023, "Not what you've signed up for: Compromising Real-World LLM-Integrated
  Applications with Indirect Prompt Injection" (arXiv 2302.12173) — primary research
  demonstrating indirect injection. OWASP Top 10 for LLM Applications, LLM01: Prompt
  Injection — an authoring body's own document.
- Strong additional primary: a frontier lab's own system card or safety doc
  acknowledging prompt injection is unsolved (Anthropic/OpenAI/Google). The
  "instruction hierarchy" paper (Wallace et al. 2024, OpenAI) is excellent primary
  material — it is the field's attempt to *add* priority, and its existence proves
  the default has none.
- Verify: who coined "prompt injection" and when; the exact claim of the
  instruction-hierarchy paper (a mitigation, not a guarantee); that the special
  tokens are tokens, not a channel. **Contradiction/steelman:** present the best
  current defenses (instruction hierarchy, delimiting, spotlighting, input
  filtering) and be honest that they reduce but do not eliminate the problem.

## Prior coverage in this library (link, do not re-teach)

- `the-mechanics/attention` (2026-07-18): every token attends to every other — the
  reason there is no isolated channel. Background link; do not re-derive.
- `the-mechanics/autoregressive-generation` (2026-07-25): the model's own output
  becomes ordinary input — the same "it's all one stream" fact, from the output
  side. Link and stay distinct (that lesson is about irreversibility; this one is
  about instruction vs. data).
- `the-mechanics/in-context-learning` (2026-07-22): the context steers behavior with
  frozen weights — the capacity injection exploits.
- `the-evidence/instructgpt` (2026-07-22): where obedience was trained in. Link for
  "instruction-following is learned."

## Structures NOT to repeat (recent habits)

Mechanics openers have often led with a crisp numeric surprise (a token-id triple,
"53.8% vs 56.1%"). This lesson is qualitative; do not manufacture a fake statistic
to match that shape. No colon-subtitle headline; no "X is not Y; it is Z" thesis;
vary heading cadence from the recent library.

## Neighboring articles tonight (make this distinct)

**Important cross-link:** `when-ai-breaks/gemini-image-generation` (tonight) is a
deployment failure that turned partly on a *hidden appended instruction*. This
Mechanics lesson owns the general mechanism; that piece owns the specific incident
and the bias-mitigation tradeoff. Do **not** dwell on the Gemini case here — one
sentence at most, if any. Keep this lesson architectural and incident-agnostic.
Because both publish tonight, do **not** put an internal Background link to the
Gemini article (it may not be merged yet); link only already-published lessons.

## Output paths

- Article: `.nb-work/the-mechanics/instructions-are-data/library/the-mechanics/instructions-are-data.html`
- Role artifacts under `agent-artifacts/the-mechanics/instructions-are-data/{writing-coach,researcher,writer,editor}/NN/`

## Harness / model

harness `claude-code-routine`; writer `claude-sonnet-5` effort medium; researcher &
editor `claude-sonnet-5` effort high; coach `claude-sonnet-5` effort low.

## Bans to watch

em-dash ≤ 4; `leverage` ≤ 1; `load-bearing` 0; `machinery` 0 (name the actual
component); `revolutionary`/`transformative`/`game-changing` 0; "AI race" 0. "No
code" is a series rule — an assembled example prompt as illustrative text is fine,
but no scripts in the article.
