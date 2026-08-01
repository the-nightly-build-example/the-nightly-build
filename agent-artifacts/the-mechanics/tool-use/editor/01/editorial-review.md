# Editorial review 01 — the-mechanics/tool-use

Skeptic: thesis "the model that calls a tool never runs it — tool use is a
documented, five-step contract in which the model only emits and reads text
while a separate program executes"; tested 4 claims (the schema-in-prompt
step, the model's emitted call is inert text, the harness executes and pastes
back a result, the settled/open line runs through training not architecture);
broke: none survive as broken. Reopened all eight cited primaries live
(Anthropic overview and how-tool-use-works, OpenAI cookbook, MCP introduction
and architecture, ReAct and Toolformer full text) and recomputed every
figure. Anthropic's "never executes anything on its own" quote, the five-step
loop, the get_weather round trip's final sentence, the OpenAI `tool_calls`
shape and its arguments-as-string field, the MCP host/client/server split and
its `tools/call` pseudocode, ReAct's ALFWorld (71/45/37), WebShop (40.0 vs
28.7), and hallucination (14% vs 6%, 56% vs 0% of failures) numbers, and
Toolformer's WebQuestions/Natural Questions counter-case (26.3 vs 29.0, 17.7
vs 22.6) all match the live primary sources exactly, direction and magnitude.
The one figure I could not confirm directly against the paper's own text was
Figure 3's caption quote ("Aside from the Apple Remote...") — the ar5iv HTML
mirror's full-text search does not surface it because that trajectory lives
inside a figure image, not the mirror's extracted text. I opened the
article's own committed asset (`tool-use/asset-1.png`) and it is a legible
crop of ReAct Figure 1(1d) carrying exactly that Apple Remote/Front Row
trajectory, Thought/Act/Observation labels intact — the citation and caption
are accurate. Display text checked descriptor by descriptor: headline and dek
both paraphrase Anthropic's own "never executes anything on its own"
language without overclaiming; the three Background-band link titles
("Language models draw no line between instructions and data," "The instant
a model writes a token, it becomes fact," "A model's weights freeze the
moment its training run ends") match the live `<h1>` of each linked article
in `library-checkout` exactly. Every `data-nb-kind` is correctly assigned:
the two Anthropic pages, the OpenAI cookbook, both MCP pages, and both papers
are primary (each is the owning source of the claim it supports); Apideck is
correctly the lone secondary, used only for context, never for a claim a
primary doesn't already carry. Confirmed the article never writes that the
model itself "accesses" the web, runs code, or searches — every instance of
that action is attributed to "a program," "your code," "the host," or "the
server," and the worked function-calling example (Anthropic's `tool_use`/
`tool_result` schema, cross-walked against OpenAI's `tools`/`tool_calls`
shape) matches both cited primary docs' current field names.

Cut: 6 direct edits, roughly 60 words net. Worst tell: "The loop itself is
settled engineering" reused the series prompt's own planning vocabulary
("Mark which steps are settled engineering and which are open questions")
as if it were reported analysis — cut "engineering," leaving "is settled."

Reader: this gives me a single continuous trace of one real tool call
stitched across sources that individually never connect to each other
(Anthropic's schema, OpenAI's wire format, MCP's execution boundary, ReAct's
name for the loop, Toolformer's proof that the boundary is trained rather
than built), with the settled/open line placed exactly where the evidence
stops — not "risks exist" but the two named, verifiable failure modes.
Prose sits close to the voice-guide exemplars: JSON is shown rather than
described, the wrong-mental-model break ("It did not.") is a flat plain
sentence, ReAct is named exactly once and reused, and the two remaining
central contrasts (the call is text and not an execution; training decides,
not a wire or an architecture) are each doing real, distinct work rather than
padding. Headline as the largest claim holds: "A model that calls a tool
never runs it" is a direct paraphrase of Anthropic's own stated contract, not
an invented dramatization.

## Direct edits made

1. `the-call-is-still-just-text`: cut ", as the next section shows" — a
   signpost about the piece's own structure, and an inaccurate one (the
   claim that the shape predates chat APIs is actually established two
   sections later, by Toolformer, not by the immediately following section).
2. Body prose: "an open standard" → "an open-source standard," matching
   MCP's own self-description exactly (MCP's introduction page: "an
   open-source standard for connecting AI applications to external
   systems").
3. `the-loop-has-a-name`: cut the opening sentence "The paper is not naming
   a style choice." — asserted the argument's importance instead of making
   it; the following sentence carries the actual claim and stands on its
   own.
4. `what-is-settled-and-what-is-not`: cut "engineering" from "is settled
   engineering" — reused the series prompt's own planning label
   ("settled engineering... open questions") as reported prose. Also cut the
   redundant trailing ", not architectural" from the paragraph's closing
   sentence, since the same trained-vs-architectural contrast had already
   been made twice in the two sentences immediately before it.
5. Same section, closing paragraph: the injection/hijack aside ran four
   sentences (setup, elaboration, the named failure mode, and a pointer to
   "a separate lesson's argument"). Both the commission ("keep it to one
   sentence and defer the argument to the jailbreaks piece") and the voice
   guide ("keep the injection/hijack risk to the one clause the commission
   allows") cap this at one sentence. Cut to one: "The same gap makes a
   fetched page dangerous: a page can tell the model to call a tool it was
   told not to, or quietly drift the arguments it fills." This keeps the
   voice guide's required named failure modes verbatim and drops the
   self-referential pointer to another article.
6. Updated the declared word count in `nb-meta` from 2198 to 2139, an
   editor's estimate of the roughly 60-word net reduction from the cuts
   above. The writer should confirm the exact figure when re-running the
   proof; `reading_minutes` (10) does not change at this size.

## Required work by owner

None. No redraft needed. The remaining "the model's call is a paragraph it
writes, not a button it presses" / "training, not a wire" contrasts in the
first two body sections are close together but each corrects a distinct,
real misconception central to this lesson's thesis (that the call is inert
text, and that a trained decision rather than a wired connection governs
when it fires) — I judged them earned rather than formula and left them for
the writer's voice rather than force a rewrite over stylistic density alone.

## Decision

Proof was not re-run (editor does not run it); all cuts were subtractive or
single-word fixes matched to source language, well inside the surgical
mandate. No broken claim, no sourcing failure, no missing evidence. Publish.
