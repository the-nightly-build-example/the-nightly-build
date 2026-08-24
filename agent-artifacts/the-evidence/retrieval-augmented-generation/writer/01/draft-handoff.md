# draft-handoff: the-evidence/retrieval-augmented-generation (writer 01)

## Original work

The article maps each of Lewis et al. (2020)'s specific claims — the four
open-domain QA benchmark wins, the frozen-index training loop, the 452-item
Jeopardy factuality finding, and the world-leaders index hot-swap — onto what
the modern retrieve-plus-LLM stack that inherited the name is actually measured
on today by Xu, Liu, Niu, and Barnett, so that a reader can tell which of the
two "RAG" systems a given number belongs to.

## Proof result

`./nb check .nb-work/the-evidence/retrieval-augmented-generation/library/the-evidence/retrieval-augmented-generation.html --series the-evidence --library /home/user/library-checkout` returns BLOCK: 0, WARN: 0, verdict: PUBLISHABLE. `nb stamp` gives words=1911, reading_minutes=8, sources=8. No warnings intentionally left.

## Open evidence/voice questions

- Bai et al. (LongBench, arXiv 2308.14508) is named in the researcher's
  Contradictions section as the primary that disagrees with Xu et al. on
  whether retrieval helps long-context models. The evidence record does not
  admit Bai as a source entry with a URL, so I carried the disagreement by
  citing Xu et al.'s own acknowledgment of the concurrent contrary result and
  their scale-effect explanation, rather than sourcing Bai directly. If the
  editor wants Bai cited as a distinct source, the researcher would need to
  admit it.

- Barnett et al.'s abstract/§1 gives the BioASQ run as "15,000 documents,"
  while §4.3 and Table 1 give 4,017 documents. I used 4,017 and named the
  discrepancy inline, per the researcher's Contradictions note that the
  case-study section is the number to trust. Flagging in case the editor
  prefers a different disposition.
