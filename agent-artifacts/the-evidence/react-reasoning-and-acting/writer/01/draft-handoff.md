# Draft handoff: the-evidence / react-reasoning-and-acting

## What this lesson teaches (commission's short list, all covered)
1. What ReAct proposed — the thought/action/observation loop, with a real worked
   trace (the paper's Apple Remote HotpotQA example) in the orientation note.
2. What the paper actually measured, honestly — Table 1 (HotpotQA 27.4 EM, below
   CoT's 29.4 and Standard's 28.7; FEVER 60.9 above CoT's 56.3), the hallucination
   analysis (CoT 56% of failures hallucinated vs ReAct 0%; ReAct's own cost: 47%
   reasoning error, 23% search failure), and the interactive gains (ALFWorld 71 vs
   BUTLER 37; WebShop 40 vs 30, humans ~60). The "34% and 10%" is placed as the
   two interactive benchmarks only.
3. How practice diverged — native structured tool_use/tool_result and OpenAI's
   five-step function-calling loop replaced the hand-written prompted format, and
   "ReAct" is now used loosely for any reason-plus-tool agent.

## Structure
- Why this matters (bookend, no cites).
- orientation `the-loop`: the loop, few-shot prompting, Wikipedia action API,
  worked trace note. Cites 1, 3.
- `hotpotqa-result`: the honest QA result + comparison table. Cites 1, 2.
- `grounding`: hallucination table, and ReAct's own failure modes. Cites 1.
- `interactive-gains`: ALFWorld + WebShop, the headline numbers. Cites 1.
- `modern-loops`: how today's agents diverged. Cites 1, 4, 5, 6.
- The takeaway (bookend, no cites).
- Sources: 6 (5 primary, 1 secondary).

## Body-first, bookends last
Body written first; both bookends written after and read as setup/resolution.
Opener poses "what ReAct showed, on what, how far agents moved"; takeaway resolves
exactly those three. Body never addresses the reader or mentions the lesson.

## Furniture
Two pieces, each earning its place: the worked-trace note (makes the loop
concrete before any number) and the ReAct-vs-baselines table (the comparison is
the point). No chart (no chart-N.py; a 4-row table carries it).

## Habits broken (per commission)
- No "credited with starting the X era, never Y" headline mold. Headline states
  ReAct's own concrete surprise: it trailed chain-of-thought on HotpotQA.
- Dek avoids the "X did A, and lost at B" comma-tail reversal; it adds the
  hallucination win instead of restating the headline loss.
- No final "How far the X reaches" section; headings vary in construction, none
  is a comma-and clause, none is a stock scaffolding label.

## Notes for the editor
- Slug/topic verified novel by orchestrator. Stays on the ReAct document; links
  (not re-teaches) chain-of-thought and tool-use in prose.
- One automated-summary discrepancy caught and discarded: bogus 78/69/39 HotpotQA
  numbers; the real 27.4/29.4/28.7 were read from the PDF. See evidence.md.
- Every source opened and returned 200 before use. No GitHub URLs.
