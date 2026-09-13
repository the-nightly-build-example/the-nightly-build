# Editorial review: the-evidence/mamba (editor/01)

## Skeptic

Thesis: Mamba proved a narrow, solid thing — a model that carries a fixed
compressed state forward and chooses per token what to keep can match a
same-size transformer on short-context reasoning up to 2.8B and generate long
sequences more cheaply — and the popular "the transformer is finished" reading
outruns that by claiming parity on retrieval, long context, and frontier scale
the paper never tested. The article makes the case by splitting the single
famous "matches transformers" line into the two different claims it actually is,
then landing the boundary with the authors' own reintroduction of attention.

Claims it stands on, and how each held:

- **The mechanism: a fixed state updated per token, cost flat in length.**
  Matches the paper (Sec 2-3) and the evidence record. The two typeset
  equations are apparatus, not claims: the linear recurrence
  (h_t = A h_{t-1} + B x_t, y_t = C h_t) and the N=1 selective gate
  (h_t = g_t x_t + (1 - g_t) h_{t-1}) are both accurate to the source
  (the gate is Theorem 1 reordered), and the gate caption reads correctly —
  g near 1 overwrites, near 0 passes through. A no-code reader can follow both.
- **"Matches Transformers twice its size" is one narrow comparison.** Zero-shot
  common-sense reasoning: Mamba-2.8B 63.3 vs Pythia-2.8B 59.1, ahead of
  Pythia-6.9B's 61.7. Figures, the 2.8B ceiling, and the "3B rounded up" point
  all check against Table 3 and the record. The dek's "twice its size" is the
  paper's own rounded framing (the real edge was over a model ~2.46x larger, as
  the body says precisely); it does not misstate.
- **The throughput headline is setup-specific.** 4-5x is inference generation on
  one GPU from having no KV cache to hold, and the training scan only overtakes
  fast attention past ~2K tokens. Matches Sec 4.5 and the record; the article
  does not sell it as a blanket speedup.
- **The copying/retrieval gap (the round's focus).** The article draws it from
  Jelassi et al., which tests the original Mamba: ~100x more training examples
  to learn copying, and a 410M transformer beating a 2.8B Mamba at long
  phone-book lookup despite lower perplexity. It does not claim the gap is proven
  at frontier scale, and it keeps the sharpest primary (original Mamba) distinct
  from the more indirect Mamba-2/hybrid evidence that follows. Held.
- **The authors put attention back; industry did too.** Mamba-2's ~10%-attention
  hybrid beating both pure Mamba-2 and a strong transformer (Sec 9.2.3), and
  Jamba's "still lag behind" line, both verify.
- **Scale honesty and the counter-current.** The piece is honest that the
  headline results were small-to-mid scale, quotes the authors' own limitation,
  and gives Falcon Mamba (pure 7B beating Mistral 7B and Llama 3.1 8B on
  short-context leaderboards) a fair two-sentence hearing before marking that it
  is 7B, short-context, and does not touch the retrieval gap. Not a strawman.

Display text held descriptor by descriptor: headline, dek, and every subhead
carry claims the piece defends, with the actors and sizes correct. `data-nb-kind`
audits clean — the six arXiv papers are the documents that own their claims
(primary), and IBM Think is outside-party reporting (secondary). Every `href`
opens on its own source; I confirmed the seven land, and verified the IBM
secondary's two quotes verbatim and the copying-paper title and authors against
the live pages.

One break, fixed directly: the article attributed to IBM that "the practical
path forward ... is a hybrid," but IBM's own text hedges ("a hybrid model could
outperform," hybrids are "active research") while pointing to its production
Granite 4.0. I rewrote the sentence to what IBM actually says — it points to
hybrids, its own models included, as the way to pair Mamba's efficiency with
attention's recall — which the evidence record already supported and the piece's
own Jamba and Mamba-2 evidence independently carries.

## Cut

Seven sentences failed the slop test, all of one kind: signposts and
self-grading at section edges that reported where the argument stood without
doing any of its reasoning. Removed:

- Orientation's closer previewing what the next sections would examine.
- "It is worth pinning down" before the scale section's real work.
- "The bottleneck is where the argument turns," which described the article's
  own structure.
- "The strongest evidence is what the authors did next" — self-grading, and it
  miscast the record, which ranks the copying gap (not the authors' concession)
  as the strongest evidence.
- "There is a genuine counter-current, and it deserves a fair hearing," which
  announced the piece's fairness instead of showing it; the Falcon Mamba
  paragraph steelmans on its own.
- "So the precise reading is this" before the synthesis paragraph.

Two more: an unearned setup, "Set that beside attention and the difference is a
single word," where no single word is actually delivered and the following
parallel construction (attention re-reads every token / a state-space model
reads one thing) carries the contrast better without it. And a negative
parallelism, "Choosing what to keep, not any change to the surrounding block, is
what closed that gap," whose "not" clause corrects a foil the article never
raised for the reader; trimmed to the plain claim.

Recent-pattern check. The headline used the desk's recurring "did A, and
[reversal]" shape (the-evidence/t5, six days prior: "recast every language task
as text in, text out, and lost at translation"). I broke it to two beats —
"Mamba dropped attention to make long sequences cheap. Its authors put some
back." — keeping every word and both actors. The dek is a two-clause thesis
contrast, not the flagged "A [noun], whose [twist]" mold, the author-and-year
opener, or a three-clause comma triad, so it stands. Section headings are the
document's own steps; I retitled "Reading the scale honestly" to "The 2.8B
behind the headline" — the old one graded the article's own honesty and faintly
echoed the commission's "show the scale honestly," and the new one names the
section's step in the piece's nouns.

No prompt leakage survives: the one brief-phrase echo ("genuine counter-current")
sat in a sentence I cut for other reasons. No borrowed phrasing from the
voice-guide exemplars; the Olah-style parallel construction the piece uses is the
technique the guide invites, not its words. Grammar and punctuation are clean —
no em-dashes, semicolons only on tightly bound contrasts, colons introducing what
they promise.

## Reader

What the reader has that the sources alone would not give: a single axis on which
Mamba's scattered results line up, and the exact point where the "transformers
are finished" story breaks — that "matches on perplexity" and "matches on the
task you'd use it for" are different claims, and the paper only earned the first.
That answer survives, and it matches the draft-handoff's original-work sentence.
The piece teaches rather than restates its sources. The prose sits closer to the
voice-guide exemplars than to a median summary: plain parallel contrasts, limits
named in the same breath as the mechanism, and a gate taught with a real
equation in ordinary words. The retitled headline is a claim the piece defends
end to end.

On the writer's open note: no source asset was captured for the copying gap. I
judge a visual is not required. The claim is carried by concrete, checkable
numbers in prose (100x fewer examples; a 410M transformer beating a 2.8B Mamba
at long lookup; the gap holding despite lower perplexity), and a benchmark
figure would push the lesson past the depth a no-code reader needs. Prose carries
it. No asset requested.

## Edits

- Headline (in `<title>`, nb-meta `title`, and `<h1>`): split the ", and"
  reversal into two sentences to break the recent T5 headline mold.
- Cut orientation's closing method-preview sentence.
- "Set that beside attention and the difference is a single word." -> "Set that
  beside attention."
- "Choosing what to keep, not any change to the surrounding block, is what
  closed that gap." -> "Choosing what to keep is what closed that gap."
- Cut "It is worth pinning down." from the scale section.
- Retitled section "Reading the scale honestly" -> "The 2.8B behind the
  headline"; updated `data-nb-section` and `id` to `behind-the-headline`.
- Cut "The bottleneck is where the argument turns."
- Cut "The strongest evidence is what the authors did next."
- Cut "There is a genuine counter-current, and it deserves a fair hearing."
- Cut "So the precise reading is this."
- Softened the IBM sentence "The practical path forward, it says, is a hybrid."
  to match what the secondary states ("It points to hybrids, its own production
  models among them, as the way to pair Mamba's efficiency with attention's
  recall.").

## Required work

None. No evidence gap, no broken central claim, and no source-policy failure
remains for the researcher or writer. Word count dropped by roughly seventy words
from the cuts and stays inside the band; the orchestrator's stamp recomputes the
count and reading time.

## Decision

Approve. The claims hold against the primaries, the scale and the copying gap are
weighed honestly, and the edits above resolved the slop and the one directional
overstatement directly.
