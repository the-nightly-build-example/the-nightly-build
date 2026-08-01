# Commission — what-could-go-wrong/jailbreaks

## Assignment
Teach the argument that a language model's safety training cannot be made robust:
that for any model trained to refuse a class of requests, an input exists that
gets it to comply, and that this is a structural property, not a bug labs will
soon patch. Present the argument at full strength, test it against what real
systems do, and bring it to the present.

## Angle (per the desk: open at full strength, then draw the line)
Open with the argument as its most careful defender makes it. The worry, stated
early by red-teamers and safety researchers: alignment/refusal is a thin layer of
fine-tuning over a model that has already learned everything, so the harmful
capability is still in the weights and only the surface behavior was changed;
adversarial ML has decades of evidence that robustness to worst-case inputs is
extraordinarily hard. Name who made it and what they had seen.

Then test against real systems, drawing the sharp line the desk requires between
demonstrated and conjectured:
- DEMONSTRATED: automated, transferable jailbreaks. The GCG attack (Zou et al.,
  2023, "Universal and Transferable Adversarial Attacks on Aligned Language
  Models", arXiv:2307.15043) — a gradient-found suffix that transfers across
  models, showing jailbreaks can be produced by optimization, not just clever
  wording. Many-shot jailbreaking (Anthropic, 2024) — long context defeats
  refusals. These are working systems, real models, published methods.
- DEMONSTRATED-BUT-BOUNDED: labs patch specific attacks; defenses (RLHF,
  circuit breakers/representation engineering, input/output classifiers,
  constitutional classifiers) raise the cost. Report what they measurably achieve
  and where they still fail. Anthropic's constitutional-classifiers work and its
  public jailbreak bounty is the fair, current counter-evidence: defenses can
  drive success rates down a lot, but the public results still show non-zero
  breakthroughs. Be precise with the numbers.
- CONJECTURE / OPEN: the strong claim that robust refusal is *impossible* in
  principle. Distinguish "no one has done it and there are theoretical reasons
  it is hard" from "proven impossible." Do not overstate. The honest state:
  empirically unsolved, theoretically suspected hard, not proven undoable.

Bring to present: who argues this today and what they want (evaluations,
mandatory red-teaming, capability restrictions, or the dismissive counter that
jailbreaks are low-stakes because the info is on the open web). Check confidence
against proof in BOTH directions: name the gap when doom outruns evidence AND when
"it's basically solved" outruns evidence.

Ground the mechanism in the-mechanics/instructions-are-data (already taught: no
architectural line between instruction and data, so refusals are learned pattern,
not enforced boundary). Link it; that lesson is the load-bearing prerequisite.

Land: leave the reader able to weigh the argument on its merits. Name no company
as an authority. State plainly what has been shown in a working system and what
remains analogy.

## Intended reader
House reader who has heard "AI jailbreaks" and cannot tell if it is a solved
nuisance or a fundamental limit.

## Required contribution
The reader can separate the demonstrated fact (transferable, optimizer-found
jailbreaks exist and defenses are partial) from the contested claim (robust
refusal is impossible), and can name what evidence would move the question.

## Source obligations (what-could-go-wrong: min 8; primary >=4, secondary >=1)
Work from original documents, never commentary about them.
- PRIMARY: GCG paper (arXiv:2307.15043) — read the transfer results and success
  rates, exact numbers and models.
- PRIMARY: Anthropic "Many-shot jailbreaking" (2024) paper/report — the scaling
  curve of attack success with number of shots.
- PRIMARY: Anthropic "Constitutional Classifiers" (2025) paper/report and/or the
  public jailbreak-bounty results — the strongest current DEFENSE evidence and
  its residual failure rate. Be fair and exact.
- PRIMARY: one foundational adversarial-examples source establishing worst-case
  fragility (e.g., Szegedy et al. 2013 / Goodfellow et al. 2015 on adversarial
  examples) OR Wei et al. 2023 "Jailbroken: How Does LLM Safety Training Fail?"
  (arXiv:2307.02483) for the mechanism (competing objectives / mismatched
  generalization). Prefer the latter for direct relevance.
- SECONDARY: reputable coverage/analysis for context only.
- Seek contradictory evidence hard: the best case that defenses are winning
  (constitutional classifiers driving success rates toward single digits), and
  the best case that it does not matter (dual-use info availability). Steelman both.

## Starting sources
arXiv:2307.15043 (GCG); arXiv:2307.02483 (Jailbroken); Anthropic many-shot
jailbreaking; Anthropic constitutional classifiers + bounty results. Researcher
verifies exact numbers against each primary.

## Relevant prior coverage (link, do not re-teach)
- the-mechanics/instructions-are-data — the mechanism under jailbreaks. Core
  Background link; do not re-derive it.
- what-could-go-wrong/reward-hacking and /deceptive-alignment are neighbors on the
  same desk but different arguments (gaming objectives; faking alignment). Do not
  overlap; this piece is specifically about robustness of refusal to adversarial
  input. Note the distinction if it helps the reader place it.

## Structures NOT to repeat
- the what-could-go-wrong desk has a habit of the "the record runs out before the
  catastrophe" / "X has never once been logged" closing move (reward-hacking,
  instrumental-convergence). Do not reuse that closer or its cadence.
- No colon-subtitle headline; no hedged-contrast dek; no scenario-triad open.
  Open on the argument at strength, in its defender's voice, per the desk.

## Neighboring articles tonight
tool-use (mechanics) may touch hijack-by-text in one sentence; this piece owns the
robustness ARGUMENT. Keep the mechanism light here and cite instructions-are-data.
Distinct from google-flu-trends (a failure incident, different desk).

## Template / mode / paths
- template: lesson; mode: open; order: null; date: 2026-08-01.
- article: .nb-work/what-could-go-wrong/jailbreaks/library/what-could-go-wrong/jailbreaks.html

## Harness / model
writer: claude-code-routine / claude-sonnet-5 / medium. researcher high, editor
high, coach low; all claude-sonnet-5.

## Tags
Suggest: ["jailbreaks", "adversarial-robustness", "ai-safety", "red-teaming"]. Writer finalizes.
