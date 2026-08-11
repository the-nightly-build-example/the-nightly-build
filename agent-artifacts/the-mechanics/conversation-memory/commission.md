# Commission: the-mechanics/conversation-memory

## Authorized work

Scheduled duty for 2026-08-11 returned `the-mechanics` as an open section: choose
one behavior within the beat, do not repeat a published slug. This commission
selects the behavior of a chatbot appearing to remember earlier turns in a
conversation. One article, lesson template, one Article PR.

## The behavior and why it

Anyone who has used a chatbot has watched it refer back to something they said
several messages earlier, and most people assume the model is holding the
conversation in some kind of memory. This desk answers "how does it actually do
that." The honest answer overturns the intuition: the model keeps nothing between
turns. The lesson matters because the misconception underneath ("it remembers me")
feeds a chain of further confusions the reader meets constantly, about privacy,
about why a new chat forgets everything, about why long chats get slow, degrade,
or lose the start, and about what a product's "memory" feature really does.

The beat's job: work backward from the behavior to its cause, step by step, each
step naming a real part of the system, with a small concrete example, until the
reader hits ground. Mark which steps are settled engineering and which vary by
product. No code.

## The angle

The chain to walk down: (1) a single model call is a pure function of the tokens
handed to it; the forward pass carries no state from any previous call, and the
within-request key/value cache that speeds generation is discarded when the call
ends. (2) So the "memory" of the conversation is not in the model; the application
rebuilds it every turn by resending the entire running transcript as the input.
(3) From that one fact fall the everyday behaviors: a brand-new chat starts blank
because nothing is resent; a long enough conversation exhausts the context window
and the app must drop or summarize the oldest turns, which is why the model
"forgets" the start; and a product "memory" feature is not the model recalling
you, it is the app storing facts elsewhere and quietly pasting them into the
prompt on later turns. Settled: statelessness and the resend. Varies / partly
open: exactly how each product trims, summarizes, or retrieves when the transcript
outgrows the window.

Keep it to a short list taught completely. Do not drift into the tokenizer, into
positional encoding, or into retrieval-over-documents beyond the one sentence
needed to connect them; those are separate lessons to link.

## Sources

Source floor: at least 8 sources, at least 4 primary, at least 1 secondary.
Primary here is the party that owns the claim: the API/product documentation for
how requests are shaped and how memory features work, and the technical
literature for statelessness and the forward pass.

Direct the researcher to read, at minimum:
- Anthropic and OpenAI API references showing that a chat request sends the full
  list of prior messages each call and that the endpoint holds no server-side
  conversation state (the `messages` array; any explicit "stateless" language).
- The product-level "memory" feature documentation (OpenAI's ChatGPT memory,
  Anthropic's memory/related feature) describing that saved facts are injected
  into context, not learned into weights.
- A primary technical source for the transformer forward pass and the KV cache
  being a within-request optimization (e.g., the attention paper and a systems
  reference on KV caching), to ground the statelessness claim.
- Documentation or a primary source on context-window limits and long-conversation
  handling (truncation/summarization), to ground the "forgets the start" step.
- At least one independent secondary source for context.

Verify each mechanism against a primary that owns it, not against a blog
restatement. Where a product's trimming/summarization behavior is undocumented,
record it as unknown rather than asserting a mechanism.

## Course placement and neighbors

The library holds `the-mechanics/prefill-and-decode` (the per-request forward
pass and KV cache within one call), `the-mechanics/knowledge-cutoff` (weights
frozen at training; new info arrives via the prompt), `the-mechanics/losing-the-thread`
(retrieval position within a long context), `the-mechanics/retrieval`, and
`the-instruments/context-window` (the window as a number). This lesson is the
one that ties the behavior "it remembers our chat" to the stateless resend; link
those rather than re-teaching them. Distinguish clearly from knowledge-cutoff
(that is about training, this is about a live conversation). Tonight's
`when-ai-breaks/bing-sydney` touches long-conversation instability; keep this
lesson to the general mechanism and let that incident link here, not the reverse.

## Production policy

Profile `balanced`; no directive `required`. Plan: coach low, researcher high,
writer medium, editor high; model class `capable`. Harness `claude-code-routine`.
Model Claude Opus 4.8. No required directive traded down.

## nb-meta

Date 2026-08-11. Harness `claude-code-routine`. Model `Claude Opus 4.8`. Three
descriptive tags, writer's choice (no tag fragments configured).

Recent habits to break travel with the writer brief.
