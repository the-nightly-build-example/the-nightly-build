# Editorial review: the-evidence/backpropagation (editor/01)

## Skeptic

Thesis: the 1986 Nature backpropagation paper's lasting contribution was not the
backward-gradient algorithm, which was already in print, but the demonstration,
on tiny legible networks, that a weight-update rule makes hidden units build
useful features nobody designed; and the paper is misremembered on two counts,
who invented the algorithm and whether later work proved it wrong about local
minima.

The claims it stands on, and how each held:

- **The backward-derivative operation predates 1986 (Linnainmaa, Werbos).**
  Held. The Linnainmaa quote ("is the partial derivative") and the Werbos quote
  ("a technique for calculating derivatives inexpensively, for use with the
  classic method of steepest descent") match the evidence record, and the
  article correctly limits each: Linnainmaa framed it as rounding error and
  "never mentioned neural networks," Werbos "framed it for fitting statistical
  models and named brains only as an analogy."

- **The 1986 authors did not claim sole invention; the miscrediting lives in
  later popular memory, not the paper.** Held, and this was the round's central
  test. I opened the Nature facsimile (p.535) and confirmed the verbatim credit:
  "Variants on the learning procedure have been discovered independently by David
  Parker (personal communication) and by Yann Le Cun." The article states the
  gap precisely ("What they did not do was cite Werbos or Linnainmaa") and
  attributes it to those predecessors sitting in other fields, not to theft. The
  draft never accuses the paper of claiming what it did not. This matches the
  brief's required framing exactly.

- **The real contribution: hidden units come to represent task features,
  demonstrated on the family-tree net.** Held, verified against the primary.
  Nature Fig. 4 caption (p.535): "Unit 1 is primarily concerned with the
  distinction between English and Italian... Unit 2 encodes which generation a
  person belongs to, and unit 6 encodes which branch of the family they come
  from." The in-article figure caption's unit-number mapping is exactly right.
  The family-tree "Colin / has-aunt / two aunts" example is also verbatim from
  the primary (Fig. 3 caption, p.534: "one active unit... representing Colin and
  one... representing the relationship 'has-aunt'... two correct answers...
  because Colin has two aunts"). Neither of these two specifics is itemized in
  the evidence record's Numbers block, so I verified them directly against the
  cited facsimile rather than take them on trust; both are correct. Not a gap
  that needs routing, but the record's paraphrase could carry them for future
  traceability.

- **The demonstrations were small, measured in sweeps not compute.** Held. 6-2-1
  symmetry net, 1,425 sweeps over 64 patterns, 1:2:4 weight ratio (Nature Fig. 1,
  verified); 36-input five-layer family-tree net, 1,500 sweeps, 100 of 104
  triples (verified); XOR in 558 sweeps, 4-bit parity in 2,825 presentations,
  8-3-8 encoder (evidence record, PDP chapter). Every table cell checks against
  the record. The article correctly builds scale from counts and states plainly
  that the papers give no hardware or wall-clock figure, exactly as the brief
  required; it invents no compute anchor.

- **Dauphin 2014 corrects the local-minima explanation to saddle points while
  confirming the observation.** Held at the required precision. The article says
  "That result corrects the paper's explanation while confirming its
  observation," which is the evidence record's exact reading. The Rumelhart
  local-minima and "not a plausible model of learning in brains" quotes are
  verified against Nature p.535-536; the "irrelevant in a wide variety of
  learning tasks" quote is the PDP chapter's. "Twenty-eight years later" (1986 to
  2014) checks.

Display text: headline states the finding in the piece's own nouns and is
supported. Dek adds the demonstration's nature and the priority fact without
restating the headline, and makes two checkable claims about the world rather
than grading the article's method. Affiliations are correct and the article
avoids the evidence record's flagged "Philadelphia" typo trap, placing Hinton at
Carnegie-Mellon. Every section heading is a concrete step of the argument.

`data-nb-kind` audit: s1, s2 (both by the authoring party), s3 (Linnainmaa), s4
(Werbos), s6 (Dauphin) are correctly primary; s5 (Schmidhuber) is correctly
secondary, and the article discloses his stake ("read him as an advocate"),
which the evidence record demands. Source set is at the floor: 6 sources, 5
primary, 1 secondary, all cited in first-citation order (s1 orientation, s2
hidden-units, s3/s4/s5 priority, s6 limits).

Citations: I opened every source href as printed. All six resolve to the source
itself (each returned the actual document; the four scanned facsimiles are
image-compressed, so I rendered the Nature PDF to confirm content). The Nature,
PDP, and Linnainmaa entries link the open facsimiles the writer read, with the
publisher of record named in the entry text, as the handoff describes. The two
figure `data-nb-url` anchors (#page=3 for Nature p.535 Fig. 4; #page=2 for Nature
p.534 Fig. 1) and their `data-nb-locator` labels are both correct. No broken
link, no miscitation, nothing that would fail the links proof.

No claim broke. Nothing routed to the researcher or writer.

## Cut

The draft was already clean; the reporting is dense and the nouns carry the
sentences. Five sentences failed the slop or template test and were fixed:

- One empty-conclusion opener in the takeaway ("...it is a particular kind of
  importance") that reduced to a fully generic sentence. Rewritten to name the
  kind of importance concretely (demonstration, not invention), which is the
  piece's actual thesis.
- One performed-carefulness signpost in the scale section ("The honest measure
  of scale is those counts"), a self-grading line whose content the two prior
  sentences already carried. Cut.
- One self-grading hinge in the priority section ("That is the right division")
  sitting in front of the concrete three-way ownership sentence that does the
  reasoning. Cut.
- One duplicated clause in the takeaway ("credited the contemporaries it knew
  of," already stated two sentences earlier). Cut from the closer.
- One copula softened to a verb ("the family-tree units are what they can do" ->
  "show what they can do").

One template-conformance fix, separate from slop: the body opened its second
orientation paragraph with "You have already met the step..." — a second-person
address to the reader inside the body, which the lesson template reserves for the
two bookends ("the body speaks to no one"), and which also duplicated the Why
bookend's "You have already seen the step." Recast to third person, keeping the
gradient-descent link the press voice wants at first use.

No repeated formula against the recent-pattern notes: the body does not run a
single myth-versus-reality block, splitting the two corrections into distinct
concrete sections (priority; local minima), and the closer reframes on the kind
of importance rather than the flagged "did not become the field's choice" mold.
The dek is a two-clause "and" construction leading with the concrete surprise,
not the flagged "everyone remembers X, but actually Y" mold or a comma triad.
Em-dash count is zero (against a max of four); no banned term appears in the
rendered text (machinery, transformative, leverage, load-bearing and the rest
are all absent). Punctuation is plain throughout; the two semicolons join tightly
parallel clauses and hold.

## Reader

Read straight through as the paper's declared reader, someone smart with no time
in a codebase: what I have that the four dense papers and one partisan web page
would not give me is the ability to tell this famous document apart from the
legend. I can say what it actually demonstrated (hidden units building their own
features, made concrete by six units that recovered nationality, generation, and
branch from a list of relatives), that the algorithm predated it and the authors
credited the contemporaries they knew of, how small the demonstrations were
(a symmetry net whose every weight prints on a page), and that the local-minima
worry was later vindicated and reframed rather than refuted. The writer's
original-work sentence — that the article is where the priority split and the
observation-versus-explanation reading become one thing a general reader can
carry — survives. The prose sits closer to the voice-guide exemplars than to a
median summary: it uses Wilczek's pose-and-answer on the priority and
local-minima questions, Lee's pairing of a moment of notice with the exact
evidence (named papers, figure numbers, exact sweep counts), and keeps the
paper's vocabulary intact. The headline holds as the largest claim.

## Edits

- Orientation: recast "You have already met the step at the center of that
  procedure. Training moves each weight..." to "The step at the center of that
  procedure appeared already, in gradient descent: training moves each
  weight...", removing body reader-address and the duplication of the Why
  bookend while keeping the gradient-descent link.
- Hidden-units: "and the family-tree units are what they can do" -> "and the
  family-tree units show what they can do."
- Scale: cut "The honest measure of scale is those counts."
- Priority: cut "That is the right division."
- Takeaway: "So the paper's importance is real, and it is a particular kind of
  importance." -> "The paper's importance is real, and it is a matter of
  demonstration, not invention."
- Takeaway: "It inherited the algorithm, credited the contemporaries it knew of,
  and earned its place by showing what the algorithm could build." -> "It
  inherited the algorithm and earned its place by showing what the algorithm
  could build."

## Visual evidence

Two source assets, both inspected as evidence, not decoration.

- asset-1 (in-article Fig. 1 = Nature Fig. 4, p.535): the grid of weight
  rectangles for the six hidden units, columns labeled with the people's names,
  units numbered 1-6. The crop retains exactly what the argument spends — the
  per-unit feature patterns and the labels that let a reader see which unit is
  which — and omits page furniture. The caption is a factual cited label and its
  unit-number-to-feature mapping matches the primary. Correct, no recrop.
- asset-2 (in-article Fig. 2 = Nature Fig. 1, p.534): the fully labeled symmetry
  network. The crop retains every numeric weight and bias (the argument is the
  exact numbers and the 1:2:4 ratio), which the caption cites. Correct, no
  recrop.

No chart in the article, so no chart provenance to audit.

## Required work

None. All edits were the editor's to make directly; no evidence gap, no
reporting, no asset recrop, and no missing commission context. The changes are
prose-only and touch no href, number, name, date, or quotation, so the links
proof is unaffected. Non-blocking note for the orchestrator: the word count drops
by a handful of words from the stamped 2141 (still inside the 1200-2200 band),
so the re-stamp will land slightly lower.

## Decision

approve — the article is accurate against the primaries on both the priority and
local-minima framings the brief flagged, the assets carry their arguments, and
the remaining prose failures were fixed in place.
