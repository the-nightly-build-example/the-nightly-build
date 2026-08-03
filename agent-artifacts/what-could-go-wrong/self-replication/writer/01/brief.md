# writer brief: what-could-go-wrong/self-replication (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/commission.md — assignment, angle, boundaries
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/editorial-direction.md — house + headline standard, press voice, lesson identity, series prompt
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/writing-coach/01/voice-guide.md — register and licensed forms (note the harness-naming sentence-level rule)
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/researcher/01/evidence.md — the complete claim set; use its Numbers exactly
- Article to edit: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/library/what-could-go-wrong/self-replication.html
- Template context dir: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/.nb-context/

Output (draft handoff): /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/writer/01/draft-handoff.md

Proof: run from repo root /home/user/the-nightly-build using the checkout's nb.
  Iterate: ./nb check --series what-could-go-wrong .nb-work/what-could-go-wrong/self-replication/library/what-could-go-wrong/self-replication.html --library /tmp/claude-0/-home-user-the-nightly-build/6cb4c49e-7d08-5720-bd17-76474fa73d16/scratchpad/library-checkout --no-check-links
  Final (BLOCK: 0, links included): same without --no-check-links. Run ./nb stamp before the final check.

This round's focus (decisions the inputs do not fully carry):
- The headline numbers CANNOT be stacked or directly compared — they measure
  different tasks. Fudan's 50%/90% is a LOCAL copy with the model's own weights
  and deploy scripts pre-placed in the folder; OpenAI's 0/100 is a harder
  resource-acquisition suite; METR's suites are explicitly "easier than ARA."
  Every capability figure must carry, in the same or adjacent sentence, how much
  the harness supplied (the voice guide's sentence-level rule). Never present a
  number as the full autonomous-replication loop.
- No public eval measures the frameworks' actual end-to-end ARA loop
  (autonomously acquire compute AND money, obtain machines, evade a determined
  operator, sustain at scale). State that gap plainly; it is the spine.
- Steelman first, undercut-free: give the alarm its full paragraphs before any
  rebuttal (voice guide). Then the two-sided gap: the alarm outruns the record
  (its strongest results rest on harness-supplied weights/servers/shutdown
  premises and "at all costs" nudging), and the dismissal outruns it too (labs
  demoted ARA as an automatic trigger — OpenAI to a Research Category, Anthropic
  to a non-triggering checkpoint, DeepMind removed the Autonomy domain — while
  explicitly keeping it in view and folding it into misalignment: "not yet,
  still watching," not "impossible"). The Shanghai AI Lab study is the
  reconciling middle: local replication is real and easy, but success rate is a
  poor proxy for risk. Attribute each framework's move to its own document.
- Link instrumental-convergence (what-could-go-wrong/instrumental-convergence)
  for the motivation rather than re-arguing why a system would want to persist.
- This is dual-use safety material for public education: stay factual and
  neutral, no operational how-to. Earn any grave word (press voice).
- Headline/dek: avoid the series' "the model that X needs Y nobody has held"
  comma mold and the "an optimizer wrote / an agent with a correct reward"
  agent-noun opener; avoid comma-triad / semicolon-reversal deks. State this
  piece's specific finding about the gap between alarm and eval record.
- nb-meta: date 2026-08-03, harness, writer model you ran as; tags array empty.
