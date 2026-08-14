# Editorial review: the-mechanics/formatting-defaults (editor/01)

## Skeptic

Thesis: the bulleted, bold-headed answer a chatbot gives to a plain question is a
learned post-training output policy, not something the question required. The
piece walks backward from the visible behavior through three stages that could
put it there (pretraining exposure to markdown, supervised imitation, preference
optimization), argues the preference stage is the heaviest driver, and reaches
ground at a steerable policy an instruction turns off.

The claims it stands on, tested:

- **The formatting is the model's own default, not a demand of the question.**
  Held. Supported by lab behavior: labs ship instructions telling the model to
  stop defaulting to lists and headers, which only makes sense if the default is
  already there. Anthropic's published prompt wording is faithful to the source
  (I confirmed the "writes prose without bullets, numbered lists, or excessive
  bolding ... unless the person asks for a list or ranking" instruction on the
  release-notes page). Willison's "LLMs love to answer with lists of things" is a
  named, correctly-attributed secondary.

- **Preference judgments reward structure and length substantially, not wholly,
  independent of correctness.** Held, and this is the load-bearing precision. The
  LMSYS coefficients (length 0.249 against lists 0.031, headers 0.024, bold 0.019
  with both controlled; lists rising to 0.111 when length is free) match the
  evidence record, and I confirmed them and the "still observational" caveat
  against the LMSYS page directly. The article carries the caveat and Singhal's
  dataset-varying split (2 percent to 53 percent non-length share), so it does
  not overclaim to content-free. Human-vote evidence (LMSYS arena) and
  automated-judge evidence (Zheng's 91.3 percent verbosity-attack rate, RM-Bench's
  below-chance 46.6 percent, Dubois's 0.94 to 0.98) are attributed to their own
  sources and not blurred together, as the record's contradiction note requires.

- **The preference stage is the heaviest of the three contributors.** Held as
  earned inference, not as a measured apportionment. The piece is explicit that
  the pretraining share is unmeasured and the SFT demonstration shapes are
  undisclosed (both marked open), and it rests "heaviest" on mechanism:
  optimization amplifies any tilt past what imitation installed, and the reward
  end is where the large measured structure-and-length pressure sits. The dek's
  "built mostly by a stage that rewarded structure and length" states this thesis
  and is consistent with the body's "Heaviest of the three." I pushed hardest here
  because the commission lists "how much each stage contributes" as open; the
  resolution is that the piece claims dominance by argument while marking exact
  magnitudes unmeasured, and those are compatible. The claim survives.

- **The chain reaches ground: the format is a policy, steerable by instruction.**
  Held after one citation fix (below). OpenAI's Model Spec interactive-default and
  overridable-by-instruction wording supports it, and the Anthropic prompts are
  the override in practice.

Display text, descriptor by descriptor: headline "One line in the system prompt
turns off the bullet points" is a concrete claim the ground section defends.
Numbers in prose and caption match their owning primaries (InstructGPT ~13k
prompts / ~40 contractors; length-only reward 56 vs 58 percent; the LMSYS
coefficients; RM-Bench 46.6 percent; AlpacaEval 0.94 to 0.98). Every
`data-nb-kind` matches the evidence record's Kind line: eight primaries and one
secondary (Willison), satisfying the 8-source, 4-primary, 1-secondary floor.

The one intentional proof warning, W-CITE-DENSITY on the `tokens` step, is the
right call and I confirmed it rather than reversed it. The pretraining
contribution is the marked-open link; the prose says the direction is clear and
the size "not measured anywhere public," names it "the first open link in the
chain," and links the prior autoregressive-generation lesson in prose (which the
press rule forbids turning into a numbered source). A citation there would have to
be padded or fabricated. Kept as a real step without one.

Broken link found and fixed: source 9 (used only in the ground section for the
interactive-default and overridable claim) linked to
`model-spec.openai.com/2025-12-18.html`. I opened that page: the current edition
carries only a "Use Markdown with LaTeX extensions" guideline and does not contain
the interactive=true/false default or the "overridden by additional instructions"
wording the article quotes. That wording lives in the 2024-05-08 edition, which the
evidence record names as the document's own page; I opened it and confirmed it owns
the claim verbatim. This is a printed-address miscitation with the right source at
hand, so I re-pointed source 9 (and the Go deeper row that describes the same
overridable-default claim) to the 2024-05-08 edition. No prose or number changed;
the claim is now cited to the edition that supports it.

## Cut

A dedicated slop pass over body, display text, bookends, caption, and the note.
One sentence failed and was cut: "The gap is the headline, and a detail inside it
refines the claim." It carried no fact and graded the article's own emphasis
("is the headline"), signposting a nuance the next sentence delivers on its own;
the paragraph now opens on the entanglement figure and reads cleaner.

Edge sentences read alone: the openers and closers of the orientation, tokens,
imitation, preference, and ground sections each carry a fact or a settled/open
marking rather than leaning on neighbors. "Each leaves a different trace, and the
traces can be told apart" sets up the three-candidate structure the voice guide
endorses and states a real separability claim, so it stays. "That is ground" is the
series' concept marker, earned.

Negative-parallelism reflex, checked on each instance: "not because the question
demanded it," "substantially independent ... not wholly," and "not another
mechanism but a switch" each correct a real, named misconception (the reader's
folk theory, the assumption that formatting wins are content-free, the expectation
of a deeper mechanism at ground). None is a strawman; all stay. The
substantially/not-wholly line is the precision the brief mandates.

Prompt-leakage pass against the commission and both briefs: the orientation's
description of the behavior is the reader's situation reported as fact, not lifted
planning language. No self-grading, no "this lesson will show," no selection rules
in the body. Second person appears only in the two bookends, as the lesson template
allows.

Recent-pattern check against the desk notes: the piece does not use the "X is all
the system ever does" opener/closer or a single-mechanism "really just Y" reveal;
it holds the behavior to several marked stages throughout. The dek is built in the
piece's own nouns and is not a stamped mold (no semicolon reversal, suspended
question, or comma triad). The five section headings vary in construction and read
as argument steps a skimmer could reconstruct.

Furniture: the "What is settled, what is open" note is the documented note
component with a label naming the move it makes, and it earns its place by
collecting the chain's settled/open verdict in one spot. The chart is a real
data-drawn figure, not decoration. No component reads as filler.

## Reader

Read straight through as the paper's declared reader, what I have that the sources
alone would not give me: a single auditable chain from the visible bulleted answer
down to a steerable output policy, with each link honestly marked settled or open,
built out of eight separate measurements that individually say nothing about the
whole habit. That is exactly the original-work sentence in the draft handoff, and
it survives the read. The prose sits closer to the voice-guide exemplars than to a
median summary: it names the reader's likely wrong guess and lets it fail ("Being
able to format is not the same as defaulting to it"), holds each stage to what it
changes and leaves alone, and says plainly where the field has no number. The
headline as the largest claim is delivered by the ground section and the
now-correctly-cited Model Spec.

## Edits

- Re-pointed source 9 href from `model-spec.openai.com/2025-12-18.html` to `cdn.openai.com/spec/model-spec-2024-05-08.html`, the edition that owns the interactive-default and overridable-by-instruction claim the ground section cites.
- Re-pointed the Go deeper row 02 link to the same 2024-05-08 edition, so its description ("names markdown the default and makes it overridable") matches the page it links.
- Cut the sentence "The gap is the headline, and a detail inside it refines the claim." from the preference section (empty signpost grading the article's own emphasis).

## Required work

None. The one sourcing defect was a printed-address miscitation fixable with the
edition already named in the evidence record, so it was fixed directly rather than
routed. For the orchestrator's awareness only: source 9 and one Go deeper link now
point to the dated 2024-05-08 Model Spec edition instead of the 2025-12-18 page;
this is a corrected href, not new reporting, and needs nothing from the researcher
or writer.

## Decision

approve. The causal chain is honest and complete, the settled/open markings match
the evidence, the load-bearing length-vs-markdown precision is intact, and the one
citation defect was corrected against a source already in the record.
