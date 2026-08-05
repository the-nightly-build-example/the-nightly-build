# Editorial review: the-instruments/parameter-count (editor/01)

## Skeptic

Thesis: a parameter count is an exact tally of a model's frozen weights, but on
a mixture-of-experts model that single number splits into two costs the sources
only ever state apart. The total is the memory that must stay resident; the
active-per-token count is the compute and speed. Neither, on its own, predicts
capability.

Load-bearing claims and how each held:

- **GPT-3 is 175B and dense (all parameters active per token).** Matches the
  evidence Numbers section and Brown et al. (s1). The article's gloss of
  "non-sparse" as "dense" is faithful to the source quote. Holds.
- **Mixtral is 46.7B total / 12.9B active, and 8x7 is not 56.** Both figures are
  Mistral's own (s5), correctly attributed; the "not 56B" reasoning is the shared
  attention/embeddings/norms argument, sourced to Lambert (s6) and consistent with
  the evidence record. The paper/HF-card rounding to 47B/13B is disclosed and
  correctly labeled as the same number rounded (s7, s8). Holds.
- **DeepSeek-V3 is 671B total / 37B active.** Matches the technical report (s9)
  and the Numbers section. "About one part in eighteen" (671/37 = 18.1) and the
  "near four times" GPT-3 comparison (671/175 = 3.83) are honest arithmetic.
  Holds.
- **Chinchilla: ~70B beat ~280B Gopher at equal compute.** Matches Hoffmann et
  al. (s2). Critically, the draft states the finding correctly: "not that
  parameters had stopped mattering" but that count and training budget must scale
  together. This is the first of the two overclaims the brief flagged, and the
  draft honors it. It does not drift into "parameters tell you nothing." Holds.

The harder overclaim — **active tracks compute/speed but NOT memory** — is the
one I pushed hardest on, because the commission's angle invites the error. The
draft handles it cleanly. The section "The total is still the memory bill"
establishes that every parameter must sit in accelerator memory before a token
arrives ("the router may send the next token to any expert"), states the total
is "the honest number" on memory, and only then flips to per-token compute. The
takeaway holds the pair in balance: "The total is the memory the model needs.
The active count is the speed and compute each token costs." No sentence calls
active "the real cost." Holds.

Display text, descriptor by descriptor: the headline states two true figures
(671 lists, 37 runs) with the actor named — legitimate under the headline
standard's "numbers earn their spot when they are the story," and not a colon
subtitle. The dek makes a claim about the world, not a grade of the article's
method. Every subhead is a real step of the argument in the piece's own nouns.
No false label found.

`data-nb-kind` audit: s1-s5, s7-s9 primary, s6 (Lambert/Interconnects)
secondary. Every label matches the evidence record; Lambert is correctly the
lone secondary as an independent analyst, not a party to Mixtral. 8 primary / 1
secondary, floor met. Every `href` matches the verified URL in the evidence
record and lands on the source itself (arXiv abstract pages, the Mistral
announcement, the DeepSeek report, the two model cards, the Interconnects post);
`nb check` with links previously returned BLOCK: 0.

## Chart

Provenance (`chart-1.py`) reads every figure off the owning primary and matches
the Numbers section exactly: GPT-3 175/175, Mixtral 46.7/12.9, DeepSeek-V3
671/37. Read as a reader, the rendered `chart-1.png` is honest: a single linear
y-axis labeled "Parameters (billions)" from 0, no truncation, a legend
distinguishing total from active, and active-fraction labels (100% / 28% / 5.5%)
that are correct arithmetic on the primary figures. GPT-3's two equal bars
correctly show a dense model runs 100% of itself. The caption is a factual cited
label. No correction needed.

## Cut

The prose sits in the measurement-explainer register the voice guide asks for:
it names the counted objects (attention and feed-forward blocks, the embedding
table) before arguing from the number, works the misleading 8x7 sum in the open
against the correct 46.7, and isolates activation as the single moving variable
across the three-model comparison. No prompt leakage: the two overclaim cautions
from the writer brief are taught in original prose, with no planning labels,
selection rules, or "this article fulfilled its assignment" claims carried over.

Recent-pattern check (the round's focus): the recent the-instruments deks lean
on the "same X, two numbers" matched-pair reversal ("both are true"; "0.3 vs
2.9"; "scored X and Y, only the compute changed"). This dek does not stage that
snap — it defines the count, then generalizes the MoE gap, as one continuous
claim rather than two numbers set in apposition and reversed. It clears the mold.
Heading cadence is varied; none joins two clauses with a comma and "and," the
specific tic the brief warned about. No recurrence to break.

Furniture: no Verdict-style restatement block closes the body — the takeaway
lands judgment in prose, as the press requires. Background rows (training-compute,
Chinchilla) and Go-deeper rows (Lambert, Switch Transformers) are each a link and
one honest line, and the lesson works for a reader who opens none of them.

Hedged contrasts stay within the ceiling and each corrects a real, named
misconception (the 56B sum, "parameters stopped mattering"). No self-narration.

One furniture defect, recorded as required work below: the header byline still
reads the initialization placeholder "N min read" rather than the stamped reading
time. It is markup, so I did not edit it directly.

No direct prose cuts were warranted; the draft is already tight and the writer's
proof left no warnings.

## Reader

Read straight through as the paper's smart, code-free reader, the piece hands
over something the sources do not: a way to read any "N billion parameters" claim
by asking whether all N run and what the total-versus-active gap means for memory
versus speed. No single primary juxtaposes GPT-3, Mixtral, and DeepSeek-V3 on
total-and-active in one frame, nor splits the one count into a memory cost and a
compute cost; the draft-handoff's original-work sentence claims exactly that
juxtaposition, and the article delivers it. The prose reads closer to the
voice-guide exemplars (Harford, Eadicicco, the clock-speed writers) than to a
median AI summary: it slows down to count, and does the misleading arithmetic
where the reader can see the step. The headline, reread as the largest claim,
commits to a finding the body defends.

## Edits

None. No surgical cut or prose fix was warranted; the one defect found is markup
and routes to the writer.

## Required work

- **writer** — Replace the header byline placeholder `N min read` (article line
  46) with `7 min read`, matching `nb-meta` `reading_minutes: 7`. Nothing
  downstream fills it: `nb stamp` reports "already stamped" without touching the
  byline, `nb.js` `normalizeByline` leaves any "min read" span untouched, and
  `nb check` passes it as PUBLISHABLE. Every published the-instruments article
  bakes the real number, so the placeholder would ship visibly on the page.

## Decision

revise — the article is editorially sound and every focus check passes, but the
reader-facing byline would publish the literal "N min read" placeholder, which no
downstream step corrects; the writer must set it to 7.
