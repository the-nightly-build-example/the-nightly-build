# Commission: the-evidence/retrieval-augmented-generation

## The document

Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
(Facebook AI Research, NeurIPS 2020), the paper that named RAG. The lesson
teaches what the paper measured, what it claimed, and what "RAG" has since come
to mean in the products that cite it.

## The angle

The paper introduced a small end-to-end learned model: a dense retriever paired
with a sequence-to-sequence generator (BART), trained together so the generator
learns to use the retrieved passages. It reported gains on knowledge-intensive
tasks like open-domain question answering and was measured on a fixed Wikipedia
dump. Teach that result honestly on its own terms.

Then bring it to the present. The word "RAG" now usually names an inference-time
pipeline — off-the-shelf retriever, off-the-shelf LLM, no joint training — that
was not the paper's system. Report the gap the primaries support: the current
retriever-plus-LLM stack inherits the name but not the training, and empirical
work published since (needle-in-a-haystack style evaluations, the "long-context
versus RAG" comparisons, and studies of the failure modes retrieval doesn't fix)
has qualified what the pipeline actually delivers. When today's usage does not
match what the document showed, the desk requires saying so plainly.

## Teach, in this order

1. Knowledge-intensive tasks and why a pure parametric model struggles at them:
   the setup the paper is answering. Keep it brief; this is what the rest
   depends on.
2. The paper's method and result: dense passage retriever, jointly trained with
   a seq2seq generator, on a fixed Wikipedia dump; the numbers it reported on
   open-domain QA and where it beat the parametric-only baseline. Give the
   figures, not the magnitudes.
3. What "RAG" means now: an inference-time pipeline the paper's authors did not
   evaluate, and the load-bearing evidence on whether that pipeline delivers
   what the name implies (long-context comparisons, retrieval failure modes,
   grounding-versus-hallucination results).

## Sources

Series policy requires at least six sources, at least three primary and at least
one secondary. The paper itself is the anchor primary. The Dense Passage
Retriever paper it uses, the earlier REALM paper (Guu et al. 2020) it built on,
and at least one primary evaluation on the modern retriever-plus-LLM pipeline
(a long-context-vs-RAG study, an ACL/NAACL failure-mode paper, or a benchmark
report on hallucinations with retrieval) are the primaries that let the lesson
report the corrections firsthand. The researcher resolves the exact set.

## Boundaries and neighbors

The 2026-08-24 edition runs this alongside the-instruments/rewardbench,
the-mechanics/first-token-latency, what-could-go-wrong/algorithmic-monoculture,
and when-ai-breaks/nyc-mycity-chatbot. No topic overlap with those.

Within the-mechanics, a `retrieval` lesson already teaches the mechanism (how a
current product answers with retrieved passages). Link it in Background and do
not re-teach the mechanism; this lesson stays on the *paper* — what its authors
built, measured, and reported. Within the-evidence, scaling-laws-kaplan and
chinchilla have taught training compute; do not re-teach that machinery.

## Production record

Template: lesson. Series: the-evidence (open section, self-chosen topic).
Production policy resolved to the balanced profile: writing-coach effort low,
researcher effort high, writer effort medium, editor effort high, model
"capable" for every role. Roles run as delegated agents on the shared checkout;
each invocation records the actual model and effort used. No `required`
directive applies, so nothing was traded down.
