# editor review-brief: the-mechanics/false-confidence (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/commission.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/writer/01/brief.md — the exact writer brief (carries the two narrowings)
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/writing-coach/01/voice-guide.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/researcher/01/evidence.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/writer/01/draft-handoff.md
- Article: /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/library/the-mechanics/false-confidence.html
- Template context: /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/editor/01/editorial-review.md

Recent-pattern notes:
- Mechanics openers to break: leading with a big table of failing examples
  (getting-math-wrong, overused-words). Confirm this piece opens on one concrete
  example, not a specimen table.
- Paradox/twist closer tic to break: "the specific words are where the
  engineering runs out," "the sums it gets right are the least understood."
  Confirm the closer is in this lesson's nouns.
- Check the dek against the banned dek molds (spec/headlines.md).

Round focus — verify most skeptically:
- The two narrowings must hold in defensible form: (1) NOT "verbalized confidence
  carries zero information" — the claim is that the assertive tone / unsolicited
  "I'm 95% sure" is uninformative, while an explicitly elicited numeric confidence
  can be better calibrated (Tian et al., uneven across datasets). (2) NOT "the
  softmax is the only internal signal" — P(True)/P(IK) (Kadavath) and latent reps
  (Lin) exist. Confirm the draft states both narrowly.
- No fabricated GPT-4 ECE in prose. NOTE: the writer found the GPT-4 report's
  Figure 8 actually prints ECE annotations (0.007 pre-train, 0.074 post-trained),
  which the researcher's evidence record omitted; the writer kept prose
  qualitative and did not cite them without a researcher record. Your call: the
  piece is publishable as qualitative. If you judge the worked example needs those
  numbers, that is a researcher item (add them to the evidence record) then a
  writer item — do not have the writer assert them from the figure alone. Do not
  prolong the loop for this if the qualitative version teaches the point.
- Confirm hallucination (already published) is linked, not re-taught, and the
  spine stays on the confidence signal.
- Audit every data-nb-kind (7 primary + 1 secondary) and open every citation href.

You may edit prose/structure/furniture directly; route any broken central claim
or needed new evidence to writer/researcher. End with Decision: approve or revise.
