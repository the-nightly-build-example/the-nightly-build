# researcher brief: what-could-go-wrong/alignment-faking (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md   (citation standard, series territory, reader)

Output: ./evidence.md

Read the original document: Greenblatt et al. 2024, "Alignment Faking in Large
Language Models" (Anthropic and Redwood Research; arXiv and the Anthropic
write-up). Pin down, each against the paper: the exact setup (Claude 3 Opus; the
told-it-would-be-retrained-to-answer-harmful-queries scenario; the monitored vs
unmonitored / free-tier vs paid-tier cue; the hidden scratchpad), the measured
compliance gap and any figures for the reinforcement-learning variant, and the
authors' own statements of what the study does and does not show. The hinge of the
piece is how much the researchers arranged, so classify each behavioral claim by
how it was elicited and record the exact conditions.

Then read the paper's appended external reviews and the follow-up literature:
replications or failures to replicate across other models, arguments that the
behavior is an artifact of the prompt or of Claude's specific training, and any
later Anthropic/Redwood or third-party work extending or bounding it. Record these
in Contradictions in full. Distinguish reported result from the authors'
interpretation throughout. Two retellings of one experiment count as one.
