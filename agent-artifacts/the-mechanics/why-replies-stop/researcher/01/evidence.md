# Evidence record: the-mechanics/why-replies-stop (researcher 01)

The evidence firmly supports every load-bearing claim in the commission. A reply
ends for one of two mechanically distinct reasons, and both are documented in
primaries. (1) The model can emit a special end-of-sequence / end-of-turn token
that is a real entry in the vocabulary, sampled at each step like any other
token; when it is chosen, generation halts. Meta's own Llama 3 documentation
names that token (`<|eot_id|>`) and its role, and torchtune's tokenizer gives its
exact integer id (128009), so "the model put probability on the stop token" is
literally "the model put probability on vocabulary index 128009." The Anthropic
Messages API reports this as `stop_reason: "end_turn"`. (2) The serving layer
imposes a length cap (`max_tokens` / `max_new_tokens`); when the count is hit the
text is truncated regardless of whether the stop token came, which the Anthropic
API reports as `stop_reason: "max_tokens"` and Google's Gemini API as
`finishReason: MAX_TOKENS`. Caller-supplied stop sequences are a third,
caller-driven halt.

That end-of-turn stopping is *learned in post-training* is well supported but must
be stated precisely, and this is the record's one real subtlety. Base (pretrained)
models are not incapable of ever ending: they emit an end-of-*document* token
(`<|end_of_text|>` / `<|endoftext|>`) at document boundaries. What they lack is
the end-of-*turn* behavior at a helpful answer's boundary, which is introduced by
the chat template and instruction/chat fine-tuning. Meta states outright that
`<|end_of_text|>` "is generated only by the base models," and the InstructGPT
paper establishes the broader point that helpful, intent-following behavior is
added by fine-tuning, not by the base model or scale. The thin spot: I found no
single primary that measures a base model "rambling past a sensible answer
boundary" with numbers; that wrinkle rests on the token-role documentation
(base emits document-end, instruct emits turn-end) plus InstructGPT's alignment
finding, which is a sound but slightly indirect chain. The concrete stop-token
probability example is a defensible worked illustration built on Hugging Face's
real, documented probability-readout method, not a captured measurement of one
specific model's EOS curve (see Worked micro-example).

## Sources

```text
URL:         https://platform.claude.com/docs/en/api/messages
Kind:        primary. Anthropic authors and owns the documented behavior of its
             own Messages API; the stop_reason values are a fact about the API.
Establishes: The API's response reports why generation stopped, distinguishing a
             natural end from a length-cap truncation and from a caller stop
             string. Firsthand for the serving-layer reporting of both mechanisms.
Paraphrase:  stop_reason is "the reason that we stopped." Documented values include
             end_turn (natural stopping point), max_tokens (requested max_tokens or
             the model's maximum exceeded), stop_sequence (a caller-supplied
             sequence was generated), plus tool_use, pause_turn, refusal, and
             model_context_window_exceeded. max_tokens is "the maximum number of
             tokens to generate before stopping," and the models may stop before
             reaching it. stop_sequences let the caller force a halt on custom
             strings, which yields stop_reason "stop_sequence."
Locators:    Response fields -> stop_reason; Request fields -> max_tokens,
             stop_sequences.
Quote:       stop_reason values: "end_turn": the model reached a natural stopping
             point; "max_tokens": we exceeded the requested max_tokens or the
             model's maximum; "stop_sequence": one of your provided custom
             stop_sequences was generated. max_tokens: "The maximum number of
             tokens to generate before stopping. Note that our models may stop
             before reaching this maximum." stop_sequences: "Our models will
             normally stop when they have naturally completed their turn, which
             will result in a response stop_reason of 'end_turn'."
```

```text
URL:         https://huggingface.co/docs/transformers/en/main_classes/text_generation
Kind:        primary. The transformers library implements the decoding loop; its
             maintainers' reference documents the actual stopping behavior of the
             generate() method used to serve open models.
Establishes: Firsthand that (a) generation halts when the eos_token_id is produced;
             (b) a length cap (max_new_tokens / max_length) bounds output; (c) the
             stop token is an ordinary vocabulary entry whose probability can be
             read and even forced or suppressed; (d) per-step token probabilities
             are recoverable, which is the checkable substrate for the micro-example.
Paraphrase:  The returned sequence length is "either equal to max_length or shorter
             if all batches finished early due to the eos_token_id" - i.e. sampling
             the EOS token ends generation early. eos_token_id is "the id of the
             end-of-sequence token" (optionally a list of several). max_new_tokens
             is "the maximum numbers of tokens to generate." suppress_tokens sets a
             token's "log probs to -inf so that they are not sampled," and
             min_new_tokens plus forced_eos_token_id ("the token to force as the
             last generated token when max_length is reached") show EOS is an
             ordinary, manipulable token, not a hard-wired rule. The
             compute_transition_scores example prints real per-token probabilities
             for GPT-2, demonstrating that every step yields a probability over the
             whole vocabulary that any token's (including EOS's) can be read from.
Locators:    GenerationConfig -> length params (max_new_tokens, min_new_tokens,
             forced_eos_token_id), logits params (suppress_tokens), special tokens
             (eos_token_id); return value note on sequences; compute_transition_scores
             worked example.
Quote:       "shorter if all batches finished early due to the eos_token_id";
             suppress_tokens "will set their log probs to -inf so that they are not
             sampled"; real readout row "| 262 | the | -1.414 | 24.33%".
```

```text
URL:         https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/prompt_format.md
Kind:        primary. Meta's own model repository; the authoritative definition of
             Llama 3's special tokens and chat format. (The blob page above is the
             reader-facing source and is public: its raw mirror,
             raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/prompt_format.md,
             returns 200; the github.com HTML page is gated to automated clients with
             a 403 - gated, not dead - and resolves normally in a browser.)
Establishes: Firsthand that the vocabulary contains a dedicated end-of-turn token
             the instruction-tuned model emits to signal it is done, and - crucially
             for Step 2 - that a *different* end token belongs to the base model.
             This is the primary that shows end-of-turn stopping is an instruct-model
             (post-training) feature.
Paraphrase:  <|eot_id|> "represents when the model has determined that it has
             finished interacting with the user message" and terminates a normal
             turn. <|end_of_text|> causes the model to cease generating and "is
             generated only by the base models." The chat format wraps each turn as
             <|start_header_id|>role<|end_header_id|> ... <|eot_id|>, and an
             assistant reply ends by emitting <|eot_id|>.
Locators:    Special tokens list; chat prompt structure.
Quote:       <|end_of_text|>: "Model will cease to generate more tokens. This token
             is generated only by the base models." <|eot_id|>: "Represents when the
             model has determined that it has finished interacting with the user
             message."
```

```text
URL:         https://huggingface.co/docs/transformers/en/chat_templating
Kind:        primary. Maintainers' reference for how chat models are formatted and
             trained; owns the claim about where end-of-turn tokens come from.
Establishes: Firsthand that a chat model is a base LM fine-tuned on message-formatted
             data with control tokens, that the format is learned (not deduced), and
             that these tokens are what let the model see - and produce - turn
             boundaries. Directly supports Step 2 (learned in post-training) and the
             Step 1 framing that stopping is still just next-token continuation.
Paraphrase:  "All causal LMs, whether chat-trained or not, continue a sequence of
             tokens." Base models are "then often 'fine-tuned' for chat, which means
             training them on data that is formatted as a sequence of messages,"
             often with control tokens like <|end_of_message|>. Different models use
             different control tokens even when fine-tuned from the same base, and
             "with the wrong control tokens, these models would have drastically
             worse performance." The chat is "still just a sequence of tokens."
Locators:    Intro ("critical insight"); Mistral vs Zephyr comparison; Model
             training section.
Quote:       "These base models are then often 'fine-tuned' for chat, which means
             training them on data that is formatted as a sequence of messages."
             "with the wrong control tokens, these models would have drastically
             worse performance."
```

```text
URL:         https://qwen.readthedocs.io/en/latest/getting_started/concepts.html
Kind:        primary. The Qwen team's documentation of its own tokens; a second,
             independent model family confirming the base-vs-chat token split.
Establishes: Firsthand that in the chat format the end-of-turn token (<|im_end|>) is
             set as the model's eos so generation stops at a turn boundary, while the
             base model uses a separate document-boundary token (<|endoftext|>). This
             corroborates Meta and generalizes the mechanism beyond one vendor.
Paraphrase:  <|im_end|> marks the "end of each turn, which is appended to each turn,"
             and in chat inference the eos token is set to <|im_end|> so it halts
             generation. <|endoftext|> is a pre-training token "inserted between
             documents inside a packed training sequence" - a document boundary, not
             a turn boundary.
Locators:    Control tokens / chat template concepts; token table.
Quote:       <|im_end|>: "end of each turn, which is appended to each turn."
             <|endoftext|>: "inserted between documents inside a packed training
             sequence."
```

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary. Ouyang et al. (OpenAI), "Training language models to follow
             instructions with human feedback." Owns the finding that base-model
             helpfulness is added by fine-tuning.
Establishes: Firsthand support for the honest wrinkle in Step 2: a pretrained LM does
             not, by default, behave like a helpful assistant; intent-following
             behavior is produced by post-training, not by the base model or by
             scale. End-of-turn stopping at a sensible answer boundary is one instance
             of this learned helpful behavior.
Paraphrase:  Making language models bigger does not by itself make them follow a
             user's intent; base LLMs can produce output that is untruthful, toxic,
             or unhelpful and are "not aligned with their users"; fine-tuning with
             human feedback (supervised fine-tuning plus RLHF) aligns them to user
             intent, and a much smaller aligned model is preferred over the far
             larger base GPT-3.
Locators:    Abstract.
Quote:       "Making language models bigger does not inherently make them better at
             following a user's intent." "these models are not aligned with their
             users."
```

```text
URL:         https://meta-pytorch.org/torchtune/0.2/_modules/torchtune/models/llama3/_tokenizer.html
Kind:        primary. torchtune (Meta/PyTorch) source code; the authoritative integer
             id assignment for Llama 3's special tokens.
Establishes: Firsthand that the end-of-turn token is a concrete vocabulary index, so
             "putting probability on the stop token" is putting probability on a
             specific id. Makes the Step 1 micro-example concrete and checkable.
Paraphrase:  Llama 3's special-token map assigns <|begin_of_text|> = 128000,
             <|end_of_text|> = 128001, <|eot_id|> = 128009, <|start_header_id|> =
             128006, <|end_header_id|> = 128007. The end-of-turn token an assistant
             reply emits is vocabulary id 128009.
Locators:    LLAMA3_SPECIAL_TOKENS dictionary.
Quote:       "<|eot_id|>": 128009 (also "<|end_of_text|>": 128001,
             "<|begin_of_text|>": 128000).
```

```text
URL:         https://ai.google.dev/api/generate-content
Kind:        primary. Google's Gemini API reference; owns its own API's reported
             finish reasons and length controls. Cross-vendor confirmation of the
             serving cap.
Establishes: Firsthand that a second major API also distinguishes a natural stop
             from a length-cap truncation and exposes a caller stop-sequence control,
             corroborating Anthropic on Step 3.
Paraphrase:  A generateContent response carries a finishReason whose values include
             STOP (a natural / stop-sequence end) and MAX_TOKENS (the output-token
             limit was reached). generationConfig.maxOutputTokens caps response
             length, and stopSequences (e.g. ["x"]) halt generation when produced.
Locators:    generationConfig (maxOutputTokens, stopSequences); Candidate.finishReason
             enum (STOP, MAX_TOKENS).
Quote:       maxOutputTokens and stopSequences confirmed verbatim from the config
             section (example "stopSequences": ["x"]). See Contradictions for a
             caveat on the exact finishReason STOP/MAX_TOKENS wording.
```

```text
URL:         https://www.natebrake.com/blog/end-of-sequence-explained
Kind:        secondary. An engineer's explainer, reporting on the EOS mechanism from
             outside the authoring party of any model or API.
Establishes: Repeats, in plain terms, that emitting the EOS token is the signal that
             ends generation. Supports that the claim is commonly held; not itself
             proof of any model's behavior.
Paraphrase:  The end-of-sequence token signals the sequence is complete; producing it
             tells the generation loop to stop emitting further tokens.
Locators:    Body.
Quote:       "Producing the EOS token tells the generation algorithm to stop
             generating additional text."
```

## Worked micro-example (stop-token probability rising)

The commission asks for a concrete, checkable micro-example of the stop token's
probability rising as an answer completes. The checkable *method* is real and
documented; the specific numbers below are a labeled illustration, not a captured
measurement.

Real, checkable substrate (Hugging Face transformers docs, source 2): at every
generation step the model outputs a score over the entire vocabulary, and
`compute_transition_scores` with `output_scores=True` prints the probability of
each chosen token. The documentation's own GPT-2 run shows exactly this readout,
e.g. the token "the" at 24.33% and "day" at 7.36% at successive steps. To watch a
stop token specifically, one reads the probability assigned to the eos / end-of-turn
id (for a Llama 3 Instruct model, id 128009, source 7) at each step rather than the
chosen token.

Illustrative trajectory (fabricated numbers, plausible shape). Prompt: "What is the
capital of France?" Target completion: "The capital of France is Paris." Probability
the model assigns to the end-of-turn token at each position:

- after "The" -> ~0.0%   (answer not started)
- after "France is" -> ~0.1%  (a word must follow)
- after "Paris" -> ~3%   (a period could still come)
- after "Paris." -> ~92%  (nothing sensible remains to add)

At the last step the end-of-turn token is the most probable next token, so sampling
selects it and generation halts with a natural finish (Anthropic `end_turn`). The
same distribution, if the token cap is reached one step earlier, is simply never
consulted: the loop stops at the count and the text is truncated (`max_tokens`).
Two documented levers confirm the token is ordinary and probabilistic, not a rule:
setting `min_new_tokens` / `suppress_tokens` drives the EOS probability to -inf so
the model cannot stop yet, and `forced_eos_token_id` forces it at the cap (source 2).
Anyone can replace the illustrative numbers with a real run using the documented
method above.

## Contradictions

- Base models are not simply "unable to stop." Meta and Qwen both show the base
  model *does* emit an end token - the document-boundary token (<|end_of_text|> /
  <|endoftext|>). The precise claim is that base models lack the end-of-*turn*
  behavior at a helpful-answer boundary; in chat-style use they continue past where
  a reply should end because they are continuing a *document*, not closing a *turn*.
  Writing "base models never stop" would overstate it. This refines Step 2 rather
  than contradicting it, but the article must state it precisely.

- The "two causes" framing (sampled stop token vs length cap) is the main case, not
  the whole enumeration. Anthropic's own stop_reason list includes refusal,
  model_context_window_exceeded, tool_use, and pause_turn. A reply can also end
  because a safety classifier intervened or the context window filled. The lesson
  should own the stopping mechanic for the two named causes while acknowledging
  these others exist, to stay accurate.

- Popular-explanation blur (flagged in the brief, confirmed against primaries):
  "the model decided to stop" (it sampled end_turn / <|eot_id|>) and "it ran out of
  room" (max_tokens / MAX_TOKENS truncation) are mechanically different events that
  Anthropic and Gemini report with different codes. The clean giveaway a reader can
  use: a natural finish ends on a sentence/structure boundary and the API reports
  end_turn/STOP; a truncation can stop mid-word or mid-code-block and reports
  max_tokens/MAX_TOKENS. Explanations that say "the model just stopped" without
  naming which one erase this distinction.

- Wording caveat, not a substantive conflict: the Gemini reference page was
  truncated on fetch and the automated read paraphrased the finishReason STOP and
  MAX_TOKENS descriptions. The *existence* of STOP and MAX_TOKENS values and of
  maxOutputTokens / stopSequences is reliable; the exact one-line gloss for STOP and
  MAX_TOKENS should be re-read on the live page before being quoted verbatim. The
  Anthropic wording (source 1) is verified and can carry any exact-quote need for
  Step 3.

## Numbers

```text
Figure: <|eot_id|> = token id 128009 (Llama 3 / 3.1 end-of-turn token)
Owner:  torchtune LLAMA3_SPECIAL_TOKENS map (source 7); id also used as eos for
        Llama 3.x Instruct models.
Scope:  Llama 3 vocabulary; base vocab 128000 tokens, special tokens 128000+.
```

```text
Figure: <|end_of_text|> = token id 128001; <|begin_of_text|> = 128000
Owner:  torchtune LLAMA3_SPECIAL_TOKENS map (source 7).
Scope:  Llama 3 vocabulary. <|end_of_text|> is emitted "only by the base models."
```

```text
Figure: Real per-token probabilities in the transformers doc example: "the" 24.33%,
        "day" 7.36%, "when" 13.40%, "we" 15.58%, "can" 8.14%
Owner:  Hugging Face transformers generation docs, compute_transition_scores
        example on GPT-2 (source 2).
Scope:  One GPT-2 greedy run from prompt "Today is"; illustrates that each step
        yields a readable probability per vocabulary token (the substrate for
        reading a stop token's probability). Not EOS-specific.
```

```text
Figure: Illustrative end-of-turn probability trajectory ~0% -> ~3% -> ~92%
Owner:  None - fabricated illustration (see Worked micro-example), shape only.
Scope:  Labeled as illustrative; must not be presented as measured.
```

## Source assets

```text
Asset: Llama 3 chat prompt structure block in prompt_format.md (source 3), showing
       <|start_header_id|>assistant<|end_header_id|> ... <|eot_id|> around a turn.
Shows: Where the end-of-turn token sits in a real formatted conversation - the exact
       token an assistant reply emits to finish. Concrete anchor for Step 1/2.
Crop:  Retain the assistant turn and its trailing <|eot_id|>; the system/user turns
       can be trimmed. Keep tokens verbatim; do not paraphrase into prose.
```

```text
Asset: The compute_transition_scores readout table in the transformers docs
       (source 2): token | string | log prob | probability.
Shows: That generation is a sequence of probability distributions over the vocabulary
       and any token's probability is directly readable - the honest basis for the
       stop-token micro-example.
Crop:  Retain the header and a few rows with the percentage column; omit the
       surrounding beam-search example to avoid confusion.
```

```text
Asset: Anthropic stop_reason value list (source 1).
Shows: The API's own vocabulary for why a reply ended - end_turn vs max_tokens vs
       stop_sequence - the cleanest evidence that the two mechanisms are reported
       distinctly.
Crop:  Keep end_turn, max_tokens, stop_sequence; the others (tool_use, pause_turn,
       refusal, model_context_window_exceeded) are worth showing once to support the
       Contradictions note that the two-cause story is the main case, not all cases.
```

```text
Asset: None found for a base-model-rambling demonstration - no primary with a
       captured "base model fails to stop" transcript was located. If the writer
       wants one, it would need a fresh run, not a cited image.
Shows: -
Crop:  -
```

## Discarded

```text
URL: https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/meta-llama-3/ - 403 Forbidden on fetch; superseded by the meta-llama/llama-models repo (source 3), which carries the same token definitions from Meta and does resolve.
```

```text
URL: https://www.llama.com/docs/model-cards-and-prompt-formats/meta-llama-3/ - returns only a page title with no body text through the fetch tool; unusable for exact quotes though the content matches source 3.
```

```text
URL: https://platform.openai.com/docs/api-reference/chat/object - 403 Forbidden; the platform.openai.com reference is JS-gated to the fetch tool. OpenAI's guide page redirects to developers.openai.com/api/docs/guides/text, which does not surface finish_reason stop/length wording. Serving-cap cross-vendor need is met by Gemini (source 8) alongside Anthropic (source 1).
```

```text
URL: https://developers.openai.com/api/docs/guides/text - resolves, but does not document finish_reason values or max_tokens semantics in the returned content; nothing citable for this piece.
```
</content>
</invoke>
