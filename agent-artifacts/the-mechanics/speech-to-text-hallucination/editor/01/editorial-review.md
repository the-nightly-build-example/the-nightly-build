# Editorial review: the-mechanics/speech-to-text-hallucination (editor/01)

## Skeptic

Thesis: a transcription tool's writing stage is an audio-conditional language
model, so when the audio carries little or nothing to condition on, that stage
falls back on its language prior and emits the most probable text (a fluent
sentence) rather than a blank. The invention over silence is the designed output
of that stage, not a glitch.

Claims it stands on, and how each held:

- **Whisper's decoder is "an audio-conditional language model" (s5, Radford et
  al.).** The evidence carries OpenAI's exact quote. Verified against the record;
  the display and body use it correctly. Held.
- **A language model given low-information input still produces its most probable
  continuation, a grammatical sentence.** Supported by the decoder's LM nature
  (s5) plus OpenAI's own model card, which attributes hallucination to "the model
  combining language prediction with transcription" (s7). Held.
- **The behavior is real and consequential in deployment: Nabla, 30,000+
  clinicians, deletes audio by default (s1 AP; s2 Nabla).** Figures and the
  opt-in nuance match the record. Held.
- **No single trustworthy rate; each figure carries its scope (s4, s1, s2).**
  This is the round's hardest-check item. See the fix below; held after
  correction.
- **Invention is distinct from mishearing (s3, Frieske & Shi); temperature 0
  still hallucinated (s4); competitors produced 0 comparable hallucinations on
  the same 187 segments (s4).** Directions and denominators match the record, and
  the competitor finding is correctly time-scoped ("As of 2023 and 2024") and
  hedged as a single comparison. Held.

Breaks found and resolved:

- **The 1.4% was misattributed.** The draft read "The 1.4% comes from interviews
  with people who have aphasia." The record (s4) shows 1.4% is the pooled average
  across all 13,140 segments, of which 7,805 are control (non-aphasic) speakers
  and 5,335 aphasia; the aphasia-only rate is 1.7%, control 1.2%. The pooled
  figure rests on more control audio than aphasia audio, so tying it to aphasic
  speakers overstates its scope. Fixed directly, without touching the number: the
  prose now reads "the average across interviews recorded for aphasia research,"
  and the table cell now reads "from interviews recorded for aphasia research."
  Both are accurate to the AphasiaBank corpus (patients and matched controls
  recorded under the same protocol) and preserve the teaching point that the
  audio was chosen for its pauses. No reporting needed; the record settles it.
- **An unsupported per-instance WER claim.** The draft said "a fluent invented
  sentence can score no worse on [WER] than an ordinary slip." A hallucinated
  sentence inserted over silence adds insertions and typically scores worse on
  WER per instance; what s3 actually establishes is the model-aggregate claim,
  that a hallucinatory and a non-hallucinatory model with similar baseline WER
  cannot be told apart. Cut the false clause; kept the accurate sentence, now
  "the same overall error rate." The point "cannot see it" still stands on the
  model-level claim.

Checks that passed without change: the "recognize speech / wreck a nice beach"
pair reads unmistakably as a hypothetical ("the audio says... and the transcript
reads..."), uncited, defining the contrast class before the invention; it cannot
be read as a Whisper output. The "trigger is low-information audio in general,
not digital silence in particular" line is intact and correctly cited to s3. The
chatbot lesson is linked in Background and referenced in prose, not duplicated;
the focus stays on the audio modality and the empty-input trigger. Every
`data-nb-kind` was audited against the researcher's authorship-and-stake test:
s2-s8 are primary (the parties own their claims or artifacts); s1 (AP) is
correctly secondary, because it reports findings owned by others (the Michigan
researcher's 8-of-10, the developer's 26,000, the Koenecke figures). Citation
order is first-appearance. The AP source is a documented KSL reprint of the
identical AP wire copy, recorded in the evidence with its reason, so it lands on
the source text.

## Cut

Slop pass against `spec/slop.md`, every sentence including display text, the
table caption, and the note. The bookends are the lesson template's two cards
that may address the reader; judged for content, both carry the lesson's own
particulars and resolve as a pair (opener poses why-invent, why-over-silence,
why-shared-with-a-chatbot; takeaway answers each and lands on the audio-deletion
safeguard). Kept intact.

Sentences cut, all empty signposts that reported where the argument stood without
doing its reasoning:

- "and the reason is worth understanding" (after "There is no single answer") —
  throat-clearing; the table and the paragraph after it deliver the reason.
- "which is the clue to the cause" (after "The rate depends on what the system is
  fed") — signposts the turn to mechanism without adding a step.
- "That second half is the crux, because of what it is." — unearned emphasis; the
  next sentence delivers "an audio-conditional language model" and carries the
  weight itself.
- "Now the behavior follows." — a bare "here comes the payoff" beat, unlike the
  Ciechanowski hinge the voice guide praises, which names a mechanism.
- "One more finding bears on how specific the problem is." — tells the reader what
  to make of the competitor finding, which the following sentences already
  interpret.

Five sentences failed the delete test; no repeated structural pattern beyond the
recurring edge-signpost habit. One earned negative-parallelism construction was
checked and kept ("The trigger is low-information audio in general, not digital
silence in particular"): the misconception it corrects is real and named, since
the rest of the piece leans on "silence." The dek's "instead of a blank," "Its
job is not to report sounds," and "work around the decoder rather than change it"
are likewise earned contrasts against named assumptions, not reflex. One
house-punctuation fix: a semicolon splicing the two developer findings became a
period (the plainer mark, two separate findings).

Register: after the signpost cuts the prose sits in the plain, level Willison
register the voice guide directs, building backward the Ciechanowski way. No
borrowed phrasing from the guide's exemplars (the piece's images are its own:
the listener and the writer, "answers silence"). No prompt leakage: the
commissioned angle is restated in the article's own words and grounded in
citations, and "settled engineering / open questions" names specific facts rather
than narrating the lesson's method. One imperative body opener ("look at how the
tool is built") was recast declaratively, since the template reserves reader
address for the two bookends. Headings and headline were compared against the
recent Mechanics record via `nb history`: the headline avoids both flagged molds,
the dek uses none of the three banned dek molds, and every heading is this
behavior's own step.

Furniture: the rate table earns its place (it is what makes the "no single rate"
finding legible, and no prose ordering would show the spread as clearly). The
"What Whisper writes over silence" note is the documented quotation-label
component and doubles as the piece's visual evidence, showing the actual invented
phrases. No component is decorative or formulaic. No source asset is required:
the behavior is shown through quoted real outputs and named examples, and the
mechanism is a reasoning chain prose carries well.

## Reader

Read straight through as the paper's declared reader, someone smart who has never
read code: I come away able to say why a transcriber invents text, not just that
it does. What the sources alone would not give me is the assembled backward
chain, from a fabricated clinical line down to the single fact that the writing
stage is a language model, plus the synthesis that turns three incompatible
"rates" into the lesson that no single rate exists and why. The original-work
sentence claims exactly that chain and that rate synthesis as the visible work,
and the article delivers both; neither lives in any one source. The prose sits
closer to the voice-guide exemplars than to a median summary, and the ending
feels earned rather than announced. The headline, read as the largest claim,
commits to what the piece defends.

## Edits

- Misattributed 1.4% scope corrected in body prose: now "the average across
  interviews recorded for aphasia research."
- Same figure's scope corrected in the rate table cell: now "from interviews
  recorded for aphasia research."
- Cut unsupported per-instance WER clause ("a fluent invented sentence can score
  no worse on it than an ordinary slip"); kept and tightened the accurate
  model-level claim to "the same overall error rate."
- Cut signpost "and the reason is worth understanding."
- Cut signpost clause "which is the clue to the cause."
- Cut signpost sentence "That second half is the crux, because of what it is."
- Cut signpost sentence "Now the behavior follows."
- Cut signpost sentence "One more finding bears on how specific the problem is."
- Recast imperative body opener "To see why... look at how the tool is built" to
  the declarative "Why nothing in the audio can still become words comes down to
  how the tool is built."
- Semicolon to period between the two developer findings in the orientation
  paragraph.

## Required work

None. Every issue was the editor's to fix and was fixed directly. No evidence is
missing, no load-bearing claim broke, and no reporting or redraft is needed. The
orchestrator stamps after these edits (word count and reading time will
recompute; several sentences were cut).

## Decision

approve — the thesis holds on the evidence, the one scope error and one
unsupported clause are fixed against the record, and the slop and formula passes
leave the piece in the register its voice guide directs.
