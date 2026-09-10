# Commission: the-evidence/palm

## The document

Chowdhery et al., "PaLM: Scaling Language Modeling with Pathways" (Google
Research, 2022; arXiv:2204.02311, later in JMLR 2023). One lesson, one document.
The reader should finish knowing what the PaLM paper actually reported: what was
built, at what scale, on what data, by what method, what it measured, and how the
claims read now.

## Why this closes a gap tonight

The reader has already met PaLM-540B twice in the recent course without ever
reading the paper that introduced it: The Evidence used it as the backbone model
in the ReAct lesson (2026-09-09), and The Instruments dissected PaLM's
model-FLOPs-utilization number (2026-09-09). The Evidence has also already taught
the Kaplan scaling laws and Chinchilla. PaLM is the document those threads hang
off, and it is a clean case of the desk's core move: a famous result read against
what the field already knew when it shipped.

## The angle the piece must earn

PaLM was the largest dense language model of its moment, and by the compute-optimal
rule Hoffmann et al. (Chinchilla) published only weeks earlier it was trained on
far too little data for its size. State the scale honestly (parameters, training
tokens, chips, tokens-per-parameter ratio), then weigh PaLM's own headline claims
(breakthrough/discontinuous jumps on BIG-bench tasks, chain-of-thought results,
the Pathways/MFU engineering) against: (1) the Chinchilla correction, which PaLM's
own token budget fails; (2) what later work confirmed or replaced (PaLM 2, then
Gemini; the emergent-abilities claim later contested as partly a metric artifact).
Say plainly where today's citations of PaLM outrun what the paper showed.

This is analysis the evidence must ground. The researcher supplies the exact
figures; the writer must not assert the "undertrained" verdict without the
Chinchilla numbers and PaLM's own token count side by side.

## Distinctness and continuity

Not a published slug in the-evidence. Do not re-teach ground the course already
holds; link it in Background at first use instead of explaining it:

- `../the-evidence/chinchilla.html` — the compute-optimal scaling result PaLM is
  measured against. The scaling correction is the spine of this lesson; cite/link,
  do not re-derive Chinchilla.
- `../the-evidence/scaling-laws-kaplan.html` — the earlier scaling laws.
- `../the-evidence/react-reasoning-and-acting.html` — used PaLM-540B; link, do not
  restate ReAct.
- `../the-instruments/model-flops-utilization.html` — the PaLM MFU number in full.
  This lesson names MFU only as one of PaLM's engineering claims; it must not
  re-teach how MFU is computed. Link and move on.
- `../the-evidence/emergent-abilities.html` and
  `../the-mechanics/in-context-learning.html` — link where relevant; the emergent
  claim is contested, so present it as claim-then-challenge, not as fact.

Chain-of-thought, mixture-of-experts, and the Transformer are taught; assume or
link, never re-teach.

## Sources (floor: min 6; primary >=3; secondary >=1)

Primary must include the PaLM paper itself (read the method, data, and results
sections and the BIG-bench/MFU figures in full, not the abstract). Strong primary
companions: the Chinchilla paper (Hoffmann et al. 2022) for the compute-optimal
numbers; the PaLM 2 technical report and/or Gemini report for what replaced it;
the emergent-abilities paper and its "Are Emergent Abilities a Mirage?" rebuttal
for the contested claim. Secondary reporting for context on reception. Every
figure the "undertrained" argument rests on is verified against the primary that
owns it.

## Production policy (balanced; nothing marked required)

writing-coach effort low, researcher high, writer medium, editor high; model
"capable" for every stage. No `required` model/effort directive, so each role
records the actual model and effort it ran at in its artifact. No deviation to
report unless the runtime forces one.

## Tags

Open section, tags optional. Suggested nb-meta tags for the writer to set if apt:
palm, google, scaling-laws, chinchilla, model-flops-utilization. The writer owns
the final tag list.

## Recent-pattern notes (habits not to inherit)

These travel to the writer and the editor. They are habits of the recent library,
not template form.

- Deks in the recent run lean hard on one mold: a concrete clause, a comma, then
  "and"/"while"/"or" introducing the twist (ReAct, AlphaZero, MFU, Cigna,
  flash-crash all do it). Vary the dek's construction; do not ship another
  comma-plus-conjunction two-parter by reflex.
- Headlines are full declarative findings, often with a number. Keep that form,
  but the number-forward opener is now frequent; earn it or choose another shape.
- Headings are argument steps in the piece's own nouns (good, keep). Do not copy a
  prior lesson's heading rhythm.

## Neighboring articles in tonight's run

Commissioned alongside: the-instruments/gaia (a benchmark), the-mechanics/
lost-in-the-middle (a behavior), what-could-go-wrong/ai-enabled-coup (a risk
argument), when-ai-breaks/deloitte-ai-report (an incident). No overlap with this
document lesson; listed so the edition reads as one paper.
