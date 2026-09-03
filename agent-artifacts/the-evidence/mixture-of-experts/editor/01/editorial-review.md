# Editorial review: the-evidence/mixture-of-experts (editor/01)

## Skeptic

Thesis: a modern MoE model's advertised parameter count (the total store) is a
different quantity from the parameters that actually run for any single token
(the active slice), and the 2017 sparsely-gated mixture-of-experts layer is
where those two came apart.

The claims it stands on, and how each held:

- The 2017 decoupling figure: one model held 4.3 billion parameters yet spent
  8.9 million operations per timestep, beating the prior best (151 M parameters,
  151 M ops, higher perplexity). Checked against the evidence record (Table 1,
  MoE-4096-h) and recomputed: 4.3 B / 151 M is roughly 28x parameters, 151 M /
  8.9 M is about 17x fewer ops. Both multipliers as printed are correct. The
  table's three rows (151 M / 151 M / 34.7; 4.3 B / 8.9 M / 34.1; 4.4 B /
  142.7 M / 28.0) each match the record cell for cell.
- The Switch scale claim: 1.571 trillion parameters at 890 billion FLOPs/seq,
  below a dense 11-billion model's 6.3 trillion. Matches the record's reading of
  Table 9 (Switch-C vs T5-XXL). 1571 / 11 is about 143x, as printed.
- Mixtral 47 B total / 13 B active. I opened the primary abstract: the sentence
  "each token has access to 47B parameters, but only uses 13B active parameters
  during inference" is exact. The 8x7B-is-not-56B reasoning and the
  FFN-only-are-experts point are carried by the Hugging Face secondary, which I
  opened and confirmed word for word. The piece correctly uses the paper's own
  47/13 rounding rather than the finer 46.7/12.9 the record flags.
- DeepSeekMoE 16.4 B total / 2.8 B active, 2 shared + 6-of-64 routed. Matches the
  record (Section 5.1.2). The primary's abstract confirms the 16B model and the
  ~40% compute claim; the finer split is the researcher's Section 5.1.2 reading,
  consistent with every other figure of theirs that verified.
- The routing dispute: Shazeer k=4, GShard top-2, Switch top-1, with Shazeer an
  author on Switch. Matches the record's contradiction entry. The Switch quote
  "we route to only a single expert" is the record's and the paper's.

Display text, descriptor by descriptor: headline ("Google's 2017 layer") — the
authors are Google Brain, submitted January 2017, seven authors including Hinton
and Dean, all confirmed against the primary. Dek (Shazeer's team, a few experts
of thousands, Mixtral 47/13) — every element sourced. Subheads each state a real
step in the piece's own nouns.

data-nb-kind audit: five primaries (each owns its own model and figures) and one
secondary (HF, a third-party summary) — correct labels, and source obligations
met (6 sources, 5 primary, 1 secondary).

Citations: I opened all six hrefs. Every one resolves to the document it claims
(1701.06538 Shazeer, 2101.03961 Switch, 2401.04088 Mixtral, 2401.06066
DeepSeekMoE, 2006.16668 GShard, huggingface.co/blog/moe). No endpoint stand-ins.

Focus items cleared: GShard's flagged BLEU is not quoted; the synthesized
"36,684 experts" figure the record discarded does not appear; no record-flagged
unverified figure is stated as fact.

One break, fixed in place: the sentence "GShard added a hard cap on how many
tokens one expert may accept" carried no citation, though the record documents it
(GShard Section 2.2) and GShard is already source #s6. I attached that citation.
No claim, number, or name was changed.

## Cut

Two prose failures, both fixed directly.

- Slop tell (unearned punchline): "A modern model usually reports two parameter
  counts instead, and the distance between them is the whole point." The "X is
  the whole point" construction grades the argument instead of continuing it, and
  the sentences after it already define both counts and show the gap. Cut the
  flourish clause; nothing was lost.
- Signpost plus redundant negative parallelism: the one-expert section opened
  "The primaries here do not fully agree ... and the disagreement is worth seeing
  because it is the field correcting itself, not an outsider's objection." This
  announced the reading before showing the evidence, and the same "self-correction,
  not outside critique" point is delivered earned at the section's end, backed by
  the fact that Shazeer co-authored Switch. I trimmed the opener to the plain fact
  ("The primaries do not agree on how many experts a token should visit") and let
  the earned version at the section end carry the interpretation. This also
  strengthens the round's focus that the dispute read as self-revision, not a
  strawman contrast.

Edges walked on their own: the section closers each land a real conclusion the
argument built ("Size and cost ... had come apart"; "the giant is the cheaper
one"; "measures the store, not the work"; "managing rather than a matter it had
closed"). None is a signpost. The article's last sentence, "Only the smaller one
is what a token pays," carries the lesson's core fact and stays.

Remaining negative-parallelism instances judged earned and kept: "not marketing
but the design choice it is" (opener), "the tell that this was a field revising
its own earlier guess rather than a rival scoring a point," and the takeaway's
"not how big it is but how much of itself it runs" — each corrects a misconception
the piece names and defends (the big number read as hype; a between-papers dispute
read as outside critique; the total read as the operative number).

Leakage: no brief or commission phrasing survives. The opener avoids the banned
"This lesson opens/reads" mold and the "By the end you will explain X, Y and Z"
list. Headings vary in construction (declarative, how-, what-, narrative) rather
than defaulting to one reveal mold, and the last body section does not close on a
stamped present-tense one-liner. No overlap with the evaluation-metric framing of
the sibling instruments pieces.

Furniture: stat strip, one annotated equation, and the reproduced Table 1 — each
carries the mechanism or the decoupling and each is cited in nearby prose. The
optional Shazeer Figure 1 routing diagram is not needed: the annotated equation
and prose carry the mechanism, and the claim a reader must test (the total-vs-active
gap) is carried by the table and stat strip. Not requested.

## Reader

Read straight through as the paper's declared reader (smart, widely read, new to
neural-network architecture): I come away able to say that an MoE model's
advertised parameter count measures the store it owns, not the work a token does,
and that this gap is a deliberate 2017 design choice now standard in shipped
models — with the numbers pinned to their denominators (4.3 B at 8.9 M ops;
1.571 T at 890 B FLOPs; 47/13; 16.4/2.8). No single source hands that over
assembled. It matches the draft-handoff's original-work sentence, which claims to
thread one honesty test through five primaries and stage the routing dispute as
self-correction; the article delivers both. The prose sits closer to the
voice-guide exemplars than to a median summary: concrete before abstract, the
denominator fixed in the Luu manner ("measures the store, not the work"), the
correction kept even ("None of this makes the larger number a lie"), and the open
problem admitted plainly ("managing rather than a matter it had closed"). The
headline holds as the largest claim.

## Edits

- Cut "and the distance between them is the whole point" from the counting-parameters opener (slop: "X is the whole point").
- Rewrote the one-expert section opener to "The primaries do not agree on how many experts a token should visit," dropping the signpost and the redundant "field correcting itself, not an outsider's objection" framing (delivered earned at the section's end).
- Added the missing citation on "GShard added a hard cap on how many tokens one expert may accept" (#s6, Section 2.2).

## Required work

None. No researcher, writer, or orchestrator item blocks publication. The
orchestrator stamps and re-checks after these edits per the brief; the edits are
prose trims and one citation addition and demand no new reporting.

## Decision

approve — the spine (total-vs-active honesty) is sound, every parameter and
compute figure verifies against its owning primary, all six citations resolve,
and the two prose failures and one citation gap I found were fixable in place.
