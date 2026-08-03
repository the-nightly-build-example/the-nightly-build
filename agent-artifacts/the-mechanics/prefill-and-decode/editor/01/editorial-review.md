# Editorial review: the-mechanics/prefill-and-decode (editor/01)

## Skeptic

Thesis: a chatbot reads the whole prompt in one parallel pass (prefill,
compute-bound) but writes its reply one token at a time (decode,
memory-bandwidth-bound), the KV cache is the step between them, and the felt
cost runs backward from intuition: the long prompt is cheap, the short reply
is expensive.

Load-bearing claims and how each held:

- **Prefill is compute-bound and scales with prompt length.** Held. Grounded
  in FlashAttention's own bound definition (s3) and DistServe's 512-token/A100
  threshold (s4, Section 2.1). The magnitude carries its conditions
  (13B-class model, A100) and the following sentence names the cause of its
  variance ("depends on the model and the GPU, but the direction does not").
- **Decode is memory-bandwidth-bound because each step rereads the whole
  cache.** Held. Splitwise (s6) and DistServe both state decode incurs
  prefill-level I/O for a single token; the bound definition is s3's. Direction
  is stated flatly, correctly, as settled.
- **The KV cache is the cause, not an optional speed trick.** Held and pinned
  to vLLM (s2, Section 3): 800 KB/token for OPT-13B and up to 1.6 GB for a
  2,048-token sequence, both labeled FP16/model-specific. Arithmetic checks:
  2 x 5120 x 40 x 2 bytes x 2 = 819,200 bytes ~= 800 KB; 800 KB x 2048 ~= 1.6 GB.
  Internally consistent.
- **The cost inversion (short reply dearer than long prompt).** This is the one
  I pushed hardest on, because it is the lesson's news. It rests on
  Sarathi-Serve's linear-operator figure: one decode token ~= 128 prefill
  tokens (s8, Section 3.2), Mistral-7B on one A100. The article carries those
  conditions and hedges the ratio while keeping the asymmetry general. The
  claim survives even when reply length is far shorter than prompt length,
  because the per-token gap swamps the token-count gap. It holds.
- **The frontier is unsettled.** Held and correctly bounded: the mechanism is
  marked settled, only the hardware organization (disaggregation via
  Splitwise/DistServe vs fusion via Sarathi-Serve chunked prefill) is marked
  live. Presented as primary-vs-primary, not smoothed to one winner.

Display text audited descriptor by descriptor. Headline and dek make
world-claims, not method grades. No named person appears in headline, dek, or
subheads. Author attributions in the source list and Go-deeper rows
(Kwon/Dao/Zhong/Vaswani/Patel/Agrawal) each match the evidence record's owners.
The two Background link titles were checked against the actual published lessons
in the library and match exactly ("An attention head is a weighted average that
computes its own weights"; "The instant a model writes a token, it becomes
fact").

`data-nb-kind` audit: seven primaries (NVIDIA NIM, vLLM, FlashAttention,
DistServe, Attention Is All You Need, Splitwise, Sarathi-Serve) and one
secondary (Databricks). Every label matches the evidence record; the one
secondary is used only for the practitioner-framing sentence, never to carry a
mechanism claim. No independent-source gap is hidden by a mislabel.

Citation hrefs: every href resolved under the links-included check, and each
arXiv id maps to the paper it claims (1706.03762 Attention; 2205.14135
FlashAttention; 2309.06180 PagedAttention; 2401.09670 DistServe; 2311.18677
Splitwise; 2403.02310 Sarathi-Serve). The three `data-nb-locator` values
(DistServe 2.1, vLLM 3, Sarathi-Serve 3.2) each point at the section the
evidence assigns. No miscitation found; nothing routed from this read.

One note, not a break: the dek foregrounds "rereading the prompt's cached keys
and values" as the cost cause, while the body's 128:1 cost figure is driven by
per-token weight reloading. Both are real memory costs of decode, the cache is
this lesson's deliberate spine, and the dek is not false, so I left it.

## Cut

Three direct changes, all subtractive.

- Cut the orientation section's closing sentence ("The rest of this lesson
  works backward... and ends at the one part the people who build these systems
  still argue about"). It was a signpost describing the piece's own structure
  and a premature preview of the frontier, both of which the standard bans. The
  paragraph now lands on the decode mechanism, and the backward-working
  structure is enacted rather than announced.
- Cut "As one illustrative point," before the DistServe figure. It was a
  generic throat-clearing frame layered on top of the sentence that already
  names the variance's cause ("depends on the model and the GPU"). Removing it
  makes the 512-token figure's hedge consistent with the other magnitudes,
  which each carry a named-cause hedge and no generic frame. The illustrative
  reading is fully preserved.
- Changed a semicolon to a period between "...the word just written" and "This
  is the sequential generation the autoregressive-generation lesson covers."
  The second clause is a labeling handoff, not a tight antithesis, so the
  period is the plainer correct mark.

Worst tell found: the structural signpost above. No repeated rhetorical shape
across paragraph endings, deks, or headings; endings vary and none use the
comma-and cadence the recent-pattern notes flag. No prompt leakage: the word
"illustrative" earlier in the draft was doing real hedging work, not echoing a
planning label, and I removed the one instance that was redundant. The
pre-empt note ("The step an explanation skips") and the two-phase table both
earn their place as deliberate emphasis the series prompt calls for; neither is
a stacked-block formula. No furniture cut.

## Reader

Read straight through as the paper's declared reader, the numbers are the
mapping of the felt pause-then-stream onto prefill, the cache, and decode, plus
the single inversion no source states outright: the long prompt is the cheap
part and the short reply is the slow, expensive one. That answer survives, and
it matches the draft-handoff's original-work sentence. The prose sits closer to
the voice-guide exemplars than a median summary: each mechanism is grounded in
a duration the reader sat through before it is named (the pause "scales with
how much you typed. ... That is because prefill does work in proportion to the
prompt"), and variance is marked by naming its cause rather than hedging. The
headline, reread as the largest claim, is fully defended by the body.

## Edits

- Cut orientation signpost sentence ("The rest of this lesson works backward... still argue about").
- Cut "As one illustrative point," before the DistServe 512-token figure.
- Changed semicolon to period between "...the word just written" and "This is the sequential generation...".
- Ran `./nb stamp`; words re-stamped 2077 -> 2037, reading_minutes 9, sources 8.

## Required work

- **writer (markup):** The byline prints the unfilled placeholder
  `<span>N min read</span>` (line 44). `nb stamp` updates only nb-meta and does
  not touch the byline, and `nb.js` `normalizeByline()` skips any span that
  already contains "min read", so the rendered page shows the literal
  "N min read" to the reader. Every published sibling shows the real figure
  (e.g. "9 min read"). Fill it to "9 min read" to match nb-meta
  `reading_minutes` and the sibling convention. This is display text, so it is
  the most visible error the page carries; it is the writer's because the editor
  does not touch markup.

## Decision

revise — the article's argument, sourcing, numbers, and frontier framing are
sound and the proof is clean, but the byline ships an unfilled "N min read"
placeholder in visible display text that only the writer can correct in markup.
