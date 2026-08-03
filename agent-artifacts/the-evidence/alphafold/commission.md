# Commission: the-evidence/alphafold

## Assignment
Read the AlphaFold document so the reader knows what it actually showed and
where today's "AI solved biology" usage outruns it. The document is the
DeepMind paper "Highly accurate protein structure prediction with AlphaFold"
(Jumper et al., *Nature*, 2021) and its companion database paper. This is the
the-evidence desk: state what the document is, who wrote it, why it became
famous, what it actually did (data, method, numbers, scale), then bring it to
the present.

## Why this document, now
AlphaFold won its authors a share of the 2024 Nobel Prize in Chemistry, and it
is the single most-cited proof that AI transforms science. The reader keeps
meeting the claim and cannot check it. The desk's job is to show the size of
the foundation under the claim: what CASP14 actually measured, how good "highly
accurate" was in numbers, what the model was trained on, and the honest limits
(single chains vs complexes, static structure vs dynamics/function, orphan
proteins, the confidence metric pLDDT and where it is low).

## Angle and required contribution
Teach the reader to read AlphaFold's own numbers. The one act of original work:
separate what the paper demonstrated (a measured jump in structure-prediction
accuracy on a specific blind assessment) from the three things it is routinely
credited with but did not show (predicting function, solving folding dynamics,
making wet-lab structural biology obsolete). Ground every claim in the paper's
own figures, CASP14's independent scoring, and at least one later source that
confirms, bounds, or corrects the 2021 result (e.g. AlphaFold-Multimer / AF3
limits, or independent critiques of database accuracy for some protein classes).

## Boundaries
- One lesson, lesson template, 1200–2200 words.
- This is a science-AI document. Everything not "algebra or probability" is
  taught on the spot: what a protein / amino-acid sequence / 3D structure is,
  what "structure prediction" means, what CASP is, what GDT_TS and pLDDT
  measure. Assume no biology background; the reader is smart and time-poor.
- Do not drift into a general "AI for science" essay. One document, its
  evidence, its present-day use.

## Source policy (from `nb source-policy --series the-evidence`)
- Minimum 6 sources; primary >= 3, secondary >= 1.
- Primary = the Nature paper(s), the CASP14 results/assessment, the AlphaFold
  DB, DeepMind's own technical materials. Prefer the paper over coverage of it.

## Production policy (from `nb production-policy --series the-evidence`, profile balanced)
- writing-coach: model capable, effort low  → run as: claude (sonnet)
- researcher: model capable, effort high     → run as: claude (opus, claude-opus-4-8)
- writer: model capable, effort medium       → run as: claude (opus, claude-opus-4-8)
- editor: model capable, effort high         → run as: claude (opus, claude-opus-4-8)
No `required` directive on any stage; capable tier honored, no deviation.

## Tags
No tag prompt-fragments are configured for this series in the current press
(`series.yaml` declares no `tags:` mapping), so the article ships with an empty
tag list. This is not a downgrade; it matches configuration.

## This edition's neighbors (keep distinct, one paper)
Four other lessons run tonight: the-instruments/cost-per-token (the $/token
metric), the-mechanics/prefill-and-decode (inference latency),
what-could-go-wrong/self-replication (autonomous-replication risk),
when-ai-breaks/amazon-hiring-tool (a hiring-bias incident). AlphaFold is the
run's only non-LLM, science-AI piece; lean into that distinctness. No overlap
risk, but do not reach for LLM examples when a protein example is the subject.

## Recent shapes in this series to break (do not inherit)
The series' recent headlines lean hard on one mold: "the famous paper never did
the thing it is credited with" (attention "never trained a language model,"
GPT-4 report "declares no further details," AlphaGo paper "never mentions Lee
Sedol," the bitter lesson "zero citations"). Do not headline AlphaFold with an
"AlphaFold never…" reveal. Find the fresh, specific claim this piece defends.
Avoid the comma-triad dek and the semicolon-reversal dek.
