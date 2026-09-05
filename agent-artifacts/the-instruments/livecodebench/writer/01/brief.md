# writer brief: the-instruments/livecodebench (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, series prompt, template rules
- ../../commission.md — subject, angle, boundaries, required contribution
- ../../writing-coach/01/voice-guide.md — how this piece should sound; read before drafting
- ../../researcher/01/evidence.md — the complete, only set of claims available to you
- ../../../../library/the-instruments/livecodebench.html — the initialized article to edit in place
- ../../../../.nb-context/ — effective template contract and runtime assets

Output: draft-handoff.md (this directory)

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-instruments/livecodebench/library/the-instruments/livecodebench.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/643ba5c9-25c5-59fc-9937-7e74191ccd45/scratchpad/library-checkout
(iterate with --no-check-links; run the exact command above, links on, until BLOCK: 0 before handoff)

This round's focus — precision the evidence record flags:
- When you show "a score paired with its window," use the verified figure exactly as recorded: DeepSeek's 19.4 is from the BASE-model table, labeled LiveCodeBench-Base (0801-1101), 3-shot. Do not silently present it as a chat/instruct number; if you reference the widely-quoted chat figure, mark that it comes from a different table the record did not fully verify.
- The "misled" case is contamination/saturation and the moving-cutoff evidence: DeepSeek's pass@1 collapses across its cutoff on LeetCode (~60 -> ~0). Use it. But keep the counter-material honest: the fix is not perfectly clean — the survey notes temporal-cutoff benchmarks "can still lead to data contamination" (problems reused in future contests); the cutoff is normalized to a vendor-supplied release date; the contamination found was LeetCode-specific, not AtCoder. These are real limits in the lesson, not a refutation.
- Comparability is the angle: six dated versions exist, and DeepSeek and Qwen each report on a different self-chosen window. Teach the reader to check window + version before comparing.
- Differentiate from published humaneval-pass-at-k, swe-bench, and codeforces-rating (link, don't re-teach): say plainly how LiveCodeBench differs from each.

Recent-pattern habits in this series to break (vary construction, do not clone):
- Do NOT reuse the recent heading sequence "The number that said X" / "N choices behind the percentage" / "Whoever grades decides the score" / "What the N actually counted" (attack-success-rate, 2026-09-04). Write headings in this measurement's own nouns.
- simpleqa already taught "a headline share was a benchmark artifact" and superglue "saturation against a human baseline" — do not re-run those exact points; this lesson's distinct subject is contamination and the moving cutoff.
- Deks recently ran to a single striking figure + reversal; check your dek against spec/headlines.md (no comma-triad, no suspended-question molds).
