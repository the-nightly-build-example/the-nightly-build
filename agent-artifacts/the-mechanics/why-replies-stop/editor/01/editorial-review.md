# Editorial review: the-mechanics/why-replies-stop (editor/01)

## Skeptic

Thesis: a chatbot reply ends for one of two mechanically distinct reasons, and
the reader can tell which from the shape of the ending on screen. Either the
model sampled a learned end-of-turn token out of its vocabulary (a whole thought,
reported `end_turn`), or the serving program's length cap truncated it before that
token arrived (often a word cut in half, reported `max_tokens`).

Load-bearing claims and how they held:

1. The stop is an ordinary sampled token, not a bolted-on rule. Held. The article
   names Llama's `<|eot_id|>`, its integer id `128009`, and the decode loop's halt
   on the end-of-sequence token. I checked the torchtune map (id 128009), the Meta
   quote ("has determined that it has finished interacting with the user message"),
   and the HF generation reference. All three land on the claim. The two levers
   (drive EOS probability off, force it at a cap) correctly prove the token is
   ordinary, not hard-wired.

2. The turn-end behavior is learned in post-training; base models are NOT unable to
   stop. This was the round's hardest push and it holds exactly. The piece states a
   base model emits a document-end token (`<|end_of_text|>` / `<|endoftext|>`) at a
   document boundary and lacks only the turn-end habit, which post-training adds. It
   never says "never stop." The Meta quote ("is generated only by the base models"),
   the Qwen document-boundary gloss, the HF chat-templating claim, and InstructGPT's
   alignment finding all support it. The "In plain language" note sharpens the exact
   distinction the whole lesson hinges on (base does stop; post-training teaches
   *where a turn ends*). Precise, per the evidence record's one real subtlety.

3. The serving cap is a second, separate actor. Held. `max_tokens` is quoted from
   the verified Anthropic wording ("the maximum number of tokens to generate before
   stopping"); Gemini's `MAX_TOKENS`/`STOP` are named as enum values, not quoted as
   prose, so no un-reverified Gemini wording is printed (the record's caveat honored).
   The "other endings exist" clause (refusal, tool use, context window) is one clause,
   correctly framed as the uncommon remainder, not padding.

4. The probability micro-example is illustrative, not measured. Held. Both the
   caption and the body sentence label it illustration; the ~0% -> ~92% shape is
   attributed to no named model as measurement, and the checkable HF
   `compute_transition_scores` method is cited as the real substrate.

Display text, descriptor by descriptor: headline is subject-verb with the surprise
in front and no colon tell; it is the exact claim the body defends. Dek adds the
post-training origin and the second cause without restating the headline, makes a
claim about the world (not a grade of the article), and is two clauses joined by
"and", not a banned triad. All five subheads are steps of this piece's own descent,
reconstructable in order, with no scaffolding slot. Byline "8 min read" matches
meta. Every named quote, token string, and id checks against its owning primary.

`data-nb-kind` audit: s1 Anthropic, s2 Meta, s3 torchtune, s4 HF generation, s6
Qwen, s7 HF chat-templating, s8 InstructGPT, s9 Gemini all correctly primary (each
authoring party owns the behavior it is cited for); s5 Nate Brake correctly
secondary. 8 primary / 1 secondary, matching the stamped count and the policy floor.

Citation hrefs: each points at the source itself. s2 is the github.com blob page,
which the record notes is gated to automated clients (403) but resolves in a
browser and is the reader-facing source, so it lands correctly for a human reader.
No endpoint-instead-of-source problems.

No break found. Every load-bearing claim survives its owning primary.

## Cut

The register is already flat and disciplined, so the cut was light. Three items:

- The worst tell: "Emitting that token is the whole of the signal that ends
  generation." That is the banned "X is the whole Y" mold the editorial direction
  names explicitly, a sentence that grades its own stakes. I could not simply delete
  it, because it carries the only inline citation to the secondary source (s5) and an
  orphaned source would break the count. I removed "the whole of" so the sentence
  states the fact flat and keeps its citation.

- "This lesson works backward from the ending on the screen to the part that
  produced it." A method signpost narrating the article's own structure. Cut; the
  paragraph now ends stronger on "...those two causes leaving their marks," and the
  Why-this-matters bookend already gives the reader the same orientation.

- "So the tell is simple." A self-grading throat-clear that announces ease instead
  of showing it. Cut; the paragraph now opens directly on the concrete
  argu/arguments example.

No prompt leakage: the caption's "illustrative" label is required factual
disclosure, not a planning label, and no "fulfilled the assignment" or step-label
language survives from the brief. Licenses are within bar: exactly one framing
question ("Where did the model learn..."), answered by the next sentence; one
second-person worked prediction (the France completion), which produces a real
prediction. The earned contrasts ("not a separate part bolted onto generation",
"A rule could not be switched off. A token can.", "The model did not stop itself.
The program stopped it.") each correct a real misconception and stay within the
ceiling. Furniture earns its place: the probability table is the illustration's
natural form and is NOT the banned "watch a product appear one line at a time"
framing; the "In plain language" note is deliberate emphasis on the piece's
subtlest precision point. No repeated heading cadence or dek mold from the recent
shelf. Ran `./nb stamp` after the cuts (words 1794).

## Reader

Read straight through, the piece gives what the scattered sources cannot: a single
sight test. The primaries hold the token facts, the stop codes, and the readout
method in separate places; the lesson joins them so a reader can look at a stopped
reply, read its shape, name which of two actors stopped it, and know whether to
raise the limit or re-ask. That matches the draft-handoff's original-work sentence,
and both survive. The prose sits with the voice-guide exemplars, not a median
summary: load-bearing steps are short subject-verb sentences, the trained fact is
stated flat with no wonder-words, and the model and the serving layer stay two named
actors the reader can point at. The headline reads true as the largest claim.

## Edits

- Changed "Emitting that token is the whole of the signal that ends generation" to
  "Emitting that token is the signal that ends generation" (removed banned "X is the
  whole Y" mold; kept the s5 secondary citation intact).
- Cut "This lesson works backward from the ending on the screen to the part that
  produced it." (self-referential method signpost).
- Cut "So the tell is simple." (self-grading throat-clear).
- Ran `./nb stamp` (words 1818 -> 1794; sources 9; reading_minutes 8 unchanged).

## Required work

None. No researcher, writer, or orchestrator work remains; the direct cuts resolved
the only tells found, and every load-bearing claim is sourced to its owning primary.

## Decision

approve. The two precision claims hold exactly, the model and serving layer stay two
named actors, `<code>` is confined to literal token strings and API values, and the
three surgical cuts cleared the only tells without leaving any publication-blocking
work.
