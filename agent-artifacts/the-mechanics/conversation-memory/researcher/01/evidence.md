# Evidence: the-mechanics/conversation-memory (01)

The evidence supports the commission's chain cleanly and from parties that own each
claim. Two API owners state in their own reference docs that a chat request is
stateless and that the application must resend the entire prior transcript every
turn (Anthropic Messages API; OpenAI conversation-state guide and Chat Completions
reference). The within-request nature of the key/value cache is grounded in the
systems literature that owns KV-cache serving (the PagedAttention/vLLM paper) and
corroborated by an independent implementation reference (Hugging Face), while the
transformer's lack of a carried-over hidden state traces to the architecture paper
itself. The everyday consequences are owned too: Anthropic's own context-window,
memory-tool, and context-management pages state that the whole conversation
accumulates inside a fixed token window, what happens when it overflows, that the
server can summarize older turns (compaction) or clear them (context editing), and
that a "memory" feature stores facts in files outside the window and reads them
back into context on later turns.

Two limits the writer must respect. First, the single claim the angle leans on that
no opened vendor page states verbatim is "a memory feature stores facts elsewhere
rather than learning them into the weights." The owned pages establish the first
half (facts stored outside the window, injected into context) firsthand; the "not
into weights" contrast is a sound synthesis from the same pages distinguishing the
context window from training data, not a vendor quotation. Write it as reasoning,
not as a citation. Second, OpenAI's consumer ChatGPT memory documentation
(help.openai.com) is gated to automated fetch (HTTP 403 on two attempts) and could
not be opened; it is recorded below but must not be cited as read. The Anthropic
memory tool page carries the product-memory mechanism firsthand and is the source
to cite for it.

The evidence does not undermine the angle. It confirms it. The one correction it
forces is on course placement, not on the mechanism: the neighbor lessons the
commission tells the writer to link are not in the published library (see the
`nb history` finding under Numbers and Discarded). Only `the-mechanics/word-order`
is a published, relevant link target.

## Sources

```text
URL:         https://platform.claude.com/docs/en/build-with-claude/working-with-messages
Kind:        primary — the API owner (Anthropic) documenting its own Messages API behavior.
Establishes: Step 2, firsthand and settled. The endpoint is stateless; the caller
             resends the full conversational history each request. Also shows,
             firsthand, that resending grows the token count (the transcript is
             literally re-sent, not referenced by ID).
Paraphrase:  Anthropic states the Messages API is stateless and that you always send
             the full conversational history to the API to build up a conversation
             over time. The worked example sends one user turn (input_tokens 12),
             then a three-message user/assistant/user transcript (input_tokens 30):
             the growth is the resent history.
Locators:    Section "Multiple conversational turns"; the two "Output" JSON blocks
             report usage.input_tokens 12 and 30 respectively.
Quote:       "The Messages API is stateless, which means that you always send the
             full conversational history to the API."
```

```text
URL:         https://developers.openai.com/api/docs/guides/conversation-state
Kind:        primary — the API owner (OpenAI) documenting request statelessness.
Establishes: Step 2, firsthand and settled, for the second major API. Each request
             is independent and stateless; multi-turn memory is reconstructed by the
             developer resending prior messages.
Paraphrase:  OpenAI states each text-generation request is independent and stateless,
             and that multi-turn conversations are implemented by passing prior
             messages as parameters on each request. Server-side helpers
             (Conversations API, previous_response_id) exist precisely because the
             underlying requests hold no state.
Locators:    Section "Manually manage conversation state," opening sentence.
Quote:       "While each text generation request is independent and stateless, you
             can still implement multi-turn conversations by providing additional
             messages as parameters to your text generation request."
```

```text
URL:         https://developers.openai.com/api/reference/chat-completions/overview
Kind:        primary — the API owner (OpenAI), the endpoint reference.
Establishes: Step 2 support, firsthand and settled. The endpoint's input is a list
             of messages comprising the conversation; nothing about a prior
             conversation is held server-side by the endpoint itself.
Paraphrase:  The Chat Completions endpoint generates a model response from a list of
             messages that make up the conversation. The conversation is the input,
             supplied each call.
Locators:    Overview paragraph.
Quote:       "The Chat Completions API endpoint will generate a model response from a
             list of messages comprising a conversation."
```

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary — the paper that owns the transformer architecture (Vaswani et
             al., 2017).
Establishes: Step 1 support, settled engineering. The transformer dispenses with
             recurrence entirely: there is no recurrent hidden state carried from a
             previous call. A forward pass attends over the tokens it is handed and
             nothing else. This is why a call cannot "remember" a prior call — there
             is no cross-call state in the architecture to carry it.
Paraphrase:  The architecture is based solely on attention, with recurrence and
             convolution removed. Attention operates over the provided sequence; no
             recurrent state persists between separate forward passes.
Locators:    Abstract, first architectural sentence.
Quote:       "We propose a new simple network architecture, the Transformer, based
             solely on attention mechanisms, dispensing with recurrence and
             convolutions entirely."
```

```text
URL:         https://arxiv.org/abs/2309.06180
Kind:        primary — the systems literature that owns KV-cache serving (Kwon et
             al., "Efficient Memory Management for LLM Serving with PagedAttention,"
             2023).
Establishes: Step 1 core, settled engineering. The KV cache is per-request state
             that grows and shrinks over the life of that one request; it is
             allocated for a request and returned to a shared pool when no request
             needs it. It is a within-request optimization, not storage that
             survives the call.
Paraphrase:  Each request has its own KV-cache memory whose size changes dynamically
             as the request runs. The serving system allocates KV blocks as a
             sequence grows and returns them to a pool when the request no longer
             needs them, so the memory is reused by later requests rather than kept.
Locators:    Abstract (KV-cache-per-request sizing); paper's memory-management
             mechanism (block allocation and return-to-pool).
Quote:       "the key-value cache (KV cache) memory for each request is huge and
             grows and shrinks dynamically"
```

```text
URL:         https://huggingface.co/docs/transformers/en/kv_cache
Kind:        secondary — an independent implementation reference (Hugging Face
             Transformers), not one of the chatbot vendors; corroborates the KV-cache
             mechanism from outside the parties whose products the lesson explains.
Establishes: Step 1 support, settled engineering. The KV cache exists to avoid
             recomputing key/value vectors for earlier tokens during one generation;
             the default cache grows dynamically as generation progresses. This is a
             speed optimization internal to a single generation, consistent with the
             vLLM primary.
Paraphrase:  For autoregressive generation the model would otherwise recompute the
             key/value vectors of all prior tokens at each step; the KV cache stores
             them for reuse within that generation. The default DynamicCache grows as
             more tokens are generated.
Locators:    "Cache strategies" / caching explanation pages; DynamicCache description.
Quote:       "A KV cache stores these calculations so they can be reused without
             recomputing them." (as rendered on the Hugging Face caching reference)
```

```text
URL:         https://platform.claude.com/docs/en/build-with-claude/context-windows
Kind:        primary — the product owner (Anthropic) documenting the context window.
Establishes: Step 3, firsthand. Mixed status: the window as a fixed working memory
             the whole conversation must fit inside is settled; the specific overflow
             behavior is product-dependent and stated here. Grounds "a long chat
             exhausts the window and the start is dropped or summarized," and grounds
             that the window is not the model's training ("working memory," distinct
             from training corpus) — the anchor for the memory-vs-weights point.
Paraphrase:  The context window is all the text the model can reference when
             generating, including its own response; it is a working memory distinct
             from the training corpus. Each turn's input contains all previous
             history plus the new message, and previous turns accumulate until the
             limit. Chat interfaces such as claude.ai can manage the window on a
             rolling first-in-first-out basis. On overflow: if the input alone
             exceeds the window the API returns a 400 "prompt is too long"; on newer
             models, if input plus max_tokens exceeds the window generation stops with
             stop_reason "model_context_window_exceeded." Server-side compaction can
             summarize earlier parts so the conversation continues past the limit.
             As token count grows, accuracy and recall degrade ("context rot").
Locators:    "How the context window works"; footnote 1 (rolling FIFO on chat
             interfaces); "Context window overflow behavior"; "Manage context with
             compaction."
Quote:       "The 'context window' refers to all the text a language model can
             reference when generating a response, including the response itself.
             This is different from the large corpus of data the language model was
             trained on, and instead represents a 'working memory' for the model."
             And: "If generation then reaches the context window limit, it stops with
             stop_reason: 'model_context_window_exceeded'."
```

```text
URL:         https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
Kind:        primary — the product owner (Anthropic) documenting a "memory" feature.
Establishes: Step 3 (the memory feature), firsthand; product-dependent mechanism.
             A memory feature stores facts in files outside the context window and
             reads them back into context on later turns/sessions. The model is not
             changed; storage lives in the application's infrastructure and is
             re-injected as ordinary tool content. Also names the two ways a long
             conversation is handled: context editing (client-side clearing of old
             turns) and compaction (server-side summarization near the limit).
Paraphrase:  The memory tool lets the model store and retrieve information across
             conversations as files that persist between sessions, "without keeping
             everything in the context window." The model checks its memory directory
             and reads files back in later conversations. Storage is client-side, in
             infrastructure the developer controls. The injected system instruction
             warns the model its context window may be reset at any moment, so
             unrecorded progress is lost. Compaction "summarizes older conversation
             context server-side"; context editing clears specific tool results on
             the client.
Locators:    Intro; "How it works"; "Prompting guidance" (the injected MEMORY
             PROTOCOL / "ASSUME INTERRUPTION" text); "Using with compaction."
Quote:       "The memory tool lets Claude store and retrieve information across
             conversations in a directory of memory files ... building up knowledge
             over time without keeping everything in the context window."
             And, from the injected system prompt: "ASSUME INTERRUPTION: Your context
             window might be reset at any moment, so you risk losing any progress that
             is not recorded in your memory directory."
```

```text
URL:         https://claude.com/blog/context-management
Kind:        primary — the product owner (Anthropic) announcing context editing and
             the memory tool. (Reached via 308 redirect from
             anthropic.com/news/context-management; record the resolved page.)
Establishes: Step 3 support, firsthand; product-dependent. Restates plainly that
             memory is stored outside the context window in files and consulted, and
             that context editing clears older tool calls/results from the window as
             the token limit approaches.
Paraphrase:  Context editing automatically clears stale tool calls and results from
             within the context window when the conversation nears the token limit.
             The memory tool lets the model store and consult information outside the
             context window through a file-based system that persists across
             conversations, in the developer's infrastructure.
Locators:    Feature descriptions for "Context editing" and "Memory tool."
Quote:       "Context editing automatically clears stale tool calls and results from
             within the context window when approaching token limits." And: "The
             memory tool enables Claude to store and consult information outside the
             context window through a file-based system."
```

```text
URL:         https://help.openai.com/en/articles/8590148-memory-faq
Kind:        primary (product owner, OpenAI) — BUT GATED. HTTP 403 on two fetch
             attempts; the automated fetcher cannot send a browser-style request, so
             the page could not be opened.
Establishes: Nothing citable. Recorded so the writer/editor know the canonical
             OpenAI consumer-memory page exists at this URL and why it is absent from
             the citable set. Do NOT cite as read. The product-memory mechanism is
             carried firsthand by the Anthropic memory tool page above; if the writer
             wants an OpenAI-specific product-memory citation, this page must be
             opened by a human or a browser-capable fetch first.
Paraphrase:  (Unverified — not opened.) Search snippets describe ChatGPT saved
             memories as part of the context used to generate a response, injected
             into the prompt rather than retrained into the model. Treat as a lead to
             confirm, not as evidence.
Locators:    n/a (page not retrieved).
Quote:       none (page not retrieved).
```

## Contradictions

No source contradicts the mechanism. The chain is consistent across two independent
API owners, the architecture paper, the systems literature, and an independent
implementation reference. The tensions worth flagging for the editor are boundaries,
not disagreements:

- **"Stateless" is a statement about the model call and the API endpoint, not about
  the whole product.** The same vendors sell stateful conveniences layered on top:
  OpenAI's Conversations API and `previous_response_id`, and Anthropic's
  server-side compaction. These do not contradict statelessness; they exist because
  the underlying call holds no state, and they store or resend the transcript for
  you. The lesson should not let "the server can keep your conversation for you"
  blur into "the model remembers." OpenAI's own doc frames these helpers as
  automating the manual resend.

- **Exactly how a product trims or summarizes when the transcript outgrows the
  window is product-dependent, and much of it is undocumented.** Anthropic documents
  three named behaviors (a rolling first-in-first-out drop on chat interfaces like
  claude.ai; server-side compaction that summarizes older turns; context editing
  that clears old tool results) and an API overflow signal
  (`model_context_window_exceeded`). It does not publish the trigger points or the
  summarization prompt. For other products the trimming/summarization policy is not
  stated at all. Record as UNKNOWN per product; do not assert a single universal
  "the app drops the oldest turns" mechanism as if every product did it the same way.

- **"Stored facts are not learned into the weights" is not stated verbatim by any
  opened vendor page.** It is sound synthesis: the context-window page distinguishes
  the window (working memory) from the training corpus, and both memory pages
  describe storage in files/infrastructure that is read back into context. The
  writer states this as reasoning grounded in those owned statements, not as a
  vendor quote.

## Numbers

```text
Figure: input_tokens 12 (one user turn) vs 30 (three-message transcript resent)
Owner:  Anthropic Messages API doc (working-with-messages), the two example outputs
Scope:  Illustrative token counts for the doc's example requests; shows the resent
        transcript is the input and grows with history. Not a benchmark.
```

```text
Figure: context window 200,000 tokens (baseline) / up to 1,000,000 tokens (newer models)
Owner:  Anthropic context-windows doc
Scope:  Per-model context window size on the Claude API; the whole conversation plus
        the new output must fit inside it. Illustrative of "the window is finite,"
        which is the load-bearing point; the exact figures are version-specific and
        not the argument's ground.
```

```text
Figure: stop_reason "model_context_window_exceeded"; 400 "prompt is too long"
Owner:  Anthropic context-windows doc ("Context window overflow behavior")
Scope:  The two documented overflow outcomes on the Claude API — input-plus-output
        overflow during generation vs input alone already over the window. Concrete
        proof that the window is a hard limit, not a soft degrade, at the API layer.
```

```text
Figure: 8 published articles in the library; 0 of the commission's named neighbors present
Owner:  this checkout's `nb history` (NB_LIBRARY checkout)
Scope:  Published slugs are: the-evidence/emergence-loss-perspective,
        the-instruments/alpacaeval, the-mechanics/prompt-sensitivity,
        the-mechanics/word-order, what-could-go-wrong/cot-monitorability,
        what-could-go-wrong/situational-awareness, when-ai-breaks/robodebt,
        when-ai-breaks/tesla-autopilot. The neighbor lessons the commission tells the
        writer to link — the-mechanics/prefill-and-decode, the-mechanics/knowledge-cutoff,
        the-mechanics/losing-the-thread, the-mechanics/retrieval, and
        the-instruments/context-window — are NOT published. The writer must not link
        them. The only published, on-topic link target is the-mechanics/word-order
        (self-attention and positional encoding).
```

## Source assets

```text
Asset: The two "Multiple conversational turns" example outputs on the Anthropic
       Messages API page, side by side (input_tokens 12 for one turn, 30 for the
       three-message transcript).
Shows: The mechanism made concrete in one screen: the transcript is the input, and
       the input-token count rises because the whole prior conversation is resent,
       not recalled. This is the cleanest single artifact for Step 2.
Crop:  Must retain both usage.input_tokens values and enough of the messages arrays
       to show one array has three messages and the other one. Omit the language-tab
       code variants (bash/python/etc.) — one language is enough.
```

```text
Asset: The context-window diagram on the Anthropic context-windows doc
       (context-window.svg), turns accumulating until the token limit.
Shows: Step 3's setup — each turn is added to the window and previous turns are kept,
       so a long conversation walks toward a fixed ceiling.
Crop:  Must retain the accumulation-toward-limit axis. This is a vendor diagram;
       reproduce only if the article's charts policy allows an external figure, and
       note the source in the caption. Prefer building the paper's own chart if a
       chart is used at all.
```

```text
Asset: The injected MEMORY PROTOCOL / "ASSUME INTERRUPTION: Your context window
       might be reset at any moment..." text on the memory-tool page.
Shows: In the vendor's own words, the model is told it has no persistent memory and
       that anything not written to external storage is lost — the memory-feature
       step stated by the party that owns it.
Crop:  Quote the "ASSUME INTERRUPTION" line; it stands on its own and needs no image.
```

```text
Asset (other pages): None found. The OpenAI conversation-state and Chat Completions
       reference pages, the attention paper, the vLLM paper, and the Hugging Face
       KV-cache pages carry the argument in prose; no single figure beats the text.
```

## Discarded

```text
https://help.openai.com/en/articles/8590148-memory-faq: OpenAI's consumer ChatGPT
  memory FAQ — the on-topic OpenAI product-memory page, but gated (HTTP 403 on two
  fetch attempts; no browser-header option available to the fetcher). Not opened, so
  not cited. Kept in Sources as a recorded-but-unverified lead; the Anthropic memory
  tool page carries the same mechanism firsthand.
https://openai.com/index/memory-and-new-controls-for-chatgpt/ and
https://openai.com/index/chatgpt-memory-dreaming/: OpenAI memory announcement pages —
  same 403 gating on the openai.com host; not opened, not cited.
https://learn.chatgpt.com/docs/customization/memories: resolved but returned Codex
  (developer tool) memory content, not the ChatGPT consumer-memory feature the
  commission asked for; off-target, discarded.
blogs.novita.ai, apidoc.cometapi.com, doc.newapi.pro, portkey.ai, medium.com,
datastudios.org, morphllm.com, aionx.co and similar: third-party restatements of the
  API and memory behavior. Every claim they carry is available firsthand from the
  vendor's own reference pages above, so they add repetition, not evidence, and a
  repetition supports only that a claim was made. Discarded in favor of the owners.
the-mechanics/prefill-and-decode, the-mechanics/knowledge-cutoff,
the-mechanics/losing-the-thread, the-mechanics/retrieval, the-instruments/context-window:
  named by the commission as link neighbors but absent from the published library
  (`nb history`), so unavailable as link targets. Recorded under Numbers; not usable.
```
