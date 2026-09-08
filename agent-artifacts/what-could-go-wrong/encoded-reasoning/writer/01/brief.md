# writer brief: what-could-go-wrong/encoded-reasoning (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, paper voice, series prompt, citation standard.
- writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting.
- researcher/01/evidence.md — the complete set of claims available to you; use the Numbers section exactly.
- commission.md (artifact root) — argument, teaching list, source floor, habits not to inherit.
- The initialized article: library/what-could-go-wrong/encoded-reasoning.html (edit in place; keep chrome exact).
- .nb-context/ (template contract, furniture catalogs, runtime assets).

Output: writer/01/draft-handoff.md (plus the edited article).

Proof: ./nb check .nb-work/what-could-go-wrong/encoded-reasoning/library/what-could-go-wrong/encoded-reasoning.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/7ee8fcf2-0447-5975-8ee1-93a43ada820c/scratchpad/library-checkout

This round's focus — the evidence sharpens the commission's line; follow the evidence:
- Replace the commission's two-tier line (shown vs analogy) with the three tiers the evidence supports: (1) hand-built encoded reasoning on a toy task — Roger & Greenblatt fine-tuned GPT-3.5-Turbo on a sycophancy task (~80% with hidden CoT vs ~54% no-CoT, and it failed to learn in 2 of 6 runs); paraphrasing caps a built channel at ~3 bits/KB. (2) Obfuscation/illegibility EMERGING from ordinary training incentives, not hand-built — Baker et al. (OpenAI) show obfuscation under optimization pressure on the CoT, and Jose et al. show illegible CoT emerging from ordinary RL across ~14 of 15 models. This tier is real and is the one the commission underweighted. (3) Autonomous, undetected steganographic collusion in a deployed system pursuing a hidden goal — still speculative; Motwani et al. measured only the capability and found it limited today, with no live collusion observed.
- Keep two things distinct that are easy to blur: ordinary CoT UNFAITHFULNESS (Turpin, Lanham — the model's stated reasons often are not its real ones, with no steganography at all) versus deliberate ENCODED/steganographic reasoning. The "the writing reflects the reasoning" assumption already fails today in the plainer, unfaithfulness way; say that, and do not present it as the same thing as hidden encoding.
- Numbers read approximately from figures (R&G accuracies from Figure 1; Lanham per-task faithfulness lives in plots) must be stated as approximate, not precise.

Steelman first, attribute the worry to who holds it (the AI-control / CoT-monitorability researchers), test against what was shown, then name the gap in both directions (over-worry and dismissal). Work from the original documents. Name no company as an authority; record a lab statement as a stated position with its author. Link ../what-could-go-wrong/cot-monitorability.html and ../the-mechanics/thinking-out-loud.html rather than re-teaching them.

Habits not to inherit (from commission.md): find this piece's own dek (avoid the flat single-line-debunk shape now familiar in the desk); vary heading construction; no colon-subtitle headline; do not join the alarm or the dismissal.
