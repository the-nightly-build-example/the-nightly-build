# researcher brief: the-mechanics/answer-length-bias (01)

Inputs:
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/editorial-direction.md — the standing editorial, sourcing and slop standards for this article.
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/commission.md — the assignment, angle, boundaries, and the resolved source obligations (minimums and the must-open primary documents).

Output: .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the archive for background. You may use web, document and nb history tools. Read the primary documents themselves, not coverage of them; open the cited passage and record honest locators. Where something you need is missing, ask me.

Run-environment note: outbound HTTPS is proxied; a 403 or paywall means gated, not dead — try a proper browser request before giving up, and record the address where the document lives, not the fetch route.

Priority questions to answer (meet the source minimums in commission.md with sources that could change the interpretation, not padding):
- A concrete, checkable instance of the behavior (a simple question answered at length). Prefer something documented.
- The measured relationship between answer length and reward-model score, and the fraction of RLHF's apparent win-rate gain attributable to length alone (Singhal et al. 2023). Get exact figures.
- The length-controlled AlpacaEval correction (Dubois et al. 2024): what it found about length confounding preference win rates; numbers.
- The RLHF pipeline and any documented human preference for longer/more-thorough answers (InstructGPT / preference-labeling papers).
- What is settled (reward models pick up length; length can be regressed out) vs open (whether raters prefer length itself or the thoroughness it proxies).
- A source asset: any figure plotting reward vs length, or win rate vs length.
