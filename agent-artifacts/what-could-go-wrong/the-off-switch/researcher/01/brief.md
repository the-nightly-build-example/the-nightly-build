# Brief 01 — researcher — what-could-go-wrong/the-off-switch

## Begin with these inputs only
- `agent-artifacts/what-could-go-wrong/the-off-switch/editorial-direction.md`
- `agent-artifacts/what-could-go-wrong/the-off-switch/commission.md` (argument,
  four-move angle, required contribution, source obligations, starting sources)

Do not browse the archive as background. `nb` at `/home/user/the-nightly-build/nb`.
The desk mandates: **work from the original documents, not commentary; name no
company as an authority.**

## Task
Follow the **researcher** skill (Skill tool: `researcher`).

- Read the **theoretical primaries**: Soares, Fallenstein, Yudkowsky, Armstrong 2015
  "Corrigibility" (intelligence.org PDF) — the problem statement and why naive fixes
  fail; Hadfield-Menell, Dragan, Abbeel, Russell 2016 "The Off-Switch Game" (arXiv
  1611.08219) — the exact result (uncertain agent allows shutdown; confident agent
  resists) and its conditions; Orseau & Armstrong 2016 "Safely Interruptible Agents";
  Omohundro 2008 "The Basic AI Drives"; Russell "Human Compatible" (2019) for the
  present framing.
- Read the **empirical** reports people cite as shutdown resistance, for their
  **methods**, and record for each *exactly who supplied the goal and how contrived
  the setup was*: Palisade Research's 2025 shutdown-resistance writeup; Anthropic's
  2025 "agentic misalignment" report; the Apollo Research / OpenAI o1 system-card
  scheming evaluations (2024). Distinguish what was demonstrated from what was
  scenario-supplied.
- Contradiction hunting (required): critics arguing the demos prove little
  (goal-handed-in, reward-shaping artifacts) and critics arguing corrigibility is
  unnecessary/handled. Steelman each side.
- Verify every experimental condition and every researcher's exact title/affiliation
  against the owning document; confirm every URL resolves (403/paywall is gated —
  try a browser fetch).

## Source policy to meet
min 8 sources; **primary ≥ 4, secondary ≥ 1.**

## Output (write only this)
`agent-artifacts/what-could-go-wrong/the-off-switch/researcher/01/evidence.md`
(stable sections; in Numbers, record the specific rates/conditions from each
empirical report — e.g. "sabotaged the shutdown script in N of M trials, goal
supplied by prompt X"). Return `DONE researcher <path>` (or `BLOCKED`/`REQUEST`).
