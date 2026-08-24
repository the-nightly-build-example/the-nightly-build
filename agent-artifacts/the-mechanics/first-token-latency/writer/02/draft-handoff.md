# Draft handoff: the-mechanics/first-token-latency (writer/02)

## Original work

The article decomposes the felt TTFT pause into four separable costs -- new
prompt compute, contention from other users on the GPU, prefill skipped for a
cached prefix, and the network round trip -- and shows with each source's own
figures that the first cost barely moves at everyday prompt lengths; no single
cited source assembles that four-part account.

## Proof

`./nb check ... --series the-mechanics --library /home/user/library-checkout`
after `nb stamp`: BLOCK: 0, WARN: 0, verdict PUBLISHABLE. words 2080, sources 12
(11 primary, 1 secondary), reading time 9 min. No warnings left standing.

## Editor/01 required items resolved

- **Crossover attribution recast.** The prompt-length section no longer sources
  the linear feed-forward/projection term to Vaswani. Vaswani Table 1 is now
  stated for exactly what it holds (self-attention O(n^2*d) versus a recurrent
  layer at O(n*d^2), no feed-forward row); the linear O(n*d^2) per-token term is
  attributed to Kaplan et al., added as a new primary in first-citation order
  (source 5). Vaswani's self-attention-versus-recurrent sentence is no longer
  repurposed as an attention-versus-feed-forward claim.
- **Crossover threshold reconciled.** The prose now rests on Kaplan's
  constant-aware condition (context term small while d > n/12), placing the
  crossover in the tens of thousands of tokens for a d of a few thousand -- in
  agreement with the record and with the existing long-context section, replacing
  the bare n = d framing.
- **Network sentence fixed.** The unsupported Anthropic clause is dropped; the
  network point now rests solely on Artificial Analysis (source 12), which states
  TTFT "includes network latency." Anthropic's reduce-latency page is retained
  and re-homed to the orientation, cited for its actual TTFT definition (source 2).
- **Together AI TTFT string.** De-quoted to a faithful paraphrase. The article's
  quoted string was contested against the live page (editor/01 retrieved
  different wording), so it is no longer presented as verbatim; the Together AI
  citation stands (source 1).

## Open questions

None. The Together AI wording was resolved by de-quoting rather than by
re-fetching the live page; if a verbatim vendor quote is later wanted there, the
source needs a fresh confirmed retrieval.
