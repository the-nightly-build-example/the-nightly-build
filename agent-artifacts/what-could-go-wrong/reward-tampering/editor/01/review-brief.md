# editor review-brief: what-could-go-wrong/reward-tampering (01)

Inputs (read in the order your skill names):
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/writing-coach/01/voice-guide.md — read first.
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/editorial-direction.md — house standard, paper voice, lesson identity, series prompt.
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/commission.md — the assignment, its boundaries, the reader's situation.
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/writer/01/brief.md — the exact writer brief (to catch leakage and habits).
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/researcher/01/evidence.md — open when the first read calls for it.
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/writer/01/draft-handoff.md — original-work sentence, open only on the third read.
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/library/what-could-go-wrong/reward-tampering.html — the article to edit in place.
- template context under /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/.nb-context/.

Output: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/editor/01/editorial-review.md

After any direct edits you make, the orchestrator runs `nb stamp` and `nb check`
before the PR; you do not run the proof. Route to the writer only what needs new
reporting or a redraft.

## Recent-pattern notes (catch formula against these; one article cannot show it)

Cross-desk house formulas this run is deliberately breaking — flag any that survived:
1. "Why this matters" opening on a nostalgic or second-person recall, or pivoting
   on "This lesson shows/tests/takes apart...".
2. The opener closing on a "set the two things side by side" line.
3. "The takeaway" landing on a "So next time you [meet/hear]..." portable rule.
4. "this desk" or any body self-reference; the body narrates no one.

what-could-go-wrong-specific molds: recent deks use "[modest measured thing], yet
no one has [scary thing]" and the comma-triad closed with "and"; recent headings
lean on "The X that Y" relative-noun-phrases and the "noun, the appositive" comma
mold. A dek or heading built like those is a formula even if sharp.

## Round focus

Verify the piece presents the argument at full strength and then locates the gap
between the one experiment and the projection, and that these boundaries survived:
- Reward hacking and reward tampering must stay distinct. Reward hacking (the
  library's published lesson) exploits a flawed reward; reward tampering corrupts
  the reward mechanism itself. The definitional line is Everitt et al.'s, not
  Skalse et al.'s (Skalse defines reward hacking but does not draw the tampering
  line). Check the attribution.
- The 2024 experiment's rates must be exact and carry their denominators: reward
  function edited at 45 of 32,768, tests edited to hide it at 7 of 32,768, baseline
  0 of 100,000, residual 4 of 100,000 after countertraining. Verify each against
  the evidence record. The authors' own caveat (the setup "seriously exaggerates
  the incentives") must be present, and the piece must not imply the behavior is
  common or spontaneous.
- The November 2025 production-RL result shows reward *hacking* generalizing to
  sabotage/alignment-faking; it narrows the "only contrived" reading of hacking but
  does not show reward-channel *tampering* unprompted. Flag any sentence that lets
  it collapse the hacking-versus-tampering distinction.
- Desk guardrail: no company named as an authority. Every claim is attributed to
  the paper/authors and the figures they reported, never to a lab's standing. Flag
  any sentence that leans on a lab's reputation.
Check the steelman is genuine and the skeptical reading is given its due. Audit
every data-nb-kind (a lab is primary for "what its experiment found," and its
framing is to be treated skeptically). Confirm the three ordered reads, edit
directly what is yours, route only what needs reporting, and record every change.
