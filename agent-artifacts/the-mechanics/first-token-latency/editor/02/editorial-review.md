# Editorial review: the-mechanics/first-token-latency (editor/02)

## Skeptic

This is the confirmation read on the two source-fidelity items I routed in
editor/01, plus the threshold and quote items the writer folded in. The thesis
is unchanged and unchallenged here: the pause before a chatbot's first word
barely tracks prompt length at the lengths people type, and any published TTFT
is a sum of four separable costs. I did not relitigate the claims that already
held in round 01. I checked the four repairs.

**Feed-forward/projection term now attributed to Kaplan, Vaswani stated for what
Table 1 holds.** In editor/01 the crossover argument sourced the linear
O(n·d²) feed-forward and projection cost to Vaswani's Table 1, which contains no
such row. The recast paragraph now says Vaswani's Table 1 gives self-attention
at O(n²·d) and sets it against a recurrent layer at O(n·d²), with no
feed-forward row, and attributes the linear per-token cost to Kaplan et al.'s
per-token FLOP table. I opened Kaplan et al. (arXiv 2001.08361), Section 2.1 and
Table 1, to confirm the substitution rather than take the record's word for it.
The table gives the feed-forward block at 2·n_layer·2·d_model·d_ff per token and
the query/key/value projections at 2·n_layer·d_model·3·d_attn per token, both
independent of context length; only the attention-score row carries n_ctx. The
article's "each cost on the order of d² per token, with no context length in
them" is faithful to what the table shows, and "Only the attention-score term
carries n" matches the one context-bearing row. Vaswani's
self-attention-versus-recurrent sentence is no longer repurposed as an
attention-versus-feed-forward claim. Fixed and confirmed.

**Crossover threshold reconciled with d > n/12.** The prose now rests the
crossover on Kaplan's constant-aware condition: the context-dependent cost stays
a small fraction of the total while d > n/12, which for a representation
dimension of a few thousand puts the crossover in the tens of thousands of
tokens. I confirmed the condition verbatim in the paper: "For contexts and
models with d_model > n_ctx/12, the context-dependent computational cost per
token is a relatively small fraction of the total compute." The round-01 wording
pegged the crossover at "several thousand tokens"; it now reads "tens of
thousands" in the prompt-length section and agrees with the long-context
section's "Past a few tens of thousands." Prose and source now agree, and the
two sections no longer contradict each other on the number. Fixed and confirmed.

**Network-latency claim rests on Artificial Analysis, not Anthropic.** The
unsupported Anthropic clause is gone. The network sentence in the prefix-cache
section now attributes the point solely to Artificial Analysis, quoting two
verbatim fragments of its methodology sentence: "TTFT is sensitive to server
location" and "includes network latency." I opened the Artificial Analysis
methodology page and confirmed the source sentence reads "Time-to-first-token
(TTFT) is sensitive to server location as it includes network latency," measured
from a us-central1-a Google Cloud VM. Both quoted fragments are faithful to the
source; the connecting "and" is the article's, and each fragment stands verbatim
on its own. Fixed and confirmed. The Anthropic reduce-latency page is now cited
in orientation only for its own TTFT definition (source 2), which the evidence
record supports; it no longer carries any network claim.

**Together AI TTFT string de-quoted.** The orientation now paraphrases Together
AI's definition ("the wait between sending a request and the first word of the
reply appearing") without quotation marks, so the contested verbatim string is
gone. The paraphrase is faithful to the source's meaning as the record states
it. Resolved.

New Kaplan citation, kind and href: source 5 is labeled data-nb-kind="primary",
which is correct under the primary/secondary test, since Kaplan et al. is the
paper that derives the per-token FLOP accounting and therefore owns that claim.
The href, https://arxiv.org/abs/2001.08361, lands on the paper's own page; it is
the paper whose Table 1 I read to confirm the term. The in-prose attribution
("Kaplan et al.'s per-token FLOP table", "Kaplan also fixes the point") names the
owner directly. Source count is now 12 (11 primary, 1 secondary), above the
series floor of 8/4/1, with Kaplan numbered in first-citation order between
Vaswani (4) and Anyscale (6).

## Cut

I ran a fresh slop and clarity pass on the three recast passages: the
orientation paragraph carrying the re-homed Anthropic definition, the
prompt-length paragraph carrying the Vaswani/Kaplan split, and the prefix-cache
paragraph carrying the network sentence. No sentence failed the test.

The prompt-length paragraph is the one that grew, since the recast added a second
source's accounting. It runs long, but it holds one idea per sentence and each
sentence carries a fact or a reasoning step: the named misconception, Vaswani's
actual table, the separate Kaplan accounting, the linear term over an n-token
prompt, the single context-bearing term, the d > n/12 crossover, and the
tens-of-thousands consequence. Its closer, "The n-squared term is present and
growing, but it is being outweighed," survives the delete test: it carries the
reconciliation the whole section exists to make, that the quadratic term is not
absent but dominated, which the preceding sentence about the linear term
dominating does not itself state. I left the paragraph intact rather than split
it; splitting would be optional polish on a settled structure, not a fix.

The network paragraph's negative-parallelism sentence ("A vendor's stated
200-millisecond TTFT is not the on-GPU prefill compute time an academic paper
measures. It is the compute, plus the queue, plus the routing, plus the client's
round trip.") corrects a real, named confusion, the one the section is built to
correct, so the contrast is earned. The worked-case closer about cutting the
round trip in half is the Somers-style grounding the voice guide asks for and was
already cleared in round 01.

I checked the recast sentences for grammar, for em-dashes, and for the press ban
on "machinery": none present. No prompt leakage entered with the recast. No edge
sentence in the changed passages leans on its neighbors for sense.

## Reader

Read straight through as the paper's declared reader, the piece still gives what
the sources alone do not: the felt pause resolved into four separable costs, the
counterintuitive result up front, and now a cleaner account of why the quadratic
intuition is real yet dominated until long contexts. The recast improved the
lesson rather than merely repairing a citation, because the two-source split
(Vaswani for the attention term, Kaplan for the linear term and the crossover)
is exactly the distinction a reader needs to see why "attention is quadratic"
does not predict the everyday pause. The prose sits closer to the voice-guide
exemplars than to a median summary: it names the folk belief and answers it with
Kaplan's own condition and Anyscale's own numbers in the same stretch, the Luu
move. The original-work sentence in draft-handoff still holds against the article,
and no single cited source assembles the four-part decomposition.

## Edits

None. The four routed items were resolved by the researcher and writer, and the
recast passages needed no editorial cut or rewrite.

## Required work

None.

## Decision

approve -- the O(n·d²) term is now correctly attributed to Kaplan et al. and
confirmed against Table 1, the crossover rests on Kaplan's verified d > n/12
condition with the threshold reconciled across both sections, the network claim
rests solely on Artificial Analysis's verified "includes network latency"
sentence, the Together AI string is de-quoted, and the fresh slop and clarity
pass on the recast paragraphs found nothing to cut.
