# Draft handoff: the-mechanics/why-replies-stop (writer 01)

## Original work
This lesson converts a scatter of per-vendor token facts and per-API stop codes
into a single sight test: it teaches the reader to read the shape of a reply's
ending, a whole thought versus a word snapped in half, as the fingerprint of
which of two actors, the model or the program running it, stopped the reply.
The synthesis is visible in the closing "the-tell" section and the takeaway; the
evidence record holds the mechanisms and codes separately but never joins them
into a giveaway the reader can apply without reading an API field.

## Proof result
`./nb check ... --series the-mechanics --library /home/user/library-checkout`
(with links): BLOCK: 0, WARN: 0, verdict PUBLISHABLE. Stamped words=1818,
reading_minutes=8, sources=9 (8 primary, 1 secondary; policy min 8 / primary >=4
/ secondary >=1 met). No warning left standing.

## Precision points honored
- Base models are not said to "never stop": the piece states they emit a
  document-end token (`<|end_of_text|>` / `<|endoftext|>`) at a document
  boundary, and that post-training adds the end-of-*turn* behavior. The evidence
  record's one thin spot (no primary measures a base model "rambling" with
  numbers) is sidestepped by stating only the token-role claim the primaries
  support, so nothing rests on the unmeasured wrinkle.
- The stop-probability micro-example is labeled illustrative in its caption and
  in the prose; the ~0% -> ~3% -> ~92% shape is not attributed to any named
  model as measured, and the checkable HF `compute_transition_scores` method is
  cited as the substrate.
- The two causes (sampled stop token vs length cap) are the main case; one
  clause notes the Anthropic field also reports refusal, tool use, and a filled
  context window.
- Only the verified Anthropic wording is quoted verbatim for the cap ("the
  maximum number of tokens to generate before stopping"). Gemini's
  `finishReason` values are named as code tokens (`MAX_TOKENS` / `STOP`), not
  quoted as prose, so no un-reverified Gemini wording is printed.
- `<code>` is used only for literal strings a reader would match
  character-for-character (token strings, API field names and values, the id
  `128009`), not for ordinary terms.
- autoregressive-generation and sampling-temperature are linked as plain prose
  links (and as Background rows), not re-taught and not numbered sources. No
  code anywhere.

## Furniture
One illustrative probability table (the rising end-of-turn token probability)
and one "In plain language" note (the base-vs-turn stopping distinction). The
banned "watch a product appear one line at a time" table framing and the recent
declarative heading cadence were deliberately avoided; headings are named from
this piece's own descent.

## Open questions
None blocking. No source asset was captured: the two candidate assets (Llama
chat-prompt block, Anthropic stop_reason list) are gated to automated clients or
add nothing the prose and table do not already carry, and the evidence found no
base-model-rambling asset. The argument spends everything it would have shown.
