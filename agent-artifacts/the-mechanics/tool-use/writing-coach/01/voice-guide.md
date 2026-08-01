# Voice guide — the-mechanics/tool-use

Register: a plain, confident engineer's explanation, not a tour-guide's. Write
as someone who has read the actual request/response payloads and is now
walking a smart reader through them line by line. The reader relationship is
peer-to-peer: you assume they can read a JSON blob once you show it, so show
it instead of describing it.

Moves that will change sentences in this draft:

- When you name a mechanical step (the schema in the prompt, the model's
  emitted call, the harness's parse-and-execute, the pasted-back result),
  produce the actual artifact at that step — the real field names from the
  Anthropic/OpenAI schema, the real shape of a tool-call span — rather than a
  paraphrase of what it contains. A reader who can see the JSON does not need
  it summarized.
- Mark the seam between settled and open inline, in the sentence where it
  occurs, not in a separate caveat paragraph. State plainly what is verified
  ("the harness executes this; that part is documented") right next to what
  is not ("why the model chose to call it here is not something anyone can
  point to in the weights"). Keep the two grammatically parallel so the
  reader can tell them apart without a label.
- Use a short, flat declarative sentence at the exact moment the reader's
  wrong mental model breaks — the point where "the model reached out to the
  web" stops being true. One sentence, plain subject and verb, then rebuild
  with the concrete mechanism in the sentences that follow. Do not soften
  that sentence with a hedge.
- Name the outer loop pattern (ReAct, or whatever term the piece settles on)
  exactly once, at the point the reader has already seen it happen in the
  worked example, then reuse that exact name. Do not redefine it a second
  time or reach for a synonym later.
- Keep the injection/hijack risk to the one clause the commission allows.
  State what specifically is uncertain (not "risks exist" but the named
  failure mode: a tool called that the model was told not to call, or
  argument-filling that silently drifts) rather than gesturing at danger in
  general terms.
- Let the worked example carry the proof. Once the reader has traced one real
  call end to end, later claims about the loop can refer back to it ("as in
  the weather call above") instead of re-explaining the mechanism.

Recently used, do not reuse: no three-scenario cold open (a the-mechanics
habit); no single-cute-number open; no colon-subtitle headline; no
hedged-contrast dek; no Verdict block.

## Simon Willison, "OpenAI: Function calling and other API updates"
Source: https://simonwillison.net/2023/Jun/13/function-calling/
Craft:
- cadence: short paragraphs, one claim per sentence, no windup before the
  mechanism is stated
- argument: states the request/response shape first, names the underlying
  pattern (ReAct) second, flags the risk third — mechanism, then
  classification, then caveat, in that fixed order
- evidence: the literal shape of the API payload, described precisely enough
  that a reader could reproduce the call
- stance: a practitioner reporting what he tested, not a commentator
  summarizing a spec
- notice: catches that this is a fine-tuned behavior riding on an existing
  pattern (ReAct), not a new architecture, and says so in one clause instead
  of a paragraph
- diction: plain nouns for the pieces (a blob of JSON, a function call,
  results passed back); no metaphor stands in for the mechanism
- reader: assumes the reader can evaluate a schema unaided once shown one
- the move the axes miss: he names the risk in the same breath as the
  feature, not in a separate section — caution is folded into the
  explanation, not appended to it
Calibration: "You can now send JSON schema defining one or more functions to
GPT 3.5 and GPT-4 — those models will then return a blob of JSON describing a
function they want you to call (if they determine that one should be
called). Your code executes the function and passes the results back to the
model to continue the execution flow."

## Julia Evans, "Why is DNS still hard to learn?"
Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/
Craft:
- cadence: conversational but never loose — a plain claim, then the concrete
  case that proves it, rarely more than two sentences apart
- argument: opens by naming the gap between how simple the mechanism actually
  is and how confusing it feels, then spends the piece closing that gap one
  named cause at a time
- evidence: real tool output and real settings (dig, ndots, resolver
  behavior) standing in for the claim instead of describing them abstractly
- stance: fellow-sufferer turned explainer — she reports her own wrong mental
  model before she corrects it, which earns the correction rather than
  asserting it
- notice: catches that a mechanism can be simple while still being hard to
  learn, because the hard part is invisible until named — a distinction most
  explainers collapse
- diction: informal register, technical terms unfussy and defined in the
  clause where they first appear, never redefined afterward
- reader: treated as capable of following a real example immediately, no
  simplification for its own sake
- the move the axes miss: she times each revelation to the exact moment a
  reader would have been confused, not to a logical outline drawn up in
  advance
Calibration: "It took me probably 5 years to realize that I shouldn't visit a
domain that doesn't have a DNS record yet, because then the nonexistence of
that record will be cached, and it gets cached for HOURS, and it's really
annoying."

## Dan Luu, "Files are hard"
Source: https://danluu.com/file-consistency/
Craft:
- cadence: short flat sentences mark the pivots ("Files are hard."); dense
  technical sentences do the actual work in between
- argument: escalates by layering one cause on the last — a single write
  failure, then filesystem semantics, then error-handling gaps, then how
  often this actually happens — each layer sits strictly on the one before
  it
- evidence: findings from primary research papers embedded with their actual
  numbers, plus one worked failure case followed through to its exact broken
  output
- stance: reluctant discoverer, not advocate — presents each finding as
  something he didn't want to be true, which is what makes the escalation
  credible
- notice: catches that a system can be well-specified and still fail in
  practice, and separates those two claims instead of treating "documented"
  as "reliable"
- diction: exact technical nouns (pwrite, rename, crash), no softening
  synonym substituted when the ugly word is the accurate one
- reader: assumes technical fluency and never re-explains a term once it is
  set, but always shows the failing case before naming the abstraction it
  illustrates
- the move the axes miss: he states what is unverified as plainly as what is
  verified — noting that a finding has never been replicated carries the same
  flat declarative weight as the finding itself
Calibration: "If nothing goes wrong, the file will contain `a bar`, but if
there's a crash during the write, we could get `a boo`, `a far`, or any other
combination."
